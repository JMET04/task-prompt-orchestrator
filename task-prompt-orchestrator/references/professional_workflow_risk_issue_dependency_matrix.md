# Professional Workflow Risk Issue Dependency Matrix

Use this matrix when a workflow needs proactive risk management, issue tracking, dependency control, assumption tracking, escalation, contingency planning, residual-risk decisions, or risk communication across projects, operations, research, production, publishing, compliance, engineering, creative delivery, CAD/package work, data pipelines, or prompt-library expansion.

## Risk Scope

| Code | Risk question | Workflow use |
|---|---|---|
| RISKSCOP01 | What outcome could fail or be harmed? | Anchor risk management to the goal, user impact, business impact, safety, compliance, quality, or delivery promise. |
| RISKSCOP02 | What risk categories apply? | Classify scope, schedule, cost, quality, source, tool, data, security, legal, people, vendor, adoption, and operational risks. |
| RISKSCOP03 | What risk time horizon matters? | Separate immediate execution risks, release risks, operational risks, long-term maintenance risks, and strategic risks. |
| RISKSCOP04 | What risk boundary is in scope? | Include only risks the workflow can monitor, mitigate, escalate, accept, transfer, or communicate. |
| RISKSCOP05 | What risk boundary is out of scope? | Exclude unrelated business, personal, market, or system risks unless they affect the workflow decision. |
| RISKSCOP06 | What stakeholder bears the risk? | Identify user, client, operator, reviewer, approver, public audience, vendor, team, or downstream system impact. |
| RISKSCOP07 | What risk tolerance applies? | Define low, moderate, high, zero-tolerance, regulated, safety-critical, or experimental tolerance. |
| RISKSCOP08 | What risk evidence is needed? | Use logs, tests, source evidence, expert review, history, dependency status, metrics, or audit findings. |
| RISKSCOP09 | What risk should be explicitly ignored? | Document intentionally accepted low-value or impossible-to-control risks to prevent distraction. |
| RISKSCOP10 | What risk scope artifact should be produced? | Leave a risk-scope note listing categories, stakeholders, tolerance, evidence, and boundaries. |

## Risk Register

| Code | Risk question | Workflow use |
|---|---|---|
| RISKREG01 | What risks must be listed before execution? | Create a concise register of material risks before irreversible, high-volume, public, or regulated work. |
| RISKREG02 | What unique ID should each risk have? | Use stable IDs so risks can be referenced in plans, decisions, alerts, and postmortems. |
| RISKREG03 | What owner does each risk need? | Assign responsible owner, accountable approver, monitor, and escalation contact. |
| RISKREG04 | What trigger or early warning indicates the risk is emerging? | Define signal, threshold, event, missed date, failed test, source change, or stakeholder concern. |
| RISKREG05 | What current status should each risk have? | Track proposed, open, watching, mitigating, escalated, accepted, closed, or realized. |
| RISKREG06 | What response strategy applies? | Choose avoid, reduce, transfer, accept, monitor, defer, or escalate. |
| RISKREG07 | What mitigation action is committed? | Record concrete action, owner, due date, expected effect, and evidence. |
| RISKREG08 | What contingency action is ready? | Record fallback, workaround, rollback, alternate source, alternate owner, or degraded mode. |
| RISKREG09 | What residual risk remains? | Keep remaining probability, impact, uncertainty, owner, and acceptance decision. |
| RISKREG10 | What risk-register QA check is required? | Verify every high risk has owner, trigger, mitigation, contingency, and review cadence. |

## Probability And Impact

| Code | Risk question | Workflow use |
|---|---|---|
| RISKPI01 | How likely is the risk? | Rate probability with evidence, history, dependency health, complexity, or uncertainty. |
| RISKPI02 | What impact would the risk have? | Rate impact on user, schedule, cost, quality, legal, security, safety, reputation, and operations. |
| RISKPI03 | What severity score should be used? | Combine probability and impact using simple low/medium/high or numeric scoring. |
| RISKPI04 | What risk velocity matters? | Identify how quickly the risk can become an issue and how much warning time exists. |
| RISKPI05 | What detectability matters? | Rate whether the workflow can detect the risk before damage occurs. |
| RISKPI06 | What uncertainty affects scoring? | Mark unknown evidence, ambiguous sources, missing metrics, or untested assumptions. |
| RISKPI07 | What compound impact exists? | Account for risks that trigger other risks or affect multiple workstreams. |
| RISKPI08 | What impact threshold requires escalation? | Escalate severe, irreversible, regulated, customer-impacting, or safety-related risks. |
| RISKPI09 | What low-probability high-impact risk must still be handled? | Add contingency for rare but severe outcomes rather than ignoring them. |
| RISKPI10 | What probability/impact artifact should be produced? | Produce a risk heat map, ranked table, or priority list with scoring rationale. |

## Mitigation Planning

| Code | Risk question | Workflow use |
|---|---|---|
| MITPLAN01 | What can reduce the probability of this risk? | Add preventive actions such as validation, review, automation, training, narrowing scope, or better source selection. |
| MITPLAN02 | What can reduce the impact of this risk? | Add rollback, isolation, staging, backups, sampling, limits, communication, or phased rollout. |
| MITPLAN03 | What mitigation is most cost-effective? | Compare effort, time, cost, complexity, and expected risk reduction. |
| MITPLAN04 | What mitigation must happen before execution? | Gate risky work on backup, approval, dry run, test, source verification, or permission check. |
| MITPLAN05 | What mitigation can happen during execution? | Monitor thresholds, sample outputs, review batches, pause on anomaly, or route exceptions. |
| MITPLAN06 | What mitigation can happen after release? | Add monitoring, feedback loops, support scripts, hotfix path, or scheduled review. |
| MITPLAN07 | What mitigation creates new risks? | Check added complexity, delay, cost, privacy exposure, dependency, or operational burden. |
| MITPLAN08 | What mitigation owner and deadline are needed? | Assign accountable action, due date, acceptance evidence, and follow-up point. |
| MITPLAN09 | What mitigation evidence proves completion? | Require test result, checklist, reviewed file, approval, metric, or run log. |
| MITPLAN10 | What mitigation plan should be archived? | Keep action, owner, date, evidence, risk reduction, and remaining risk. |

## Contingency Planning

| Code | Risk question | Workflow use |
|---|---|---|
| CONTPLAN01 | What fallback path exists if the risk realizes? | Define alternate source, alternate tool, manual path, degraded mode, delay, rollback, or replacement workflow. |
| CONTPLAN02 | What trigger activates contingency? | Use failed validation, missed deadline, incident severity, cost cap, quality threshold, or access loss. |
| CONTPLAN03 | Who decides to activate contingency? | Assign decision owner, escalation path, and required evidence. |
| CONTPLAN04 | What resources must be reserved? | Reserve time, budget, backup owner, alternate tool, support channel, or emergency window. |
| CONTPLAN05 | What data or artifact must be backed up? | Preserve source, package, previous version, manifest, config, logs, and approval records. |
| CONTPLAN06 | What communication is needed when contingency activates? | Notify affected users, stakeholders, support, clients, reviewers, and owners. |
| CONTPLAN07 | What contingency has been tested? | Run tabletop, dry run, restore test, sample fallback, or rollback rehearsal. |
| CONTPLAN08 | What contingency is only theoretical? | Label untested fallback and avoid relying on it for high-risk decisions. |
| CONTPLAN09 | What contingency exit condition applies? | Define when to return to normal, continue degraded mode, or close the issue. |
| CONTPLAN10 | What contingency artifact should be produced? | Keep trigger, decision owner, steps, resources, communication, validation, and exit criteria. |

## Issue Management

| Code | Risk question | Workflow use |
|---|---|---|
| ISSUEMGT01 | What realized problem must be tracked as an issue? | Convert actual blockers, defects, incidents, missed dependencies, and failures into issue records. |
| ISSUEMGT02 | What severity does the issue have? | Classify by impact, urgency, affected users, compliance, safety, reversibility, and deadline risk. |
| ISSUEMGT03 | What issue owner is accountable? | Assign owner, responder, reviewer, approver, and escalation contact. |
| ISSUEMGT04 | What issue evidence is required? | Capture reproduction, logs, source, affected artifact, user report, screenshot, metric, or failed check. |
| ISSUEMGT05 | What issue response is needed now? | Choose workaround, fix, rollback, pause, reassign, escalate, communicate, or accept. |
| ISSUEMGT06 | What issue SLA applies? | Define response time, resolution time, update cadence, and escalation threshold. |
| ISSUEMGT07 | What issue dependencies block resolution? | Link missing data, approval, tool access, vendor response, SME review, or upstream fix. |
| ISSUEMGT08 | What issue communication is required? | Send status, impact, workaround, next update, owner, and expected resolution. |
| ISSUEMGT09 | What issue closure criteria apply? | Close only when fix, validation, communication, and prevention follow-up are complete. |
| ISSUEMGT10 | What issue log should be preserved? | Keep issue ID, severity, owner, evidence, actions, timestamps, resolution, and lessons. |

## Dependency Management

| Code | Risk question | Workflow use |
|---|---|---|
| DEPMGMT01 | What upstream dependency must be ready? | Track source material, approval, data, tool, API, vendor, SME, asset, environment, or decision. |
| DEPMGMT02 | What downstream dependency relies on this workflow? | Identify users, systems, teams, launches, reports, production runs, or client commitments affected. |
| DEPMGMT03 | What dependency owner is responsible? | Assign owner, backup owner, due date, status, and communication channel. |
| DEPMGMT04 | What dependency status should be tracked? | Use not started, requested, in progress, ready, blocked, late, changed, or retired. |
| DEPMGMT05 | What dependency date matters? | Track needed-by date, delivery date, freeze date, approval date, release date, and expiry date. |
| DEPMGMT06 | What dependency quality gate applies? | Require completeness, format, version, permission, accuracy, acceptance, or validation. |
| DEPMGMT07 | What dependency risk exists? | Score likelihood and impact of lateness, quality failure, scope change, access loss, or vendor issue. |
| DEPMGMT08 | What dependency fallback exists? | Prepare alternate source, substitute tool, manual path, staged release, or scope reduction. |
| DEPMGMT09 | What dependency change needs notification? | Notify when status, date, scope, quality, owner, or assumptions change. |
| DEPMGMT10 | What dependency map should be produced? | Produce dependency table, chain, graph, critical path, or handoff map. |

## Assumption Tracking

| Code | Risk question | Workflow use |
|---|---|---|
| RISKASSUMP01 | What assumption is the workflow relying on? | List unverified beliefs about users, sources, tools, data, timing, quality, cost, or approvals. |
| RISKASSUMP02 | Which assumption is critical? | Identify assumptions that would change the plan if false. |
| RISKASSUMP03 | What evidence supports the assumption? | Cite source, metric, user input, test, precedent, SME review, or explicit decision. |
| RISKASSUMP04 | What assumption is unsupported? | Mark unknown, untested, inferred, or user-provided-only assumptions. |
| RISKASSUMP05 | How can the assumption be validated? | Define test, source check, stakeholder confirmation, pilot, sample, or analysis. |
| RISKASSUMP06 | What deadline exists for validation? | Set latest safe date before execution, release, spend, or irreversible decision. |
| RISKASSUMP07 | What happens if the assumption is false? | Define impact, fallback, replan trigger, communication, and owner. |
| RISKASSUMP08 | What assumption can be accepted without validation? | Accept low-impact assumptions explicitly with owner and rationale. |
| RISKASSUMP09 | What assumption should be converted into a requirement? | Promote critical assumptions into acceptance criteria, source requirements, or gates. |
| RISKASSUMP10 | What assumption log should be preserved? | Keep assumption, evidence, status, validation method, owner, deadline, and outcome. |

## Escalation And Governance

| Code | Risk question | Workflow use |
|---|---|---|
| ESCGOV01 | What risk or issue needs escalation? | Escalate severe, blocked, cross-team, regulated, customer-impacting, or unresolved items. |
| ESCGOV02 | Who receives escalation? | Route to owner, approver, sponsor, legal, security, operations, vendor, client, or executive. |
| ESCGOV03 | What escalation evidence is required? | Include issue, impact, options, recommendation, deadline, owner, and requested decision. |
| ESCGOV04 | What decision is needed from escalation? | Ask for approval, scope change, resource, priority, acceptance, exception, or stop/go. |
| ESCGOV05 | What escalation timing applies? | Escalate immediately, after SLA breach, before deadline, at gate, or during review cadence. |
| ESCGOV06 | What escalation channel is appropriate? | Use ticket, meeting, status update, incident channel, email, dashboard, or formal memo. |
| ESCGOV07 | What governance rule applies? | Follow policy, compliance, audit, change control, risk appetite, or approval authority. |
| ESCGOV08 | What escalation should not happen? | Avoid escalating vague, ownerless, unevidenced, or low-impact noise. |
| ESCGOV09 | What escalation outcome should be recorded? | Capture decision, rationale, owner, deadline, exception, and follow-up. |
| ESCGOV10 | What escalation review should occur? | Review whether escalation was timely, clear, correctly routed, and effective. |

## Residual Risk And Acceptance

| Code | Risk question | Workflow use |
|---|---|---|
| RESRISK01 | What risk remains after mitigation? | Identify residual likelihood, impact, uncertainty, and affected stakeholders. |
| RESRISK02 | Who can accept the residual risk? | Assign risk acceptance to the accountable owner with appropriate authority. |
| RESRISK03 | What acceptance rationale is needed? | Explain why remaining risk is tolerable relative to value, constraints, alternatives, and controls. |
| RESRISK04 | What residual risk is unacceptable? | Block when risk exceeds tolerance, violates policy, lacks owner, or affects safety/regulated outcomes. |
| RESRISK05 | What condition would reopen the risk? | Define monitoring trigger, new evidence, scope change, incident, source change, or stakeholder objection. |
| RESRISK06 | What residual risk must be disclosed? | Communicate material limitations, known issues, uncertainty, safety, compliance, or quality caveats. |
| RESRISK07 | What residual risk should be transferred? | Move responsibility through contract, insurance, vendor commitment, user acceptance, or formal signoff. |
| RESRISK08 | What residual risk needs monitoring? | Track indicators, thresholds, owner review, and refresh cadence. |
| RESRISK09 | What residual risk should inform future work? | Convert recurring residual risks into backlog, standards, automation, or training. |
| RESRISK10 | What risk acceptance record should be kept? | Preserve owner, rationale, scope, conditions, disclosure, and review date. |

## Risk Review

| Code | Risk question | Workflow use |
|---|---|---|
| RISKREV01 | What review cadence applies? | Review risks daily, weekly, per milestone, per release, per batch, per incident, or per audit cycle. |
| RISKREV02 | What changed since the last review? | Check new risks, closed risks, score changes, realized issues, dependency movement, and assumption validation. |
| RISKREV03 | What risk trend matters? | Track increasing risk, repeated issues, unresolved blockers, growing backlog, or shrinking error budget. |
| RISKREV04 | What mitigation is overdue? | Escalate late actions, missing evidence, unassigned owners, or stale contingency plans. |
| RISKREV05 | What risk should be closed? | Close when trigger passed, mitigation complete, issue resolved, dependency delivered, or scope removed. |
| RISKREV06 | What risk should be reopened? | Reopen when evidence changes, issue recurs, assumption fails, or downstream impact appears. |
| RISKREV07 | What risk should be consolidated? | Merge duplicates, related issues, shared dependencies, and common root causes. |
| RISKREV08 | What risk should become a workflow improvement? | Add templates, gates, monitors, scripts, checklists, training, or ownership changes. |
| RISKREV09 | What review summary should be produced? | Summarize top risks, changes, decisions needed, overdue actions, and residual exposure. |
| RISKREV10 | What risk review evidence should be archived? | Keep review date, participants, register snapshot, decisions, actions, and next review. |

## Risk Communication

| Code | Risk question | Workflow use |
|---|---|---|
| RISKCOMM01 | Who needs risk visibility? | Identify user, client, sponsor, operator, reviewer, support, vendor, regulator, or public audience. |
| RISKCOMM02 | What level of detail is appropriate? | Tailor executive summary, operator detail, client caveat, audit evidence, or public limitation. |
| RISKCOMM03 | What risk should be communicated immediately? | Communicate severe, time-sensitive, user-impacting, compliance, security, safety, or deadline risks. |
| RISKCOMM04 | What risk belongs in routine status? | Include top risks, changes, mitigations, owners, due dates, and decisions needed. |
| RISKCOMM05 | What risk should be framed as a decision? | Present options, tradeoffs, recommendation, deadline, and consequence of inaction. |
| RISKCOMM06 | What risk language avoids panic or ambiguity? | Use factual impact, probability, evidence, action, owner, and next update. |
| RISKCOMM07 | What risk disclosure belongs in final output? | Disclose material assumptions, limitations, unresolved issues, and accepted risks. |
| RISKCOMM08 | What risk communication needs approval? | Gate legal, financial, public, regulated, client-sensitive, or executive-risk statements. |
| RISKCOMM09 | What communication feedback should be captured? | Record stakeholder objections, acceptance, questions, new risks, or decision changes. |
| RISKCOMM10 | What risk communication evidence should be kept? | Archive message, audience, date, approved wording, decisions, and follow-up. |

