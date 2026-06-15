# Professional Workflow Evaluation Metrics Matrix

Use this when a workflow needs measurable success criteria, quality tracking, speed/cycle-time measurement, throughput, cost, risk, reliability, coverage, adoption, user experience, learning improvement, or outcome evaluation. Metrics prevent workflow expansion from becoming unmeasured complexity.

Selection rule:

1. Identify what "better" means for the workflow.
2. Select the closest metric code.
3. Add metric definition, denominator, measurement method, threshold, and reporting cadence to the prompt packet.
4. Avoid metrics that cannot change decisions or reveal workflow health.

## SUCM Success Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| SUCM01 | Completion rate | Completed runs / started runs | Workflow has repeat runs | Completion report |
| SUCM02 | Acceptance rate | Accepted outputs / delivered outputs | User/reviewer approval matters | Acceptance log |
| SUCM03 | Goal match rate | Outputs meeting original goal / total outputs | Goal drift is possible | Acceptance mapping |
| SUCM04 | First-pass success | Runs accepted without rework / total runs | Rework should decrease | QA/review log |
| SUCM05 | On-time delivery | Deliveries before deadline / total deliveries | Deadlines matter | Schedule report |
| SUCM06 | Handoff success | Handoffs needing no clarification / total handoffs | Transfer quality matters | Handoff feedback |
| SUCM07 | Automation success | Automated runs completing without manual rescue / automated runs | Automation is used | Automation log |
| SUCM08 | Reuse success | Reused templates that work without major edits / reuse attempts | Library value matters | Reuse log |
| SUCM09 | Decision success | Decisions producing intended downstream result / decisions tracked | Decision quality matters | Outcome review |
| SUCM10 | Closeout integrity | Runs with evidence, risks, and next action / closed runs | Closure quality matters | Closeout audit |

## QUALM Quality Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| QUALM01 | Accuracy score | Correct facts or calculations / checked facts | Factual correctness matters | Verification table |
| QUALM02 | Completeness score | Required criteria met / required criteria | Coverage matters | QA checklist |
| QUALM03 | Consistency score | Consistent terms/numbers/decisions / checked items | Multi-artifact work | Consistency check |
| QUALM04 | Format pass rate | Outputs passing schema/format checks / outputs | Structured handoff | Format validation |
| QUALM05 | Citation closure rate | Claims with traceable evidence / claims | Research or sourced writing | Citation audit |
| QUALM06 | Visual fidelity score | Preserved visual/spec requirements / checked requirements | Image2/design/CAD | Visual QA |
| QUALM07 | Technical correctness | Tests/checks passing / relevant checks | Code/automation/data | Test result |
| QUALM08 | Review severity mix | Blocking/major/minor finding counts | Review prioritization | Review findings |
| QUALM09 | Production readiness score | Ready criteria met / ready criteria | Release/handoff | Readiness checklist |
| QUALM10 | Quality trend | Quality score over repeated runs | Continuous improvement | Trend report |

## SPEEDM Speed / Time Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| SPEEDM01 | Cycle time | Time from start to done | End-to-end speed matters | Timestamp log |
| SPEEDM02 | Lead time | Time from request to delivery | Queue and wait matter | Request/delivery log |
| SPEEDM03 | Planning time | Time spent before execution | Planning overhead matters | Plan timestamp |
| SPEEDM04 | Execution time | Time spent doing work | Execution bottlenecks matter | Action log |
| SPEEDM05 | Review time | Time waiting/in review | Human gates matter | Review log |
| SPEEDM06 | Approval time | Time from request to approval | Approval bottlenecks matter | Approval log |
| SPEEDM07 | Recovery time | Time from failure to restored state | Resilience matters | Recovery log |
| SPEEDM08 | Time-to-first-value | Time until useful partial output | Interactive workflows | Progress log |
| SPEEDM09 | Refresh latency | Time from source update to workflow update | Freshness matters | Refresh log |
| SPEEDM10 | Schedule variance | Actual time - planned time | Predictability matters | Schedule report |

## THRUM Throughput / Volume Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| THRUM01 | Items processed | Count processed per run/window | Batch workflows | Batch manifest |
| THRUM02 | Items per hour | Processed items / hour | Capacity planning | Throughput log |
| THRUM03 | Queue depth | Pending items at measurement time | Backlog management | Queue report |
| THRUM04 | Backlog age | Oldest pending item age | SLA/backlog health | Backlog report |
| THRUM05 | Batch failure rate | Failed items / batch items | Bulk reliability | Failure manifest |
| THRUM06 | Review throughput | Reviewed artifacts / time window | Reviewer capacity | Review report |
| THRUM07 | Automation throughput | Automated items / time window | Automation scale | Automation log |
| THRUM08 | Source processing volume | Sources processed / window | Research/data scale | Source inventory |
| THRUM09 | Library growth rate | New prompts/workflows / window | Library expansion | Index diff |
| THRUM10 | Throughput trend | Volume over time | Capacity changes | Trend report |

## COSTMET Cost Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| COSTMET01 | Cost per run | Total cost / workflow run | Cost control | Cost note |
| COSTMET02 | Cost per item | Total cost / processed item | Batch economics | Batch cost |
| COSTMET03 | Tool/API cost | Tool usage cost by run/window | Paid tools/APIs | Usage/cost log |
| COSTMET04 | Human review cost | Review time * cost rate | Review is expensive | Review time log |
| COSTMET05 | Rework cost | Time/cost spent on revisions | Rejection reduction | Rework log |
| COSTMET06 | Automation ROI | Manual cost avoided - automation cost | Automation decision | ROI note |
| COSTMET07 | Maintenance cost | Time/cost to keep workflow current | Long-lived workflows | Maintenance log |
| COSTMET08 | Delay cost | Impact of missed deadline/waiting | SLA/business impact | Delay note |
| COSTMET09 | Cost variance | Actual cost - planned cost | Budget tracking | Budget report |
| COSTMET10 | Value-to-cost ratio | Estimated value / cost | Prioritization | Value estimate |

## RISKMET Risk Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| RISKMET01 | Open risk count | Unresolved risks by severity | Risk tracking | Risk register |
| RISKMET02 | High-risk gate pass | High-risk outputs with required gate / high-risk outputs | Governance | Gate log |
| RISKMET03 | Residual risk rate | Closed runs with residual risk / closed runs | Caveat management | Closeout risk |
| RISKMET04 | Privacy exception count | Privacy issues/exceptions per period | Sensitive workflows | Privacy log |
| RISKMET05 | Security finding count | Security findings by severity | Technical workflows | Security review |
| RISKMET06 | Compliance exception count | Compliance exceptions per period | Regulated work | Compliance log |
| RISKMET07 | Unsafe output prevention | Unsafe requests safely rerouted / unsafe requests | Safety tracking | Safety log |
| RISKMET08 | Risk aging | Time risks remain open | Risk ownership | Risk register |
| RISKMET09 | Mitigation effectiveness | Risks reduced/closed after mitigation | Risk treatment | Mitigation review |
| RISKMET10 | Escalation rate | Escalated risks / total risks | Governance tuning | Escalation log |

## RELMET Reliability Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| RELMET01 | Run success rate | Successful runs / total runs | Repeat workflows | Run log |
| RELMET02 | Failure recurrence | Same failure count over time | Failure prevention | Failure index |
| RELMET03 | Retry success rate | Successful retries / retry attempts | Automation/tooling | Retry log |
| RELMET04 | Uptime/availability | Available time / total time | Services/tools | Availability log |
| RELMET05 | Idempotency pass | Re-runs without duplicate side effects / re-runs | Automation safety | Idempotency check |
| RELMET06 | Rollback success | Successful rollbacks / rollback attempts | Release/change workflows | Rollback log |
| RELMET07 | Recovery success | Resolved incidents / incidents | Incident handling | Incident report |
| RELMET08 | Data freshness reliability | Fresh outputs / outputs needing fresh sources | Current data workflows | Freshness log |
| RELMET09 | Handoff reliability | Handoffs completed without dropped state / handoffs | Multi-role workflows | Handoff audit |
| RELMET10 | Reliability trend | Run success/failure trend over time | Operational workflows | Reliability report |

## COVMET Coverage Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| COVMET01 | Scenario coverage | Covered scenarios / target scenarios | Library expansion | Coverage table |
| COVMET02 | Workflow dimension coverage | Selected dimensions / required dimensions | Full workflow design | Dimension checklist |
| COVMET03 | Input coverage | Input types supported / target input types | Multi-input workflows | Input matrix |
| COVMET04 | Output coverage | Deliverable types supported / target types | Multi-format workflows | Output matrix |
| COVMET05 | Risk coverage | Risk classes gated / relevant risk classes | High-risk workflows | Risk coverage |
| COVMET06 | Audience coverage | Audience variants handled / needed variants | Communication/adaptation | Audience map |
| COVMET07 | Lifecycle coverage | Lifecycle stages covered / needed stages | Long-lived projects | Lifecycle map |
| COVMET08 | Failure-mode coverage | Failure modes with prevention / likely failure modes | Hardening | Failure audit |
| COVMET09 | Test coverage | Tested criteria / required criteria | Validation | Test map |
| COVMET10 | Index coverage | Indexed artifacts / created artifacts | Findability | Index audit |

## ADOPTMET Adoption Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| ADOPTMET01 | Usage count | Number of workflow/template uses | Reuse tracking | Usage log |
| ADOPTMET02 | Active user count | Distinct users/operators in period | Adoption health | User log |
| ADOPTMET03 | Repeat use rate | Repeat users / users | Stickiness | Usage trend |
| ADOPTMET04 | Search success | Successful searches / total searches | Library findability | Search log |
| ADOPTMET05 | Template selection rate | Template chosen / relevant tasks | Template usefulness | Selection log |
| ADOPTMET06 | Abandonment rate | Started but abandoned runs / starts | UX/process friction | Run log |
| ADOPTMET07 | Manual override rate | Overrides / automated runs | Automation trust | Override log |
| ADOPTMET08 | Training completion | Users trained / target users | Enablement | Training log |
| ADOPTMET09 | Handoff adoption | Receivers using handoff packet / handoffs | Transfer usefulness | Handoff feedback |
| ADOPTMET10 | Adoption trend | Adoption metric over time | Scale monitoring | Adoption report |

## UXMET User Experience Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| UXMET01 | Clarity score | User/reviewer clarity rating | Handoff/communication | Feedback |
| UXMET02 | Time-to-understand | Time/questions needed to understand output | Complex deliverables | Follow-up count |
| UXMET03 | Next-action clarity | Outputs with clear next action / outputs | Actionability | Handoff QA |
| UXMET04 | Cognitive load signal | Number of choices/questions/steps exposed | Beginner workflows | Interaction log |
| UXMET05 | Satisfaction score | User satisfaction after delivery | User-facing workflows | Feedback |
| UXMET06 | Friction count | Reported points of confusion | UX/process improvement | Feedback log |
| UXMET07 | Correction count | User corrections after delivery | Expectation fit | Correction log |
| UXMET08 | Help request rate | Help asks / workflow uses | Usability | Support log |
| UXMET09 | Confidence signal | User expresses confidence/approval | Trust | Feedback note |
| UXMET10 | UX trend | UX signals over time | Continuous improvement | UX report |

## EVLEARNMET Learning / Improvement Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| EVLEARNMET01 | Lessons captured | Lessons added / runs | Learning loop | Lessons log |
| EVLEARNMET02 | Lessons applied | Lessons used in later runs / captured lessons | Improvement reuse | Change log |
| EVLEARNMET03 | Failure reduction | Failure rate after fix vs before | Hardening | Failure trend |
| EVLEARNMET04 | Prompt improvement | Benchmark score after prompt revision | Prompt tuning | Benchmark results |
| EVLEARNMET05 | Template improvement | Rework/clarification rate after template update | Template quality | Reuse QA |
| EVLEARNMET06 | Coverage growth | New covered categories over time | Library expansion | Coverage diff |
| EVLEARNMET07 | Staleness reduction | Stale items closed / stale items found | Maintenance | Maintenance log |
| EVLEARNMET08 | Experiment conversion | Experiments that become adopted workflows / experiments | R&D value | Experiment log |
| EVLEARNMET09 | User correction reduction | Corrections over time | Preference learning | Correction trend |
| EVLEARNMET10 | Maturity progression | Workflow maturity level over time | Process improvement | Maturity report |

## OUTMET Outcome Metrics

| Code | Metric | Definition | Use when | Evidence |
|---|---|---|---|---|
| OUTMET01 | Business impact | Revenue/cost/risk/time impact tied to workflow | Business workflows | Impact note |
| OUTMET02 | Decision impact | Decision quality or speed improved | Decision workflows | Decision review |
| OUTMET03 | Customer impact | Customer satisfaction, resolution, or conversion change | Client/customer workflows | Customer metric |
| OUTMET04 | Operational impact | SLA, throughput, error, or backlog improvement | Ops workflows | Ops report |
| OUTMET05 | Creative impact | Engagement, approval, brand fit, variant performance | Creative workflows | Creative report |
| OUTMET06 | Learning impact | Skill/knowledge gained by target learner | Education/training | Learning check |
| OUTMET07 | Research impact | Source quality, citation closure, insight usefulness | Research workflows | Research evaluation |
| OUTMET08 | Product impact | Adoption, activation, retention, usability effect | Product workflows | Product metric |
| OUTMET09 | Compliance impact | Reduced exceptions, audit readiness, policy adherence | Governance workflows | Compliance report |
| OUTMET10 | Strategic impact | Progress toward strategic objective | Strategy workflows | Strategy review |

