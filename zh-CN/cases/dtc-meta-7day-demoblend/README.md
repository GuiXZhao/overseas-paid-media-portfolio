# 第一周购物测试 · DemoBlend One · 美国

**类型：** 封闭测试 · Meta 广告（Facebook / Instagram）  
**周期：** 2026-10-04 — 2026-10-10（7 天）  
**广告主：** **DemoBlend One** — **虚构 DTC 品牌**（台式搅拌机，规划客单价约 $89，落地页为练习设定，无真实店铺）  
**优化目标：** 购物（Purchase）  
**数据性质：** **方法论仿真** — 下表数字自洽，非广告后台导出；日后可换成脱敏真实 CSV，结构不变  

**附件：** [daily-account.csv](../../../daily-account.csv) · [adset-daily.csv](../../../adset-daily.csv) · [adset-summary.csv](../../../adset-summary.csv) · [creative-summary.csv](../../../creative-summary.csv) · [账户结构](./assets/account-structure.md)  

**背景：** Hook 方向来自 [搅拌机品类竞品日志](../../appendix/competitive-log-blenders.md)；CPA 护栏对照 [家居品类公开基准](../../references/simulation-vs-benchmark.md)。虚实划分见 [中文 README](../../README.md#约定)。

---

## 摘要

第一周约 **$418** Purchase 测试：**仅两个广告组对照** — **Broad 大范围** vs **Interest 烹饪兴趣**。Broad 内两条视频（结果向 vs 参数向）；Interest 上挂 Outcome + 静态，用于投出去并对照 **同一 Outcome 在 Broad / Interest 的 CPA 差**。**Broad 胜出；Interest 在 D5 触达关停规则后暂停，D6–D7 仅 Broad 花钱。**

**本周动作**

| 广告组 | 7日花费 | 订单 | CPA | 决策 |
|--------|---------|------|-----|------|
| Broad-US-25-54-ADV+ | $198.40 | 5 | **$39.68** | **加预算 20%**（自 D6）· 频次 2.1 |
| Interest-Cooking-US | $219.92 | 2 | **$109.96** | **关停** · D5 末触发规则；**D6–D7 花费 $0** |

**下一格（只改一个变量）：** 保留 Broad · **仅新增 UGC-POV-v2** · 不改受众 · Brief 见 [此处](../../deliverables/creative-brief-example.md)。

---

## 测试设计（花钱前锁死）

| 项 | 选择 | 原因 |
|----|------|------|
| 规划客单价 | ~$89 | 小家电 DTC |
| 主 KPI | 购物 CPA | 销售战役，不是纯引流 |
| CPA 护栏（加码参考） | **≤ $55** | 约为家居品类公开中位 × 1.2 |
| **关停规则** | 某广告组累计花费 **> $40** 且 CPA **> $82.5** | 单条规则；Interest 在 D5 末 CPA $109.96 触发，**D6 起暂停该组** |
| 预算 | 账户约 $60/天 · 广告组上限 | 一周争取 5–8 单用于判断 |
| 变量顺序 | **先受众**（Broad vs Interest）· **再在 Broad 内比两条视频** | 同一周不在 Interest 内做 Hook 矩阵 |

---

## 追踪（仿真设定）

Purchase：**Pixel + CAPI**，仿真中视为匹配良好。GA4 与 Meta 购物差 **11%** — 日常优化可接受；关账前再对财务口径。

UTM：`utm_source=facebook&utm_medium=paid&utm_campaign={campaign.name}`

结构：[account-structure.md](./assets/account-structure.md)

---

## 账户 · 按日

完整数据：[daily-account.csv](../../../daily-account.csv)  
**广告组按日（两组）：** [adset-daily.csv](../../../adset-daily.csv) — **D6、D7 的 Interest 行 spend_usd_day = 0**

| 日 | 花费 | 订单 | 当日 CPA | 操作备注 |
|----|------|------|----------|----------|
| D1 | $58.20 | 0 | — | 上线 · learning · 不动结构 |
| D2 | $62.40 | 1 | $62.40 | 首单 · 仍早 |
| D3 | $61.80 | 1 | $61.80 | 维持 |
| D4 | $60.50 | 2 | $30.25 | Interest CPA 走高 · 略减 Interest 日预算 |
| D5 | $59.10 | 3 | — | **触达 kill 规则 · 暂停 Interest** |
| D6 | $58.72 | 5 | — | **仅 Broad** · Broad 预算 +20% |
| D7 | $57.60 | 7 | — | 关账 |

账户 **7 单 · CPA $59.76** 是两组混合结果；**关停看广告组 CPA，别看账户平均。**

---

## 广告组复盘

累计：[adset-summary.csv](../../../adset-summary.csv)

### Broad-US-25-54-ADV+ — 加码

- CPA **$39.68**，花费与单量够做第一周判断。  
- D6 起加预算；D6–D7 账户花费即 Broad 花费。

### Interest-Cooking-US — 关停

- 组级 CPA **$109.96**（> **$82.5** 且花费 > **$40**）。  
- 同一 **Outcome30s**：Broad **$37.43** vs Interest **$98.50** → **受众不匹配**，不是视频单独失效。  
- **D5 末暂停后，D6–D7 不再消耗**（见 adset-daily）。

---

## 创意层说明

[creative-summary.csv](../../../creative-summary.csv) 共 **4 行**（Broad 2 + Interest 2）。**Week2 UGC-POV 只在 Broad 新增。**

### Broad 内对比

| 创意 | CTR | CPA | 结论 |
|------|-----|-----|------|
| VID-Outcome30s-v1 | 1.37% | **$37.43** | 主放量素材 |
| VID-SpecPower-v1 | 1.33% | $43.05 | 保留 |

---

## 与公开基准对照

| 指标 | 本测试（账户） | 外部参考 |
|------|----------------|----------|
| CPA | $59.76 | 家居品类中位约 **$46–49** |
| Broad 组 CPA | $39.68 | 接近中位 → 胜出组合理 |
| CTR | 1.20% | 新户小预算，第一周不必追全行业中位 |

详见 [simulation-vs-benchmark.md](../../references/simulation-vs-benchmark.md)。

---

## 第二周计划

1. **仅 Broad** · 维持 D6 的 +20% 方向。  
2. 上线 **UGC-POV-v2**。  
3. **不恢复 Interest**，除非 Broad 明显疲劳或 CPA 连续超护栏。  

---

## 数据声明

虚构商品 · 仿真数字 · 流程与 live 账户写法一致。

**相关：** [周报范例](../../deliverables/weekly-intel-memo.md) · [中文导航](../../README.md)
