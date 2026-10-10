# 第一周购物测试 · DemoBlend One · 美国

**类型：** 封闭测试 · Meta 广告（Facebook / Instagram）  
**周期：** 2026-10-04 — 2026-10-10（7 天）  
**广告主：** **DemoBlend One** — **虚构 DTC 品牌**（台式搅拌机，规划客单价约 $89，落地页为练习设定，无真实店铺）  
**优化目标：** 购物（Purchase）  
**数据性质：** **方法论仿真** — 下表数字自洽，非广告后台导出；日后可换成脱敏真实 CSV，结构不变  

**附件：** [daily-account.csv](../../../daily-account.csv) · [adset-summary.csv](../../../adset-summary.csv) · [creative-summary.csv](../../../creative-summary.csv) · [账户结构](./assets/account-structure.md)  

**背景：** Hook 方向来自 [搅拌机品类竞品日志](../../appendix/competitive-log-blenders.md)；CPA 护栏对照 [家居品类公开基准](../../references/simulation-vs-benchmark.md)。虚实划分见 [中文 README](../../README.md#约定)。

---

## 摘要

第一周用约 **$418** 做 Purchase 探测：两个受众假设（**Broad 自动扩量** vs **Interest 做饭兴趣栈**），Broad 内两条视频（**结果向** vs **参数向**）。**Broad 在成本上胜出；Interest 触发关停规则。** 账户层面 **8 单 · CPA $52.29** 是「好广告组 + 差广告组」混合后的数——**不要用账户平均 CPA 决定加预算，要看每个广告组花够钱后的 CPA。**

**本周动作**

| 广告组 | 7日花费 | 订单 | CPA | 决策 |
|--------|---------|------|-----|------|
| Broad-US-25-54-ADV+ | $198.40 | 5 | **$39.68** | **加预算 20%** · 频次 2.1 正常 |
| Interest-Cooking-US | $156.20 | 2 | **$78.10** | **关停** · 超 kill 线 $82.5 且花费 > $40 |
| Interest-Cooking-STATIC-only | $63.72 | 1 | $63.72 | **关闭** · 随 Interest 栈一起停 |

**下一格（只改一个变量）：** 保留 Broad + 结果向胜出素材 · **仅新增 UGC-POV-v2** · 不改受众 · Brief 见 [此处](../../deliverables/creative-brief-example.md)。

---

## 测试设计（花钱前锁死）

| 项 | 选择 | 原因 |
|----|------|------|
| 规划客单价 | ~$89 | 小家电 DTC |
| 主 KPI | 购物 CPA | 销售战役，不是纯引流 |
| CPA 护栏 | **≤ $55** | 约为家居品类公开中位 × 1.2，留给 learning 波动 |
| 关停规则 | 某广告组 CPA **> $82.5** 且花费 **> $40** | 差组早停，少「再观察一天」 |
| 预算 | 账户约 $60/天 · 广告组上限 | 结构正常时，一周争取 5–8 单用于判断 |
| 变量顺序 | **先受众**（Broad vs Interest）· **再在 Broad 内比 Hook** | 同一周不要同时改受众和素材 |

**假设（测前写好）**

1. 同样「结果向」视频，Broad 的购物 CPA 不劣于 Interest 栈。  
2. 在 Broad 内，前 3 秒讲「30 秒做好」优于堆参数（同 offer、同落地页）。

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

[adset-summary.csv](../../../adset-summary.csv)

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

## 创意（仅 Broad 内公平对比）

[creative-summary.csv](../../../creative-summary.csv)

| 创意 | CTR | CPA | 结论 |
|------|-----|-----|------|
| VID-Outcome30s-v1 | 1.37% | **$37.43** | 主放量素材 |
| VID-SpecPower-v1 | 1.33% | $43.05 | 保留，非首要加码对象 |

Outcome 赢在 **CPA**，CTR 差距不大——厨房类 demo 常见。参数向不是「差」，是 **第二位**，等 UGC POV 测完再排。

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
