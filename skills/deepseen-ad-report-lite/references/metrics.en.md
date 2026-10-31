# Fields, arithmetic and scope

Python 3.10+, standard library; CSV UTF-8/GB18030 and XLSX, no executed formulas/macros. Provide headers and at least one raw metric. Export old XLS as CSV/XLSX. More than 5,000 rows or 10 MB is rejected rather than silently truncated; formula values need a numeric export.

| Field | English headers | Meaning |
|---|---|---|
| Creative | creative_id, creative, ad_id | Material identifier |
| Market | market, country, marketplace | Separate markets; missing stays unknown |
| Scope | currency, product_id, account_id, period, attribution_window, click_scope | Separate comparison groups |
| Spend | spend, cost | Advertising spend |
| Impressions/clicks | impressions, clicks, destination_clicks | Preserve click definition |
| Orders | orders, purchases | Purchase orders, not generic conversions |
| Click-attributed orders | click_attributed_orders | Numerator for click CVR |
| Ad revenue | ad_revenue, attributed_revenue | Confirmed ad-attributed revenue |

Generic revenue/sales is not used for ROAS until the user confirms attribution, using an explicit ad header or --revenue-scope ad-attributed. Never relabel store-wide or organic revenue through that flag.

CTR=clicks/impressions×100; click CVR=click-attributed orders/clicks×100; orders/clicks may include view-attributed orders and is not click CVR. CPC=spend/clicks; CPM=spend/impressions×1000; CPA=spend/orders; ROAS=ad-attributed revenue/spend, not net profit.

Recompute group ratios from raw totals, not average ratios. Missing fields are not zero; incomplete fields block affected aggregate ratios. Zero denominators stay unavailable. Targets are supplied by users, not industry profitability standards. A group median is a sample signal, not significance or a benchmark. Unknown markets are not inferred from currency/account names. Mixed currencies cannot share one target CPA.

Platform definitions depend on the actual export and current documentation: [TikTok basic metrics](https://ads.tiktok.com/help/article/basic-data?lang=en) and [TikTok Shop attribution](https://ads.tiktok.com/resources/help/article/about-tiktok-shop-ads-attribution?lang=en). Example windows do not establish current platform policy.
