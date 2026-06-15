# Professional Workflow Telecommunications Network Service Operations Matrix

Use this matrix when a workflow must plan, operate, support, secure, monitor, improve, or govern telecommunications, broadband, mobile, fiber, fixed wireless, satellite, voice, messaging, network infrastructure, service activation, incidents, field operations, billing, and telecom customer experience.

## Telecom Network Scope

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| TELCOSCOPE01 | What telecommunications workflow is involved? | Define mobile, fiber, broadband, fixed wireless, satellite, voice, messaging, enterprise circuit, wholesale, MVNO, IoT, or emergency communications context. |
| TELCOSCOPE02 | Who depends on the service? | Identify consumers, businesses, carriers, public safety, critical infrastructure, wholesale partners, field teams, regulators, and internal operators. |
| TELCOSCOPE03 | What service promise matters? | Define availability, coverage, speed, latency, capacity, installation date, repair SLA, security, privacy, and billing accuracy expectations. |
| TELCOSCOPE04 | What network layer is in scope? | Map access, transport, core, IP, DNS, OSS/BSS, radio, fiber plant, customer premises equipment, cloud edge, or interconnect layer. |
| TELCOSCOPE05 | What geography and topology apply? | Capture service area, cell sites, exchanges, cabinets, POPs, fiber routes, backhaul, peering, and customer locations. |
| TELCOSCOPE06 | What commercial or regulatory constraint applies? | Include franchise, universal service, spectrum, number portability, emergency calling, lawful access, wholesale terms, or service credits. |
| TELCOSCOPE07 | What customer impact must be protected? | Define affected subscribers, enterprise SLAs, vulnerable users, emergency services, critical sites, and outage communication obligations. |
| TELCOSCOPE08 | What systems and data are involved? | Identify OSS, BSS, CRM, inventory, NMS, telemetry, GIS, workforce, billing, provisioning, trouble ticket, and data lake systems. |
| TELCOSCOPE09 | What safety or security boundary applies? | Check tower work, excavation, fiber splicing, electrical hazards, cyber risk, lawful intercept controls, privacy, and access permissions. |
| TELCOSCOPE10 | What final telecom artifact is required? | Produce network plan, activation runbook, incident report, field work order, capacity plan, regulatory response, dashboard, or improvement roadmap. |

## Network Planning Capacity And Architecture

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| TELPLAN01 | What network planning decision is needed? | Define coverage expansion, capacity upgrade, fiber build, spectrum use, peering, core upgrade, resiliency, or decommissioning decision. |
| TELPLAN02 | What demand and traffic evidence is required? | Use subscriber growth, traffic forecast, busy-hour load, enterprise demand, latency, complaints, dropped sessions, and event demand. |
| TELPLAN03 | What architecture option should be compared? | Compare fiber, wireless, small cell, microwave, satellite, edge compute, caching, route diversity, and vendor platform options. |
| TELPLAN04 | What capacity constraint exists? | Identify spectrum, ports, fiber strands, backhaul, power, cooling, IP addresses, licenses, processing, and cabinet/rack capacity. |
| TELPLAN05 | What site or right-of-way dependency applies? | Track tower lease, pole attachment, conduit, permits, landlord access, easements, municipalities, and environmental constraints. |
| TELPLAN06 | What redundancy or diversity is required? | Define dual homing, ring topology, alternate backhaul, battery/generator backup, route diversity, and failover targets. |
| TELPLAN07 | What vendor or technology lifecycle matters? | Account for hardware support, software versions, vendor roadmap, interoperability, spares, and end-of-life risk. |
| TELPLAN08 | What cost and funding model applies? | Estimate capex, opex, spectrum fees, installation, maintenance, subsidy, ROI, service credits, and cost per passed premise. |
| TELPLAN09 | What approval and implementation package is needed? | Prepare architecture diagram, bill of materials, cutover plan, risk register, permits, budget approval, and acceptance tests. |
| TELPLAN10 | What planning evidence must be archived? | Store forecasts, assumptions, maps, design choices, approvals, vendor inputs, capacity model, and review cadence. |

## Radio Access Mobile And Spectrum Operations

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| RANOPS01 | What radio access workflow is involved? | Define macro cell, small cell, DAS, private network, spectrum refarm, optimization, outage, interference, or site launch. |
| RANOPS02 | What coverage or quality issue exists? | Evaluate RSRP/RSRQ/SINR, throughput, handover, dropped calls, congestion, indoor coverage, and customer complaints. |
| RANOPS03 | What spectrum or frequency plan applies? | Capture band, channel, license boundary, guard band, reuse, interference, sharing, and regulatory restrictions. |
| RANOPS04 | What site configuration must be managed? | Define antennas, azimuth, tilt, power, sectors, carriers, neighbor lists, software, alarms, and transmission path. |
| RANOPS05 | What optimization action is needed? | Recommend parameter tuning, antenna adjustment, carrier add, small cell, backhaul upgrade, load balancing, or feature activation. |
| RANOPS06 | What field or tower work is required? | Plan access, safety, weather, rigging, outage window, permits, materials, vendor crew, and post-work validation. |
| RANOPS07 | What service launch gate applies? | Verify integration, call/data tests, emergency calling, alarms, handover, backhaul, documentation, and monitoring. |
| RANOPS08 | What interference investigation is needed? | Locate source, correlate alarms, test spectrum, coordinate with regulator/vendor, mitigate, and document evidence. |
| RANOPS09 | What RAN metrics matter? | Track availability, accessibility, retainability, throughput, latency, utilization, complaints, and dropped sessions. |
| RANOPS10 | What RAN record must be retained? | Archive site config, test results, changes, alarms, optimization notes, approvals, and performance before/after. |

## Core Network IP And Interconnect Operations

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| CORENET01 | What core or IP network workflow is involved? | Define packet core, voice core, IMS, routing, DNS, peering, transit, interconnect, firewall, NAT, or service platform workflow. |
| CORENET02 | What dependency map is required? | Map nodes, links, VNFs/CNFs, cloud zones, routing domains, vendors, upstreams, downstream services, and customer segments. |
| CORENET03 | What change or capacity action is needed? | Plan software upgrade, route change, capacity add, policy change, new peer, firewall rule, or service migration. |
| CORENET04 | What routing or interconnect control applies? | Manage BGP, MPLS, QoS, SIP trunks, number routing, peering policy, route filters, and failover rules. |
| CORENET05 | What security control is required? | Protect management access, DDoS, signaling security, segmentation, secrets, lawful access boundaries, and audit logs. |
| CORENET06 | What maintenance window and rollback applies? | Define window, customer impact, pre-checks, backout, validation, escalation, and communication. |
| CORENET07 | What interoperability test is needed? | Test vendor compatibility, roaming, emergency calling, SMS/voice/data, QoS, billing mediation, and monitoring. |
| CORENET08 | What incident or alarm must be handled? | Triage node failure, routing leak, congestion, packet loss, DNS issue, registration failure, or signaling storm. |
| CORENET09 | What core network metrics matter? | Track availability, sessions, throughput, packet loss, latency, signaling load, call completion, and error rates. |
| CORENET10 | What core network evidence is required? | Archive topology, configs, change record, test evidence, alarms, approvals, and post-change performance. |

## Broadband Fiber And Customer Premises Operations

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| BROADBAND01 | What broadband or fixed access workflow is involved? | Define fiber, DSL, cable, fixed wireless, satellite, enterprise circuit, CPE install, repair, upgrade, or migration. |
| BROADBAND02 | What service qualification is needed? | Check address, plant availability, port capacity, line distance, signal levels, ONT/CPE support, and construction need. |
| BROADBAND03 | What installation path applies? | Plan self-install, technician install, drop build, inside wiring, equipment shipment, appointment, and activation. |
| BROADBAND04 | What speed or quality issue must be diagnosed? | Check sync, optical power, Wi-Fi, CPE, congestion, packet loss, latency, firmware, and customer device factors. |
| BROADBAND05 | What outside plant work is needed? | Manage survey, locates, trenching, aerial work, splicing, cabinet work, permits, and restoration. |
| BROADBAND06 | What customer premises work is needed? | Define access, wiring, ONT/router placement, Wi-Fi coverage, safety, customer education, and acceptance test. |
| BROADBAND07 | What outage or degradation response applies? | Handle fiber cut, power issue, equipment failure, node congestion, storm damage, or multi-dwelling access issue. |
| BROADBAND08 | What equipment lifecycle action applies? | Ship, swap, reclaim, refurbish, firmware update, replace, or retire CPE and accessories. |
| BROADBAND09 | What broadband metrics matter? | Track install cycle time, first-time-right, speed attainment, trouble repeat, churn, utilization, and repair time. |
| BROADBAND10 | What broadband evidence must be archived? | Store service qualification, work order, test results, photos, CPE serial, customer acceptance, and closeout notes. |

## Provisioning Activation And Numbering

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| PROVACT01 | What service provisioning workflow is needed? | Define new activation, upgrade, downgrade, migration, disconnect, suspend, restore, number port, SIM/eSIM, or enterprise circuit. |
| PROVACT02 | What order data must be validated? | Check customer, address, product, eligibility, credit/KYC where applicable, appointment, equipment, and consent. |
| PROVACT03 | What resource assignment is required? | Assign number, SIM, IP, port, VLAN, circuit, device, service profile, CPE, or network slice. |
| PROVACT04 | What activation sequence applies? | Coordinate order entry, inventory reservation, network config, equipment shipment, field task, test, and billing start. |
| PROVACT05 | What number portability or identity process applies? | Validate authorization, donor carrier, LOA, port window, emergency address, SMS/voice routing, and fallback. |
| PROVACT06 | What provisioning fallout must be handled? | Resolve inventory mismatch, failed config, duplicate order, address error, port rejection, missing equipment, or billing mismatch. |
| PROVACT07 | What customer communication is needed? | Send order confirmation, appointment, activation status, port timing, outage notice, instructions, and completion confirmation. |
| PROVACT08 | What test and acceptance gate applies? | Verify service registration, speed, voice/SMS/data, emergency calling, CPE status, billing trigger, and customer acceptance. |
| PROVACT09 | What provisioning metrics matter? | Track cycle time, fallout rate, first-time-right, missed appointments, port success, activation defects, and rework. |
| PROVACT10 | What activation record must be retained? | Archive order, resource assignment, config, tests, customer notices, exceptions, approvals, and billing handoff. |

## Network Incidents Outages And Service Assurance

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| NETINC01 | What network incident is involved? | Classify outage, degradation, congestion, fiber cut, power failure, cyber event, vendor fault, weather damage, or planned maintenance issue. |
| NETINC02 | What impact assessment is required? | Estimate affected customers, services, geography, critical sites, enterprise SLAs, emergency services, and revenue impact. |
| NETINC03 | What triage and escalation path applies? | Assign severity, incident commander, network owner, vendor, field crew, communications, and executive escalation. |
| NETINC04 | What diagnostic evidence is needed? | Gather alarms, telemetry, logs, topology, recent changes, trouble tickets, field reports, and customer symptoms. |
| NETINC05 | What restoration action should be taken? | Implement reroute, failover, rollback, dispatch, equipment swap, capacity relief, vendor ticket, or workaround. |
| NETINC06 | What customer or regulator notification is needed? | Prepare outage page, enterprise notice, public-safety notice, regulator report, credits notice, and internal updates. |
| NETINC07 | What change freeze or risk control applies? | Pause risky changes, protect restoration path, require approvals, and document exceptions. |
| NETINC08 | What post-incident review is required? | Produce timeline, root cause, contributing factors, customer impact, corrective actions, and owner/due dates. |
| NETINC09 | What service assurance metrics matter? | Track MTTA, MTTR, availability, repeat incidents, affected customers, SLA breaches, and corrective-action closure. |
| NETINC10 | What incident evidence must be archived? | Store tickets, alarms, logs, decisions, communications, restoration evidence, credits, and postmortem. |

## Telecom Field Construction And Maintenance

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| FIELDNET01 | What telecom field work is needed? | Define survey, install, repair, splice, tower work, cabinet work, fiber locate, equipment swap, site audit, or preventive maintenance. |
| FIELDNET02 | What location and access details are required? | Capture address, site ID, coordinates, contact, access window, landlord, permit, keys, hazards, and weather constraints. |
| FIELDNET03 | What safety controls apply? | Manage working at height, electrical hazards, excavation, traffic control, RF exposure, confined space, PPE, and stop-work authority. |
| FIELDNET04 | What materials and tools are needed? | Reserve cable, connectors, optics, radios, CPE, SIMs, meters, splicing gear, ladders, lifts, and spare parts. |
| FIELDNET05 | What crew or vendor assignment applies? | Match skills, certifications, geography, availability, union/contract rules, and SLA priority. |
| FIELDNET06 | What field test must be completed? | Capture OTDR, optical power, speed, signal, call/data, grounding, alarms, photos, and customer acceptance. |
| FIELDNET07 | What exception path is required? | Handle no access, missing permit, damaged plant, unsafe condition, insufficient materials, or customer no-show. |
| FIELDNET08 | What restoration or cleanup is required? | Restore sidewalk/roadway, remove debris, label assets, update drawings, and notify affected stakeholders. |
| FIELDNET09 | What field metrics matter? | Track first-time-right, repeat truck rolls, repair time, missed appointments, safety incidents, and cost per job. |
| FIELDNET10 | What field record must be updated? | Close work order, update inventory/GIS/OSS, upload tests/photos, record serials, and trigger billing/support follow-up. |

## Telecom Customer Care Billing And Revenue

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| TELBILL01 | What customer care or billing issue is involved? | Classify plan change, high bill, roaming charge, outage credit, device installment, payment, collections, cancellation, or dispute. |
| TELBILL02 | What account and entitlement data is needed? | Review customer identity, products, discounts, contract, device, usage, payment, credit status, and consent. |
| TELBILL03 | What rating or tariff logic applies? | Check plan, usage units, roaming, taxes/fees, proration, promotions, bundles, overage, and enterprise contract terms. |
| TELBILL04 | What service credit or adjustment workflow applies? | Validate outage, SLA, billing error, goodwill limit, approval authority, customer notice, and ledger impact. |
| TELBILL05 | What collections or suspension boundary applies? | Apply notices, grace periods, hardship rules, payment plans, reconnection, and regulatory restrictions. |
| TELBILL06 | What retention or save action is allowed? | Offer plan review, discount, device option, service fix, escalation, or cancellation with clear policy boundaries. |
| TELBILL07 | What dispute evidence is needed? | Gather bills, usage records, tickets, outage data, call notes, contract terms, and prior adjustments. |
| TELBILL08 | What customer communication is required? | Explain charges, usage, credits, next bill impact, dispute rights, technical steps, and escalation path. |
| TELBILL09 | What revenue metrics matter? | Track ARPU, churn, collections, dispute rate, credits, bad debt, plan mix, usage, and retention outcomes. |
| TELBILL10 | What billing audit record is required? | Archive rating logic, adjustments, approvals, communications, payments, dispute findings, and retention actions. |

## Telecom Regulatory Compliance And Public Obligations

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| TELREG01 | What telecom obligation applies? | Identify spectrum, emergency calling, outage reporting, privacy, lawful intercept, accessibility, universal service, or consumer protection rule. |
| TELREG02 | What jurisdiction and authority matter? | Map national regulator, local authority, public safety agency, data protection body, franchise authority, or industry code. |
| TELREG03 | What service or product is regulated? | Define voice, broadband, mobile, messaging, enterprise service, IoT, emergency service, or wholesale offering. |
| TELREG04 | What reporting or filing is required? | Prepare outage report, coverage report, subscriber report, QoS filing, spectrum filing, consumer complaint response, or audit evidence. |
| TELREG05 | What customer notice or disclosure is required? | Provide price, speed, data cap, privacy, contract, cancellation, accessibility, emergency limitation, and complaint disclosures. |
| TELREG06 | What lawful access or data request boundary applies? | Verify authority, scope, minimization, approval, logging, retention, and confidentiality. |
| TELREG07 | What accessibility or vulnerable-user support applies? | Support relay services, accessible billing, emergency address accuracy, language access, and medical/priority repair programs. |
| TELREG08 | What compliance calendar is needed? | Track license renewals, filings, audits, policy updates, training, and control tests. |
| TELREG09 | What compliance metrics matter? | Track complaint rate, outage reporting timeliness, filing completeness, audit findings, accessibility requests, and corrective actions. |
| TELREG10 | What compliance record must be retained? | Archive filings, notices, approvals, evidence, customer records, requests, correspondence, and remediation closure. |

## Telecom Data Platforms Automation And Security

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| TELDATA01 | What telecom data or automation workflow is involved? | Define telemetry, inventory, assurance, provisioning, billing, customer analytics, capacity planning, fraud, or automation workflow. |
| TELDATA02 | What data integration is required? | Join network events, tickets, orders, inventory, usage, billing, customer, device, location, and field work data. |
| TELDATA03 | What data quality controls apply? | Validate timestamps, service IDs, topology, location, units, duplicate alarms, stale inventory, missing telemetry, and late records. |
| TELDATA04 | What automation use case exists? | Define alarm correlation, auto-healing, dispatch optimization, capacity prediction, churn prediction, fraud detection, or provisioning automation. |
| TELDATA05 | What privacy boundary applies? | Protect location, usage, call/message metadata, customer identity, payment, lawful-access records, and employee data. |
| TELDATA06 | What cybersecurity risk applies? | Protect OSS/BSS, network management, APIs, credentials, vendor access, signaling, DDoS response, and backup/recovery. |
| TELDATA07 | What human approval is required? | Require operator review for service-affecting automation, customer denial, billing correction, lawful request, or public communication. |
| TELDATA08 | What dashboard or alert is needed? | Build availability, capacity, activation, truck roll, churn, billing, fraud, SLA, or compliance dashboard. |
| TELDATA09 | What lineage and reproducibility must be preserved? | Store source, transformations, metric definitions, model versions, automation decisions, approvals, and timestamps. |
| TELDATA10 | What lifecycle governance applies? | Define owner, access review, retention, backup, vendor SLA, change control, testing, and decommissioning. |

## Telecom Resilience Continuity And Emergency Communications

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| TELRES01 | What resilience risk threatens service? | Identify storm, wildfire, flood, power outage, fiber cut, cyberattack, vendor outage, congestion, or supply shortage. |
| TELRES02 | What critical service priority applies? | Prioritize emergency calling, public safety, hospitals, government, enterprise SLAs, vulnerable users, and high-traffic areas. |
| TELRES03 | What continuity plan is needed? | Define backup power, mobile cell, route diversity, spare parts, emergency crews, vendor support, and customer communications. |
| TELRES04 | What degraded mode is acceptable? | Define minimum voice/data, emergency-only service, throttling, temporary routing, manual provisioning, or priority restoration. |
| TELRES05 | What restoration sequencing is required? | Sequence life safety, core, transport, access, enterprise, residential, and low-priority restoration. |
| TELRES06 | What exercise or simulation is needed? | Run disaster drill, cyber tabletop, fiber-cut simulation, power outage drill, or high-traffic event rehearsal. |
| TELRES07 | What mutual aid or vendor dependency exists? | Coordinate roaming, shared infrastructure, emergency suppliers, tower crews, fuel vendors, and government agencies. |
| TELRES08 | What resilience metrics matter? | Track backup runtime, restoration time, route diversity, critical site uptime, drill findings, and mitigation closure. |
| TELRES09 | What customer and public communication is needed? | Prepare outage maps, restoration estimates, emergency guidance, enterprise updates, and regulator/public statements. |
| TELRES10 | What resilience evidence must be archived? | Store risk assessment, continuity plan, drill records, incident learnings, investments, approvals, and updates. |

## Telecom Performance And Continuous Improvement

| Code | Question | Prompt/workflow requirement |
|---|---|---|
| TELPERF01 | What telecom performance question is being answered? | Define coverage, availability, speed, latency, activation, repair, churn, billing, complaint, safety, or compliance performance. |
| TELPERF02 | What metrics and definitions apply? | Use availability, throughput, latency, packet loss, dropped calls, install interval, MTTR, NPS, ARPU, churn, and complaint rate. |
| TELPERF03 | What benchmark or target is relevant? | Compare SLA, regulatory target, historic trend, peer market, product promise, board goal, or vendor scorecard. |
| TELPERF04 | What root-cause analysis is needed? | Analyze network, capacity, field execution, provisioning, vendor, billing, CPE, weather, demand, and customer education causes. |
| TELPERF05 | What improvement action is available? | Recommend capacity upgrade, process redesign, automation, training, vendor action, pricing fix, communication change, or policy update. |
| TELPERF06 | What customer and equity impact should be reviewed? | Assess underserved areas, accessibility, affordability, emergency reliance, language access, and complaint concentration. |
| TELPERF07 | What management report is required? | Produce operations review, network dashboard, regulator report, executive scorecard, vendor review, or improvement roadmap. |
| TELPERF08 | What corrective action tracking is needed? | Assign owner, due date, budget, status, verification metric, customer impact, and closure evidence. |
| TELPERF09 | What reusable learning should be captured? | Update design rules, field playbooks, provisioning checks, customer scripts, automation rules, and metric definitions. |
| TELPERF10 | What performance evidence must be archived? | Store source data, metric definitions, dashboards, reports, decisions, approvals, and follow-up results. |
