# Task Prompt Orchestrator 中文介绍

## 一句话定位

`task-prompt-orchestrator` 是一个面向 Codex 的任务提示词编排 skill。它把用户随口说出的需求，转化成可执行、可验证、可交接的专业工作流。

它不是一个“把所有提示词都塞进上下文”的大模板包，而是一个低 token 消耗的智能调度入口：先收集任务信息，再扫描现有能力，然后只读取当前任务真正需要的最小索引、最小模板和最小参考文件。

换句话说，它做的是：

```text
用户的模糊目标 -> 精准 brief -> 能力扫描 -> 最小工作流 -> 专业提示词包 -> 执行 -> 验收证据
```

## 为什么需要它

很多 AI 任务失败，不是因为模型能力不够，而是因为一开始没有把任务组织好。

常见问题包括：

- 用户说了一个大目标，但没有拆成可执行步骤。
- 输入材料、文件、链接、截图、已有输出没有被系统整理。
- 明明本机已经安装了合适的 skill、插件、MCP 工具或脚本，却没有先用现成能力。
- 一上来就写长提示词，结果真正关键的约束、格式、验收标准没有进入执行流程。
- 为了找一个模板，把完整提示词库、全部矩阵或大量参考文档读进上下文，造成 token 浪费。
- 任务最后没有验证，只是“看起来做完了”，但没有文件、测试、链接、截图或检查结果作为证据。

`task-prompt-orchestrator` 的设计目标，就是把这些混乱点收束成一个稳定的执行入口。它让 Codex 在动手前先知道：目标是什么、输入在哪里、该调用什么能力、该读哪一个索引、该生成什么产物、用什么标准确认完成。

## 适合什么场景

这个 skill 特别适合以下任务：

1. 复杂任务启动
   - 用户只给了一个方向，比如“帮我做一个完整工作流”“把这个项目完善一下”“帮我把提示词库整理成专业体系”。
   - skill 会先把目标、输入、约束、可用工具和验收标准整理成 compact brief。

2. 多步骤执行任务
   - 例如研究、设计、写作、代码修改、数据分析、文档生成、图片生成、插件调用、GitHub 发布。
   - skill 会把任务拆成若干可执行 step，每一步都有输入、动作、输出和 done_when。

3. 提示词优化与提示词包生成
   - 适合把用户原始需求改写成专业 prompt packet。
   - 每个 packet 包含角色、目标、上下文、输入、流程、输出格式、约束、质量检查和交接信息。

4. 专业提示词库路由
   - 例如 image2、包装 CAD、商业海报、研究报告、代码审查、营销文案、教育辅导等。
   - skill 会先看索引，再进入命中的专业模板，不会默认打开整套库。

5. 插件和 skill 能力扫描
   - 当用户想知道“我现在能调用哪些能力”“这个任务该装什么插件”“GitHub/Codex/OpenAI 常用插件怎么选”时，它会优先扫描当前会话可见能力和本地 skill。

6. 新手 AI 工作流教学
   - 对不熟悉 AI 的用户，它不会抛出一堆理论，而是给出一个可复制、可执行、低认知负担的下一步动作。

## 核心功能

### 1. 任务接收信息结构化

skill 会把用户输入整理成一份内部 intake：

```text
Goal:
Raw user request:
Inputs supplied:
Workspace state:
Capability state:
Output target:
Constraints:
Acceptance checks:
Execution permissions:
Open questions:
Assumptions:
```

这一步的重点不是形式化，而是防止遗漏关键执行条件。比如文件在哪里、目标输出是图片还是仓库、是否允许安装插件、是否需要推送 GitHub、结果用什么标准验收。

### 2. 能力优先，而不是从零发明

它遵循 capability-first 原则：

1. 先看当前会话可见工具。
2. 再看已安装 skills。
3. 再看启用的 plugins/connectors。
4. 再看 MCP/app 能力。
5. 再看本地脚本、索引、提示词库和项目已有文件。
6. 只有没有合适能力时，才设计新的流程或模板。

这样做的好处是：结果更稳定，执行更快，也更容易复用用户已经配置好的环境。

### 3. 专业工作流路由

skill 内置了多类路由入口，能把任务分配到更具体的专业流程：

- image2 / 视觉生成 / 海报 KV / 产品图 / 包装图 / CAD-like 图纸
- GitHub / Codex / OpenAI / 仓库发布 / 插件安装 / 自动化
- 研究 / 分析 / 决策 / 学术资料整理
- 文档 / Word / Markdown / 汇报材料
- 数据分析 / dashboard / KPI / 可视化
- 前端 / 后端 / 代码审查 / 安全扫描
- 市场营销 / 广告素材 / 品牌定位 / 销售工作流
- 法律 / 金融 / 合规 / 商业计划
- 教育 / 复习 / 学习路径 / 新手训练

它不是每个领域都自己做到底，而是先找到最适合的专业能力，再把任务交给那个能力或模板执行。

### 4. 提示词包生成

当一个任务需要交给另一个 agent、工具或后续回合执行时，它会生成 prompt packet：

```text
Step ID:
Role:
Objective:
Context:
Inputs:
Procedure:
Output format:
Constraints:
Quality checks:
Handoff:
```

这个结构让任务可以被复用、交接、拆分，也方便后续审查哪里做对了、哪里需要补。

### 5. 执行与验收闭环

如果用户要求的是“做完”，skill 不会停在计划阶段。它会推动执行，并在最后给出证据：

- 文件路径
- Git commit
- GitHub 链接
- 测试命令
- 脚本输出
- 图片路径
- 渲染检查
- 远程访问结果
- 仍然存在的风险或缺口

这让“完成”变成可以检查的状态，而不是一句口头承诺。

## 实现原理

### 1. 渐进式披露

这个 skill 的关键设计是 progressive disclosure，也就是按需加载。

第一层：metadata

- `name`
- `description`

这部分最短，用于触发 skill。

第二层：`SKILL.md`

主文件只保留核心工作流：能力扫描、输入收集、brief 优化、步骤拆分、模板选择、执行和验收。

第三层：`references/`

具体领域的长内容都放在 references 中。只有当任务命中某个方向时，才读取对应文件。

第四层：`scripts/`

脚本用于快速路由、校验激活面、扫描能力，减少重复读取和重复判断。

这种结构的重点是：默认只加载必要信息，复杂任务才逐步打开更细的资料。

### 2. 索引优先

对于 image2 这样的专业提示词库，skill 不会直接打开全部 prompt 文件。它会先读索引：

```text
D:\image2专业提示词库\indexes\IMAGE2_VERTICAL_PROMPT_INDEX.md
```

如果任务涉及生产沟通、包装、CAD、工程图、工业设计，再读：

```text
D:\image2专业提示词库\indexes\IMAGE2_PRODUCTION_SCENARIO_INDEX.md
```

只有索引命中具体方向后，才打开对应 prompt 文件，例如：

- `IMAGE2_POSTER_KV_PRO_TEMPLATES.md`
- `IMAGE2_PRODUCT_VISUAL_PRO_TEMPLATES.md`
- `IMAGE2_PACKAGING_PRO_TEMPLATES.md`
- `IMAGE2_CAD_TECHNICAL_PRO_TEMPLATES.md`

这就是它低 token 的核心原因之一。

### 3. 脚本快速路由

`scripts/route_ai_workflow.py` 可以对短请求做快速初筛，返回最可能的路线和应读取的文件。

例如用户说：

```text
帮我把这个 skill 介绍写得更吸引人，并用 image2 画宣传海报
```

路由结果会优先指向：

- image creative generation
- GitHub/Codex/OpenAI 发布流程
- prompt-template / 文案优化

这比人工在几十个矩阵里翻找更快，也更节省上下文。

### 4. 主 skill 不承载所有知识

`SKILL.md` 不负责装下所有提示词、所有领域知识和所有模板。它只负责：

- 判断要做什么
- 判断该读什么
- 判断该调用什么
- 判断完成标准是什么

真正的长知识留在 references 和外部提示词库里，按需读取。

## 低 token 消耗承诺

这个 skill 明确强调低 token 消耗。

它不会每次都读取完整提示词库。

它不会每次都读取全部专业矩阵。

它不会为了一个小任务加载一整套领域手册。

默认策略是：

1. 先读最小入口
   - 只用 `SKILL.md` 和必要的总索引判断方向。

2. 再读命中的最小文件
   - 只打开当前任务真正需要的 reference 或 prompt。

3. 能用脚本筛选就先筛选
   - 用 `route_ai_workflow.py` 得到候选路线，再决定是否读更长文档。

4. 能用现有能力就不重写
   - 已有 skill、插件、脚本、索引能解决，就不再生成一套泛化流程。

5. 介绍文档不进默认执行路径
   - 这份中文介绍只在用户要求解释、发布、展示或写文档时读取。正常执行任务时不需要加载它。

这让它更像一个高效的“任务调度台”，而不是一个每次全量展开的“超级提示词仓库”。

## 一个完整例子

用户说：

```text
帮我从网上搜集所有专业提示词，分门别类，写好索引。
```

skill 不会立刻开始无边界搜索，而会先拆成：

1. 明确范围：哪些行业、哪些模型、哪些输出形式。
2. 能力扫描：是否已有本地提示词库、搜索脚本、分类索引、浏览能力。
3. 建立分类法：按行业、任务、输入材料、输出物、验收标准分类。
4. 采集和去重：只保留可复用、可验证、专业度高的提示词。
5. 建索引：让后续任务先读索引再读模板。
6. 验收：检查覆盖范围、重复度、可检索性和示例质量。

用户说：

```text
我要 image2 输出专业包装 CAD 图纸提示词。
```

skill 会先读 image2 索引，再命中包装/CAD 专项模板，而不是打开整个提示词库。然后生成一个带结构、视图、尺寸标注、折线/切线、负面提示和验收清单的 prompt packet。

用户说：

```text
帮我扫描我已安装的插件和 skill，看看还能怎么提高能力。
```

skill 会先做 capability inventory，再区分：

- 已安装可用能力
- 当前会话可调用能力
- 可以安装但还没安装的插件
- 这个任务真正值得调用的能力
- 不建议调用的能力及原因

## 适合放在 GitHub README 的宣传文案

`task-prompt-orchestrator` turns messy requests into execution-ready workflows.

它像 Codex 的任务调度台：先收集输入，再扫描能力，然后用最小上下文找到最专业的执行路径。

它适合需要“先规划、再执行、最后验证”的任务，也适合大型提示词库、image2 工作流、插件调用、GitHub 发布、文档生成、研究分析和多步骤自动化。

最重要的是，它不是靠暴力读取完整提示词库来工作，而是靠索引、路由和渐进式加载来节省 token。

## 对用户的承诺

- 先扫描现有能力，再设计新流程。
- 先整理输入信息，再写提示词。
- 先选工作流，再拆步骤。
- 先用索引缩小范围，再读具体模板。
- 先执行和验证，再宣布完成。
- 保持低 token 消耗，不默认读取完整提示词库。

## 推荐调用方式

```text
Use $task-prompt-orchestrator to collect my goal, inputs, constraints, available skills/plugins, and acceptance checks, then route it through the smallest useful workflow and execute or produce prompt packets.
```

中文调用：

```text
使用 task-prompt-orchestrator：先收集我的目标、输入材料、约束、当前可用插件和 skill、验收标准，再选择最小可用工作流并执行。
```

更适合新手的调用：

```text
请用 task-prompt-orchestrator 帮我把这个需求拆成可以执行的步骤。先检查现成能力，只问真正阻塞的问题，然后给我一个可复制、可执行、可验证的工作流。
```
