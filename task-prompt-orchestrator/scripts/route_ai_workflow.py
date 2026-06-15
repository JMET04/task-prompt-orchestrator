#!/usr/bin/env python3
"""Suggest the smallest workflow references for an AI task request."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Route:
    id: str
    zone: str
    tier: str
    keywords: tuple[str, ...]
    read_next: tuple[str, ...]
    plugin_hint: str
    fallback: str


@dataclass(frozen=True)
class StarterPack:
    id: str
    name: str
    keywords: tuple[str, ...]
    read_next: str


STARTER_PACKS: tuple[StarterPack, ...] = (
    StarterPack("SP01", "First Useful Ask", ("ask", "how to ask", "beginner", "小白", "怎么问", "不会问"), "references/ai_beginner_starter_packs.md#sp01-first-useful-ask"),
    StarterPack("SP02", "Turn Goal Into Plan", ("goal", "plan", "idea", "workflow", "目标", "计划", "想法", "工作流"), "references/ai_beginner_starter_packs.md#sp02-turn-goal-into-plan"),
    StarterPack("SP03", "Research With Sources", ("research", "source", "citation", "compare", "调研", "研究", "资料", "引用", "对比"), "references/ai_beginner_starter_packs.md#sp03-research-with-sources"),
    StarterPack("SP04", "Write Or Rewrite", ("write", "rewrite", "summarize", "polish", "写", "写作", "改写", "总结", "润色"), "references/ai_beginner_starter_packs.md#sp04-write-or-rewrite"),
    StarterPack("SP05", "Image Or Visual Prompt", ("image", "image2", "visual", "cad", "packaging", "图片", "包装", "图纸", "视觉"), "references/ai_beginner_starter_packs.md#sp05-image-or-visual-prompt"),
    StarterPack("SP06", "Code Or App Help", ("code", "build", "app", "bug", "repo", "代码", "开发", "应用", "修复"), "references/ai_beginner_starter_packs.md#sp06-code-or-app-help"),
    StarterPack("SP07", "Data Or Spreadsheet", ("data", "spreadsheet", "dashboard", "report", "数据", "表格", "报表", "指标"), "references/ai_beginner_starter_packs.md#sp07-data-or-spreadsheet"),
    StarterPack("SP08", "Office Output", ("slide", "doc", "email", "meeting", "ppt", "文档", "邮件", "会议"), "references/ai_beginner_starter_packs.md#sp08-office-output"),
    StarterPack("SP09", "Marketing Content", ("marketing", "ad", "post", "sales copy", "营销", "广告", "文案", "种草"), "references/ai_beginner_starter_packs.md#sp09-marketing-content"),
    StarterPack("SP10", "Learn Something", ("learn", "study", "teach", "tutor", "学习", "教我", "复习", "教程"), "references/ai_beginner_starter_packs.md#sp10-learn-something"),
    StarterPack("SP11", "Automate Or Use Plugins", ("automate", "plugin", "install", "tool", "自动化", "插件", "安装", "工具"), "references/ai_beginner_starter_packs.md#sp11-automate-or-use-plugins"),
    StarterPack("SP12", "Review And Improve", ("review", "improve", "check", "evaluate", "检查", "优化", "评估", "改进"), "references/ai_beginner_starter_packs.md#sp12-review-and-improve"),
)


ROUTES: tuple[Route, ...] = (
    Route(
        id="beginner-ai-control",
        zone="Beginner AI control and prompt habits",
        tier="T1",
        keywords=("beginner", "new to ai", "learn ai", "teach me", "how to ask", "小白", "新手", "学习", "怎么问", "上手", "控制ai"),
        read_next=("references/ai_beginner_starter_packs.md", "references/ai_beginner_workflows.md"),
        plugin_hint="Use built-in skill guidance first; no plugin is required.",
        fallback="Return a compact Goal/Context/Task/Output/Review prompt packet.",
    ),
    Route(
        id="capability-plugin-routing",
        zone="Capability scan, plugin selection, and install boundary",
        tier="T1",
        keywords=("plugin", "install", "connector", "skill scan", "capability", "mcp", "插件", "安装", "能力", "扫描", "skill"),
        read_next=(
            "references/professional_workflow_capability_discovery_matrix.md",
            "references/professional_workflow_plugin_skill_scan_auto_install_matrix.md",
            "references/common_plugin_directory.md",
        ),
        plugin_hint="Check visible tools first; request plugin installation only for exact matches and explicit install intent.",
        fallback="Use local skills, scripts, web sources, and user-provided files with the limitation labeled.",
    ),
    Route(
        id="github-codex-openai",
        zone="GitHub, Codex, OpenAI, repository, security, and delivery workflow",
        tier="T1",
        keywords=("github", "codex", "openai", "repo", "pull request", "pr", "ci", "agents sdk", "api key", "代码仓库", "仓库", "接口", "安全"),
        read_next=("references/github_codex_common_plugin_directory.md",),
        plugin_hint="Prefer GitHub, OpenAI Developers, Codex Security, Superpowers, or Build Web Apps when exact and available.",
        fallback="Use local git, repo files, official docs, local tests, or pasted issue/PR text.",
    ),
    Route(
        id="code-app-build",
        zone="Code, app building, debugging, testing, and developer delivery",
        tier="T2",
        keywords=("code", "coding", "build app", "web app", "frontend", "backend", "debug", "test", "代码", "写代码", "开发", "应用", "app", "修复", "调试", "测试"),
        read_next=(
            "references/professional_workflow_testing_simulation_matrix.md",
            "references/professional_workflow_release_distribution_matrix.md",
            "references/github_codex_common_plugin_directory.md",
        ),
        plugin_hint="Use local repo tools first; prefer GitHub, Build Web Apps, OpenAI Developers, Codex Security, Vercel, Netlify, Render, or Cloudflare when exact and available.",
        fallback="Use local files, package scripts, tests, browser checks, and a small implementation plan.",
    ),
    Route(
        id="prompt-template",
        zone="Prompt engineering, reusable prompt packets, and prompt-library design",
        tier="T1",
        keywords=("prompt", "template", "prompt library", "prompt packet", "提示词", "提示词库", "模板", "提示包"),
        read_next=("references/professional_prompt_pattern_matrix.md", "references/prompt_templates.md"),
        plugin_hint="No plugin required unless the prompt targets a specific connected app or model platform.",
        fallback="Use the skill prompt packet format with role, objective, context, procedure, output, and checks.",
    ),
    Route(
        id="image-creative-generation",
        zone="Image2, creative generation, CAD/packaging visuals, and media assets",
        tier="T1",
        keywords=("image", "image2", "visual", "cad", "packaging", "render", "design asset", "图片", "包装", "图纸", "视觉", "渲染"),
        read_next=(
            "references/professional_workflow_brand_creative_design_asset_production_matrix.md",
            "D:/image2专业提示词库/indexes/IMAGE2_VERTICAL_PROMPT_INDEX.md",
            "D:/image2专业提示词库/indexes/IMAGE2_PRODUCTION_SCENARIO_INDEX.md",
        ),
        plugin_hint="Use imagegen, Creative Production, Fal, Picsart, Shutterstock, Canva, or Figma when visible and task-fit.",
        fallback="Produce a structured image prompt with subject, reference, style, camera/view, callouts, materials, constraints, and negatives.",
    ),
    Route(
        id="ai-app-agent-modelops",
        zone="AI apps, agents, RAG, tool calling, evals, and model operations",
        tier="T2",
        keywords=("agent", "rag", "tool calling", "eval", "model ops", "llm app", "automation runner", "智能体", "评测", "自动化", "工作流自动化"),
        read_next=(
            "references/professional_workflow_ai_llm_application_model_ops_matrix.md",
            "references/professional_workflow_agentic_automation_tool_governance_matrix.md",
        ),
        plugin_hint="Prefer OpenAI Developers, Cloudflare, Vercel, GitHub, Build Web Apps, or Codex Security when exact and available.",
        fallback="Design a local prompt/tool workflow with explicit state, tool permissions, evals, and rollback.",
    ),
    Route(
        id="research-evidence",
        zone="Source-backed research, evidence synthesis, and citations",
        tier="T1",
        keywords=("research", "source", "citation", "evidence", "market research", "literature", "调研", "研究", "资料", "引用", "证据", "文献"),
        read_next=(
            "references/professional_workflow_source_evidence_matrix.md",
            "references/professional_workflow_research_analysis_knowledge_synthesis_matrix.md",
        ),
        plugin_hint="Use web, Google Drive, Zotero, Hebbia, or domain research plugins when the task and access require them.",
        fallback="Use authoritative web/source-backed research with explicit dates and uncertainty labels.",
    ),
    Route(
        id="data-analytics",
        zone="Data, spreadsheets, KPI reports, dashboards, and BI governance",
        tier="T2",
        keywords=("data", "spreadsheet", "dashboard", "kpi", "analytics", "bi", "dataset", "数据", "表格", "仪表盘", "报表", "指标"),
        read_next=(
            "references/professional_workflow_data_lifecycle_retention_matrix.md",
            "references/professional_workflow_data_product_bi_semantic_governance_matrix.md",
        ),
        plugin_hint="Use Data Analytics, Spreadsheets, Deepnote, Supabase, Neon Postgres, or Documents when visible and task-fit.",
        fallback="Analyze local files with scripts, then produce tables/charts and source-backed definitions.",
    ),
    Route(
        id="business-growth",
        zone="Product, marketing, sales, customer success, and business strategy",
        tier="T2",
        keywords=("product", "marketing", "sales", "customer success", "strategy", "growth", "商业", "营销", "销售", "产品", "增长"),
        read_next=(
            "references/professional_workflow_product_management_roadmap_feedback_matrix.md",
            "references/professional_workflow_content_operations_editorial_distribution_matrix.md",
            "references/professional_workflow_customer_success_account_retention_matrix.md",
        ),
        plugin_hint="Use Sales, Product Design, Data Analytics, Notion, or CRM-like connectors when visible and relevant.",
        fallback="Use a structured business workflow with audience, offer, channel, evidence, metrics, and next action.",
    ),
    Route(
        id="high-risk",
        zone="Legal, finance, health, safety, privacy, compliance, and regulated tasks",
        tier="T2",
        keywords=("legal", "compliance", "finance", "tax", "medical", "health", "safety", "privacy", "法律", "合规", "金融", "税", "医疗", "隐私", "安全"),
        read_next=(
            "references/professional_high_risk_validation_matrix.md",
            "references/professional_workflow_source_evidence_matrix.md",
            "references/detailed_template_routing_directory.md",
        ),
        plugin_hint="Use exact domain plugins only when visible and authenticated; preserve professional handoff boundaries.",
        fallback="Provide organization, evidence, questions, and handoff preparation rather than professional advice.",
    ),
    Route(
        id="personal-life-admin",
        zone="Personal life administration and household workflows",
        tier="T2",
        keywords=("personal", "household", "family", "travel", "records", "life admin", "个人", "家庭", "生活", "证件", "行程", "记录"),
        read_next=("references/detailed_template_routing_directory.md",),
        plugin_hint="Use calendar, drive, documents, email, or travel/commerce connectors only when visible and task-fit.",
        fallback="Route to the exact personal `professional_workflow_personal_*_matrix.md` file after intent is clear.",
    ),
    Route(
        id="coverage-audit",
        zone="Library coverage, workflow expansion, and directory architecture",
        tier="T3",
        keywords=("coverage", "audit", "index", "expand", "directory", "architecture", "complete", "覆盖", "索引", "目录", "扩展", "完整", "数量级"),
        read_next=("references/professional_workflow_dimension_index.md", "scripts/validate_workflow_library.py"),
        plugin_hint="Use local validators and inventory scripts first.",
        fallback="Report verified counts, gaps, and next coverage lanes.",
    ),
)


def score_route(route: Route, query: str) -> int:
    q = query.casefold()
    return sum(1 for keyword in route.keywords if keyword.casefold() in q)


def route_by_id(route_id: str) -> Route:
    return next(route for route in ROUTES if route.id == route_id)


def suggest(query: str, top: int) -> list[dict[str, object]]:
    ranked = sorted(
        ((score_route(route, query), route) for route in ROUTES),
        key=lambda item: (-item[0], item[1].id),
    )
    matches = [(score, route) for score, route in ranked if score > 0]
    if not matches:
        matches = [
            (0, route_by_id("beginner-ai-control")),
            (0, route_by_id("prompt-template")),
            (0, route_by_id("coverage-audit")),
        ]
    return [
        {
            "score": score,
            **asdict(route),
        }
        for score, route in matches[:top]
    ]


def choose_starter_pack(query: str, route: Route) -> StarterPack:
    q = query.casefold()
    forced_by_route = {
        "capability-plugin-routing": "SP11",
        "github-codex-openai": "SP11",
        "code-app-build": "SP06",
        "image-creative-generation": "SP05",
        "ai-app-agent-modelops": "SP11",
        "research-evidence": "SP03",
        "data-analytics": "SP07",
        "business-growth": "SP09",
        "high-risk": "SP03",
        "personal-life-admin": "SP02",
        "coverage-audit": "SP12",
    }
    if route.id in forced_by_route:
        return next(pack for pack in STARTER_PACKS if pack.id == forced_by_route[route.id])
    if any(keyword in q for keyword in ("research", "source", "citation", "调研", "研究", "引用", "文献")):
        return next(pack for pack in STARTER_PACKS if pack.id == "SP03")
    ranked = sorted(
        ((sum(1 for keyword in pack.keywords if keyword.casefold() in q), pack) for pack in STARTER_PACKS),
        key=lambda item: (-item[0], item[1].id),
    )
    if ranked and ranked[0][0] > 0:
        return ranked[0][1]
    defaults = {"beginner-ai-control": "SP01", "prompt-template": "SP01"}
    default_id = defaults.get(route.id, "SP01")
    return next(pack for pack in STARTER_PACKS if pack.id == default_id)


def required_inputs_for(route: Route) -> list[str]:
    common = [
        "goal or desired deliverable",
        "available files, links, examples, or source material",
        "audience, format, constraints, deadline, and quality bar",
    ]
    by_route = {
        "capability-plugin-routing": [
            "current visible tools/plugins/skills if known",
            "whether the user explicitly wants missing plugins installed",
        ],
        "github-codex-openai": [
            "repository, branch, issue, PR, CI, API, or security context",
            "whether private GitHub/OpenAI access is visible in the session",
        ],
        "code-app-build": [
            "repository or project path, stack, target feature/bug, commands, logs, and test expectations",
            "whether the task requires UI/browser verification, deployment, or external service access",
        ],
        "image-creative-generation": [
            "product/object details, dimensions, materials, labels, view angle, and reference images",
            "target generator or output type: prompt only, image, CAD-like drawing, or production callout",
        ],
        "research-evidence": [
            "research question, geography, time freshness, source type, and citation style",
        ],
        "data-analytics": [
            "dataset path/source, metric definitions, grain, filters, and desired chart/report format",
        ],
        "high-risk": [
            "jurisdiction/context, source authority needs, risk boundary, and professional handoff requirement",
        ],
        "coverage-audit": [
            "scope to audit, expected counts if known, and whether to update indexes or only report gaps",
        ],
    }
    return common + by_route.get(route.id, [])


def output_contract_for(route: Route) -> str:
    contracts = {
        "beginner-ai-control": "A beginner-safe prompt packet plus the next 1-3 actions.",
        "capability-plugin-routing": "A capability decision packet with enabled route, exact install candidate if authorized, fallback, and verification.",
        "github-codex-openai": "A GitHub/Codex/OpenAI route decision with exact plugin/tool choice, fallback, and execution plan.",
        "code-app-build": "A coding/app execution packet with implementation steps, files or commands to inspect, verification, and remaining risks.",
        "prompt-template": "A reusable prompt template with role, context, task, output format, constraints, examples, and checks.",
        "image-creative-generation": "A generation-ready visual prompt with subject, structure, materials, labels/callouts, view, style, constraints, and negatives.",
        "ai-app-agent-modelops": "An AI workflow architecture with tool permissions, state, evals, guardrails, deployment/ops checks, and rollback.",
        "research-evidence": "A source-backed evidence plan or answer with dates, citations, uncertainty labels, and synthesis.",
        "data-analytics": "An analysis/report plan with source table, metric logic, charts/tables, assumptions, and validation checks.",
        "business-growth": "A business workflow with audience, offer/problem, channel, evidence, metrics, and next actions.",
        "high-risk": "A bounded organization/evidence/handoff packet that avoids replacing licensed or official advice.",
        "personal-life-admin": "A personal admin checklist or workflow with records, deadlines, communication drafts, privacy, and handoff.",
        "coverage-audit": "A verified coverage report with counts, route gaps, index status, and next expansion lanes.",
    }
    return contracts.get(route.id, "An execution-ready workflow packet with inputs, steps, output, checks, and fallback.")


def safety_boundary_for(route: Route) -> str:
    if route.id in {"high-risk", "personal-life-admin"}:
        return "Use organization, evidence, checklists, and handoff support; do not replace legal, medical, financial, safety, tax, or official decisions."
    if route.id in {"capability-plugin-routing", "github-codex-openai"}:
        return "Do not claim unavailable private access or install plugins without explicit intent and an exact install candidate."
    if route.id == "code-app-build":
        return "Use existing project patterns, avoid unrelated rewrites, preserve user changes, and verify with tests or runtime evidence."
    if route.id == "image-creative-generation":
        return "Preserve IP, trademark, likeness, safety, and production-validity boundaries; label CAD-like visuals as prompts unless real CAD output is produced."
    if route.id == "research-evidence":
        return "Use authoritative sources, explicit dates, and uncertainty labels; browse when freshness or citations matter."
    return "State assumptions, avoid unsupported claims, and verify against the requested output contract."


def verification_for(route: Route) -> str:
    checks = {
        "beginner-ai-control": "The user can copy the prompt and knows the next action.",
        "capability-plugin-routing": "The selected capability is visible/callable or the fallback limitation is labeled.",
        "github-codex-openai": "The route uses visible tools/plugins or a local/git fallback with evidence.",
        "code-app-build": "The change plan or implementation names files, commands, tests, runtime checks, and unresolved risks.",
        "prompt-template": "The prompt contains goal, context, task, output format, constraints, and quality checks.",
        "image-creative-generation": "The prompt includes inspectable geometry, materials, labels, view, constraints, and negative instructions.",
        "ai-app-agent-modelops": "The workflow defines tools, permissions, state, evals, monitoring, and recovery.",
        "research-evidence": "Every key claim has a source or is labeled as inference/unknown.",
        "data-analytics": "Metrics, filters, grain, and source assumptions are explicit and reproducible.",
        "business-growth": "The output names audience, value proposition, channel, metric, and next step.",
        "high-risk": "The output has clear boundaries, sources, uncertainty, and professional/official handoff where needed.",
        "personal-life-admin": "The workflow captures deadlines, documents, privacy, communications, and next action.",
        "coverage-audit": "Validator output or file evidence proves counts, route coverage, and gaps.",
    }
    return checks.get(route.id, "The output satisfies the contract and names remaining unknowns.")


def build_activation_packet(query: str, route: Route, score: int) -> dict[str, object]:
    read_next = list(route.read_next)
    starter_pack = choose_starter_pack(query, route)
    if starter_pack.read_next not in read_next:
        read_next.append(starter_pack.read_next)
    next_actions = [
        f"Read or inspect: {read_next[0]}" if read_next else "Use the selected route without extra reference loading.",
        f"Use starter pack: {starter_pack.id} {starter_pack.name}.",
        "Ask only for blocking missing inputs; otherwise execute the first useful step.",
        "Verify against the output contract before claiming completion.",
    ]
    packet = {
        "user_intent": query,
        "route_id": route.id,
        "score": score,
        "activation_tier": route.tier,
        "prompt_zone": route.zone,
        "read_next": read_next,
        "starter_pack": asdict(starter_pack),
        "skill_tool_plugin_route": route.plugin_hint,
        "required_inputs": required_inputs_for(route),
        "output_contract": output_contract_for(route),
        "safety_authority_boundary": safety_boundary_for(route),
        "verification": verification_for(route),
        "fallback": route.fallback,
        "next_actions": next_actions,
    }
    packet["copyable_prompt"] = (
        "Role: You are an AI workflow router and prompt architect.\n"
        f"Goal: Help me complete this request: {query}\n"
        f"Route: Use {route.zone} ({route.tier}).\n"
        f"Starter pack: Use {starter_pack.id} {starter_pack.name}.\n"
        f"Read next if needed: {', '.join(read_next) if read_next else 'no extra reference'}.\n"
        "Procedure: first check existing skills/plugins/tools; ask only blocking questions; then produce or execute the smallest useful workflow.\n"
        f"Output: {packet['output_contract']}\n"
        f"Safety boundary: {packet['safety_authority_boundary']}\n"
        f"Verify: {packet['verification']}"
    )
    return packet


def suggest_with_packets(query: str, top: int) -> list[dict[str, object]]:
    suggestions = suggest(query, top)
    packets: list[dict[str, object]] = []
    for item in suggestions:
        route = next(route for route in ROUTES if route.id == item["id"])
        packet = build_activation_packet(query, route, int(item["score"]))
        packets.append(packet)
    return packets


def render_markdown_route(item: dict[str, object]) -> str:
    read_next = "\n".join(f"- `{ref}`" for ref in item.get("read_next", []))
    return (
        f"## {item['id']}\n\n"
        f"- Zone: {item['zone']}\n"
        f"- Tier: {item['tier']}\n"
        f"- Score: {item['score']}\n"
        f"- Plugin/tool route: {item['plugin_hint']}\n"
        f"- Fallback: {item['fallback']}\n\n"
        f"Read next:\n{read_next if read_next else '- None'}"
    )


def render_markdown_packet(packet: dict[str, object]) -> str:
    read_next = "\n".join(f"- `{ref}`" for ref in packet["read_next"])
    required_inputs = "\n".join(f"- {item}" for item in packet["required_inputs"])
    next_actions = "\n".join(f"{index + 1}. {item}" for index, item in enumerate(packet["next_actions"]))
    starter = packet["starter_pack"]
    return (
        f"# AI Activation Packet\n\n"
        f"**User intent:** {packet['user_intent']}\n\n"
        f"**Route:** `{packet['route_id']}` ({packet['activation_tier']})\n\n"
        f"**Prompt zone:** {packet['prompt_zone']}\n\n"
        f"**Starter pack:** {starter['id']} {starter['name']}\n\n"
        f"## Read Next\n\n{read_next}\n\n"
        f"## Required Inputs\n\n{required_inputs}\n\n"
        f"## Output Contract\n\n{packet['output_contract']}\n\n"
        f"## Tool / Plugin Route\n\n{packet['skill_tool_plugin_route']}\n\n"
        f"## Safety Boundary\n\n{packet['safety_authority_boundary']}\n\n"
        f"## Verification\n\n{packet['verification']}\n\n"
        f"## Fallback\n\n{packet['fallback']}\n\n"
        f"## Next Actions\n\n{next_actions}\n\n"
        f"## Copyable Prompt\n\n```text\n{packet['copyable_prompt']}\n```"
    )


def render_markdown(payload: object, packet_mode: bool, list_mode: bool) -> str:
    if list_mode:
        rows = ["| Route | Tier | Zone |", "|---|---|---|"]
        for item in payload:
            rows.append(f"| `{item['id']}` | {item['tier']} | {item['zone']} |")
        return "\n".join(rows)
    items = payload if isinstance(payload, list) else [payload]
    if packet_mode:
        return "\n\n---\n\n".join(render_markdown_packet(item) for item in items)
    return "\n\n---\n\n".join(render_markdown_route(item) for item in items)


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest low-cost workflow routes for an AI task.")
    parser.add_argument("query", nargs="*", help="User task or intent to route.")
    parser.add_argument("--top", type=int, default=3, help="Number of route suggestions to return.")
    parser.add_argument("--list", action="store_true", help="List all route ids and zones.")
    parser.add_argument("--packet", action="store_true", help="Return beginner-friendly activation packets instead of route summaries.")
    parser.add_argument("--format", choices=("json", "markdown"), default="json", help="Output format.")
    args = parser.parse_args()

    if args.list:
        payload: object = [{"id": route.id, "zone": route.zone, "tier": route.tier} for route in ROUTES]
    else:
        query = " ".join(args.query).strip()
        if not query:
            parser.error("provide a query or use --list")
        payload = suggest_with_packets(query, max(1, args.top)) if args.packet else suggest(query, max(1, args.top))

    if args.format == "markdown":
        print(render_markdown(payload, args.packet, args.list))
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
