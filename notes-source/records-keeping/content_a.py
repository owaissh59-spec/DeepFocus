# -*- coding: utf-8 -*-
"""Part I — Foundations: Chapter 1 & Chapter 2"""


def chapter1(b):
    b.part('PART I', 'Foundations of Stores & Records Keeping')
    b.chapter(1, 'Drug Store Management & Records Keeping — Foundation',
              'Terminology \u2022 objectives \u2022 principles of record keeping \u2022 types of stores '
              '\u2022 organisation \u2022 layout \u2022 legal framework')

    b.lead('Every single record discussed in this book exists for only three reasons — to prove '
           'that a drug was received, to prove where it went, and to prove that it was safe and '
           'legal at every moment in between. Keep these three "proofs" in mind and the whole '
           'chapter of Stores Records becomes logical instead of a list to be memorised.')

    # ------------------------------------------------------------------ 1.1
    b.h2('1.1', 'Store, Stores and Drug Store — Basic Terminology')
    b.box('def', 'STORE',
          'A **store** is a *specified, secure place* where materials (drugs, surgicals, '
          'chemicals, equipment, stationery) are **received, kept safely and issued** as and '
          'when required. The word **"stores"** (plural) is used for the *department/section* '
          'that performs this function, while **"stock"** means the *material actually lying* '
          'in that store.')
    b.kv([
        ('Drug store', 'A store that specifically receives, stores and issues drugs, medicines, '
                       'surgical dressings and allied pharmaceutical items.'),
        ('Store keeping', 'The physical activity of receipt, custody, preservation, '
                          'record-keeping and issue of materials.'),
        ('Stores management', 'The managerial function of planning, organising, staffing, '
                              'directing and controlling all store activities economically.'),
        ('Materials management', 'The **umbrella function** covering purchasing, stores, '
                                 'inventory control, transportation, material handling and '
                                 'disposal of surplus. Stores + Records keeping is one arm of it.'),
        ('Records keeping (record maintenance)',
         'Systematic **writing, posting, preserving and retrieving** of all documents that '
         'evidence the movement (in-flow, holding and out-flow) of every item of stock.'),
        ('Custodian', 'The officer personally responsible and accountable for the stock — '
                      'normally the **Store Officer / Pharmacist-in-charge of stores**.'),
    ])

    b.h3('1.1.1  Difference between Store Keeping and Stores Management')
    b.table(['Point', 'Store Keeping', 'Stores Management'],
            [['Nature', 'Operative / physical activity', 'Managerial / decision-making activity'],
             ['Scope', 'Narrow — receipt, custody, issue, records',
              'Wide — includes store keeping + planning, layout, inventory control, budgeting, staff'],
             ['Performed by', 'Store keeper, store clerk, packer',
              'Store officer / Chief Pharmacist / Materials Manager'],
             ['Aim', 'Safe custody and correct records',
              'Right material, right quantity, right time, right cost'],
             ['Output', 'Registers, bin cards, vouchers', 'Policy, SOPs, budget, performance reports']])

    # ------------------------------------------------------------------ 1.2
    b.h2('1.2', 'Records Keeping — Meaning, Purpose and Scope')
    b.p('A **record** is any written, printed or electronic document that furnishes *permanent, '
        'retrievable evidence* of a transaction or an event. In a drug store, a transaction is '
        'either a **receipt**, a **transfer**, an **issue**, a **return**, a **loss** or a '
        '**disposal** — and *each one must leave a paper (or electronic) trail*.')

    b.h3('1.2.1  Purposes of Records Keeping')
    b.numbered([
        '**Legal / statutory compliance** — the Drugs and Cosmetics Act, 1940 & Rules, 1945, '
        'the NDPS Act, 1985 and the Pharmacy Act, 1948 make certain records *compulsory*; absence '
        'of a record is itself an offence.',
        '**Accountability and custody** — fixes personal responsibility for every unit of stock '
        'on a named custodian.',
        '**Financial control** — shows the value of stock held, consumed and wasted; feeds the '
        'annual accounts, budget and audit.',
        '**Inventory control** — consumption data from records is the raw material for ABC/VED '
        'analysis, EOQ, re-order level and indenting.',
        '**Traceability / recall** — batch-wise records allow instant location of every unit of a '
        'batch declared *Not of Standard Quality (NSQ)* or recalled.',
        '**Prevention of pilferage, theft and misuse** — especially of narcotics, psychotropics '
        'and Schedule X drugs.',
        '**Avoidance of expiry and over-stocking** — expiry registers and near-expiry reports.',
        '**Information for management (MIS)** — consumption trends, supplier performance, '
        'lead-time analysis, price trends.',
        '**Evidence in disputes** — with suppliers, carriers, insurers, and in courts of law.',
        '**Continuity** — the store does not stop working when a store keeper is transferred; the '
        'records carry the memory of the organisation.',
    ])

    b.box('hy', 'HIGH-YIELD',
          'The single-line examination answer: *"Records keeping is the systematic maintenance of '
          'documents relating to receipt, storage, issue and disposal of stores, to ensure '
          '**accountability, legal compliance, financial control and traceability**."* Remember the '
          'four italicised words — they are the usual four options of an MCQ.')

    b.h3('1.2.2  Scope — What all is "Records Keeping" in a Drug Store?')
    b.table(['Stage of material flow', 'Typical records generated'],
            [['Demand / need identification', 'Indent, requisition slip, consumption statement, '
              'stock position statement'],
             ['Procurement', 'Purchase requisition, tender/quotation file, comparative statement, '
              'purchase order, rate-contract register'],
             ['Receipt (goods inward)', 'Gate entry register, delivery challan, invoice, packing '
              'list, Goods Inward Register, Goods Received Note (GRN), inspection/test report, '
              'discrepancy & damage report'],
             ['Storage', 'Bin card, stock ledger / stock register, batch & expiry register, '
              'temperature–humidity log, location (bin) index, narcotic register'],
             ['Issue / distribution', 'Issue voucher, issue register, daily consumption register, '
              'sub-store & ward ledger, gate pass'],
             ['Return / rejection', 'Material Return Note (MRN), rejection memo, debit note, '
              'credit note, supplier-return register'],
             ['Loss / deterioration', 'Breakage & loss register, expiry register, discrepancy '
              'report, write-off sanction'],
             ['Disposal', 'Condemnation register, board proceedings, auction/destruction '
              'certificate, bio-medical waste record'],
             ['Verification & audit', 'Stock verification sheet, shortage/excess statement, '
              'verification certificate, audit para file']],
            caption='Table 1.1  Records generated at each stage of the material cycle')

    # ------------------------------------------------------------------ 1.3
    b.h2('1.3', 'Objectives and Functions of a Drug Store')
    b.h3('1.3.1  Objectives')
    b.bullets([
        'To make available the **right drug, of right quality, in right quantity, at the right '
        'time, at right cost** to the user departments (the *5 R\u2019s*).',
        'To **protect** the stock from deterioration, damage, pilferage, fire, moisture, heat, '
        'light, rodents and insects.',
        'To maintain **minimum investment** in inventory consistent with uninterrupted supply '
        '(*no stock-out, no over-stock*).',
        'To keep **accurate, up-to-date records** of receipt, balance and issue of every item.',
        'To provide information for **purchase planning and budgeting**.',
        'To ensure **statutory compliance** in storage and documentation.',
        'To achieve **economy** in space, manpower and handling cost.',
    ])
    b.h3('1.3.2  Functions (the classic "receipt-to-disposal" list)')
    b.numbered([
        '**Receiving** the materials and checking them against purchase order.',
        '**Inspection** (quantitative + qualitative) and arranging quality testing where required.',
        '**Storage / preservation** in an orderly, coded, retrievable and condition-appropriate manner.',
        '**Record keeping** — bin cards, ledgers, registers, batch and expiry data.',
        '**Issue** of materials against authorised indents, on FIFO/FEFO basis.',
        '**Stock control** — maintaining levels, initiating indents at re-order level.',
        '**Stock verification** — perpetual and periodic physical counting.',
        '**Housekeeping and safety** — cleanliness, pest control, fire safety, security.',
        '**Disposal** of expired, damaged, obsolete, surplus and condemned items.',
        '**Information & liaison** — with purchase, accounts, user departments and audit.',
    ], )
    b.box('mnem', 'MNEMONIC — functions of stores',
          '**"R-I-S-R-I-S-V-H-D-I"** \u2192 **R**eceive, **I**nspect, **S**tore, **R**ecord, '
          '**I**ssue, **S**tock-control, **V**erify, **H**ousekeep, **D**ispose, **I**nform.')

    # ------------------------------------------------------------------ 1.4
    b.h2('1.4', 'Importance / Advantages of Systematic Records Keeping')
    b.table(['Beneficiary', 'How good records help'],
            [['Patient', 'Correct, unexpired, potent drug; quick recall of a defective batch'],
             ['Pharmacist / store keeper', 'Protection from blame; proof of due diligence; easy '
              'hand-over on transfer'],
             ['Hospital / firm', 'Control on expenditure; reduced wastage; better negotiation with '
              'suppliers using purchase history'],
             ['Purchase department', 'Reliable consumption and lead-time data for indenting'],
             ['Accounts / audit', 'Verifiable link between money spent and material received'],
             ['Drug regulatory authority', 'Evidence of legal storage, sale and distribution'],
             ['Management', 'MIS reports — turnover ratio, stock-out rate, expiry loss %, '
              'supplier performance']])
    b.box('caution', 'CONSEQUENCES OF POOR RECORD KEEPING',
          bullets=['Stock-outs of life-saving drugs and simultaneous over-stocking of slow movers.',
                   'Heavy **expiry loss** and wastage of public money.',
                   'Undetected **pilferage**, particularly of narcotics — invites criminal action '
                   'under the NDPS Act, 1985.',
                   'Failure of **recall** of a Not-of-Standard-Quality batch \u2192 patient harm.',
                   '**Audit objections**, disallowance of bills, recovery from the custodian\u2019s salary.',
                   '**Suspension or cancellation of the drug licence** for contravention of '
                   'Rule 65 conditions of the Drugs and Cosmetics Rules, 1945.'])

    # ------------------------------------------------------------------ 1.5
    b.h2('1.5', 'Principles (Golden Rules) of Records Keeping')
    b.numbered([
        '**Contemporaneous entry** — record the transaction *at the time it happens*, never from memory later.',
        '**Accuracy & completeness** — every column of the format must be filled; "nil" is written, not left blank.',
        '**Legibility & permanence** — written in **ink** (blue/black ball pen), never in pencil; '
        'no loose sheets — bound registers with printed serial page numbers.',
        '**No erasure / no overwriting / no whitener** — a wrong entry is **scored out with a '
        'single line**, the correct entry written above/beside, and the correction **initialled '
        'and dated** by the authorised person.',
        '**Chronological order** — entries strictly date-wise; each page totalled and carried forward.',
        '**Authentication** — every entry and every voucher signed (with name, designation, date) '
        'by the person making it and countersigned by the controlling officer.',
        '**Cross-referencing** — every entry quotes its source document number (GRN No., Invoice '
        'No., Indent No., Issue Voucher No.) so that any figure can be traced back.',
        '**Double entry / two-point recording** — the same transaction is posted in *two* records '
        '(bin card **and** stock ledger) which are periodically tallied.',
        '**Confidentiality and security** — records kept under lock; access restricted; narcotic '
        'registers under the personal custody of a named officer.',
        '**Retention** — preserved for the statutory period (see Chapter 11) and destroyed only '
        'after proper sanction, with a destruction certificate.',
        '**Uniformity & standardisation** — same format, same code numbers, same units of issue '
        'throughout the organisation.',
        '**Simplicity & economy** — the minimum number of records that satisfy law and control; '
        'avoid duplicate registers.',
        '**Auditability** — records must satisfy an outsider (auditor, drug inspector) without '
        'oral explanation. *"If it is not written, it was not done."*',
    ])
    b.box('exam', 'FREQUENTLY ASKED',
          'A wrong entry in a stock register is corrected by **scoring out with a single line and '
          'attesting with signature and date** — *never* by erasing, overwriting, or using '
          'correcting fluid. Registers must be **bound with machine-numbered pages**, and a '
          '**certificate of number of pages** is recorded on the first page by the officer-in-charge.')

    # ------------------------------------------------------------------ 1.6
    b.h2('1.6', 'Types and Classification of Store Records')
    b.h3('1.6.1  On the basis of legal compulsion')
    b.table(['Category', 'Meaning', 'Examples'],
            [['Statutory (mandatory) records',
              'Prescribed by law; must be produced on demand to an inspector',
              'Schedule H / H1 / X sale registers, prescription records, narcotic (NDPS) register, '
              'purchase & sale bills, batch-wise records, blood bank records, bio-medical waste records'],
             ['Non-statutory (managerial) records',
              'Maintained for internal control and efficiency',
              'Bin card, stock ledger, indent register, GRN, issue voucher, temperature log, '
              'supplier performance register']])
    b.h3('1.6.2  On the basis of function')
    b.bullets([
        '**Receipt records** — Goods Inward Register, GRN, inspection report, day book of receipts.',
        '**Custody / holding records** — bin card, stock ledger, batch-expiry register, bin index.',
        '**Issue records** — indent, issue voucher, issue register, consumption register, gate pass.',
        '**Financial records** — invoice file, bill register, payment voucher, priced stores ledger.',
        '**Control records** — re-order level statement, ABC/VED list, stock verification sheet.',
        '**Statutory records** — as listed above.',
        '**Miscellaneous records** — correspondence file, guard file of orders/circulars, '
        'complaint and drug-alert file.',
    ])
    b.h3('1.6.3  Other useful classifications')
    b.table(['Basis', 'Types'],
            [['Form', 'Manual (registers, cards, vouchers) \u2022 Mechanised/Computerised '
              '(software, barcode, e-registers)'],
             ['Period', 'Permanent (dead-stock register, licence file) \u2022 Temporary/periodic '
              '(daily receipt register, monthly consumption)'],
             ['Origin', 'Internal (indent, GRN, issue voucher) \u2022 External (invoice, challan, '
              'test report, credit note)'],
             ['Level of detail', 'Primary/original (voucher, challan) \u2022 Secondary/derived '
              '(ledger, register, statement)']])

    # ------------------------------------------------------------------ 1.7
    b.h2('1.7', 'Types of Stores in a Hospital / Pharmaceutical Set-up')
    b.table(['Type of store', 'Purpose / features'],
            [['Central (Main) store', 'Single large store receiving all supplies and feeding all '
              'sub-stores; keeps master records (stock ledger); usually located near the '
              'receiving dock with easy vehicular access'],
             ['Sub-store / departmental store', 'Small store in a ward, OT, ICU, casualty, '
              'dispensary; receives from main store on indent; works on **imprest / top-up** system'],
             ['Dispensary / pharmacy counter stock', 'Working stock for daily dispensing to patients'],
             ['Bonded store', 'For goods on which duty/excise is not yet paid (e.g. **rectified '
              'spirit, alcohol**) — kept under excise bond and double lock'],
             ['Narcotic store (DDA cupboard)', 'Separate locked steel cupboard/safe embedded in '
              'wall, double lock, key with a named officer; NDPS register maintained'],
             ['Cold store / cold chain room', 'Walk-in cooler, ILR, deep freezer for vaccines, '
              'sera, insulin, blood products'],
             ['Inflammable / hazardous store', 'Detached building for ether, spirit, LPG, '
              'cylinders; flame-proof fittings'],
             ['Quarantine store', '"Under test" area for material awaiting inspection/QC clearance'],
             ['Transit / receiving store', 'Temporary holding of consignments in the goods inward section'],
             ['Salvage / condemned store', 'Holds expired, damaged, obsolete and condemned items '
              'pending disposal — must be **physically separate and labelled**'],
             ['Equipment / dead-stock store', 'Non-consumable capital items on permanent register'],
             ['General / miscellaneous store', 'Stationery, linen, sanitary, POL, engineering spares']])
    b.box('hy', 'HIGH-YIELD',
          'Expired, damaged and recalled drugs must be kept in a **separate, clearly marked and '
          'preferably locked area** (quarantine/salvage) to prevent accidental issue — this is a '
          'favourite one-liner MCQ.')

    # ------------------------------------------------------------------ 1.8
    b.h2('1.8', 'Organisation and Staffing of the Stores Department')
    b.flow(['Medical Superintendent / MD', 'Materials Manager / Store Officer',
            'Pharmacist (Stores)', 'Store Keeper', 'Store Clerk', 'Packer / Helper'])
    b.table(['Post', 'Principal duties relating to records'],
            [['Store Officer / Materials Manager', 'Overall custody & accountability; sanctions '
              'indents; countersigns GRN and issue vouchers; orders stock verification; replies '
              'to audit'],
             ['Pharmacist (Stores) / Chief Pharmacist', 'Technical scrutiny of receipts (batch, '
              'expiry, storage condition); maintains narcotic, Schedule X and expiry registers; '
              'prepares indents'],
             ['Store Keeper', 'Physical receipt, storage, issue; maintains **bin cards** and '
              'stock registers; bin location; FIFO/FEFO'],
             ['Store Clerk / Ledger Clerk', 'Posting of **stock ledger**, preparation of GRN, '
              'issue vouchers, statements, filing'],
             ['Receipt (Goods Inward) Clerk', 'Gate entry, checking of challan/invoice, unpacking, '
              'counting, drafting GRN and discrepancy reports'],
             ['Packer / Helper / Loader', 'Material handling, stacking, packing for despatch'],
             ['Stock Verifier (independent)', 'Physical verification; must **not** be the custodian '
              '\u2014 principle of *separation of duties*']])
    b.box('exam', 'PRINCIPLE OF SEPARATION OF DUTIES',
          'The person who **orders** (purchase), the person who **receives/keeps** (stores) and the '
          'person who **pays** (accounts) must be *different*; and the **stock verifier must be '
          'independent of the custodian**. This is the basic internal-check principle behind all '
          'store documentation.')

    # ------------------------------------------------------------------ 1.9
    b.h2('1.9', 'Planning and Layout of the Main Drug Store')
    b.h3('1.9.1  Sections (zones) of a well-planned store')
    b.numbered([
        '**Goods inward / receiving bay** — unloading platform, weighing scale, unpacking table.',
        '**Quarantine ("under test") area** — clearly demarcated, yellow-labelled.',
        '**Approved / main storage area** — racks, bins, pallets, code-wise arrangement.',
        '**Cold storage area** — refrigerators, ILR, deep freezer, walk-in cooler + temperature charts.',
        '**Narcotic & Schedule X vault** — double-locked cupboard.',
        '**Inflammable / hazardous bay** — separate, ventilated, fire-fighting equipment.',
        '**Rejected / expired / salvage area** — red-labelled, locked.',
        '**Issue / despatch counter** — with issue window, trolleys, packing table.',
        '**Records / office room** — ledgers, registers, filing cabinets, computer.',
        '**Bulk & heavy item area** — IV fluids, oxygen cylinders, near the entrance at ground level.',
    ])
    b.h3('1.9.2  Points to remember in layout & storage practice')
    b.table(['Parameter', 'Norm / good practice'],
            [['Location', 'Ground floor, near the receiving gate, with easy access to lift/ramp '
              'and to the dispensary; away from wards for noise/traffic reasons'],
             ['Flow of material', '**One-way (straight-line) flow**: receive \u2192 inspect \u2192 store '
              '\u2192 issue; no back-tracking, no crossing of clean and rejected stock'],
             ['Aisle / gangway', 'Wide enough for trolleys (about 1\u20131.5 m); main gangway wider'],
             ['Distance from wall', 'Stacks/pallets kept **at least 30 cm (1 ft) away from walls** '
              'to allow air circulation, cleaning, inspection and pest control'],
             ['Height from floor', 'Nothing stored directly on the floor; use **pallets/duck-boards '
              '(\u2248 10 cm high)** to protect from damp and flooding'],
             ['Distance from ceiling / lights', 'Adequate gap below ceiling and light fittings; '
              'sprinkler clearance maintained'],
             ['Racks & shelves', 'Metal/steel, adjustable, labelled with item name + code + bin no.'],
             ['Lighting', 'Adequate, diffused; **direct sunlight avoided**; windows painted/'
              'shaded; UV-filtered where needed'],
             ['Ventilation & temperature', 'Cross-ventilation, exhaust fans, air-conditioning; '
              'store temperature normally kept **below 25 \u00B0C** with **RH < 60 %**'],
             ['Floor', 'Smooth, non-absorbent, crack-free, easily washable; no crevices for pests'],
             ['Security', 'Grilled windows, single controlled entry, locks, CCTV, fire alarm, '
              'restricted entry'],
             ['Fire safety', 'CO\u2082 / dry-powder extinguishers, sand buckets, hydrants, '
              '"NO SMOKING" boards, marked exits'],
             ['Pest control', 'Rodent-proof, insect screens, periodic fumigation record'],
             ['Space norm', 'Provide for present + future stock; commonly ~60\u201365 % of area for '
              'storage and the rest for aisles, receiving and office']])
    b.box('mnem', 'MNEMONIC — layout of a store',
          '**"R-Q-S-C-N-H-R-I-O-B"** \u2192 **R**eceiving, **Q**uarantine, **S**torage, **C**old, '
          '**N**arcotic, **H**azardous, **R**ejected, **I**ssue, **O**ffice, **B**ulk.')

    # ------------------------------------------------------------------ 1.10
    b.h2('1.10', 'Legal & Regulatory Framework Governing Store Records')
    b.table(['Law / rule', 'What it demands of a drug store'],
            [['**Drugs and Cosmetics Act, 1940** and **Rules, 1945**',
              'Licence to stock & sell (Form 20/20B/21/21B; Form 20F/20G for Schedule X); '
              'qualified person; storage conditions; records of purchase and sale; prescription '
              'and Schedule H/H1/X registers; labelling; no sale of expired drugs'],
             ['**Pharmacy Act, 1948**', 'Drugs to be compounded/dispensed only by a **registered '
              'pharmacist**; register of pharmacists; renewal records'],
             ['**NDPS Act, 1985** & Rules', 'Licence/permit for narcotics & psychotropics; '
              'separate register; safe custody under lock; consumption and balance accounted; '
              'destruction only with official sanction'],
             ['**Drugs (Prices Control) Order (DPCO)** / NPPA',
              'Ceiling price of scheduled formulations; price list display; records of price '
              'compliance'],
             ['**Bio-Medical Waste Management Rules, 2016**',
              'Segregation & recording of discarded/expired medicines and cytotoxic waste (yellow '
              'category); annual return'],
             ['**Legal Metrology Act** & Packaged Commodities Rules',
              'Correct declaration of net quantity, MRP, mfg. date; verified weighing scales in store'],
             ['**GST Act** / financial rules', 'Tax invoice, HSN code, e-way bill; books of '
              'account preserved for the prescribed period'],
             ['**General Financial Rules (GFR) / State Store Purchase Rules**',
              'Government stores: purchase procedure, stock registers, physical verification, '
              'condemnation, write-off powers'],
             ['**Factories Act / Explosives & Petroleum Rules**',
              'Storage of inflammables, compressed gas cylinders, spirit'],
             ['**AERB regulations**', 'Radiopharmaceuticals — licence, lead storage, radiation '
              'log-book'],
             ['**Schedule M / GMP (for manufacturers)**',
              'Warehousing area requirements, batch manufacturing & distribution records, '
              'retention periods']])
    b.box('note', 'REMEMBER THE HIERARCHY',
          '**Act** (passed by Parliament) \u2192 **Rules / Order** (made by Government under the Act) '
          '\u2192 **Schedule** (a list appended to the Rules). Thus *Schedule H is a part of the '
          'Drugs and Cosmetics **Rules, 1945***, not of the Act.')

    # ------------------------------------------------------------------ 1.11
    b.h2('1.11', 'Materials Management — Where Records Keeping Fits')
    b.flow(['Demand forecast', 'Indent', 'Purchase', 'Goods inward',
            'Storage & records', 'Issue', 'Consumption data'])
    b.p('Notice that the cycle is **closed**: consumption data recorded at the issue stage becomes '
        'the forecast for the next indent. This is exactly why the syllabus links *records, '
        'classification, stock books, indents and storage* into one topic — they are five points '
        'on one circle.')
    b.table(['Element of materials management', 'Objective'],
            [['Materials planning & forecasting', 'How much will be needed'],
             ['Purchasing', 'Buying at right price/quality/time'],
             ['Receiving & inspection', 'Getting exactly what was ordered'],
             ['Stores & warehousing', 'Safe custody and quick retrieval'],
             ['Inventory control', 'Minimum investment, no stock-out'],
             ['Material handling & transport', 'Least damage, least cost'],
             ['Records, codification & standardisation', 'Identification, accountability, information'],
             ['Disposal of surplus/scrap', 'Recovery of value, space release']])
    b.box('hy', 'ECONOMIC IMPORTANCE',
          'In a typical hospital, **drugs and medical supplies consume roughly 30\u201340 % of the '
          'total recurring budget** (second only to salaries). Materials/stores management is '
          'therefore the biggest single area where a pharmacist can save money.')
    b.page_break()


def chapter2(b):
    b.chapter(2, 'The Purchase Cycle and Its Documents',
              'Because every store record begins with a purchase \u2022 methods of purchase '
              '\u2022 tenders \u2022 purchase order \u2022 document trail')

    b.lead('The goods inward section cannot check a consignment unless it holds the purchase '
           'order; the main store cannot post a ledger unless it holds the GRN; accounts cannot '
           'pay unless all three tally. Hence a working knowledge of the purchase cycle is '
           'compulsory before studying stores records.')

    # ------------------------------------------------------------------ 2.1
    b.h2('2.1', 'Purchasing — Meaning, Objectives and the 5 R\u2019s')
    b.box('def', 'PURCHASING',
          'Purchasing is the **procurement of materials of the right quality and quantity, from '
          'the right source, at the right price, and delivered at the right time and place**.')
    b.h3('2.1.1  The 5 R\u2019s (Six R\u2019s) of purchasing')
    b.table(['R', 'Meaning', 'Record that proves it'],
            [['Right **Quality**', 'Conforms to pharmacopoeial/tender specification',
              'Specification in PO, analytical/test report, GRN remarks'],
             ['Right **Quantity**', 'Neither excess (blocked capital, expiry) nor short (stock-out)',
              'Indent computation sheet, EOQ working, PO quantity'],
             ['Right **Price**', 'Lowest evaluated cost, not merely lowest quoted rate',
              'Comparative statement, rate contract, invoice'],
             ['Right **Time**', 'Supply before stock falls below minimum level',
              'Delivery schedule in PO, GRN date, lead-time register'],
             ['Right **Source**', 'Licensed, GMP-compliant, reliable manufacturer/dealer',
              'Supplier registration file, licence copies, performance register'],
             ['(Right **Place**)', 'Delivered at the specified store/consignee',
              'Consignee address in PO, challan, gate entry']])
    b.box('mnem', 'MNEMONIC', '**"Q-Q-P-T-S"** \u2014 **Q**uality, **Q**uantity, **P**rice, **T**ime, **S**ource.')

    # ------------------------------------------------------------------ 2.2
    b.h2('2.2', 'Steps in the Purchase Procedure')
    b.steps([
        '**Recognition of need** — stock reaches re-order level / user department demand / new '
        'item approved by the Pharmacy & Therapeutics Committee.',
        '**Preparation of indent (purchase requisition)** by the store, showing item, '
        'specification, code, quantity required, stock in hand, average consumption and budget head.',
        '**Scrutiny & sanction** of the indent by the competent authority (technical scrutiny by '
        'pharmacist, financial sanction by the officer having powers).',
        '**Selection of method of purchase** — tender, rate contract, spot purchase, etc.',
        '**Issue of enquiry / tender notice (NIT)** with complete specifications, terms, '
        'earnest money and last date.',
        '**Receipt and opening of quotations/tenders** on the notified date and time before a '
        'committee, all members initialling each rate.',
        '**Preparation of comparative statement** and **technical evaluation** (licence, GMP, '
        'market standing, samples).',
        '**Negotiation** (only with the lowest evaluated/L-1 bidder, as a rule) and '
        '**approval of the Purchase Committee**.',
        '**Placing the Purchase Order (PO) / supply order** on the successful bidder; security '
        'deposit / performance guarantee obtained.',
        '**Follow-up** with the supplier for timely delivery (reminders, delivery-period extension).',
        '**Receipt of consignment in the goods inward section**; checking, inspection, testing, '
        'GRN.',
        '**Posting of stock records** (bin card, stock ledger, batch/expiry register).',
        '**Bill passing** — three-way matching of PO, GRN and invoice; deduction of penalties/'
        'liquidated damages if any.',
        '**Payment** through accounts and **release of security deposit** after the warranty period.',
        '**Recording of supplier performance** (delay, short supply, quality failure) for future '
        'vendor rating.',
    ])
    b.flow(['Indent', 'Sanction', 'Tender/Enquiry', 'Comparative statement', 'Purchase Order',
            'Receipt + GRN', 'Stock records', 'Bill passing', 'Payment'])

    # ------------------------------------------------------------------ 2.3
    b.h2('2.3', 'Methods of Purchase')
    b.table(['Method', 'When used / salient features'],
            [['**Open / global tender** (advertised tender)',
              'Widest publicity in newspapers & website; for large value purchases; most '
              'transparent but slow. "Global" when foreign firms may also bid'],
             ['**Limited / closed tender**', 'Enquiry sent only to a short-list of registered, '
              'approved suppliers; used for medium value or urgent needs'],
             ['**Single tender / proprietary purchase**',
              'Only one source exists (patented or proprietary item, sole manufacturer); '
              'justification recorded in writing'],
             ['**Rate contract (RC)**', 'Rates & terms fixed in advance for a period (usually 1\u20132 '
              'years) by a central agency; indenting unit simply places supply orders as needed. '
              '**No tendering each time, no stock holding by the buyer** \u2014 biggest advantage'],
             ['**Running contract / standing contract**',
              'Fixed quantity to be supplied over a period in instalments'],
             ['**Negotiated purchase**', 'Price negotiated with supplier(s) after bids; normally '
              'only with L-1'],
             ['**Spot / cash purchase (local purchase)**',
              'Small, urgent, emergency requirement purchased locally within delegated financial '
              'powers, against cash memo'],
             ['**Direct purchase from manufacturer / government pool**',
              'e.g. from a public-sector drug company, Jan Aushadhi/BPPI, CMSS or state medical '
              'services corporation'],
             ['**GeM / e-procurement portal**', 'Government e-Marketplace; online bidding, '
              'reverse auction, transparent audit trail'],
             ['**Group / centralised (pooled) purchase**',
              'Several hospitals pool demand to obtain quantity discount'],
             ['**Blanket order**', 'One order for a period; deliveries as per call-off schedule'],
             ['**Consignment / VMI purchase**',
              'Supplier keeps stock in the hospital store; payment only on consumption']])
    b.box('exam', 'MOST COMMONLY ASKED',
          '**Rate Contract** = *rate is fixed, quantity is not fixed*. **Running contract** = '
          '*quantity is also fixed*. The **lowest tenderer is called L-1**; earnest money is also '
          'called **bid security**, and money kept after award of contract is the **security '
          'deposit / performance guarantee**.')

    # ------------------------------------------------------------------ 2.4
    b.h2('2.4', 'The Tender System in Detail')
    b.h3('2.4.1  Sequence')
    b.numbered([
        'Notice Inviting Tender (**NIT**) published / uploaded.',
        'Sale or download of **tender document** (specifications, terms & conditions, '
        'eligibility, penalty clause).',
        'Submission in **two-bid system** \u2014 *Technical bid* and *Price (financial) bid* in '
        'separate sealed covers.',
        'Deposit of **Earnest Money Deposit (EMD)** with the technical bid.',
        '**Opening of technical bids** on the appointed date before the tender committee; '
        'evaluation of licences, GMP/WHO-GMP certificate, market standing, samples, turnover.',
        '**Opening of price bids** of only technically qualified firms.',
        'Preparation of **comparative statement**; identification of **L-1**.',
        'Approval of the competent authority / Purchase Committee.',
        'Issue of **Letter of Intent / Purchase Order**; EMD of unsuccessful bidders refunded.',
        'Successful bidder furnishes **Security Deposit / Performance Bank Guarantee** and signs '
        'the agreement.',
    ])
    b.h3('2.4.2  Important tender terminology')
    b.table(['Term', 'Meaning'],
            [['EMD (earnest money / bid security)', 'Token deposit with the bid to prevent '
              'frivolous bidding; forfeited if bidder withdraws'],
             ['Security deposit / performance guarantee', 'Held during the contract to ensure '
              'performance; refunded after satisfactory completion'],
             ['Liquidated damages (LD) / penalty', 'Deduction for late supply, commonly a % of '
              'value per week of delay subject to a maximum'],
             ['Risk purchase', 'If supplier fails, the buyer purchases elsewhere and recovers the '
              'extra cost from the defaulter'],
             ['Validity of offer', 'Period during which the quoted rate cannot be withdrawn'],
             ['Fall-clause', 'Supplier must not sell the same item to anyone else at a lower rate '
              'during the contract'],
             ['Escalation clause', 'Provision for price revision if raw material/statutory levies change'],
             ['FOR destination', 'Freight paid by supplier up to the consignee\u2019s store'],
             ['FOB / CIF', '*Free On Board* (buyer bears freight & insurance from port) / '
              '*Cost, Insurance, Freight* (seller bears them up to destination port)'],
             ['Pre-qualification', 'Screening of bidders before price bids are opened'],
             ['Reverse auction', 'Online downward bidding by suppliers to reach the lowest price']])

    # ------------------------------------------------------------------ 2.5
    b.h2('2.5', 'Purchase Committee, PTC and the Hospital Formulary')
    b.kv([
        ('Purchase / Tender Committee', 'Opens and evaluates tenders, negotiates, recommends '
                                        'award. Usually includes the Medical Superintendent, '
                                        'Store Officer, Chief Pharmacist, Accounts Officer and a '
                                        'clinician.'),
        ('Pharmacy and Therapeutics Committee (PTC)', 'Advisory body of doctors + pharmacists that '
                                                      'selects which drugs the hospital will stock, '
                                                      'prepares and revises the **hospital '
                                                      'formulary**, frames drug-use policies, '
                                                      'reviews ADRs and monitors drug utilisation.'),
        ('Hospital formulary', 'A continually revised compilation of the drugs **approved for use '
                               'in that hospital**, with essential prescribing information. It '
                               '*limits the variety of items* the store must stock \u2014 i.e. it is '
                               'the first step of **standardisation and variety reduction**.'),
        ('Essential Medicines List (NLEM)', 'National list of medicines that satisfy the priority '
                                            'health-care needs of the population, selected on '
                                            'efficacy, safety, cost-effectiveness; the basis of '
                                            'most government indenting and of DPCO price control.'),
    ])
    b.box('hy', 'HIGH-YIELD',
          'The body that decides **which** drugs are stocked = **Pharmacy & Therapeutics Committee**. '
          'The body that decides **from whom and at what rate** they are bought = **Purchase / '
          'Tender Committee**. The document that lists approved drugs = **Hospital Formulary**.')

    # ------------------------------------------------------------------ 2.6
    b.h2('2.6', 'Documents of the Purchase\u2013Receipt\u2013Payment Cycle')
    b.table(['Document', 'Raised by', 'Purpose / contents'],
            [['Indent / Purchase requisition', 'Store or user department',
              'Formal demand: item, code, specification, quantity, stock in hand, consumption, '
              'urgency, budget head'],
             ['Enquiry / RFQ / NIT', 'Purchase section',
              'Invites rates with specification and terms'],
             ['Quotation / tender / bid', 'Supplier', 'Offer of rate, terms, delivery period, validity'],
             ['Comparative statement', 'Purchase section',
              'Side-by-side rates of all bidders to identify L-1'],
             ['**Purchase Order (PO) / supply order**', 'Purchase section',
              'The **contract**: what, how much, at what rate, when and where to deliver'],
             ['Acknowledgement / acceptance of order', 'Supplier', 'Confirms acceptance of PO terms'],
             ['**Delivery challan / despatch note**', 'Supplier',
              'Accompanies goods, lists what has physically been sent'],
             ['**Invoice / bill (tax invoice)**', 'Supplier',
              'Demand for money: rate, quantity, discount, GST, total; batch nos. and expiry '
              'dates for drugs'],
             ['Packing list / case-wise list', 'Supplier', 'Contents of each case/carton'],
             ['Lorry receipt (LR) / consignment note / railway receipt', 'Transporter',
              'Proof of handing over goods to the carrier; needed for transit claims'],
             ['Insurance policy / transit insurance', 'Supplier or buyer', 'Cover for transit loss'],
             ['Gate entry (inward) register', 'Security / gate',
              'Vehicle no., time, name of supplier, no. of packages'],
             ['**Goods Received Note (GRN) / Material Receipt Report**', 'Goods inward section',
              'Certifies what was actually received, in what condition, accepted/rejected quantity'],
             ['Inspection / analytical test report', 'Inspection cell / QC laboratory',
              'Quality clearance ("approved"/"rejected")'],
             ['Discrepancy / shortage / damage report', 'Goods inward section',
              'Basis of claim on supplier, carrier or insurer'],
             ['Debit note / credit note', 'Buyer / supplier', 'Financial adjustment for rejected, '
              'short or over-charged goods'],
             ['Bill passing order / payment voucher', 'Accounts',
              'Sanction and record of payment after three-way matching'],
             ['Material Return Note (MRN)', 'User dept. / store', 'Return of unused or rejected material'],
             ['Gate pass (returnable / non-returnable)', 'Store',
              'Authorises material to leave the premises']])
    b.box('exam', 'THREE-WAY MATCHING',
          'No bill is passed for payment until **Purchase Order = Goods Received Note = Invoice** '
          'agree on item, quantity and rate. Learn this triad \u2014 it is the most commonly examined '
          'internal-control concept in stores accounting.')

    # ------------------------------------------------------------------ 2.7
    b.h2('2.7', 'Purchase Order — Contents and Distribution of Copies')
    b.h3('2.7.1  Essential contents')
    b.bullets([
        'PO number and date (the unique reference quoted in every later document).',
        'Name and address of the **supplier**; reference to their quotation/tender & rate contract no.',
        'Name and address of the **consignee** (where to deliver) and of the **paying authority**.',
        'Full **description, specification, brand/generic name, strength, dosage form, pack size** '
        'and **store code number** of each item.',
        '**Quantity** ordered with unit of measurement; **rate** per unit; discount; GST/HSN; total value.',
        '**Delivery period / schedule** and place; mode of despatch; packing & marking instructions.',
        '**Shelf-life clause** — commonly *"not less than 5/6 of the total shelf life remaining at '
        'the time of delivery"* (a very frequently asked condition for drug purchase).',
        'Requirement of **batch-wise analytical report** and/or pre-despatch inspection.',
        'Terms of **payment**, penalty/liquidated damages, warranty/guarantee, replacement of '
        'NSQ or expired stock.',
        'Arbitration and jurisdiction clause; signature of the competent authority with seal.',
    ])
    b.h3('2.7.2  Typical distribution of copies')
    b.table(['Copy', 'Sent to', 'Why'],
            [['Original', 'Supplier', 'The contract / authority to supply'],
             ['2nd copy', 'Accounts / finance', 'To create liability and check the bill'],
             ['3rd copy', '**Goods inward / receiving section**', 'To check the consignment on arrival'],
             ['4th copy', 'Main store / indenting department', 'To know dues-in and update records'],
             ['5th (office) copy', 'Purchase section file', 'Record & follow-up']])
    b.box('note', 'DUES-IN (ON-ORDER) REGISTER',
          'The quantity ordered but not yet received is called **dues-in / on-order quantity**. It '
          'is recorded in the *Purchase Order (dues-in) Register* and **must be deducted while '
          'preparing the next indent**, otherwise double ordering occurs \u2014 a classic audit objection.')

    # ------------------------------------------------------------------ 2.8
    b.h2('2.8', 'Records Maintained by the Purchase Section')
    b.table(['Register / file', 'Contents'],
            [['Indent register', 'Serial no., date, indenting dept., item, quantity, action taken'],
             ['Tender / quotation register', 'NIT no., date of opening, firms responded, L-1'],
             ['Purchase order (supply order) register',
              'PO no., date, firm, item, quantity, rate, value, delivery due date'],
             ['Dues-in / pending order register', 'Outstanding quantity against each PO, reminders sent'],
             ['Rate contract register', 'Item, firm, rate, validity period'],
             ['Supplier / vendor registration file', 'Licence, GMP certificate, PAN/GST, past performance'],
             ['Vendor rating / performance register', 'Timeliness, quality failures, short supplies, '
              'blacklisting'],
             ['Bill / invoice register', 'Bill no., date, amount, GRN no., date of passing, payment date'],
             ['Price history / market rate register', 'Rate trend of each item over the years'],
             ['Budget control register', 'Head-wise allotment, commitment, expenditure, balance']])
    b.box('hy', 'LINK TO THE SYLLABUS',
          'The examiner\u2019s phrase *"clerical procedure in the goods inward section"* begins exactly '
          'where this chapter ends \u2014 at the moment the supplier\u2019s vehicle reaches the gate with '
          'the goods, the challan and the invoice, against the Purchase Order already lying with '
          'the receiving clerk.')
    b.page_break()
