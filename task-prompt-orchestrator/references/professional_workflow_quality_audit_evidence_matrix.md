# Professional Workflow Quality Audit Evidence Matrix

Use this when a workflow must prove quality, compliance, production readiness, review integrity, auditability, or signoff. Quality audit evidence rules define standards, evidence packets, traceability, controls, sampling, nonconformance handling, corrective action, document control, records, approvals, and certification readiness.

Selection rule:

1. Identify the quality or audit requirement.
2. Select the closest evidence code.
3. Add standard, evidence artifact, owner, reviewer, pass/fail rule, record location, and retention rule to the prompt packet.
4. Do not mark quality complete without objective evidence or an explicit accepted exception.

## QPLAN Quality Planning

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| QPLAN01 | Quality objective | Define what quality means for this workflow | Link objective to acceptance criteria | Quality objective |
| QPLAN02 | Quality scope | Define products, steps, and outputs covered | Exclude out-of-scope explicitly | QA scope |
| QPLAN03 | Quality owner | Assign accountable quality owner | Owner approves QA plan | Owner record |
| QPLAN04 | Quality gate map | Identify required checks by phase | Gate cannot be skipped silently | Gate map |
| QPLAN05 | Risk-based QA | Match QA depth to risk | High-risk areas get stronger evidence | Risk QA plan |
| QPLAN06 | Reviewer plan | Assign reviewer by domain and availability | Reviewer scope documented | Review plan |
| QPLAN07 | Acceptance plan | Map requirements to evidence | No orphan requirements | Acceptance map |
| QPLAN08 | Sampling plan | Define sampling rule for volume | Sampling statistically or operationally justified | Sampling plan |
| QPLAN09 | Tool QA plan | Define validators, tests, scripts, checklists | Tool results reviewed | Tool QA plan |
| QPLAN10 | Quality closeout plan | Define final signoff and archive requirements | Close only with evidence | Closeout plan |

## STDCHK Standard / Requirement Check

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| STDCHK01 | Requirement standard | Identify user/business requirement | Check output against requirement | Requirement check |
| STDCHK02 | Format standard | Identify schema/layout/file standard | Validate format exactly | Format check |
| STDCHK03 | Technical standard | Identify engineering/test standard | Run technical checks | Technical check |
| STDCHK04 | Brand standard | Identify brand/style rules | Review tone, visuals, claims | Brand check |
| STDCHK05 | Legal standard | Identify legal/compliance requirement | Route to legal gate if needed | Legal check |
| STDCHK06 | Safety standard | Identify safety-critical criteria | Block unsafe output | Safety check |
| STDCHK07 | Accessibility standard | Identify accessibility requirement | Validate inclusive access | Accessibility check |
| STDCHK08 | Data standard | Identify metric/schema/lineage rule | Validate data contract | Data standard check |
| STDCHK09 | Manufacturing standard | Identify tolerance/material/spec rule | Validate production readiness | Manufacturing check |
| STDCHK10 | Standard uncertainty | Standard missing or ambiguous | Record uncertainty and escalate | Standard gap |

## EVIDPKT Evidence Packet

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| EVIDPKT01 | Source evidence | Need prove factual claims | Attach source list and claim links | Source packet |
| EVIDPKT02 | Test evidence | Need prove checks passed | Attach test/validator output | Test packet |
| EVIDPKT03 | Review evidence | Need prove review occurred | Attach findings and disposition | Review packet |
| EVIDPKT04 | Approval evidence | Need prove authorization | Attach signoff and criteria | Approval packet |
| EVIDPKT05 | Data evidence | Need prove data correctness | Attach lineage, sample, reconciliation | Data packet |
| EVIDPKT06 | Design evidence | Need prove visual/spec compliance | Attach screenshots/spec checks | Design packet |
| EVIDPKT07 | Manufacturing evidence | Need prove physical spec readiness | Attach drawings, BOM, tolerances, QA notes | MFG packet |
| EVIDPKT08 | Security evidence | Need prove security/privacy controls | Attach scan, access, redaction proof | Security packet |
| EVIDPKT09 | Exception evidence | Need prove accepted deviation | Attach exception owner and rationale | Exception packet |
| EVIDPKT10 | Closeout evidence | Need prove completion | Bundle outputs, checks, risks, archive | Closeout packet |

## AUDTRL Audit Trail

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| AUDTRL01 | Action trail | Need know who did what | Log actor, action, time, artifact | Action log |
| AUDTRL02 | Decision trail | Need know why decision changed | Log option, criteria, owner, rationale | Decision log |
| AUDTRL03 | Change trail | Need track edits/versions | Log diff, reason, approval | Change log |
| AUDTRL04 | Source trail | Need trace claim to source | Link claim/source/date | Source trace |
| AUDTRL05 | Tool trail | Need trace tool outputs | Log command/tool/version/config | Tool trace |
| AUDTRL06 | Review trail | Need trace finding resolution | Link finding to fix/defer/accept | Review trace |
| AUDTRL07 | Approval trail | Need prove signoff sequence | Log approver, scope, timestamp | Approval trace |
| AUDTRL08 | Access trail | Need know data/system access | Log access grant/use/removal | Access trace |
| AUDTRL09 | Exception trail | Need trace deviations | Log deviation, owner, mitigation | Exception trace |
| AUDTRL10 | Archive trail | Need prove evidence retained | Log archive path and retention | Archive trace |

## CTRLQA Control Check

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| CTRLQA01 | Preventive control | Stop error before it happens | Add pre-check or gate | Preventive control |
| CTRLQA02 | Detective control | Detect error after execution | Add review, metric, alert, or audit | Detective control |
| CTRLQA03 | Corrective control | Repair known error path | Add fix and verification | Corrective control |
| CTRLQA04 | Manual control | Human judgment required | Define reviewer, checklist, evidence | Manual control |
| CTRLQA05 | Automated control | Deterministic validation possible | Add script/test/schema check | Automated control |
| CTRLQA06 | Compensating control | Primary control unavailable | Add alternate evidence or review | Compensating control |
| CTRLQA07 | Segregation control | Same actor should not execute and approve | Separate owner and approver | Segregation record |
| CTRLQA08 | Access control | Restrict who can modify/release | Enforce permission boundary | Access control |
| CTRLQA09 | Release control | Output must not ship without gates | Require release checklist | Release control |
| CTRLQA10 | Control effectiveness | Need prove control works | Test control on sample | Control test |

## SAMPLEQA Sampling / Inspection

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| SAMPLEQA01 | Random inspection | Need unbiased quality signal | Sample random items | Random sample |
| SAMPLEQA02 | Stratified inspection | Items differ by category/risk | Sample each important segment | Stratified sample |
| SAMPLEQA03 | Critical-item inspection | Certain items are high impact | Inspect all critical items | Critical inspection |
| SAMPLEQA04 | First-article inspection | New process/output needs initial approval | Inspect first output before scale | First-article report |
| SAMPLEQA05 | In-process inspection | Errors should be caught midstream | Inspect during production | In-process report |
| SAMPLEQA06 | Final inspection | Output ready for handoff/release | Inspect final artifact | Final inspection |
| SAMPLEQA07 | Regression inspection | Change may break prior behavior | Inspect old and new cases | Regression inspection |
| SAMPLEQA08 | Defect sampling | Failures need pattern analysis | Sample defects by type/cause | Defect sample |
| SAMPLEQA09 | Reviewer calibration | Multiple reviewers may drift | Review same sample and align rubric | Calibration record |
| SAMPLEQA10 | Sampling failure | Sample fails threshold | Stop batch and trigger rework | Sample failure |

## NONCONF Nonconformance / Defect

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| NONCONF01 | Defect identification | Output fails requirement | Record defect type and evidence | Defect record |
| NONCONF02 | Severity classification | Defect impact differs | Assign blocking/major/minor | Severity label |
| NONCONF03 | Defect containment | Defect may spread | Quarantine affected output/items | Containment log |
| NONCONF04 | Root cause link | Defect reason unclear | Link to diagnosis/root cause | Cause note |
| NONCONF05 | Disposition decision | Defect needs accept/fix/reject decision | Record owner and rationale | Disposition record |
| NONCONF06 | Rework requirement | Defect must be corrected | Define fix and retest | Rework ticket |
| NONCONF07 | Accepted deviation | Defect accepted as exception | Require approval and residual risk | Deviation approval |
| NONCONF08 | Supplier/vendor defect | External source caused defect | Notify vendor and track remedy | Vendor defect |
| NONCONF09 | Recurring defect | Defect repeats | Escalate to corrective action | Recurrence log |
| NONCONF10 | Nonconformance closeout | Defect resolved or accepted | Verify action and archive evidence | NC closeout |

## CORACT Corrective / Preventive Action

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| CORACT01 | Immediate correction | Single output needs fix | Correct and verify affected artifact | Correction proof |
| CORACT02 | Corrective action | Root cause needs removal | Define action, owner, due date | CAPA item |
| CORACT03 | Preventive action | Similar future failure likely | Add prevention control | Preventive action |
| CORACT04 | Effectiveness check | Need prove action worked | Recheck after defined interval/sample | Effectiveness check |
| CORACT05 | Training action | Human process caused issue | Update guidance/training | Training proof |
| CORACT06 | Process action | Workflow step caused issue | Modify process/runbook | Process update |
| CORACT07 | Tool action | Tool/script/check failed | Patch tool or add validator | Tool update |
| CORACT08 | Supplier action | Vendor source caused issue | Request corrective action | Supplier CAPA |
| CORACT09 | Risk acceptance | Fix not feasible or not worth cost | Record accepted residual risk | Risk acceptance |
| CORACT10 | CAPA closeout | Corrective action complete | Verify evidence and update records | CAPA closeout |

## DOCCTRL Document Control

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| DOCCTRL01 | Controlled document | Output is official procedure/spec | Assign owner, version, approval | Controlled doc |
| DOCCTRL02 | Draft control | Draft not approved for use | Mark draft and restrict use | Draft label |
| DOCCTRL03 | Version control | Multiple versions exist | Identify current version and history | Version record |
| DOCCTRL04 | Change control | Document changed materially | Log reason, reviewer, approval | Change record |
| DOCCTRL05 | Distribution control | Users need correct version | Publish current version and remove stale copies | Distribution log |
| DOCCTRL06 | Template control | Reusable template needs governance | Version and approve template | Template record |
| DOCCTRL07 | Translation control | Localized document may drift | Link translation to source version | Translation record |
| DOCCTRL08 | Obsolete control | Old document should not be used | Mark obsolete and redirect | Obsolete label |
| DOCCTRL09 | Retention control | Document needs retention rule | Set retention and archive path | Retention note |
| DOCCTRL10 | Document audit | Need verify document system health | Check owner/version/status/index | Doc audit |

## RECORDQA Quality Records

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| RECORDQA01 | Record definition | Need know what counts as record | Define record type and required fields | Record spec |
| RECORDQA02 | Record creation | Evidence must be captured | Create record at required workflow point | Record entry |
| RECORDQA03 | Record completeness | Record may miss fields | Validate required metadata | Completeness check |
| RECORDQA04 | Record retention | Record must be kept | Set keep/delete rule | Retention record |
| RECORDQA05 | Record retrieval | Audit needs fast lookup | Index record by code/date/owner | Retrieval index |
| RECORDQA06 | Record integrity | Record must not be altered silently | Protect or log modifications | Integrity log |
| RECORDQA07 | Record privacy | Record may contain sensitive data | Redact/restrict access | Privacy record |
| RECORDQA08 | Record transfer | Record moves between owners/systems | Track handoff and receipt | Transfer record |
| RECORDQA09 | Record disposal | Record eligible for deletion | Dispose under retention rule | Disposal proof |
| RECORDQA10 | Record audit | Need prove records are adequate | Sample and report records | Record audit |

## SIGNQA Review / Signoff

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| SIGNQA01 | Self signoff | Executor certifies basic completion | Use checklist before handoff | Self signoff |
| SIGNQA02 | Peer signoff | Peer validates quality | Peer review required for risk/quality | Peer signoff |
| SIGNQA03 | SME signoff | Domain expert validates specialized content | SME approves defined scope | SME signoff |
| SIGNQA04 | Owner signoff | Accountable owner accepts outcome | Owner signs against acceptance criteria | Owner signoff |
| SIGNQA05 | Client signoff | External client accepts delivery | Capture client approval or comments | Client signoff |
| SIGNQA06 | Compliance signoff | Compliance/legal/security gate required | Gate owner approves | Compliance signoff |
| SIGNQA07 | Release signoff | Artifact/process goes live | All required gates pass | Release signoff |
| SIGNQA08 | Exception signoff | Deviation accepted | Approver signs residual risk | Exception signoff |
| SIGNQA09 | Conditional signoff | Approval depends on follow-up | Record conditions and owner | Conditional signoff |
| SIGNQA10 | Signoff audit | Need verify approvals are valid | Check authority, scope, timestamp | Signoff audit |

## CERTQA Certification / External Audit Readiness

| Code | Audit need | Required setup | Control | Evidence |
|---|---|---|---|---|
| CERTQA01 | Audit scope readiness | External audit scope known | Map processes, records, owners | Audit scope |
| CERTQA02 | Evidence binder | Evidence must be packaged | Assemble required packets by requirement | Evidence binder |
| CERTQA03 | Control matrix | Controls must map to requirements | Create requirement-control-evidence table | Control matrix |
| CERTQA04 | Internal audit | Practice audit before external review | Run sample audit and findings | Internal audit |
| CERTQA05 | Audit finding response | Auditor raises finding | Record response, owner, corrective action | Finding response |
| CERTQA06 | Certification gap | Requirement not met | Record gap, risk, remediation plan | Gap register |
| CERTQA07 | Management review | Leadership review required | Summarize performance, risks, actions | Mgmt review |
| CERTQA08 | Supplier audit | Supplier evidence required | Request and review supplier records | Supplier audit |
| CERTQA09 | Renewal readiness | Certification/reporting renewal due | Verify current evidence and changes | Renewal packet |
| CERTQA10 | Audit closeout | External/internal audit complete | Archive findings, actions, signoff | Audit closeout |
