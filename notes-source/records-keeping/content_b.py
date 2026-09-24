# -*- coding: utf-8 -*-
"""Part II — The core syllabus: Chapter 3 (goods inward) & Chapter 4 (main stores)"""


def chapter3(b):
    b.part('PART II', 'Goods Inward Section & Main Stores')
    b.chapter(3, 'Clerical Procedure in the Goods Inward Section',
              'Receiving section \u2022 documents accompanying a consignment \u2022 checking '
              '\u2022 GRN \u2022 quarantine \u2022 discrepancies & claims \u2022 bill passing')

    b.lead('This is the chapter the syllabus names first, and it is the most examined. Learn the '
           'procedure as a *chain of documents*: Gate entry \u2192 Challan/Invoice \u2192 GRN \u2192 '
           'Inspection report \u2192 Bin card & Ledger \u2192 Bill passing. If you can write that chain '
           'in order, you can answer almost any question set on it.')

    # ------------------------------------------------------------------ 3.1
    b.h2('3.1', 'Goods Inward Section — Meaning, Siting and Layout')
    b.box('def', 'GOODS INWARD SECTION',
          'The **goods inward (receiving) section** is that part of the stores department where all '
          'incoming consignments are **received, unloaded, unpacked, counted, checked against the '
          'purchase order, inspected for quality, documented on a Goods Received Note and then '
          'either taken on charge or rejected**. It is also called the *receiving section*, '
          '*receiving bay*, *inward goods section* or *goods receipt section*.')
    b.kv([
        ('Position in the flow of materials', 'It is the **entry gate of the store** — the point at '
         'which the ownership, custody and accountability of material passes from the supplier '
         '(and carrier) to the organisation.'),
        ('Why "clerical" procedure', 'Because the physical work of unloading is only half the job; '
         'the other half is **paper work** — entering, verifying, certifying, posting and filing '
         'the documents, which is what fixes legal and financial responsibility.'),
        ('Siting', 'On the **ground floor**, adjoining the main store, with a *covered loading/'
         'unloading platform* at truck-bed height, wide doors, direct road access and a weighing '
         'machine. It must be **separate from the issue/despatch counter** so that incoming and '
         'outgoing material never mix.'),
        ('Golden rule of layout', '**One-way (straight-line) flow** \u2014 unloading \u2192 unpacking '
         '\u2192 counting/checking \u2192 quarantine \u2192 approved storage; never allow back-tracking '
         'or cross-traffic.'),
    ])
    b.h3('3.1.2  Facilities and equipment needed in the receiving section')
    b.table(['Facility', 'Purpose'],
            [['Covered unloading dock / platform + ramp / trolleys / pallet truck',
              'Safe, weather-protected unloading; prevents breakage of glass and IV fluids'],
             ['Weighing scale (verified/stamped)', 'To verify weight-based consignments and detect '
              'pilferage in transit'],
             ['Unpacking table with good light, cutters, crow-bar',
              'Opening cases without damaging contents'],
             ['Counting space / counting tray', 'Accurate quantitative check'],
             ['Sampling table + sampling tools, sample bottles, labels',
              'Drawing samples for quality testing'],
             ['**Quarantine ("Under Test") area** \u2014 yellow marked',
              'Holding the consignment till quality clearance; must be lockable'],
             ['**Approved** (green) and **Rejected** (red) areas',
              'Physical segregation prevents accidental issue of untested/rejected goods'],
             ['Refrigerator / ILR near the dock', 'Immediate shifting of cold-chain items'],
             ['Thermometer, data-logger, cold-chain monitor readers',
              'Verifying that the cold chain was not broken in transit'],
             ['Desk, computer/terminal, GRN books, rubber stamps, PO file',
              'The clerical work itself'],
             ['Fire extinguisher, first-aid box, spill kit',
              'Safety during handling of chemicals and glass']])

    # ------------------------------------------------------------------ 3.2
    b.h2('3.2', 'Functions of the Goods Inward Section')
    b.numbered([
        'To **receive** all incoming consignments and record their arrival (gate entry).',
        'To verify that the goods are **meant for the organisation** and are covered by a valid '
        '**purchase order / rate contract**.',
        'To **unload, unpack and count** the goods and carry out the **quantitative check**.',
        'To carry out the **qualitative (technical) check** — name, strength, dosage form, pack, '
        'batch number, manufacturing and expiry date, storage condition, physical condition, '
        'labelling, MRP, manufacturer\u2019s licence number.',
        'To **draw samples** and send them for analytical testing where the order or policy requires.',
        'To place the consignment in **quarantine** pending inspection/test results.',
        'To prepare the **Goods Received Note (GRN)** and the entry in the **Goods Inward Register**.',
        'To record and report **discrepancies** — shortage, excess, breakage, damage, wrong supply, '
        'short expiry, unordered goods.',
        'To arrange **acceptance** (transfer to main store with documents) or **rejection** '
        '(segregation, intimation to supplier, return).',
        'To lodge **claims** on the supplier, the carrier (transporter/railway) or the insurance company.',
        'To **certify the invoice/bill** for payment and forward it to accounts with the GRN.',
        'To **file and preserve** all receipt documents for audit and legal inspection.',
    ])

    # ------------------------------------------------------------------ 3.3
    b.h2('3.3', 'Staff of the Goods Inward Section and Their Duties')
    b.table(['Personnel', 'Duties'],
            [['Receiving / Goods Inward Clerk', 'Gate entry; checks challan & invoice against PO; '
              'supervises unpacking and counting; prepares GRN and discrepancy report; maintains '
              'Goods Inward Register; files documents'],
             ['Pharmacist (receiving)', '**Technical check** \u2014 generic & brand name, strength, '
              'dosage form, batch no., mfg./exp. date, remaining shelf life, storage requirement, '
              'labelling & pack integrity; draws samples; certifies fitness for taking on charge'],
             ['Store Keeper', 'Takes accepted goods on charge, allots bin/rack location, posts '
              '**bin card**'],
             ['Store Officer / Materials Manager', 'Countersigns GRN; decides on rejections, '
              'claims, penalties; liaises with purchase and accounts'],
             ['Inspection committee / QC laboratory', 'Independent quality inspection and '
              'analytical report'],
             ['Security / gate staff', 'Gate entry register, vehicle details, number of packages, '
              'seal condition'],
             ['Helper / packer / loader', 'Unloading, unpacking, stacking, shifting to quarantine '
              'or store']])
    b.box('exam', 'INTERNAL CHECK',
          'The person who **receives** the goods should **not** be the person who **ordered** them, '
          'and the **inspecting** authority should preferably be independent of both. This is why '
          'the GRN is prepared by the receiving clerk but **countersigned** by the store officer '
          'and supported by a separate **inspection report**.')

    # ------------------------------------------------------------------ 3.4
    b.h2('3.4', 'Documents Accompanying / Supporting a Consignment')
    b.table(['Document', 'Issued by', 'What the receiving clerk checks in it'],
            [['**Purchase Order (PO) copy**', 'Purchase section (already held)',
              'The master reference — item, specification, quantity, rate, delivery date, '
              'shelf-life clause, consignee'],
             ['**Delivery challan / despatch note**', 'Supplier',
              'What has physically been sent; number of cases; PO number quoted'],
             ['**Invoice / tax invoice / bill**', 'Supplier',
              'Description, quantity, rate, discount, GST & HSN, total; **batch no. and expiry '
              'date of each item**; supplier\u2019s drug licence no., GSTIN, and (for scheduled '
              'formulations) the DPCO ceiling price'],
             ['**Packing list / case-wise list**', 'Supplier',
              'Contents of each carton, so that a short-packed case can be pinpointed'],
             ['**Lorry receipt (LR) / consignment note / railway receipt (RR)**', 'Transporter',
              'Number of packages booked, weight, condition at booking, freight paid/to-pay — '
              'basis of any **transit claim**'],
             ['**Insurance policy / cover note**', 'Supplier or buyer',
              'Whether transit loss is insured and by whom'],
             ['**Test / analytical report (batch certificate of analysis)**',
              'Manufacturer\u2019s QC', 'Batch-wise compliance with pharmacopoeial standards'],
             ['**Gate entry (inward) slip**', 'Security',
              'Date & time of arrival, vehicle number, driver, number of packages, seal intact?'],
             ['**Guarantee / warranty certificate, and (for equipment) manuals**', 'Supplier',
              'Warranty period, installation obligation'],
             ['**Cold-chain / temperature data-logger record**', 'Transporter/supplier',
              'Whether 2\u20138 \u00B0C was maintained throughout transit']])
    b.box('hy', 'CHALLAN vs INVOICE \u2014 classic MCQ',
          '**Delivery challan** = document of *movement of goods* (says *what has been sent*); it '
          'travels with the goods and does **not** demand money. **Invoice (bill)** = document of '
          '*demand for payment* (says *what is payable*), showing rate, GST and total value. A '
          '**GRN** is prepared by the **buyer**, not the supplier.')

    # ------------------------------------------------------------------ 3.5
    b.h2('3.5', 'The Clerical Procedure — Step by Step')
    b.p('This is the *heart of the syllabus*. Learn the 16 steps in order; every sub-question '
        '(GRN, discrepancy, quarantine, bill passing) is only a detail of one of these steps.')
    b.steps([
        '**Arrival & gate entry.** The vehicle reports at the gate. Security records date, time, '
        'vehicle number, name of supplier/transporter and **number of packages** in the '
        '**Gate Entry (Inward) Register** and issues a gate entry slip. Condition of seals and of '
        'packages is noted *before* unloading.',
        '**Receipt of documents.** The driver/representative hands over the **delivery challan, '
        'invoice, packing list and LR**. The clerk stamps them with date of receipt and a serial '
        '*inward number*.',
        '**Verification of authority to supply.** The clerk retrieves the **office copy of the '
        'Purchase Order** (or the rate-contract supply order) and confirms: correct consignee, '
        'valid PO number, item actually ordered, **delivery period not expired**. *Unordered goods '
        'are not unloaded* — they are refused or kept unopened with intimation to purchase section.',
        '**Unloading and counting of packages.** Packages are counted against the challan/LR. Any '
        'shortage in the **number of packages**, or a torn/wet/re-stitched/open package, is '
        'recorded **on the carrier\u2019s copy of the LR itself** and the driver\u2019s signature '
        'obtained — this is essential to sustain a claim later. Weighment is done where relevant.',
        '**Unpacking.** Cases are opened carefully at the unpacking table in the presence of the '
        'receiving clerk (and the supplier\u2019s representative if present). Packing material is '
        'retained until checking is complete, as small items often remain inside.',
        '**Quantitative check.** Each item is counted/measured and compared with **(a)** the '
        'challan, **(b)** the invoice and **(c)** the purchase order. Units of measurement are '
        'converted where necessary (e.g. PO in "1,000 tablets", supply in "10 boxes of 10 \u00D7 10").',
        '**Qualitative / technical check by the pharmacist.** Name (generic + brand), strength, '
        'dosage form, pack size, **batch number, date of manufacture, date of expiry, remaining '
        'shelf-life**, storage instruction, label completeness, manufacturer\u2019s name & licence '
        'number, MRP/DPCO price, ISI/BIS or sterility markings, physical condition (colour, '
        'clarity, caking, leakage, broken seal, cracked ampoule), and whether the batch figures in '
        'any **drug alert / recall list**.',
        '**Sampling for analytical test.** Where the PO or hospital policy requires, a sample of '
        'each batch is drawn, labelled (item, batch, GRN no., date), entered in the '
        '**Sample Register** and sent to the approved laboratory with a covering memo. The '
        'consignment stays in quarantine meanwhile.',
        '**Movement to the quarantine ("Under Test") area.** The consignment is stacked in the '
        'quarantine area with a **yellow "QUARANTINE / UNDER TEST" label** showing item, batch, '
        'quantity and GRN number. Cold-chain items go straight into the refrigerator/ILR, still '
        'labelled as quarantined.',
        '**Entry in the Goods Inward Register (Daily Receipt Register).** A serial, date-wise entry '
        'of every consignment received on that day — the *primary chronological record* of receipts.',
        '**Preparation of the Goods Received Note (GRN).** The clerk prepares the GRN in the '
        'prescribed number of copies showing quantity ordered, quantity received, quantity '
        'accepted, quantity rejected/short, batch and expiry details and remarks. It is signed by '
        'the receiving clerk, the pharmacist and countersigned by the Store Officer. **The GRN is '
        'the pivotal document of the whole section.**',
        '**Inspection / test result and disposal of the consignment.** On receipt of the inspection '
        'or analytical report the quarantine label is replaced by a **green "APPROVED"** label '
        '(goods moved to main store) or a **red "REJECTED"** label (goods moved to the rejected/'
        'salvage area, supplier informed, arranged for return/replacement).',
        '**Taking on charge and posting of stock records.** For accepted quantities the store '
        'keeper allots a bin/rack location and posts the **bin card**; the ledger clerk posts the '
        '**stock ledger / stock register** and the **batch-and-expiry register** — each quoting '
        'the **GRN number** as authority.',
        '**Reporting of discrepancies and lodging of claims.** A **Discrepancy / Shortage / Damage '
        'Report** is raised and copies sent to the purchase section, the supplier, the carrier and '
        'the insurer as applicable, followed by a **debit note** for the value involved.',
        '**Certification of the bill and passing for payment.** The invoice is stamped and '
        'certified *"Received in good condition and taken on stock vide GRN No. ____ dated ____"*, '
        'the accepted quantity and rate verified against the PO (**three-way matching**), '
        'penalties/liquidated damages for late supply noted, and the bill forwarded to accounts.',
        '**Filing, follow-up and MIS.** GRN, challan, invoice copy, inspection report and claim '
        'correspondence are filed **PO-wise / GRN-number-wise**; the purchase section is informed '
        'so that the **dues-in (pending order) register** is closed or partly closed; supplier '
        'performance (delay, short supply, quality failure) is recorded for **vendor rating**.',
    ])
    b.flow(['Gate entry', 'Documents vs PO', 'Unload & count', 'Quantity check',
            'Quality check', 'Sample to QC', 'Quarantine', 'GRN',
            'Approved / Rejected', 'Bin card + Ledger', 'Bill passing', 'Filing'])
    b.box('mnem', 'MNEMONIC for the 16 steps',
          '**"G-D-P-U-U-Q-Q-S-Q-G-G-I-T-D-B-F"** \u2014 **G**ate entry, **D**ocuments, **P**O check, '
          '**U**nload, **U**npack, **Q**uantity, **Q**uality, **S**ample, **Q**uarantine, '
          '**G**oods Inward Register, **G**RN, **I**nspection result, **T**ake on charge, '
          '**D**iscrepancy report, **B**ill passing, **F**iling.')

    # ------------------------------------------------------------------ 3.6
    b.h2('3.6', 'Checking of the Consignment in Detail')
    b.h3('3.6.1  Quantitative check')
    b.bullets([
        'Count/measure **every item** — sample counting is allowed only for large homogeneous '
        'consignments, and then the method must be recorded.',
        'Compare with **three** documents: challan (what was sent), invoice (what is charged) and '
        '**purchase order (what was ordered)**. The *lowest* of the three governs what can be '
        'accepted and paid for.',
        'Convert units carefully (strips \u2192 tablets, vials \u2192 ml, bottles \u2192 litres).',
        'Watch for **excess supply**: excess quantity is **not** taken on charge without sanction; '
        'it is either returned or a supplementary order/regularisation is obtained.',
        'Record **shortages** immediately on the carrier\u2019s documents and on the GRN.',
    ])
    b.h3('3.6.2  Qualitative (technical) check — the pharmacist\u2019s checklist')
    b.table(['What to check', 'Why it matters / what to reject'],
            [['Generic name, brand, strength, dosage form',
              'Supply of a different salt, strength or dosage form = wrong supply; reject'],
             ['Pack size and pack type', 'Affects rate per unit and dispensing convenience'],
             ['**Batch (Lot) number**', 'Mandatory for traceability and recall; unbatched stock is '
              'not acceptable'],
             ['**Date of manufacture (Mfg.) & date of expiry (Exp.)**',
              'Expired or expiring stock must never be accepted'],
             ['**Remaining shelf life**', 'Standard tender condition: at least **5/6 (83 %) of the '
              'total shelf life**, or a minimum of **~75 % / not less than 2 years** as specified '
              'in the PO; short-expiry stock is rejected or accepted only with written sanction'],
             ['Storage condition on the label', 'Cold-chain, "protect from light", "do not freeze" '
              '\u2014 dictates immediate shifting'],
             ['Condition of container & seal', 'Leakage, breakage, cracked ampoules, loose caps, '
              'swollen/punctured blister, wet cartons, damaged strip = reject'],
             ['Physical appearance of the drug', 'Discolouration, caking, mottling of tablets, '
              'turbidity or precipitate in injections, separation of emulsion, mould growth, '
              'crystallisation, softening of suppositories'],
             ['Sterility indicators for sterile products',
              'Intact seal, clarity, absence of particulate matter, valid sterilisation lot'],
             ['Label particulars', 'Manufacturer\u2019s name & address, **mfg. licence number**, '
              'net content, **"Schedule H / H1 / X"** warning with **Rx / \u2716 symbol**, storage '
              'directions, batch, mfg./exp. dates, MRP, "for hospital/government supply \u2014 not '
              'for sale" where applicable'],
             ['MRP / DPCO ceiling price', 'Overcharging on price-controlled formulations must be '
              'objected to'],
             ['Presence in **drug alert / NSQ / recall list**', 'Batch to be quarantined and '
              'reported at once'],
             ['Accompanying documents', 'Certificate of analysis, warranty, manuals, accessories'],
             ['Cold-chain evidence', 'Vaccine Vial Monitor stage, cold-chain monitor card, '
              'data-logger printout \u2014 breach = reject']])
    b.box('caution', 'NEVER ACCEPT',
          bullets=['Drugs **without batch number, manufacturing date or expiry date**.',
                   'Drugs that are **expired or of short expiry** beyond the PO condition.',
                   'Consignments with **broken seals, leakage, wet or re-stitched packages** '
                   '(accept "under protest" only after recording the damage).',
                   'Cold-chain items where the **cold chain has demonstrably broken** (VVM stage '
                   '3/4, frozen DPT/Hep-B, thawed insulin).',
                   '**Unordered / excess** goods without written sanction.',
                   'Physician\u2019s **samples** or "not for sale" stock for regular hospital use '
                   'unless specifically permitted.'])

    # ------------------------------------------------------------------ 3.7
    b.h2('3.7', 'Goods Received Note (GRN) — The Pivotal Document')
    b.box('def', 'GRN',
          'A **Goods Received Note** (also *Goods Receipt Note*, *Material Receipt Report*, '
          '*Receiving Report*, *Store Receipt Voucher*) is the internal document prepared by the '
          'receiving section **certifying the quantity and condition of material actually '
          'received** against a purchase order. It is the **authority (a) for the store to take '
          'goods on charge, (b) for the ledger clerk to post the stock records and (c) for '
          'accounts to pay the bill.**')
    b.h3('3.7.1  Contents of a GRN')
    b.table(['Group', 'Columns / particulars'],
            [['Identification', 'GRN serial number and date; inward/gate entry number'],
             ['Supplier', 'Name & address of supplier; their challan no. & date; invoice no. & '
              'date; LR/RR no. & date; transporter'],
             ['Order reference', 'Purchase order no. & date (or rate contract no.); indent no.'],
             ['Item details', 'Sl. no.; **store code number**; description/specification; unit of '
              'measurement'],
             ['Quantities', 'Quantity ordered \u2022 quantity as per challan/invoice \u2022 **quantity '
              'actually received** \u2022 quantity accepted \u2022 quantity rejected/short/damaged'],
             ['Drug-specific data', '**Batch no., date of manufacture, date of expiry**, pack size, '
              'manufacturer'],
             ['Value', 'Rate, discount, GST, total value of accepted quantity'],
             ['Inspection', 'Sample sent (yes/no), test report no. & date, result: approved/rejected'],
             ['Storage', 'Bin/rack/location allotted; storage condition required'],
             ['Remarks', 'Shortage, breakage, short expiry, late delivery, damage in transit, '
              '"accepted under protest"'],
             ['Signatures', 'Receiving clerk \u2022 Pharmacist/inspecting officer \u2022 Store keeper '
              '\u2022 **Countersignature of Store Officer**']])
    b.h3('3.7.2  Copies of the GRN and their distribution')
    b.table(['Copy', 'Goes to', 'Use'],
            [['1st (original)', '**Accounts / finance section**',
              'Attached to the supplier\u2019s bill; authority for payment'],
             ['2nd', '**Purchase section**', 'To close/partly close the order in the dues-in '
              'register and to record supplier performance'],
             ['3rd', '**Main store (ledger clerk)**', 'Authority to post the stock ledger and bin card'],
             ['4th', '**Supplier** (when required)', 'Acknowledgement of receipt of goods'],
             ['5th (book copy)', '**Goods inward section file**', 'Record, audit and reference']])
    b.box('hy', 'REMEMBER',
          'GRN is prepared in the **goods inward/receiving section**, normally in **4\u20135 copies**, '
          'and is **numbered serially**. *No material may be taken on stock, and no bill may be '
          'paid, without a GRN.* Where the material fails inspection, the GRN still records the '
          'receipt but shows the quantity as **rejected**.')
    b.h3('3.7.3  Specimen format — Goods Received Note')
    b.table(['Sl.', 'Code', 'Description', 'Unit', 'Qty ord.', 'Qty recd.',
             'Qty acc.', 'Qty rej.', 'Batch', 'Mfg.', 'Exp.', 'Rate', 'Value', 'Remarks'],
            [['1', '', '', '', '', '', '', '', '', '', '', '', '', ''],
             ['2', '', '', '', '', '', '', '', '', '', '', '', '', ''],
             ['3', '', '', '', '', '', '', '', '', '', '', '', '', '']],
            size=7.5, first_col_bold=False, min_cm=0.85,
            caption='Format 3.1  GRN (upper part carries GRN No. & date, supplier, challan, '
                    'invoice, LR and PO references; lower part carries signatures)')

    # ------------------------------------------------------------------ 3.8
    b.h2('3.8', 'Goods Inward Register (Daily Receipt Register)')
    b.p('While the GRN is *consignment-wise*, the Goods Inward Register is *date-wise* — it is the '
        'chronological diary of the receiving section and the first document an auditor or drug '
        'inspector asks for.')
    b.table(['Sl. No.', 'Date of receipt', 'Supplier', 'Challan/Invoice No. & date',
             'PO No. & date', 'Item & quantity', 'GRN No.', 'Remarks / disposal'],
            [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']],
            size=8, first_col_bold=False, min_cm=1.1,
            caption='Format 3.2  Goods Inward / Daily Receipt Register')

    # ------------------------------------------------------------------ 3.9
    b.h2('3.9', 'Quarantine, Acceptance and Rejection')
    b.table(['Status', 'Label colour (usual practice)', 'Action'],
            [['Under test / quarantine', '**Yellow**', 'Stacked separately in the quarantine area; '
              'no issue permitted; entry in quarantine register'],
             ['Approved / released', '**Green**', 'Moved to the main storage area; taken on charge; '
              'bin card and ledger posted'],
             ['Rejected', '**Red**', 'Moved to the rejected/salvage area under lock; supplier '
              'informed; returned within the stipulated period; debit note raised'],
             ['Recalled / NSQ', '**Red "RECALLED \u2014 DO NOT ISSUE"**',
              'Batch withdrawn from all sub-stores, quarantined, reported to the licensing '
              'authority, returned/destroyed as directed']])
    b.box('exam', 'QUARANTINE',
          'Quarantine means **physical or administrative segregation of material awaiting a '
          'decision on its quality**. In a computerised store it may be "electronic quarantine" — '
          'the stock exists in the system but is *blocked for issue*. Colour convention: '
          '**yellow = under test, green = approved, red = rejected**.')

    # ------------------------------------------------------------------ 3.10
    b.h2('3.10', 'Handling of Discrepancies, Shortages, Damages and Claims')
    b.table(['Type of discrepancy', 'Meaning', 'Action by the goods inward section'],
            [['**Shortage in number of packages**', 'Fewer cases received than booked',
              'Record on the carrier\u2019s LR at the time of delivery, obtain driver\u2019s '
              'signature, take "short certificate" from the transporter, lodge claim on carrier'],
             ['**Short supply / short packing**', 'Package intact but contents fewer than invoiced',
              'Open in the presence of a witness, prepare shortage report, inform supplier, pay '
              'only for quantity received, raise debit note'],
             ['**Breakage / damage in transit**', 'Broken ampoules, leaking bottles, crushed cartons',
              'Preserve the damaged goods and packing as evidence, photograph, prepare damage '
              'report, claim on carrier and/or insurer, demand free replacement'],
             ['**Wrong supply**', 'Different drug, strength, dosage form, brand or pack than ordered',
              'Reject; do **not** take on charge; intimate purchase section; return at '
              'supplier\u2019s cost'],
             ['**Excess supply**', 'More than ordered',
              'Keep unopened/segregated; do not take on charge; obtain sanction for retention or '
              'return the excess'],
             ['**Short expiry / expired stock**', 'Remaining shelf life below the PO condition',
              'Reject; if unavoidable and urgently needed, accept only with **written sanction of '
              'the competent authority** and a supplier undertaking to replace unused stock'],
             ['**Not of Standard Quality (NSQ) on test**',
              'Analytical report fails pharmacopoeial limits',
              'Quarantine the entire batch, inform supplier & licensing authority, recall issued '
              'stock, reject and claim replacement/refund; enter in NSQ register'],
             ['**Spurious / misbranded / adulterated suspicion**', 'Doubtful label, price, source',
              'Freeze the stock, inform the **Drugs Control Organisation** immediately, do not '
              'return to supplier without instructions'],
             ['**Unordered goods**', 'No PO exists', 'Refuse delivery or keep unopened and inform '
              'purchase section'],
             ['**Late delivery**', 'Received after the delivery period',
              'Record the delay on the GRN so that **liquidated damages / penalty** can be '
              'deducted from the bill; extension of delivery period, if granted, must be on record'],
             ['**Cold-chain breach**', 'Temperature excursion during transit',
              'Segregate, do not use, obtain manufacturer\u2019s opinion, reject if stability is '
              'compromised; record data-logger printout']])
    b.h3('3.10.1  Debit note and credit note')
    b.kv([
        ('Debit note', 'Raised by the **buyer** on the supplier to reduce the amount payable — for '
                       'short supply, rejected goods, breakage, over-charging, penalty. It '
                       '*debits* the supplier\u2019s account.'),
        ('Credit note', 'Issued by the **supplier** to the buyer accepting that reduction, or on '
                        'return of goods. It *credits* the buyer\u2019s account.'),
        ('Material Return Note (MRN)', 'Prepared when material already taken on charge is returned '
                                       '\u2014 to the supplier (rejected/expired) or to the store '
                                       'by a user department (unused).'),
        ('Non-returnable / returnable gate pass', 'Authority for material to physically leave the '
                                                  'premises (e.g. goods returned to supplier, '
                                                  'equipment sent for repair).'),
    ])

    # ------------------------------------------------------------------ 3.11
    b.h2('3.11', 'Bill Passing and Payment Procedure')
    b.steps([
        'Invoice received (with the consignment or separately by post) is entered in the **Bill '
        '/ Invoice Register** with date of receipt.',
        'The invoice is linked with the **GRN** and the **Purchase Order** — the **three-way '
        'matching** of *item, quantity and rate*.',
        'Arithmetical accuracy, discount, GST rate & HSN, freight and other charges are checked; '
        'DPCO ceiling price verified for scheduled formulations.',
        'Deductions are computed: short/rejected quantity, breakage, **liquidated damages for late '
        'supply**, recovery of earlier advances, statutory deductions (TDS, etc.).',
        'The receiving officer **certifies** on the invoice: *"Goods received in good condition, '
        'quantity and quality verified, taken on stock vide GRN No. __ dated __, entered at page '
        '__ of the stock register."*',
        'The store officer **countersigns** and forwards the bill with GRN and inspection report '
        'to the accounts section.',
        'Accounts pre-audit the bill, pass it for payment, and issue the cheque/e-payment; entry '
        'made in the payment register.',
        '**Security deposit / performance guarantee** is released only after the warranty or '
        'contract period ends; EMD of unsuccessful bidders is refunded.',
    ])
    b.box('caution', 'AUDIT WILL OBJECT IF \u2026',
          bullets=['A bill is passed **without a GRN**, or the GRN quantity exceeds the PO quantity.',
                   'The **stock register page number** is not quoted on the bill (no proof that '
                   'the material was taken on charge).',
                   '**Liquidated damages** for late supply are not deducted, or waiver is granted '
                   'without sanction.',
                   'Payment is made for **short-supplied or rejected** quantity.',
                   'The **same GRN** is used to support two payments (double payment).',
                   'Short-expiry stock is accepted without written sanction and later expires unused.'])

    # ------------------------------------------------------------------ 3.12
    b.h2('3.12', 'Receipt of Special Categories of Items')
    b.table(['Category', 'Extra precautions at the goods inward stage'],
            [['**Narcotics & psychotropics (NDPS)**',
              'Received by a **named officer**; counted ampoule/tablet-wise in the presence of a '
              'witness; entered the **same day** in the NDPS/DDA register; stored at once in the '
              '**double-locked cupboard**; no quarantine outside the safe'],
             ['**Schedule X drugs**', 'Separate register and separate locked cupboard; quantity '
               'verified against the special licence/permit'],
             ['**Cold-chain items (vaccines, sera, insulin, blood products)**',
              'Check **VVM stage, cold-chain monitor card, data-logger**; shift to ILR/refrigerator '
              'within minutes; record receipt temperature; never leave on the dock'],
             ['**Blood and blood components**', 'Verified against blood-bank records; stored at '
              '**2\u20136 \u00B0C** (whole blood/PRBC), platelets at **20\u201324 \u00B0C with '
              'agitation**, FFP **below \u201330 \u00B0C**'],
             ['**Cytotoxic / anticancer drugs**', 'Check for leakage using intact outer packing; '
              'handle with gloves; keep spill kit ready; store separately with a '
              '**"CYTOTOXIC \u2014 HANDLE WITH CARE"** label'],
             ['**Radiopharmaceuticals**', 'Received by the authorised radiation-safety officer; '
              'survey meter check; lead-lined storage; entry in the radiation log-book (AERB '
              'requirements)'],
             ['**Inflammables (ether, spirit, acetone, LPG)**',
              'Unloaded away from the main building; "No smoking"; stored in the detached '
              'inflammable store; spirit entered in the **excise/bonded store register**'],
             ['**Compressed gas cylinders**', 'Verify **colour code**, valve condition, test date, '
              'cap in place; chain cylinders upright; never roll or drop'],
             ['**Glassware, IV fluids, ampoules**',
              'Open carefully; count broken units; claim on carrier; stack at low level'],
             ['**Equipment / capital items**', 'Check accessories, manuals, warranty card, serial '
              'number; installation and demonstration certificate; entry in the **dead-stock '
              '(non-consumable) register**'],
             ['**Free samples, donations, drugs received from other institutions**',
              'Entered in a **separate register**; checked for expiry and labelling; donated drugs '
              'must have adequate remaining shelf life'],
             ['**Bio-medical / hazardous chemicals**', 'MSDS obtained; segregated storage; PPE used']])

    # ------------------------------------------------------------------ 3.13
    b.h2('3.13', 'Precautions, Do\u2019s and Don\u2019ts in the Goods Inward Section')
    b.h3('Do\u2019s')
    b.bullets([
        'Always keep the **PO copy** ready before unloading; unload only what is covered by an order.',
        'Record damage **before** the carrier leaves and get his signature.',
        'Check **batch, mfg. and expiry dates of every item** — this is the pharmacist\u2019s '
        'personal responsibility.',
        'Shift **cold-chain items first**, other items later.',
        'Prepare the GRN **on the day of receipt**; delay is an audit objection.',
        'Use **serially numbered, bound** GRN books and registers.',
        'Segregate quarantine, approved and rejected stock physically.',
        'Retain packing material until checking is complete.',
        'File every document against its GRN number for instant retrieval.',
    ])
    b.h3('Don\u2019ts')
    b.bullets([
        'Do **not** sign "received in good condition" on the transporter\u2019s copy before counting.',
        'Do **not** take excess or unordered goods on charge.',
        'Do **not** mix a new batch with an existing batch in the same bin without separate batch '
        'identification.',
        'Do **not** issue any material lying in quarantine.',
        'Do **not** allow the supplier\u2019s representative to handle or count the stock unsupervised.',
        'Do **not** use pencil, whitener or erasers in any register.',
        'Do **not** keep narcotics even briefly outside the double-locked cupboard.',
    ])

    # ------------------------------------------------------------------ 3.14
    b.h2('3.14', 'Summary — Records of the Goods Inward Section')
    b.table(['Record', 'Nature', 'Purpose in one line'],
            [['Gate entry (inward) register', 'Chronological', 'Proof of arrival of the vehicle and '
              'number of packages'],
             ['Goods inward / daily receipt register', 'Chronological',
              'Date-wise diary of all consignments received'],
             ['**Goods Received Note (GRN)**', 'Transaction voucher',
              'Certifies quantity & condition received; authority to take on charge and to pay'],
             ['Inspection / test report file', 'Technical', 'Quality clearance of each batch'],
             ['Sample register', 'Technical', 'Record of samples drawn and sent for analysis'],
             ['Quarantine register', 'Control', 'What is under test, since when'],
             ['Discrepancy / shortage / damage report file', 'Claim',
              'Basis of claim on supplier, carrier, insurer'],
             ['Rejection memo & supplier-return register', 'Claim',
              'What was rejected and whether it went back'],
             ['Debit note / credit note file', 'Financial', 'Adjustment of the supplier\u2019s account'],
             ['Bill / invoice register', 'Financial', 'Receipt, passing and payment of bills'],
             ['Freight / transport & insurance claim file', 'Financial', 'Recovery of transit losses'],
             ['Supplier performance (vendor rating) register', 'MIS',
              'Delay, short supply and quality record of each firm'],
             ['Drug alert / NSQ / recall file', 'Statutory', 'Action taken on alerts and recalls'],
             ['Gate pass (returnable & non-returnable) book', 'Control',
              'Authority for material to leave the premises']])
    b.box('hy', 'ONE-LINE ANSWERS FROM THIS CHAPTER',
          bullets=['Document prepared **by the buyer** on receipt of goods \u2014 **GRN**.',
                   'Document that **travels with the goods** \u2014 **delivery challan**.',
                   'Document that **demands payment** \u2014 **invoice**.',
                   'Document required for a **transit claim** \u2014 **lorry receipt / consignment note**.',
                   'Area where goods await quality clearance \u2014 **quarantine (yellow label)**.',
                   'Matching of PO + GRN + Invoice \u2014 **three-way matching**.',
                   'Deduction for late supply \u2014 **liquidated damages**.',
                   'Minimum remaining shelf life usually demanded in drug tenders \u2014 '
                   '**5/6 of total shelf life**.'])
    b.page_break()



def chapter4(b):
    b.chapter(4, 'Records and Procedures in the Main Stores',
              'Functions of the main store \u2022 master list of registers \u2022 receipt, storage, '
              'issue, transfer & return \u2022 specimen formats \u2022 filing \u2022 verification')

    b.lead('The main store is the *central bank of materials*. Everything it receives must be '
           'accounted for, everything it issues must be authorised, and at any moment the physical '
           'stock on the shelf must equal the balance shown in its books. The records described '
           'here are simply the tools that make that equality provable.')

    # ------------------------------------------------------------------ 4.1
    b.h2('4.1', 'Main (Central) Store — Meaning and Functions')
    b.box('def', 'MAIN STORE',
          'The **main or central store** is the principal storage facility of the institution '
          'which **receives all approved material from the goods inward section, holds it in safe '
          'custody, maintains its complete accounts, and issues it to sub-stores, wards, '
          'departments and the dispensary against authorised indents**.')
    b.h3('4.1.1  Functions')
    b.numbered([
        '**Custody** — safe keeping of all drugs and supplies under proper storage conditions.',
        '**Accounting** — maintenance of quantitative (and where required, priced) records of '
        'receipt, issue and balance of every item, batch-wise.',
        '**Issue and distribution** — supply to sub-stores/wards on **FIFO/FEFO** basis against '
        'indents.',
        '**Stock control** — watching minimum, maximum, re-order and danger levels; initiating '
        'indents in time.',
        '**Preservation** — protection from heat, light, moisture, pests, fire, theft; cold-chain '
        'maintenance.',
        '**Codification and location control** — every item has a code and a fixed bin address.',
        '**Verification** — perpetual and annual physical verification, reconciliation of book '
        'balance with ground balance.',
        '**Expiry and quality surveillance** — near-expiry reporting, action on drug alerts and '
        'recalls.',
        '**Disposal** — segregation and condemnation of expired, damaged, obsolete and surplus stock.',
        '**Information** — consumption statements, stock position reports, expenditure statements '
        'for management, purchase and audit.',
    ])
    b.h3('4.1.2  Centralised vs decentralised stores')
    b.table(['Point', 'Centralised store', 'Decentralised (sub-)stores'],
            [['Investment in stock', 'Lower (pooled buffer)', 'Higher (buffer at every point)'],
             ['Control & records', 'Strong, uniform, single set of books', 'Weaker, duplicated records'],
             ['Bulk purchase economy', 'High \u2014 quantity discounts possible', 'Low'],
             ['Storage conditions & security', 'Easier to provide (cold room, vault)',
              'Difficult and costly to replicate'],
             ['Expiry / obsolescence loss', 'Lower \u2014 stock can be redistributed', 'Higher'],
             ['Speed of supply to user', 'Slower; needs transport & indenting',
              'Immediate at the point of use'],
             ['Handling & transport cost', 'Higher internal movement', 'Lower'],
             ['Best practice', 'Centralised main store for bulk custody **+** small imprest '
              'sub-stores for daily use', '']])

    # ------------------------------------------------------------------ 4.2
    b.h2('4.2', 'Broad Groups of Main-Store Records')
    b.flow(['Receipt records', 'Custody records', 'Issue records', 'Control records',
            'Financial records', 'Statutory records'])
    b.bullets([
        '**Receipt records** — GRN file, receipt register/day book, batch & expiry register.',
        '**Custody (holding) records** — **bin card**, **stock ledger / stock register**, '
        'bin-location index, kardex, temperature & humidity log.',
        '**Issue records** — indent file, issue voucher, issue register, daily consumption '
        'register, sub-store/ward ledger, gate pass book.',
        '**Control records** — re-order level statement, ABC/VED classification list, dues-in '
        'statement, stock verification sheet, near-expiry statement.',
        '**Financial records** — priced stores ledger, bill register, expenditure/budget control '
        'register, loss & write-off register.',
        '**Statutory records** — Schedule H/H1/X registers, NDPS register, prescription records, '
        'licences & renewals file, bio-medical waste records, DPCO price list.',
    ])

    # ------------------------------------------------------------------ 4.3
    b.h2('4.3', 'Master List of Registers and Records Maintained in the Main Store')
    b.table(['No.', 'Register / record', 'What it contains / why it is kept'],
            [['1', '**Stock register / stock ledger** (item-wise, page per item)',
              'The master account: opening balance, receipts, issues, closing balance of every '
              'item, with source document references'],
             ['2', '**Bin card (stock card)**', 'Card kept *at the bin*: quantity received, issued '
              'and balance only \u2014 posted by the store keeper at the time of each transaction'],
             ['3', '**Batch and expiry register**', 'Batch-wise quantity with date of expiry; basis '
              'of FEFO issue and near-expiry reporting'],
             ['4', 'Goods Received Note (GRN) file / receipt register',
              'All receipts with supplier, PO and inspection references'],
             ['5', '**Indent register**', 'Serial record of indents received from wards/departments '
              'and of indents raised on the purchase section'],
             ['6', '**Issue voucher / issue register**',
              'Every issue with date, indent no., indenting department, item, batch, quantity, '
              'receiver\u2019s signature'],
             ['7', 'Daily / monthly consumption register',
              'Consumption per item per period \u2014 the basis of all forecasting'],
             ['8', 'Sub-store & ward ledger (departmental account)',
              'What each ward/department has drawn; controls over-drawal'],
             ['9', '**Dead stock / non-consumable (permanent) register**',
              'Equipment, furniture, instruments \u2014 never "consumed", verified annually, '
              'written off only on condemnation'],
             ['10', 'Consumable (expendable) stores register', 'Drugs, dressings, chemicals, stationery'],
             ['11', '**Narcotic / NDPS (DDA) register**',
              'Drug-wise, date-wise receipt, issue and balance of narcotics & psychotropics; '
              'countersigned; kept under lock'],
             ['12', '**Schedule X register**', 'Purchase and sale/issue of Schedule X (habit-forming) drugs'],
             ['13', '**Schedule H / H1 register**',
              'Sale/issue records of prescription drugs; **H1 register** for the specified '
              'antibiotics, anti-TB and psychotropic drugs'],
             ['14', 'Prescription file / register', 'Prescriptions retained as required by the '
              'Drugs and Cosmetics Rules'],
             ['15', 'Spirit / alcohol (bonded store) register',
              'Excise-controlled receipt, issue and wastage of rectified spirit'],
             ['16', '**Expiry register / near-expiry statement**',
              'Items expiring in the next 3\u20136 months, for redistribution or return to supplier'],
             ['17', '**Breakage, damage and loss register**',
              'Every breakage/loss with cause, value, sanction of write-off'],
             ['18', '**Condemnation / disposal register**',
              'Items condemned, board proceedings, mode and date of disposal'],
             ['19', 'Stock verification register & discrepancy statement',
              'Date of verification, book balance, ground balance, shortage/excess, action taken'],
             ['20', '**Temperature and humidity record (log)**',
              'Twice-daily readings of store, refrigerator, ILR and deep freezer'],
             ['21', 'Refrigerator/ILR maintenance & breakdown register',
              'Defrosting, servicing, power failure, action taken'],
             ['22', 'Bin location index / location register',
              'Code number \u2192 rack/shelf/bin address, for instant retrieval'],
             ['23', 'Gate pass book (returnable & non-returnable)',
              'Authority for material to leave the premises'],
             ['24', 'Material Return Note (MRN) file',
              'Unused material returned by departments; rejected material returned to suppliers'],
             ['25', 'Transfer voucher file', 'Inter-store / inter-institutional transfers'],
             ['26', 'Priced stores ledger / valuation register',
              'Value of receipts, issues and closing stock for accounts'],
             ['27', 'Bill register & payment register', 'Bills received, passed and paid'],
             ['28', 'Budget control (allotment vs expenditure) register',
              'Head-wise funds, commitment and balance'],
             ['29', 'Licence and statutory documents file',
              'Drug licences, renewals, pharmacist registration, NDPS permits, AERB licence'],
             ['30', '**Drug alert / NSQ / recall register**',
              'Alerts received, batches held, action taken, report sent'],
             ['31', 'ADR (adverse drug reaction) & complaint file',
              'Quality complaints from wards, forwarded to the manufacturer/authority'],
             ['32', 'Bio-medical waste register (yellow category)',
              'Expired/discarded medicine and cytotoxic waste handed over, with dates & quantities'],
             ['33', 'Free supply / donation / sample register',
              'Drugs received free, from donations or as samples'],
             ['34', 'ABC / VED analysis file & re-order level statement',
              'Inventory control working papers'],
             ['35', 'Guard file of orders, circulars and SOPs',
              'Standing instructions, delegation of financial powers, price lists'],
             ['36', 'Visitor / inspection book',
              'Inspections by drug inspector, audit, accreditation team and their remarks']])
    b.box('exam', 'MOST ASKED PAIRS',
          bullets=['**Bin card** \u2014 kept *with the material*, shows **quantity only**, posted by '
                   'the **store keeper**, *at the time of each transaction*.',
                   '**Stock ledger** \u2014 kept *in the office*, may show **quantity and value**, '
                   'posted by the **ledger clerk / accounts**, from vouchers.',
                   '**Dead stock register** \u2014 for **non-consumable** items (equipment, '
                   'furniture); **consumable register** \u2014 for drugs and dressings.'])

    # ------------------------------------------------------------------ 4.4
    b.h2('4.4', 'Receipt Procedure in the Main Store')
    b.steps([
        'Accepted material is transferred from the goods inward section **with the GRN** (and the '
        'inspection/test report).',
        'The store keeper **re-counts** the quantity handed over and signs the GRN as having taken '
        'the goods on charge.',
        '**Bin/rack location** is allotted as per the code number; the item is placed with the '
        '**label facing outward**.',
        '**Bin card** is posted at once: date, GRN no., quantity received, new balance, batch and '
        'expiry.',
        '**Stock ledger** is posted by the ledger clerk from the GRN, quoting GRN number and date.',
        '**Batch & expiry register** is posted; the expiry date is also written on the bin card and '
        'on the carton in bold marker.',
        'For narcotics, Schedule X and spirit \u2014 entry in the **respective statutory register '
        'the same day** and immediate storage under double lock.',
        'Cold-chain items are placed in the ILR/refrigerator and the **temperature log** noted.',
        'Where the new receipt is of a **different batch**, it is stacked **behind** the existing '
        'stock so that the **earlier-expiring stock is issued first (FEFO)**.',
        'The GRN is filed; the purchase section is informed to close the dues-in entry.',
    ])
    b.box('hy', 'GOLDEN RULE',
          '**No material enters the store without a GRN, and no material leaves the store without '
          'an issue voucher.** Every figure in the stock ledger must be traceable to one of these '
          'two documents (or to a transfer voucher, MRN or write-off sanction).')

    # ------------------------------------------------------------------ 4.5
    b.h2('4.5', 'Storage Procedure in the Main Store')
    b.bullets([
        'Store **code-wise / group-wise** as per the classification adopted (see Chapters 5, 6 and 10).',
        'Observe the **storage condition on the label** — cold place, cool place, room temperature, '
        'protect from light/moisture.',
        'Follow **FIFO** (first-in-first-out) and more correctly **FEFO** (first-expiry-first-out).',
        'Keep stock **30 cm away from walls** and on **pallets ~10 cm above the floor**; never on '
        'the floor directly.',
        'Heavy and bulky items (IV fluids, cylinders) at **floor/lower shelf level**, light items above.',
        'Fast-moving items **near the issue counter**; slow-moving items at the far end.',
        'Keep **narcotics, Schedule X, spirit, inflammables, cytotoxics and radiopharmaceuticals '
        'in their designated secure areas**.',
        'Never store **look-alike / sound-alike (LASA)** drugs adjacent to each other; use LASA '
        'labels and separation.',
        'Record **temperature and humidity twice daily**; maintain the cold-chain log for every '
        'refrigerator and ILR.',
        'Keep the **expiry date visible**; mark near-expiry stock with a coloured sticker '
        '(traffic-light system).',
        'Maintain cleanliness, pest control and fire-safety equipment; keep aisles clear.',
    ])

    # ------------------------------------------------------------------ 4.6
    b.h2('4.6', 'Issue Procedure in the Main Store')
    b.steps([
        '**Receipt of indent** from the ward/department/sub-store on the prescribed form, signed by '
        'the **authorised indenting officer** within his delegated powers.',
        '**Scrutiny of the indent** — is the item stocked? is the quantity reasonable in relation '
        'to the previous issue and the patient load? is the indent within the imprest scale? is '
        'stock available?',
        '**Entry in the indent register** with a serial number and date.',
        '**Approval / sanction** by the store officer; quantity may be reduced (\u201Ccut\u201D) '
        'and the reason recorded.',
        '**Preparation of the issue voucher** (issue slip / material issue note) showing item, '
        'code, batch, expiry, quantity issued and balance.',
        '**Physical picking of stock on FEFO basis** \u2014 the batch expiring earliest is issued '
        'first; batch and expiry are written on the voucher.',
        '**Handing over** to the authorised messenger/representative, who **signs the issue '
        'voucher/register in token of receipt**.',
        '**Posting of records**: bin card (quantity issued and new balance), stock ledger, batch & '
        'expiry register, departmental/ward ledger, daily consumption register; narcotics also in '
        'the NDPS register.',
        '**Closing balance checked** against the bin card; if the balance has fallen to the '
        '**re-order level**, an indent is initiated on the purchase section.',
        '**Filing** of the indent and issue voucher; preparation of the monthly consumption and '
        'expenditure statement.',
    ])
    b.flow(['Indent received', 'Scrutiny & sanction', 'Issue voucher', 'FEFO picking',
            'Receiver signs', 'Bin card + Ledger', 'Consumption register'])
    b.h3('4.6.1  Specimen format — Issue Voucher / Material Issue Note')
    b.table(['Sl.', 'Code No.', 'Item & specification', 'Unit', 'Qty indented', 'Qty issued',
             'Batch No.', 'Expiry', 'Ledger folio', 'Remarks'],
            [['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '']],
            size=8, first_col_bold=False, min_cm=1.0,
            caption='Format 4.1  Issue voucher (header: voucher no. & date, indent no. & date, '
                    'indenting department; footer: signatures of store keeper, receiver and '
                    'store officer)')
    b.box('caution', 'ISSUE DISCIPLINE',
          bullets=['Never issue against a **verbal order**; if unavoidable in an emergency, it must '
                   'be **regularised in writing the same day**.',
                   'Never issue to a person who is **not authorised**; obtain signature with name '
                   'and designation.',
                   'Never issue **expired, near-expiry (without a plan of use), quarantined or '
                   'recalled** stock.',
                   'Never issue **without posting the records** \u2014 unposted issues are the '
                   'commonest cause of shortage at verification.'])

    # ------------------------------------------------------------------ 4.7
    b.h2('4.7', 'Transfers, Returns and the Imprest (Top-up) System')
    b.kv([
        ('Transfer voucher', 'Used when stock moves from one store/institution to another; the '
                             'transferring store shows it as an **issue**, the receiving store as '
                             'a **receipt**, both quoting the same voucher number.'),
        ('Material Return Note (MRN)', 'Unused or excess material returned by a ward to the main '
                                       'store; it is taken back on charge with a receipt entry, '
                                       'and the ward ledger is credited.'),
        ('Return to supplier', 'Rejected, damaged, expired or recalled stock returned under an '
                               '**MRN + non-returnable gate pass + debit note**; the reduction is '
                               'posted in the stock records.'),
        ('Imprest system', 'A ward/department is allotted a **fixed scale (imprest) of each item**. '
                           'It periodically indents **only the quantity consumed**, so that the '
                           'stock is topped up back to the imprest level. Also called the '
                           '**top-up or replenishment system**.'),
        ('Advantages of imprest', 'Ward never runs dry; indenting is simple (consumption = indent); '
                                  'over-stocking at ward level is prevented; audit is easy because '
                                  'the closing stock should always equal the imprest scale.'),
        ('Floor/ward stock check', 'The pharmacist inspects ward stock periodically for expiry, '
                                   'storage condition, unauthorised accumulation and correctness '
                                   'of the ward register.'),
    ])

    # ------------------------------------------------------------------ 4.8
    b.h2('4.8', 'Handling of Expiry, Breakage, Loss and Condemnation')
    b.h3('4.8.1  Expiry management')
    b.numbered([
        'A **near-expiry statement** is generated **monthly**, listing stock expiring within the '
        'next 3\u20136 months.',
        'Colour-coded stickers (**traffic-light system**) are pasted: e.g. *red* = expires within '
        '3 months, *yellow* = 3\u20136 months, *green* = more than 6 months.',
        'Near-expiry stock is **redistributed** to high-consumption wards/institutions or '
        '**returned to the supplier** if the purchase order has a buy-back/replacement clause.',
        'On expiry the stock is **immediately removed from the shelf**, entered in the '
        '**expiry register**, stored in the **separate locked expired-drug area** with a red label, '
        'and its quantity written off from the stock register after sanction.',
        'Disposal is done as **bio-medical waste (yellow category)** through the authorised common '
        'facility, or returned to the manufacturer, and the certificate of destruction is filed.',
        'The **value of expiry loss** is reported to management and analysed (wrong forecasting, '
        'over-indenting, prescriber change, short-expiry acceptance).',
    ])
    b.h3('4.8.2  Breakage, pilferage and loss')
    b.bullets([
        'Every breakage/loss is recorded **immediately** in the **Breakage and Loss Register** with '
        'item, batch, quantity, value, date, cause and name of the person responsible.',
        'Losses are classified as **normal/unavoidable** (handling breakage, evaporation, '
        'leakage \u2014 within permissible limits) or **abnormal/avoidable** (negligence, theft).',
        'Write-off requires **sanction of the competent authority**; abnormal losses may involve '
        '**recovery from the person at fault** and disciplinary/criminal action.',
        'Loss of **narcotics** must be reported to the authority prescribed under the NDPS Rules '
        'without delay.',
        'After sanction, the quantity is deducted from the stock register quoting the sanction '
        'number \u2014 *never* quietly adjusted.',
    ])
    b.h3('4.8.3  Condemnation and disposal of unserviceable stores')
    b.steps([
        'Items that are **expired, damaged beyond use, obsolete, surplus or beyond economical '
        'repair** are listed by the store keeper.',
        'A **Condemnation Board / Survey Committee** (usually 3 members, including a technical '
        'officer and an officer not connected with the store) inspects and certifies them.',
        'The board records the **reason, residual value and recommended mode of disposal**.',
        'Sanction of the **competent authority** is obtained as per delegated financial powers.',
        'Disposal is by **auction/sale of scrap, transfer, return to supplier, or destruction** '
        '(incineration/deep burial for drugs, as per the Bio-Medical Waste Rules).',
        'The **Condemnation Register** is completed, the stock register credited/deducted, sale '
        'proceeds deposited, and the destruction certificate filed.',
    ])

    # ------------------------------------------------------------------ 4.9
    b.h2('4.9', 'Stock Verification in the Main Store')
    b.table(['Type', 'How it is done', 'Remarks'],
            [['**Perpetual / continuous verification**',
              'A few items verified every day by rotation, so that every item is covered at least '
              'once (high-value items more often) during the year',
              'Best method; no closure of the store; errors detected early; suits ABC-based '
              'frequency (A items monthly, B quarterly, C annually)'],
             ['**Periodic / annual (physical) stock taking**',
              'The whole stock counted on a fixed date, usually at the close of the financial year; '
              'store may be closed for issues',
              'Statutory/accounting requirement; heavy work load; disrupts supply'],
             ['**Spot / surprise verification**', 'Sudden check of selected items by a superior '
              'officer or a flying squad',
              'Deterrent against pilferage; compulsory for narcotics and high-value items'],
             ['**Verification by an independent verifier / audit party**',
              'External stock verifier not connected with custody',
              'Satisfies the principle of internal check']])
    b.h3('4.9.1  Procedure and treatment of discrepancies')
    b.numbered([
        'The verifier counts the **ground (physical) balance** and records it on the verification '
        'sheet **before** looking at the book balance (blind counting is the ideal).',
        'The **book balance** is then taken from the bin card and stock ledger and the two compared.',
        'Differences are listed in the **shortage/excess (discrepancy) statement**.',
        'Obvious causes are investigated first: unposted vouchers, wrong unit of measurement, '
        'issue not recorded, receipt posted twice, transfer not accounted, breakage not written off.',
        'Genuine **shortages** are regularised by write-off sanction, or recovered from the '
        'custodian if negligence is established; **excesses** are taken on charge to prevent their '
        'misuse.',
        'The custodian and the verifier both **sign the verification certificate**, and a note of '
        'verification with date is made in the stock register.',
        'A report is placed before management; repeated discrepancies attract change of custodian '
        'or a special audit.',
    ])
    b.box('formula', 'BASIC STOCK EQUATION',
          '**Closing balance = Opening balance + Receipts \u2212 Issues \u2212 Losses/Write-offs + '
          'Returns**.\nIf the physical count does not satisfy this equation, either a voucher is '
          'unposted or stock is missing. This equation is the logic of every stock register page.')

    # ------------------------------------------------------------------ 4.10
    b.h2('4.10', 'Filing, Indexing and Documentation Systems')
    b.table(['System of filing', 'Basis of arrangement', 'Typical use in a store'],
            [['Alphabetical', 'By name of item or supplier', 'Supplier files, drug information files'],
             ['Numerical', 'By serial number of the document', 'GRN files, issue voucher bundles, '
              'PO files'],
             ['**Code / classification-wise (decimal)**', 'By store code number of the item',
              'Stock ledger folios, bin index'],
             ['Chronological (date-wise)', 'By date', 'Daily receipt register, gate passes'],
             ['Subject-wise', 'By topic', 'Circulars, licences, audit paras'],
             ['Geographical', 'By place/institution', 'Sub-store and peripheral institution files'],
             ['Vertical / horizontal / lateral filing', 'Physical method of keeping files',
              'Filing cabinets, box files, guard files'],
             ['Electronic / digital', 'Scanned and indexed soft copies',
              'Back-up of GRNs, invoices, test reports']])
    b.bullets([
        'Each file has a **file number, subject and index of contents**; pages are serially numbered.',
        'A **guard file** keeps original standing orders, circulars and delegation of powers for '
        'ready reference.',
        'Registers are **bound with machine-numbered pages**, and the first page carries a '
        '**certificate of the number of pages** signed by the officer-in-charge.',
        'A **movement/transit register** is kept for files and registers taken out of the store.',
        '**Hand-over / take-over (charge) certificate** is prepared whenever the custodian changes, '
        'listing verified balances of all items and all registers handed over.',
    ])

    # ------------------------------------------------------------------ 4.11
    b.h2('4.11', 'Security, Confidentiality and Computerisation of Records')
    b.bullets([
        'Registers kept under **lock in a fire-resistant almirah**; narcotic and Schedule X '
        'registers in the personal custody of a named officer.',
        'Access restricted on a **need-to-know basis**; no register leaves the store without entry '
        'in the movement register.',
        'Patient-identifiable data in prescription/Schedule H1 registers is **confidential**.',
        'In computerised stores: **individual user IDs and passwords, role-based rights, no shared '
        'logins, automatic audit trail** of every entry and modification, daily **back-up** kept '
        'off-site, and **periodic printing and binding** of statutory registers where law requires '
        'a physical record.',
        'The **manual register is still legally required** for narcotics and certain statutory '
        'records unless the rules expressly permit electronic records.',
    ])

    # ------------------------------------------------------------------ 4.12
    b.h2('4.12', 'Common Errors and Audit Objections in Store Records')
    b.table(['Error / objection', 'Correct practice'],
            [['Entries made in pencil, or erased/whitened',
              'Ink only; single-line scoring with attestation'],
             ['Loose sheets used as stock register', 'Bound, page-numbered register with page '
              'certificate'],
             ['Bin card balance \u2260 ledger balance', 'Post both at the time of the transaction; '
              'reconcile weekly'],
             ['Issues made without vouchers / verbal issues',
              'Written indent and signed issue voucher for every issue'],
             ['Batch and expiry not recorded', 'Batch-wise posting; expiry register maintained'],
             ['Expired stock lying on the shelf with live stock',
              'Immediate segregation in a locked, labelled area'],
             ['Goods taken on charge without a GRN / without inspection',
              'GRN + inspection report compulsory'],
             ['Bill paid for short-supplied quantity; LD not deducted',
              'Three-way matching and penalty computation'],
             ['Dues-in not deducted while indenting \u2192 double ordering',
              'Maintain and consult the pending-order register'],
             ['Physical verification not done / no verification certificate',
              'Perpetual verification plus annual stock taking with certificate'],
             ['Narcotic register not countersigned, balance not tallied daily',
              'Daily tally and countersignature by the designated officer'],
             ['Condemned items lying for years without disposal',
              'Timely board, sanction and disposal'],
             ['Sub-store stock not accounted after issue from main store',
              'Ward ledgers and periodic ward stock checks'],
             ['Free/donated drugs not recorded', 'Separate register; taken on charge like purchases']])
    b.box('hy', 'CHAPTER SUMMARY IN FIVE LINES',
          bullets=['Main store = custody + accounting + issue + control of all materials.',
                   'Receipt is authorised by the **GRN**; issue is authorised by the '
                   '**indent + issue voucher**.',
                   'Quantity records = **bin card (at the bin)** and **stock ledger (in the office)**.',
                   'Issue is always on **FEFO/FIFO**; batch and expiry are recorded at every step.',
                   'Book balance must equal ground balance \u2014 proved by **perpetual + annual '
                   'verification**.'])
    b.page_break()
