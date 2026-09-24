# -*- coding: utf-8 -*-
"""Part VII — Chapter 11 (statutory records) & Chapter 12 (computerisation)"""


def chapter11(b):
    b.part('PART VII', 'Statutory Records & Modern Systems')
    b.chapter(11, 'Statutory and Legal Records of a Drug Store',
              'Drugs & Cosmetics Rules \u2022 Schedules H, H1 & X \u2022 NDPS records \u2022 '
              'licence forms \u2022 retention periods \u2022 inspection by the Drug Inspector')

    b.lead('Managerial records can be simplified; statutory records cannot. They must exist in the '
           'prescribed form, contain the prescribed particulars, be preserved for the prescribed '
           'period, and be produced to the inspector on demand. This chapter collects them in one '
           'place \u2014 it is the densest source of one-mark questions in the whole topic.')

    # ------------------------------------------------------------------ 11.1
    b.h2('11.1', 'Records under the Drugs and Cosmetics Act, 1940 and Rules, 1945')
    b.table(['Requirement', 'Substance of the provision'],
            [['**Licence to stock and sell**', 'A drug store must hold a valid licence; it must be '
              '**displayed** on the premises, and renewed in time'],
             ['**Qualified person**', 'Sale/dispensing of drugs must be **under the personal '
              'supervision of a registered pharmacist** (retail) or a competent person (wholesale); '
              'registration certificate kept on record'],
             ['**Premises & storage**', 'Adequate space, proper storage including **refrigeration '
              'where required**; storage conditions as per the label and **Schedule P**'],
             ['**Records of purchase**', 'Purchase bills/invoices showing the name of the '
              'manufacturer, batch number and quantity, preserved and available for inspection'],
             ['**Records of sale**', 'Cash/credit memo (bill) for every sale showing the name & '
              'address of the seller, licence number, date, name of the drug, quantity, batch '
              'number and price; counterfoils preserved'],
             ['**Prescription records**', 'Sales of **Schedule H, H1 and X** drugs only against a '
              'prescription; the prescription/register entry preserved for the prescribed period'],
             ['**No sale of expired drugs**', 'Stocking or selling a drug after its expiry date is '
              'an offence; expired stock must be segregated'],
             ['**Inspection book / records available**',
              'All registers, bills and records must be produced to a **Drugs Inspector** on demand'],
             ['**Price display**', 'Price list of scheduled formulations displayed as required '
              'under the DPCO']])
    b.h3('11.1.1  Principal licence forms (frequently asked)')
    b.table(['Form', 'Purpose'],
            [['**Form 19**', 'Application for a licence to **sell, stock, exhibit or distribute** '
              'drugs (retail/wholesale)'],
             ['**Form 19A**', 'Application for a **restricted** licence (sale by a dealer without a '
              'qualified person)'],
             ['**Form 19C**', 'Application for a licence to sell drugs specified in **Schedule X**'],
             ['**Form 20**', 'Licence for **retail sale** of drugs other than those in Schedules C, '
              'C(1) and X'],
             ['**Form 20A**', '**Restricted** licence for retail sale'],
             ['**Form 20B**', 'Licence for **wholesale** of drugs other than those in Schedules C, '
              'C(1) and X'],
             ['**Form 21**', 'Licence for **retail sale of drugs specified in Schedule C and C(1)** '
              '(other than Schedule X)'],
             ['**Form 21A**', 'Restricted licence for retail sale of Schedule C/C(1) drugs'],
             ['**Form 21B**', 'Licence for **wholesale of Schedule C and C(1)** drugs'],
             ['**Form 20F**', '**Licence to sell Schedule X drugs by retail**'],
             ['**Form 20G**', '**Licence to sell Schedule X drugs wholesale**'],
             ['**Form 25 / 28**', 'Licence to **manufacture** drugs (28 = Schedule C & C(1) '
              'biological/special products)'],
             ['**Form 25A / 28A**', '**Loan licence** to manufacture'],
             ['**Form 29**', 'Licence to manufacture drugs for **examination, test or analysis**'],
             ['**Form 13**', 'Report of the **Government Analyst** on a sample'],
             ['**Form 16**', '**Receipt** given by the Inspector for a **sample** taken'],
             ['**Form 17**', '**Intimation** to the person from whom a sample has been taken that it '
              'is being sent for test/analysis'],
             ['**Form 18**', 'Order of the Inspector **prohibiting the sale/disposal of stock** '
              '(stock "frozen")']])
    b.box('hy', 'SCHEDULE X TRIAD',
          '**Application in Form 19C \u2192 Retail licence in Form 20F \u2192 Wholesale licence in '
          'Form 20G.** Schedule X drugs are kept in a **separate locked cupboard**, the prescription '
          'is required **in duplicate** (one copy retained by the pharmacy), and the records are '
          'preserved for **2 years**.')

    # ------------------------------------------------------------------ 11.2
    b.h2('11.2', 'Schedule H, H1 and X — Record Requirements Compared')
    b.table(['Point', '**Schedule H**', '**Schedule H1**', '**Schedule X**'],
            [['What it covers', 'General prescription-only drugs (most antibiotics, '
              'cardiovascular, hormonal, etc.)',
              'Specified higher-generation antibiotics, anti-TB drugs and certain '
              'sedatives/psychotropics',
              'Habit-forming / narcotic-type drugs such as barbiturates and amphetamines'],
             ['Label marking', '**"Rx"** + the Schedule H warning',
              '**"Rx"** + H1 warning inside a box with a **red vertical line on the left border**',
              '**"NRx"** (in red) + the Schedule X warning'],
             ['Sale only on prescription of', 'Registered medical practitioner',
              'Registered medical practitioner', 'Registered medical practitioner'],
             ['Separate register', 'Not separately prescribed (prescription record kept)',
              '**Yes \u2014 a separate H1 register** showing the name & address of the prescriber, '
              'the name of the patient, the name of the drug and the quantity supplied, with the '
              'date',
              '**Yes \u2014 a separate Schedule X register**'],
             ['Prescription handling', 'Retained/recorded as prescribed',
              'Recorded in the H1 register',
              'Prescription **in duplicate**; one copy retained by the seller'],
             ['Storage', 'With general stock',
              'With general stock (register controlled)',
              '**Separate cupboard under lock and key**'],
             ['Special licence', 'Normal Form 20/20B',
              'Normal Form 20/20B', '**Form 20F (retail) / 20G (wholesale)**'],
             ['Preservation of records', '**2 years**', '**3 years**', '**2 years**']])

    # ------------------------------------------------------------------ 11.3
    b.h2('11.3', 'Records under the NDPS Act, 1985')
    b.bullets([
        'Narcotic drugs and psychotropic substances may be possessed, stored and used only under '
        'the **licence/permit/authorisation** prescribed by the NDPS Rules (and the State Rules).',
        'A **separate, bound narcotic register (Dangerous Drug register)** is maintained with a '
        '**separate page for each drug and each strength**, showing date, quantity received (with '
        'source and voucher), quantity issued (with the name of the patient/ward and the prescriber), '
        'and the **running balance**.',
        'Entries are made **immediately, in ink, by the responsible person**; corrections are '
        '**attested**; no page may be removed.',
        'The **balance must be physically verified regularly** (daily/at each shift change in a '
        'hospital ward) and the register **countersigned** by the designated officer.',
        'Stock is kept in a **double-locked, fixed steel cupboard/safe**, the keys remaining in the '
        'personal custody of the authorised person.',
        '**Loss, theft or discrepancy must be reported at once** to the prescribed authority and to '
        'the police as required.',
        '**Destruction** of expired/unusable narcotics is done only **before/by the officer '
        'authorised** under the Rules, and a **certificate of destruction** is preserved.',
        'Records and registers must be preserved for the period prescribed by the Rules '
        '(commonly **2 years**) and produced for inspection on demand.',
        'Prescribing of narcotics in hospitals is regulated (e.g. **Recognised Medical Institution '
        '(RMI)** provisions for morphine for palliative care), each state prescribing its own '
        'formats.',
    ])
    b.box('caution', 'ZERO TOLERANCE',
          'An unexplained shortage of a narcotic drug is not merely an audit objection \u2014 it is '
          'a **criminal matter** under the NDPS Act, which carries stringent penalties and where '
          'the burden of explanation lies on the custodian. This is why the narcotic register is '
          'the most rigorously examined record in any drug store.')

    # ------------------------------------------------------------------ 11.4
    b.h2('11.4', 'Other Statutory Records Relevant to a Drug Store')
    b.table(['Law / rule', 'Record to be maintained'],
            [['**Pharmacy Act, 1948**', 'Registration certificate of the pharmacist (and its '
              'renewal); record of the pharmacist on duty'],
             ['**Drugs (Prices Control) Order / NPPA**',
              'Price list of scheduled formulations, purchase and sale records proving compliance '
              'with the ceiling price'],
             ['**Bio-Medical Waste Management Rules, 2016**',
              'Daily record of waste generated category-wise (yellow/red/white/blue), handing-over '
              'record to the common facility, **annual report**, training and accident records'],
             ['**Schedule M (GMP)** \u2014 manufacturers',
              'Master formula records, **batch manufacturing and packaging records**, raw-material '
              'and finished-product analytical records, distribution records (for recall), '
              'validation, calibration and training records; **records generally retained for one '
              'year beyond the expiry date of the batch**'],
             ['**Blood bank (Schedule F Part XII-B)**',
              'Donor records, testing records, issue records, **preserved for the prescribed period '
              '(commonly 5 years)**'],
             ['**Legal Metrology / Packaged Commodities Rules**',
              'Verified/stamped weighing and measuring instruments with calibration certificates'],
             ['**GST law**', 'Tax invoices, purchase and sale registers, e-way bills; books of '
              'account preserved for the statutory period (**72 months / 6 years**)'],
             ['**Income-tax & financial rules / GFR**',
              'Vouchers, cash book, stock registers, physical verification certificates, '
              'condemnation records'],
             ['**AERB (radiation)**', 'Licence, radiation survey log, personnel dosimetry (TLD) '
              'records, source inventory'],
             ['**Factories Act / Explosives & Petroleum Rules**',
              'Licence and register for storage of inflammables and compressed gases'],
             ['**Excise rules (rectified spirit)**',
              'Bonded store register, permits, wastage statements'],
             ['**NABH / accreditation standards (voluntary)**',
              'SOPs, temperature logs, LASA & high-alert drug lists, emergency-trolley checklists, '
              'expiry-check records, staff training records']])

    # ------------------------------------------------------------------ 11.5
    b.h2('11.5', 'Retention (Preservation) Periods of Records')
    b.table(['Record', 'Usual retention period', 'Governed by'],
            [['**Prescription / records of sale of Schedule H and C(1) drugs**', '**2 years**',
              'Drugs & Cosmetics Rules'],
             ['**Schedule H1 register**', '**3 years**', 'Drugs & Cosmetics Rules'],
             ['**Schedule X records, registers and prescriptions**', '**2 years**',
              'Drugs & Cosmetics Rules'],
             ['**Narcotic / psychotropic registers and vouchers**',
              '**2 years** (or as the State NDPS Rules prescribe)', 'NDPS Rules'],
             ['**Purchase bills / invoices and sale bills (cash & credit memo counterfoils)**',
              'Commonly **2\u20133 years** for drug-law purposes, but **6 years (72 months)** under '
              'GST law \u2014 so keep for the longer period',
              'Drugs & Cosmetics Rules + GST law'],
             ['**Batch manufacturing & analytical records (manufacturers)**',
              '**One year beyond the expiry date** of the batch (Schedule M); some records longer',
              'Schedule M / GMP'],
             ['**Blood bank records**', 'Commonly **5 years**', 'Drugs & Cosmetics Rules, Sch. F'],
             ['**Stock registers of consumables, GRNs, issue vouchers, indents**',
              'Generally **5 years (or until audit is completed)**',
              'GFR / State store & financial rules'],
             ['**Dead stock (non-consumable) register**',
              '**Permanent** \u2014 until the item is condemned and written off',
              'GFR / State rules'],
             ['**Condemnation, write-off and auction records**', 'Commonly **5\u201310 years**',
              'Financial rules'],
             ['**Bio-medical waste records & annual returns**',
              'Commonly **5 years**', 'BMW Rules, 2016'],
             ['**Temperature / cold-chain logs**',
              'Commonly **2\u20133 years** (accreditation bodies often ask for the current + '
              'previous year)', 'Institutional SOP / accreditation'],
             ['**Licences, agreements, court and audit files**',
              '**Permanent / till finally settled**', 'Institutional rules']])
    b.box('note', 'HOW TO ANSWER A RETENTION QUESTION',
          'Quote the **statutory** periods with confidence \u2014 *Schedule H/X = 2 years, '
          'Schedule H1 = 3 years* \u2014 and remember that where two laws prescribe different '
          'periods (drug law vs tax law), the record must be kept for the **longer** period. '
          'Departmental/financial periods vary from State to State and are prescribed by the local '
          'financial code or record-retention schedule.')

    # ------------------------------------------------------------------ 11.6
    b.h2('11.6', 'Inspection by the Drugs Inspector — What is Examined')
    b.numbered([
        '**Licence** — valid, displayed, covers the categories actually stocked (including '
        'Schedule C/C(1) and X).',
        '**Registered pharmacist** present and his registration current.',
        '**Premises** — area, cleanliness, refrigeration, storage as per the label/Schedule P.',
        '**Stock** — presence of expired, unlabelled, spurious, misbranded, physician-sample or '
        '"not for sale" drugs; recalled batches.',
        '**Purchase records** — bills showing manufacturer, batch and quantity; ability to trace '
        'the source of any drug on the shelf.',
        '**Sale records** — cash/credit memos, prescription records, **Schedule H1 register**, '
        '**Schedule X register**.',
        '**Narcotic register** and the double-locked cupboard; balance tallied physically.',
        '**Cold-chain records** — refrigerator temperature log, functioning thermometer.',
        '**Price compliance** — DPCO ceiling prices, price list displayed.',
        '**Samples** — the Inspector may take a sample, give a **receipt in Form 16**, send it for '
        'test with **intimation in Form 17**, and may **prohibit sale of the stock by an order in '
        'Form 18**; the Government Analyst reports in **Form 13**.',
        '**Records of bio-medical waste** disposal of expired medicines.',
        'Remarks are recorded in the **inspection book**, and compliance must be reported within '
        'the time allowed.',
    ])
    b.box('hy', 'PENALTY PERSPECTIVE',
          'Contravention of the conditions of a licence (including **failure to maintain the '
          'prescribed records**) can lead to **suspension or cancellation of the licence**, apart '
          'from prosecution. Sale of a **spurious or adulterated** drug attracts the most severe '
          'penalties under the Drugs and Cosmetics Act. Offences relating to narcotics are dealt '
          'with under the **NDPS Act**, which is far stricter.')
    b.page_break()


def chapter12(b):
    b.chapter(12, 'Computerisation, Bar Coding and Modern Store Management',
              'Manual vs computerised records \u2022 software modules \u2022 e-procurement '
              '\u2022 data integrity \u2022 advantages and limitations')

    b.lead('Every state health service is now moving to computerised drug distribution '
           '(DVDMS, e-Aushadhi and similar systems). Questions increasingly ask what a store '
           'software does, and what safeguards an electronic record needs.')

    # ------------------------------------------------------------------ 12.1
    b.h2('12.1', 'Why Computerise Store Records?')
    b.table(['Problem of the manual system', 'How computerisation solves it'],
            [['Slow, repetitive writing; posting backlog',
              'One entry updates the ledger, bin balance, batch record and consumption data '
              'simultaneously'],
             ['Arithmetical and posting errors', 'Balances computed automatically; bar-code capture '
              'removes transcription error'],
             ['Expiry loss', '**Automatic near-expiry alerts** and **FEFO-based batch prompting** at '
              'the time of issue'],
             ['Stock-outs', 'Automatic **re-order level alerts** and draft indent generation'],
             ['Difficulty of analysis', 'ABC/VED analysis, consumption trends, expiry-loss and '
              'supplier-performance reports at a keystroke'],
             ['Recall of a defective batch', 'Instant list of where every unit of a batch went'],
             ['Duplicate ordering', 'Dues-in automatically deducted from the requirement'],
             ['Weak accountability', '**Audit trail** records who made or altered every entry, and when']])

    # ------------------------------------------------------------------ 12.2
    b.h2('12.2', 'Typical Modules of Drug Store / Pharmacy Software')
    b.bullets([
        '**Item master (stores vocabulary)** — code, description, unit, storage condition, '
        'min/max/re-order level, ABC-VED class.',
        '**Indent & purchase module** — indent generation, approval workflow, tender/rate-contract '
        'data, purchase order printing, dues-in tracking.',
        '**Goods receipt module** — GRN entry with batch, expiry, rate; inspection status; '
        'quarantine flag; discrepancy record.',
        '**Inventory module** — batch-wise stock, bin location, expiry alerts, stock transfer, '
        'physical verification sheets.',
        '**Issue / distribution module** — ward & patient-wise issue, FEFO prompt, imprest top-up.',
        '**Narcotic & Schedule X module** — restricted access, mandatory balance tally, printable '
        'statutory register.',
        '**Financial module** — priced ledger, bill passing, budget control, expenditure statements.',
        '**MIS & analytics** — consumption trend, turnover ratio, stock-out and expiry reports, '
        'vendor rating.',
        '**Bar-code / scanner interface** and, in advanced systems, **RFID and temperature-logger '
        'integration**.',
        '**Integration with the HMIS** — prescription \u2192 dispensing \u2192 billing \u2192 stock '
        'deduction in one flow.',
    ])
    b.h3('12.2.1  Public-sector systems worth knowing by name')
    b.table(['System', 'What it is'],
            [['**DVDMS** (Drugs & Vaccines Distribution Management System)',
              'National/state platform for demand, procurement, warehousing and distribution of '
              'drugs and vaccines'],
             ['**e-Aushadhi**', 'State-level drug inventory and distribution software used by '
              'several state medical services corporations'],
             ['**GeM** (Government e-Marketplace)', 'Online public procurement portal '
              '(e-bidding, reverse auction)'],
             ['**e-Tendering / CPP Portal**', 'Electronic publication and submission of tenders'],
             ['**Jan Aushadhi / PMBJP**', 'Generic medicine supply scheme with its own stock and '
              'sale software'],
             ['**eVIN** (Electronic Vaccine Intelligence Network)',
              'Real-time vaccine stock and cold-chain temperature monitoring on a mobile platform']])

    # ------------------------------------------------------------------ 12.3
    b.h2('12.3', 'Safeguards for Electronic Records')
    b.table(['Safeguard', 'Requirement'],
            [['**Individual user accounts**', 'Unique user ID and password for every user; '
              '**no shared logins**; periodic password change'],
             ['**Role-based access rights**', 'Only the authorised role can create a code, approve '
              'an indent, or post a write-off'],
             ['**Audit trail**', 'Automatic, non-editable log of every entry, change and deletion '
              'with user and time stamp'],
             ['**No deletion of transactions**', 'Corrections made only by a reversal entry, with '
              'a reason recorded'],
             ['**Back-up**', 'Daily back-up, stored **off-site**, with periodic restoration testing'],
             ['**Business continuity**', 'UPS/generator; a manual fallback register for use during '
              'downtime, posted into the system afterwards'],
             ['**Validation & calibration**', 'The software is validated; bar-code scanners, '
              'printers and temperature loggers calibrated'],
             ['**Printing & preservation of statutory registers**',
              'Where the law requires a physical record (e.g. narcotics), print, bind, sign and '
              'preserve it'],
             ['**Data privacy**', 'Patient-identifiable data (Schedule H1, prescriptions) protected '
              'and accessed on a need-to-know basis']])
    b.box('note', 'DATA INTEGRITY \u2014 ALCOA+',
          '**A**ttributable \u2022 **L**egible \u2022 **C**ontemporaneous \u2022 **O**riginal '
          '\u2022 **A**ccurate \u2014 plus **C**omplete, **C**onsistent, **E**nduring, '
          '**A**vailable. Applies equally to paper and to electronic records; increasingly asked '
          'in pharmacy examinations.')

    # ------------------------------------------------------------------ 12.4
    b.h2('12.4', 'Limitations and Precautions')
    b.bullets([
        '**Capital cost** of hardware, software, scanners and networking; recurring cost of '
        'maintenance and licences.',
        '**Training and resistance to change** among staff; a half-trained user creates worse data '
        'than a careful clerk.',
        '**Garbage-in, garbage-out** — if the opening balances, codes and batch data are entered '
        'wrongly, every report is wrong.',
        '**Dependence on power and network**; failure halts issue unless a manual fallback exists.',
        '**Data loss/corruption and cyber-security** risks; hence back-up, antivirus and access '
        'control.',
        '**Legal acceptability** — statutory registers may still be required in physical form; '
        'electronic records must satisfy audit-trail requirements.',
        '**Physical verification is still compulsory** — a computer shows the book balance, never '
        'the ground balance.',
    ])
    b.box('hy', 'REMEMBER',
          'Computerisation improves **speed, accuracy and information** \u2014 it does **not** '
          'replace the pharmacist\u2019s duties of **physical verification, storage-condition '
          'monitoring, expiry checking and statutory record keeping**.')
    b.page_break()
