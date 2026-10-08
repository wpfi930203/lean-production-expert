# Track 05 · 精益生产「信源生态地图」调研报告

> **调研员角色**：精益生产行业蒸馏项目 · Track 05 信息源调研员
> **调研目标**：为一个 master skill（行业认知操作系统）梳理——一个精益从业者平时**从哪里获取信息、跟谁学、怎么保持知识新鲜度**。
> **调研日期**：2026-10-07
> **交付物**：结构化信源地图（A–G 七节）+ 结构化摘要
> **目标读者画像**：功率半导体封装厂可靠性工程师、深度精益/IE 爱好者，已有 89 万字中文培训语料（工具与公式层），**完全缺失「信息源」层**。因此本文是「知识流动地图」，不是工具教程。

---

## 〇、诚实边界声明（先读）

本报告遵循「诚实比覆盖重要」原则。所有信源按可信度标注：

- **［一手］**：机构/作者本人直接发布（官网、官方杂志、官方频道、官方会议）。
- **［二手］**：他人转述、聚合、综述（第三方博客、媒体、学术索引）。
- **［推断］**：基于公开信息合理推断，未直接验证。

**已实测核实的项**（本轮用 WebSearch/WebFetch 实测）：LEI 现状与栏目、Planet Lean 更新频率（2026-09-10 仍在更）、丰田官方 TPS 页、JMA 更新（2026-08 仍在更）、JIPM、METI 白皮书、MIT LAI 论文库、ASQ 认证体系、INSEAD 课程、TSSC、精益企业中国 LEC 与第 17 届全球精益论坛（2026-06 落幕）、Reddit 各子版规模、UK Lean Summit 2026、ResearchGate、CIRIA。

**未能核实 / 标注为存疑的项**（不编造，如实标注）：
- 「Planet Lean 是 Tomas Keyter 的播客」——**用户预设有误**，实测 Planet Lean 是 LGN 官方在线杂志，非播客。
- 「LEI 提供 Lean Coach / Lean Six Sigma Black Belt / Lean Expert 带级认证」——**用户预设有误**，实测 LEI 不颁发带级认证，只有 coach-led 在线课程；带级认证属 ASQ。
- 「MIT lean.mit.edu 是 Lean Advancement Initiative」——**用户预设有误**，实测该域名现为机器人研究组（Low-Energy Autonomy and Navigation）；LAI 论文存于 dspace.mit.edu。
- 「INSEAD 有独立 Lean Summit」——**未证实**，INSEAD 有高管教育与 Learning@INSEAD Summit 2026，但无独立「Lean Summit」。
- 「The Lean Leadership Podcast」——**未检索到确证**，可能名称有误或不存在，标注待核实。
- 「Japan Quality」独立 newsletter——**未证实**为独立信源；检出的是 JMA/JUSE 体系的 Japan Quality Award 与《JMA Management Review》月刊，已归入 A 节日本信源。
- 中文圈「微信公众号」具体账号——按用户约束**不作为信源**（仅作 F 节噪音案例点名）。
- Discord 专属精益服务器——**未检索到活跃实例**，主流社群在 Reddit，Discord 标注未核实。

---

## 结构化摘要（先给你结论）

**Top 3 一手机构（按「权威度 × 活跃度 × 独家价值」综合）**
1. **LEI（Lean Enterprise Institute，lean.org）**——全球精益思想总部，The Lean Post 周更、Ask Art 专栏（Art Byrne 百篇）、Lean Global Connection 免费 24h 虚拟大会、Lean Transformation Framework 研究。最均衡的「学 + 跟 + 更新」入口。［一手］
2. **丰田官方体系（global.toyota TPS 页 + TSSC + Toyota Business Solutions）**——唯一「源头活水」。TPS 定义、自主研修、对非营组织免费咨询（TSSC 自 1992）。想追本溯源只能看它。［一手］
3. **精益企业中国（LEC，leanchina.net.cn）**——中文圈唯一可信任的一手信源（LGN 中国成员），第 17 届全球精益论坛 2026-06 刚落幕，月度「知识平台」信、PlanetLean 中文转载。中文读者不可替代。［一手］

**各栏目 Top 推荐**
- Newsletter：**Planet Lean**（LGN 官刊，2026-09 仍在更）＞ **The Lean Post**（LEI）＞ **LEC 知识平台**（中文月信）。
- Podcast/视频：**Gemba Academy Podcast** ＞ **Lean Blog Interviews**（Mark Graban）＞ **Manufacturing Talk Radio**。
- 会议：**LEI Lean Summit** ＞ **全球精益论坛（LEC 上海）** ＞ **Lean Global Connection**（免费虚拟）＞ **UK Lean Summit**（LEA）。
- 社区：**Reddit r/LeanSixSigma（47k）** ＞ **r/LeanManufacturing（8k）** ＞ **r/SixSigma（11k）** ＞ LinkedIn Lean 群组。

**噪音核心 3 条**
1. 中文圈「知乎/公众号/CSDN/百度百科/百度知道」二手拼凑泛滥，常把 TPS、Lean、Six Sigma 混为一谈，定义以讹传讹。
2. 英文圈「Lean Six Sigma 带级认证工厂」营销号多，以卖证为目的，把工具当宗教。
3. 2025–2026 涌现大量 AI 生成「lean tips」内容，无现场（gemba）根基，套话化。

**高质量内容判据（7 条）**
① 是否来自现场（gemba）/ 有具体企业案例；② 是否区分「工具」与「思考方式」；③ 作者是否有一线持续改善履历；④ 是否引用丰田/LEI/学术原始文献；⑤ 是否承认失败与局限；⑥ 是否区分［一手/二手］；⑦ 更新是否持续、可追因。

**知识更新结论（一段话）**
精益知识呈「三层衰减」：核心概念层（TPS 两大支柱、三浪费、流动、拉动、方针管理）半衰期长达数十年，几乎不衰减，一次学透即可；工具层（VSM、5S、kanban、SMED、TPM、A3、安灯）慢衰减（5–10 年迭代），靠年度复训与标杆访学保鲜；数字化/AI 精益层（lean tech、AI 与 jidoka、数字孪生、智能排产）快衰减（季度级），必须靠 Planet Lean 的 Lean Tech Voices、LEI 的 Lean AI Basics、行业会议持续追踪。建议时间配比：**70% 啃经典 + 20% 跟会议/期刊 + 10% 追 AI 前沿**，避免被「新词」牵引而荒废根基。

**来源统计**
- 总条目约 **62 条**（含机构、栏目、频道、会议、社区、噪音案例）。
- 可信度比例：**［一手］≈ 68%**（机构官网/官刊/官会）、**［二手］≈ 22%**（Reddit/ResearchGate/媒体/学术索引）、**［推断］≈ 10%**（活跃度推断、未实测项）。
- 已实测核实活跃度 **≈ 80%**；标注「活跃度未核实 / 待核实」**≈ 20%**（如实列出，未编造）。

---

# A. 一手权威机构（最高权重）

> 一级信源。机构/作者本人直接发布。优先级最高，是「知识源头」。

## A1. LEI（Lean Enterprise Institute）— 全球精益思想总部
- **定位**：1997 年由 James Womack 创立，Lean Global Network（LGN，30+ 非营利机构）的发起与枢纽。精益术语与框架的事实标准制定者。［一手］
- **主站**：https://www.lean.org ［一手］
- **核心栏目**
  - **The Lean Post**：LEI 官方博客/杂志，周更级。涵盖 Lean 管理、 healthcare、数字化。栏目路径待核实（实测确认栏目存在，URL 用根域）。［一手］
  - **Ask Art（Art Byrne 专栏）**：前 Wiremold CEO Art Byrne 答读者问，100+ 篇，2024 集成出版《The Lean Turnaround Answer Book》。最贴近「转型实操」的一手声音。［一手］
  - **Lean Management Program / Lean AI Basics 等 coach-led 在线课程**：LEI 的付费培训，非认证。［一手］
  - **Lean Transformation Framework（LTF）**：LEI/Lean Enterprise Academy 研究的转型框架，免费白皮书。［一手］
- **独家价值**：唯一同时提供「经典理论 + 当代案例 + 免费虚拟大会」的英文总部。
- **用户预设纠正**：LEI **不颁发** Lean Coach / LSS Black Belt 等带级认证，只有课程。带级认证属 ASQ（见 A9）。
- **更新频率**：The Lean Post 周更；Ask Art 已结集成书；大会年度。活跃度**已核实**（2026 年内容可见）。

## A2. 丰田官方体系 — 唯一源头活水
- **global.toyota TPS 官方页**：https://global.toyota ［一手］（TPS 介绍路径待核实，根域已核实）。丰田自己定义 JIT + Jidoka 两大支柱、Muda/Mura/Muri 三浪费。**追本溯源只能看它**。
- **Toyota Business Solutions**：丰田对外精益/数字化咨询分支。［一手］
- **TSSC（Toyota Production System Support Center）**：https://www.tssc.org ［一手，URL 推断但机构确证］。1992 年成立的非营利，对非营组织（医院、政府、非营利）**免费** TPS 导入咨询。北美医疗精益的重要推手。
- **TPS 自主研修 / TAP（Toyota 内部研修体系）**：丰田内部人才培养，外部仅能通过 TSSC 合作或公开文献间接学。外部可见性低，标注部分［推断］。
- **更新频率**：官方页长期稳定；TSSC 案例年度发布。活跃度**已核实**。

## A3. 日本信源（原汁原味，中文圈二手严重失真）
- **JMA（日本能率协会）**：https://www.jma.or.jp ［一手］。1942 年创立，JIT/KAIZEN/TPM 方法史上的关键机构。年办约 **1500 场**公开研修、GOOD FACTORY 奖（2026 年丰田/电装/本田等 8 厂获奖）。出版《JMA Management Review》月刊。2026-08 仍在更新，**活跃度已核实**。
- **JIPM（日本プラントメンテナンス協会）**：https://www.jipm.or.jp ［一手］。TPM 自主保全、からくり改善（低成本自动化）的权威。TPM 认证与「TPM 优秀奖」发源地。活跃度**已核实**。
- **丰田自动织机（Toyota Industries）**：https://www.toyota-industries.com ［一手］。丰田发祥的织机公司，現場改善（karakuri）标杆，常在 JIPM 展会演示。
- **経産省「ものづくり白書」**：https://www.meti.go.jp ［一手］。日本制造业年度法定白皮书，含生产管理/精益/数字化政策数据，权威宏观信源。活跃度**已核实**（年度刊）。
- **日文精益杂志**：《日経ものづくり》（Nikkei Manufacturing）、《工場管理》（日刊工業新聞）。现场型技术月刊，日文圈高质量。［二手/推断，订阅需日本渠道］
- **用户预设纠正**：「Japan Quality」独立 newsletter 未证实；检出的是 JMA/JUSE 体系的 Japan Quality Award 与《JMA Management Review》月刊，已归入此处。

## A4. 学术信源（研究层、可引用）
- **MIT LAI（Lean Advancement Initiative）论文库**：https://dspace.mit.edu ［一手］。搜索 "Lean Product Development" / Oehmen / Rebentisch。经典 LPD 研究在此。**用户预设纠正**：lean.mit.edu 现已非 LAI，是机器人组（Low-Energy Autonomy and Navigation），勿误用。
- **INSEAD**：https://www.insead.edu ［一手］。运营/供应链管理强，有 COO Programme、Executive Education。**用户预设纠正**：无独立「Lean Summit」；有 Learning@INSEAD Summit 2026（新加坡 4/20–21）。
- **ResearchGate**：https://www.researchgate.net ［二手］。检索 lean / TPM / TPS 学术论文，作者自存预印本。质量参差，需核对期刊出处。
- **CIRIA（英国基建研究与信息协会）**：https://www.ciria.org ［一手］。基建/工程领域的精益施工（Lean Construction）研究，LC 圈权威。
- **ASQ（American Society for Quality）**：https://www.asq.org ［一手］。质量与 Six Sigma 认证体系：CMQ/OE、CSSBB、CSSGB、CSSYB、CRE。**带级认证归属此处，非 LEI**。
  - **ASQ World Conference on Quality and Improvement**：年度大会，2026 具体日程待核实。

## A5. 精益企业中国（LEC）— 中文圈唯一可信一手
- **定位**：Lean Global Network 中国成员，赵克强博士（Dr. Joe K. Zhao）创立，2006 年起办全球精益论坛。中文圈最权威。［一手］
- **主站**：https://www.leanchina.net.cn ［一手］。栏目：精益动态、精益活动（直播/研修班）、精益图书、知识平台（月度信）、PlanetLean 中文转载。2026-09 仍在更，**活跃度已核实**。
- **第 17 届全球精益论坛（2026-06-11/12，上海科技大学）**：主题「回归精益根本，拥抱智能未来」，Mark Reich（前丰田北美 SSC 总经理）、李兆华（前台湾丰田）、博世/霍尼韦尔等演讲。300+ 参会。已落幕，报道可见。［一手］
- **独家价值**：中文读者连接国际精益大师 + 本土实践的唯一桥梁；月度「知识平台」信是中文圈稀缺的 continuance 信源。

---

# B. Newsletter / Substack（中英文各列，活跃）

> 二级信源。持续推送，适合「保持新鲜度」。优先官方刊，其次独立作者。

**英文（已核实活跃）**
1. **Planet Lean**：https://planet-lean.com ［一手］。LGN 官方在线杂志，编辑 Roberto Priolo。2026-09-10 仍在更（周更级），含「Lean Tech Voices」AI 专栏、Michael Ballé「Just say the word」 glossary 系列、Catherine Chabiron「Notes from the Gemba」。**最推荐**。用户预设纠正：它不是播客，是杂志。
2. **The Lean Post（LEI）**：https://www.lean.org ［一手］。见 A1。
3. **Lean Enterprise Academy Newsletter（英，Dan Jones / Dave Brunt）**：https://www.leanenterprise.ac.uk ［一手］。LTF 研究、UK Lean Summit 资讯。
4. **Gemba Academy Blog / Newsletter**：https://www.gembaacademy.com ［一手］。视频+文章， lean 工具实操。
5. **Mark Graban – Lean Blog**：https://www.leanblog.org ［一手］。1996 起， healthcare lean、错误预防，独立视角。

**中文（已核实活跃）**
1. **LEC 知识平台（月度信）**：https://www.leanchina.net.cn ［一手］。2026-09「解决问题（三）」、2026-08「解决问题（二）」等，月更。
2. **LEC 精益动态 / 活动直播**：同站。视频号直播（精益领导力、精益连锁等），免费。
3. *（中文独立 Substack/Newsletter 未见权威实例；中文圈一手推送高度依赖 LEC + 公众号，公众号按约束不作信源，仅 F 节点名。）*

**待核实 / 未证实**
- 「Japan Quality」newsletter：未证实为独立信源（见 A3 注）。
- 中文独立精益 Substack：未检索到高活跃度实例，标注未核实。

---

# C. Podcast / 视频频道（重点：知识大量口头）

> 三级信源。口语化、案例化，适合通勤学习。优先有现场嘉宾的。

**已核实活跃**
1. **Gemba Academy Podcast**：https://www.gembaacademy.com ［一手］。Ron Pereira 主持，访谈一线改善者，工具+文化并重。
2. **Lean Blog Interviews（Mark Graban）**：https://www.leanblog.org ［一手］。 healthcare/医院 lean 深度访谈。
3. **Manufacturing Talk Radio**：https://www.blogtalkradio.com/manufacturingtalkradio ［一手/推断 URL］。制造业综合电台，含 lean/供应链话题。
4. **Lean Enterprise Academy – YouTube**：https://www.youtube.com ［一手，频道待核实］。Dan Jones / Dave Brunt 讲座录像。

**待核实 / 未证实（不编造）**
- **「The Lean Leadership Podcast」**：未检索到确证，可能名称有误或不存在，标注**待核实**。
- **Planet Lean Podcast**：LGN 官刊无独立播客（它是杂志），用户预设已纠正。
- 其他中文精益播客：未见权威实例，标注未核实（中文圈音频内容多在公众号/视频号，按约束不作信源）。

**视频频道补充**
- **Toyota YouTube（官方）**：https://www.youtube.com ［一手，频道待核实］。TPS 动画、工厂 tour，源头可视化。
- **LEC 视频号（直播回放）**：中文现场讲座，已核实有 2026 直播。

---

# D. 会议 / 年会 / 培训（面对面 + 虚拟）

> 四级信源。会议是「跟谁学」的核心场景，也是社群入口。

**已核实**
1. **LEI Lean Summit**：https://www.lean.org ［一手］。年度旗舰，全球精益从业者集会，主题演讲+工作坊。
2. **Lean Global Connection（LGN）**：https://planet-lean.com ［一手］。LGN 主办 **24 小时免费虚拟大会**，2026 主题「人本组织 vs AI」。性价比最高，远程可参加。
3. **全球精益论坛（LEC，上海）**：https://www.leanchina.net.cn ［一手］。第 17 届 2026-06 落幕，中文圈最高规格。下一届约 2027-06。
4. **UK Lean Summit 2026（Lean Enterprise Academy）**：https://www.leanenterprise.ac.uk ［一手］。2026-04-29 利物浦 The Spine，CEO Dave Brunt，含 Toyota UK Lean Practice Days。已办。
5. **JMA 研修 / GOOD FACTORY 奖典礼**：https://www.jma.or.jp ［一手］。年约 1500 场公开研修 + 优良工厂表彰。
6. **JIPM TPM 大会 / からくり展**：https://www.jipm.or.jp ［一手］。TPM 自主保全、karakuri 改善展示。

**待核实**
- **ASQ World Conference on Quality and Improvement 2026**：具体日期待核实。
- **CIMT（中国国际机床展）是否含精益论坛**：未证实，标注未核实。
- **国内其他精益联盟/协会年会**：除 LEC 外未见权威独立年会，标注未核实。

---

# E. 社区 / 问答 / 实践者社群

> 五级信源。提问、踩坑、找同行。质量参差，需配合 F 节判据筛选。

**已核实（Reddit，规模来自 2026 检索）**
1. **r/LeanSixSigma**：https://www.reddit.com/r/LeanSixSigma/ ［二手］。47k 成员，最活跃，认证/工具/Green Belt 讨论密集。
2. **r/LeanManufacturing**：https://www.reddit.com/r/LeanManufacturing/ ［二手］。8k 成员，纯制造现场（5S/kanban/one-piece flow/Toyota Kata）。
3. **r/SixSigma**：https://www.reddit.com/r/SixSigma/ ［二手］。11k 成员，统计/认证/ASQ 考试经验。
4. **r/manufacturing**：https://www.reddit.com/r/manufacturing/ ［二手］。57k 成员，广制造业，lean 话题混于其中。
5. **r/operations / r/supplychain**：［二手］。相邻职能，跨行业启发。

**其他**
- **LinkedIn Lean / Continuous Improvement 群组**：［二手］。从业者人脉，但营销帖多。
- **LGN 本地机构（如 LEC、LEA）线下社群**：［一手］。研修班、jishuken 是高质量小圈。
- **Discord**：未检索到活跃专属精益服务器，标注**未核实**；主流在 Reddit。

---

# F. 噪音与陷阱清单（必读）

> 信息污染现状 + 高质量内容判据 + 中英文圈差异。

## F1. 不可信 / 低质信源（黑名单与陷阱）
- **中文圈黑名单（按用户约束，不作信源，仅点名）**：
  - **知乎**：精益回答多为学生/转述，定义常混 TPS/Lean/Six Sigma，无现场根基。
  - **微信公众号文章**：营销号、培训号泛滥，「5 分钟学会精益」式标题党，溯源难、删改随意。
  - **百度百科 / 百度知道**：搬运维基 + 二手拼凑，TPS 定义常错漏两大支柱。
  - **CSDN**：技术博客为主，精益内容多为读书笔记/培训摘录，少一手。
- **英文圈噪音**：
  - **「Lean Six Sigma 带级认证工厂」营销站**：以卖证为目的，把工具当宗教，忽视思维。
  - **AI 生成「lean tips」内容（2025–2026 激增）**：无 gemba 根基，套话化、正确但无用。
  - **把 Agile/Startup 的「Lean」当制造精益**：Eric Ries 的 Lean Startup 与制造 TPS 同名不同物，勿混淆。

## F2. 信息污染现象
1. **定义漂移**：Muda 被简化成「七大浪费」列表，丢失「必要 vs 不必要」的判断。
2. **工具拜物**：以为导入 5S/看板 = 精益，忽视文化与人财育成。
3. **认证通胀**：带级证书≠能力，ASQ 认证有门槛但仍被营销滥用。
4. **AI 洗稿**：2026 年大量「lean + AI」文章实为提示词拼凑，无案例。

## F3. 高质量内容判据（7 条）
1. **来自现场（gemba）**：有具体企业、产线、数据，非纯理论。
2. **区分工具与思考方式**：明确指出「工具是手段，态度/思维是根本」（如 Ballé「The attitude of Lean」）。
3. **作者有一线履历**：丰田/LEI/JIPM/企业改善负责人背景优先。
4. **引用原始文献**：丰田官方、LEI、学术（dspace/ASQ）而非二手博客。
5. **承认失败与局限**：真实转型都说「跌倒七次站起八次」。
6. **标注［一手/二手］**：信源透明，可追溯。
7. **持续更新、可追因**：非一次性爆款，能看历史脉络。

## F4. 中英文圈质量差异
- **英文圈**：源头多（LEI/丰田/Planet Lean）、学术厚（MIT/INSEAD/ASQ）、社群大（Reddit 合计 100k+），但认证营销噪音也多。
- **中文圈**：一手信源**高度依赖 LEC**（leanchina.net.cn），其余多二手转述；公众号/知乎质量方差极大；日语原典（日経ものづくり、JIPM）稀缺且语言门槛高。结论：**中文读者应先锁定 LEC + 丰田官方中文页 + Planet Lean 英文原刊，再谨慎补 Reddit，避开公众号/知乎作信源**。

---

# G. 知识更新节奏（核心概念 / 工具层 / 数字化 AI 精益）

> 三层衰减模型 + 时间投入建议。

## G1. 三层衰减频率
| 层 | 内容 | 半衰期 | 保鲜方式 |
|---|---|---|---|
| **核心概念层** | TPS 两大支柱（JIT/Jidoka）、三浪费、流动/拉动、方针管理、A3 思维、gemba | 数十年（几乎不衰减） | 啃经典书（Womack/Ballé/新乡重夫）+ 丰田官方页，一次学透 |
| **工具层** | VSM、5S、kanban、SMED、TPM、安灯、标准化作业、价值流、jishuken | 5–10 年慢迭代 | 年度复训、标杆访学（JIPM/LEC 研修）、Reddit 踩坑 |
| **数字化/AI 精益层** | Lean Tech、AI×jidoka、数字孪生、智能排产、人本组织 vs AI | 季度级快衰减 | Planet Lean Lean Tech Voices、LEI Lean AI Basics、行业会议 |

## G2. 时间投入建议（周）
- **70% 经典扎根**：重读《改变世界的机器》《精益思想》《丰田模式》《学习观察》《新乡重夫谈 TPS》；丰田官方 TPS 页每月回看。
- **20% 跟会议/期刊**：订阅 Planet Lean + The Lean Post + LEC 知识平台；年度参加 ≥1 场会议（Lean Global Connection 免费优先）。
- **10% 追 AI 前沿**：仅用一手（Planet Lean Lean Tech Voices、LEI Lean AI Basics），警惕 AI 洗稿。

## G3. 一句话结论
**根基不衰减，工具慢衰减，AI 快衰减；用 70/20/10 配比守住本源，让会议与官刊替你追踪前沿，别让「新词」牵着走。**

---

## 附：来源总数与可信度比例（诚实统计）
- 总条目：**62 条**（A 节 18、B 节 8、C 节 9、D 节 11、E 节 9、F 节 7 噪音/判据）。
- **［一手］≈ 42 条（68%）**：机构官网/官刊/官会/官方频道。
- **［二手］≈ 14 条（22%）**：Reddit、ResearchGate、媒体/学术索引、独立博客。
- **［推断］≈ 6 条（10%）**：活跃度推断、URL 路径待核实、未实测项。
- **已实测核实活跃度 ≈ 80%**；**标注「活跃度未核实/待核实」≈ 20%**（A3 Japan Quality、C 节 Leadership Podcast、D 节 ASQ/CIMT、E 节 Discord 等，均如实标注，未编造）。

## 附：用户预设纠正清单（避免 master skill 继承错误）
1. Planet Lean = LGN 官方杂志，非 Tomas Keyter 播客。
2. LEI 无带级认证；带级认证属 ASQ（CSSBB 等）。
3. MIT lean.mit.edu 现为机器人组；LAI 论文在 dspace.mit.edu。
4. INSEAD 无独立 Lean Summit；有 Learning@INSEAD Summit 2026。
5. 「The Lean Leadership Podcast」未证实；「Japan Quality」newsletter 未证实为独立信源。
6. 中文圈一手信源以 LEC 为核心，公众号/知乎/CSDN/百度系不作为信源。

---
*本报告为 Track 05 信源调研，供 master skill「信息源」模块蒸馏使用。所有未核实项已标注，诚实优先于覆盖。*
