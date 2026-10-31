# 虚构杯子投放复盘

这是人为编造的报表，用于演示计算和交接，不能证明商品卖得动、视频投放有效或模型生成质量。

从仓库根目录实际运行：

```sh
python -X utf8 skills/deepseen-ad-report-lite/scripts/diagnose_ads.py skills/deepseen-ad-report-lite/assets/cup-ads.csv --target-roas 2.5 --demo
```

同一虚构商品DEMO-CUP-001、同一账户/统计期/币种/归因窗口下，示例消耗360美元、广告归因成交金额450美元，汇总广告回报1.25；不是三行回报的简单平均，也不是净利润。目标2.5仅为演示参数，不是行业基准。

素材A回报3.0、素材B回报0.5、素材C有消耗无订单。可以优先核对B/C的展示内容、落地承接与归因，不能仅凭这些数字断定导演脚本导致失败，也不自动调预算。若要回到商品验证，补充真实成本、商品评价或履约证据；若要回到导演，给实际素材和问题位置。店铺总成交和自然流量另算。

本例数据来源与[选品参谋的虚构杯子](https://github.com/kanehuang168/deepseen-product-advisor/blob/main/skills/deepseen-product-advisor-lite/assets/cup-brief.md)一样均为人为设定，不是同一批真实用户行为。
