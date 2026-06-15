# Image2 Poster Prompt

This poster uses the image2 poster/KV workflow:

- Route from `IMAGE2_VERTICAL_PROMPT_INDEX.md`
- Category: `prompts/IMAGE2_POSTER_KV_PRO_TEMPLATES.md`
- Scene: brand image poster / campaign key visual
- Text policy: generate the visual background without readable text, then add real text locally

## Background Generation Prompt

```text
Use case: ads-marketing
Asset type: promotional poster background for a Codex skill / developer workflow tool
Primary request: Create a premium vertical promotional poster background for an AI workflow orchestration skill called Task Prompt Orchestrator. No readable text, no fake letters, no logos, no watermark. Leave clean empty regions for later typography: a large title area at the top left, three feature callout zones in the middle, and a CTA strip at the bottom.
Scene/backdrop: a sophisticated developer workspace transformed into an abstract command center: floating workflow cards, connected nodes, plugin tiles, prompt packets, a subtle GitHub repository panel, a lightweight token meter, and an image-generation panel. Make it feel like a smart routing dashboard, not a generic AI robot.
Subject: central luminous orchestration hub made of layered translucent cards and fine connection lines, showing the idea of messy requests becoming structured workflows.
Style/medium: high-end tech campaign key visual, clean editorial poster design, premium SaaS launch visual, crisp 3D glassmorphism mixed with flat UI panels.
Composition/framing: vertical 4:5 poster, strong central focus, safe margins, readable empty panels for later Chinese typography, balanced negative space, no clutter.
Lighting/mood: confident, precise, energetic, calm intelligence; soft studio glow, subtle depth, sharp details.
Color palette: deep graphite, clean white, electric cyan, warm amber highlights, small accents of green for low-token efficiency; avoid a one-note purple/blue gradient.
Materials/textures: matte glass panels, precise thin lines, subtle paper-like prompt cards, polished product-launch finish.
Constraints: no readable text, no random characters, no brand logos, no QR code, no people, no animals, no messy cyberpunk clutter, no fake UI text, no watermark. Leave intentional blank areas for real text overlay.
```

## Overlay Copy

```text
Task Prompt Orchestrator
低 token 工作流调度台
把模糊需求变成可执行、可验证、可交接的专业工作流
先扫描能力 · 再选择最小索引 · 最后生成提示词包

01 收集输入
目标、文件、约束、权限、验收标准先归位

02 路由能力
优先调用已安装 skill、插件、脚本和索引

03 节省 token
不全量读取提示词库，只加载命中的最小文件

适合：image2 工作流 · GitHub 发布 · 插件扫描 · 多步骤自动化 · 专业提示词库路由
Use $task-prompt-orchestrator → smallest useful workflow, verified output
```
