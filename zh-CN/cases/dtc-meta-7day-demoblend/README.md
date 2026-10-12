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

第一周用约 **$418** 做 Purchase 探测：**1 个 Broad 组 + 2 个 Interest 组**（主组混投视频/静态，附属组仅静态，见[账户结构](./assets/account-structure.md)）。Week1 **主线**是 Broad 栈 vs Interest 栈谁更划算；Broad 内再比两条视频（**结果向** vs **参数向**）。**Broad 胜出；Interest 栈关停。** 账户 **8 单 · CPA $52.29** 是好组+差组混合——**决策看各广告组累计 CPA，别看账户平均。**

**本周动作**

| 广告组 | 7日花费 | 订单 | CPA | 决策 |
|--------|---------|------|-----|------|
| Broad-US-25-54-ADV+ | $198.40 | 5 | **$39.68** | **加预算 20%** · 频次 2.1 正常 |
| Interest-Cooking-US | $156.20 | 2 | **$78.10** | **关停** · 花费 > $40 且 CPA ≥ Broad 的 1.95 倍（≈$77.4） |
| Interest-Cooking-STATIC-only | $63.72 | 1 | $63.72 | **关闭** · Interest 栈一并停投，不再加预算 |

**下一格（只改一个变量）：** 保留 Broad + 结果向胜出素材 · **仅新增 UGC-POV-v2** · 不改受众 · Brief 见 [此处](../../deliverables/creative-brief-example.md)。

---

## 测试设计（花钱前锁死）

| 项 | 选择 | 原因 |
|----|------|------|
| 规划客单价 | ~$89 | 小家电 DTC |
| 主 KPI | 购物 CPA | 销售战役，不是纯引流 |
| CPA 护栏 | **≤ $55** | 约为家居品类公开中位 × 1.2，留给 learning 波动 |
| 关停规则 | 花费 **> $40**，且（CPA **> $82.5** **或** CPA **≥ 当周最优广告组 CPA 的 1.95 倍**） | 差组早停；本案例 Interest 主组 $78.10 触发相对 Broad 规则 |
| 预算 | 账户约 $60/天 · 广告组上限 | 结构正常时，一周争取 5–8 单用于判断 |
| 变量顺序 | **先受众栈**（Broad vs Interest）· **再在 Broad 内比两条视频** | 同一周不在 Interest 内做创意大矩阵；Interest 上素材仅为「能投出去 + 对照同一视频在 Broad 的表现」 |

---

## 追踪（仿真设定）

Purchase：**Pixel + CAPI**，仿真中视为匹配良好。GA4 与 Meta 购物差 **11%** — 日常优化可接受；关账前再对财务口径。

UTM：`utm_source=facebook&utm_medium=paid&utm_campaign={campaign.name}`

结构：[account-structure.md](./assets/account-structure.md)

---

## 账户 · 按日

完整数据：[daily-account.csv](../../../daily-account.csv)

| 日 | 花费 | 订单 | 当日 CPA | 操作备注 |
|----|------|------|----------|----------|
| D1 | $58.20 | 0 | — | 上线 · learning · 不动结构 |
| D2 | $62.40 | 1 | $62.40 | 首单 · 仍早 |
| D3 | $61.80 | 1 | $61.80 | 维持 |
| D4 | $60.50 | 2 | $30.25 | Interest 拉高混合 CPA · Interest 日预算 −15% |
| D5 | $59.10 | 1 | $59.10 | Interest 累计超 kill 线 · **暂停 Interest 主组** |
| D6 | $58.72 | 2 | $29.36 | Broad 扛量 · **Broad 预算 +20%** |
| D7 | $57.60 | 1 | $57.60 | 关账 · 不开新测试 |

账户 CTR 约 **1.20%** 对冷启动 Purchase 可接受；**CTR 高不代表该加预算**，广告组 CPA 才是决策依据。

---

## 广告组复盘

累计决策：[adset-summary.csv](../../../adset-summary.csv) · **按日下钻（三组 7 天）：** [adset-daily.csv](../../../adset-daily.csv)（与账户按日 [daily-account.csv](../../../daily-account.csv) 加总一致）

### Broad-US-25-54-ADV+ — 加码

- CPA **$39.68**，花费 **$198**，单量够做第一周判断。  
- 频次 **2.1**，尚未明显疲劳，可先加预算再谈换素材。  
- D1–D3 未改目标/受众，D6 加码有依据。

### Interest-Cooking-US — 关停

- 同一支 **Outcome30s** 在 Interest **CPA $98.50**，在 Broad **$37.43** → **受众/市场匹配问题**，不是「视频废了」。  
- 应在差广告组里少换片、**先关组**。  
- 常见错：在输钱广告组里疯狂换创意，混淆原因。

### Interest-Cooking-STATIC-only — 关闭

- 附属栈，随 Interest 主组停，避免漏网花费。

---

## 创意层说明

[creative-summary.csv](../../../creative-summary.csv) 共 **5 行**：Broad 内 2 条视频做 **Hook 对比**；Interest 行用于证明 **同一 Outcome 视频在 Interest 上 CPA $98.5**，在 Broad 上 **$37.43**（受众问题）。**Week2 新增创意（UGC-POV）只在 Broad 上测**，不在本表 Week1 快照里。

### Broad 内对比（公平）

| 创意 | CTR | CPA | 结论 |
|------|-----|-----|------|
| VID-Outcome30s-v1 | 1.37% | **$37.43** | 主放量素材 |
| VID-SpecPower-v1 | 1.33% | $43.05 | 保留，非首要加码对象 |

Outcome 赢在 **CPA**；参数向为 **第二位**，等 UGC POV 测完再排。

---

## 与公开基准对照

| 指标 | 本测试（账户） | 外部参考 |
|------|----------------|----------|
| CPA | $52.29 | 家居品类中位约 **$46–49**（Triple Whale 等） |
| Broad 组 CPA | $39.68 | 接近中位 → 胜出组 **合理** |
| CTR | 1.20% | 全行业中位约 **2.4%** — 新户小预算，第一周不必追 median CTR |

详见 [simulation-vs-benchmark.md](../../references/simulation-vs-benchmark.md)。

---

## 第二周计划

1. **仅 Broad** · 维持 D6 的 +20% 方向。  
2. 上线 **UGC-POV-v2**（手持 POV · 同 offer · 落地页首屏仍「约 30 秒」）。  
3. **不恢复 Interest**，除非 Broad 频次 **> 2.8** 或 CPA 连续 3 天超护栏——再测也应换 **LAL 1% 购买人群** 等，而非原 Interest 栈。  
4. 每次加码前核对：广告里促销价 = 落地页首屏价。

---

## 数据声明

本报告展示 **虚构商品** 上 **第一周 Purchase 测试** 的写法：测前规则、按广告组决策、单变量队列。数字为 portfolio 仿真；流程与 live 账户一致。

**相关：** [周报范例](../../deliverables/weekly-intel-memo.md) · [中文导航](../../README.md)
