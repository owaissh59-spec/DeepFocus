# -*- coding: utf-8 -*-
"""Part VIII — Chapter 13 (revision capsule) & Chapter 14 (glossary)"""


def chapter13(b):
    b.part('PART VIII', 'Revision')
    b.chapter(13, 'Quick Revision Capsule',
              'Everything examinable from Chapters 1\u201312, compressed \u2014 read this the '
              'night before the examination')

    # ------------------------------------------------------------------ 13.1
    b.h2('13.1', 'One-Line Definitions')
    b.table(['Term', 'Definition in one line'],
            [['Store', 'A specified secure place where materials are received, kept and issued'],
             ['Records keeping', 'Systematic writing, posting, preserving and retrieving of all '
              'documents evidencing receipt, storage, issue and disposal of stores'],
             ['Goods inward section', 'The receiving section where consignments are unloaded, '
              'checked against the PO, inspected and documented on a GRN'],
             ['GRN', 'Internal note certifying the quantity and condition of material actually '
              'received \u2014 authority to take on charge and to pay'],
             ['Delivery challan', 'Supplier\u2019s document of *movement* of goods, travelling with '
              'the consignment'],
             ['Invoice', 'Supplier\u2019s *demand for payment* showing rate, tax and total value'],
             ['Quarantine', 'Segregation of material awaiting a decision on its quality '
              '(yellow label)'],
             ['Classification', 'Grouping of similar items on the basis of a common characteristic'],
             ['Codification', 'Allotting a unique symbol (number/letter) to each item of stores'],
             ['Standardisation', 'Fixing a definite specification for each item stocked'],
             ['Variety reduction', 'Reducing the number of varieties/brands/pack sizes of the same item'],
             ['Stores vocabulary / item master', 'Master list of all code numbers with descriptions'],
             ['Stock book / stock register', 'Item-wise permanent account of receipts, issues and '
              'balance'],
             ['Bin card', 'Card at the bin showing quantity received, issued and balance, posted by '
              'the store keeper'],
             ['Stores ledger', 'Office record of quantity (and value) posted from vouchers by the '
              'ledger clerk'],
             ['Indent', 'Formal written demand for supply of specified materials'],
             ['Purchase order', 'The external contract placed on a supplier'],
             ['Lead time', 'Time from raising the indent to the material being available for issue'],
             ['Re-order level', 'Balance at which a fresh order must be placed'],
             ['Safety (buffer) stock', 'Reserve held to absorb unexpected demand or delay'],
             ['EOQ', 'Order size at which total ordering cost = total carrying cost, so total cost '
              'is minimum'],
             ['Inventory turnover ratio', 'Annual consumption value \u00F7 average inventory value'],
             ['FIFO / FEFO', 'First-in-first-out / first-expiry-first-out method of issue'],
             ['Imprest system', 'Fixed scale of stock at a ward, topped up to full each cycle'],
             ['Cold chain', 'System keeping thermolabile products continuously at +2 to +8 \u00B0C '
              'from manufacturer to patient'],
             ['Shelf life', 'Period for which a drug retains its specified potency (\u2265 90 %) '
              'under stated storage conditions'],
             ['Condemnation', 'Formal declaration by a board that stores are unserviceable and may '
              'be disposed of']])

    # ------------------------------------------------------------------ 13.2
    b.h2('13.2', 'All Formulae on One Page')
    b.table(['Quantity', 'Formula'],
            [['Closing balance', 'Opening balance + receipts \u2212 issues \u2212 losses + returns'],
             ['**EOQ**', '**\u221A(2AO / C)**  where A = annual demand, O = ordering cost/order, '
              'C = carrying cost/unit/year (= i \u00D7 p)'],
             ['Number of orders per year', 'Annual consumption \u00F7 EOQ'],
             ['**Re-order level**', '(Average consumption \u00D7 lead time) + safety stock'],
             ['Re-order level (simplified)', 'Maximum consumption \u00D7 maximum lead time'],
             ['**Safety stock**', '(Maximum consumption \u2212 average consumption) \u00D7 lead time'],
             ['Minimum level', 'ROL \u2212 (average consumption \u00D7 average lead time)'],
             ['**Maximum level**', 'ROL + order quantity \u2212 (minimum consumption \u00D7 '
              'minimum lead time)'],
             ['Danger level', 'Average consumption \u00D7 emergency lead time'],
             ['Average stock', 'Minimum level + \u00BD order quantity  *or*  '
              '(maximum + minimum) \u00F7 2'],
             ['**Indent quantity**', 'AMC \u00D7 (period of cover + lead time) + buffer '
              '\u2212 stock in hand \u2212 dues-in'],
             ['Average monthly consumption (AMC)', 'Total issues of n months \u00F7 n'],
             ['**Inventory turnover ratio**', 'Annual consumption value \u00F7 average inventory value'],
             ['Average inventory value', '(Opening stock + closing stock) \u00F7 2'],
             ['Months of stock in hand', 'Closing stock \u00F7 average monthly consumption'],
             ['Expiry (wastage) rate %', '(Value expired \u00F7 value consumed) \u00D7 100'],
             ['Carrying cost', 'Commonly taken as 20\u201325 % of average inventory value per year']])

    # ------------------------------------------------------------------ 13.3
    b.h2('13.3', 'Selective Inventory Control — Criterion Table (memorise)')
    b.table(['Technique', 'Criterion', 'Classes'],
            [['**ABC**', 'Annual consumption **value**',
              'A \u2248 10 % items/70 % value \u2022 B \u2248 20 %/20 % \u2022 C \u2248 70 %/10 %'],
             ['**VED**', '**Criticality**', 'Vital \u2022 Essential \u2022 Desirable'],
             ['**VEN**', 'Criticality (WHO)', 'Vital \u2022 Essential \u2022 Non-essential'],
             ['**HML**', '**Unit price**', 'High \u2022 Medium \u2022 Low'],
             ['**XYZ**', 'Value of **stock lying in store**', 'X high \u2022 Y moderate \u2022 Z low'],
             ['**FSN / FSND**', 'Rate of **movement**', 'Fast \u2022 Slow \u2022 Non-moving '
              '(\u2022 Dead)'],
             ['**SDE**', '**Availability**', 'Scarce \u2022 Difficult \u2022 Easy'],
             ['**GOLF**', '**Source of supply**',
              'Government \u2022 Ordinary \u2022 Local \u2022 Foreign'],
             ['**SOS**', '**Seasonality**', 'Seasonal \u2022 Off-seasonal'],
             ['**MUSIC-3D**', 'Cost + criticality + availability together', 'Multi-dimensional']])

    # ------------------------------------------------------------------ 13.4
    b.h2('13.4', 'Storage Temperatures and Conditions (IP)')
    b.table(['Term', 'Temperature'],
            [['Deep freezer / store frozen', 'Below \u221218 to \u221220 \u00B0C'],
             ['**Cold place**', '**Not exceeding 8 \u00B0C**'],
             ['**Refrigerator**', '**2 \u2013 8 \u00B0C**'],
             ['**Cool place**', '**8 \u2013 25 \u00B0C**'],
             ['Room temperature', '15 \u2013 30 \u00B0C (WHO 15 \u2013 25 \u00B0C)'],
             ['Controlled room temperature', '20 \u2013 25 \u00B0C'],
             ['**Warm**', '**30 \u2013 40 \u00B0C**'],
             ['**Excessive heat**', '**Above 40 \u00B0C**'],
             ['Whole blood / packed cells', '**2 \u2013 6 \u00B0C**'],
             ['Platelets', '**20 \u2013 24 \u00B0C with continuous agitation**'],
             ['Fresh frozen plasma', '**Below \u221230 \u00B0C**'],
             ['Vaccines (cold chain)', '**+2 to +8 \u00B0C**; ice packs/OPV in deep freezer at '
              '\u221215 to \u221225 \u00B0C'],
             ['General drug store', 'Below 25 \u00B0C, RH below 60 %'],
             ['Distance of stock from wall / floor', '**30 cm from the wall \u2022 10 cm above the '
              'floor (pallets)**']])

    # ------------------------------------------------------------------ 13.5
    b.h2('13.5', 'Schedules, Forms and Retention Periods')
    b.table(['Item', 'Answer'],
            [['Schedule prescribing **life period & storage conditions** of drugs', '**Schedule P**'],
             ['Schedule prescribing **minimum equipment for a pharmacy**', '**Schedule N**'],
             ['Schedule prescribing **GMP and records** for manufacturers', '**Schedule M**'],
             ['Schedule of **prescription-only drugs**', '**Schedule H**'],
             ['Schedule needing a **separate register kept for 3 years** and a red vertical line '
              'on the label', '**Schedule H1**'],
             ['Schedule of **habit-forming drugs** needing a separate locked cupboard and '
              'duplicate prescription', '**Schedule X**'],
             ['Schedule of **biological & special products** (sera, vaccines, insulin)',
              '**Schedule C and C(1)**'],
             ['Schedule needing the caution "to be taken under medical supervision"', '**Schedule G**'],
             ['Schedule listing **exemptions**', '**Schedule K**'],
             ['Schedule for **clinical trials / new drugs**', '**Schedule Y**'],
             ['Retail licence (ordinary drugs)', '**Form 20**'],
             ['Wholesale licence (ordinary drugs)', '**Form 20B**'],
             ['Retail / wholesale licence for **Schedule C & C(1)**', '**Form 21 / 21B**'],
             ['Application for **Schedule X** licence', '**Form 19C**'],
             ['Retail / wholesale licence for **Schedule X**', '**Form 20F / 20G**'],
             ['Government Analyst\u2019s report', '**Form 13**'],
             ['Inspector\u2019s receipt for a sample', '**Form 16**'],
             ['Intimation that a sample is sent for test', '**Form 17**'],
             ['Order prohibiting sale/disposal of stock', '**Form 18**'],
             ['Retention: Schedule H / Schedule X records', '**2 years**'],
             ['Retention: Schedule H1 register', '**3 years**'],
             ['Retention: narcotic registers', '**2 years** (as per NDPS Rules)'],
             ['Retention: GST books of account', '**6 years (72 months)**'],
             ['Retention: batch records of a manufacturer',
              '**1 year beyond expiry date** (Schedule M)'],
             ['Retention: dead-stock register', '**Permanent** (till condemnation)']])

    # ------------------------------------------------------------------ 13.6
    b.h2('13.6', 'Colour Codes')
    b.table(['Context', 'Colour \u2192 meaning'],
            [['Consignment status', '**Yellow** = quarantine/under test \u2022 **Green** = approved '
              '\u2022 **Red** = rejected'],
             ['Expiry traffic light', '**Red** \u2264 3 months \u2022 **Yellow** 3\u20136 months '
              '\u2022 **Green** > 6 months'],
             ['Oxygen cylinder (India)', '**Black body, white shoulder** (USA: green)'],
             ['Nitrous oxide', '**Blue**'],
             ['Carbon dioxide', '**Grey**'],
             ['Medical air (India)', '**Grey body, black & white quartered shoulders**'],
             ['Nitrogen (India)', '**Grey body, black shoulder**'],
             ['Helium', '**Brown**'],
             ['Entonox', '**Blue body, blue & white quartered shoulders**'],
             ['BMW \u2014 expired/discarded medicines, cytotoxic, anatomical waste',
              '**Yellow** \u2192 incineration / deep burial'],
             ['BMW \u2014 contaminated recyclable plastic (tubing, IV sets, gloves)',
              '**Red** \u2192 autoclave + shred + recycle'],
             ['BMW \u2014 sharps (needles, blades)',
              '**White translucent puncture-proof** \u2192 autoclave + shred'],
             ['BMW \u2014 glassware, ampoules, metallic implants',
              '**Blue** \u2192 disinfect + recycle']])

    # ------------------------------------------------------------------ 13.7
    b.h2('13.7', 'Differences You Must Be Able to Write')
    b.table(['Pair', 'Key distinction'],
            [['Bin card vs stores ledger', 'At the bin, quantity only, store keeper vs in the '
              'office, quantity + value, ledger clerk'],
             ['Challan vs invoice', 'Movement of goods vs demand for payment'],
             ['GRN vs challan', 'Prepared by the **buyer** vs prepared by the **supplier**'],
             ['Indent vs purchase order', 'Internal demand vs external contract'],
             ['FIFO vs FEFO', 'Oldest **received** first vs earliest **expiring** first'],
             ['FIFO vs LIFO (valuation)', 'Issues priced at oldest rate vs latest rate'],
             ['Rate contract vs running contract', 'Rate fixed, quantity not fixed vs both fixed'],
             ['EMD vs security deposit', 'Deposited **with the bid** vs kept **after award** of contract'],
             ['ABC vs VED', 'Annual consumption **value** vs **criticality**'],
             ['HML vs ABC', '**Unit price** vs **annual consumption value**'],
             ['Perpetual vs periodic verification', 'Few items daily, all year round vs whole stock '
              'on one date'],
             ['Consumable vs dead stock', 'Used up (drugs) vs permanent (equipment)'],
             ['Debit note vs credit note', 'Raised by the buyer vs issued by the supplier'],
             ['Quarantine vs rejected area', 'Awaiting decision vs decision taken \u2014 rejected'],
             ['Cold place vs cool place (IP)', '\u2264 8 \u00B0C vs 8\u201325 \u00B0C'],
             ['Freeze-sensitive vs heat-sensitive vaccine',
              'DPT/Hep-B/TT/insulin (never freeze) vs OPV/measles/BCG (tolerate freezing)'],
             ['Centralised vs decentralised store', 'Lower stock & better control vs faster supply '
              'at the point of use'],
             ['Brisch vs Kodak code', '7 digits, 3 stages, UK vs 10 digits (3+4+3), '
              'source-of-supply oriented, USA']])

    # ------------------------------------------------------------------ 13.8
    b.h2('13.8', 'Sequences and Procedures in Order')
    b.table(['Process', 'Correct order'],
            [['Purchase cycle', 'Indent \u2192 sanction \u2192 enquiry/tender \u2192 comparative '
              'statement \u2192 PO \u2192 receipt & GRN \u2192 stock records \u2192 bill passing '
              '\u2192 payment'],
             ['Goods inward clerical procedure',
              'Gate entry \u2192 documents vs PO \u2192 unload & count \u2192 unpack \u2192 quantity '
              'check \u2192 quality check \u2192 sample to QC \u2192 quarantine \u2192 goods inward '
              'register \u2192 GRN \u2192 inspection result \u2192 take on charge (bin card + '
              'ledger) \u2192 discrepancy report/claims \u2192 bill passing \u2192 filing'],
             ['Issue cycle', 'Indent \u2192 scrutiny \u2192 sanction \u2192 issue voucher \u2192 '
              'FEFO picking \u2192 receiver\u2019s signature \u2192 posting of bin card, ledger and '
              'ward register \u2192 consumption statement'],
             ['Stores system design',
              'Classification \u2192 standardisation/variety reduction \u2192 codification \u2192 '
              'bin location \u2192 stock records'],
             ['Condemnation', 'Listing \u2192 condemnation board \u2192 sanction \u2192 disposal '
              '(auction/destruction) \u2192 register entry + certificate'],
             ['Expiry handling', 'Monthly near-expiry list \u2192 colour tagging \u2192 '
              'redistribution/return \u2192 on expiry segregate & enter register \u2192 write-off '
              'sanction \u2192 BMW disposal \u2192 destruction certificate'],
             ['Tender process', 'NIT \u2192 tender document \u2192 two-bid submission with EMD '
              '\u2192 technical bid opening \u2192 price bid opening \u2192 comparative statement '
              '\u2192 L-1 \u2192 approval \u2192 PO \u2192 security deposit/agreement']])

    # ------------------------------------------------------------------ 13.9
    b.h2('13.9', 'Numbers, Percentages and Standards Worth Memorising')
    b.table(['Fact', 'Value'],
            [['ABC classes', 'A: \u2248 10 % of items, 70 % of value \u2022 B: 20 %/20 % \u2022 '
              'C: 70 %/10 %'],
             ['Inventory carrying cost', '\u2248 20\u201325 % of average inventory value per year'],
             ['Drugs as a share of the hospital recurring budget', '\u2248 30\u201340 %'],
             ['Minimum remaining shelf life demanded in drug tenders',
              'Usually **5/6 (\u2248 83 %) of total shelf life** at delivery'],
             ['Potency limit defining shelf life', 'Not less than **90 %** of the labelled amount'],
             ['Store temperature / humidity', 'Below **25 \u00B0C** / RH below **60 %**'],
             ['Temperature recording frequency', '**Twice daily** (morning and evening)'],
             ['Distance of stock from wall / height above floor', '**30 cm / 10 cm**'],
             ['Multi-dose eye-drop in-use period after opening', 'Commonly **28 days**'],
             ['VVM usable stages', '**Stages 1 and 2** only (discard at 3 and 4)'],
             ['Cytotoxic waste incineration temperature', '**\u2265 1,200 \u00B0C**'],
             ['Frost thickness at which an ILR must be defrosted', 'More than about **5 mm**'],
             ['Number of GRN copies usually prepared', '**4\u20135**'],
             ['Members of a condemnation board', 'Usually **3** (including one officer unconnected '
              'with the store)']])

    # ------------------------------------------------------------------ 13.10
    b.h2('13.10', 'Mnemonic Collection')
    b.table(['Topic', 'Mnemonic'],
            [['5 R\u2019s of purchasing', '**Q-Q-P-T-S** \u2014 Quality, Quantity, Price, Time, Source'],
             ['Functions of stores',
              '**R-I-S-R-I-S-V-H-D-I** \u2014 Receive, Inspect, Store, Record, Issue, '
              'Stock-control, Verify, Housekeep, Dispose, Inform'],
             ['Layout zones of a store',
              '**R-Q-S-C-N-H-R-I-O-B** \u2014 Receiving, Quarantine, Storage, Cold, Narcotic, '
              'Hazardous, Rejected, Issue, Office, Bulk'],
             ['Goods inward steps',
              '**G-D-P-U-U-Q-Q-S-Q-G-G-I-T-D-B-F** (gate entry \u2026 filing)'],
             ['Good code',
              '**U-B-F-S-M-E** \u2014 Unique, Brief, Flexible, Simple, Mnemonic, Exhaustive'],
             ['Inventory criteria',
              '**A**=Amount(value), **V**=Vitality, **H**=High price, **X**=eXisting stock value, '
              '**F**=Frequency of movement, **S**=Scarcity, **G**=Geographic source, **S**=Season'],
             ['Data integrity', '**ALCOA+** \u2014 Attributable, Legible, Contemporaneous, Original, '
              'Accurate (+ Complete, Consistent, Enduring, Available)'],
             ['Special storage categories',
              '**N-X-T-B-L-M-V-C-C-R-G-L-H** \u2014 Narcotics, Schedule X, Thermolabile, Blood, '
              'Light-sensitive, Moisture-sensitive, Volatile, Corrosives, Cytotoxics, '
              'Radiopharmaceuticals, Gases, LASA, High-alert']])

    # ------------------------------------------------------------------ 13.11
    b.h2('13.11', 'Fifty Facts \u2014 Final Rapid Fire')
    b.numbered([
        'Records keeping ensures **accountability, legal compliance, financial control and traceability**.',
        'A wrong entry is corrected by **scoring out with one line + attestation**; never erased.',
        'Registers must be **bound with machine-numbered pages** and carry a page certificate.',
        'The **stock verifier must be independent of the custodian**.',
        '**Purchase, receipt and payment functions must be separated** (internal check).',
        'The **PTC** decides which drugs are stocked; the **purchase committee** decides from whom.',
        'The **hospital formulary** is the list of drugs approved for use in that hospital.',
        '**Rate contract** fixes the rate, not the quantity.',
        'The lowest evaluated bidder is **L-1**; bid security is **EMD**.',
        '**Three-way matching** = Purchase Order + GRN + Invoice.',
        'The **GRN** is prepared by the receiving section, usually in 4\u20135 copies.',
        'The **delivery challan** accompanies the goods; the **invoice** demands payment.',
        'Transit claims need the **lorry receipt/consignment note** and damage noted at delivery.',
        '**Quarantine = yellow, approved = green, rejected = red.**',
        'Late supply attracts **liquidated damages**.',
        'Drug tenders normally demand at least **5/6 of the shelf life** remaining at delivery.',
        'Excess or unordered goods are **not taken on charge** without sanction.',
        '**Dues-in must be deducted** while preparing the next indent.',
        '**Bin card** = store keeper, quantity, at the bin; **ledger** = ledger clerk, quantity + '
        'value, in the office.',
        '**Dead-stock register** = non-consumable items; removed only on condemnation.',
        'Sequence: **classification \u2192 standardisation \u2192 codification**.',
        '**Brisch = 7 digits, 3 stages (UK); Kodak = 10 digits (USA)**; decimal system = **Dewey**.',
        'The commonest practical coding system is **alpha-numerical**.',
        'The master list of codes is the **stores vocabulary / item master**.',
        '**ABC** is based on annual consumption **value** (Pareto 80:20 idea).',
        '**VED** is based on **criticality**; all **V** items go into control **Category I**.',
        '**HML** = unit price; **XYZ** = value of stock in store; **FSN** = movement; '
        '**SDE** = availability; **GOLF** = source; **SOS** = season.',
        '**EOQ = \u221A(2AO/C)**; at EOQ, ordering cost = carrying cost.',
        '**ROL = (average consumption \u00D7 lead time) + safety stock.**',
        '**Danger level** \u2192 stop normal issues and make an emergency purchase.',
        '**Two-bin system** suits cheap **C** items.',
        '**Perpetual verification** covers a few items daily throughout the year.',
        'The stock equation: **closing = opening + receipts \u2212 issues \u2212 losses + returns**.',
        '**Inventory turnover = annual consumption value \u00F7 average inventory value.**',
        'Indent quantity = **AMC \u00D7 (cover + lead time) + buffer \u2212 stock in hand '
        '\u2212 dues-in**.',
        'For a new hospital with no consumption data, use the **morbidity method**.',
        'Indent by **generic name + strength + dosage form + pack + IP standard**.',
        'Commonest store arrangement: **dosage form-wise, alphabetical within the form**.',
        '**FEFO** is superior to FIFO for drugs.',
        '**IP: cold \u2264 8 \u00B0C, refrigerator 2\u20138 \u00B0C, cool 8\u201325 \u00B0C, '
        'warm 30\u201340 \u00B0C, excessive heat > 40 \u00B0C.**',
        '**Schedule P** = life period and storage conditions; **Schedule N** = pharmacy equipment.',
        'Cold chain = **+2 to +8 \u00B0C**; **ILR** for vaccines, **deep freezer** for ice packs.',
        '**Freeze-sensitive**: DPT, TT/Td, Hep-B, IPV, pentavalent, insulin. '
        '**Heat-sensitive**: OPV (most), measles, BCG.',
        'A **VVM** at stage 3 or 4 means **discard the vial**.',
        'Blood **2\u20136 \u00B0C**, platelets **20\u201324 \u00B0C with agitation**, FFP '
        '**below \u221230 \u00B0C**.',
        'Narcotics: **double-locked cupboard, daily tally, NDPS register, destruction only before '
        'the authorised officer**.',
        'Schedule X: **Form 19C \u2192 20F/20G**, separate locked cupboard, duplicate prescription, '
        'records **2 years**.',
        '**Schedule H1 register is preserved for 3 years**; the label carries a **red vertical line**.',
        'Expired medicines go into the **yellow** bio-medical waste category; cytotoxic waste is '
        '**incinerated**.',
        'Stock kept **30 cm from the wall, 10 cm above the floor**, store **below 25 \u00B0C**, '
        'RH **below 60 %**, temperature logged **twice daily**.',
    ])
    b.page_break()


def chapter14(b):
    b.chapter(14, 'Glossary and Abbreviations',
              'Every technical term used in this book, in one alphabetical list')

    b.h2('14.1', 'Glossary of Terms')
    b.table(['Term', 'Meaning'],
            [['**ABC analysis**', 'Classification of items by annual consumption value'],
             ['**AMC**', 'Average monthly consumption'],
             ['**Beyond-use date (BUD)**', 'Date after which an opened/reconstituted product must '
              'not be used'],
             ['**Bin**', 'Compartment, rack or shelf position in which an item is kept'],
             ['**Bin card**', 'Card at the bin recording quantity received, issued and balance'],
             ['**Bonded store**', 'Store for goods on which duty/excise has not yet been paid '
              '(e.g. spirit)'],
             ['**Buffer stock**', 'Reserve/safety stock'],
             ['**Carrying cost**', 'Cost of holding inventory (interest, storage, insurance, expiry)'],
             ['**CIF**', 'Cost, Insurance and Freight \u2014 seller bears these up to destination'],
             ['**Cold chain**', 'Unbroken +2 to +8 \u00B0C chain for thermolabile products'],
             ['**Condemnation**', 'Declaring stores unserviceable and fit for disposal'],
             ['**Credit note**', 'Document by which a supplier reduces the amount payable'],
             ['**Danger level**', 'Stock level at which emergency purchase becomes necessary'],
             ['**Dead stock**', 'Non-consumable, permanent items (equipment, furniture)'],
             ['**Debit note**', 'Document by which the buyer reduces the supplier\u2019s claim'],
             ['**Dues-in**', 'Quantity ordered but not yet received'],
             ['**EMD**', 'Earnest Money Deposit (bid security)'],
             ['**EOQ**', 'Economic Order Quantity'],
             ['**FEFO**', 'First Expiry First Out'],
             ['**FIFO**', 'First In First Out'],
             ['**FOB**', 'Free On Board'],
             ['**Gate pass**', 'Authority for material to leave the premises (returnable or not)'],
             ['**GDP / GSP**', 'Good Distribution Practice / Good Storage Practice'],
             ['**GRN**', 'Goods Received Note'],
             ['**GS1 / GTIN**', 'Global standards body / Global Trade Item Number used in bar codes'],
             ['**HML analysis**', 'Classification by unit price (High, Medium, Low)'],
             ['**ILR**', 'Ice-Lined Refrigerator (+2 to +8 \u00B0C)'],
             ['**Imprest**', 'Fixed scale of stock held by a ward, replenished to full each cycle'],
             ['**Indent**', 'Written demand for supply of material'],
             ['**Inventory turnover ratio**', 'Annual consumption value \u00F7 average inventory value'],
             ['**Kardex**', 'Visible-index card system for stock records'],
             ['**LASA**', 'Look-Alike Sound-Alike drugs'],
             ['**L-1**', 'Lowest evaluated (successful) tenderer'],
             ['**LD**', 'Liquidated damages (penalty for late supply)'],
             ['**Lead time**', 'Time from raising the indent to material being available for issue'],
             ['**LR / RR**', 'Lorry Receipt / Railway Receipt (consignment note)'],
             ['**MRN**', 'Material Return Note'],
             ['**NLEM**', 'National List of Essential Medicines'],
             ['**NSQ**', 'Not of Standard Quality'],
             ['**NDPS**', 'Narcotic Drugs and Psychotropic Substances (Act, 1985)'],
             ['**PO**', 'Purchase Order'],
             ['**PTC**', 'Pharmacy and Therapeutics Committee'],
             ['**Quarantine**', 'Segregation of material awaiting a quality decision'],
             ['**Rate contract**', 'Contract fixing the rate for a period, quantity not fixed'],
             ['**Re-order level (ROL)**', 'Balance at which a fresh order must be placed'],
             ['**RFID**', 'Radio-Frequency Identification'],
             ['**Salvage store**', 'Area holding expired, damaged or condemned stock'],
             ['**SDE analysis**', 'Classification by availability (Scarce, Difficult, Easy)'],
             ['**Shelf life**', 'Period for which the product retains its specified quality'],
             ['**Stores vocabulary**', 'Master list of code numbers and descriptions'],
             ['**Three-way matching**', 'Agreement of PO, GRN and invoice before payment'],
             ['**Two-bin system**', 'Re-ordering when the first of two bins empties'],
             ['**VED analysis**', 'Classification by criticality (Vital, Essential, Desirable)'],
             ['**VMI**', 'Vendor Managed Inventory'],
             ['**VVM**', 'Vaccine Vial Monitor'],
             ['**XYZ analysis**', 'Classification by the value of stock lying in store']])

    b.h2('14.2', 'A Final Word on Method')
    b.box('exam', 'HOW TO REVISE THIS BOOK IN THREE PASSES',
          bullets=['**Pass 1 (understanding):** read Chapters 1\u201312 once, slowly, following the '
                   'flow diagrams. Do not memorise yet.',
                   '**Pass 2 (structure):** re-read only the **tables** and the **coloured boxes**. '
                   'Write the step-lists of Chapter 3 (goods inward), Chapter 4 (issue procedure) '
                   'and Chapter 9 (indent preparation) from memory.',
                   '**Pass 3 (recall):** use Chapter 13 alone. Cover the right-hand column of every '
                   'table and recite the answer.',
                   'Pay special attention to: **definitions, the temperature table, schedules and '
                   'forms, retention periods, the inventory-criteria table, all formulae, and the '
                   'colour codes** \u2014 these carry the highest density of objective questions.'])
    b.rule()
    b.p('*Prepared as complete study notes for the Records Keeping \u2014 Stores Records & '
        'Procedures section of the JKSSB Junior Pharmacist syllabus: clerical procedure in the '
        'goods inward section, records and procedures in main stores, classification and '
        'codification, keeping of stock books, preparation of indents and methods of storing '
        'drugs. Content is compiled from standard hospital pharmacy, drug store management and '
        'materials management texts and from the Drugs and Cosmetics Act & Rules, the NDPS Act, '
        'the Bio-Medical Waste Management Rules and WHO storage/cold-chain guidance. Where State '
        'rules or institutional practice vary (financial powers, departmental retention periods, '
        'local formats), the position given is the commonly prescribed one.*',
        size=9)
