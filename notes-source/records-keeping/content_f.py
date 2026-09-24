# -*- coding: utf-8 -*-
"""Part VI — Chapter 10: Methods of storing drugs"""


def chapter10(b):
    b.part('PART VI', 'Storage of Drugs')
    b.chapter(10, 'Methods of Storing Drugs',
              'Good storage practice \u2022 systems of arrangement \u2022 storage conditions & '
              'temperature terms \u2022 cold chain \u2022 special categories \u2022 deterioration '
              '\u2022 expiry & disposal')

    b.lead('Storage has two halves: **where you put the drug (the method of arrangement)** and '
           '**under what conditions you keep it (the storage environment)**. Examiners ask both, '
           'and they love the temperature definitions, the cold chain, and the special categories. '
           'This is the longest chapter for good reason.')

    # ------------------------------------------------------------------ 10.1
    b.h2('10.1', 'Storage — Meaning and Objectives')
    b.box('def', 'STORAGE / GOOD STORAGE PRACTICE',
          '**Storage** is the holding of drugs and related materials **in such a manner and under '
          'such conditions that their identity, purity, potency, safety and quality are preserved '
          'until they are issued to the patient**. The set of rules that achieves this is called '
          '**Good Storage Practice (GSP)**, described by the WHO as part of Good Distribution '
          'Practice (GDP).')
    b.h3('10.1.1  Objectives of proper storage')
    b.numbered([
        'To **preserve the quality, potency and stability** of every drug up to its labelled expiry '
        'date.',
        'To prevent **physical damage** (breakage, crushing, leakage) and **chemical deterioration** '
        '(oxidation, hydrolysis, photolysis).',
        'To prevent **microbial contamination** of sterile and non-sterile products.',
        'To enable **quick and correct retrieval** of any item (right drug to the right patient).',
        'To prevent **expiry loss** by enforcing FEFO and near-expiry monitoring.',
        'To prevent **theft, pilferage and misuse**, especially of narcotics and costly drugs.',
        'To ensure **legal compliance** with the labelled storage conditions and with Schedule P.',
        'To ensure **safety of staff and premises** (inflammables, cytotoxics, radioactives, fire).',
        'To make the best use of **space, manpower and equipment**.',
    ])

    # ------------------------------------------------------------------ 10.2
    b.h2('10.2', 'Requirements of a Good Drug Store')
    b.table(['Requirement', 'Standard / good practice'],
            [['**Location & building**', 'Ground floor, near the receiving gate and the dispensary; '
              'dry, well-drained site; pucca, leak-proof, rodent-proof construction; separate '
              'entry and exit'],
             ['**Area / space**', 'Sufficient for present stock + expansion; separate zones for '
              'receiving, quarantine, bulk, cold chain, narcotics, inflammables, rejected stock, '
              'issue and office'],
             ['**Temperature**', 'Store generally maintained **below 25 \u00B0C** '
              '(air-conditioned or well-ventilated); **cold rooms/refrigerators at 2\u20138 '
              '\u00B0C**; deep freezer as required; temperature **recorded twice daily** with a '
              'calibrated thermometer'],
             ['**Humidity**', 'Relative humidity preferably **below 60 %**; dehumidifiers, silica '
              'gel, good ventilation; hygroscopic items in tightly closed containers'],
             ['**Light**', 'Adequate diffused illumination for reading labels; **direct sunlight '
              'excluded** (shaded/painted windows, blinds); light-sensitive drugs in amber '
              'containers/cartons'],
             ['**Ventilation**', 'Cross-ventilation and exhaust fans to prevent heat and vapour '
              'accumulation'],
             ['**Floor, walls, ceiling**', 'Smooth, crack-free, non-absorbent, easily washable; no '
              'crevices for insects; no seepage'],
             ['**Racks, shelves, pallets**', 'Metal/steel, adjustable, labelled with item name, '
              'code and bin number; stock **\u2265 30 cm from walls** and on **pallets '
              '\u2248 10 cm above the floor**; nothing directly on the floor'],
             ['**Aisles & gangways**', 'Wide enough for trolleys and for stock-taking; kept clear'],
             ['**Security**', 'Grilled windows, strong doors, single controlled entry, restricted '
              'access, locks/CCTV; **double-locked cupboard** for narcotics and a separate locked '
              'cupboard for Schedule X'],
             ['**Fire safety**', 'CO\u2082 and dry-chemical extinguishers, sand buckets, hydrants, '
              'smoke detectors, marked exits, "NO SMOKING"; inflammables in a **detached** store'],
             ['**Pest & rodent control**', 'Screened windows, rat traps/guards, periodic '
              'fumigation/pest control with records; no food or waste inside the store'],
             ['**Cleanliness & housekeeping**', 'Daily cleaning, no dust, no cobwebs, periodic '
              'defrosting of refrigerators, waste removed daily'],
             ['**Equipment**', 'Refrigerator(s), **ILR and deep freezer** with voltage stabiliser, '
              'thermometers/data loggers, weighing scale, trolleys, ladders, fire extinguishers, '
              'generator/UPS back-up for the cold chain'],
             ['**Records area**', 'Separate, secure space for registers, ledgers and the computer'],
             ['**Water & drainage**', 'Wash basin, no water lines passing over the stock, no '
              'chance of flooding']])
    b.box('hy', 'NUMBERS EXAMINERS LIKE',
          bullets=['Stock kept **at least 30 cm (1 foot) away from the wall**.',
                   'Stock kept on pallets **\u2248 10 cm above the floor** \u2014 never directly '
                   'on the floor.',
                   'General drug store temperature: **below 25 \u00B0C**; RH **below 60 %**.',
                   'Refrigerator for drugs/vaccines: **+2 to +8 \u00B0C**.',
                   'Temperature recorded **twice a day** (morning and evening) in the log.'])

    # ------------------------------------------------------------------ 10.3
    b.h2('10.3', 'Methods / Systems of Arranging Drugs in the Store')
    b.p('This is the *core* of the syllabus phrase "methods of storing drugs". Learn all the '
        'systems, their advantages and their drawbacks, and remember which is commonest.')
    b.table(['Method of arrangement', 'How it works', 'Advantages', 'Disadvantages'],
            [['**1. Alphabetical**', 'Drugs arranged A\u2013Z by **generic** (or brand) name',
              'Simplest; anyone can locate an item; no training needed; ideal for small '
              'pharmacies and retail shops',
              'Similar-sounding names come together \u2192 **LASA dispensing errors**; a name '
              'change/brand change displaces the item; no relation to storage conditions'],
             ['**2. Therapeutic / pharmacological category**',
              'Grouped by action \u2014 antibiotics, analgesics, antihypertensives\u2026 and '
              'alphabetically within each group',
              'Clinically logical; helps substitution of an equivalent drug; convenient for '
              'ward stock and formulary work',
              'Needs pharmacological knowledge; a drug with several actions is hard to place'],
             ['**3. Dosage form / route of administration**',
              'Separate racks for oral solids, orals liquids, injections, externals, ophthalmics, '
              'inhalations, suppositories',
              'Keeps liquids away from powders; heavy bottles on low shelves; suits the different '
              'storage needs of each form; **prevents the serious error of issuing an external '
              'preparation for internal use**',
              'A drug available in several forms is stored in several places'],
             ['**4. Alphabetical within dosage form** *(the commonest hospital practice)*',
              'First divide by dosage form, then arrange alphabetically inside each group',
              'Combines the advantages of methods 1 and 3; fast retrieval; widely recommended',
              'Still needs LASA precautions'],
             ['**5. Code number / classification-wise (systematic)**',
              'Items arranged in the serial order of their **store code numbers**',
              'Perfect link with bin cards, ledgers and computer records; ideal for large stores',
              'Needs a codification system and a location index; a new staff member cannot find '
              'anything without the index'],
             ['**6. Storage-condition-wise**',
              'Separate areas for room temperature, cool, cold chain, frozen, light-sensitive, '
              'inflammable, hazardous',
              '**Protects quality** \u2014 the single most important consideration for '
              'thermolabile drugs',
              'Same drug group gets scattered'],
             ['**7. Frequency of use (popularity / movement) system**',
              'Fast-moving items nearest to the issue counter, slow movers at the far end',
              'Minimises walking and handling time; based on **FSN analysis**',
              'Locations must be revised as consumption changes'],
             ['**8. Fixed location system**', 'Every item has a permanent bin address',
              'Easy to memorise; no index needed', 'Space lies idle when the item is out of stock'],
             ['**9. Random / floating location system**',
              'Item placed wherever space exists, address recorded in the index/computer',
              'Best space utilisation', 'Totally dependent on accurate records'],
             ['**10. Size / weight / volume-wise**',
              'Bulky and heavy items (IV fluids, cylinders, cartons) on the floor/lowest shelf near '
              'the entrance; small items in bins above',
              'Safety, ease of handling, prevents breakage', 'Not a complete system by itself'],
             ['**11. Manufacturer / supplier-wise**', 'All items of one firm kept together',
              'Convenient for returns and for rate-contract checking', 'Poor clinical logic; '
              'not recommended for drugs'],
             ['**12. Legal-category-wise**',
              'Narcotics, Schedule X, Schedule H/H1 kept in their prescribed separate, locked places',
              '**Legally compulsory**', 'Applies only to those categories'],
             ['**13. FIFO / FEFO arrangement (within any of the above)**',
              'Older/earlier-expiring stock in front, newer stock behind',
              '**Prevents expiry loss** \u2014 the most important day-to-day storage discipline',
              'Requires discipline at every receipt']])
    b.box('exam', 'MOST LIKELY MCQ ANSWERS',
          bullets=['Commonest/most convenient system in a hospital drug store \u2014 '
                   '**dosage-form-wise, alphabetically within each form**.',
                   'System best suited to a large store with codification \u2014 **code-number '
                   '(systematic) arrangement**.',
                   'System that gives the best space utilisation \u2014 **random/floating location**.',
                   'System based on rate of movement \u2014 **frequency-of-use (FSN) system**.',
                   'The principle that prevents expiry \u2014 **FEFO (first expiry first out)**.'])
    b.h3('10.3.1  FIFO and FEFO in practice')
    b.bullets([
        'New stock is **always placed behind (or below)** the existing stock; issue is from the front.',
        'The **expiry date is written boldly** on the carton/shelf label and on the bin card.',
        'When a new receipt has an **earlier expiry** than the existing stock, it is placed **in '
        'front** — that is the difference between FIFO and **FEFO**.',
        'A **monthly near-expiry list** is generated and colour stickers applied '
        '(traffic-light system).',
        'Bar-code/software systems can enforce FEFO automatically by prompting the batch to be '
        'picked.',
    ])

    # ------------------------------------------------------------------ 10.4
    b.h2('10.4', 'Storage Conditions and Temperature Terminology')
    b.p('The label of every medicine states the condition under which it must be kept. The words '
        'used on the label have **precise, defined meanings** — these definitions are among the '
        'most frequently asked objective questions in pharmacy examinations.')
    b.table(['Term on the label', 'Indian Pharmacopoeia (IP) / WHO', 'USP (for comparison)'],
            [['**Freezer / store frozen**', 'Below \u2212 **18 to \u221220 \u00B0C** (deep freezer)',
              '\u221225 \u00B0C to \u221210 \u00B0C'],
             ['**Cold place**', '**A temperature not exceeding 8 \u00B0C**',
              'Any temperature not exceeding 8 \u00B0C'],
             ['**Refrigerator**', '**2 \u00B0C to 8 \u00B0C**', '2 \u00B0C to 8 \u00B0C'],
             ['**Cool place**', '**8 \u00B0C to 25 \u00B0C**', '8 \u00B0C to 15 \u00B0C'],
             ['**Room temperature**', 'The temperature prevailing in a working area; commonly taken '
              'as **15\u201330 \u00B0C** (WHO: 15\u201325 \u00B0C)',
              'The temperature prevailing in a working area'],
             ['**Controlled room temperature**', 'Usually **20\u201325 \u00B0C**, excursions '
              'permitted between 15 and 30 \u00B0C',
              '20\u201325 \u00B0C, allowed excursions 15\u201330 \u00B0C'],
             ['**Warm**', '**30 \u00B0C to 40 \u00B0C**', '30 \u00B0C to 40 \u00B0C'],
             ['**Excessive heat**', '**Above 40 \u00B0C**', 'Above 40 \u00B0C'],
             ['**Protect from freezing**', 'Must not be frozen — freezing damages the product '
              '(e.g. **DPT, Hep-B, Td, insulin**) even though it is stored cold', 'Same'],
             ['**Store below 30 \u00B0C / below 25 \u00B0C**',
              'The stated maximum must never be exceeded', 'Same'],
             ['**Protect from light**', 'Keep in an amber/opaque container or in its carton, away '
              'from sunlight and UV', 'Same'],
             ['**Protect from moisture**', 'Tightly closed container, desiccant, low humidity', 'Same'],
             ['**Dry place**', 'Relative humidity preferably below 60 %', 'Same']],
            caption='Table 10.1  Defined storage terms (the IP/WHO column is the one to quote in '
                    'an Indian examination)')
    b.box('caution', 'THE CLASSIC TRAP',
          '**"Cool place" is NOT the refrigerator.** In the **Indian Pharmacopoeia a cool place is '
          '8\u201325 \u00B0C**, whereas a **cold place is not exceeding 8 \u00B0C** and a '
          '**refrigerator is 2\u20138 \u00B0C**. (In the USP, "cool" is the narrower 8\u201315 '
          '\u00B0C.) Also remember: **Schedule P of the Drugs and Cosmetics Rules prescribes the '
          'life period and storage conditions of drugs.**')
    b.h3('10.4.1  Types of containers and closures (storage-related)')
    b.table(['Container', 'Meaning / use'],
            [['**Well-closed container**', 'Protects the contents from **extraneous solids** and '
              'from loss during handling'],
             ['**Tightly closed container**', 'Protects from extraneous solids, **liquids and '
              'vapours (moisture)**, and from loss, efflorescence, deliquescence or evaporation'],
             ['**Hermetically sealed container**', '**Impervious to air or any other gas** '
              '(e.g. sealed glass ampoule) \u2014 used for sterile products'],
             ['**Light-resistant container**', 'Amber/opaque glass or an opaque outer wrapper, '
              'protecting light-sensitive drugs'],
             ['**Single-dose / multi-dose container**', 'Ampoule vs multi-dose vial (which needs a '
              'preservative and a limited in-use shelf life)'],
             ['**Tamper-evident / child-resistant closure**',
              'Safety and evidence of interference']])

    # ------------------------------------------------------------------ 10.5
    b.h2('10.5', 'The Cold Chain')
    b.box('def', 'COLD CHAIN',
          'The **cold chain** is the **system of people, equipment and procedures that keeps '
          'thermolabile products (vaccines, sera, insulin, oxytocin, blood products) continuously '
          'within their prescribed temperature range \u2014 usually +2 to +8 \u00B0C \u2014 from '
          'the manufacturer right up to the patient**.')
    b.table(['Equipment', 'Purpose / temperature'],
            [['**Walk-in cooler (WIC)**', 'Bulk storage at **+2 to +8 \u00B0C** at regional/state level'],
             ['**Walk-in freezer (WIF)**', 'Bulk storage of frozen items / ice packs at '
              '**\u221215 to \u221225 \u00B0C**'],
             ['**ILR (Ice-Lined Refrigerator)**', 'Keeps vaccines at **+2 to +8 \u00B0C** and holds '
              'the temperature for many hours during power failure because of the lining of '
              'ice packs; **top-opening** design retains cold air'],
             ['**Deep freezer (DF)**', 'For **freezing ice packs** and storing OPV and other '
              'freeze-safe vaccines at **\u221215 to \u221225 \u00B0C**'],
             ['**Domestic refrigerator**', 'Acceptable only in small units; vaccines kept in the '
              'body of the fridge, **never in the door shelves or freezer compartment**'],
             ['**Cold box**', 'Insulated box with ice packs for transporting vaccines over longer '
              'distances (holds cold for days)'],
             ['**Vaccine carrier**', 'Small insulated carrier with 4 ice packs for daily field '
              'sessions (holds cold for several hours)'],
             ['**Ice packs / conditioned ice packs**',
              'Frozen water packs; **conditioning** (leaving them out until water begins to '
              'appear) prevents freezing of freeze-sensitive vaccines'],
             ['**Thermometer / dial thermometer / data logger**',
              'Continuous record of temperature; readings noted **twice daily** on the log chart'],
             ['**Vaccine Vial Monitor (VVM)**', 'Heat-sensitive square on the vial label: as heat '
              'exposure accumulates the **inner square darkens**. **Usable while the inner square '
              'is lighter than the outer ring (stages 1\u20132); discard at stage 3\u20134** when '
              'it matches or is darker than the ring'],
             ['**Cold Chain Monitor (CCM) card / freeze indicator (Freeze-tag)**',
              'Shows whether the consignment has been exposed to heat or to freezing during transit'],
             ['**Voltage stabiliser, generator/solar back-up**',
              'Protects the equipment and the chain during power fluctuation and failure']])
    b.h3('10.5.1  Freeze-sensitive vs heat-sensitive vaccines')
    b.table(['Group', 'Examples', 'Rule'],
            [['**Most freeze-sensitive** (damaged by freezing \u2014 never put in the freezer or '
              'against ice packs)',
              'DPT, DT, Td, TT, Hepatitis B, Pentavalent, IPV, Rabies, Typhoid, JE (killed), '
              '**Insulin**', 'Store at **+2 to +8 \u00B0C**; "**do not freeze**"; discard if frozen '
              '(shake test for adsorbed vaccines)'],
             ['**Most heat-sensitive** (damaged by heat, tolerate freezing)',
              'OPV (most heat-sensitive of all), Measles, MR/MMR, BCG',
              'May be stored in the **freezer/coldest part**; protect from heat and light'],
             ['**Diluents**', 'Diluents of BCG, Measles, MMR',
              'Never frozen; must be **cooled to +2 to +8 \u00B0C before reconstitution**; use only '
              'the diluent supplied by the same manufacturer']])
    b.h3('10.5.2  Cold-chain do\u2019s and don\u2019ts')
    b.bullets([
        '**Do** record temperature **twice daily** (morning & evening) on the log chart, including '
        'holidays; plot it.',
        '**Do** keep the ILR/refrigerator **away from direct sunlight and at least 10 cm from the '
        'wall**, on a level base, in a ventilated room.',
        '**Do** keep vaccines in the **basket/body of the ILR**, arranged with space for air '
        'circulation, earliest expiry on top.',
        '**Do** defrost regularly (frost > 5 mm reduces efficiency) and keep a **spare set of ice '
        'packs frozen** for emergencies.',
        '**Do** use the **shake test** if a freeze-sensitive vaccine is suspected to have frozen — '
        'a frozen-and-thawed vial shows rapid sedimentation and flakes; it must be discarded.',
        '**Don\u2019t** store food, drinks or laboratory specimens in the vaccine refrigerator.',
        '**Don\u2019t** keep vaccines in the **door shelves** of a domestic refrigerator '
        '(temperature fluctuates most there).',
        '**Don\u2019t** open the ILR unnecessarily, and never leave it open.',
        '**Don\u2019t** use a vaccine whose **VVM has reached stage 3 or 4**, or which has passed '
        'its expiry date, or a reconstituted vaccine beyond the permitted hours.',
        '**Don\u2019t** refreeze thawed ice packs together with freeze-sensitive vaccine without '
        '**conditioning** them first.',
        '**Do** have a written **power-failure/breakdown SOP**: do not open the ILR, arrange a '
        'generator, shift stock to a cold box, record the excursion and take a decision on '
        'usability in consultation with the manufacturer/authority.',
    ])

    # ------------------------------------------------------------------ 10.6
    b.h2('10.6', 'Storage of Special Categories of Drugs')
    b.table(['Category', 'Method of storage \u2014 key points'],
            [['**Narcotics & psychotropics (NDPS Act)**',
              'In a **substantial, locked steel cupboard or safe, embedded in a wall or fixed to '
              'the floor, with a double lock**; keys in the **personal custody of a named officer**; '
              'stock physically **tallied daily/at each shift change**; entries in the **NDPS/DDA '
              'register the same day**, countersigned; **no other article kept in the cupboard**; '
              'loss/theft reported immediately; destruction only in the presence of the authorised '
              'officers with a certificate'],
             ['**Schedule X (habit-forming) drugs**',
              'Separate **locked cupboard** (apart from other stock), special licence (Form 20F '
              'retail / 20G wholesale, applied for in Form 19C), prescription retained **in '
              'duplicate**, separate register, records preserved for the prescribed period '
              '(**2 years**)'],
             ['**Schedule H / H1 drugs**',
              'Stored with the general stock but **sold/issued only against a prescription**; the '
              '**H1 register** (patient, prescriber, drug, quantity, date) maintained and preserved '
              'for **3 years**'],
             ['**Thermolabile drugs (vaccines, sera, insulin, oxytocin, some eye drops, '
              'suppositories, probiotics)**',
              '**+2 to +8 \u00B0C** in a refrigerator/ILR with a twice-daily temperature log; '
              '**never frozen** unless the label permits; transported in a cold box/vaccine carrier'],
             ['**Blood and blood components**',
              'Whole blood & packed red cells **+2 to +6 \u00B0C** in a blood-bank refrigerator '
              'with an alarm; **platelets +20 to +24 \u00B0C with continuous gentle agitation**; '
              '**fresh frozen plasma at \u221230 \u00B0C or below**; never stored in an ordinary '
              'refrigerator'],
             ['**Light-sensitive drugs** (e.g. vitamin A & D, riboflavin, chlorpromazine, '
              'nitroprusside, furosemide, adrenaline, silver salts, phenothiazines)',
              '**Amber/opaque containers**, kept inside the outer carton, away from sunlight and '
              'fluorescent UV; do not transfer to clear containers'],
             ['**Moisture-sensitive / hygroscopic & deliquescent drugs** (e.g. effervescent '
              'granules, aspirin, dispersible tablets, calcium chloride, KOH, NaOH, glycerin)',
              '**Tightly closed containers** with a **desiccant (silica gel)**, in a dry place with '
              'RH < 60 %; strips/blisters not broken until issue'],
             ['**Volatile & inflammable liquids** (ether, spirit, acetone, alcohol, chloroform, '
              'petrol)',
              '**Detached, well-ventilated, fire-resistant store** away from the main building; '
              '**cool place, away from heat and flame**; flame-proof electrical fittings; '
              '"NO SMOKING"; CO\u2082/dry-powder extinguishers, sand buckets; small quantities '
              'only in the working area; **rectified spirit also in the excise-bonded store with '
              'its register**'],
             ['**Corrosives and hazardous chemicals** (strong acids, alkalis, phenol)',
              'On **low shelves in trays**, never above eye level; acids away from alkalis and from '
              'oxidising agents; PPE, eye-wash and spill kit available; MSDS on file'],
             ['**Cytotoxic / anticancer drugs**',
              'Segregated, clearly labelled **"CYTOTOXIC \u2014 HANDLE WITH CARE"** area or '
              'cupboard; stored at the labelled temperature; kept in a tray/secondary container to '
              'contain spillage; **spill kit and PPE** nearby; reconstitution only in a '
              'biological safety cabinet; waste in **yellow cytotoxic bags**'],
             ['**Radiopharmaceuticals**',
              '**Lead-lined containers inside a lead-shielded room/safe** in a restricted area with '
              'the **radiation trefoil** sign; handled only by authorised persons; radiation '
              'survey and log-book maintained as per **AERB** requirements; decay storage before '
              'disposal'],
             ['**Medical gas cylinders**',
              'Stored **upright, chained/secured**, in a cool, dry, well-ventilated, fire-free '
              'area; **full and empty cylinders kept separately and labelled**; valve caps in '
              'place; **never oiled or greased** (oxygen + oil = fire risk); not rolled or dropped; '
              'colour code verified; kept away from inflammables'],
             ['**LASA (look-alike, sound-alike) drugs**',
              '**Never stored side by side**; separated physically, with **bold/contrasting labels, '
              '"tall-man lettering"** and LASA stickers; a LASA list is displayed'],
             ['**High-alert / high-risk drugs** (concentrated KCl, heparin, insulin, '
              'neuromuscular blockers, concentrated electrolytes)',
              'Stored in a **separate, clearly marked location with a warning label**; quantity in '
              'ward stock restricted; double-check at issue'],
             ['**Antiseptics & disinfectants**',
              'Stored **away from internal medicines** (a favourite examination point) in a cool '
              'place; original labelled containers only; never decanted into medicine bottles'],
             ['**Sutures & sterile disposables**',
              'Dust-free, dry, cool place; **cartons not crushed**; sterility date and pack '
              'integrity checked; FEFO strictly'],
             ['**X-ray films**',
              'Cool, dry place, **away from radiation, chemicals and heat**; boxes stored '
              '**vertically (on edge)** to avoid pressure marks; expiry monitored'],
             ['**Diagnostic reagents & test kits**',
              'Mostly **2\u20138 \u00B0C**; protected from light; in-use stability noted'],
             ['**IV fluids & large-volume parenterals**',
              'On **pallets on the lowest shelf/floor level** (heavy); protected from freezing and '
              'from direct sun; checked for clarity, leakage and particulate matter before issue'],
             ['**Ayurvedic / homoeopathic medicines**',
              'Stored **separately** from allopathic drugs; homoeopathic preparations kept away '
              'from strong odours, camphor and direct sunlight'],
             ['**Expired, recalled and rejected stock**',
              '**Separate, locked, red-labelled area**, physically apart from live stock, pending '
              'return or destruction']])
    b.box('mnem', 'MNEMONIC for special storage',
          '**"N-X-T-B-L-M-V-C-C-R-G-L-H"** \u2014 **N**arcotics, Schedule **X**, **T**hermolabile, '
          '**B**lood, **L**ight-sensitive, **M**oisture-sensitive, **V**olatile/inflammable, '
          '**C**orrosives, **C**ytotoxics, **R**adiopharmaceuticals, **G**ases, **L**ASA, '
          '**H**igh-alert.')

    # ------------------------------------------------------------------ 10.7
    b.h2('10.7', 'Deterioration of Drugs — Causes and Signs')
    b.h3('10.7.1  Factors causing deterioration')
    b.table(['Factor', 'Mechanism', 'Examples / prevention'],
            [['**Heat / temperature**', 'Accelerates hydrolysis, oxidation and loss of potency '
              '(rate of reaction roughly doubles for every 10 \u00B0C rise)',
              'Vaccines, insulin, suppositories, antibiotics in syrup; prevent by cold chain and '
              'a cool store'],
             ['**Moisture / humidity**', 'Hydrolysis, caking, softening, microbial growth',
              'Aspirin, effervescent salts, dispersible tablets, capsules; tightly closed '
              'containers + desiccant'],
             ['**Light (especially UV)**', 'Photolysis and oxidation',
              'Vitamin A, riboflavin, chlorpromazine, adrenaline, sodium nitroprusside; '
              'amber containers, cartons'],
             ['**Air / oxygen**', 'Oxidation, rancidity of oils',
              'Oils, fats, vitamins, adrenaline; hermetic or tightly closed containers, '
              'antioxidants, nitrogen filling'],
             ['**Microbial contamination**', 'Spoilage, loss of sterility',
              'Syrups, creams, eye drops; preservatives, sterile technique, intact seals'],
             ['**pH and chemical interaction**', 'Degradation, incompatibility',
              'Buffered formulations; do not store acids with alkalis'],
             ['**Packaging failure / leaching**', 'Interaction between drug and container, leakage',
              'Use the specified container; reject leaking packs'],
             ['**Time (age)**', 'Natural degradation up to and beyond the expiry date',
              'FEFO, near-expiry monitoring'],
             ['**Physical stress / rough handling**', 'Breakage, powdering, crushing of tablets',
              'Careful handling, no over-stacking'],
             ['**Pests, rodents and insects**', 'Contamination and physical destruction',
              'Pest control, rodent-proofing, screens']])
    b.h3('10.7.2  Signs of deterioration by dosage form')
    b.table(['Dosage form', 'Signs that the product must not be used'],
            [['**Tablets**', 'Discolouration, mottling, spots, chips or cracks, swelling, softening, '
              'stickiness, unusual smell (e.g. vinegar smell of degraded aspirin), loss of coating, '
              'crumbling'],
             ['**Capsules**', 'Softening, sticking together, hardening/brittleness, leakage, '
              'swelling, discolouration of the shell'],
             ['**Powders / granules**', 'Caking, hardening, clumping, discolouration, damp lumps'],
             ['**Syrups & elixirs**', 'Cloudiness, crystallisation, mould growth, change of colour '
              'or taste, gas formation, broken seal'],
             ['**Suspensions**', 'Caking that does not redisperse on shaking, large crystals, '
              'colour change'],
             ['**Emulsions**', 'Separation/cracking of phases that does not re-emulsify, rancid smell'],
             ['**Injections / ampoules & vials**', '**Any turbidity, precipitate, particulate '
              'matter, discolouration, leakage, cracked ampoule, loose/bulging rubber closure, '
              'broken tamper seal** \u2014 discard'],
             ['**IV fluids**', 'Cloudiness, floating particles, leakage from the bag/bottle, '
              'damaged port'],
             ['**Ointments & creams**', 'Separation of oil, change of colour or smell, granular or '
              'gritty texture, drying/hardening'],
             ['**Eye/ear drops**', 'Turbidity, particles, discolouration, broken seal, exceeding '
              'the in-use period (usually **28 days** after opening for a multi-dose preservative '
              'containing eye drop)'],
             ['**Suppositories & pessaries**', 'Softening, melting, deformation, mould'],
             ['**Vaccines**', 'VVM stage 3/4, frozen appearance of an adsorbed vaccine, flakes on '
              'shake test, expiry crossed'],
             ['**Effervescent tablets/powders**', 'Loss of effervescence, swollen strip/tube, '
              'dampness']])

    # ------------------------------------------------------------------ 10.8
    b.h2('10.8', 'Shelf Life, Expiry Date and Near-Expiry Management')
    b.kv([
        ('Shelf life (life period)', 'The period during which a drug, if stored under the labelled '
                                     'conditions, retains at least the specified percentage '
                                     '(generally **not less than 90 %**) of its labelled potency '
                                     'and remains within all other specifications. Prescribed for '
                                     'various classes in **Schedule P** of the Drugs and Cosmetics '
                                     'Rules.'),
        ('Expiry date', 'The date up to and including which the product is expected to comply with '
                        'specifications **if stored correctly**. If only month and year are given, '
                        'the drug is usable up to the **last day of that month**.'),
        ('Date of manufacture', 'The date on which the manufacturing process was completed; '
                                'the shelf life is counted from it.'),
        ('Retest date', 'Used mainly for active raw materials \u2014 the date on which the material '
                        'must be re-analysed to confirm it is still fit for use.'),
        ('Beyond-use date (BUD) / in-use shelf life', 'The date after which a product **that has '
                                                      'been opened, reconstituted or diluted** must '
                                                      'not be used (e.g. reconstituted antibiotic '
                                                      'syrup 7\u201314 days refrigerated; opened '
                                                      'multi-dose eye drop 28 days; reconstituted '
                                                      'vaccine a few hours).'),
        ('Near-expiry', 'Conventionally stock expiring within the next **3\u20136 months**; it is '
                        'listed monthly, colour-tagged and redistributed or returned.'),
    ])
    b.h3('10.8.1  Managing near-expiry and expired stock')
    b.steps([
        'Generate the **near-expiry statement monthly** from the batch/expiry register or software.',
        'Apply **traffic-light stickers** (red \u2264 3 months, yellow 3\u20136 months, green '
        '> 6 months).',
        '**Redistribute** to high-consumption wards or other institutions, or **return to the '
        'supplier** under the buy-back/replacement clause of the purchase order.',
        'On expiry, **remove from the shelf the same day**, enter in the **expiry register**, and '
        'move to the **locked, red-labelled expired-stock area**.',
        'Obtain **write-off sanction** and deduct from the stock register quoting the sanction.',
        'Dispose of as **bio-medical waste (yellow category)** through the authorised common '
        'treatment facility, or return to the manufacturer; obtain and file the '
        '**destruction certificate**.',
        'Analyse the **cause of expiry** (over-indenting, short-expiry acceptance, change of '
        'prescribing, poor FEFO) and correct it in the next indent.',
    ])
    b.table(['Method of disposal of expired/unwanted drugs', 'Suitability'],
            [['**Return to the manufacturer/supplier**', 'The best option where the contract permits'],
             ['**High-temperature incineration (\u2265 1,200 \u00B0C)**',
              'Cytotoxics, controlled substances, most solid dosage forms'],
             ['**Encapsulation**', 'Sealing drugs in a steel drum with cement/plastic foam before '
              'landfill'],
             ['**Inertisation**', 'Grinding and mixing with cement, lime and water, then landfill'],
             ['**Engineered/sanitary landfill**', 'Small quantities of non-hazardous solids'],
             ['**Sewer / dilution and flushing**',
              'Only small quantities of harmless liquids (e.g. dilute syrups, IV fluids) with '
              'plenty of water; **never for antibiotics or cytotoxics**'],
             ['**Waste immobilisation / deep burial**',
              'Permitted in specified situations under the Bio-Medical Waste Rules'],
             ['**Destruction before the prescribed authority**',
              '**Compulsory for narcotics and psychotropics** \u2014 in the presence of the '
              'authorised officer(s), with a certificate of destruction']])
    b.box('caution', 'ABSOLUTE RULES',
          bullets=['**Expired drugs must never be dispensed, sold, donated or kept with live stock** '
                   '\u2014 it is an offence under the Drugs and Cosmetics Act.',
                   '**Cytotoxic waste must not be landfilled or discharged into a drain** \u2014 '
                   'incineration at high temperature only.',
                   '**Narcotics cannot be destroyed by the store** \u2014 only by/before the '
                   'authority prescribed under the NDPS Rules, with a certificate.',
                   'Antibiotics must **not** be flushed into the sewer (antimicrobial resistance).'])

    # ------------------------------------------------------------------ 10.9
    b.h2('10.9', 'Housekeeping, Pest Control, Fire and Security in the Store')
    b.bullets([
        '**Daily** sweeping/mopping, dusting of racks, removal of waste and empty cartons; no food '
        'or personal articles in the store.',
        '**Weekly/monthly** deep cleaning, defrosting of refrigerators, checking of expiry stickers '
        'and of the near-expiry list.',
        '**Pest control** — screened windows and doors, rodent guards and traps, periodic '
        'professional pest control with a **record of date, agent used and area treated**; '
        'insecticides stored away from drugs.',
        '**Fire safety** — appropriate extinguishers (CO\u2082/dry powder for electrical and '
        'inflammable fires), sand buckets, water hydrant, smoke detectors, marked and unobstructed '
        'exits, a displayed **evacuation plan**, staff trained in drills, "NO SMOKING" boards.',
        '**Electrical safety** — no overloading, earthed equipment, voltage stabilisers, periodic '
        'inspection; flame-proof fittings in the inflammable store.',
        '**Security** — single controlled entry, restricted access, key register, locks on narcotic '
        'and Schedule X cupboards, CCTV, night watchman, gate pass for material leaving the premises.',
        '**Documentation of housekeeping** — cleaning checklist, pest-control record, temperature '
        'and humidity log, equipment maintenance register: an accreditation team looks for exactly '
        'these papers.',
    ])

    # ------------------------------------------------------------------ 10.10
    b.h2('10.10', 'Storage at the Ward / Sub-Store Level')
    b.bullets([
        'Ward stock kept in a **locked medicine cupboard/trolley**, with the ward register and the '
        'imprest scale displayed.',
        'A **refrigerator with a temperature log** for thermolabile drugs; **no food** in it.',
        '**Narcotics** in a double-locked box within the ward cupboard, with the ward narcotic '
        'register and shift-wise tally.',
        '**Emergency (crash) trolley** — a fixed list of drugs, sealed, checked and signed '
        '**every shift/daily** for completeness and expiry, re-sealed after use.',
        '**LASA and high-alert drugs** separated and labelled; concentrated electrolytes not kept '
        'loose in the ward.',
        '**FEFO** followed; near-expiry items returned to the main store in time.',
        'Periodic **ward stock inspection by the pharmacist** with a written report: expiry, '
        'storage condition, unauthorised accumulation, register accuracy.',
    ])
    b.box('hy', 'CHAPTER 10 \u2014 RAPID RECALL',
          bullets=['Commonest arrangement in a hospital store: **dosage-form-wise, then alphabetical**.',
                   '**IP: cold place \u2264 8 \u00B0C \u2022 refrigerator 2\u20138 \u00B0C \u2022 '
                   'cool place 8\u201325 \u00B0C \u2022 warm 30\u201340 \u00B0C \u2022 excessive '
                   'heat > 40 \u00B0C.**',
                   '**Schedule P** = life period & storage conditions; **Schedule N** = minimum '
                   'equipment for a pharmacy.',
                   'Cold chain = **+2 to +8 \u00B0C**; **ILR** for vaccines; **deep freezer** for '
                   'ice packs & OPV; **VVM** shows heat exposure.',
                   'Freeze-sensitive: **DPT, TT/Td, Hep-B, IPV, Pentavalent, insulin**. '
                   'Heat-sensitive: **OPV (most), measles, BCG**.',
                   'Blood **2\u20136 \u00B0C**; platelets **20\u201324 \u00B0C with agitation**; '
                   'FFP **below \u221230 \u00B0C**.',
                   'Stock **30 cm from the wall, 10 cm off the floor**; store below **25 \u00B0C**, '
                   'RH below **60 %**.',
                   'Narcotics: **double-locked cupboard, daily tally, NDPS register**; '
                   'Schedule X: **separate locked cupboard, duplicate prescription**.',
                   'Expired medicines \u2192 **yellow** BMW category; cytotoxic waste \u2192 '
                   '**incineration**.'])
    b.page_break()
