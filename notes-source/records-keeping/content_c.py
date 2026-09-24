# -*- coding: utf-8 -*-
"""Part III — Chapter 5 (classification) & Chapter 6 (codification)"""


def chapter5(b):
    b.part('PART III', 'Classification & Codification of Stores')
    b.chapter(5, 'Classification of Stores and Drug Items',
              'Meaning \u2022 need \u2022 bases of classification \u2022 hospital store groups '
              '\u2022 classification of drugs \u2022 schedules \u2022 standardisation')

    b.lead('Classification answers the question *"what kind of thing is this?"*; codification then '
           'answers *"what shall we call it in our books?"*. Classification always comes first — '
           'you cannot give a rational code number to an item whose group you have not yet decided.')

    # ------------------------------------------------------------------ 5.1
    b.h2('5.1', 'Meaning, Definition and Need')
    b.box('def', 'CLASSIFICATION',
          '**Classification of stores** is the **systematic grouping (sorting) of all items of '
          'stores into classes, groups and sub-groups** on the basis of some common characteristic '
          '\u2014 nature, use, source, value, movement, criticality or storage requirement \u2014 '
          'so that similar items lie together and can be identified, stored, accounted and '
          'controlled uniformly.')
    b.h3('5.1.1  Need / objectives of classification')
    b.numbered([
        'To **identify** each item unambiguously and to eliminate confusion between similar items.',
        'To make **codification possible** — a code is meaningful only when built on a classification.',
        'To group items that need **similar storage conditions** (cold chain, inflammables, narcotics).',
        'To permit **selective control** — different inventory-control rules for costly, vital and '
        'fast-moving items.',
        'To simplify **location, stacking and retrieval** in the store.',
        'To standardise **specifications and units of issue**, and thereby reduce the **variety** '
        'of items stocked.',
        'To help **purchase** by grouping items of the same trade/supplier for combined tendering.',
        'To make **accounting, costing and budgeting** group-wise (drugs, surgicals, X-ray, '
        'laboratory, stationery).',
        'To simplify **stock verification** and **statistical analysis** (consumption of a group '
        'over the years).',
        'To meet **legal requirements** that certain classes (Schedule H, H1, X, narcotics) be '
        'stored and recorded separately.',
    ])
    b.box('hy', 'ONE LINE',
          '**Classification = grouping of similar items. Codification = giving a symbol/number to '
          'each item. Standardisation = fixing a specification. Variety reduction (simplification) '
          '= reducing the number of varieties of the same item.** These four are always examined '
          'together as a set of definitions.')

    # ------------------------------------------------------------------ 5.2
    b.h2('5.2', 'Bases of Classification')
    b.table(['Basis', 'Classes formed', 'Example'],
            [['**Nature / physical character**', 'Solids, liquids, semi-solids, gases; glass, '
              'rubber, metal, plastic, textile', 'Tablets \u2022 syrups \u2022 ointments \u2022 oxygen'],
             ['**End use / function**', 'Drugs, surgical dressings, laboratory reagents, X-ray, '
              'linen, stationery, equipment, engineering spares, POL, diet',
              'The standard hospital store groups'],
             ['**Source of supply**', 'Indigenous, imported, government pool, rate contract, local',
              'Basis of **GOLF** analysis'],
             ['**Value / cost**', 'High, medium, low unit cost; high, medium, low annual consumption '
              'value', 'Basis of **HML** and **ABC** analysis'],
             ['**Criticality / importance**', 'Vital, essential, desirable',
              'Basis of **VED** analysis'],
             ['**Movement / rate of consumption**', 'Fast, slow, non-moving',
              'Basis of **FSN** analysis'],
             ['**Availability**', 'Scarce, difficult, easy to obtain', 'Basis of **SDE** analysis'],
             ['**Shelf life**', 'Long shelf life, short shelf life, perishable',
              'Vaccines, sera, blood products'],
             ['**Storage requirement**', 'Room temperature, cool, cold chain, frozen, '
              'light-sensitive, inflammable, hazardous', 'Determines the storage area'],
             ['**Legal status**', 'Schedule H, H1, X, C, C(1), G, narcotics & psychotropics, '
              'OTC/general sale', 'Determines the record and the lock'],
             ['**Therapeutic / pharmacological action**', 'Antibiotics, analgesics, antihypertensives, '
              'anti-diabetics \u2026', 'Common arrangement in hospital pharmacies'],
             ['**Dosage form / route**', 'Oral solids, orals liquids, injections, externals, '
              'ophthalmics, inhalations, suppositories', 'Commonest physical arrangement in a store'],
             ['**Consumable vs non-consumable**', 'Expendable (drugs, dressings) vs permanent/dead '
              'stock (equipment, furniture)', 'Determines which register is used'],
             ['**Accounting classification**', 'Capital vs revenue; budget head-wise',
              'For financial reporting']])

    # ------------------------------------------------------------------ 5.3
    b.h2('5.3', 'Classification of Hospital Store Items (Functional Groups)')
    b.table(['Group', 'Typical items'],
            [['**Drugs & pharmaceuticals**', 'Tablets, capsules, injections, IV fluids, syrups, '
              'ointments, eye/ear drops, inhalers, vaccines & sera'],
             ['**Surgical dressings & disposables**', 'Gauze, bandages, cotton, plaster of Paris, '
              'sutures, syringes, needles, catheters, IV sets, gloves, masks'],
             ['**Chemicals & laboratory reagents**', 'Stains, indicators, solvents, diagnostic kits, '
              'glassware'],
             ['**X-ray & imaging materials**', 'Films, contrast media, developer, fixer, cassettes'],
             ['**Instruments & equipment (dead stock)**', 'Surgical instruments, BP apparatus, '
              'autoclaves, monitors, refrigerators'],
             ['**Linen & clothing**', 'Bed sheets, draw sheets, OT gowns, uniforms, mackintosh'],
             ['**Furniture & fixtures**', 'Beds, lockers, trolleys, almirahs, chairs'],
             ['**Stationery & printing**', 'Registers, case sheets, forms, prescription pads, '
              'computer consumables'],
             ['**Sanitary & housekeeping**', 'Disinfectants, phenyl, bleaching powder, brooms, '
              'detergents, waste bags'],
             ['**Engineering / maintenance spares & POL**', 'Electrical fittings, plumbing spares, '
              'oils, lubricants, generator fuel'],
             ['**Medical gases**', 'Oxygen, nitrous oxide, carbon dioxide, medical air, nitrogen'],
             ['**Diet / provisions**', 'Rations for the hospital kitchen'],
             ['**Narcotics & psychotropics**', 'Morphine, pethidine, fentanyl, diazepam, '
              'pentazocine, buprenorphine'],
             ['**Cold-chain items**', 'Vaccines, sera, insulin, oxytocin, blood products, some '
              'antibiotic eye drops'],
             ['**Hazardous items**', 'Inflammables (ether, spirit), corrosives (acids), cytotoxics, '
              'radiopharmaceuticals']])

    # ------------------------------------------------------------------ 5.4
    b.h2('5.4', 'Classification of Drugs')
    b.h3('5.4.1  On the basis of therapeutic / pharmacological action')
    b.p('e.g. **analgesics & antipyretics, NSAIDs, antibiotics (further sub-grouped as penicillins, '
        'cephalosporins, aminoglycosides, macrolides, quinolones\u2026), antitubercular, antimalarial, '
        'antifungal, antiviral, antihypertensives, diuretics, cardiac drugs, antidiabetics, '
        'hormones, vitamins & minerals, antihistamines, corticosteroids, anaesthetics, '
        'psychotropics, anticonvulsants, gastro-intestinal drugs, respiratory drugs, oxytocics, '
        'vaccines & sera, antiseptics & disinfectants, IV fluids and electrolytes, anticancer drugs**.')
    b.h3('5.4.2  On the basis of dosage form')
    b.table(['Class', 'Forms'],
            [['Oral solids', 'Tablets, capsules, powders, granules, lozenges'],
             ['Oral liquids', 'Syrups, elixirs, suspensions, emulsions, drops, linctus'],
             ['Parenterals (injections)', 'Ampoules, vials, pre-filled syringes, large-volume '
              'IV fluids'],
             ['Externals / topicals', 'Ointments, creams, pastes, gels, lotions, liniments, powders'],
             ['Ophthalmic / otic / nasal', 'Eye drops & ointments, ear drops, nasal sprays'],
             ['Rectal & vaginal', 'Suppositories, pessaries, enemas'],
             ['Inhalations / respiratory', 'MDI, DPI, nebuliser solutions, medical gases'],
             ['Transdermal & implants', 'Patches, implants']])
    b.h3('5.4.3  On the basis of legal status — Schedules of the Drugs and Cosmetics Rules, 1945')
    b.table(['Schedule', 'Subject matter (as relevant to a store)'],
            [['**Schedule C and C(1)**', '**Biological and special products** \u2014 sera, vaccines, '
              'toxoids, antitoxins, insulin, pituitary/other hormones, sterile products and other '
              'special drugs; require licence in **Form 21/21B** and generally **cold storage**'],
             ['**Schedule D**', 'Classes of drugs exempted from import provisions'],
             ['**Schedule F / F(1)**', 'Requirements for blood banks, blood components and for '
              'vaccines & sera'],
             ['**Schedule F(II)**', 'Standards for surgical dressings'],
             ['**Schedule F(III)**', 'Standards for umbilical tapes'],
             ['**Schedule G**', 'Drugs to be used **only under medical supervision** \u2014 label '
              'carries the caution *"Caution: it is dangerous to take this preparation except '
              'under medical supervision"* (e.g. many antineoplastics)'],
             ['**Schedule H**', '**Prescription drugs** \u2014 sold only on the prescription of a '
              'registered medical practitioner; label bears **"Rx"** and the warning *"Schedule H '
              'drug \u2014 Warning: to be sold by retail on the prescription of a Registered '
              'Medical Practitioner only"*'],
             ['**Schedule H1**', 'Specified **3rd/4th-generation antibiotics, anti-TB drugs and '
              'certain psychotropics**; label bears a **red vertical line** on the left border with '
              'the H1 warning; a **separate register** of sales must be kept'],
             ['**Schedule J**', 'Diseases & conditions for which **no drug may claim to cure** '
              '(advertisement prohibition)'],
             ['**Schedule K**', 'Classes of drugs **exempted** from certain provisions (e.g. '
              'household remedies, supply by registered practitioners, drugs supplied by a '
              'hospital to its own patients)'],
             ['**Schedule M**', '**GMP** \u2014 requirements of premises, plant, equipment and of '
              '**records & documentation** for manufacturers'],
             ['**Schedule M(III)**', 'Requirements for medical devices'],
             ['**Schedule N**', 'Minimum **equipment for the efficient running of a pharmacy**'],
             ['**Schedule P**', '**Life periods (shelf life) and storage conditions** of drugs'],
             ['**Schedule P(1)**', 'Pack sizes of drugs'],
             ['**Schedule Q**', 'Permitted colours/dyes in drugs & cosmetics'],
             ['**Schedule V**', 'Standards for patent and proprietary medicines'],
             ['**Schedule W**', 'Drugs marketable only under generic names'],
             ['**Schedule X**', '**Habit-forming / narcotic & psychotropic type drugs** '
              '(e.g. barbiturates, amphetamine, methaqualone-type substances) \u2014 require '
              '**special licence (Forms 20F/20G on application in Form 19C)**, storage in a '
              '**separate locked cupboard**, prescription in **duplicate**, and a separate register'],
             ['**Schedule Y**', 'Requirements for **clinical trials** and import/manufacture of new '
              'drugs']])
    b.box('hy', 'SCHEDULE P \u2014 REMEMBER THE NAME',
          '**Schedule P of the Drugs and Cosmetics Rules prescribes the *life period (shelf life)* '
          'and the *conditions of storage* of drugs** \u2014 the single most directly relevant '
          'schedule for the topic "methods of storing drugs". **Schedule N** = minimum equipment '
          'for a pharmacy; **Schedule M** = GMP and records.')
    b.h3('5.4.4  Other classifications of drugs')
    b.bullets([
        '**By source** — natural (plant, animal, mineral, microbial), synthetic, semi-synthetic, '
        'biotechnological.',
        '**By system of medicine** — allopathic (modern), ayurvedic, siddha, unani, homoeopathic '
        '(stored **separately**, with separate licences and registers).',
        '**By essentiality** — NLEM/EML drugs vs non-essential; hospital formulary vs non-formulary.',
        '**By price control** — scheduled formulations (ceiling price under DPCO) vs non-scheduled.',
        '**By risk in handling** — LASA (look-alike sound-alike), high-alert/high-risk drugs '
        '(insulin, heparin, concentrated electrolytes, narcotics, chemotherapy), '
        'ordinary drugs.',
        '**Alphabetical** — simple A\u2013Z arrangement of generic (or brand) names; commonest in '
        'small pharmacies.',
    ])

    # ------------------------------------------------------------------ 5.5
    b.h2('5.5', 'Standardisation, Simplification and Variety Reduction')
    b.kv([
        ('Standardisation', 'Fixing a **definite specification, size, quality and unit** for each '
                            'item to be stocked (e.g. only 5 ml disposable syringes of one make '
                            'and specification).'),
        ('Simplification / variety reduction', 'Reducing the **number of varieties, brands, '
                                               'strengths and pack sizes** of the same item — the '
                                               'work of the hospital formulary and the '
                                               'Pharmacy & Therapeutics Committee.'),
        ('Benefits', 'Fewer items to store and record \u2022 larger quantity per item \u2192 better '
                     'price \u2022 less capital blocked \u2022 less obsolescence \u2022 easier '
                     'codification and stock verification \u2022 fewer dispensing errors.'),
        ('Link with codification', 'Standardisation and variety reduction must be done **before** '
                                   'codification; otherwise the code list is bloated with '
                                   'duplicate items under different brand names.'),
    ])
    b.box('exam', 'SEQUENCE TO REMEMBER',
          '**Classification \u2192 Standardisation / variety reduction \u2192 Codification \u2192 '
          'Location (bin) allotment \u2192 Stock records.** Examiners often ask which step comes '
          'first: *classification*.')
    b.page_break()


def chapter6(b):
    b.chapter(6, 'Codification of Stores Items',
              'Meaning \u2022 objectives \u2022 essentials of a good code \u2022 methods '
              '\u2022 Brisch & Kodak systems \u2022 bar codes \u2022 colour codes')

    b.lead('A code is the *name of an item in the language of the store*. It replaces a long, '
           'ambiguous description ("Injection Ceftriaxone 1 g vial, 10\u2019s pack") with a short, '
           'unique symbol that a clerk, a computer and an auditor all understand identically.')

    # ------------------------------------------------------------------ 6.1
    b.h2('6.1', 'Meaning and Definition')
    b.box('def', 'CODIFICATION',
          '**Codification (coding)** is the **process of assigning a systematic, unique symbol \u2014 '
          'numbers, letters or a combination of both \u2014 to every item of stores**, so that the '
          'item can be identified, described, located, recorded and communicated briefly and '
          'without ambiguity.')
    b.kv([
        ('Code / code number', 'The symbol itself, e.g. `02-14-0357`.'),
        ('Vocabulary of stores / stores catalogue', 'The master printed or electronic list showing '
                                                    'every code number with its full description, '
                                                    'unit of issue and location. Also called the '
                                                    '**item master**.'),
        ('Nomenclature', 'The standard *naming* of the item; codification is the standard '
                         '*numbering* of it.'),
    ])

    # ------------------------------------------------------------------ 6.2
    b.h2('6.2', 'Objectives and Advantages of Codification')
    b.numbered([
        '**Unique identification** of every item — eliminates confusion between similar items '
        '(different strengths, pack sizes, brands).',
        '**Brevity and accuracy** in all documents — indents, POs, GRNs, vouchers, ledgers.',
        '**Avoidance of duplication** — the same item cannot be stocked twice under two '
        'descriptions, so duplicate purchase is prevented.',
        '**Secrecy** — the nature/value of the item is not obvious to outsiders.',
        '**Ease of location** — the code can be linked to the rack/bin address.',
        '**Mechanisation / computerisation** — a computer needs a unique key field; the code is that key.',
        '**Standardisation and variety reduction** are exposed by coding (duplicates become visible).',
        '**Simplified pricing, costing and accounting** — group codes roll up into budget heads.',
        '**Faster stock verification** and posting; fewer clerical errors.',
        '**Better inventory analysis** — group-wise consumption and ABC/VED analysis become easy.',
        '**Language independence** — useful where staff speak different languages.',
    ])
    b.h3('6.2.1  Limitations / disadvantages')
    b.bullets([
        'Initial **cost, time and expertise** required to design the system and code thousands of items.',
        'Staff need **training**; a wrong digit means a wrong item (**transposition errors**).',
        'A badly designed (rigid) code becomes **inadequate when new items appear**.',
        'Purely numeric codes are **difficult to memorise**; very long codes are error-prone.',
        'Requires **continuous maintenance** of the item master (additions, deletions, mergers).',
    ])

    # ------------------------------------------------------------------ 6.3
    b.h2('6.3', 'Essentials (Requirements) of a Good Coding System')
    b.table(['Essential', 'Meaning'],
            [['**Uniqueness**', 'One code for one item and one item for one code — never two codes '
              'for the same item'],
             ['**Exhaustiveness**', 'Every item in the store must be codable; no item left out'],
             ['**Mutual exclusiveness**', 'An item must fall in one group only, with no overlap'],
             ['**Brevity / concise**', 'As short as possible while remaining unique (usually 6\u201310 '
              'characters)'],
             ['**Flexibility / expansibility**', 'Room for new items, new groups and new '
              'technologies without redesigning the whole system'],
             ['**Simplicity / ease of use**', 'Easy to read, write, remember and dictate; avoid '
              'confusing characters (I/1, O/0)'],
             ['**Mnemonic value**', 'The code itself should suggest the item wherever possible '
              '(e.g. `TAB` for tablet, `INJ` for injection)'],
             ['**Logical / hierarchical structure**', 'Digits should progress from the general group '
              'to the specific item'],
             ['**Uniformity**', 'Same length and same structure for all codes; same code used by '
              'every department'],
             ['**Compatibility**', 'Should fit the accounting heads, the computer system and, '
              'ideally, national standards (e.g. GS1 bar codes)'],
             ['**Documented & centrally controlled**', 'Only one authority may allot codes; the '
              'item master is the sole authentic list']])
    b.box('mnem', 'MNEMONIC — a good code is "U-B-F-S-M-E"',
          '**U**nique, **B**rief, **F**lexible, **S**imple, **M**nemonic, **E**xhaustive.')

    # ------------------------------------------------------------------ 6.4
    b.h2('6.4', 'Methods / Systems of Codification')
    b.table(['Method', 'How it works', 'Example', 'Comment'],
            [['**Alphabetical (mnemonic) system**',
              'Letters, usually the initials of the item name, form the code',
              '`PCM` = paracetamol; `CTX` = ceftriaxone; `COT` = cotton',
              'Easy to remember; but limited combinations, confusing for similar names'],
             ['**Numerical (numeric) system**',
              'Plain serial numbers allotted to items, either sequentially or in blocks reserved '
              'for groups', '`0001`, `0002` \u2026 or block `1000\u20131999` = tablets',
              'Simple and unlimited; but the number carries no meaning'],
             ['**Block / group numerical system**',
              'Blocks of numbers reserved for each group and sub-group',
              '`10\u201319` = drugs, `20\u201329` = surgicals',
              'Adds group meaning to a numeric code; widely used'],
             ['**Alpha-numerical (combined) system**',
              'Letters denote the group and numbers the individual item',
              '`TAB-0125`, `INJ-0341`, `SUR-0088`',
              '**Most popular** \u2014 combines mnemonic value with unlimited numbering'],
             ['**Decimal system (Dewey decimal)**',
              'Each digit after the decimal point denotes a finer sub-division; based on the '
              'library classification of **Melvil Dewey**', '`61.24.031`',
              'Highly logical and expandable; codes may become long'],
             ['**Universal Decimal Classification (UDC)**',
              'International extension of the Dewey system', '`615.4`',
              'Used in technical libraries and large depots'],
             ['**Brisch system**', 'Seven-digit, monocode, applied in three stages', 'See 6.5',
              'Hierarchical, British origin'],
             ['**Kodak system**', 'Ten-digit numeric code, source-of-supply oriented', 'See 6.5',
              'Developed by Eastman Kodak Co., USA'],
             ['**Colour coding**',
              'Colours (or coloured labels/stickers) identify a group, hazard, year of receipt or '
              'expiry status',
              'Gas cylinders; BMW bins; red/yellow/green expiry stickers',
              'Instantly visible; limited number of distinguishable colours'],
             ['**Bar coding / QR / 2-D DataMatrix**',
              'Machine-readable representation of the code printed on the pack',
              'GS1 GTIN + batch + expiry',
              'Fast, error-free data capture; the modern standard'],
             ['**RFID tagging**', 'Radio-frequency tag read without line of sight',
              'Tagged cold-chain boxes, equipment', 'Enables real-time tracking and '
              'temperature logging'],
             ['**Arbitrary / random system**', 'Numbers allotted arbitrarily as items arrive',
              '\u2014', 'Simple but unstructured; not recommended for large stores']])
    b.box('exam', 'MONOCODE vs POLYCODE',
          '**Monocode (hierarchical code)** — each digit\u2019s meaning **depends on the digits '
          'before it** (like Dewey, Brisch); compact and good for retrieval of groups. '
          '**Polycode (attribute/multi-code)** — each digit position denotes an **independent '
          'attribute** (size, material, colour); better for describing items fully. Many practical '
          'systems are **hybrid**.')

    # ------------------------------------------------------------------ 6.5
    b.h2('6.5', 'Standard Codification Systems — Brisch and Kodak')
    b.table(['Feature', '**Brisch system**', '**Kodak system**'],
            [['Origin', 'Developed in the **United Kingdom** by E. G. Brisch (a consulting engineer)',
              'Developed by **Eastman Kodak Company, New York, USA**'],
             ['Number of digits', '**7 digits** (all numeric)', '**10 digits** (all numeric)'],
             ['Structure', 'A **monocode** \u2014 hierarchical; applied in **3 stages**: '
              '(1) items grouped into broad preliminary categories (assemblies, sub-assemblies, '
              'components, off-the-shelf/standard items, raw material); (2) grouping within each '
              'category on the basis of function, material, type; (3) allotment of the final '
              'code number to the individual item',
              'Digits are grouped **3 + 4 + 3**; the **first digits indicate the source/mode of '
              'procurement**, the rest indicate the classification by material, function and use; '
              'materials are spread over **100 main classifications**'],
             ['Chief emphasis', 'Logical, hierarchical **grouping of similar items** so that every '
              'item has a meaningful and unique identity',
              '**Procurement orientation** \u2014 how and from where the item is bought'],
             ['Suitability', 'Engineering stores and large organisations with many components',
              'Large organisations with wide, varied purchasing']])
    b.h3('6.5.1  Steps in developing a codification system')
    b.steps([
        'Prepare a **complete inventory list** of all items actually stocked.',
        'Carry out **standardisation and variety reduction** — delete duplicates and obsolete varieties.',
        'Decide the **classification** (groups and sub-groups) and the number of levels required.',
        'Decide the **type of code** (alpha-numeric, decimal, etc.) and the **number of digits**, '
        'keeping room for expansion.',
        'Allot **group and sub-group digits**, then **serial numbers** to individual items.',
        'Prepare the **stores vocabulary / item master** with code, full description, unit of issue, '
        'storage condition and bin location.',
        'Mark the code on **bins, racks, bin cards, ledger folios and all forms**.',
        'Train the staff, and centralise the authority to **create or amend a code**.',
        '**Review periodically** — add new items, delete obsolete codes, never re-use a deleted code.',
    ])
    b.h3('6.5.2  A worked example of building a drug code')
    b.table(['Digit position', 'Meaning', 'Example value'],
            [['1\u20132  (Group)', 'Main group of stores',
              '`01` = drugs, `02` = surgicals, `03` = laboratory, `04` = X-ray'],
             ['3\u20134  (Sub-group)', 'Dosage form / category within the group',
              '`01` = tablets, `02` = capsules, `03` = injections, `04` = orals liquids'],
             ['5\u20136  (Therapeutic class)', 'Pharmacological class',
              '`07` = antibiotics, `12` = analgesics'],
             ['7\u20139  (Item serial)', 'Individual drug', '`045` = ceftriaxone'],
             ['10 (Variant)', 'Strength / pack variant', '`2` = 1 g vial']],
            caption='Table 6.1  Structure of a hierarchical (monocode) drug code')
    b.box('note', 'READING THE CODE',
          'The code **`01-03-07-045-2`** therefore reads: *drug \u2192 injection \u2192 antibiotic '
          '\u2192 ceftriaxone \u2192 1 g vial*. Notice that the code tells the store keeper where to '
          'put it, the pharmacist what it is, and the accountant which budget head to debit.')

    # ------------------------------------------------------------------ 6.6
    b.h2('6.6', 'Bar Coding and Modern Identification Technology')
    b.table(['Technology', 'Key points'],
            [['**Linear (1-D) bar code**', 'Parallel bars of varying width read by a laser scanner; '
              'holds a single number such as the **GS1 GTIN** (Global Trade Item Number, commonly '
              'a 13-digit EAN); printed on retail medicine packs'],
             ['**2-D codes (DataMatrix, QR)**',
              'Store much more data in a small area \u2014 GTIN **plus batch number, expiry date '
              'and serial number**; the basis of **track-and-trace / anti-counterfeiting** systems'],
             ['**GS1 application identifiers**', '`(01)` GTIN, `(10)` batch/lot, `(17)` expiry date, '
              '`(21)` serial number \u2014 the standard used for pharmaceutical traceability'],
             ['**RFID**', 'Radio-frequency identification tag; no line of sight needed; can be read '
              'in bulk and can log temperature \u2014 used for cold-chain boxes, high-value '
              'implants and equipment'],
             ['**Advantages of bar coding in a store**',
              'Very fast data entry \u2022 near-zero transcription error \u2022 instant batch and '
              'expiry capture \u2022 automatic FEFO enforcement \u2022 instant recall of a batch '
              '\u2022 real-time stock position \u2022 easy physical verification with hand-held '
              'scanners'],
             ['**Limitations**', 'Cost of scanners & printers \u2022 damaged/dirty labels do not '
              'scan \u2022 needs power & software \u2022 staff training \u2022 loose/repacked '
              'items must be re-labelled'],
             ['**Indian context**', 'Bar coding/track-and-trace is mandatory on exported '
              'pharmaceutical packs, and QR codes are required on the packs of specified '
              'formulations to let a buyer verify authenticity']])

    # ------------------------------------------------------------------ 6.7
    b.h2('6.7', 'Colour Coding — A Special Form of Codification')
    b.h3('6.7.1  Medical gas cylinders')
    b.table(['Gas', 'Indian standard (IS) colour', 'US (compressed gas) colour'],
            [['**Oxygen**', '**Black body with white shoulder**', 'Green'],
             ['**Nitrous oxide**', '**Blue**', 'Blue'],
             ['**Carbon dioxide**', '**Grey**', 'Grey'],
             ['**Medical air**', '**Grey body, white & black quartered shoulders**',
              'Yellow'],
             ['**Nitrogen**', '**Grey body, black shoulder**', 'Black'],
             ['**Helium**', '**Brown**', 'Brown'],
             ['**Entonox** (50 % O\u2082 + 50 % N\u2082O)',
              '**Blue body, blue & white quartered shoulders**', 'Blue/green quartered'],
             ['**Cyclopropane**', '**Orange**', 'Orange'],
             ['**Ethylene**', '**Violet**', 'Red'],
             ['**Vacuum (suction) pipeline**', '**Yellow**', 'White']],
            caption='Table 6.2  Colour coding of medical gas cylinders (Indian practice differs '
                    'from the US code \u2014 read the question carefully)')
    b.box('caution', 'EXAM TRAP',
          'In **India (IS 3933 / hospital practice) oxygen is BLACK with a WHITE shoulder**, whereas '
          'in the **USA oxygen cylinders are GREEN**. If the question says "as per Indian standard", '
          'answer *black body, white shoulder*.')
    b.h3('6.7.2  Bio-medical waste colour coding (BMW Rules, 2016)')
    b.table(['Colour of container/bag', 'What goes in it', 'Treatment & disposal'],
            [['**Yellow**', 'Human & animal anatomical waste; soiled waste; **expired, discarded '
              'and contaminated medicines**; chemical waste; **cytotoxic waste** (in a separate '
              'yellow cytotoxic bag); microbiology & laboratory waste',
              'Incineration / plasma pyrolysis / deep burial; expired medicines may also be '
              'returned to the manufacturer; **cytotoxic waste incinerated at high temperature**'],
             ['**Red**', 'Contaminated recyclable plastic \u2014 tubing, bottles, IV sets, '
              'catheters, urine bags, syringes **without needles**, gloves',
              'Autoclaving / microwaving / hydroclaving, then shredding and recycling'],
             ['**White (translucent, puncture-proof)**', '**Sharps** \u2014 needles, syringes with '
              'fixed needles, scalpels, blades',
              'Autoclave / dry heat sterilisation, then shredding or encapsulation'],
             ['**Blue (puncture-proof box/bag)**', 'Broken or discarded **glassware** including '
              'medicine vials & ampoules; metallic body implants',
              'Disinfection or autoclaving, then recycling']])
    b.h3('6.7.3  Other colour conventions used in stores')
    b.bullets([
        '**Quarantine yellow / approved green / rejected red** labels on consignments.',
        '**Expiry traffic-light stickers** — red (expires \u2264 3 months), yellow (3\u20136 months), '
        'green (> 6 months).',
        '**LASA (look-alike/sound-alike)** drugs given contrasting coloured labels and shelf '
        'separation.',
        '**High-alert drug** labels (e.g. bright orange for concentrated potassium chloride).',
        '**Year-of-receipt colour dots** — a quick visual FIFO aid on cartons.',
        '**Fire-safety and hazard labels** — inflammable, corrosive, oxidising, cytotoxic, '
        'radioactive (trefoil) symbols.',
    ])
    b.box('hy', 'CHAPTER 6 IN ONE BOX',
          bullets=['Codification = allotting a **unique symbol** to each item.',
                   '**Brisch = 7 digits, 3 stages (UK)**; **Kodak = 10 digits, 3+4+3, source-of-'
                   'supply oriented (USA)**; **Decimal = Dewey**.',
                   'Most widely used practical system = **alpha-numerical**.',
                   'A good code is unique, brief, flexible, simple, mnemonic and exhaustive.',
                   'The master list of all codes = **stores vocabulary / item master**.',
                   'India: oxygen cylinder = **black body, white shoulder**; expired medicines = '
                   '**yellow** BMW bag; sharps = **white** container.'])
    b.page_break()
