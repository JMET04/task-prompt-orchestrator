# Professional Workflow Governance and Policy Matrix

Use this when a workflow must operate under policy, compliance, privacy, security, audit, AI governance, data governance, finance controls, legal review, brand rules, vendor controls, safety requirements, or accessibility standards. Governance rules convert "be careful" into explicit gates, evidence, owners, and stop conditions.

Selection rule:

1. Identify which governance domain applies.
2. Select the closest governance code.
3. Add policy boundary, required control, owner, evidence, and escalation path to the prompt packet.
4. Treat unknown governance status as a risk until reviewed or scoped out.

## POLICY Policy Boundaries

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| POLICY01 | Internal policy | Check applicable rule before execution | Policy reference or no-policy note | Policy owner |
| POLICY02 | External regulation | Identify jurisdiction and rule | Regulation/source/date | Legal/compliance |
| POLICY03 | Terms of service | Check platform/tool terms | Terms note | Tool/platform owner |
| POLICY04 | Content policy | Route unsafe/restricted content | Policy-safe output | Safety reviewer |
| POLICY05 | Data policy | Limit collection/use/storage | Data handling note | Data owner |
| POLICY06 | Publishing policy | Approve before public release | Publishing approval | Communications owner |
| POLICY07 | Procurement policy | Follow vendor/spend rules | Procurement record | Procurement owner |
| POLICY08 | Recordkeeping policy | Preserve required evidence | Retention/archive record | Records owner |
| POLICY09 | Exception policy | Require rationale and owner | Exception approval | Exception approver |
| POLICY10 | Policy uncertainty | Rule unclear or unavailable | Uncertainty note and safe fallback | Policy escalation |

## PRIVG Privacy Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| PRIVG01 | Data minimization | Use only necessary personal data | Minimal field list | Privacy owner |
| PRIVG02 | Purpose limitation | Use data only for stated purpose | Purpose note | Privacy/compliance |
| PRIVG03 | Redaction | Remove direct identifiers where possible | Redaction log | Data owner |
| PRIVG04 | Consent/legal basis | Confirm permission/legal basis | Consent/legal-basis note | Legal/privacy |
| PRIVG05 | Retention | Define keep/delete period | Retention record | Records owner |
| PRIVG06 | Access control | Restrict who can see/use data | Access note | Security/privacy |
| PRIVG07 | External sharing | Gate sharing outside allowed audience | Sharing approval | Privacy/legal |
| PRIVG08 | Sensitive category | Add stronger controls for sensitive data | Sensitive-data handling note | Privacy officer |
| PRIVG09 | Deletion request | Handle deletion/correction request | Request and action record | Privacy owner |
| PRIVG10 | Privacy incident | Stop, preserve evidence, notify owner | Incident packet | Privacy/security |

## SECG Security Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| SECG01 | Secret handling | Never expose secrets; store status only | Secret-safe note | Security owner |
| SECG02 | Least privilege | Use minimal access needed | Access scope note | Security/admin |
| SECG03 | Threat review | Check abuse/misuse path | Threat note | Security reviewer |
| SECG04 | Vulnerability handling | Triage, verify, fix, validate | Finding record | Security owner |
| SECG05 | Secure command execution | Scope risky commands and paths | Command log | Technical owner |
| SECG06 | Dependency security | Check vulnerable/outdated dependencies | Dependency note | Security/engineering |
| SECG07 | Authentication control | Confirm auth method and session safety | Auth note | Security/admin |
| SECG08 | Authorization control | Confirm actor can perform action | Authorization note | System owner |
| SECG09 | Security logging | Preserve action/audit trail | Security log | Security/audit |
| SECG10 | Security incident | Isolate, report, recover, postmortem | Incident report | Security lead |

## AUDG Audit Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| AUDG01 | Evidence trail | Preserve source, action, decision, result | Evidence ledger | Audit owner |
| AUDG02 | Decision audit | Record options, criteria, rationale | Decision log | Decision owner |
| AUDG03 | Change audit | Record what changed and why | Changelog/diff | Change owner |
| AUDG04 | Approval audit | Tie approval to artifact version | Approval record | Approver |
| AUDG05 | Source audit | Record source reliability/freshness | Source inventory | Research owner |
| AUDG06 | Command audit | Record command, cwd, result | Command log | Technical owner |
| AUDG07 | Data audit | Record lineage and transforms | Data provenance | Data owner |
| AUDG08 | Access audit | Record actor/resource/action | Access log | Security owner |
| AUDG09 | Exception audit | Record deviation and acceptance | Exception log | Exception approver |
| AUDG10 | Closeout audit | Map requirements to proof | Completion audit | Goal owner |

## AIG AI Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| AIG01 | AI use disclosure | State where AI assists if needed | AI-use note | Governance owner |
| AIG02 | Human oversight | Require human review for high-impact AI output | Review record | Responsible owner |
| AIG03 | Evaluation set | Test prompts/agents on representative cases | Eval result | AI owner |
| AIG04 | Model/tool limitation | Document known limits and uncertainty | Limitation note | AI owner |
| AIG05 | AI output verification | Verify factual/high-impact claims | Verification table | Reviewer |
| AIG06 | Bias/fairness check | Check protected/fairness impact | Fairness note | HR/legal/compliance |
| AIG07 | Prompt/version control | Track prompt/model/tool version | Version record | AI maintainer |
| AIG08 | AI safety boundary | Route unsafe requests to safe alternatives | Safety route | Safety owner |
| AIG09 | AI audit log | Preserve prompt, inputs, outputs when appropriate | AI audit log | Audit owner |
| AIG10 | AI retirement | Disable outdated/unsafe AI workflow | Retirement note | AI governance |

## DATAG Data Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| DATAG01 | Data ownership | Name data owner/steward | Data owner note | Data steward |
| DATAG02 | Data dictionary | Define fields, metrics, grain | Data dictionary | Data owner |
| DATAG03 | Data quality | Profile missing/duplicate/outlier issues | Quality report | Data steward |
| DATAG04 | Data lineage | Track source and transform | Lineage note | Data owner |
| DATAG05 | Data access | Limit access by role/purpose | Access record | Data/security |
| DATAG06 | Data freshness | Define refresh threshold | Freshness report | Data owner |
| DATAG07 | Data retention | Define retention/disposal | Retention note | Records owner |
| DATAG08 | Data sharing | Gate export/sharing | Sharing approval | Data/privacy |
| DATAG09 | Data reconciliation | Reconcile totals/keys | Reconciliation report | Data owner |
| DATAG10 | Data incident | Stop use, preserve evidence, escalate | Data incident report | Data/security |

## FING Financial Controls

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| FING01 | Budget approval | Require approval above threshold | Budget approval | Budget owner |
| FING02 | Spend tracking | Track cost by run/tool/vendor | Cost log | Finance owner |
| FING03 | Financial assumption | State assumption/source/sensitivity | Assumption note | Finance reviewer |
| FING04 | Forecast control | Define scenario and caveat | Forecast packet | Finance owner |
| FING05 | Procurement control | Follow vendor/procurement route | Procurement record | Procurement |
| FING06 | Invoice/payment control | Reconcile invoice/payment data | Reconciliation note | Finance/AP |
| FING07 | Revenue/metric control | Validate metric definition and source | Metric validation | Finance/data |
| FING08 | Cost-benefit review | Compare value to cost | ROI note | Finance/business |
| FING09 | Financial risk gate | Review material financial exposure | Risk approval | Finance/legal |
| FING10 | Audit-ready finance | Preserve evidence and formulas | Finance audit pack | Finance/audit |

## LEGALG Legal Review

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| LEGALG01 | Contract review | Extract clauses, obligations, risks | Clause table | Legal owner |
| LEGALG02 | Terms/claims review | Check public claims and commitments | Claim substantiation | Legal/comms |
| LEGALG03 | Jurisdiction review | Identify governing jurisdiction | Jurisdiction note | Legal |
| LEGALG04 | IP rights review | Check ownership/license/usage | Rights note | Legal/IP |
| LEGALG05 | Employment/legal fairness | Check HR/legal fairness | Fairness note | Legal/HR |
| LEGALG06 | Consumer/regulatory review | Check consumer-facing obligations | Compliance note | Legal/compliance |
| LEGALG07 | Legal caveat | Avoid legal advice overclaim | Caveat and escalation | Legal |
| LEGALG08 | Legal hold | Preserve records when needed | Hold record | Legal/records |
| LEGALG09 | Legal exception | Approve deviation from standard terms | Exception approval | Legal approver |
| LEGALG10 | Legal closeout | Record final legal decision/caveat | Legal closeout | Legal owner |

## BRANDG Brand / Reputation Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| BRANDG01 | Brand voice | Check tone against brand | Brand QA note | Brand owner |
| BRANDG02 | Visual identity | Check logo/color/type/asset use | Visual brand QA | Brand/design |
| BRANDG03 | Claim substantiation | Verify marketing/public claims | Evidence table | Brand/legal |
| BRANDG04 | Audience sensitivity | Check cultural/context risk | Sensitivity note | Comms/brand |
| BRANDG05 | Reputation risk | Assess potential public backlash | Reputation risk note | Comms lead |
| BRANDG06 | Crisis messaging | Use factual, approved, non-speculative message | Crisis message | Comms/legal |
| BRANDG07 | Sponsorship/partner brand | Check co-brand rules | Partner brand approval | Partner owner |
| BRANDG08 | Asset rights | Confirm image/media/font rights | Rights record | Legal/brand |
| BRANDG09 | Brand exception | Approve off-brand deviation | Exception note | Brand approver |
| BRANDG10 | Brand archive | Store approved brand assets/output | Brand archive | Brand/design |

## VENDG Vendor / Third-Party Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| VENDG01 | Vendor selection | Use criteria and due diligence | Vendor comparison | Procurement |
| VENDG02 | Vendor access | Limit vendor data/system access | Access record | Security/procurement |
| VENDG03 | Vendor SLA | Track service commitment | SLA record | Vendor owner |
| VENDG04 | Vendor data handling | Confirm data/privacy obligations | DPA/privacy note | Legal/privacy |
| VENDG05 | Vendor security | Check security posture or controls | Security review | Security |
| VENDG06 | Vendor cost | Track spend and renewal | Vendor cost note | Finance/procurement |
| VENDG07 | Vendor performance | Monitor quality/timeliness | Vendor scorecard | Vendor owner |
| VENDG08 | Vendor incident | Escalate vendor failure | Incident/escalation note | Vendor owner |
| VENDG09 | Vendor exit | Plan migration/offboarding | Exit plan | Procurement/security |
| VENDG10 | Vendor archive | Preserve contract/SLA/evidence | Vendor archive | Procurement |

## SAFEG Safety / Physical Controls

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| SAFEG01 | Physical safety | Identify hazards and stop rules | Safety note | Safety owner |
| SAFEG02 | Manufacturing safety | Check materials/tolerances/warnings | Manufacturing safety QA | Engineering/safety |
| SAFEG03 | Product use safety | Include safe-use instructions | Safety instructions | Product/safety |
| SAFEG04 | Medical/health safety | Avoid unsupported health guidance | Medical caveat/review | Medical reviewer |
| SAFEG05 | Child/vulnerable user safety | Add stronger safeguards | Vulnerable-user note | Safety/legal |
| SAFEG06 | Operational safety | Check runbook risks and emergency stops | Ops safety note | Ops/safety |
| SAFEG07 | Unsafe workaround | Reject shortcut that increases harm | Safe alternative | Safety owner |
| SAFEG08 | Safety incident | Stop, report, recover | Safety incident report | Safety lead |
| SAFEG09 | Safety approval | Require approval before risky release | Safety signoff | Safety approver |
| SAFEG10 | Safety closeout | Record residual risk and controls | Safety closeout | Safety owner |

## ACCG Accessibility / Inclusion Governance

| Code | Governance area | Control | Required evidence | Escalation |
|---|---|---|---|---|
| ACCG01 | Accessibility requirement | Identify target accessibility needs | Accessibility note | Accessibility owner |
| ACCG02 | Alt text/media access | Provide alt/caption/transcript when needed | Alt/caption record | Content owner |
| ACCG03 | Readability | Match reading level and clarity | Readability check | Content owner |
| ACCG04 | Color/contrast | Check contrast and non-color cues | Visual accessibility QA | Design owner |
| ACCG05 | Keyboard/navigation | Ensure keyboard/user flow where applicable | UX/accessibility QA | Product/design |
| ACCG06 | Localization inclusion | Adapt language/culture/locale | Localization note | Localization owner |
| ACCG07 | Bias/fairness inclusion | Check unfair exclusion or stereotypes | Inclusion review | HR/legal/brand |
| ACCG08 | Accommodation request | Handle specific accessibility need | Accommodation note | Accessibility owner |
| ACCG09 | Accessibility exception | Document unmet need and mitigation | Exception record | Accessibility approver |
| ACCG10 | Accessibility closeout | Record checks and residual gaps | Accessibility closeout | Accessibility owner |
