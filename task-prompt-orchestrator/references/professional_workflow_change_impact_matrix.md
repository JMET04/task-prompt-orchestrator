# Professional Workflow Change Impact Matrix

Use this when a workflow, prompt, artifact, automation, source, index, data contract, policy, or operating process changes. Change impact rules identify who or what is affected, what must be retested, what must be communicated, and how to roll back safely.

Selection rule:

1. Identify the object being changed.
2. Select the closest impact code.
3. Add affected parties, affected artifacts/systems, required checks, communication, and rollback to the prompt packet.
4. Do not treat a change as safe until downstream compatibility and required approvals are checked.

## STKIMP Stakeholder Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| STKIMP01 | User impact | Who uses the output or workflow? | Notify or update instructions | User impact note |
| STKIMP02 | Reviewer impact | Does review criteria change? | Update reviewer checklist | Review impact |
| STKIMP03 | Approver impact | Does approval authority/criteria change? | Refresh approval path | Approval impact |
| STKIMP04 | Operator impact | Does runbook/operator behavior change? | Update runbook/training | Operator impact |
| STKIMP05 | Client impact | Does client-facing scope/output change? | Send impact note or approval ask | Client impact |
| STKIMP06 | Downstream team impact | Does another team depend on output? | Send handoff/change notice | Downstream note |
| STKIMP07 | SME impact | Does expert validation need update? | Request SME review | SME review |
| STKIMP08 | Support impact | Will support questions/process change? | Update support notes | Support impact |
| STKIMP09 | Executive impact | Does decision/risk/cost change materially? | Prepare executive summary | Exec impact |
| STKIMP10 | Public audience impact | Does public claim/asset change? | Add brand/legal review | Public impact |

## SYSIMP System / Tool Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| SYSIMP01 | Local file impact | Which files are read/written differently? | Verify paths and diffs | File impact |
| SYSIMP02 | API impact | Does endpoint/payload/version change? | Validate API contract | API impact |
| SYSIMP03 | Database impact | Does schema/query/metric change? | Re-run data validation | DB impact |
| SYSIMP04 | Automation impact | Does trigger/job/output change? | Dry run automation | Automation impact |
| SYSIMP05 | Toolchain impact | Does required tool/version change? | Update tool readiness/fallback | Toolchain note |
| SYSIMP06 | Integration impact | Does downstream system consume new format? | Validate handoff/import | Integration check |
| SYSIMP07 | Monitoring impact | Do logs/metrics/alerts change? | Update monitor config | Monitoring impact |
| SYSIMP08 | Auth/access impact | Do permissions or audiences change? | Recheck least privilege | Access impact |
| SYSIMP09 | Environment impact | Does runtime/platform differ? | Record version/env check | Environment impact |
| SYSIMP10 | Release impact | Does publish/deploy path change? | Run release rehearsal | Release impact |

## DATAIMP Data / Source Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| DATAIMP01 | Source set impact | Does source list or authority change? | Refresh source inventory | Source impact |
| DATAIMP02 | Citation impact | Do claims/citations need relinking? | Re-run citation closure | Citation impact |
| DATAIMP03 | Dataset impact | Does dataset/schema/grain change? | Re-profile and reconcile | Dataset impact |
| DATAIMP04 | Metric impact | Does metric definition/denominator change? | Update metric dictionary | Metric impact |
| DATAIMP05 | Lineage impact | Does transform/provenance change? | Update lineage note | Lineage impact |
| DATAIMP06 | Freshness impact | Does change alter freshness requirements? | Update refresh cadence | Freshness impact |
| DATAIMP07 | Sensitive data impact | Does data class/exposure change? | Re-run privacy gate | Privacy impact |
| DATAIMP08 | Data retention impact | Does keep/delete rule change? | Update retention note | Retention impact |
| DATAIMP09 | Data export impact | Does export schema/fields change? | Validate export/import | Export impact |
| DATAIMP10 | Data quality impact | Could quality checks change? | Re-run data QA | Data QA impact |

## PROCIMP Process Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| PROCIMP01 | Step impact | Which workflow steps change? | Update phase/step plan | Step impact |
| PROCIMP02 | Gate impact | Which gates change? | Update gate criteria | Gate impact |
| PROCIMP03 | Role impact | Do responsibilities change? | Update RACI/owners | Role impact |
| PROCIMP04 | Trigger impact | Does start condition/cadence change? | Update trigger/cadence rule | Trigger impact |
| PROCIMP05 | State transition impact | Does allowed next state change? | Update state machine | State impact |
| PROCIMP06 | IO contract impact | Does input/output shape change? | Update IO schema | IO impact |
| PROCIMP07 | Artifact impact | Does required evidence/output change? | Update artifact contract | Artifact impact |
| PROCIMP08 | Communication impact | Do status/approval/handoff messages change? | Update comms templates | Comms impact |
| PROCIMP09 | Testing impact | Which tests must rerun? | Update test plan | Test impact |
| PROCIMP10 | Maintenance impact | Does owner/cadence/retirement change? | Update maintenance rule | Maintenance impact |

## RISKIMP Risk Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| RISKIMP01 | Risk tier impact | Does risk level increase/decrease? | Re-run risk triage | Risk tier note |
| RISKIMP02 | Compliance impact | Does regulation/policy exposure change? | Re-run compliance gate | Compliance impact |
| RISKIMP03 | Security impact | Does attack/access surface change? | Security review | Security impact |
| RISKIMP04 | Privacy impact | Does personal/sensitive data exposure change? | Privacy review | Privacy impact |
| RISKIMP05 | Financial risk impact | Does exposure/cost/assumption change? | Finance review | Finance impact |
| RISKIMP06 | Legal impact | Does obligation/claim/right change? | Legal review | Legal impact |
| RISKIMP07 | Brand/reputation impact | Does public perception change? | Brand/comms review | Brand impact |
| RISKIMP08 | Safety impact | Does physical/user harm potential change? | Safety review | Safety impact |
| RISKIMP09 | Residual risk impact | Does accepted risk change? | Update residual risk note | Residual risk |
| RISKIMP10 | Escalation impact | Does owner/threshold change? | Update escalation path | Escalation impact |

## COSTIMP Cost / Budget Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| COSTIMP01 | Tool cost impact | Does tool/API cost change? | Update cost estimate | Tool cost note |
| COSTIMP02 | Human effort impact | Does review/execution effort change? | Update capacity plan | Effort impact |
| COSTIMP03 | Automation setup impact | Does automation build/maintenance cost change? | Recompute ROI | Automation cost |
| COSTIMP04 | Rework cost impact | Could change cause rework? | Add pilot/regression test | Rework impact |
| COSTIMP05 | Delay cost impact | Could timeline slip? | Update schedule risk | Delay note |
| COSTIMP06 | Vendor cost impact | Does vendor spend/SLA change? | Procurement review | Vendor cost |
| COSTIMP07 | Maintenance cost impact | Does upkeep grow/shrink? | Update maintenance budget | Maintenance cost |
| COSTIMP08 | Training cost impact | Do users/operators need retraining? | Update training plan | Training cost |
| COSTIMP09 | Opportunity cost impact | What work is displaced? | Re-prioritize backlog | Opportunity note |
| COSTIMP10 | Budget approval impact | Does spend cross threshold? | Request budget approval | Budget gate |

## TIMEIMP Time / Schedule Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| TIMEIMP01 | Deadline impact | Does delivery date change? | Update deadline and status | Deadline impact |
| TIMEIMP02 | Cycle-time impact | Does run time change? | Update time estimate | Cycle-time note |
| TIMEIMP03 | Review-time impact | Does review take longer? | Reserve review capacity | Review schedule |
| TIMEIMP04 | Approval-time impact | Does approval path lengthen? | Update approval calendar | Approval schedule |
| TIMEIMP05 | Migration-time impact | Does transition require migration window? | Plan migration window | Migration plan |
| TIMEIMP06 | Testing-time impact | Do more tests need rerun? | Update test schedule | Test schedule |
| TIMEIMP07 | Training-time impact | Does onboarding time change? | Update training cadence | Training schedule |
| TIMEIMP08 | Refresh-time impact | Does data/source refresh cadence change? | Update refresh schedule | Refresh schedule |
| TIMEIMP09 | Downtime impact | Could release cause downtime? | Add maintenance window/rollback | Downtime note |
| TIMEIMP10 | Grace-period impact | Does escalation buffer change? | Update SLA/grace rule | Grace update |

## QUALIMP Quality Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| QUALIMP01 | Accuracy impact | Could facts/calculations change? | Re-run accuracy checks | Accuracy impact |
| QUALIMP02 | Completeness impact | Could required coverage change? | Re-run coverage check | Coverage impact |
| QUALIMP03 | Consistency impact | Could terms/specs drift? | Re-run consistency check | Consistency impact |
| QUALIMP04 | Format impact | Could schema/layout break? | Re-validate format | Format impact |
| QUALIMP05 | Visual impact | Could design/image/CAD specs drift? | Visual QA | Visual impact |
| QUALIMP06 | Technical impact | Could code/tool behavior break? | Run technical tests | Technical impact |
| QUALIMP07 | Data quality impact | Could data errors increase? | Data QA | Data quality |
| QUALIMP08 | Prompt quality impact | Could prompt output regress? | Prompt benchmark | Prompt impact |
| QUALIMP09 | UX quality impact | Could user friction increase? | UX acceptance test | UX impact |
| QUALIMP10 | Production readiness impact | Could release readiness change? | Readiness checklist | Readiness impact |

## LEGIMP Legal / Contract Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| LEGIMP01 | Contract obligation impact | Does obligation change? | Legal/contract review | Obligation note |
| LEGIMP02 | IP rights impact | Does asset/source usage change? | Rights review | IP note |
| LEGIMP03 | Terms impact | Does platform/vendor term apply? | Terms review | Terms note |
| LEGIMP04 | Jurisdiction impact | Does location/legal scope change? | Jurisdiction review | Jurisdiction note |
| LEGIMP05 | Consumer claim impact | Does claim/offer change? | Claim substantiation | Claim note |
| LEGIMP06 | Employment/legal fairness impact | Does people/HR decision change? | HR/legal review | Fairness note |
| LEGIMP07 | Data processing impact | Does DPA/privacy obligation change? | Legal/privacy review | Processing note |
| LEGIMP08 | Liability impact | Does exposure change? | Legal risk review | Liability note |
| LEGIMP09 | Retention/legal hold impact | Does recordkeeping change? | Records/legal review | Retention note |
| LEGIMP10 | Legal approval impact | Does legal signoff need refresh? | Re-approval | Legal signoff |

## COMMIMP Communication Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| COMMIMP01 | Status update impact | Who needs to know change status? | Send status update | Status note |
| COMMIMP02 | Release note impact | Does release/changelog need update? | Write release note | Release note |
| COMMIMP03 | Client message impact | Does client-facing message change? | Send client change note | Client note |
| COMMIMP04 | Internal announcement impact | Do operators/users need announcement? | Send internal notice | Announcement |
| COMMIMP05 | Support script impact | Does support answer change? | Update support script | Support update |
| COMMIMP06 | Training material impact | Does guide/tutorial change? | Update training material | Training update |
| COMMIMP07 | Approval request impact | Does approval ask change? | Reissue approval packet | Approval message |
| COMMIMP08 | Risk communication impact | Do risks/caveats change? | Update risk notice | Risk comms |
| COMMIMP09 | Archive/index communication impact | Does findability note change? | Update index/archive notice | Archive note |
| COMMIMP10 | Executive communication impact | Does leadership need summary? | Prepare executive brief | Exec summary |

## TRAINIMP Training / Adoption Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| TRAINIMP01 | User training impact | Does user behavior change? | Update quick-start guide | User training |
| TRAINIMP02 | Operator training impact | Does runbook execution change? | Update operator training | Operator training |
| TRAINIMP03 | Reviewer training impact | Does review rubric change? | Update reviewer guidance | Reviewer training |
| TRAINIMP04 | Approver training impact | Does approval criteria change? | Update approver guidance | Approver training |
| TRAINIMP05 | Support training impact | Does support need new answer? | Update support FAQ | Support training |
| TRAINIMP06 | Client training impact | Does client need new instructions? | Update client guide | Client training |
| TRAINIMP07 | Agent training impact | Does prompt/skill route change? | Update reference/routing | Agent training |
| TRAINIMP08 | Onboarding impact | Does new-user onboarding change? | Update onboarding packet | Onboarding update |
| TRAINIMP09 | Adoption impact | Could change reduce use/trust? | Monitor adoption feedback | Adoption note |
| TRAINIMP10 | Learning impact | Does change reveal reusable lesson? | Capture lesson | Lesson note |

## ROLLIMP Rollback / Migration Impact

| Code | Impact area | Check | Required action | Evidence |
|---|---|---|---|---|
| ROLLIMP01 | Rollback availability | Can previous state be restored? | Define rollback path | Rollback plan |
| ROLLIMP02 | Rollback trigger | When should rollback happen? | Define trigger and owner | Rollback trigger |
| ROLLIMP03 | Migration need | Must old artifacts/users move? | Create migration map | Migration note |
| ROLLIMP04 | Compatibility need | Must old and new formats coexist? | Add compatibility adapter | Compatibility note |
| ROLLIMP05 | Data migration risk | Could data be lost/corrupted? | Back up and reconcile | Data rollback |
| ROLLIMP06 | Automation rollback | Can trigger/job be disabled safely? | Add disable path | Automation rollback |
| ROLLIMP07 | Communication rollback | Need to retract/replace message? | Prepare correction notice | Comms rollback |
| ROLLIMP08 | Approval rollback | Does approval become invalid? | Revoke/refresh approval | Approval rollback |
| ROLLIMP09 | Archive rollback | Can old version be retrieved? | Verify archive snapshot | Archive rollback |
| ROLLIMP10 | Post-rollback review | What caused rollback? | Capture lesson and prevention | Rollback review |
