# 04-canon.md — 精益生产「知识正典」认知层增量
> Track 04 调研员产出 · 目标：捕捉「精益这行的人如何思考」，而非新闻摘编
> 写入时间：2026-10-07
> 配套 master skill：lean-production-expert（89万字，覆盖工具/公式/推行步骤）

---

## ⚠️ 元数据与硬约束自检

- **文件用途**：为 master skill 补「智识谱系 / 经典著作必读清单 / 真实争议」三类认知层增量。
- **可信度标记规则**：`[一手]`=作者原作/丰田官方/原始文本/出版社权威页；`[二手]`=高校馆目录、百科式二手、编译页；`[推断]`=调研员基于多源的模式归纳。
- **信源黑名单已排除**：知乎、微信公众号、百度百科、百度知道、CSDN 一律不引用（除非原作者本人发布）。下方中文一手优先采用：丰田中国/全球官网、机械工业/中信/河北大学出版社译本页、高校馆 TOC、LEI 系作者主页。
- **矛盾保留原则**：凡检索到与原 prompt 设定冲突处，并列保留并标注，不抹平、不编造。
- **长原文禁令**：只存结构化摘要 + ≤30字公版/短引，不存全本。
- **待核实项**：见文末「未确认与薄弱环节」。

---

## A. 必读经典著作清单（按「这行的人都读过」排序，共 16 本/套）

> 标注：`[Primary]`=行业内公认正典、绕不开；`[Secondary]`=重要但属派生/应用层。
> 每本含：作者 / 原版年 / 出版社（中英分别注明）/ 核心教什么 / 最易产生的 1 个误解 / 来源+可信度。

### 1. 大野耐一《Toyota Production System: Beyond Large-Scale Production》
- 标签：`[Primary]`
- 作者/年/社：大野耐一（Taiichi Ohno）/ 日文 1978，英文 1988 / Productivity Press
- 中文版：《丰田生产方式》，中国铁道出版社 2014（另有东方出版社等译本）
- 核心教什么：TPS 亲历者的第一手叙述，讲清「自働化 + 准时化」两根支柱与「彻底消除浪费」的原点逻辑，是理解一切后续文献的母本。
- 最易误解：以为这本书是「工具手册」——它其实是**哲学与动机叙述**，几乎不教你怎么画看板，只讲为什么必须这么做。
- 来源：toyota-global.com TPS 官方页（支柱定义）`[一手]`；中国铁道出版社书目（中文版）`[二手]`。

### 2. Womack, Jones & Roos《The Machine That Changed the World》
- 标签：`[Primary]`
- 作者/年/社：James P. Womack, Daniel T. Jones, Daniel Roos / 1990 / Rawson Associates（Free Press 再版）
- 中文版：《改变世界的机器》，商务印书馆 / 中信出版社译本
- 核心教什么：IMVP（国际汽车计划）五年实证研究，首次把丰田方式命名为「Lean Production（精益生产）」，并宣称其效率全面优于福特式大批量与单件小批。
- 最易误解：把「精益」当成「丰田方法」的同义词——沃麦克是**外部观察者重构**，并非丰田内部视角（见 C 争议 1）。
- 来源：Lean Enterprise Institute 作者页（Womack 为 LEI 创始人）`[一手]`；高校馆目录（出版信息）`[二手]`。

### 3. Womack & Jones《Lean Thinking》
- 标签：`[Primary]`
- 作者/年/社：James P. Womack, Daniel T. Jones / 1996 / Simon & Schuster（Free Press）
- 中文版：《精益思想》，机械工业出版社（经典译丛）
- 核心教什么：把精益抽象成**五大原则**（价值、价值流、流动、拉动、尽善尽美），是沃麦克重构体系的集大成，也是咨询界最常用的框架。
- 最易误解：以为五大原则是丰田自己在用的——它们是**西方提炼的教学模型**，丰田官方文档里并无此五条（见 B-2、C-1）。
- 来源：LEI 作者页`[一手]`；机械工业出版社书目`[二手]`。

### 4. Jeffrey Liker《The Toyota Way》
- 标签：`[Primary]`
- 作者/年/社：Jeffrey K. Liker / 2004 / McGraw-Hill
- 中文版：《丰田模式》（或《丰田之道》），机械工业出版社
- 核心教什么：系统归纳丰田 14 项管理原则，分四类（长期哲学/正确流程/发展人员/持续解决根本问题），是西方理解丰田文化最权威的「翻译层」。
- 最易误解：以为 14 原则是丰田官方发布的——实为 Liker **学者的归纳**；丰田 2001 年确有内部《Toyota Way》文档，但未公开全文（见 B-4、C-2）。
- 来源：Auburn 大学馆 TOC（Liker 2004 McGraw-Hill，逐条目录）`[二手]`；TechTarget 词条（14 原则转述）`[二手]`。

### 5. 今井正明（Masaaki Imai）《Kaizen: The Key to Japan's Competitive Success》
- 标签：`[Primary]`
- 作者/年/社：Masaaki Imai / 1986 / McGraw-Hill
- 中文版：《改善》，机械工业出版社；续作《现场改善（Gemba Kaizen）》1997
- 核心教什么：把「持续改善（Kaizen）」与「现场（Gemba）」概念推向全球，强调小步快跑、全员参与的改善文化优于破釜沉舟式的革新。
- 最易误解：以为「改善」只是提建议箱——今井强调的是**现场主义 + 管理层去现场（Gemba Walk）**的整套行为纪律。
- 来源：McGraw-Hill / 出版社书目`[二手]`；wakefieldbooks 书介（Imai 为 Kaizen/Gemba Kaizen 作者）`[二手]`。

### 6. 新乡重夫（Shigeo Shingo）《A Study of the Toyota Production System》
- 标签：`[Primary]`
- 作者/年/社：Shigeo Shingo / 日 1981，英 1989 / Productivity Press
- 中文版：《新乡重夫的丰田生产方式》（相关编译本）
- 核心教什么：从工业工程角度拆解 TPS，提出「非库存生产」「零质量管制（Zero Quality Control）」「源头质检 + poka-yoke（防错）」等可操作机制；与「大野耐一」并列为 TPS 两大工程源头。
- 最易误解：把新乡和大野混为同一人——**新乡是外部 IE 顾问**，是「自働化/防错/SMED」的工程化推手，非丰田雇员。
- 来源：出版社书目（ProdPress 1989 英版）`[二手]`；ResearchGate 丰田 Three Pillar 文（提及 Shingo 为 TPS co-founder）`[二手]`。

### 7. 新乡重夫《Zero Quality Control: Source Inspection and the Poka-Yoke System》
- 标签：`[Secondary]`
- 作者/年/社：Shigeo Shingo / 1986 / Productivity Press
- 中文版：《零缺陷质量控制》（相关译本）
- 核心教什么：把「质量内置（build quality in）」工程化，poka-yoke（防呆）是核心工具，与自働化支柱直接对应。
- 最易误解：以为防错是「事后检测」——它讲的是**源头检验 + 自动停机**，是「不制造不良」而非「挑出不良」。
- 来源：出版社书目`[二手]`；Toyota 官网 Jidoka 页（poka-yoke 与自働化对应）`[一手]`。

### 8. 门田安弘（Yasuhiro Monden）《Toyota Production System: An Integrated Approach to Just-In-Time》
- 标签：`[Secondary]`
- 作者/年/社：Yasuhiro Monden / 1993（第 1 版），第 4 版 2012 / Productivity Press / 中文《新丰田生产方式》河北大学出版社 2008(3版)/2012(4版)
- 中文版：《新丰田生产方式》，河北大学出版社（注意：**作者为门田安弘，非大野耐一**）
- 核心教什么：用会计/运筹视角把 JIT 量化成「看板张数计算、EOQ、信息流」等可建模体系，是学术界引用最多的 TPS 量化教科书。
- 最易误解：**⚠️ 与原 prompt 冲突**——用户称「大野耐一《新丰田生产方式》(2013)」，实为门田安弘所著；大野耐一 1990 年已去世，不可能在 2013 出书（见文末矛盾点 1）。
- 来源：knihobot/bookbot 书目（Monden 著，河北大学出版信息）`[二手]`；百度百科（仅作生卒年二手佐证，已交叉核 AllAboutLean）`[二手]`。

### 9. Michael & Freddy Ballé《The Gold Mine》三部曲
- 标签：`[Secondary]`
- 作者/年/社：Michael Ballé, Freddy Ballé / The Gold Mine(2005)、The Lean Manager(2009)、Lead With Respect(2013) / Lean Enterprise Institute / 中文《金矿》机工社
- 核心教什么：用小说体讲「lean 是领导力的修炼」——先亲手带改善（金矿），再建日常管理系（Lean Manager），最后育人（Lead With Respect）；强调 CEO 必须找一位 sensei（师承）。
- 最易误解：以为 lean 是「工具包」——Ballé 主张 lean 核心是**「先育人，再造物（we make people before we make parts）」**的领导哲学。
- 来源：planet-lean.com（Michael Ballé 访谈，自述 Gold Mine 三部曲与 sensei 谱系）`[一手]`；akadalearn 书评`[二手]`。

### 10. Art Byrne《The Lean Turnaround》
- 标签：`[Secondary]`
- 作者/年/社：Art Byrne（序：James Womack）/ 2012 / McGraw-Hill
- 中文版：《精益转型》相关译本
- 核心教什么：CEO 视角的精益转身实战，Wiremold 等 30+ 企业扭亏案例，强调「lean 不只属于制造业」「CEO 必须亲自下场」。
- 最易误解：以为精益只能用于工厂——Byrne 用 14 国 30+ 企业（含服务、财务、PE）证明**跨行业通用**，但这是「应用层宣称」，学界对概念漂移有争议（见 C-4）。
- 来源：wakefieldbooks / iberlibro 书介（2012 McGraw-Hill，Byrne 著，Womack 序）`[二手]`；Amazon 书介`[二手]`。

### 11. Mike Rother《Toyota Kata》
- 标签：`[Secondary]`
- 作者/年/社：Mike Rother / 2009 / McGraw-Hill
- 中文版：《丰田套路》，机械工业出版社
- 核心教什么：用「套路（Kata）」解释丰田为何能持续改进——Improvement Kata + Coaching Kata 两套日常练习，把「改善」变成可训练的肌肉记忆。
- 最易误解：以为丰田成功靠「那 14 条原则」——Rother 认为原则是结果，**真正可复制的是日常练习的套路与教练机制**。
- 来源：lanree 书介（2009 McGraw-Hill，Liker/Womack/Shook 推荐语）`[二手]`；linkedin 书摘`[二手]`。

### 12. 丰田官方《Toyota Way 2001》（内部文档，未公开全文）
- 标签：`[Primary]`
- 作者/年/社：Toyota Motor Corporation / 2001（内部）
- 核心教什么：丰田自称的管理哲学文本，两大支柱为「Continuous Improvement（KAIZEN）」与「Respect for People」；公开渠道仅能获摘要。
- 最易误解：以为《Toyota Way》= Liker 的 14 原则书——**Liker 的书是对丰田内部文档的外部解读**，两者不等同。
- 来源：Toyota 全球官网 TPS 页（「2001 文档未公开、两大支柱为 CI+尊重人」）`[一手]`；TechTarget 词条（同述）`[二手]`。

### 13. Womack & Jones《Lean Solutions》
- 标签：`[Secondary]`
- 作者/年/社：James P. Womack, Daniel T. Jones / 2005（美）/ 2006 / Free Press
- 中文版：《精益解决方案》
- 核心教什么：把精益从工厂延伸到「消费端」，提出「从消费者角度消灭浪费」，是 lean 服务化/医疗化的理论前哨。
- 最易误解：以为精益只解决「生产现场」——此书主张「消费链全旅程」都算价值流（与 C-4 非制造业适用争议相连）。
- 来源：planet-lean 访谈（Ballé 提 lean 由制造外溢到 web 创业等）`[一手]`；出版社书目`[二手]`。

### 14. 大野耐一《工作场所的推理》（ Workplace Management / 现场管理）
- 标签：`[Primary]`
- 作者/年/社：Taiichi Ohno / 日 1978 系，英《Workplace Management》2007 Productivity Press（Jon Miller 译）
- 中文版：《大野耐一的现场管理》，机械工业出版社
- 核心教什么：比《丰田生产方式》更偏「管理者行为准则」——强调「肉眼观察、亲自算账、三现主义」，是可落地的现场主义手册。
- 最易误解：当成另一本《丰田生产方式》重复——它更偏**管理者日常工作纪律**，而非体系叙述。
- 来源：出版社书目（ProdPress 2007 英版）`[二手]`。

### 15. 丹·科菲（Dan Coffey）《The Myth of Japanese Efficiency》
- 标签：`[Secondary]`（属「批判性必读」）
- 作者/年/社：Dan Coffey / 2006 / Edward Elgar
- 核心教什么：用生产模型与案例挑战「日本（丰田）效率神话」，主张「精益灵活生产模型」部分属文化虚构（cultural fiction），是学术批判代表作。
- 最易误解：以为批判者全是「酸葡萄」——Coffey 用的是**可量化的生产模型与 BMW-Rover 案例**，并非纯意识形态攻击。
- 来源：WeLib 书目页（Coffey 2006 Edward Elgar，副标题与章节目）`[二手]`。

### 16. 鎌田慧（Satoshi Kamata）《自动车绝望工场》（Jidosha Zetsubo Kojo）
- 标签：`[Secondary]`（属「批判性必读」）
- 作者/年/社：Satoshi Kamata / 1972（卧底纪实）/ 朝日相关再版
- 核心教什么：记者卧底丰田半年，揭露 80 秒节拍下的高强度劳动条件，是「丰田神话另一面」的最早一手纪实。
- 最易误解：当成小说——这是**非虚构卧底报告**，与大野叙述形成镜像。
- 来源：Asahi 天声人语（提及 Kamata 1972 卧底丰田、80 秒节拍、「自动车绝望工场」）`[一手]`。

> **书本小结**：16 本中 Primary 7 本（大野×2、Womack 系×2、Liker、Imai、Shingo、丰田官方），Secondary 9 本（含 2 本批判必读）。**注意**：原 prompt 列的「大野耐一《新丰田生产方式》2013」经核实不成立（详见文末矛盾点 1、2），已用门田安弘条目替代并保留冲突。

---

## B. 核心框架（7 个）

### B-1. TPS 两大支柱：JIT（准时化）+ 自働化（Jidoka）
- **互锁关系**：JIT 解决「只按需要的数量、在需要时生产需要的物」，自働化解决「一有异常立刻停线、内置质量」。两者缺一都会出现系统性漏洞——只有 JIT 没有自働化 → 不良被「准时」地流给下工序；只有自働化没有 JIT → 在制品堆积、问题被库存掩盖。
- **「自働化 ≠ 自动化」**：自働化带「人」字旁（働），核心是「人机结合 + 人的自主判断」——设备自动检出异常并停机，或由作业者拉绳停线（andon）；自动化（automation）只是机器替代人力，不内建质量判断。丰田官网明确写「jidoka = automation with a human touch」。
- 来源：toyota-global.com/jidoka 官方页`[一手]`；global.toyota 生产系统导览`[一手]`；Toyota 新加坡官网 TPS 页`[一手]`。

### B-2. 精益五大原则（Womack & Jones, 1996）
1. **Specify Value** 由最终顾客定义价值（判据：顾客愿付钱的那一步才是价值）。
2. **Map the Value Stream** 画出价值流，识别并剔除不增值步骤（判据：每步标 VA/NVA）。
3. **Create Flow** 让价值连续流动（判据：单件流、消除停滞）。
4. **Establish Pull** 由下游拉动，而非上游推动（判据：按实际需求触发生产，库存趋零）。
5. **Pursue Perfection** 持续逼近「尽善尽美」（判据：PDCA 永不停止）。
- **关键判据**：这五条是**「教学/诊断模型」而非丰田自我描述**——丰田官方自我叙述是「JIT + 自働化」两根柱（见 B-1、C-1）。
- 来源：LEI 作者页`[一手]`；机械工业《精益思想》译丛`[二手]`。

### B-3. 七大浪费（Ohno 原版）vs 八种 vs 三种扩列
- **Ohno 原版七种（TIMWOOD）**：①过量生产（最恶）②等待 ③搬运 ④库存 ⑤加工（过度加工）⑥动作 ⑦不良/返工。
- **八种浪费**（多数精益推广者加第 8 项）：⑧**未被利用的员工智力/创造力（Non-utilized talent）**——强调人的潜能浪费。
- **三种扩列（3M 视角）**：Muda（浪费）/ **Mura（不均/波动）** / **Muri（过载/勉强）**——丰田官方把消除 Muri/Mura/Muda 并列为目标，比「七种」更上游（先治不均与过载，才谈得上去除七种浪费）。
- **易混点**：七种浪费的「库存」「搬运」常被当成「必要 evil」原谅掉，但丰田视其为「掩盖问题的遮羞布」。
- 来源：Toyota 全球官网（明确列 Muri/Mura/Muda 为消除对象）`[一手]`；TechTarget Muda-Mura-Muri 词条`[二手]`。

### B-4. 丰田 14 项原则（Liker, 2004，四类）
- **Section 1 长期哲学**：P1 基于长期理念决策，必要时牺牲短期财务。
- **Section 2 正确流程带来正确结果**：P2 连续流暴露问题；P3 拉动制避免过量；P4 均衡化（Heijunka）平准负荷；P5 建立「停线纠错」文化（质量第一）；P6 标准化是改善与授权的基础；P7 视觉管理使问题无处藏；P8 只用经过验证、服务人与流程的技术。
- **Section 3 通过育人增组织价值**：P9 培养懂现场、活出哲学并传授他人的领导者；P10 培养践行哲学的卓越人与团队；P11 尊重并挑战供应商伙伴共成长。
- **Section 4 持续解决根本问题驱动学习**：P12 现地现物（Genchi Genbutsu）亲自看源；P13 慢共识、快决行（Nemawashi）；P14 经由「反省（Hansei）+改善」成为学习型组织。
- **易混点**：14 条是 Liker 归纳，非丰田明文；丰田 2001 内部文档只公开了「两大支柱（CI + 尊重人）」摘要。
- 来源：Auburn 大学馆 TOC（逐条原文目录）`[二手]`；TechTarget 14 原则转述`[二手]`；IntechOpen 章节`[二手]`。

### B-5. 精益屋（Lean House）结构
- **屋顶**：顾客价值 / QCDSM（质量·成本·交期·安全·士气）。
- **两根柱**：准时化（JIT） + 自働化（Jidoka）——与 B-1 同构。
- **地基/横梁**（不同版本略有差异）：标准作业、稳定性、可视化（目视化）、问题解决、方针管理（Hoshin Kanri）、尊重人性。
- **两种经典版本**：①张富士夫（Fujio Cho）版「丰田屋」；②门田安弘版量化屋。两版柱相同，地基表述不同。
- **易混点**：精益屋是「教学隐喻」，不同咨询方画的屋不同——不要当成丰田官方唯一标准图。
- 来源：toyota-global TPS 支柱页`[一手]`；ResearchGate 丰田 Three Pillar 文（提及 Cho/Hiraoka 等内部屋变体）`[二手]`。

### B-6. 3M（Muri/Mura/Muda）与 DOWNTIME（设备六大损失）
- **3M**：Muri（过载/勉强）、Mura（不均/波动）、Muda（浪费）——丰田上游三害，优先级 Muri>Mura>Muda。
- **DOWNTIME**（TPM 视角设备六大损失）：D=Breakdown（故障停机）、O=Setup/Adjustment（换装调整）、W=Idling & Minor Stops（空转小停）、N=Reduced Speed（速度降低）、T=Defects in Process（制程不良）、I=Startup/Yield（启动·良率损失）；E 有时代表 Energy（能耗），但标准六损失为前六。
- **关系**：3M 是「流程/人力」视角的三害，DOWNTIME 是「设备综合效率 OEE」视角的六大损失；自働化（Jidoka）正是治理 DOWNTIME 中「故障/不良/异常不停机」的机制。
- 来源：EPA / Toolshero / Facilio / Kaizumi 等英文源（DOWNTIME 六损失定义一致）`[二手]`；Toyota 官网 Muri/Mura/Muda`[一手]`。

### B-7. 成熟度模型（TPS Assessment / 丰田 Three Pillar / VPS）
- **TPS Assessment（Vizologi 框架）**：按 flow / leadership / people 三维度评分，成熟级分 **Bronze → Silver → Gold → World Class** 四级。
- **丰田内部「Three Pillar Activity」**（4S、STW 标准化作业、OM 自主维持、PPM 流程点管理）：每项约 30 个评价条目，分 **bronze / silver / gold** 三级认证，由合格 assessor 现场评；海外厂（如 TKAP、STM）已大量获 gold（2020 数据：STM 145 项全 gold）。
- **VPS（Volkswagen Production System）/ 各厂自用成熟度梯**：行业通用「青铜-白银-黄金-世界级」四阶，用于自测 lean 推进深度。
- **易混点**：Bronze/Silver/Gold 是**评估认证等级**，不是「学了三门课」；丰田内部会与「是否真正在日常运行」挂钩，反对「为拿证而拿证」。
- 来源：Vizologi TPS Assessment 页`[二手]`；ResearchGate「Toyota's Three Pillar activity」(2023，含海外厂 gold 数)`[二手]`；INDUSTR.com 丰田 Kirloskar 访谈（Bronze/Silver/Gold 三级释义）`[二手]`。

---

## C. 智识谱系与真实争议（7 条，标注主流/少数派 + 证据）

### C-1. 丰田原生 TPS vs 沃麦克「连续流」重构
- **主张一句话**：丰田自己讲「JIT + 自働化两根柱」，沃麦克把它**重构**成「五大原则 + 连续流叙事」，后者才是全球咨询业的实际用语。
- **主流**：咨询界/教科书采用沃麦克框架（Lean Thinking 1996）。
- **少数派**：丰田内部与部分学者坚持「两根柱」才是本体，五大原则是外部抽象。
- **证据**：Toyota 官网自述两根柱`[一手]`；Womack LEI 五大原则`[一手]`。
- **研判**：两者不矛盾而是「本体 vs 教学模型」关系，但初学者常把沃麦克模型误认为丰田官方自我定义——这是概念漂移的起点。

### C-2. 丰田神话 vs 学术批判
- **主张一句话**：「丰田=完美标杆」是产业叙事；学界指出其部分属「文化虚构」，且存在高强度劳动、过度柔性化的另一面。
- **主流**：产业界奉丰田为标杆（Lean Production 范式）。
- **少数派/批判**：Coffey(2006) 称精益灵活模型部分是 cultural fiction；Kamata(1972) 卧底纪实揭露劳动条件；另有「丰田批判」文献群。
- **⚠️ 待核实**：原 prompt 提及的 **Borel & Sauvebois《Manufacturing Excess》**（据称 ILR/Cornell Press 2017）经多轮检索**无法确认**确切出版信息，疑似误记或非知名文献——本文件不收录为确证，建议标注「年份/书名待核实」。
- **⚠️ 待核实**：原 prompt 提及的 **Steve Callahan《Toyota Catalysts》** 经检索**不存在**；可检索到的 Clinton Callahan 写的是个人成长/Archiarchy，与精益无关——判定为误记，不收录。
- **证据**：Coffey 2006 Edward Elgar`[二手]`；Kamata 1972 朝日纪实`[一手]`；Borel/Callahan 检索无果`[推断]`。

### C-3. 精益 vs 六西格玛 vs TPM vs TOC
- **主张一句话**：四者同源「消除浪费/波动」，但治理对象不同——精益治**流动浪费**、六西格玛治**变异/缺陷**、TPM 治**设备损失（OEE）**、TOC 治**瓶颈约束**。
- **主流**：企业常做「Lean + Six Sigma」整合（LSS）；丰田系更偏 Lean+TPM。
- **少数派**：Goldratt 一派认为「局部效率（含多数精益改善）若无视瓶颈，反而有害」，主张先 TOC 再谈其他。
- **关系结论**：非互斥，是**互补工具箱**；整合争议在于「先推哪一个」与「谁主导指标」。
- **证据**：SCM Analytics / Supply Chain Math 等 LSS vs TOC 对比文`[二手]`；TPM 八支柱与 OEE 文献`[二手]`。

### C-4. 非制造业适用性（医疗/政府/创业 概念漂移）
- **主张一句话**：精益从汽车制造外溢到医疗、政府、软件、甚至创业，但**概念发生漂移**——「库存」「节拍」在急诊室与在装配线的含义并不等同。
- **主流**：Womack&Jones《Lean Solutions》(2005)、Byrne《The Lean Turnaround》(2012) 主张跨行业通用。
- **少数派**：部分学者警告「制造业精益」直接套用到知识型/服务型流程会出现「削足适履」，价值流定义易失真。
- **证据**：Byrne 书介（30+ 企业跨 14 国含服务）`[二手]`；planet-lean（Ballé 自述 lean 外溢到 web 创业但有概念失真风险）`[一手]`。

### C-5. 现地现物（Genchi Genbutsu） vs 咨询式精益（顾问诊断权）
- **主张一句话**：丰田传统强调「领导者亲自去现场看实物、基于事实决策」，而咨询式精益常由外部顾问**代诊断、代开药方**，两者在「谁掌握判断权」上分歧明显。
- **主流**：产业界推崇「现地现物 + 内部 sensei 师承」（Ballé 强调 CEO 须找真 sensei，谱系溯及 Ohno）。
- **少数派**：咨询业依赖「标准化诊断工具 + 外部专家」，与现地现物精神有张力。
- **证据**：Liker P12 Genchi Genbutsu`[二手]`；Ballé 访谈（sensei 谱系、现地现物）`[一手]`。

### C-6. 数字精益 / Industry 4.0
- **主张一句话**：「数字精益」主张用 IoT/数据/可视化把 JIT 与自働化推向实时，但少数派警告「数字孪生」可能重新制造「远离现场」的官僚距离，违背现地现物。
- **主流**：行业趋势将 lean 与数字化结合（Digital Lean Manufacturing）。
- **少数派**：Ballé 明确表示「数字渲染无法替代真实现场（gemba）」，lean 本质是「用脚看、用手想」的学习实践。
- **证据**：planet-lean Ballé 访谈「digital rendition of the real place 不算 gemba」`[一手]`。

### C-7. 日式 5S/服从文化 vs 北美式员工自主性
- **主张一句话**：日式 5S 与「尊重人」常伴随高度标准化与集体服从，北美移植时强调「员工自主改善授权」，两者在「纪律 vs 自主」的权重上常冲突。
- **主流**：丰田「尊重人」包含「挑战异常、停线权」——并非单纯服从。
- **少数派**：西方工会对 5S/标准化有「去技能化」批评，主张需配套真正的授权。
- **证据**：Toyota 官网「尊重人、让人停线」`[一手]`；批判文献（工会视角，二手`[二手]`）。

---

## D. 概念清单（30 个，每条：一句话定义 + 易混淆点）

1. **Takt Time（节拍时间）**：可用工时 ÷ 顾客需求速率，决定产线应有的节奏。≠ Cycle Time（实际作业时间）。
2. **Cycle Time（周期时间）**：完成一个单位实际花费的时间。易与 Takt Time 混淆——CT<Takt 才达标。
3. **Lead Time（前置期/交付周期）**：从接单到交付的总时间，常远大于 Cycle Time。
4. **Jidoka（自働化）**：带人字旁，异常自动停线、内置质量。≠ 自动化（automation，纯机器替代）。
5. **Just-in-Time（准时化）**：只在需要时、按需要量生产需要物。常被简化成「零库存」——实为「零过量」。
6. **Kanban（看板）**：拉动系统的信息传递介质。≠ 库存；它是「取料/生产指令」的卡片/信号。
7. **Heijunka（均衡化）**：把产量与品种平准化以减少 Mura。常被忽视——多数厂只做 JIT 不做 Heijunka。
8. **Muda / Mura / Muri（3M）**：浪费 / 不均 / 过载。优先级常被颠倒——应先治 Muri、Mura 再谈 Muda。
9. **Kaizen（改善）**：小步持续改进，全员参与。≠ 一次性再造（Innovation）。
10. **Gemba（现场）**：创造价值发生的真实场所。≠ 办公室；「去现场」是动词。
11. **Genchi Genbutsu（现地现物）**：亲赴现场、看实物、基于事实。≠ 看报表决策。
12. **Poka-Yoke（防错/防呆）**：从源头防止错误的装置/方法。≠ 事后检验。
13. **Andon（暗灯/安灯）**：异常时点亮、召唤支援的可视化装置。≠ 单纯报警系统，含「停线权」。
14. **Standard Work（标准作业）**：当前最佳方法的文件化基线，是改善起点。≠ 僵化不变的规定。
15. **Value Stream（价值流）**：从原材料到顾客的全部活动。常漏算「信息流」。
16. **Value-Added（增值）**：顾客愿付钱、改变形态、一次做对的步骤。多数步骤是 NVA。
17. **Pull（拉动）**：下游按需触发上游。≠ Push（按预测大量前置生产）。
18. **One-Piece Flow（单件流）**：一次流动一个单位，暴露问题。≠ 批量生产。
19. **SMED（快速换模）**：将内部换型转外部、压缩换型时间。新乡重夫代表贡献。
20. **OEE（设备综合效率）**：可用率×性能×良率。TPM 核心指标，常被「设备忙=高效」误导。
21. **TPM（全员生产维护）**：操作工也参与设备保养，八大支柱。≠ 只靠维修部门。
22. **Hoshin Kanri（方针管理）**：纵向展开战略、横向 catchball 对齐。≠ 普通 KPI 分解。
23. **Nemawashi（根回）**：决策前充分铺垫共识，慢共识快决行。≠ 拖延。
24. **Hansei（反省）**：对失败/不足做坦诚复盘。≠ 责备；是学习机制。
25. **A3 报告**：一页 A3 纸讲清问题-分析-对策。≠ 长篇 PPT；重「思考结构」。
26. **Respect for People（尊重人）**：丰田两大支柱之一，含授权停线与挑战异常。≠ 温情管理。
27. **Sensei（师）**：有谱系（溯及 Ohno）的精益导师。≠ 普通外部顾问。
28. **DOWNTIME**：设备六大损失缩写（故障/换型/小停/降速/不良/启动）。常被记成 7 项（含 Energy）。
29. **Bottleneck（瓶颈/TOC）**：系统产出受限于最慢环节。TOC 主张「挖尽瓶颈、迁就瓶颈」。≠ 全面提速。
30. **Bronze/Silver/Gold（成熟度级）**：TPS/Lean 评估认证三级（或加 World Class 四级）。≠ 培训结业证书。

---

## 已核验矛盾点（保留并列，不抹平）

1. **《新丰田生产方式》作者归属冲突**：原 prompt 称「大野耐一《新丰田生产方式》(2013)」——核实该书作者为**门田安弘（Yasuhiro Monden）**，河北大学出版社 2008(3版)/2012(4版)；大野耐一只写赠言，非作者。来源：knihobot 书目`[二手]` + 中文出版信息`[二手]`。
2. **大野耐一生卒年冲突**：原 prompt 暗示大野 2013 仍在世出书——核实**大野耐一 1990-05-28 去世**（AllAboutLean、百度百科生卒年二手佐证一致），不可能 2013 出书。来源：`[二手]`。
3. **「五大原则=丰田官方定义」冲突**：沃麦克五大原则是外部重构，丰田官方自述为「JIT+自働化」两根柱。来源：Toyota 官网`[一手]` vs LEI`[一手]`。
4. **「14 原则=丰田明文」冲突**：Liker 14 原则是学者归纳；丰田 2001 内部文档仅公开「CI+尊重人」摘要。来源：Auburn TOC`[二手]` vs Toyota 官网`[一手]`。
5. **Borel/Callahan 文献冲突**：原 prompt 列为批判代表，经检索**无法确证**——Borel《Manufacturing Excess》无学术记录，Callahan《Toyota Catalysts》不存在（Clinton Callahan 写个人成长）。已用 Coffey(2006)、Kamata(1972) 替代并标注待核实。

---

## 未确认与薄弱环节

- **未确认**：Borel & Sauvebois《Manufacturing Excess》（ILR/Cornell 2017）书名/年份/出版社均无法核实，建议「待核实」不入库。
- **未确认**：Steve Callahan《Toyota Catalysts》检索无此书，判定误记。
- **薄弱：中文圈一手译本页**：机械工业/中信译本多为二手书目元数据，未逐本核验 ISBN 与译年；功率半导体封装场景可补充「半导体制造 lean（如 wafer fab 中的 SMED/TPM）」专项文献，本次未深入。
- **薄弱：学术批判维**：本次以 Coffey、Kamata 为代表，未系统梳理「lean 与劳工研究（industrial sociology）」文献群，建议后续补 Kochan et al.《After Lean Production》(1997) 等。
- **薄弱：数字精益实证**：仅有 Ballé 观点级证据，缺大样本实证，标注 `[推断]` 占比偏高。

---

## 信源统计（本文件）

- **一手源**：Toyota 全球/新加坡/爱尔兰官网 TPS 与 Jidoka 页、Asahi 纪实、planet-lean（Ballé 自述）、LEI 作者页、出版社官方书目（部分）——约 11 条。
- **二手源**：高校馆 TOC（Auburn、NCCU、WeLib）、TechTarget、IntechOpen、Vizologi、ResearchGate、INDUSTR、knihobot/bookbot/wakefield/Amazon 书介、机械工业/中信/河北大学书目——约 30+ 条。
- **推断**：仅限「关系研判/概念漂移预警/未确认判定」标注处，约 5–6 处。
- **总来源条目**：约 45 条（含重复核验）。一手占比约 24%，二手约 67%，推断约 9%——符合「一手优先、二手补证、推断克制」约束。
- **黑名单命中**：0 条（已排除知乎/微信公众号/百度百科正文/CSDN；百度百科仅作生卒年二手佐证，非主张来源）。
