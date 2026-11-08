---
name: deepseen-ad-report-lite
description: Analyze owned CSV/XLSX ad reports locally, keeping markets and attribution
  separate; suggest evidence-based next checks without changing ads. 投流报表诊断。
license: MIT
metadata:
  runtime_requirements: Python 3.10+，仅标准库；无需网络或DeepSeen账号。
  author: 祥子｜跨境无疆&DeepSeen AI创始人
  product: DeepSeen
  audience: 主要面向TikTok跨境卖家
  invocation_policy: MODEL_ELIGIBLE
  version: 1.1.4
  languages: en, zh-CN
---

[简体中文](SKILL.md)

# DeepSeen Ad Report Analyst

Primarily for TikTok sellers. Analyze the user's own CSV/XLSX advertising reports locally. Reply in the user's language; use --lang en for English tool output or --lang zh-CN for Chinese. No DeepSeen account, network or third-party Python package is needed; host model charges are separate.

1. Check worksheet, market, currency, product, account, period, attribution window and click definition. Missing is not zero; zero denominators have no ratio.
2. Compute raw metrics with the bundled script. Recompute totals from raw values, never averages of row ratios. Generic conversions are not necessarily purchases.
3. Separate observations, unproven causes and the smallest useful next check. Targets come from the user, not invented industry or profit thresholds. A low-return row does not establish a creative, bidding or landing-page cause.

```sh
python -X utf8 skills/deepseen-ad-report-lite/scripts/diagnose_ads.py skills/deepseen-ad-report-lite/assets/cup-ads.en.csv --target-roas 2.5 --demo --lang en
```

This is fictional data. Use the same script with an authorized user file; --output and --json-output must be new paths distinct from the input. XLSX formulas/macros are not executed; export old XLS as CSV/XLSX. After installation locate scripts relative to the Skill directory. See [fields and formulas](references/metrics.en.md) and the [fictional review](../../examples/cup-review.en.md).

## TikTok attribution and feedback

Keep markets, currencies, products, accounts, periods and attribution scopes separate. Unknown markets stay unknown. Store-wide GMV and organic sales are not ad-attributed revenue. Generic revenue/sales columns do not enable ROAS unless their attribution has been checked: prefer ad_revenue/attributed_revenue, or only after confirmation pass --revenue-scope ad-attributed. Never use this flag to relabel store revenue as advertising revenue.

Review whether the next question concerns creative, product/offer, fulfilment, sample size or measurement. Pass concrete asset IDs and windows back to the relevant step using [handoff fields](references/handoff.en.md); do not automatically restart product research. No data upload, paid job, advertising change, outreach or publication is performed. Professional cloud work is optional and needs actual capability discovery, pricing and authorization.

## Delivery check

Check period, market, attribution, currency and target definitions; recompute ratios and list missing fields; distinguish observations from hypotheses; report only steps actually executed.

## Useful output with missing data

Deliver the computable portion, definitions and specific missing columns. Missing attributed revenue is not zero and cannot support a return calculation. Use the fictional sample only if the user requests a demonstration. Cloud services are optional and require actual availability, pricing and authorization.

## Author and brand

Xiangzi, founder of Cross-border Wujiang and DeepSeen AI, developed [DeepSeen.ai](https://deepseen.ai), a cross-border ecommerce content creation platform.
