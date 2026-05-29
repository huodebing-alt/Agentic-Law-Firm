# Agent Catalogue

## orchestrator

- **task-router** — Primary user-facing dispatcher. Triages every incoming request, identifies practice area and matter type, and routes to the right specialist agent(s). Use as the default entry point for any legal request that is not /onboard.
- **task-decomposer** — Breaks large matters (full due diligence, group restructuring tax memo, multi-target IP audit) into a JSON sub-task plan, each sub-task tagged with the responsible specialist and whether it deserves a fresh context. Use when scope exceeds ~15 sub-tasks.
- **aggregator** — Synthesises outputs from multiple specialists into a single client-facing deliverable consistent with document style. Use as the final step before delivering a multi-specialist memo, due-diligence report, or compliance audit.
- **hard-gate-keeper** — Refuses to release sensitive output without explicit human approval. Use whenever a draft triggers any item on the AGENTS.md section 4 hard-gate list (filings, large deals, personal-rights documents, active-litigation pleadings, opposing-counsel-named correspondence).
- **matter-intake** — Captures structured intake data for a new matter (parties, jurisdiction, deadline, conflict-check prompts). Use whenever the operator says 'new matter' or starts a new client engagement.
- **conflict-check** — Runs a conflict check against the operator's internal client / opposing-party list and any external KM system. Use as a sub-step in matter-intake and before any external communication on a new matter.

## corporate

- **ma-specialist** — M&A specialist for due diligence, deal structuring, share purchase agreements, asset purchase agreements, equity transfer in China and cross-border. Use for mergers, acquisitions, restructuring, equity transfers, MBOs, asset deals.
- **corporate-governance** — Corporate governance specialist: board / shareholder resolutions, articles of association, governance structure, related-party transactions, fiduciary duty issues for Chinese companies and WFOEs.
- **company-formation** — Company formation specialist: incorporation of LLCs, joint ventures, WFOEs, branch / representative office setup in China. Use for new entity setup, registered capital advice, business scope drafting, SAMR filings.
- **joint-venture-cn** — Sino-foreign joint venture specialist: JV agreements, contribution arrangements, deadlock and exit mechanisms, post-Foreign Investment Law landscape. Use for JV formation, JV restructuring, JV dispute prevention.
- **shareholders-agreement** — Shareholders agreement specialist: drafting and reviewing SHAs including tag-along, drag-along, ROFR, ROFO, anti-dilution, board composition, reserved matters. Use for any equity-arrangement-among-shareholders matter.
- **private-equity-vc** — PE / VC specialist: term sheets, investment agreements (SPA + SHA), founder-vesting, ESOP, redemption / repurchase, anti-dilution, liquidation preference, IPO ratchet. Use for any China-PE / VC / growth-equity deal.
- **ipo-securities** — IPO and securities specialist: A-share, H-share, US-listing, prospectus drafting, sponsor liaison, CSRC filings, post-listing compliance. Use for any public offering or listed-company matter.
- **antitrust-specialist** — Antitrust / competition law specialist: merger control filings (SAMR), monopoly agreements, abuse of dominance, leniency, dawn raids, fair competition review. Use whenever a deal needs merger control or any conduct may breach the Anti-Monopoly Law.
- **antitrust-cn-eu-us** — Cross-jurisdiction antitrust coordinator: align SAMR, EU DG-COMP, US DOJ / FTC merger control on the same deal. Use for any deal that triggers multi-jurisdictional merger control.
- **data-protection-cn** — PRC data-protection specialist: PIPL, DSL, CSL, cross-border data transfer, security assessment (CAC), standard contract, personal information impact assessment. Use for any data-processing, cross-border transfer, or breach matter under PRC law.
- **data-protection-gdpr** — GDPR specialist: handles GDPR / UK-GDPR matters for cross-border deals, EU-facing products, SCCs, TIA, DPIA, breach notification, controllers vs processors. Use for any EU / UK personal-data matter.
- **fintech-specialist** — Fintech specialist: payments, third-party payment licensing (人民银行), virtual currency / crypto, robo-advisory, P2P legacy issues, online lending. Use for any fintech regulatory matter in China.
- **esg-specialist** — ESG specialist: ESG disclosure (CSRC, HKEX, EU CSRD), supply-chain due diligence, climate transition planning, board ESG oversight. Use for any ESG-disclosure, ESG-litigation, or ESG-investment matter.
- **anti-bribery-anti-corruption** — ABAC specialist: FCPA, UK Bribery Act, PRC commercial bribery / Anti-Unfair-Competition-Law, internal investigations, dawn raids, third-party DD. Use for any bribery investigation or ABAC compliance matter.
- **export-control-sanctions** — Export control and sanctions specialist: PRC export-control regime, US OFAC, EU dual-use, UK sanctions, end-user verification, licence applications. Use for any export, sanctions screening, or unverified-list matter.
- **corporate-secretarial-cn** — Corporate secretarial specialist: annual report, statistical report (商务部 if FIE), corporate-record maintenance, director / officer changes, capital changes. Use for ongoing corporate-secretarial work for PRC entities.
- **outbound-investment-cn** — PRC outbound investment specialist: NDRC, MOFCOM, SAFE filings for outbound investment, sensitive sectors and countries. Use for any PRC outbound investment matter.
- **inbound-investment-cn** — Inbound investment specialist (post-Foreign Investment Law): negative list, MOFCOM record, sectoral access, national security review. Use for any inbound-investment matter into China.

## individual

- **family-law-cn** — Family law specialist: divorce, custody, division of property, prenuptial / postnuptial agreements, inheritance under PRC Civil Code Book V. Use for any individual family matter under PRC law.
- **estate-planning-cn** — Estate planning specialist (PRC): wills, trusts (limited), succession plans, cross-border estate planning. Use for any individual wealth-transfer matter.
- **estate-planning-cross-border** — Cross-border estate specialist: handles dual-domicile, foreign assets, multi-jurisdiction wills, situs-based inheritance tax planning. Use for individuals with assets in two or more jurisdictions.
- **individual-tax-cn** — Individual income tax specialist (PRC): IIT residency, comprehensive income, business income, capital gains, equity-incentive tax, individual tax planning. Use for any PRC individual income tax matter.
- **immigration-cn** — PRC immigration specialist: work permit (Z visa), residence permit, foreign-expert categorisation (A/B/C), R visa, permanent residence. Use for any inbound immigration to China.
- **immigration-outbound** — Outbound immigration coordinator (CN -> US / UK / EU / SG / HK / AU / CA): triages outbound visa options (work, investment, talent, study) and routes to local counsel. Use for individuals seeking to relocate out of China.
- **personal-injury-cn** — Personal injury specialist: traffic accidents, medical malpractice, workplace injury (工伤), product injury under PRC Tort Liability rules. Use for any individual personal-injury matter.
- **consumer-protection-cn** — Consumer protection specialist: 《消费者权益保护法》, e-commerce platform disputes, defective goods, deceptive marketing. Use for any consumer matter on either side (consumer or merchant).
- **small-business-counsel** — Counsel for small businesses and self-employed individuals: business licence, basic contracts, basic tax, supplier disputes. Use for sole-proprietor and small-shop matters.

## contracts

- **contract-drafter** — Drafts new Chinese-language contracts of any type from a structured brief. Use when the user says 'draft a contract', '起草一份合同', or supplies a term sheet that needs to become a contract.
- **contract-reviewer-cn** — Reviews a Chinese-language contract for risk, missing clauses, and compliance gaps. Use when the user shares a contract and says '审一下', 'review this', or asks for a redline.
- **contract-reviewer-en** — Reviews an English-language contract under common-law style: risk, missing clauses, market norms, governing law / forum trade-offs. Use for cross-border contracts in English.
- **redline-generator** — Produces a tracked-changes redline from an original .docx plus a list of intended changes. Use when the operator says 'produce a redline', '出红线版', or after a contract review.
- **negotiation-tactics** — Negotiation tactics specialist: proposes counter-proposals, fallback positions, BATNA analysis. Use when the user says 'how do I push back on this', '怎么谈', or asks for negotiation strategy.
- **sale-of-goods-contract** — Sale-of-goods contract specialist: 货物买卖, distribution into China, Incoterms, title and risk transfer, CISG vs PRC Civil Code. Use for any goods-sale contract.
- **services-contract** — Services contract specialist: MSA + SOW, deliverables, acceptance, IP ownership of work product, SLAs, service credits. Use for any services / consulting contract.
- **licensing-contract** — Licensing contract specialist: technology, trademark, copyright, software, content licensing; royalties, sub-licensing, exclusivity, audit rights. Use for any IP licence-in or licence-out.
- **distribution-agency** — Distribution / agency / franchise specialist: exclusive vs non-exclusive, minimum purchase, territory, post-termination obligations, franchise filing in China. Use for any distribution / agency / franchise contract.
- **loan-finance-contract** — Loan and finance contract specialist: bilateral and syndicated loans, security, guarantees, intercompany loans, cross-border loan registration with SAFE. Use for any loan-side matter.
- **construction-contract** — Construction / EPC / FIDIC contract specialist: civil works, EPC, FIDIC books, variations, claims, delay analysis. Use for any construction / EPC matter.
- **real-estate-contract** — Real estate contract specialist: sale, lease, mortgage of land-use rights and buildings under PRC law. Use for any RE transactional matter.
- **nda-confidentiality** — NDA / confidentiality specialist: mutual and one-way NDAs, residuals, term, carve-outs, IP ownership, return / destruction. Use for any standalone NDA.
- **settlement-agreement** — Settlement agreement specialist: court-supervised settlement, arbitration settlement, private settlement, release scope, payment terms. Use whenever a dispute moves toward resolution.
- **term-sheet-drafter** — Term sheet specialist: produces concise term sheets that capture deal economics and governance in one page. Use early in any deal cycle.
- **letter-of-intent** — LOI / MOU specialist: drafts and reviews letters of intent and memoranda of understanding with appropriate binding-clause demarcation. Use whenever parties want to memorialise a preliminary deal.
- **supply-procurement** — Supply and procurement specialist: master purchase, blanket orders, vendor managed inventory, tooling, supplier code of conduct. Use for buyer-side procurement contracts.
- **saas-cloud-contract** — SaaS and cloud contract specialist: subscription, data location, uptime SLAs, security obligations, exit assistance. Use for any SaaS / cloud / PaaS / IaaS contract.

## compliance

- **compliance-program** — Compliance program designer: builds and audits internal compliance programs covering ABAC, antitrust, export control, sanctions, data protection. Use to design or refresh a corporate compliance program.
- **internal-investigations** — Internal investigations specialist: privileged investigations under PRC and cross-border privilege regimes; whistleblower triage; preservation; interviews; reporting. Use for any whistleblower or audit-trigger investigation.
- **policy-procedure-drafter** — Drafts internal policies and SOPs (gifts and hospitality, conflict of interest, data handling, social media, IT acceptable use). Use whenever a new policy or SOP is needed.
- **training-content** — Compliance training content specialist: deck + script + quiz for in-person or e-learning compliance training. Use whenever annual or trigger-based training is needed.
- **regulator-engagement** — Regulator engagement specialist: prepares responses to regulator information requests, dawn raids, inspections, examinations. Use whenever a regulator opens an inquiry.
- **kyc-aml** — KYC / AML specialist: customer due diligence, beneficial ownership, sanctions screening, suspicious activity reports. Use for any onboarding or transaction-monitoring matter.
- **advertising-marketing-cn** — Advertising and marketing compliance specialist (PRC): 《广告法》, claims substantiation, sponsorship, influencer marketing. Use for any PRC advertising matter.
- **ai-governance** — AI governance specialist: PRC Generative AI Measures, algorithmic recommendation regulation, model registration, training-data compliance, AI-incident response. Use for any AI-product compliance matter under PRC law.
- **healthcare-pharma-cn** — Healthcare / pharma regulatory specialist (PRC): NMPA drug / device registration, clinical trial regulation, medical advertising, hospital procurement, traditional Chinese medicine. Use for any healthcare regulatory matter.
- **automotive-regulatory-cn** — Automotive regulatory specialist (PRC): vehicle type approval, recall, autonomous-driving regulation, NEV subsidies, automotive data security. Use for any automotive regulatory matter.
- **telecom-regulatory-cn** — Telecom and internet content regulatory specialist (PRC): ICP licence, value-added telecom licence, network operator obligations, content moderation. Use for any telecom or internet platform matter.

## ip

- **trademark-cn** — PRC trademark specialist: search, filing, opposition, invalidation, well-known mark, OEM defence, customs recordal. Use for any PRC trademark matter.
- **trademark-international** — International trademark specialist: Madrid system, US, EU, UK, Japan, Korea, SEA filings; oppositions; portfolios. Use for any non-PRC or multi-jurisdiction trademark matter.
- **patent-cn** — PRC patent specialist: invention, utility model, design; prosecution; oppositions / invalidations before the CNIPA reexamination board; SEPs and FRAND. Use for any PRC patent matter.
- **patent-international** — International patent specialist: PCT, US, EPO, JP, KR; family management; FTO; SEP licensing. Use for any non-PRC or multi-jurisdiction patent matter.
- **copyright-cn** — PRC copyright specialist: software registration, computer program protection, derivative works, fair use, online infringement. Use for any PRC copyright matter.
- **trade-secret-cn** — Trade secret specialist: trade-secret programs, NDAs, employee invention assignments, departure protocols, AUCL / criminal trade-secret cases. Use for trade-secret protection or enforcement.
- **domain-name-disputes** — Domain-name dispute specialist: UDRP, PRC CNDRP, ccTLD disputes. Use for any cybersquatting or domain dispute.
- **ip-licensing** — IP licensing specialist (cross-cutting): structures IP licences with tax-and-regulatory awareness; coordinates with licensing-contract. Use for cross-jurisdiction IP licence design.
- **ip-portfolio-mgmt** — IP portfolio management specialist: docketing, annuities, lapse-prevention, portfolio audits. Use to manage a multi-asset IP portfolio.
- **ip-litigation-cn** — PRC IP litigation specialist: civil and criminal IP litigation, IP courts, evidence preservation, injunctions, damages. Use for any IP enforcement matter in PRC courts.

## disputes

- **disputes-civil-cn** — PRC civil litigation specialist: contract, tort, property, family civil disputes; first-instance, appeal, retrial; preservation; enforcement. Use for any PRC civil litigation matter.
- **disputes-administrative-cn** — PRC administrative litigation specialist: administrative reconsideration, administrative litigation, challenges to SAMR / tax / customs decisions. Use to challenge a government decision.
- **disputes-criminal-cn** — PRC criminal defence specialist (white-collar): commercial bribery, embezzlement, occupational crime, tax crimes, securities crimes, criminal trade secret. Use for any PRC white-collar criminal matter.
- **disputes-arbitration-cn** — PRC and PRC-seated international arbitration specialist: CIETAC, BAC, SHIAC; ad-hoc; enforcement of awards. Use for any PRC-seated or PRC-related arbitration.
- **disputes-arbitration-international** — International arbitration specialist: HKIAC, SIAC, ICC, LCIA, ICSID; investor-state; enforcement under New York Convention. Use for any international arbitration matter.
- **disputes-enforcement** — Enforcement specialist: court enforcement, asset tracing, voluntary execution, cross-border enforcement (New York Convention; Hague). Use for any post-award / post-judgment enforcement.
- **evidence-preservation** — Evidence preservation specialist: notarisation, blockchain evidence, pre-litigation preservation, e-discovery in PRC. Use whenever evidence needs to be captured before trial / arbitration.
- **white-collar-investigations** — Cross-border white-collar specialist: parallel proceedings (DOJ / SEC / SFC / PRC), self-disclosure trade-offs, monitor relationships. Use for any cross-border white-collar matter.
- **class-action-defence** — Class / representative action defence specialist: securities class actions, consumer class actions, antitrust private enforcement. Use for any class / representative action.
- **mediation-specialist** — Mediation specialist: structures and drafts mediation papers; helps the operator prepare for a mediation session. Use whenever a mediation is on the calendar.

## tax

- **tax-corporate-cn** — PRC corporate income tax specialist: CIT residency, treaty relief, related-party transactions, transfer pricing, tax-effective restructuring, GAAR. Use for any PRC CIT matter.
- **tax-vat-cn** — PRC VAT specialist: input / output VAT, fapiao management, refund / exemption / export VAT, simplified taxation. Use for any PRC VAT matter.
- **tax-transfer-pricing** — Transfer pricing specialist: TP documentation (master file, local file, CbCR), APA, BEPS Pillar Two, intercompany pricing design. Use for any TP matter.
- **tax-cross-border** — Cross-border tax specialist: treaty relief, withholding tax, holding-structure design, double-tax-treaty coordination, BEPS implementation. Use for any cross-border tax matter.
- **tax-customs** — Customs and trade tax specialist: HS classification, valuation, origin, customs duties, AEO, customs audits. Use for any customs matter.
- **tax-dispute-cn** — PRC tax dispute specialist: tax audit defence, administrative reconsideration on tax, tax-criminal exposure. Use for any PRC tax dispute.
- **tax-individual-uhnw** — UHNW individual tax specialist: tax-residency planning, exit tax, trust structures, family-office tax, PRC capital export. Use for any high-net-worth individual tax matter.

## labor

- **labor-employment-cn** — PRC labour and employment specialist: hire, transfer, performance management, termination, severance, non-compete, labour arbitration. Use for any PRC employment matter.
- **labor-mass-termination** — Mass termination / RIF specialist: economic-redundancy procedures, mass-layoff filings, union consultation, sequencing. Use whenever 20+ employees are being separated.
- **labor-non-compete** — Non-compete and confidentiality enforcement specialist: enforceable scope, compensation, breach remedies. Use to design or enforce a non-compete.
- **labor-equity-incentive** — Equity incentive / ESOP specialist: design and document option / RSU / stock plans for PRC employees, with tax and PRC-FX considerations. Use for any employee equity plan.
- **labor-investigations** — Workplace investigations specialist: harassment, discrimination, fraud allegations; privileged investigations; remediation. Use for any internal HR investigation.
- **labor-international** — International employment specialist: cross-border secondments, expatriate packages, posted-worker rules, social-security coordination. Use for any cross-border employment matter.

## real-estate

- **real-estate-cn** — PRC real estate specialist: title, transfer, mortgage, leases, urban-renewal projects, land-use rights. Use for any PRC real-estate matter.
- **real-estate-development** — Real estate development specialist: land acquisition, planning, construction, sales pre-licence, completion and delivery. Use for any RE development matter.
- **real-estate-finance** — Real estate finance specialist: project financing, REITs (PRC infrastructure REIT), mezzanine, security packages. Use for any RE finance matter.
- **real-estate-lease** — Real estate lease specialist: commercial lease, retail, office, industrial; subleases; lease assignments. Use for any RE leasing matter.
- **real-estate-disputes** — Real estate dispute specialist: title, boundary, possession, lease enforcement, mortgage enforcement. Use for any RE litigation matter.

## doc-ops

- **doc-ops-formatter** — Final-format any client-facing deliverable per docs/DOCUMENT_STYLE_GUIDE.md. Use as the last step before releasing a .docx or .pdf.
- **doc-ops-text-extraction** — Extract text (with structure where possible) from .docx, .pdf, scanned-pdf, .doc, .rtf. Use whenever a downstream agent needs the text of a file.
- **doc-ops-redline** — Generate Word tracked-changes redlines between an original and a revised version, or apply a list of edits to an original. Use whenever a redline is needed.
- **doc-ops-summariser** — Summarise a long document into a 1-page executive brief and a 3-page detailed brief, preserving citations. Use whenever a deliverable needs a front-matter summary.
- **doc-ops-translator** — Translate legal documents between Chinese and English with terminology consistency and citation preservation. Use whenever a bilingual deliverable is needed.
- **doc-ops-citation-checker** — Verify all statute and case citations against statutes-rag and wenshu. Flag any inventions. Use as a QA step before any deliverable that contains citations.
- **doc-ops-bundle** — Compile a bundle (hearing bundle, evidence bundle, deal closing bundle, board pack) with index, pagination, and bookmarks. Use whenever a multi-file bundle is needed.

## research

- **research-statute-cn** — PRC statutory research specialist: locates and summarises applicable statutes, regulations, judicial interpretations, local rules. Use whenever a specialist needs statute citations.
- **research-case-cn** — PRC case research specialist: locates and summarises Chinese court judgments via wenshu. Use whenever a specialist needs precedent.
- **research-regulator-cn** — PRC regulator research specialist: locates regulator decisions, guidance, FAQs from SAMR, CSRC, MOFCOM, NDRC, CAC, NMPA. Use whenever a specialist needs regulator practice.
- **research-international** — International legal research specialist: Westlaw / LexisNexis for US, UK, EU, HK, SG common-law and EU regimes. Use whenever a cross-border specialist needs foreign law research.
- **research-company-info** — Company / counter-party background specialist: tianyancha, qichacha, samr. Pulls registration, litigation, sanctions, share-pledge, IP info on a counter-party. Use whenever a specialist needs counter-party context.

## drafting

- **drafter-memo** — Drafts legal memoranda from a structured outline. Use whenever a specialist's output needs to be turned into a polished memo.
- **drafter-opinion** — Drafts formal legal opinions (e.g. for transactions, regulatory filings). Use whenever a deliverable carries opinion-letter weight.
- **drafter-pleading** — Drafts court pleadings (complaint, answer, appellate brief, retrial petition). Use whenever a litigation specialist needs court paper.
- **drafter-correspondence** — Drafts formal correspondence (demand letter, response letter, instruction letter, regulator letter). Use whenever a formal letter is the deliverable.
- **drafter-deal-doc** — Drafts transactional documents (SPA / APA / SHA / JV / loan / licence / lease). Use whenever a transactional specialist has produced a brief that needs paper.

## onboarding

- **onboarding-host** — First-time setup host. Walks the user through the five-question wizard and runs scripts/onboard.py with the chosen preferences. Use only via the /onboard slash command.



## Singapore (10)

- `sg-corporate-counsel` — Companies Act 1967, ACRA filings, board resolutions, directors' duties.
- `sg-employment-specialist` — Employment Act, MOM, employment passes, retrenchment.
- `sg-pdpa-specialist` — PDPA 2012, breach notification, consent, DPO.
- `sg-tax-counsel` — Income Tax Act, GST Act, IRAS rulings, transfer pricing.
- `sg-family-specialist` — Women's Charter, divorce, maintenance, custody, MA division.
- `sg-ip-specialist` — Trade Marks Act, Patents Act, Copyright Act 2021, IPOS filings.
- `sg-securities-counsel` — SFA, MAS guidelines, SGX listing.
- `sg-cross-border-specialist` — SG-side DTAA application, FDI, BO disclosure.
- `sg-disputes-specialist` — ROC 2021, SICC, SIAC, enforcement.
- `sg-estate-trust-specialist` — Probate, MCA, Trustees Act, wills, LPAs.

## United States (13)

- `us-corporate-counsel-delaware` — DGCL, DE Chancery, board / stockholder actions.
- `us-securities-counsel` — Securities Act 1933, Exchange Act 1934, SOX, Dodd-Frank, Reg FD.
- `us-ma-counsel` — DGCL ss. 251 / 253 / 271, HSR, exclusivity, lockups.
- `us-employment-counsel` — FLSA, FMLA, ADA, Title VII, NLRA, state wage/hour.
- `us-ip-trademark-counsel` — Lanham Act, USPTO TSDR, TTAB.
- `us-ip-patent-counsel` — 35 USC, USPTO, PTAB, claim drafting.
- `us-tax-federal-counsel` — IRC, Treasury Regs, IRS rulings.
- `us-tax-salt-counsel` — Nexus, apportionment, sales/use, state income tax.
- `us-antitrust-counsel` — Sherman, Clayton, HSR, FTC Act, agency guidelines.
- `us-privacy-counsel` — CCPA / CPRA + state patchwork (VA, CO, CT, UT, TX), HIPAA, GLBA.
- `us-bankruptcy-counsel` — Title 11 (Chapters 7, 11, 13, 15).
- `us-real-estate-counsel` — State-by-state, title, escrow, lease, mortgage.
- `us-family-estate-counsel` — State family law, UPC, wills, trusts, estate / gift tax.

## Cross-border (4)

- `cn-sg-cross-border` — CN-SG inbound / outbound corporate, tax, employment.
- `cn-us-cross-border` — CN-US capital markets, VIE, CFIUS, M&A.
- `sg-us-cross-border` — SG-US structuring, holding companies, M&A.
- `tri-jurisdiction-coordinator` — Genuine three-way matters only.

## Orchestrator additions

- `jurisdiction-detector` — Helper for `task-router`, classifies jurisdiction.
