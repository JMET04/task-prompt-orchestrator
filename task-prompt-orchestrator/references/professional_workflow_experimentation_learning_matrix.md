# Professional Workflow Experimentation and Learning Matrix

Use this when a workflow must learn under uncertainty, test a hypothesis, compare variants, validate demand, improve prompts, optimize operations, run pilots, or convert evidence into iteration. Experimentation and learning rules define hypotheses, experiment mapping, baselines, design, variants, sampling, execution, analysis, learnings, iteration, scaling, and ethical boundaries.

Selection rule:

1. Identify the uncertainty or improvement opportunity.
2. Select the closest experimentation/learning code.
3. Add hypothesis, metric, baseline, sample, variant, run plan, analysis rule, decision threshold, learning record, and next iteration to the prompt packet.
4. Do not scale a change from an experiment until success criteria and guardrails are met.

## HYP Hypothesis Framing

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| HYP01 | Problem hypothesis | State what problem exists | Link to evidence or caveat | Problem hypothesis |
| HYP02 | Solution hypothesis | State why solution should work | Define mechanism | Solution hypothesis |
| HYP03 | User hypothesis | State who benefits | Name segment/persona | User hypothesis |
| HYP04 | Value hypothesis | State expected outcome/value | Define measurable value | Value hypothesis |
| HYP05 | Risk hypothesis | State possible downside | Define guardrail metric | Risk hypothesis |
| HYP06 | Adoption hypothesis | State why users will adopt | Define behavior signal | Adoption hypothesis |
| HYP07 | Prompt hypothesis | State prompt change expected effect | Define output metric | Prompt hypothesis |
| HYP08 | Workflow hypothesis | State process change expected effect | Define operational metric | Workflow hypothesis |
| HYP09 | Null hypothesis | State no-effect baseline | Prevent wishful reading | Null hypothesis |
| HYP10 | Hypothesis freeze | Lock hypothesis before run | Avoid post-hoc reframing | Frozen hypothesis |

## EXPMAP Experiment Mapping

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| EXPMAP01 | Uncertainty map | Identify what must be learned | Rank uncertainty by impact | Uncertainty map |
| EXPMAP02 | Experiment type | Choose test, pilot, survey, prototype, analysis | Match method to question | Experiment type |
| EXPMAP03 | Learning objective | Define what decision experiment informs | Avoid curiosity-only tests | Learning objective |
| EXPMAP04 | Success metric map | Link hypothesis to metric | One primary metric preferred | Metric map |
| EXPMAP05 | Guardrail map | Define safety/quality/cost guardrails | Stop on guardrail breach | Guardrail map |
| EXPMAP06 | Segment map | Define target and excluded segments | Avoid mixed populations | Segment map |
| EXPMAP07 | Channel map | Define where experiment runs | Match channel to behavior | Channel map |
| EXPMAP08 | Dependency map | Identify data/tool/review dependencies | Resolve before run | Dependency map |
| EXPMAP09 | Decision map | Define possible decisions after result | Continue/pivot/stop/scale | Decision map |
| EXPMAP10 | Experiment backlog | Store candidate experiments | Prioritize by learning value | Experiment backlog |

## BASELN Baseline / Control

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| BASELN01 | Current baseline | Measure current performance | Capture before change | Baseline metric |
| BASELN02 | Historical baseline | Use past data for comparison | Check comparability | Historical baseline |
| BASELN03 | Control group | Keep unchanged group/path | Avoid contamination | Control group |
| BASELN04 | Benchmark baseline | Compare to standard/external benchmark | State benchmark limits | Benchmark note |
| BASELN05 | Qualitative baseline | Capture current user/operator sentiment | Use consistent questions | Baseline feedback |
| BASELN06 | Cost baseline | Capture current cost/time/effort | Include unit basis | Cost baseline |
| BASELN07 | Quality baseline | Capture current error/QA rate | Use same rubric | Quality baseline |
| BASELN08 | Prompt baseline | Capture current prompt output | Save prompt and examples | Prompt baseline |
| BASELN09 | Workflow baseline | Capture current process state | Map steps and pain points | Workflow baseline |
| BASELN10 | Baseline gap | Baseline missing or unreliable | Collect proxy or delay claim | Baseline caveat |

## DESIGNX Experiment Design

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| DESIGNX01 | A/B design | Compare control vs one variant | Randomize or explain assignment | A/B plan |
| DESIGNX02 | Multivariate design | Compare multiple factors | Limit combinations | MVT plan |
| DESIGNX03 | Pilot design | Test with small real audience | Define pilot exit criteria | Pilot plan |
| DESIGNX04 | Prototype test design | Test low-fidelity solution | Define task and feedback | Prototype plan |
| DESIGNX05 | Wizard-of-Oz design | Simulate automation manually | Disclose if needed and log process | Wizard plan |
| DESIGNX06 | Before/after design | Compare before and after change | Control for confounders | Before-after plan |
| DESIGNX07 | Holdout design | Reserve non-exposed group | Protect future comparison | Holdout plan |
| DESIGNX08 | Sequential design | Learn in stages | Gate next stage on result | Sequential plan |
| DESIGNX09 | Qualitative study design | Interview/observe users/operators | Use guide and coding plan | Study plan |
| DESIGNX10 | Experiment design review | Design may be biased/unsafe | Review method and guardrails | Design review |

## VARX Variant Design

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| VARX01 | Copy variant | Test wording/message | Change one meaningful variable | Copy variant |
| VARX02 | UI variant | Test interface/layout | Preserve accessibility | UI variant |
| VARX03 | Workflow variant | Test process sequence/gate | Track operational impact | Workflow variant |
| VARX04 | Prompt variant | Test prompt pattern/variables | Save prompt versions | Prompt variant |
| VARX05 | Pricing/offer variant | Test offer framing | Check legal/ethical rules | Offer variant |
| VARX06 | Training variant | Test enablement approach | Measure behavior not just completion | Training variant |
| VARX07 | Support variant | Test support response/path | Protect service quality | Support variant |
| VARX08 | Channel variant | Test distribution channel | Track comparable audience | Channel variant |
| VARX09 | Policy variant | Test process policy only if allowed | Require governance approval | Policy variant |
| VARX10 | Variant freeze | Lock variant before run | Prevent mid-run drift | Variant spec |

## SAMPLEX Experiment Sampling

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| SAMPLEX01 | Sample definition | Define who/items included | Match target population | Sample spec |
| SAMPLEX02 | Sample size estimate | Estimate needed volume | State power/practical limits | Sample estimate |
| SAMPLEX03 | Random assignment | Assign participants/items randomly | Prevent selection bias | Assignment log |
| SAMPLEX04 | Stratified sample | Include important segments | Avoid segment imbalance | Stratified sample |
| SAMPLEX05 | High-risk exclusion | Exclude unsafe participants/items | Protect vulnerable/high-risk cases | Exclusion rule |
| SAMPLEX06 | Representative sample | Ensure sample matches use case | Compare sample attributes | Representation check |
| SAMPLEX07 | Convenience sample | Use available sample cautiously | Label limitations | Convenience caveat |
| SAMPLEX08 | Qualitative sample | Select interview/test participants | Cover target personas | Qual sample |
| SAMPLEX09 | Sample contamination | Participants/items cross exposure | Detect and exclude/flag | Contamination note |
| SAMPLEX10 | Sample closeout | Final sample locked | Record included/excluded counts | Sample closeout |

## RUNX Experiment Execution

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| RUNX01 | Launch experiment | Start experiment with locked plan | Confirm tracking and guardrails | Launch log |
| RUNX02 | Monitor run | Watch metrics/errors/guardrails | Pause on breach | Monitor log |
| RUNX03 | Run fidelity | Ensure experiment follows design | Audit exposure and execution | Fidelity check |
| RUNX04 | Data capture | Capture events/outputs/feedback | Validate collection | Data capture |
| RUNX05 | Issue handling | Handle runtime issue | Log deviations and decisions | Issue log |
| RUNX06 | Midpoint review | Check health without peeking bias | Review guardrails only unless planned | Midpoint note |
| RUNX07 | Stop early | Stop for harm, futility, or clear result | Use pre-defined stop rule | Stop record |
| RUNX08 | Extend run | Need more data/time | Approve extension and reason | Extension note |
| RUNX09 | Close run | End experiment cleanly | Lock data and versions | Close log |
| RUNX10 | Run handoff | Analyst/reviewer receives data | Provide run context and caveats | Run handoff |

## ANALYX Experiment Analysis

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| ANALYX01 | Primary metric analysis | Analyze primary metric | Use pre-defined method | Primary result |
| ANALYX02 | Guardrail analysis | Check safety/quality/cost guardrails | Do not ignore guardrail failure | Guardrail result |
| ANALYX03 | Segment analysis | Analyze important segments | Avoid overfitting small slices | Segment result |
| ANALYX04 | Qualitative analysis | Synthesize interviews/feedback | Preserve quotes/themes | Qual analysis |
| ANALYX05 | Statistical analysis | Estimate significance/confidence | State limitations | Stats result |
| ANALYX06 | Practical significance | Assess real-world value | Compare lift to cost/risk | Practical result |
| ANALYX07 | Confounder analysis | Identify external influences | Label uncertainty | Confounder note |
| ANALYX08 | Failure analysis | Experiment failed or inconclusive | Identify why and next learning | Failure analysis |
| ANALYX09 | Cost analysis | Analyze cost of variant/change | Include unit economics | Cost analysis |
| ANALYX10 | Analysis review | Results need independent check | Review method and conclusions | Analysis review |

## LEARNX Learning Capture

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| LEARNX01 | Validated learning | Record what was learned | Link to hypothesis and evidence | Learning note |
| LEARNX02 | Inconclusive learning | Result does not answer question | Record why and next test | Inconclusive note |
| LEARNX03 | Negative learning | Hypothesis disproven | Capture stop/pivot implication | Negative learning |
| LEARNX04 | Unexpected learning | New insight emerges | Separate exploration from proof | Surprise note |
| LEARNX05 | Segment learning | Learning differs by group | Record segment-specific result | Segment learning |
| LEARNX06 | Operational learning | Process/tool/cost insight emerges | Update runbook/workflow | Ops learning |
| LEARNX07 | User learning | User behavior/need insight emerges | Update journey/requirements | User learning |
| LEARNX08 | Prompt learning | Prompt behavior insight emerges | Update prompt pattern/template | Prompt learning |
| LEARNX09 | Risk learning | New risk/guardrail insight emerges | Update risk/control | Risk learning |
| LEARNX10 | Learning archive | Learning should be reusable | Add index/provenance/tags | Learning archive |

## ITERX Iteration Decision

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| ITERX01 | Continue decision | Result supports continuing | Define next milestone | Continue note |
| ITERX02 | Pivot decision | Result suggests new direction | Record changed hypothesis | Pivot note |
| ITERX03 | Stop decision | Result shows poor value/risk | Close and archive | Stop note |
| ITERX04 | Scale decision | Result supports broader rollout | Check guardrails and adoption | Scale note |
| ITERX05 | Retest decision | Result unreliable | Fix design and rerun | Retest note |
| ITERX06 | Narrow decision | Result works for subset only | Limit scope/segment | Narrow note |
| ITERX07 | Broaden decision | Result suggests larger opportunity | Define expansion hypothesis | Broaden note |
| ITERX08 | Product/process change | Convert result into change request | Update backlog/roadmap | Change item |
| ITERX09 | Knowledge update | Convert result into reusable knowledge | Update template/index | Knowledge update |
| ITERX10 | Decision closeout | Decision made from experiment | Record owner, rationale, action | Decision record |

## SCALEX Experiment Scaling

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| SCALEX01 | Scale readiness | Check if experiment can scale | Require success and guardrail pass | Readiness check |
| SCALEX02 | Phased scale | Roll out by cohort/region/team | Monitor each phase | Phase scale |
| SCALEX03 | Operational scale | Process must handle higher volume | Add capacity/runbook/support | Ops scale |
| SCALEX04 | Technical scale | Tool/system must handle larger load | Validate performance/reliability | Tech scale |
| SCALEX05 | Training scale | Users/operators need enablement | Add training/adoption plan | Training scale |
| SCALEX06 | Policy scale | Wider rollout needs policy/governance | Add approvals/controls | Policy scale |
| SCALEX07 | Cost scale | Cost changes at volume | Re-estimate unit/total cost | Cost scale |
| SCALEX08 | Quality scale | Quality may degrade at volume | Add sampling/QA controls | Quality scale |
| SCALEX09 | Scale rollback | Scaling may fail | Define rollback/degrade plan | Scale rollback |
| SCALEX10 | Scale closeout | Scaling completed | Record adoption/outcome evidence | Scale closeout |

## ETHX Ethics / Safety in Experiments

| Code | Experiment need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| ETHX01 | Consent boundary | Participants may need consent/notice | Check legal/ethical requirement | Consent note |
| ETHX02 | Privacy boundary | Experiment uses personal/sensitive data | Minimize and protect data | Privacy note |
| ETHX03 | Fairness boundary | Variant may affect groups unfairly | Check segment harm | Fairness check |
| ETHX04 | Safety boundary | Experiment may create harm | Add stop rule and escalation | Safety gate |
| ETHX05 | Deception boundary | Users may be misled | Avoid or govern carefully | Deception review |
| ETHX06 | Vulnerable users | Special population involved | Exclude or add safeguards | Vulnerable-user note |
| ETHX07 | Financial/legal/medical impact | High-stakes outcome affected | Require expert/governance review | High-stakes review |
| ETHX08 | Public claim risk | Experiment changes public claims | Substantiate and approve claims | Claim review |
| ETHX09 | Experiment transparency | Stakeholders need disclosure | Provide appropriate transparency | Transparency note |
| ETHX10 | Ethics closeout | Ethical risk resolved/accepted | Archive review and residual risk | Ethics closeout |
