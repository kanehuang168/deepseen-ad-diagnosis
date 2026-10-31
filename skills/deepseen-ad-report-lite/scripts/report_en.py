"""English presentation only; arithmetic and source values are not changed."""
import copy
import re

LABELS={'消耗':'Spend','成交金额':'Revenue','展示次数':'Impressions','点击次数':'Clicks','订单数':'Orders','点击归因订单数':'Click-attributed orders'}

def diagnostic(text):
    exact={
        '部分市场、币种、商品、账户、统计期、归因窗口或点击口径未注明；分组相同不证明原始口径相同。':'Some market/currency/product/account/period/attribution/click definitions are unspecified; a shared group does not establish comparable source scope.',
        '成交金额或销售额未明确属于广告归因，未用于广告回报计算；店铺总成交和自然成交不能代入。请核实后使用明确列名，或显式提供--revenue-scope ad-attributed。':'Generic revenue is not confirmed as ad-attributed and is excluded from ROAS. Store-wide and organic sales must not be substituted. After verification use an explicit ad-revenue header or --revenue-scope ad-attributed.',
        '输出不能覆盖原报表。':'Output must not overwrite the source report.',
        '输出文件已存在，请使用新文件名以保留历史报告。':'Output already exists; use a new path to preserve history.',
        'Markdown与JSON输出路径不能相同。':'Markdown and JSON outputs must have distinct paths.',
        '目标必须是大于0的有限数值。':'The target must be a finite number greater than zero.',
        '文件超过10MB，请只导出本次分析所需字段。':'The input exceeds 10 MB; export only the required fields.',
        '工作簿展开后过大，请导出所需工作表为CSV。':'The expanded workbook is too large; export the required sheet as CSV.',
        '不读取外部工作表链接，请导出为本地CSV。':'External worksheet links are not read; export a local CSV.',
        '工作表路径无效。':'Invalid worksheet path.',
        '工作表缺少单元格坐标。':'A worksheet cell is missing its coordinates.',
        '报表列数超过200，请只导出所需字段。':'The report exceeds 200 columns; export the required fields.',
        '明细超过5000行，请分批导出；本次未截断分析。':'The input exceeds 5,000 rows; split the export. No truncated analysis was performed.',
        '仅支持CSV或XLSX；请将旧格式导出为CSV/XLSX。':'Only CSV and XLSX are supported; export older formats accordingly.',
        '请提供表头及至少一行实际数据。':'Provide headers and at least one actual data row.',
        '未识别到原始指标。请至少提供消耗、展示次数、点击次数、订单数或成交金额一列。':'No raw metric was recognized. Provide spend, impressions, clicks, orders or confirmed attributed revenue.',
        '没有可分析的明细数据，合计行不能替代素材明细。':'No analyzable detail rows; total rows cannot replace creative-level data.',
        '文件包含多种币种，不能套用同一个目标每单花费；请分币种分析。':'Multiple currencies cannot share one target CPA; analyze them separately.',
    }
    if text in exact:return exact[text]
    if text.startswith('找不到指定工作表：'):return 'Worksheet not found: '+text.split('：',1)[1]
    if text.startswith('未提供字段：'):
        fields=text.split('：',1)[1].split('；',1)[0]
        return 'Missing fields: '+', '.join(LABELS.get(x,x) for x in fields.split('、'))+'. Affected calculations are unavailable, not zero.'
    m=re.match(r'数据行(\d+)的(.+?)为公式',text)
    if m:return f'Row {m[1]}, {LABELS.get(m[2],m[2])}: formula values are not executed or taken from stale caches; export numeric values.'
    m=re.match(r'数据行(\d+)的(.+?)不是',text)
    if m:return f'Row {m[1]}, {LABELS.get(m[2],m[2])}: invalid nonnegative finite value (zero or magnitude 10^-12 to 10^18; counts must be integers); not treated as zero.'
    m=re.match(r'忽略(\d+)行(完全重复|合计)记录',text)
    if m:return f'Ignored {m[1]} '+('exact duplicate rows' if m[2]=='完全重复' else 'total rows')+' to avoid double counting.'
    m=re.match(r'多个列对应同一字段“(.+?)”',text)
    if m:return f'Multiple columns map to {m[1]}; confirm which scope to retain.'
    m=re.match(r'识别字段“(.+?)”存在多列，使用“(.+?)”',text)
    if m:return f'Multiple columns map to {m[1]}; using source column "{m[2]}". Other matching columns are not used.'
    return 'Analysis could not be completed. Check input format, field definitions, numeric values and file accessibility. ('+type(text).__name__+')'

def number(value):
    if value is None:return 'Not calculated'
    if isinstance(value,(int,float)):return str(value)
    return format(value,'.4f').rstrip('0').rstrip('.')

def localized_report(report):
    r=copy.deepcopy(report);r['execution']='Local calculation; DeepSeen was not called'
    r['data_kind']='Fictional example' if report.get('data_kind')=='虚构示例' else 'User-provided data'
    r['warnings']=[diagnostic(x) for x in report['warnings']]
    actions={
      'spend_without_orders':('Spend with zero recorded orders.','Verify purchase reporting and attribution, then product/page/checkout; this does not prove the creative failed.'),
      'below_target_roas':('ROAS below the supplied target.','Compare click and order evidence and test one hypothesis. Missing cost evidence prevents a net-loss conclusion.'),
      'above_target_cpa':('CPA above the supplied target.','Verify purchase events and currency, then inspect conversion steps. Do not change the ad account automatically.'),
      'below_sample_median':('ROAS below this comparison group median.','A within-sample prioritization signal, not an industry benchmark or statistically significant result.'),
      'one_order':('Only one recorded order.','Recheck performance; one order is not a stable scaling basis.'),
    }
    for g in r['groups']:
        g['scope']={k:('Not specified' if v=='未注明' else v) for k,v in g['scope'].items()}
        for row in g['rows']:
            for f in row['findings']:f['observation'],f['action']=actions[f['code']]
    return r

def render(report,safe):
    r=localized_report(report)
    lines=['# Ad report analysis','',r['execution']+'. No advertising settings were changed.','']
    if r['data_kind']=='Fictional example':lines+=['**Fictional sample, not real advertising performance.**','']
    lines+=[f"Sheet: {safe(r['sheet'])}; {r['row_count']} detail rows; {len(r['groups'])} comparison groups.",'ROAS is attributed revenue divided by spend, not net profit. Missing data is not zero.','',f"Targets: ROAS {number(r['targets']['roas'])}; CPA {number(r['targets']['cpa'])}."]
    labels={'spend':'Spend','revenue':'Attributed revenue','impressions':'Impressions','clicks':'Clicks','orders':'Orders','click_orders':'Click-attributed orders'}
    for i,g in enumerate(r['groups'],1):
        lines+=['',f'## Scope {i}','', '; '.join(f'{k}: {safe(v)}' for k,v in g['scope'].items()),'','| Metric | Known total | Rows with data / total |','|---|---:|---:|']
        for k,label in labels.items():lines.append(f"| {label} | {number(g['known_totals'][k]) if g['coverage'][k] else 'Not provided'} | {g['coverage'][k]}/{g['row_count']} |")
        lines+=['',f"Aggregate ROAS: {number(g['metrics']['roas'])}; CTR: {number(g['metrics']['ctr'])}%.",'','| Creative | Spend | Clicks | Orders | Revenue | CTR% | Orders/clicks% | Click CVR% | CPA | ROAS |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
        for row in g['rows']:
            creative=re.sub(r'^数据行(\d+)$',r'Data row \1',row['creative'])
            values=[safe(creative)]+[number(row[k]) for k in ('spend','clicks','orders','revenue')]+[number(row['metrics'][k]) for k in ('ctr','orders_per_click','click_cvr','cpa','roas')]
            lines.append('| '+' | '.join(values)+' |')
        lines+=['','### Checks']
        for row in g['rows']:
            for f in row['findings']:lines.append(f"- {safe(row['creative'])}: {f['observation']} {f['action']}")
    lines+=['','## Scope and evidence gaps','']+['- '+safe(x) for x in r['warnings']]
    lines+=['','- Recompute ratios from raw totals, not averages. Missing or zero-denominator ratios remain unavailable.','- Click CVR uses click-attributed orders; all orders/clicks may include view attribution.','- Observations and hypotheses do not establish causation. Attribution may still be incomplete.','','## Formulas','','CTR=clicks/impressions*100; click CVR=click-attributed orders/clicks*100; orders/clicks=all orders/clicks*100; CPC=spend/clicks; CPM=spend/impressions*1000; CPA=spend/orders; ROAS=ad-attributed revenue/spend.']
    return '\n'.join(lines)
