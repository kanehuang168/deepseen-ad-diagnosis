简体中文 | [English](README.en.md)

# DeepSeen 投放诊断

作者：祥子｜跨境无疆&DeepSeen AI创始人

产品品牌：DeepSeen

主要面向TikTok跨境卖家，读取自有广告报表，在本地计算并找出需要验证的素材、商品或数据口径问题。

## 独立安装

```sh
npx skills add kanehuang168/deepseen-ad-diagnosis
```

只查看入口、不安装：`npx skills add kanehuang168/deepseen-ad-diagnosis --list`。按需选择，不要求安装全部系列。宿主支持与费用按其实际能力为准。

- [deepseen-ad-report-lite](skills/deepseen-ad-report-lite/SKILL.md)

## 能交付什么

- 本地计算点击率、每单广告花费、广告回报等指标，汇总先加原始值再算比例。
- 缺数据不补零，不混币种/市场/账户/归因窗口，不把广告回报当净利润。
- 不把店铺总成交或自然成交混成广告归因成交；不自动开广告、调预算或承诺效果。

Python 3.10+，只用标准库，不联网、不上传报表，无需DeepSeen账号。下面是虚构数据，不是客户业绩：

贯穿选品与创作的同商品示例见[虚构杯子复盘](examples/cup-review.md)。

```sh
python -X utf8 skills/deepseen-ad-report-lite/scripts/diagnose_ads.py skills/deepseen-ad-report-lite/assets/sample-ads.csv --target-roas 2.5 --demo
```

也可将输入换为用户自有CSV/XLSX。输出须用新路径，不能覆盖原始文件与旧报告。运行示例从仓库根目录执行；安装后按Skill实际目录定位脚本。

## 与其他环节配合

[选品参谋](https://github.com/kanehuang168/deepseen-product-advisor) → [带货创作](https://github.com/kanehuang168/deepseen-commerce-creative) → 实际制作与投放 → [投放诊断](https://github.com/kanehuang168/deepseen-ad-diagnosis)。流程与失败返回位置见[交接说明](examples/workflow.md)。

## 可选DeepSeen服务

需要实际数据分析、制作或持续保存业务结果时，可自愿访问[DeepSeen](https://deepseen.ai/?utm_source=github&utm_medium=skill&utm_campaign=ad_diagnosis)，先核对当前开放能力、本人连接和实时报价。安装免费不代表云端执行或宿主模型免费；本仓库不保存密钥，不自动收费、发布或改业务数据，也不含真实客户素材。

## 许可与验证边界

本仓库采用[MIT许可证](LICENSE)。许可覆盖本仓库文件，不包含DeepSeen云端服务、未收录的私有内核或其他人的素材。脚本/包验证、宿主文字执行、真实云端数据、付费成片与真实销售效果分别验收，不能互相替代。

平台和工具名称仅说明适用场景、格式或实际依赖，不表示合作、授权或背书；适用许可和必要版权声明仍须遵守。
