"""
content_part2.py  -  PART II : STERILIZATION AND DISINFECTION
Chapters 10-17 of the JKSSB Junior Pharmacist notes.
"""

from docx_style import (
    BLUE, GREEN, MAROON, NAVY, ORANGE, PURPLE, TEAL,
    SH_BAND, SH_BAND_GREEN, SH_HEADER_BLUE, SH_HEADER_GREEN,
    SH_HEADER_PURPLE, SH_HEADER_TEAL,
    box, bullet, bullets, chapter_end, chapter_title, defn, h2, h3, h4,
    numbered, para, part_title, rule, table,
)
from docx.shared import Pt


# ===========================================================================
# CHAPTER 10
# ===========================================================================
def chapter_10(doc):
    chapter_title(doc, 10, "Fundamentals and Terminology of Sterilization and Disinfection")

    para(doc, "Every question in this unit ultimately tests one of three things: "
              "**a definition**, **a temperature\u2013time combination**, or **which method "
              "is used for which article**. This chapter fixes the definitions; the "
              "following chapters supply the rest.")

    h2(doc, "10.1  The Essential Definitions")
    table(doc,
          ["Term", "Definition", "Key discriminator"],
          [["**Sterilization**",
            "The process by which **all forms of microbial life \u2014 including bacterial "
            "and fungal spores, vegetative bacteria, viruses and prions \u2014 are "
            "completely destroyed or removed** from an article.",
            "**Absolute term.** There is no such thing as 'partially sterile'. "
            "^^Spores must be killed.^^"],
           ["**Disinfection**",
            "The destruction or removal of **pathogenic (vegetative) organisms** capable of "
            "causing infection; **spores are not necessarily destroyed**.",
            "**Relative term.** Applied to **inanimate objects**."],
           ["**Antisepsis**",
            "The prevention of infection by destroying or inhibiting the growth of "
            "micro-organisms **on living tissues** \u2014 skin, mucous membranes, wounds.",
            "Applied to **living tissue**; an agent so used is an **antiseptic**."],
           ["**Disinfectant**",
            "A chemical (germicide) used on **inanimate surfaces and objects** to destroy "
            "pathogens; usually too toxic or irritant for living tissue.",
            "Object \u2192 disinfectant."],
           ["**Antiseptic**",
            "A chemical applied to **living tissue** that destroys or inhibits "
            "micro-organisms.",
            "Skin/wound \u2192 antiseptic. Some agents (e.g. 70% alcohol, povidone-iodine) "
            "serve both roles at different concentrations."],
           ["**Sanitization**",
            "Reduction of the microbial population on an inanimate surface to a level "
            "judged **safe by public health standards** \u2014 it does not imply "
            "sterility.",
            "Used for eating utensils, dairy and food equipment."],
           ["**Decontamination**",
            "Any process that removes or reduces contamination so that an article is "
            "**safe to handle**; the first step before cleaning and sterilization.",
            "Protects the **handler**, not the patient."],
           ["**Cleaning**",
            "Physical removal of visible soil, organic matter and micro-organisms by water, "
            "detergent and mechanical action.",
            "**Cleaning must always precede disinfection or sterilization** \u2014 no "
            "sterilant works reliably through dirt."],
           ["**Asepsis**",
            "The absence of pathogenic organisms; the set of practices that **prevents "
            "micro-organisms from reaching** the tissue or article.",
            "**Aseptic technique**; contrast with antisepsis, which destroys organisms "
            "already present."],
           ["**Sterilant / chemisterilant**",
            "A chemical agent capable of producing **complete sterilization**, including "
            "the killing of spores.",
            "Examples: ethylene oxide, glutaraldehyde (long contact), peracetic acid, "
            "formaldehyde gas, hydrogen peroxide plasma, beta-propiolactone."],
           ["**Germicide / microbicide**",
            "Any agent that destroys micro-organisms; the suffix names the target \u2014 "
            "**bactericide, virucide, fungicide, sporicide, tuberculocide, "
            "amoebicide**.",
            "**-cidal** = kills; **-static** = inhibits multiplication without killing "
            "(bacteriostatic, fungistatic, sporostatic)."],
           ["**Fumigation**",
            "Disinfection of an enclosed space, air and surfaces by exposure to a gas or "
            "vapour.",
            "Classic agent: **formaldehyde vapour** for the operation theatre."],
           ["**Preservative**",
            "A substance added to a product to **prevent microbial spoilage or growth** "
            "during storage and use.",
            "Examples: benzoic acid, benzalkonium chloride, chlorocresol, thiomersal, "
            "parabens in pharmaceuticals and multi-dose vials."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 10.1  Core terminology")

    box(doc, "highyield",
        ["^^Sterilization kills spores; disinfection does not.^^ This is the single "
         "commonest MCQ in the whole unit.",
         "**Disinfectant \u2192 inanimate objects; Antiseptic \u2192 living tissue.**",
         "**Boiling is NOT sterilization** (spores survive) \u2014 it is high-level "
         "disinfection. Similarly **pasteurisation is not sterilization**."])

    h2(doc, "10.2  Types and Levels of Disinfection")
    table(doc,
          ["Classification", "Description", "Examples"],
          [["**Concurrent disinfection**",
            "Immediate disinfection of infectious discharges and contaminated articles "
            "**while the patient is still the source of infection**.",
            "Disinfection of a tuberculosis patient's sputum, or of a cholera patient's "
            "stool, as they are produced."],
           ["**Terminal disinfection**",
            "Disinfection carried out **after the patient has been removed** \u2014 by "
            "death, discharge or recovery \u2014 or after he has ceased to be a source.",
            "Cleaning and disinfecting the bed, locker, linen, mattress and room after "
            "discharge; fumigation of an isolation room."],
           ["**Prophylactic (pre-current) disinfection**",
            "Disinfection done in **anticipation** of infection, as a routine preventive "
            "measure.",
            "Chlorination of drinking water, pasteurisation of milk, antiseptic preparation "
            "of the skin before injection or surgery."]],
          header_fill=SH_HEADER_TEAL)

    h3(doc, "10.2.1  Spaulding Classification of Instruments and the Level of Processing")
    table(doc,
          ["Category", "Definition", "Processing required", "Examples"],
          [["**Critical**",
            "Items that enter **sterile tissue, the vascular system or sterile body "
            "cavities**. Any contamination carries a high risk of infection.",
            "**STERILIZATION** \u2014 steam under pressure, dry heat, ethylene oxide, "
            "hydrogen peroxide plasma, or a chemical sterilant with prolonged contact.",
            "Surgical instruments, needles and syringes, implants, cardiac and urinary "
            "catheters, dental hand-pieces, arthroscopes and laparoscopes, "
            "intra-uterine devices."],
           ["**Semi-critical**",
            "Items that contact **intact mucous membranes or non-intact skin** but do not "
            "penetrate sterile tissue.",
            "**HIGH-LEVEL DISINFECTION (HLD)** as a minimum \u2014 kills all organisms "
            "except large numbers of bacterial spores.",
            "Flexible endoscopes (gastroscope, colonoscope, bronchoscope), laryngoscope "
            "blades, respiratory therapy and anaesthesia equipment, oesophageal manometry "
            "probes, vaginal specula, thermometers."],
           ["**Non-critical**",
            "Items that contact **intact skin only**, or do not touch the patient at all.",
            "**LOW-LEVEL DISINFECTION** or simple cleaning with detergent and water.",
            "Blood-pressure cuff, stethoscope, bed-pan, crutches, bed rails, linen, "
            "furniture, floors, walls, patient trolley."]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 10.2  Spaulding classification (1957/1968)")

    table(doc,
          ["Level of disinfection", "Kills", "Does not reliably kill", "Typical agents"],
          [["**High (HLD)**",
            "Vegetative bacteria, **mycobacteria**, fungi, all viruses (lipid and non-lipid), "
            "and some spores",
            "**Large numbers of bacterial spores**",
            "2% glutaraldehyde (20\u201345 min), 0.55% ortho-phthalaldehyde, 6\u20137.5% "
            "hydrogen peroxide, 0.2% peracetic acid, pasteurisation at 75 \u00b0C, "
            "\u2265 1000 ppm free chlorine"],
           ["**Intermediate**",
            "Vegetative bacteria, **mycobacteria** (tuberculocidal), most viruses, most "
            "fungi",
            "Bacterial spores",
            "70\u201390% alcohols, phenolics, iodophors, chlorine compounds "
            "(\u2248 500 ppm), some quaternary compounds with alcohol"],
           ["**Low**",
            "Most vegetative bacteria, some fungi, **lipid (enveloped) viruses** "
            "such as HIV, HBV and influenza",
            "**Mycobacteria, spores, non-lipid (non-enveloped) viruses** such as polio and "
            "norovirus",
            "Quaternary ammonium compounds, 3% hydrogen peroxide (surfaces), low-strength "
            "phenolics, detergents"]],
          header_fill=SH_HEADER_PURPLE,
          caption="Table 10.3  Levels of disinfection")

    h2(doc, "10.3  Order of Microbial Resistance to Germicides")
    para(doc, "The processing level needed is decided by the **most resistant organism** "
              "likely to be present. Learn this ladder from most resistant at the top.")
    table(doc,
          ["Rank", "Organism group", "Examples", "Comment"],
          [["1 (most resistant)", "**Prions**",
            "Creutzfeldt\u2013Jakob disease agent, scrapie",
            "Resist routine autoclaving; require **134 \u00b0C for 18 min (pre-vacuum) or "
            "121 \u00b0C for 1 hour**, or 1 N NaOH followed by autoclaving; incineration "
            "preferred."],
           ["2", "**Bacterial spores**",
            "__Bacillus__, __Geobacillus stearothermophilus__, __Clostridium "
            "difficile__, __C. tetani__, __C. perfringens__",
            "The **benchmark for sterilization**; killing them defines the process."],
           ["3", "**Coccidia / protozoal cysts**",
            "__Cryptosporidium__, __Giardia__ cysts",
            "Highly resistant to chlorine \u2014 the reason for filtration of drinking "
            "water."],
           ["4", "**Mycobacteria**",
            "__M. tuberculosis__, __M. avium__, __M. terrae__",
            "Waxy, lipid-rich cell wall; a **tuberculocidal claim marks an intermediate "
            "level disinfectant**."],
           ["5", "**Non-lipid / small non-enveloped viruses**",
            "Poliovirus, coxsackievirus, rhinovirus, norovirus, hepatitis A, "
            "**human papilloma virus**",
            "No lipid envelope to dissolve \u2014 resist alcohols and quaternary "
            "compounds."],
           ["6", "**Fungi and fungal spores**",
            "__Candida__, __Aspergillus__, dermatophytes, __Trichophyton__",
            "Moderately susceptible."],
           ["7", "**Vegetative bacteria**",
            "__Staphylococcus aureus__, __Pseudomonas aeruginosa__, __Salmonella__, "
            "__E. coli__",
            "Readily killed, though __Pseudomonas__ tolerates many weak disinfectants and "
            "can grow in them."],
           ["8 (least resistant)", "**Lipid / medium-sized enveloped viruses**",
            "**HIV, hepatitis B and C, influenza, herpes simplex, SARS-CoV-2**, measles",
            "The lipid envelope is dissolved by alcohols, detergents and soaps \u2014 hence "
            "hand rub works well against them."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 10.4  Descending order of microbial resistance")

    box(doc, "mnemonic",
        "Top of the ladder downwards: ^^**P**rions \u2192 **S**pores \u2192 "
        "**C**occidia \u2192 **M**ycobacteria \u2192 **N**on-lipid viruses \u2192 "
        "**F**ungi \u2192 **V**egetative bacteria \u2192 **L**ipid viruses^^ "
        "\u2014 __\u201cPretty Sure Cats Make Nice Furry Vet Labs\u201d__.")

    h2(doc, "10.4  Kinetics of Microbial Death")
    table(doc,
          ["Term", "Meaning", "Exam point"],
          [["**D-value (decimal reduction time)**",
            "The time (at a stated temperature) or the radiation dose required to reduce the "
            "microbial population by **90%, i.e. by one logarithm (1 log\u2081\u2080)**.",
            "For __G. stearothermophilus__ at 121 \u00b0C, D \u2248 **1.5\u20132 minutes**."],
           ["**Z-value**",
            "The **temperature change (in \u00b0C) required to produce a tenfold change in "
            "the D-value**.",
            "For moist heat and __G. stearothermophilus__, Z \u2248 **10 \u00b0C**."],
           ["**F-value / F\u2080**",
            "The **equivalent time in minutes at 121 \u00b0C** delivered by a process to a "
            "product, with Z = 10 \u00b0C. An **F\u2080 of 8\u201312 minutes** is generally "
            "accepted for pharmaceutical steam sterilization.",
            "Allows a lower-temperature, longer cycle to be shown equivalent to 121 \u00b0C."],
           ["**Thermal death point (TDP)**",
            "The **lowest temperature** that kills all the organisms in a standardised "
            "suspension in a fixed time (usually 10 minutes).", ""],
           ["**Thermal death time (TDT)**",
            "The **minimum time** needed to kill all the organisms in a suspension at a "
            "given temperature.", ""],
           ["**Sterility Assurance Level (SAL)**",
            "The probability that a single unit which has been through the process is "
            "**non-sterile**. The pharmacopoeial requirement is ~~SAL of "
            "10\u207b\u2076~~ \u2014 not more than one chance in a million of a viable "
            "organism surviving.",
            "**Very frequently asked.** A 12-log reduction ('overkill') cycle is designed "
            "to achieve it."],
           ["**Bioburden**",
            "The number and type of viable organisms present on an article before "
            "sterilization.",
            "The **higher the bioburden, the longer the process needed** \u2014 hence "
            "cleaning first."]],
          header_fill=SH_HEADER_TEAL)

    h2(doc, "10.5  Factors Influencing the Efficacy of Sterilization and Disinfection")
    table(doc,
          ["Factor", "Effect"],
          [["**Number of organisms (bioburden)**",
            "Death is logarithmic; the larger the initial population, the longer the time "
            "required."],
           ["**Type and form of organism**",
            "Spores, mycobacteria and non-enveloped viruses need far harsher treatment "
            "(Table 10.4). Biofilms are extremely resistant."],
           ["**Concentration / potency of the agent**",
            "In general, activity rises with concentration \u2014 but there are important "
            "exceptions: **70% alcohol is more effective than absolute (100%) alcohol** "
            "because water is needed for protein denaturation, and **iodine and hydrogen "
            "peroxide** have optimum concentrations."],
           ["**Duration of exposure (contact time)**",
            "The agent must remain **wet on the surface** for the full stated contact time; "
            "this is the most commonly violated requirement in practice."],
           ["**Temperature**",
            "Activity of chemical disinfectants generally **increases 2- to 3-fold for each "
            "10 \u00b0C rise**; heat sterilization time falls steeply as temperature rises."],
           ["**pH**",
            "Glutaraldehyde needs **alkaline** pH (7.5\u20138.5) for sporicidal activity; "
            "hypochlorites and phenols are more active at **acidic** pH; quaternary "
            "ammonium compounds prefer alkaline pH."],
           ["**Presence of organic matter** (blood, pus, serum, faeces, sputum, milk)",
            "**Neutralises and physically shields** the organisms. Hypochlorites, iodine and "
            "quaternary compounds are badly inactivated; **glutaraldehyde and phenolics are "
            "relatively resistant to inactivation**. Hence the rule: **clean first**."],
           ["**Nature of the surface / article**",
            "Rough, porous, cracked, jointed, lumened and hinged items are hard to "
            "penetrate; **narrow lumens and hinges must be opened and flushed**."],
           ["**Interfering substances**",
            "Soaps and anionic detergents inactivate **quaternary ammonium compounds** and "
            "chlorhexidine; hard water (Ca\u00b2\u207a, Mg\u00b2\u207a) reduces QAC "
            "activity; cork and some plastics adsorb preservatives."],
           ["**Humidity**",
            "Critical for gaseous agents: **ethylene oxide needs 30\u201360% relative "
            "humidity**; formaldehyde vapour needs > 60%; dry spores resist gases."],
           ["**Presence of air**",
            "Trapped air prevents steam contact \u2014 **air is the chief enemy of the "
            "autoclave**; it must be completely displaced or evacuated."]],
          header_fill=SH_HEADER_GREEN)

    h2(doc, "10.6  Mechanisms of Antimicrobial Action")
    table(doc,
          ["Mechanism", "How it kills", "Agents acting this way"],
          [["**Protein denaturation and coagulation**",
            "Unfolds and precipitates structural and enzyme proteins.",
            "**Moist heat**, alcohols, phenols, acids and alkalies."],
           ["**Oxidative damage / oxidation of cell constituents**",
            "Oxidises proteins, lipids and nucleic acids; generates free radicals.",
            "**Dry heat**, hydrogen peroxide, peracetic acid, halogens, potassium "
            "permanganate, ozone, plasma."],
           ["**Damage to the cell membrane**",
            "Disorganises the lipid bilayer, causing leakage of cell contents.",
            "**Surface-active agents (QACs, soaps)**, alcohols, phenols, chlorhexidine, "
            "polymyxins."],
           ["**Alkylation of proteins and nucleic acids**",
            "Substitutes alkyl groups on \u2013NH\u2082, \u2013SH, \u2013COOH and \u2013OH "
            "groups, destroying function.",
            "**Ethylene oxide, formaldehyde, glutaraldehyde, beta-propiolactone** "
            "(all alkylating agents)."],
           ["**Reaction with \u2013SH (sulphydryl) groups of enzymes**",
            "Inactivates essential enzymes.",
            "**Heavy metals \u2014 mercury, silver, copper**; oxidising agents."],
           ["**Damage to nucleic acid**",
            "Forms thymine dimers or breaks the DNA strand, preventing replication.",
            "**Ultraviolet radiation** (thymine dimers), **ionising radiation** (strand "
            "breaks, free radicals), acridine and aniline dyes."],
           ["**Physical removal of organisms**",
            "The organism is not killed but separated from the fluid or air.",
            "**Filtration**, washing, scrubbing, sedimentation, centrifugation."]],
          header_fill=SH_HEADER_PURPLE)

    h2(doc, "10.7  Master Classification of Methods")
    table(doc,
          ["Category", "Sub-group", "Methods"],
          [["**A. PHYSICAL**", "Sunlight", "Direct sunlight (natural method of "
            "sterilization)"],
           ["", "Drying / desiccation", "Air drying \u2014 unreliable, bacteriostatic only"],
           ["", "**Dry heat**",
            "Red heat \u00b7 Flaming \u00b7 Incineration \u00b7 **Hot air oven** \u00b7 "
            "Infrared radiation \u00b7 Microwave"],
           ["", "**Moist heat below 100 \u00b0C**",
            "Pasteurisation \u00b7 Inspissation (Koch\u2013Henle) \u00b7 Vaccine bath "
            "\u00b7 Serum bath \u00b7 Low-temperature steam formaldehyde (LTSF)"],
           ["", "**Moist heat at 100 \u00b0C**",
            "Boiling \u00b7 Steam at atmospheric pressure (Koch's or Arnold's steamer) "
            "\u00b7 Tyndallisation (intermittent sterilization)"],
           ["", "**Moist heat above 100 \u00b0C**",
            "**Autoclave** (steam under pressure) \u2014 gravity displacement and "
            "pre-vacuum (porous load) types"],
           ["", "**Radiation**",
            "Non-ionising \u2014 **ultraviolet**, infrared \u00b7 Ionising \u2014 "
            "**gamma rays (Co-60)**, X-rays, electron/cathode beams"],
           ["", "Sonic energy", "Ultrasonic and sonic vibration (mainly used for cleaning)"],
           ["**B. MECHANICAL**", "Removal of organisms",
            "**Filtration** \u2014 candle, asbestos, sintered glass, membrane, HEPA filters "
            "\u00b7 Washing, scrubbing, mopping, dusting \u00b7 Ultrasonic and "
            "washer-disinfector cleaning \u00b7 Sedimentation and centrifugation \u00b7 "
            "Laminar air flow"],
           ["**C. CHEMICAL**", "Liquid agents",
            "Alcohols \u00b7 Aldehydes \u00b7 Phenols \u00b7 Halogens \u00b7 Oxidising "
            "agents \u00b7 Heavy metals \u00b7 Surface-active agents \u00b7 Dyes \u00b7 "
            "Acids and alkalies"],
           ["", "Gaseous agents",
            "**Ethylene oxide** \u00b7 Formaldehyde gas \u00b7 Beta-propiolactone \u00b7 "
            "Hydrogen peroxide vapour and plasma \u00b7 Ozone \u00b7 Chlorine dioxide"]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 10.5  Master classification of methods of sterilization and "
                  "disinfection")

    h2(doc, "10.8  Control of Sterilization \u2014 Sterility Indicators")
    para(doc, "Every sterilizing process must be monitored. Three classes of monitor are "
              "used, and a fourth \u2014 sterility testing \u2014 tests the product itself.")
    table(doc,
          ["Type of control", "What it monitors", "Examples"],
          [["**Physical (mechanical) indicators**",
            "That the machine reached and held the required physical conditions.",
            "Thermometer and thermocouple readings, pressure gauge, timer, "
            "temperature\u2013time\u2013pressure chart recorder or printout, vacuum gauge, "
            "**Browne's tube** (a sealed glass tube whose indicator turns from red through "
            "amber to **green** when the correct temperature\u2013time has been reached)."],
           ["**Chemical indicators**",
            "That a chemical change requiring the sterilizing conditions has occurred; "
            "graded as **Class 1 to Class 6** by ISO 11140.",
            "**Class 1** \u2013 external process indicator (autoclave tape, indicator on "
            "the pack). **Class 2** \u2013 specific-use test, notably the ^^Bowie\u2013Dick "
            "test^^ which detects **residual air and inadequate steam penetration in a "
            "pre-vacuum autoclave** (done daily). **Class 3** \u2013 single-variable. "
            "**Class 4** \u2013 multi-variable. **Class 5** \u2013 integrating indicator, "
            "reacting to all critical variables. **Class 6** \u2013 emulating "
            "cycle-verification indicator."],
           ["**Biological indicators (BI)**",
            "That **standardised, highly resistant bacterial spores were actually killed** "
            "\u2014 the most reliable proof of sterilization.",
            "Spore strips, self-contained vials or ampoules. Placed in the most "
            "inaccessible part of the load, then incubated: **no growth = process "
            "effective**."],
           ["**Sterility testing of the product**",
            "Whether the finished article is in fact sterile.",
            "Sample units incubated in **fluid thioglycollate medium at 30\u201335 \u00b0C** "
            "(for anaerobes and aerobes) and **soyabean\u2013casein digest (tryptone soya) "
            "broth at 20\u201325 \u00b0C** (for fungi and aerobes) for **14 days**; or "
            "**membrane filtration** of the whole volume followed by culture of the "
            "membrane."]],
          header_fill=SH_HEADER_TEAL)

    table(doc,
          ["Sterilizing process", "Biological indicator organism", "Note"],
          [["**Autoclave / moist heat**",
            "~~__Geobacillus stearothermophilus__~~ (formerly __Bacillus "
            "stearothermophilus__), ATCC 7953",
            "Thermophilic; spores killed in about **12 minutes at 121 \u00b0C**; incubated "
            "at **55\u201360 \u00b0C**."],
           ["**Hot air oven / dry heat**",
            "~~__Bacillus atrophaeus__~~ (formerly __B. subtilis__ var. __niger__ / "
            "__globigii__)",
            "Incubated at 30\u201335 \u00b0C."],
           ["**Ethylene oxide gas**", "__Bacillus atrophaeus__",
            "Same organism as for dry heat \u2014 a common examination pairing."],
           ["**Ionising (gamma) radiation**",
            "__Bacillus pumilus__", "Highly radiation-resistant spores."],
           ["**Hydrogen peroxide gas plasma**", "__Geobacillus stearothermophilus__", ""],
           ["**Low-temperature steam formaldehyde**",
            "__Geobacillus stearothermophilus__", ""],
           ["**Filtration (membrane integrity / bacterial challenge)**",
            "__Brevundimonas diminuta__ (formerly __Pseudomonas diminuta__)",
            "The standard challenge organism for validating a **0.22 \u00b5m** sterilising "
            "filter."]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 10.6  Biological indicators \u2014 must be memorised")

    box(doc, "highyield",
        ["^^__Geobacillus stearothermophilus__ = autoclave^^; "
         "^^__Bacillus atrophaeus__ = dry heat and ethylene oxide^^; "
         "^^__Bacillus pumilus__ = gamma radiation^^; "
         "^^__Brevundimonas (Pseudomonas) diminuta__ = 0.22 \u00b5m filter^^.",
         "**Bowie\u2013Dick test** = detection of **air removal / steam penetration** "
         "failure in a **pre-vacuum** autoclave. **Browne's tube turning green** = correct "
         "temperature\u2013time achieved.",
         "The **biological indicator is the most reliable** monitor of sterilization; "
         "physical and chemical indicators only show that conditions were probably met."])

    chapter_end(doc)



# ===========================================================================
# CHAPTER 11
# ===========================================================================
def chapter_11(doc):
    chapter_title(doc, 11, "Physical Methods \u2014 I : Sunlight, Drying and Dry Heat")

    h2(doc, "11.1  Sunlight")
    bullets(doc, [
        "Sunlight is the **natural method of sterilization** of water in tanks, rivers and "
        "lakes and of exposed surfaces.",
        "Its action is due mainly to the **ultraviolet component** together with heat and "
        "drying.",
        "In tropical countries such as India sunlight is appreciably **more effective** "
        "because of the greater intensity and duration of sunshine.",
        "**Uses:** drying and airing of bedding, mattresses, blankets, clothing, books and "
        "shoes in infectious disease; **SODIS** (solar disinfection) of drinking water in "
        "transparent PET bottles exposed for 6 hours of bright sun; solar drying of grain "
        "and chillies.",
        "**Limitations:** slow, unreliable, only surface action, no penetration through "
        "glass, cloth or dirt, and dependent on the weather \u2014 therefore **never used "
        "when true sterility is needed**.",
    ])

    h2(doc, "11.2  Drying (Desiccation)")
    bullets(doc, [
        "Water is essential for bacterial growth; drying therefore has a definite "
        "**bacteriostatic (inhibitory) effect** on vegetative bacteria.",
        "**Spores are unaffected**, and many organisms survive drying for long periods "
        "\u2014 __M. tuberculosis__ in dust, staphylococci in dried pus, and dried "
        "spore-formers indefinitely.",
        "**Freeze-drying (lyophilisation)** \u2014 rapid freezing followed by dehydration "
        "under high vacuum \u2014 is used not to kill but to **preserve** bacteria, "
        "vaccines, sera and heat-labile drugs for years.",
        "**Conclusion: drying is an unreliable method and is not a method of "
        "sterilization.**",
    ])

    h2(doc, "11.3  Dry Heat \u2014 General Principles")
    box(doc, "definition",
        ["**Mechanism of killing by dry heat:** ^^oxidative damage to cell constituents, "
         "denaturation of proteins, a toxic rise in electrolyte concentration as water is "
         "lost, and finally charring and carbonisation.^^",
         "Dry heat **penetrates poorly and kills more slowly** than moist heat, so it needs "
         "a **higher temperature and a longer time** for the same effect."])

    table(doc,
          ["Method", "Temperature", "Time", "Articles sterilized", "Notes"],
          [["**Red heat**",
            "Until the metal glows **red** (\u2248 800\u20131000 \u00b0C)", "A few seconds",
            "**Bacteriological (inoculating) loops and wires, straight wires, tips of "
            "forceps, needles, searing spatulas**",
            "Held in the flame of a Bunsen burner until red-hot; the simplest and commonest "
            "laboratory method. The loop must be cooled before touching the culture."],
           ["**Flaming**",
            "Passed through a **Bunsen flame** without letting the article become red hot",
            "A few seconds",
            "**Mouths of culture tubes and flasks, glass slides, cover slips, scalpels, "
            "needles, cotton-wool plugs**",
            "Often the article is first dipped in **spirit (alcohol) and then ignited** "
            "\u2014 this is called **flaming** and is of **doubtful efficacy**; it is not "
            "true sterilization."],
           ["**Incineration**",
            "**\u2248 870\u20131200 \u00b0C** (primary chamber 800 \u00b1 50 \u00b0C, "
            "secondary chamber 1050 \u00b1 50 \u00b0C in a hospital incinerator)",
            "Until reduced to ash",
            "**Soiled dressings, cotton swabs, bandages, surgical pads, plaster casts, "
            "bedding, pathological and anatomical waste, animal carcasses, placenta, "
            "laboratory cultures and expired/cytotoxic drugs**",
            "An excellent method of **safe disposal** by complete destruction. "
            "**Never incinerate** PVC and chlorinated plastics (produce dioxins and furans), "
            "mercury, radioactive material or pressurised containers."],
           ["**Hot air oven**",
            "~~160 \u00b0C~~ (also 170 \u00b0C or 180 \u00b0C)",
            "~~2 hours at 160 \u00b0C~~ (1 hour at 170 \u00b0C; 30 min at 180 \u00b0C; "
            "2\u00bd hours at 150 \u00b0C) \u2014 holding time counted **after** the "
            "thermometer reaches the set temperature",
            "**Glassware (test tubes, petri dishes, pipettes, flasks), metal instruments, "
            "forceps, scalpels, scissors, glass syringes, swabs, oils, fats, waxes, "
            "greases, liquid paraffin, dusting and sulphonamide powders, ointment bases, "
            "glycerol, all-glass syringes**",
            "The **most widely used method of dry-heat sterilization.** See \u00a711.4."],
           ["**Infrared radiation**",
            "**\u2248 180 \u00b0C**", "**7\u00bd\u201310 minutes**",
            "**Metal instruments, glass syringes, needles, catheters, packaged goods on a "
            "conveyor belt**",
            "Infrared rays from an electrically heated element are focused; the articles "
            "travel through a **tunnel on a conveyor belt**. Rapid and suited to mass "
            "industrial processing; radiation does not itself sterilize \u2014 it heats the "
            "article."],
           ["**Microwave**",
            "Generated at **2450 MHz**; the article reaches roughly 97\u2013100 \u00b0C",
            "Varies (minutes)",
            "**Non-metallic items, laboratory waste, some biomedical waste, food, "
            "dentures**",
            "Kills by the heat produced when water molecules are agitated; needs **moisture** "
            "and gives **uneven heating** (hot and cold spots). It is **not recommended for "
            "anatomical, cytotoxic or radioactive waste** and cannot be used for metals."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 11.1  Dry-heat methods")

    h2(doc, "11.4  The Hot Air Oven in Detail")
    h3(doc, "11.4.1  Construction and Working")
    bullets(doc, [
        "An insulated, **double-walled metal chamber** heated by electrical elements in the "
        "walls or floor; the standard laboratory pattern is the **Hot Air Oven of "
        "Pasteur**.",
        "Fitted with **perforated shelves**, a **thermostat**, a **thermometer** (or "
        "thermocouple) projecting into the chamber, a **timer** and usually a **fan** or "
        "blower to circulate air and prevent hot and cold spots (a 'forced-air' or "
        "'mechanical-convection' oven).",
        "**Loading:** the oven must be **loosely packed** \u2014 no article should touch the "
        "walls, and air must circulate freely between the packs, because **hot air is a bad "
        "conductor with poor penetrating power**.",
        "**Wrapping:** articles are wrapped in paper, placed in metal canisters or boxes, or "
        "plugged with cotton wool; test tubes and flasks are plugged and covered with paper "
        "caps.",
        "**Cycle:** load \u2192 heat to the set temperature \u2192 **hold for the full "
        "holding time** \u2192 switch off \u2192 allow to cool to below **60 \u00b0C before "
        "opening** \u2014 if opened while hot, **the sudden inrush of cool air cracks the "
        "glassware**.",
    ])

    h3(doc, "11.4.2  Precautions, Sterility Control, Advantages and Limitations")
    table(doc,
          ["Heading", "Points"],
          [["**Precautions**",
            "Articles must be **clean, dry and grease-free** before loading \u00b7 "
            "do not overload \u00b7 leave space between articles \u00b7 the holding time "
            "begins only when the **whole load** reaches the temperature \u00b7 never place "
            "articles on the floor of the chamber \u00b7 cotton wool, paper and cloth char "
            "above 160 \u00b0C \u00b7 rubber, plastics and most fabrics cannot be used "
            "\u00b7 cool before opening."],
           ["**Sterility controls**",
            "**Physical** \u2014 thermocouples and a temperature chart; **chemical** \u2014 "
            "**Browne's tube No. 3** (turns green) and heat-indicating tape; "
            "**biological** \u2014 spores of ~~__Bacillus atrophaeus__~~ "
            "(10\u2076 spores on paper strips) placed in the centre of the load, which "
            "should be killed in 60 minutes at 160 \u00b0C."],
           ["**Advantages**",
            "Simple, reliable, cheap to run, no corrosion of metal instruments or blunting "
            "of sharp edges compared with steam, **no wetting of the load**, suitable for "
            "articles that steam cannot penetrate (**oils, fats, waxes, powders, "
            "glycerol**) and for **closed containers**."],
           ["**Limitations / disadvantages**",
            "**Slow** (a full cycle with heating-up and cooling takes several hours) \u00b7 "
            "**poor penetration** \u00b7 the **high temperature destroys** rubber, "
            "plastics, fabrics, cotton, paper, most culture media, surgical dressings and "
            "aqueous solutions \u00b7 **graduated and volumetric glassware may lose "
            "calibration** \u00b7 glass may crack on rapid cooling \u00b7 unsuitable for "
            "heat-labile pharmaceuticals."]],
          header_fill=SH_HEADER_TEAL)

    box(doc, "highyield",
        ["^^Hot air oven: 160 \u00b0C for 2 hours^^ is the standard answer. Equivalents: "
         "**170 \u00b0C \u2013 1 hour**, **180 \u00b0C \u2013 30 minutes**, "
         "**150 \u00b0C \u2013 2\u00bd hours**.",
         "Articles sterilized **only by dry heat, never by autoclave**: ~~oils, fats, waxes, "
         "greases, liquid paraffin, dusting powders, glycerol and closed glass "
         "containers~~ \u2014 because **steam cannot penetrate them**.",
         "**Incineration temperature** in a hospital incinerator: primary chamber "
         "**800 \u00b1 50 \u00b0C**, secondary chamber **1050 \u00b1 50 \u00b0C** with a gas "
         "retention time of at least **2 seconds**."])

    chapter_end(doc)


# ===========================================================================
# CHAPTER 12
# ===========================================================================
def chapter_12(doc):
    chapter_title(doc, 12, "Physical Methods \u2014 II : Moist Heat and the Autoclave")

    box(doc, "definition",
        ["**Mechanism of killing by moist heat:** ^^denaturation and coagulation of "
         "proteins^^, especially of essential enzymes, together with disruption of "
         "membranes and breakage of hydrogen bonds. Water vapour carries a large amount of "
         "**latent heat of condensation** (about 518\u2013540 calories per gram at "
         "100 \u00b0C), which is released directly onto the article the moment steam "
         "condenses on it.",
         "**Moist heat is far more efficient than dry heat** and therefore works at a lower "
         "temperature and in a shorter time. This is the single most important comparison in "
         "the chapter."])

    h2(doc, "12.1  Moist Heat Below 100 \u00b0C")
    table(doc,
          ["Method", "Temperature and time", "Purpose and material treated"],
          [["**Pasteurisation of milk \u2014 Holder (LTLT) method**",
            "~~63 \u00b0C (145 \u00b0F) for 30 minutes~~, then rapid cooling to 13 \u00b0C "
            "or below",
            "Kills the milk-borne pathogens **__Mycobacterium bovis__ and __M. "
            "tuberculosis__, __Brucella abortus__, __Salmonella__, __Streptococcus__, "
            "__Coxiella burnetii__, __Campylobacter__, __Listeria__** without altering the "
            "taste or nutritive value. **Spores and thermoduric organisms survive** \u2014 "
            "it is **not sterilization**."],
           ["**Pasteurisation \u2014 Flash / HTST method**",
            "~~72 \u00b0C (161 \u00b0F) for 15\u201320 seconds~~, then rapid cooling",
            "The method used in modern large dairies; HTST = High Temperature Short Time. "
            "The most widely used commercially."],
           ["**Ultra High Temperature (UHT)**",
            "**125\u2013150 \u00b0C for 1\u20135 seconds** (commonly 135\u2013140 \u00b0C "
            "for 2\u20134 seconds)",
            "Gives commercially sterile, long-shelf-life packaged (tetra-pack) milk."],
           ["**Inspissation (Koch\u2013Henle method)**",
            "~~80\u201385 \u00b0C for 30 minutes on 3 successive days~~ in an inspissator",
            "Solidifies **and** disinfects **egg- and serum-containing culture media** "
            "\u2014 ^^L\u00f6wenstein\u2013Jensen medium, Dorset egg medium and "
            "L\u00f6ffler's serum slope^^. Autoclaving would coagulate and ruin them."],
           ["**Vaccine bath**",
            "**60 \u00b0C for 1 hour** in a water bath",
            "Inactivates the organisms in a **bacterial vaccine** and destroys "
            "contaminating organisms without destroying antigenicity."],
           ["**Serum / body-fluid bath**",
            "**56 \u00b0C for 1 hour on several successive days** (heating serum to "
            "56 \u00b0C for 30 minutes also **inactivates complement**)",
            "Disinfection of **serum and body fluids**, whose proteins coagulate at "
            "higher temperatures."],
           ["**Low-Temperature Steam Formaldehyde (LTSF)**",
            "**Dry saturated steam at 73\u201380 \u00b0C with formaldehyde vapour**, "
            "\u2248 2 hours",
            "A **sterilizing** process for **heat-sensitive** items \u2014 cystoscopes, "
            "plastic and rubber goods, some endoscopes. Requires efficient air removal and "
            "post-cycle aeration."],
           ["**Low-temperature steam (LTS) / pasteurising washer-disinfector**",
            "**73 \u00b0C for 10 minutes** (or 80 \u00b0C for 1 min; 90 \u00b0C for 1 s)",
            "High-level **disinfection** of respiratory and anaesthetic equipment, "
            "bed-pans and utensils in a washer-disinfector."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 12.1  Moist heat below 100 \u00b0C")

    box(doc, "highyield",
        ["**Pasteurisation temperatures: 63 \u00b0C/30 min (Holder) and 72 \u00b0C/"
         "15\u201320 s (Flash).** The organism whose thermal resistance sets the standard "
         "is ~~__Coxiella burnetii__~~ (the most heat-resistant milk pathogen); the "
         "classical target was __Mycobacterium tuberculosis/bovis__.",
         "The test used to check the efficiency of pasteurisation is the ^^phosphatase "
         "test^^ (alkaline phosphatase should be destroyed); the **standard plate count** "
         "and **coliform count** are also used, and the **methylene blue reduction test** "
         "assesses milk quality.",
         "**Inspissation = 80\u201385 \u00b0C \u00d7 30 min \u00d7 3 days**, used for "
         "**L\u00f6wenstein\u2013Jensen medium**. Do not confuse it with "
         "**Tyndallisation = 100 \u00b0C \u00d7 20 min \u00d7 3 days**."])

    h2(doc, "12.2  Moist Heat At 100 \u00b0C")
    table(doc,
          ["Method", "Conditions", "Uses", "Comments"],
          [["**Boiling**",
            "**100 \u00b0C for 10\u201330 minutes** (at least 10 min; 20\u201330 min "
            "preferred). Boiling point falls with altitude, so time must be increased.",
            "Emergency disinfection of **metal instruments, syringes, needles, glass "
            "syringes, rubber goods, bed-pans, feeding utensils, linen and drinking water** "
            "where no autoclave exists.",
            "**NOT sterilization** \u2014 ^^bacterial spores, hepatitis B virus and some "
            "thermophiles may survive^^. Adding **2% sodium bicarbonate (washing soda)** "
            "raises the boiling point to about 105 \u00b0C, increases the killing power and "
            "**prevents rusting of instruments**. Articles must be fully immersed and the "
            "lid kept closed; timing starts when boiling begins."],
           ["**Steam at atmospheric pressure (free steam)**",
            "**100 \u00b0C for 90 minutes** in a **Koch's or Arnold's steamer** (or an "
            "autoclave with the lid loose and the discharge tap open)",
            "**Culture media that are damaged by higher temperatures** \u2014 media "
            "containing sugars, gelatin, milk, DCA and selenite F broth.",
            "Steam at 100 \u00b0C kills vegetative organisms but **not spores** in a single "
            "exposure."],
           ["**Tyndallisation (intermittent or fractional sterilization)**",
            "~~Free steam at 100 \u00b0C for 20\u201345 minutes on 3 successive days~~ "
            "(classically 20 min \u00d7 3 days), the material being incubated at room "
            "temperature between exposures",
            "**Heat-labile culture media containing sugars, gelatin, egg, serum or milk**; "
            "some pharmaceutical preparations.",
            "**Principle:** the first exposure kills the vegetative forms; surviving "
            "**spores germinate** into vegetative forms during the interval and are killed "
            "by the next exposure. Named after **John Tyndall**. Also called the "
            "**Koch\u2013Henle principle** when applied at 80 \u00b0C (inspissation)."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 12.2  Moist heat at 100 \u00b0C")

    h2(doc, "12.3  Moist Heat Above 100 \u00b0C \u2014 The Autoclave")
    box(doc, "definition",
        "An **autoclave (steam sterilizer)** sterilizes by exposing articles to "
        "**saturated steam under pressure**. Raising the pressure raises the temperature at "
        "which water boils, so steam hotter than 100 \u00b0C is obtained. It is the "
        "^^most widely used, most reliable, quickest and cheapest method of "
        "sterilization^^ in hospitals and laboratories.")

    h3(doc, "12.3.1  Principle")
    bullets(doc, [
        "Water boils at 100 \u00b0C when the pressure above it is one atmosphere. If the "
        "pressure is raised, the boiling point and therefore the temperature of the steam "
        "rises.",
        "The killing is done by **saturated steam that condenses on the article**, giving up "
        "its **latent heat** and simultaneously wetting the surface \u2014 hence the two "
        "essentials are **direct steam contact** and **complete removal of air**.",
        "**Air is the great enemy of the autoclave.** Air is heavier than steam, forms a "
        "layer at the bottom, prevents steam from contacting the load, and lowers the "
        "temperature actually achieved for a given pressure. Therefore all air must be "
        "displaced downwards through the discharge tap or evacuated by a pump.",
    ])

    table(doc,
          ["Gauge pressure", "Absolute pressure", "Temperature of saturated steam",
           "Holding time", "Chief use"],
          [["**0 psi** (atmospheric)", "1 atm", "**100 \u00b0C**", "\u2014 (free steam)",
            "Tyndallisation, delicate media"],
           ["~~15 psi (1.05 kg/cm\u00b2, \u2248 103 kPa, 1 bar)~~", "2 atm",
            "~~121 \u00b0C~~", "~~15\u201320 minutes~~",
            "**The standard cycle** \u2014 culture media, aqueous solutions, rubber, "
            "glassware, instruments, linen"],
           ["**20 psi (1.4 kg/cm\u00b2)**", "\u2248 2.4 atm", "**126 \u00b0C**",
            "**10 minutes**", "Faster routine cycle"],
           ["**30 psi (2.1 kg/cm\u00b2)**", "\u2248 3 atm", "**134 \u00b0C**",
            "**3\u20137 minutes** (commonly 3\u20133\u00bd min)",
            "**High-vacuum porous-load cycle** \u2014 dressings, gowns, drapes, "
            "instruments; the standard hospital 'flash' cycle"],
           ["**30 psi**", "\u2248 3 atm", "**134 \u00b0C**", "**18 minutes**",
            "**Prion (CJD) decontamination**"]],
          header_fill=SH_HEADER_GREEN, align_center_cols=[0, 1, 2, 3],
          caption="Table 12.3  Pressure\u2013temperature\u2013time relationships "
                  "(must be memorised)")

    h3(doc, "12.3.2  Types of Autoclave")
    table(doc,
          ["Type", "Description", "Suitable for"],
          [["**Laboratory (domestic / pressure-cooker) type**",
            "A vertical, cylindrical vessel of gunmetal or stainless steel in a supporting "
            "iron case, heated electrically or by gas; the lid is fastened by screw clamps "
            "and carries a **pressure gauge, a safety (blow-off) valve, a steam discharge "
            "tap and a thermometer**.",
            "Small laboratory loads \u2014 culture media, glassware, discarded cultures."],
           ["**Gravity (downward) displacement type \u2014 e.g. the hospital 'bowl and "
            "instrument' sterilizer**",
            "Steam, being lighter than air, enters at the **top** and drives the air "
            "**downward and out through the discharge channel at the bottom**, which "
            "contains a **near-to-steam thermostatic trap** that closes when steam reaches "
            "it.",
            "**Unwrapped solid instruments, bowls, fluids in vented containers, culture "
            "media**. Poor at penetrating porous loads."],
           ["**Pre-vacuum / high-vacuum porous-load type**",
            "A **vacuum pump removes about 98% of the air before steam admission**, so "
            "steam penetrates instantly and evenly; the cycle is very short "
            "(**134 \u00b0C for 3\u20134 minutes**) and the load is dried by a post-cycle "
            "vacuum.",
            "**Porous loads \u2014 surgical dressings, gowns, drapes, linen packs, wrapped "
            "instrument trays, hollow and lumened instruments.** The standard in a modern "
            "**CSSD**. Must be checked **daily by the Bowie\u2013Dick test**."],
           ["**Horizontal rectangular (hospital) type**",
            "A large, jacketed, rectangular chamber with a door at one or both ends "
            "(**double-ended / pass-through**, allowing loading on the dirty side and "
            "unloading on the clean side).",
            "Bulk hospital work; the basis of CSSD design."],
           ["**Continuous / rotary and hydroclave types**",
            "Industrial designs for continuous processing of ampoules, bottles and "
            "biomedical waste.",
            "Pharmaceutical manufacture; **hydroclaving** of biomedical waste."]],
          header_fill=SH_HEADER_PURPLE)

    h3(doc, "12.3.3  Parts of a Laboratory Autoclave")
    bullets(doc, [
        "**Chamber (inner vessel)** \u2014 gunmetal or stainless steel, holding the load on "
        "a perforated tray above the water.",
        "**Outer jacket / case** \u2014 insulating and protective.",
        "**Lid** with a rubber gasket and radial screw clamps to make it airtight.",
        "**Heating element** (electric immersion heater) or gas burner beneath the water.",
        "**Pressure gauge** \u2014 shows the steam pressure inside.",
        "**Safety valve (blow-off valve)** \u2014 a spring-loaded or weighted valve that "
        "releases steam if the pressure exceeds the set limit, preventing explosion.",
        "**Steam discharge (air-vent) tap / stopcock** \u2014 to allow the air\u2013steam "
        "mixture to escape at the start and to release steam at the end.",
        "**Thermometer or thermocouple** \u2014 the **temperature, not the pressure, is the "
        "true measure of sterilizing conditions**.",
        "**Whistle / pet-cock** and a **water-level indicator**.",
    ])

    h3(doc, "12.3.4  Operating Procedure")
    numbered(doc, [
        "Check that there is **sufficient water** in the chamber.",
        "**Load loosely**, leaving space for steam circulation; place articles on the "
        "perforated tray, not in the water; bottles and tubes must have **loosened caps or "
        "vented closures**, and dressing drums must have their **vents open**.",
        "Close the lid and **tighten the clamps evenly**, keeping the **discharge tap "
        "open**.",
        "Switch on the heater. Allow steam to escape freely from the discharge tap until "
        "**all the air has been driven out** (a steady, forceful jet of steam with no "
        "spluttering; about 10 minutes, or until the mixture emerging is pure steam).",
        "**Close the discharge tap.** The pressure now rises.",
        "When the gauge reads **15 psi** and the thermometer reads **121 \u00b0C**, start "
        "timing the **holding period of 15\u201320 minutes**, keeping the pressure steady.",
        "Switch off the heat and allow the autoclave to **cool until the pressure gauge "
        "returns to zero**.",
        "Open the discharge tap **slowly** to admit air; then open the lid. For fluids, cool "
        "slowly to prevent the bottles boiling over and cracking.",
        "Remove the load, check the indicators, and **allow packs to dry** before storage; "
        "a **wet pack is a contaminated pack**.",
    ])

    h3(doc, "12.3.5  Articles Sterilized by Autoclave")
    table(doc,
          ["Suitable (autoclavable)", "NOT suitable"],
          [["**Culture media** (except those with sugars, egg, serum or gelatin), "
            "**aqueous solutions, parenteral (IV) fluids, buffers**",
            "**Oils, fats, waxes, greases, liquid paraffin, petroleum jelly** \u2014 steam "
            "cannot penetrate them (use **dry heat**)"],
           ["**Surgical instruments, bowls, kidney trays, forceps, scissors** (stainless "
            "steel)",
            "**Dry powders** (dusting powder, talc, sulphonamide powder) \u2014 steam cannot "
            "penetrate (use **dry heat**)"],
           ["**Surgical dressings, gauze, cotton, gowns, drapes, linen, caps, masks, "
            "towels** (pre-vacuum porous load cycle)",
            "**Sharp cutting instruments** \u2014 scalpel blades, scissors, needles may be "
            "**blunted and corroded** by repeated steam (prefer dry heat or a chemical "
            "sterilant)"],
           ["**Rubber goods** \u2014 gloves, tubing, catheters, bungs, closures "
            "(115\u2013121 \u00b0C, shorter cycle)",
            "**Heat-labile plastics** \u2014 polystyrene, PVC, most disposables (use "
            "**ethylene oxide or gamma radiation**)"],
           ["**Glassware, glass syringes, pipettes, petri dishes, flasks**",
            "**Heat-labile solutions** \u2014 sera, vaccines, antibiotic and vitamin "
            "solutions, urea broth, blood products (use **filtration**)"],
           ["**Discarded cultures, contaminated media, plates, pipettes and infectious "
            "laboratory waste** (**121 \u00b0C for 30\u201360 minutes**)",
            "**Delicate instruments with lenses and fibre optics** \u2014 endoscopes, "
            "cystoscopes (use **chemical HLD or LTSF**)"],
           ["**Autoclavable plastics** \u2014 polypropylene, PTFE, polycarbonate",
            "**Volumetric/graduated glassware** may lose calibration; sealed glass ampoules "
            "may burst"]],
          header_fill=SH_HEADER_BLUE)

    h3(doc, "12.3.6  Causes of Failure of the Autoclave")
    bullets(doc, [
        "**Incomplete removal of air** \u2014 by far the commonest cause; produces an "
        "air\u2013steam mixture whose temperature is below 121 \u00b0C at 15 psi.",
        "**Overloading or tight packing**, preventing steam circulation and penetration.",
        "**Use of superheated steam** (too dry) or **wet steam** (excessive water content) "
        "\u2014 only **dry saturated steam** sterilizes properly.",
        "**Holding time not observed** \u2014 timing begun before the whole load reached "
        "temperature, or the cycle cut short.",
        "**Failure to open vents** of drums and to loosen container caps.",
        "**Wrapping in impervious material** (e.g. aluminium foil, oil-cloth) which steam "
        "cannot penetrate.",
        "**Faulty gauges, thermostat, gasket or steam trap**; leakage; insufficient water.",
        "**Articles not cleaned** beforehand \u2014 organic matter and grease protect "
        "organisms.",
        "**Wet packs on removal**, which wick contamination from the environment.",
    ])

    h2(doc, "12.4  Dry Heat versus Moist Heat \u2014 The Comparison Table")
    table(doc,
          ["Feature", "Dry heat (hot air oven)", "Moist heat (autoclave)"],
          [["**Mechanism of killing**",
            "**Oxidation** of cell constituents, protein denaturation, charring, and a toxic "
            "rise in electrolyte concentration",
            "**Coagulation and denaturation of proteins**; latent heat of condensation of "
            "steam"],
           ["**Temperature required**", "**Higher** \u2014 160\u2013180 \u00b0C",
            "**Lower** \u2014 121\u2013134 \u00b0C"],
           ["**Time required**", "**Longer** \u2014 30 min to 2 hours holding, plus long "
            "heating and cooling", "**Shorter** \u2014 3 to 20 minutes holding"],
           ["**Penetration**", "**Poor** (air is a bad conductor)",
            "**Excellent** (steam penetrates and condenses)"],
           ["**Efficiency**", "Less efficient", "**More efficient**"],
           ["**Effect on the load**", "Leaves the load **dry**; may char paper and cloth, "
            "blunt and discolour instruments and crack glass on rapid cooling",
            "Leaves the load **moist**; may corrode and blunt steel and cannot be used for "
            "moisture-sensitive items"],
           ["**Best suited for**", "**Oils, fats, waxes, powders, glassware, glass syringes, "
            "metal instruments, closed containers**",
            "**Culture media, aqueous solutions, dressings, linen, gowns, rubber goods, "
            "instruments, laboratory waste**"],
           ["**Biological indicator**", "__Bacillus atrophaeus__",
            "__Geobacillus stearothermophilus__"],
           ["**Chemical indicator**", "Browne's tube No. 3, dry-heat indicator tape",
            "Browne's tube No. 1, autoclave tape, **Bowie\u2013Dick test** (pre-vacuum)"]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 12.4  Dry heat compared with moist heat")

    box(doc, "highyield",
        ["^^121 \u00b0C \u00b7 15 psi \u00b7 15 minutes^^ \u2014 memorise this triad. "
         "15 psi = **1.05 kg/cm\u00b2 \u2248 103 kPa \u2248 1 bar \u2248 2 atmospheres "
         "absolute**.",
         "**Moist heat kills by protein coagulation; dry heat kills by oxidation.**",
         "The **commonest cause of autoclave failure is incomplete removal of air**; the "
         "temperature (not the pressure) is the true index of sterilizing conditions.",
         "**Discarded cultures and contaminated media** are autoclaved at "
         "~~121 \u00b0C for 30\u201360 minutes~~ before disposal \u2014 a longer time than "
         "the routine cycle because of the very high bioburden."])

    chapter_end(doc)



# ===========================================================================
# CHAPTER 13
# ===========================================================================
def chapter_13(doc):
    chapter_title(doc, 13, "Physical Methods \u2014 III : Radiation and Sonic Energy")

    h2(doc, "13.1  Classification of Radiation")
    table(doc,
          ["Type", "Examples", "Mechanism", "Effect"],
          [["**Non-ionising radiation**",
            "**Ultraviolet (UV)** rays, **infrared** rays, microwaves",
            "Low energy, **poor penetration**; UV acts on DNA, infrared and microwaves act "
            "by generating heat",
            "Surface disinfection only"],
           ["**Ionising radiation**",
            "**Gamma rays** (from **Cobalt-60**, caesium-137), **X-rays**, "
            "**electron beams / cathode rays** (accelerated electrons), alpha and beta "
            "particles",
            "High energy; ejects electrons, producing **ions and free radicals** that break "
            "DNA strands",
            "**True sterilization**, with excellent penetration"]],
          header_fill=SH_HEADER_BLUE, align_center_cols=[])

    h2(doc, "13.2  Ultraviolet Radiation")
    table(doc,
          ["Heading", "Details"],
          [["**Source**", "Low-pressure **mercury vapour lamps** (UV or 'germicidal' lamps); "
            "also present in sunlight."],
           ["**Wavelength**",
            "The germicidal range is **200\u2013280 nm (UV-C)**; maximum bactericidal "
            "activity is at ~~253.7 nm (\u2248 254 nm, often quoted as 260 nm)~~, which "
            "corresponds to the **absorption maximum of nucleic acid (DNA) at 260 nm**."],
           ["**Mechanism**",
            "Absorbed by DNA, producing **cross-linking between adjacent thymine bases "
            "\u2014 pyrimidine (thymine) dimers** \u2014 which block replication and "
            "transcription; also causes mutation. Repair is possible by **photo-reactivation "
            "and excision repair**, so sub-lethal doses may allow recovery."],
           ["**Uses**",
            "**Air disinfection** of operation theatres, laminar-flow hoods, biological "
            "safety cabinets, tissue-culture rooms, pharmaceutical filling rooms, "
            "bacteriological laboratories, entry vestibules and hospital isolation rooms "
            "\u00b7 **surface disinfection** of work benches and safety cabinets \u00b7 "
            "**disinfection of drinking water and of waste water** \u00b7 disinfection of "
            "the inside of biosafety cabinets after work."],
           ["**Advantages**",
            "No chemical residue, no toxicity to the article, cheap to run, effective "
            "against bacteria, fungi and viruses (including __M. tuberculosis__ and "
            "SARS-CoV-2) on exposed surfaces."],
           ["**Limitations / disadvantages**",
            "**Very poor penetration** \u2014 does not pass through glass, water films, "
            "paper, cloth, dust, plastics or grease, and acts only on the **surface "
            "directly exposed**; **shadowed areas are unaffected** \u00b7 activity falls "
            "with distance, with the age of the lamp and at low temperature or high "
            "humidity \u00b7 **spores are relatively resistant** \u00b7 organic matter and "
            "dust protect organisms \u00b7 lamps need regular cleaning and output "
            "monitoring."],
           ["**Hazards to staff**",
            "**Conjunctivitis, photokeratitis ('welder's flash'), erythema and burns of "
            "skin**, and a long-term risk of skin cancer; ozone may be produced. "
            "**Lamps must be switched off while people are in the room**, and protective "
            "goggles and clothing worn."]],
          header_fill=SH_HEADER_TEAL)

    box(doc, "highyield",
        "^^UV maximum germicidal wavelength = 253.7 nm (\u2248 254 nm)^^; the mechanism is "
        "the formation of ~~thymine (pyrimidine) dimers in DNA~~. UV is used for "
        "**air and surface disinfection, not for sterilization of instruments**, because "
        "it has **no penetrating power**.")

    h2(doc, "13.3  Ionising Radiation \u2014 'Cold Sterilization'")
    table(doc,
          ["Heading", "Details"],
          [["**Sources**",
            "**Gamma rays from Cobalt-60 (\u2076\u2070Co)** \u2014 the commercial standard; "
            "also caesium-137; **high-energy electron (cathode) beams** from linear "
            "accelerators; **X-rays**."],
           ["**Dose**",
            "The internationally accepted sterilizing dose is ~~25 kGy = 2.5 Mrad~~ "
            "(2.5 megarad); 1 Gy = 1 J/kg and 1 kGy = 0.1 Mrad. Lower doses "
            "(**radurisation, radicidation** at 1\u201310 kGy) are used for food "
            "preservation, and **radappertisation** (> 10 kGy) for commercial sterility."],
           ["**Mechanism**",
            "Ejects electrons from atoms, generating **ions and highly reactive free "
            "radicals (especially hydroxyl radicals from water)** that cause "
            "**single- and double-strand breaks in DNA**, cross-linking and damage to "
            "enzymes and membranes. It is a **non-thermal** process."],
           ["**Uses**",
            "**Industrial, large-scale sterilization of pre-packed single-use disposables:** "
            "^^plastic syringes and needles, IV infusion sets, blood-collection bags and "
            "transfusion sets, catheters, urine bags, surgical gloves, cannulae, "
            "sutures and surgical dressings, petri dishes and plastic labware, dental "
            "items, bone and tissue grafts, heart valves, prosthetic implants, "
            "adhesive dressings^^; also sterilization of some **pharmaceuticals, "
            "ophthalmic ointments, antibiotics, hormones, vitamins and food**, and the "
            "production of some **vaccines**."],
           ["**Advantages**",
            "**Excellent penetration** \u2014 sterilizes articles **already sealed inside "
            "their final packaging**, so there is no risk of recontamination \u00b7 "
            "**no rise in temperature**, therefore ideal for heat-labile plastics and "
            "biological materials \u00b7 **no toxic residue and no need for aeration** "
            "(unlike ethylene oxide) \u00b7 continuous, automated, high-throughput, reliable "
            "and easily validated \u00b7 highly **sporicidal**."],
           ["**Disadvantages**",
            "**Very high capital cost** and elaborate shielding \u2014 available only in "
            "large industrial plants, **never in a hospital** \u00b7 needs trained staff and "
            "strict **radiation protection**, licensing and monitoring \u00b7 may cause "
            "**discoloration, embrittlement and degradation of some plastics (PTFE, "
            "polypropylene) and of glass**, and may produce free radicals or off-flavours in "
            "some drugs and foods \u00b7 public apprehension about irradiated products."],
           ["**Biological indicator**",
            "Spores of ~~__Bacillus pumilus__~~; dosimetry is monitored with "
            "**radiochromic and perspex dosimeters** and colour-change dose indicators."]],
          header_fill=SH_HEADER_GREEN)

    box(doc, "highyield",
        ["^^Disposable plastic syringes, needles, IV sets, gloves, catheters and sutures are "
         "sterilized by GAMMA RADIATION from Cobalt-60 at a dose of 2.5 Mrad (25 kGy) at "
         "the factory.^^ This is one of the most frequently asked facts in the entire unit.",
         "Ionising radiation is called **'cold sterilization'** because there is no "
         "significant rise in temperature.",
         "**Order of increasing resistance to radiation:** vegetative bacteria < moulds and "
         "yeasts < bacterial spores < **viruses (most resistant)**. Note this is "
         "**different** from the order of resistance to heat and chemicals."])

    h2(doc, "13.4  Sonic and Ultrasonic Vibration")
    bullets(doc, [
        "High-frequency sound waves (**> 20 000 cycles per second**) passed through a liquid "
        "produce **cavitation** \u2014 the rapid formation and collapse of microscopic "
        "bubbles \u2014 which disrupts cells mechanically.",
        "**It is not a reliable method of sterilization or disinfection**: many organisms, "
        "and all spores, survive.",
        "Its real and important use is **mechanical cleaning**: the **ultrasonic cleaner "
        "(sonicator)** removes blood, tissue debris and cement from the **joints, hinges, "
        "serrations and lumens of surgical and dental instruments** before they are "
        "sterilized. It is therefore a **pre-sterilization cleaning device** and a "
        "**mechanical method**.",
        "Ultrasonics are also used in the laboratory to **disrupt bacterial cells** in order "
        "to release intracellular enzymes and antigens.",
    ])

    box(doc, "note",
        "Associate ultrasonic waves with ^^cleaning of instruments, not "
        "sterilization^^. They are a **pre-sterilization** step, and they belong to the "
        "**mechanical** group of methods.")

    chapter_end(doc)


# ===========================================================================
# CHAPTER 14
# ===========================================================================
def chapter_14(doc):
    chapter_title(doc, 14, "Mechanical Methods \u2014 Filtration and Physical Removal")

    para(doc, "Mechanical methods **remove** micro-organisms rather than killing them. The "
              "most important of them, and the one always asked about, is **filtration**.")

    h2(doc, "14.1  Filtration \u2014 Principle and Indications")
    box(doc, "definition",
        ["**Principle:** a liquid or a gas is passed through a filter of pore size small "
         "enough to **retain the micro-organisms mechanically** (by sieving), assisted by "
         "**adsorption** onto the filter material and by the electrostatic charge of the "
         "membrane. The organisms are **removed, not killed**.",
         "**Chief indication:** ^^sterilization of heat-labile (thermolabile) fluids^^ that "
         "would be destroyed by autoclaving."])

    bullets(doc, [
        "**Materials sterilized by filtration:** sera and serum-containing media, "
        "**vaccines and toxoids**, bacterial toxins and culture filtrates, **antibiotic "
        "solutions**, **vitamin and hormone solutions**, **urea broth**, sugar solutions, "
        "**heat-labile parenteral (large- and small-volume) solutions**, ophthalmic "
        "solutions, radiopharmaceuticals, tissue-culture media, blood products, "
        "**enzyme preparations**, and **air** (by HEPA filters).",
        "Also used to **separate soluble products of bacterial growth** (exotoxins, "
        "bacteriophage) from the organisms, to **clarify** liquids, and to **concentrate "
        "organisms from large volumes of water, urine or beverages for culture** (the "
        "membrane-filter technique used in water bacteriology).",
    ])

    h2(doc, "14.2  Types of Filters")
    table(doc,
          ["Filter", "Material", "Description and grades", "Uses and remarks"],
          [["**Earthenware candle filters \u2014 Chamberland filter**",
            "**Porcelain (unglazed kaolin / clay)**",
            "Hollow candle-shaped filters; graded **L1 to L13** (Chamberland\u2013Pasteur), "
            "L1 being the coarsest. French in origin.",
            "Water purification and filtration of fluids; largely historical in the "
            "laboratory but the principle survives in domestic candle water filters."],
           ["**Earthenware candle filters \u2014 Berkefeld filter**",
            "**Kieselguhr (diatomaceous earth)**",
            "Graded by porosity as ~~**V (Veil \u2013 coarse), N (Normal \u2013 medium) and "
            "W (Wenig \u2013 fine/dense)**~~. German in origin.",
            "Water purification; the **grades V, N, W are a classic MCQ**."],
           ["**Mandler filter**", "Kieselguhr, asbestos and plaster of Paris", "\u2014",
            "Filtration of fluids."],
           ["**Seitz filter**", "**Asbestos (magnesium silicate) pads**",
            "A single-use **compressed asbestos disc** clamped in a metal mount; the pad is "
            "discarded after use.",
            "Was widely used for sterilizing sera and sugar solutions. Its great "
            "disadvantages are that asbestos is **carcinogenic**, and the pad **adsorbs "
            "protein and alters the fluid**; largely **abandoned** in favour of membranes."],
           ["**Sintered (fritted) glass filter**",
            "**Finely ground borosilicate glass fused into a disc**",
            "Grades numbered by porosity (e.g. No. 5 for bacteria); fused into a funnel.",
            "**Minimal adsorption of protein**, chemically inert, re-usable and cleanable; "
            "but **brittle and expensive**."],
           ["**Membrane filter** (the modern standard)",
            "**Cellulose acetate, cellulose nitrate, mixed cellulose esters, "
            "polycarbonate, PVDF, PTFE, nylon**",
            "Thin (\u2248 150 \u00b5m) discs with a very high proportion of uniform pores. "
            "Common pore sizes: **0.8, 0.45 and ~~0.22 \u00b5m~~**; a **0.22 \u00b5m "
            "membrane is the accepted 'sterilising grade' filter**, while 0.45 \u00b5m is "
            "the standard for **water bacteriology** (coliform counting). Pre-filters and "
            "0.1 \u00b5m membranes are used for mycoplasma.",
            "**The method of choice today** for sterilizing heat-labile pharmaceutical "
            "solutions, and for counting organisms in water. **Advantages:** no "
            "adsorption/alteration of the fluid, disposable, cheap, rapid, allows the "
            "organisms retained to be cultured, and can be integrity-tested "
            "(**bubble-point test**). **Disadvantages:** low capacity and clogs easily, and "
            "membrane rupture would be unnoticed without integrity testing."],
           ["**Syringe filter**", "Membrane in a plastic housing",
            "0.22 or 0.45 \u00b5m, attached to the nozzle of a syringe.",
            "Bedside and small-volume sterilization of drug solutions and of solutions for "
            "cell culture."],
           ["**HEPA filter** \u2014 **H**igh **E**fficiency **P**articulate **A**ir",
            "Pleated glass-fibre / borosilicate microfibre paper",
            "Removes ~~99.97% of particles of 0.3 \u00b5m~~ and above (H13/H14 grades remove "
            "99.95\u201399.995%); works by interception, impaction and diffusion.",
            "**Air sterilization** in operation theatres, **laminar air flow benches**, "
            "biological safety cabinets, pharmaceutical clean rooms, and isolation rooms for "
            "immunocompromised and transplant patients. **ULPA** filters are still finer."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 14.1  Types of filters")

    box(doc, "highyield",
        ["^^0.22 \u00b5m^^ = the sterilising-grade membrane pore size. ^^0.45 \u00b5m^^ = "
         "used for water bacteriology / coliform counts. ^^HEPA = 99.97% of particles "
         "\u2265 0.3 \u00b5m^^.",
         "**Berkefeld grades: V, N, W** (coarse \u2192 fine). **Chamberland: L1\u2013L13**. "
         "**Seitz = asbestos.** **Sintered glass = ground borosilicate glass.**",
         "~~Filtration removes bacteria and fungi but does NOT remove viruses, mycoplasma, "
         "prions, bacterial toxins, endotoxins (pyrogens) or L-forms~~, since these are "
         "smaller than the pore size. Therefore a filtered fluid is **not necessarily "
         "virus-free** \u2014 a very common MCQ."])

    h2(doc, "14.3  Laminar Air Flow and Biological Safety Cabinets")
    bullets(doc, [
        "**Laminar air flow (LAF)** is the flow of HEPA-filtered air in **parallel, "
        "unidirectional streams at a uniform velocity (\u2248 0.45 m/s \u00b1 20%)** so that "
        "particles are swept away without turbulence.",
        "**Horizontal LAF** \u2014 filtered air blows from the back of the cabinet "
        "**towards the operator**. It protects the **product only**, not the worker; it must "
        "**never** be used for infectious material, but is suitable for aseptic dispensing "
        "of sterile non-hazardous preparations and media pouring.",
        "**Vertical LAF** \u2014 filtered air flows downward from the top. Protects both the "
        "product and, in properly designed cabinets, the operator.",
    ])
    table(doc,
          ["Biological safety cabinet", "Air flow and features", "Protects", "Used for"],
          [["**Class I**",
            "Room air is drawn in across the open front at \u2265 0.38 m/s and exhausted "
            "through a HEPA filter. Open-fronted.",
            "**Operator and environment** (not the product)",
            "Low- and moderate-risk work; Biosafety Level 1\u20133 agents."],
           ["**Class II (A1, A2, B1, B2)**",
            "About **70% of the air is recirculated** through a HEPA filter as a vertical "
            "downflow over the work surface, with an inward air curtain at the front "
            "aperture; 30% exhausted through HEPA.",
            "**Operator, environment AND product**",
            "**The commonest type in hospitals and laboratories** \u2014 tissue culture, "
            "microbiology, and **aseptic compounding of sterile and cytotoxic drugs** "
            "(Class II B2 for cytotoxics)."],
           ["**Class III (glove box)**",
            "**Totally enclosed, gas-tight, maintained under negative pressure**; access "
            "only through attached rubber gloves; supply and exhaust air both HEPA-filtered "
            "(exhaust often double-HEPA or incinerated).",
            "**Maximum containment** \u2014 absolute protection",
            "**Biosafety Level 4** agents \u2014 highly dangerous pathogens such as the "
            "Ebola, Marburg, Nipah and Lassa viruses."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 14.2  Biological safety cabinets")

    h2(doc, "14.4  Other Mechanical Methods")
    table(doc,
          ["Method", "How it works and where it is used"],
          [["**Washing, scrubbing and cleaning**",
            "The **most basic and most important** mechanical method. Water, detergent and "
            "friction physically remove organic matter and the great majority of organisms. "
            "**Hand-washing with soap and water for 40\u201360 seconds** is the single most "
            "effective measure for preventing hospital-acquired infection. Cleaning is "
            "**always the first step** before any disinfection or sterilization."],
           ["**Wet mopping, damp dusting and wiping**",
            "Used for floors, walls, furniture and surfaces. **Dry sweeping and dry dusting "
            "are forbidden in hospitals** because they raise infected dust into the air; "
            "always use damp or wet methods, ideally with a detergent\u2013disinfectant, "
            "and clean from the cleanest to the dirtiest area."],
           ["**Ultrasonic cleaner (sonicator) and washer-disinfector**",
            "Removes debris from hinges, box-joints, serrations and lumens of instruments "
            "before sterilization; the **automated washer-disinfector** combines washing "
            "with thermal disinfection (e.g. 90 \u00b0C for 1 min) and is the standard first "
            "stage in a modern CSSD."],
           ["**Sedimentation and centrifugation**",
            "Sedimentation (with or without coagulants such as alum) removes suspended "
            "matter and a large proportion of organisms from water in the **plain and "
            "chemical sedimentation** stages of water purification; centrifugation "
            "concentrates or removes cells in the laboratory."],
           ["**Slow and rapid sand filtration of water**",
            "The **biological (slow sand / Jewel) filter** removes **98\u201399% of "
            "bacteria**, largely through the **__Schmutzdecke__ ('dirt blanket')** \u2014 a "
            "slimy, biologically active zoogleal layer on the sand surface; "
            "**rapid sand (mechanical) filters** are faster but less efficient "
            "bacteriologically and must be followed by chlorination."],
           ["**Straining, air filtration and dilution**",
            "Straining through cloth (e.g. of drinking water to remove __Cyclops__ in "
            "guinea-worm control); dilution and ventilation reduce the concentration of "
            "airborne organisms."]],
          header_fill=SH_HEADER_GREEN)

    box(doc, "note",
        "In classifications, remember that **filtration is placed under MECHANICAL methods** "
        "(some textbooks list it under physical methods) because it acts by **physical "
        "removal**, not by killing. Washing, scrubbing, dusting, mopping, sedimentation and "
        "ultrasonic cleaning are the other mechanical methods.")

    chapter_end(doc)



# ===========================================================================
# CHAPTER 15
# ===========================================================================
def chapter_15(doc):
    chapter_title(doc, 15, "Chemical Methods of Sterilization and Disinfection")

    h2(doc, "15.1  Properties of an Ideal Disinfectant")
    bullets(doc, [
        "**Wide (broad) spectrum** \u2014 active against bacteria, spores, mycobacteria, "
        "fungi, viruses and protozoa.",
        "**Rapid action** at a low, economical concentration, with a **long shelf life** and "
        "stability in storage and in dilution.",
        "**Not inactivated by organic matter**, soap, hard water, plastics or rubber.",
        "**Non-toxic, non-irritant, non-allergenic and non-carcinogenic** to man and "
        "animals.",
        "**Non-corrosive** to metals and not damaging to rubber, plastics, fabrics, paint or "
        "cement.",
        "**Soluble in water**, able to penetrate crevices and organic matter, and with good "
        "**wetting (surface-active) properties**.",
        "**Odourless or pleasant smelling**, colourless and non-staining.",
        "**Cheap, readily available and easy to use**; **environmentally safe and "
        "biodegradable**.",
        "Ideally **leaves a residual effect** and has a **visible indicator** of activity.",
    ])
    box(doc, "note",
        "**No single disinfectant possesses all of these properties** \u2014 the ideal "
        "disinfectant does not exist, and the choice always involves a compromise between "
        "efficacy, safety, material compatibility and cost.")

    h2(doc, "15.2  Classification of Chemical Agents")
    table(doc,
          ["Group", "Members"],
          [["**1. Alcohols**", "Ethyl alcohol (ethanol), isopropyl alcohol, methyl alcohol "
            "(methanol), benzyl alcohol, trichlorobutanol"],
           ["**2. Aldehydes**", "Formaldehyde (formalin), **glutaraldehyde**, "
            "ortho-phthalaldehyde (OPA), glyoxal"],
           ["**3. Phenols and related compounds**",
            "Phenol (carbolic acid), cresol, **Lysol**, **chloroxylenol (Dettol)**, "
            "hexachlorophene, thymol, **chlorhexidine** (a bisbiguanide), "
            "triclosan, resorcinol, creosote"],
           ["**4. Halogens**",
            "**Chlorine** and chlorine-releasing agents (bleaching powder, sodium "
            "hypochlorite, chloramine, sodium dichloroisocyanurate, chlorine dioxide, "
            "halazone); **Iodine** and **iodophors** (povidone-iodine)"],
           ["**5. Oxidising agents (peroxygens)**",
            "**Hydrogen peroxide**, **peracetic acid**, potassium permanganate, benzoyl "
            "peroxide, ozone, sodium perborate"],
           ["**6. Heavy metals and their salts**",
            "**Mercury** \u2014 mercuric chloride, mercurochrome, thiomersal (merthiolate), "
            "phenyl mercuric nitrate; **Silver** \u2014 silver nitrate, silver "
            "sulphadiazine, colloidal silver; **Copper** \u2014 copper sulphate; zinc salts"],
           ["**7. Surface-active agents (surfactants / detergents)**",
            "**Cationic \u2014 quaternary ammonium compounds (QACs)**: cetrimide, "
            "cetylpyridinium chloride, benzalkonium chloride (Zephiran), "
            "**Savlon** (cetrimide + chlorhexidine); **Anionic** \u2014 soaps, "
            "alkyl sulphates, sodium lauryl sulphate; **Non-ionic** \u2014 Tweens (mostly "
            "inactive, may even support growth); **Amphoteric (ampholytic)** \u2014 'Tego' "
            "compounds"],
           ["**8. Dyes**",
            "**Aniline dyes** \u2014 crystal violet, gentian violet, brilliant green, "
            "malachite green; **Acridine dyes** \u2014 proflavine, acriflavine, euflavine, "
            "aminacrine"],
           ["**9. Acids and alkalies**",
            "Mineral acids (HCl, H\u2082SO\u2084), organic acids (benzoic, acetic, "
            "salicylic, propionic, sorbic, undecylenic acid), **sodium hydroxide, calcium "
            "oxide (quicklime), lime, washing soda**"],
           ["**10. Gaseous (vapour-phase) agents**",
            "**Ethylene oxide (EtO)**, formaldehyde gas, **beta-propiolactone (BPL)**, "
            "hydrogen peroxide vapour and **plasma**, ozone, chlorine dioxide, "
            "propylene oxide, methyl bromide"],
           ["**11. Miscellaneous**",
            "Ethylene glycol and propylene glycol vapour (air disinfection), "
            "8-hydroxyquinoline, salts of heavy metals in paints, essential oils"]],
          header_fill=SH_HEADER_PURPLE,
          caption="Table 15.1  Classification of chemical disinfectants")

    # ---------------- Alcohols
    h2(doc, "15.3  Alcohols")
    table(doc,
          ["Heading", "Details"],
          [["**Agents and strength**",
            "**Ethyl alcohol (ethanol) 60\u201390%, optimally ~~70%~~ (v/v)**; "
            "**isopropyl alcohol 60\u201380%** (slightly more potent and less volatile, but "
            "more toxic and with a stronger odour); **methyl alcohol** (methanol) "
            "\u2014 used only for **fungicidal action on incubators and inoculation hoods**, "
            "since it is toxic and neuro-/retinotoxic."],
           ["**Mechanism**",
            "**Denaturation and precipitation of proteins**, dissolution of membrane lipids "
            "and dehydration of the cell. ^^Water is essential for protein denaturation^^, "
            "which is why **70% alcohol is far more effective than absolute (100%) "
            "alcohol** \u2014 a favourite MCQ."],
           ["**Spectrum**",
            "Rapidly kills vegetative bacteria, **__M. tuberculosis__**, fungi and "
            "**lipid-enveloped viruses (HIV, HBV, influenza, SARS-CoV-2)**. "
            "**NOT sporicidal** and poorly active against **non-enveloped viruses "
            "(poliovirus, norovirus, hepatitis A) and protozoal cysts**. Therefore an "
            "**intermediate-level disinfectant**."],
           ["**Uses**",
            "**Skin antiseptic** before injection and venepuncture \u00b7 the basis of "
            "**alcohol-based hand rub** (WHO formulation: 80% ethanol or 75% isopropanol "
            "with hydrogen peroxide and glycerol) \u00b7 disinfection of clinical "
            "thermometers, stethoscope diaphragms, rubber stoppers of multi-dose vials, "
            "ampoule necks and small surfaces \u00b7 **70% alcohol with 0.5\u20132% "
            "chlorhexidine or with iodine (tincture of iodine) for surgical skin "
            "preparation** \u00b7 as a solvent for other antiseptics."],
           ["**Limitations**",
            "**Not sporicidal** \u00b7 **inactivated by organic matter** and must be applied "
            "to clean skin \u00b7 **evaporates rapidly**, so the required contact time may "
            "not be achieved \u00b7 **inflammable \u2014 a fire hazard**, and must be dry "
            "before diathermy or cautery \u00b7 **no residual activity** \u00b7 dries, "
            "cracks and irritates the skin, and stings open wounds \u00b7 hardens and "
            "damages rubber, some plastics and the cement of lensed instruments."]],
          header_fill=SH_HEADER_BLUE)

    # ---------------- Aldehydes
    h2(doc, "15.4  Aldehydes")
    h3(doc, "15.4.1  Formaldehyde")
    table(doc,
          ["Heading", "Details"],
          [["**Nature and preparations**",
            "A gas at room temperature, highly soluble in water. **Formalin = a 37\u201340% "
            "w/v aqueous solution of formaldehyde** (often stabilised with methanol). "
            "**10% formalin** (i.e. \u2248 4% formaldehyde) is the standard **histological "
            "fixative**; formaldehyde gas is used for **fumigation**."],
           ["**Mechanism**", "**Alkylation** of the amino, carboxyl, sulphydryl and hydroxyl "
            "groups of proteins and of the amino groups of nucleic acid bases."],
           ["**Spectrum**",
            "**Bactericidal, sporicidal, fungicidal and virucidal** \u2014 a true "
            "**chemisterilant**, though it acts slowly."],
           ["**Uses**",
            "**Fumigation of operation theatres, wards, laboratories, safety cabinets, "
            "sick rooms and ambulances** \u00b7 disinfection of **bedding, mattresses, "
            "blankets, furniture, books, leather and clothing** \u00b7 "
            "**inactivation of viruses and toxins in vaccine production** \u2014 the "
            "preparation of **toxoids** (diphtheria and tetanus), **inactivated polio "
            "(Salk) vaccine** and rabies vaccine \u00b7 preservation of anatomical "
            "specimens \u00b7 **destruction of anthrax spores** in hides and wool \u00b7 "
            "disinfection of instruments (8% formaldehyde in 70% alcohol) and of renal "
            "dialysis equipment \u00b7 **1\u20132% formaldehyde** as a surface "
            "disinfectant."],
           ["**Method of fumigation**",
            "The room is **sealed** (windows, doors, ventilators and exhausts taped) and "
            "cleaned. Then either: **(a)** boil ~~500 ml of formalin with 1000 ml of water "
            "per 1000 cubic feet~~ of room space in an electric boiler; or **(b)** "
            "the **potassium permanganate method** \u2014 add ~~280 ml of formalin to 150 g "
            "of KMnO\u2084 per 1000 cubic feet~~ in a deep, heat-resistant vessel placed on "
            "the floor (the reaction is **violently exothermic and may spatter**, so the "
            "operator leaves immediately). Relative humidity must be **> 60\u201370%** and "
            "the temperature **> 20 \u00b0C**. The room is kept sealed for "
            "**12\u201324 hours** (at least 12 h), then the residual vapour is neutralised "
            "with ~~ammonia (ammonium bicarbonate/ammonium carbonate, \u2248 250 ml of "
            "strong ammonia per litre of formalin used)~~ and the room ventilated for "
            "several hours before it is re-occupied."],
           ["**Disadvantages and hazards**",
            "**Pungent, intensely irritating vapour** causing lacrimation, rhinitis, "
            "conjunctivitis, cough, bronchospasm and asthma \u00b7 skin irritation and "
            "**contact dermatitis/sensitisation** \u00b7 ~~classified as a human carcinogen "
            "(nasopharyngeal carcinoma)~~ \u00b7 **poor penetration** \u2014 acts only on "
            "surfaces reached by the vapour \u00b7 activity falls sharply at low temperature "
            "and low humidity \u00b7 leaves a **white residue of paraformaldehyde** \u00b7 "
            "prolonged sealing and ventilation make the theatre unusable for a day. "
            "Because of these hazards, **formaldehyde fumigation has largely been replaced "
            "by hydrogen peroxide vapour/fogging** and by improved ventilation and HEPA "
            "filtration."]],
          header_fill=SH_HEADER_TEAL)

    h3(doc, "15.4.2  Glutaraldehyde \u2014 The Most Important Liquid Chemisterilant")
    table(doc,
          ["Heading", "Details"],
          [["**Preparation**",
            "A **2% aqueous solution** (trade name **Cidex**). Supplied acidic and "
            "**'activated' just before use by adding the sodium bicarbonate activator** to "
            "bring the pH to **7.5\u20138.5 (alkaline)**, which is necessary for sporicidal "
            "activity. Once activated its **shelf life is about 14 days** (longer for "
            "stabilised formulations); the concentration must be checked with test strips "
            "before each use."],
           ["**Mechanism**", "**Alkylation** of amino, sulphydryl, hydroxyl and carboxyl "
            "groups; it also cross-links proteins of the cell wall and membrane. It is a "
            "**dialdehyde**, more potent than formaldehyde."],
           ["**Contact times**",
            "^^High-level disinfection: 20\u201345 minutes at 20\u201325 \u00b0C^^ (20 min "
            "is the common Indian/CDC figure; 45 min at 25 \u00b0C by some standards). "
            "^^Sterilization (sporicidal): 3\u201310 hours^^ (often quoted as 10 h to kill "
            "all spores). **__M. tuberculosis__ requires at least 20 minutes.**"],
           ["**Uses**",
            "^^The agent of choice for heat-sensitive instruments^^ \u2014 "
            "**flexible fibre-optic endoscopes (gastroscopes, colonoscopes, "
            "bronchoscopes, cystoscopes, laparoscopes), arthroscopes, "
            "anaesthetic and respiratory equipment, face masks and corrugated tubing, "
            "plastic and rubber goods, dialysers, dental instruments, thermometers, "
            "polythene tubing, metal instruments including sharp cutting edges and "
            "lensed instruments**."],
           ["**Advantages**",
            "**Sporicidal, tuberculocidal, virucidal and fungicidal** \u00b7 **relatively "
            "unaffected by organic matter (blood, protein)** \u2014 a major advantage over "
            "hypochlorites \u00b7 **non-corrosive to metals, and does not damage rubber, "
            "plastics, lenses or the cement of instruments** \u00b7 active over a wide "
            "temperature range."],
           ["**Disadvantages and precautions**",
            "**Irritant and sensitising** \u2014 causes dermatitis, conjunctivitis, "
            "rhinitis, epistaxis and **occupational asthma**; must be used in a "
            "**covered container in a well-ventilated area or fume cupboard**, with gloves, "
            "gown, eye protection and a mask \u00b7 slow sporicidal action \u00b7 "
            "**expensive**; unstable once activated \u00b7 **coagulates blood and fixes "
            "tissue**, so instruments must be **scrupulously cleaned first** \u00b7 "
            "**instruments must be thoroughly rinsed with sterile water** before use, as "
            "residues cause chemical colitis and keratitis \u00b7 may leave a sticky residue "
            "and stain the hands brown \u00b7 __Mycobacterium chelonae__ and some "
            "glutaraldehyde-resistant mycobacteria have caused outbreaks."],
           ["**Ortho-phthalaldehyde (OPA) 0.55%**",
            "A newer aromatic dialdehyde (**Cidex OPA**); achieves high-level disinfection in "
            "**5\u201312 minutes at 20\u201325 \u00b0C**, needs no activation, is "
            "**less irritant with a milder odour** and is more stable, but is **more "
            "expensive** and **stains skin, clothing and surfaces grey-green**."]],
          header_fill=SH_HEADER_GREEN)

    box(doc, "highyield",
        ["^^2% alkaline glutaraldehyde (Cidex) is the disinfectant of choice for endoscopes^^ "
         "\u2014 HLD in **20 minutes**, sterilization in **3\u201310 hours**.",
         "It must be **activated with sodium bicarbonate** to pH 7.5\u20138.5; activated "
         "shelf life \u2248 **14 days**.",
         "Both formaldehyde and glutaraldehyde act by ~~alkylation~~; so do ethylene oxide "
         "and beta-propiolactone."])

    # ---------------- Phenols
    h2(doc, "15.5  Phenols and Related Compounds")
    table(doc,
          ["Agent", "Strength and features", "Uses"],
          [["**Phenol (carbolic acid)**",
            "The **first widely used surgical antiseptic**, introduced by ^^Joseph Lister "
            "(1867)^^, who sprayed carbolic acid in the operating theatre and is regarded as "
            "the **father of antiseptic surgery**. Used as a **1\u20135% solution**; it is "
            "the **reference standard against which other disinfectants are compared "
            "(phenol coefficient)**. Bactericidal and fungicidal but **not sporicidal**; "
            "poorly active against non-enveloped viruses.",
            "Disinfection of **sputum, faeces, urine, pus and laboratory discard jars "
            "(5%)**; disinfection of drains and floors. **Too caustic and toxic for skin "
            "use.**"],
           ["**Cresol (and Lysol)**",
            "Cresol is a methyl phenol, **3\u201310 times more powerful than phenol**; "
            "**Lysol** is a 50% solution of cresol in soap (a saponified cresol), used at "
            "**2\u20135%**. Cheap, with a strong smell, and **retains activity in the "
            "presence of organic matter** better than most agents. Caustic to skin.",
            "Disinfection of **floors, walls, drains, sinks, bed-pans, urinals, spittoons, "
            "furniture, ambulances and excreta**; the classic hospital 'carbolisation'."],
           ["**Chloroxylenol (Dettol)**",
            "A halogenated phenol; **much less toxic and irritant** than phenol and cresol, "
            "with a pleasant smell; usually used as a **4.8% concentrate diluted for use**. "
            "Its great weakness is that it is **relatively weak, is inactivated by hard "
            "water and organic matter, and __Pseudomonas aeruginosa__ can survive and even "
            "multiply in dilute solutions**.",
            "Domestic antiseptic; skin and wound cleansing, first aid, floors and "
            "surfaces. Not a hospital-grade disinfectant."],
           ["**Hexachlorophene**",
            "A bisphenol, highly active against **Gram-positive** organisms, especially "
            "**staphylococci**; used in **3% soaps and detergents**. It **accumulates on "
            "the skin** giving a persistent effect, but is **absorbed through the skin and "
            "is neurotoxic**, having caused **vacuolar encephalopathy in neonates** \u2014 "
            "hence **routine bathing of newborns with it is prohibited**.",
            "Surgical hand scrub; control of staphylococcal outbreaks in nurseries "
            "(restricted use only)."],
           ["**Chlorhexidine (a bisbiguanide, not a true phenol)**",
            "Available as the **gluconate or acetate**: **0.5% in 70% alcohol** for "
            "pre-operative skin preparation, **2\u20134% detergent scrub (Hibiscrub)** for "
            "surgical hand disinfection, **0.2% mouthwash**, **0.05\u20130.1% for bladder "
            "irrigation and wound cleaning**, and 0.5\u20131% dusting powder. Most active at "
            "**alkaline pH**; has **excellent substantivity (persistent residual activity on "
            "skin)** and **low irritancy**. Active against Gram-positive and (less so) "
            "Gram-negative bacteria; **NOT sporicidal, NOT tuberculocidal**, poor against "
            "non-enveloped viruses; **inactivated by soaps, anionic detergents and hard "
            "water**. **Ototoxic (avoid in the middle ear) and neurotoxic (avoid contact "
            "with brain, meninges and eye)**; can cause anaphylaxis rarely.",
            "^^The first choice for surgical hand scrub, pre-operative skin preparation, "
            "central-line and umbilical cord care, oral hygiene and bladder irrigation.^^ "
            "**2% chlorhexidine in 70% alcohol is now the recommended skin antiseptic before "
            "surgery and central-line insertion.**"],
           ["**Triclosan**",
            "A chlorinated bisphenol, **0.3\u20132%**; active mainly against Gram-positive "
            "organisms; used in medicated soaps, hand washes, toothpastes and deodorants. "
            "Concerns exist about **resistance and environmental persistence**.",
            "Hand hygiene products; control of MRSA carriage."],
           ["**Thymol, resorcinol, creosote**",
            "Weaker phenolic derivatives.",
            "Mouth washes, dental preparations, preservation of timber."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 15.2  Phenols and related antiseptics")

    h3(doc, "15.5.1  Testing the Potency of Disinfectants")
    table(doc,
          ["Test", "Principle", "Key point"],
          [["**Phenol coefficient \u2014 Rideal\u2013Walker (RW) test**",
            "The **highest dilution of the test disinfectant** that kills a standard "
            "suspension of ~~__Salmonella typhi__~~ in a given time (2\u00bd, 5, 7\u00bd "
            "and 10 minutes) is divided by the corresponding dilution of **phenol**.",
            "^^Carried out in the ABSENCE of organic matter^^ \u2014 therefore it "
            "**overestimates** the value of a disinfectant in real use. A phenol coefficient "
            "**> 1 means more potent than phenol**."],
           ["**Chick\u2013Martin test**",
            "The same comparison with phenol, but carried out ~~in the PRESENCE of organic "
            "matter~~ (dried human faeces or yeast suspension) and at a fixed contact time "
            "of 30 minutes.",
            "**More realistic** than the RW test and gives a **lower coefficient**. "
            "This contrast \u2014 RW without organic matter, Chick\u2013Martin with organic "
            "matter \u2014 is a very common MCQ."],
           ["**Kelsey\u2013Sykes capacity (in-use) test**",
            "Measures the **capacity of a disinfectant to retain its activity when "
            "repeatedly challenged** with successive additions of a bacterial suspension, "
            "with and without organic matter.",
            "Assesses **re-use life** of a working solution."],
           ["**In-use test (Kelsey\u2013Maurer)**",
            "A sample of the disinfectant **actually in use in the ward** is diluted and "
            "cultured to count survivors.",
            "Detects **contaminated disinfectant solutions in the hospital** \u2014 e.g. "
            "__Pseudomonas__ growing in dilute chloroxylenol or QAC."],
           ["**AOAC use-dilution test**",
            "Standard American (Association of Official Analytical Chemists) method using "
            "dried inocula on carriers; also the AOAC **sporicidal** and "
            "**tuberculocidal** tests.",
            "Basis of regulatory label claims."],
           ["**Minimum inhibitory / minimum bactericidal concentration (MIC / MBC)**",
            "Lowest concentration inhibiting or killing the organism.",
            "Used mainly for antibiotics and preservatives."]],
          header_fill=SH_HEADER_TEAL)

    # ---------------- Halogens
    h2(doc, "15.6  Halogens")
    h3(doc, "15.6.1  Chlorine and Chlorine-Releasing Agents")
    table(doc,
          ["Heading", "Details"],
          [["**Mechanism**",
            "In water, chlorine forms **hypochlorous acid (HOCl)**, which liberates "
            "**nascent oxygen** and chlorinates the cell; it is a powerful **oxidising "
            "agent** that destroys enzymes, membranes and nucleic acid. Activity is "
            "expressed as ^^available (free) chlorine in ppm or %^^ and is **greater at "
            "acidic pH** (undissociated HOCl is the active form)."],
           ["**Preparations**",
            "**Bleaching powder (chlorinated lime, calcium hypochlorite)** \u2014 contains "
            "about **33% available chlorine** when fresh, but loses it on storage; "
            "**sodium hypochlorite solution (liquid bleach)** \u2014 commonly supplied at "
            "**4\u20136%** and diluted for use; **stabilised bleach, bleach powder, "
            "chloramine-T, halazone tablets, sodium dichloroisocyanurate (NaDCC) tablets** "
            "(convenient and stable, widely used in hospitals), **chlorine dioxide**, "
            "**chlorine gas** (for water works), **double bleaching powder**."],
           ["**Working strengths (learn these)**",
            "~~1% sodium hypochlorite (10 000 ppm available chlorine)~~ \u2014 for "
            "**blood and body-fluid spills** and for **discard jars for plastic waste** "
            "\u00b7 **5% hypochlorite** \u2014 laboratory discard jars, highly infectious "
            "material \u00b7 **0.5% (5000 ppm)** \u2014 general surface decontamination in "
            "laboratories and for viral haemorrhagic fevers \u00b7 "
            "**0.1% (1000 ppm)** \u2014 routine environmental surfaces, floors, and "
            "non-critical items \u00b7 **0.05\u20130.1%** \u2014 clean surfaces and "
            "toys \u00b7 **0.5\u20135 ppm** \u2014 **chlorination of drinking water** "
            "(minimum **free residual chlorine of 0.5 mg/L for one hour** contact; "
            "**0.5 ppm** is the standard, raised to **\u2265 0.7 ppm during an epidemic**) "
            "\u00b7 **1\u20132 ppm** \u2014 swimming pools \u00b7 "
            "**Horrock's apparatus** is used to determine the **chlorine demand/dose** of a "
            "well."],
           ["**Uses**",
            "**Disinfection of drinking water and swimming pools** \u00b7 "
            "**blood and body-fluid spills** \u00b7 disinfection of floors, sinks, toilets, "
            "bed-pans and surfaces \u00b7 **dairy, food and catering equipment** \u00b7 "
            "**laboratory discard jars** and pipette jars \u00b7 disinfection of "
            "**plastic biomedical waste** before shredding \u00b7 **dental and "
            "endodontic irrigation (2.5\u20135.25% NaOCl)** \u00b7 disinfection of milk "
            "cans and haemodialysis water systems \u00b7 **Dakin's solution and Eusol** for "
            "wound irrigation."],
           ["**Advantages**",
            "Cheap, widely available, **rapid and very broad spectrum \u2014 bactericidal, "
            "virucidal (including HIV, HBV and non-enveloped viruses), fungicidal, "
            "tuberculocidal and, at high strength, sporicidal**; leaves no toxic residue on "
            "surfaces; effective against __C. difficile__ spores at 1000\u20135000 ppm."],
           ["**Disadvantages**",
            "**Rapidly inactivated by organic matter** (blood, pus, faeces) \u2014 so the "
            "surface must be cleaned or a higher concentration used \u00b7 "
            "**corrosive to metals** and damages fabrics, rubber and some plastics \u00b7 "
            "**unstable** \u2014 loses chlorine on exposure to light, heat and air, so "
            "solutions must be **freshly prepared daily** and stored in dark, closed "
            "containers \u00b7 **irritant to skin, eyes and the respiratory tract**; "
            "**bleaches fabrics** \u00b7 ^^must NEVER be mixed with acids (releases toxic "
            "chlorine gas), with ammonia (releases chloramine vapour) or with formaldehyde "
            "(forms a carcinogen)^^ \u00b7 activity falls at alkaline pH \u00b7 "
            "chlorination of organic-rich water produces **trihalomethanes**."]],
          header_fill=SH_HEADER_GREEN)

    h3(doc, "15.6.2  Iodine and Iodophors")
    table(doc,
          ["Preparation", "Composition and strength", "Uses and comments"],
          [["**Aqueous iodine solution (Lugol's iodine)**",
            "5% iodine + 10% potassium iodide in water.",
            "Skin antiseptic; also used in microbiology (Gram's stain, Lugol's iodine for "
            "stool microscopy)."],
           ["**Tincture of iodine**",
            "**2% iodine + 2.4% sodium iodide in 50% alcohol** (strong tincture contains 7% "
            "iodine).",
            "Powerful and rapid skin antiseptic before surgery and venepuncture; but "
            "**stains the skin and clothing, stings, and causes irritation, burns under "
            "occlusion and hypersensitivity**; must be removed with alcohol after the "
            "procedure."],
           ["**Iodophors \u2014 povidone-iodine (PVP-I, Betadine)**",
            "Iodine complexed with the carrier **polyvinylpyrrolidone**, which releases free "
            "iodine slowly. ~~10% povidone-iodine contains 1% available iodine~~ (\u2248 "
            "0.1% free iodine); also supplied as a 7.5% surgical scrub, 5% solution for "
            "mucosa and 2.5% ophthalmic preparation.",
            "^^The most widely used skin and mucous-membrane antiseptic today^^ \u2014 "
            "pre-operative skin preparation and painting, surgical hand scrub, wound and "
            "burn dressing, umbilical cord care, gargles and mouthwash, vaginal pessaries, "
            "**and 2.5% drops for prevention of ophthalmia neonatorum**. "
            "**Advantages over tincture:** much **less irritant and staining**, "
            "water-miscible, sustained release of iodine, pleasant to use. "
            "**Disadvantages:** slower action (needs **2 minutes' contact and must be "
            "allowed to dry**), inactivated by organic matter and by dilution beyond the "
            "optimum, may cause **hypersensitivity and, in neonates or over large burns, "
            "iodine absorption with transient hypothyroidism**; discolours surfaces."]],
          header_fill=SH_HEADER_PURPLE)

    bullets(doc, [
        "**Mechanism of iodine:** iodinates and oxidises proteins, nucleotides and fatty "
        "acids, and blocks hydrogen bonding \u2014 killing rapidly.",
        "**Spectrum:** bactericidal, **tuberculocidal**, virucidal, fungicidal, "
        "amoebicidal and, with prolonged contact, **sporicidal** \u2014 the broadest "
        "spectrum of the common skin antiseptics.",
        "**Contraindications/cautions:** known iodine allergy, pregnancy and lactation "
        "(large areas), neonates, thyroid disease; **do not use on the eye except the "
        "specific ophthalmic preparation**.",
    ])

    # ---------------- Oxidising agents
    h2(doc, "15.7  Oxidising Agents (Peroxygens)")
    table(doc,
          ["Agent", "Strength", "Uses", "Notes"],
          [["**Hydrogen peroxide**",
            "**3% (10 volumes)** for wounds and surfaces; **6% and 7.5%** for high-level "
            "disinfection; **10%** for soft contact lenses; "
            "**30\u201335% (vaporised, VHP)** and **plasma** for sterilization; "
            "**1.5\u20133% mouthwash**",
            "Wound and ear cleaning (mechanical loosening of slough and pus by effervescence), "
            "mouthwash for oral ulcers and gingivitis, disinfection of contact lenses, "
            "ventilators and soft plastics, **decontamination of rooms and safety cabinets "
            "by vapour or fogging**, and (as gas plasma) sterilization of heat-sensitive "
            "instruments",
            "Acts by liberating **free hydroxyl radicals and nascent oxygen**. "
            "Bactericidal, virucidal, fungicidal and, at high concentration, **sporicidal**. "
            "**Decomposed by catalase in tissues and blood** (the fizzing), which limits its "
            "activity on tissue; **unstable \u2014 must be stored cool, dark and in a vented "
            "container**; concentrated solutions are **corrosive and cause skin blanching "
            "and burns**; can cause **surgical emphysema** if instilled into closed cavities."],
           ["**Peracetic acid (peroxyacetic acid)**",
            "**0.2\u20130.35%** (automated systems); 0.08% with hydrogen peroxide",
            "**Automated sterilization of flexible endoscopes, dialysers and dental "
            "instruments** (e.g. the STERIS system, \u2248 30\u201340 \u00b0C for "
            "12\u201330 minutes); food-industry and aseptic-packaging sanitisation",
            "**Very rapid, sporicidal at low temperature and in the presence of organic "
            "matter**; decomposes to harmless acetic acid, water and oxygen \u2014 "
            "**environmentally friendly and leaves no toxic residue**. But it is "
            "**unstable, corrosive to soft metals (copper, brass, bronze, plain steel), "
            "pungent and irritant**, and expensive."],
           ["**Potassium permanganate (KMnO\u2084)**",
            "**1:1000 to 1:10 000** (a pink solution); crystals for fumigation",
            "Disinfection of **water in wells (the classic Indian practice), fruits and "
            "vegetables**, gargles, urethral irrigation, **wet dressings and sitz baths for "
            "weeping skin lesions**, snake-bite (obsolete), and as the oxidiser in "
            "**formaldehyde fumigation**",
            "A powerful oxidising agent; **astringent and deodorising**. "
            "**Rapidly inactivated by organic matter**, **stains skin, nails and fabrics "
            "brown**, irritant in strong solution, and the crystals are a fire/explosion "
            "hazard with glycerol and organic material."],
           ["**Ozone**", "Generated on site; 1\u20134 mg/L in water",
            "**Disinfection of drinking water and of bottled water**, air and surface "
            "decontamination, sterilization chambers",
            "Extremely powerful oxidiser; **leaves no taste, odour or residue and does not "
            "form trihalomethanes**, but has **no residual protective effect**, must be "
            "generated on site, is **costly**, and is **toxic and irritant to the lungs**."],
           ["**Benzoyl peroxide, sodium perborate**", "2.5\u201310%",
            "Acne treatment; oral rinses and denture cleaning", "Mild oxidising agents."]],
          header_fill=SH_HEADER_BLUE)

    # ---------------- Heavy metals
    h2(doc, "15.8  Heavy Metals and Their Salts")
    para(doc, "Heavy metals act by combining with the **sulphydryl (\u2013SH) groups** of "
              "enzymes and by precipitating proteins. Very low concentrations are inhibitory "
              "\u2014 the **oligodynamic action**. Most are **bacteriostatic rather than "
              "bactericidal**, and are **toxic**, so their use has declined greatly.")
    table(doc,
          ["Metal", "Compounds and strength", "Uses", "Limitations"],
          [["**Mercury**",
            "**Mercuric chloride (perchloride of mercury) 1:500\u20131:1000**; "
            "**mercurochrome**; **merthiolate (thiomersal) 1:10 000**; **phenyl mercuric "
            "nitrate/acetate 1:50 000**; ammoniated mercury ointment",
            "Formerly a general disinfectant; **thiomersal and phenylmercuric salts as "
            "preservatives in vaccines, sera, eye drops and biological products**; "
            "mercurochrome as a skin antiseptic",
            "**Highly toxic (nephrotoxic, neurotoxic), corrosive to metals, inactivated by "
            "organic matter, and only bacteriostatic**. Now **largely abandoned**, and "
            "mercury is being **phased out of health care (Minamata Convention)**; mercury "
            "waste must go to **yellow/special collection, never to incineration**."],
           ["**Silver**",
            "**Silver nitrate 1% (Cred\u00e9's prophylaxis)**; **0.5% silver nitrate** for "
            "burns; **1% silver sulphadiazine cream**; **silver-impregnated catheters and "
            "dressings**; colloidal silver",
            "**1% silver nitrate eye drops for the prevention of ophthalmia neonatorum "
            "(gonococcal conjunctivitis of the newborn) \u2014 Cred\u00e9's method**; "
            "**silver sulphadiazine is a standard topical agent for burns**; "
            "antimicrobial dressings, water purification",
            "Causes **chemical conjunctivitis** (hence largely replaced by erythromycin "
            "ointment or povidone-iodine for Cred\u00e9's prophylaxis); **argyria** (grey "
            "pigmentation) on prolonged use; stains; silver nitrate is caustic."],
           ["**Copper**", "**Copper sulphate 1:100 000**; copper\u2013silver ionisation",
            "**Algicide in water tanks, swimming pools and reservoirs**; "
            "**molluscicide against snails** in schistosomiasis control; fungicide in "
            "agriculture (Bordeaux mixture); control of __Legionella__ in water systems",
            "More **fungicidal and algicidal than bactericidal**; toxic to fish and plants."],
           ["**Zinc**", "Zinc sulphate, zinc oxide, zinc undecylenate",
            "Astringent and mild antiseptic in calamine and barrier creams; "
            "antifungal preparations", "Weak activity."]],
          header_fill=SH_HEADER_TEAL)

    # ---------------- Surface active
    h2(doc, "15.9  Surface-Active Agents (Surfactants / Detergents)")
    para(doc, "These molecules have a **hydrophilic (water-loving) head and a hydrophobic "
              "(lipid-loving) tail**, so they concentrate at interfaces, reduce surface "
              "tension and **disorganise the cell membrane**, causing leakage of cell "
              "contents.")
    table(doc,
          ["Class", "Examples", "Activity and uses", "Limitations"],
          [["**Cationic \u2014 quaternary ammonium compounds (QACs)**",
            "**Cetrimide (cetyltrimethylammonium bromide)**, **benzalkonium chloride "
            "(Zephiran)**, cetylpyridinium chloride, **Savlon (cetrimide + "
            "chlorhexidine)**, domiphen bromide. Used at **0.1\u20132%**.",
            "**The most active surfactant group.** Good against **Gram-positive** bacteria, "
            "fungi and **lipid (enveloped) viruses**; also **detergent, deodorant, "
            "low-irritant and non-corrosive** with a pleasant smell. Used for "
            "**cleaning and disinfecting floors, walls, furniture and non-critical "
            "equipment**, skin and wound cleansing, pre-operative skin preparation, "
            "and as **preservatives in eye drops and nasal sprays** (benzalkonium 0.01%). "
            "Cetrimide is also a **selective medium for __Pseudomonas aeruginosa__**.",
            "**LOW-LEVEL disinfectants only.** ^^NOT sporicidal, NOT tuberculocidal, "
            "and inactive against non-enveloped viruses (polio, noro) and __Pseudomonas__^^ "
            "\u00b7 ~~INACTIVATED BY SOAPS AND ANIONIC DETERGENTS, hard water, organic "
            "matter, cotton gauze, cork and some plastics~~ \u00b7 "
            "**__Pseudomonas__ and __Serratia__ can survive and multiply in QAC "
            "solutions**, causing outbreaks \u2014 hence solutions must never be "
            "topped up and must be freshly made."],
           ["**Anionic**",
            "**Soaps** (sodium and potassium salts of fatty acids), alkyl and aryl "
            "sulphates, **sodium lauryl sulphate**, bile salts",
            "Weak antibacterial action, but **excellent cleansing and mechanical removal of "
            "organisms** \u2014 the value of hand-washing with soap and water is chiefly "
            "**mechanical**. Active against some Gram-positives, __Neisseria__, "
            "pneumococci and enveloped viruses.",
            "Very weak germicides; **incompatible with cationic agents**."],
           ["**Non-ionic**", "Tweens (polysorbates), Spans, Triton X",
            "Essentially **no antimicrobial activity**; used as emulsifiers and wetting "
            "agents in pharmacy.",
            "**May actually protect organisms and even support their growth**; they "
            "**neutralise QACs and are used in culture media to inactivate residual "
            "disinfectant**."],
           ["**Amphoteric (ampholytic)**", "'Tego' compounds",
            "Combine the detergency of anionic with some of the germicidal power of cationic "
            "agents; active over a wide pH range and relatively non-toxic; used in the food "
            "industry.", "Expensive; intermediate activity."]],
          header_fill=SH_HEADER_GREEN)

    # ---------------- Dyes
    h2(doc, "15.10  Dyes")
    table(doc,
          ["Group", "Members", "Action and uses"],
          [["**Aniline dyes**",
            "**Crystal violet, gentian violet, brilliant green, malachite green**",
            "Much more active against **Gram-positive** bacteria than Gram-negative, and "
            "active against some fungi; **weak and readily inactivated by pus**. Uses: "
            "**1% gentian violet paint for oral candidiasis, impetigo, superficial fungal "
            "infection and burns**; **selective agents in culture media** (crystal violet "
            "in MacConkey and in blood agar; **malachite green in "
            "L\u00f6wenstein\u2013Jensen medium**; brilliant green in Wilson\u2013Blair). "
            "They stain the skin and clothing."],
           ["**Acridine dyes**",
            "**Proflavine, acriflavine, euflavine, aminacrine, aminoacridine**",
            "Act by **intercalating into DNA** and displacing the purine bases; more active "
            "against **Gram-positive** organisms; **retain activity in the presence of pus "
            "and serum** better than aniline dyes. Uses: **antiseptic for wounds, burns and "
            "ulcers (0.1% acriflavine)**, urethral and bladder irrigation, and as a "
            "mutagen and a curing agent for plasmids in the laboratory. They stain "
            "yellow and may delay wound healing."]],
          header_fill=SH_HEADER_PURPLE)

    # ---------------- acids and alkalies
    h2(doc, "15.11  Acids and Alkalies")
    bullets(doc, [
        "Act by **altering the pH**, denaturing proteins and, for organic acids, by "
        "undissociated molecules penetrating the cell.",
        "**Mineral acids** (hydrochloric, sulphuric) are strongly germicidal but "
        "**corrosive**; used for disinfecting hides in anthrax and for cleaning.",
        "**Organic acids** \u2014 **benzoic acid, sorbic acid, propionic acid, acetic acid, "
        "salicylic acid, undecylenic acid, lactic acid** \u2014 are widely used as "
        "**food and pharmaceutical preservatives** (benzoates in syrups, propionates in "
        "bread, sorbates in foods), as **antifungals** (salicylic and benzoic acid in "
        "Whitfield's ointment, undecylenic acid for tinea pedis), and **1\u20132% acetic "
        "acid for __Pseudomonas__ in burns, ear and urinary infections**. "
        "**Lactic acid vapour** has been used for air disinfection.",
        "**Alkalies** \u2014 **sodium hydroxide, lime (calcium oxide/quicklime), sodium "
        "carbonate (washing soda), soda ash** \u2014 are used for the disinfection of "
        "**animal houses, cattle sheds, drains, floors and premises in anthrax and "
        "foot-and-mouth disease**, for **whitewashing** with lime, and for treating "
        "**prion-contaminated** material (**1 N NaOH for 1 hour, followed by autoclaving**).",
        "**Boric acid** (weak antiseptic, eye washes) and **quicklime/bleaching powder** for "
        "**deep burial and excreta disposal** are also included here.",
    ])

    # ---------------- gaseous
    h2(doc, "15.12  Gaseous Sterilization")
    h3(doc, "15.12.1  Ethylene Oxide (EtO) \u2014 The Most Important Gaseous Sterilant")
    table(doc,
          ["Heading", "Details"],
          [["**Physical nature**",
            "A **colourless gas** with a **sweet, ethereal (fruity) odour**; "
            "**boiling point 10.7 \u00b0C**, so it is stored as a liquid under pressure. "
            "**Highly inflammable and explosive above 3% in air**, therefore supplied "
            "**diluted with an inert carrier \u2014 carbon dioxide (10:90) or "
            "hydrochlorofluorocarbon** \u2014 or used as 100% EtO in small single-use "
            "cartridges within a sealed chamber."],
           ["**Mechanism**",
            "**Alkylation** of the amino, carboxyl, sulphydryl and hydroxyl groups of "
            "proteins and of the bases of nucleic acids, which blocks metabolism and "
            "replication."],
           ["**Spectrum**",
            "**Highly effective against all micro-organisms including spores, mycobacteria, "
            "fungi, all viruses and even some prions** \u2014 a true **sterilant**."],
           ["**Cycle parameters (learn these)**",
            "Concentration ~~450\u20131200 mg/L~~ \u00b7 temperature "
            "~~37\u201363 \u00b0C (commonly 55\u201360 \u00b0C)~~ \u00b7 "
            "**relative humidity ~~30\u201360%~~** (essential \u2014 dry spores are "
            "resistant) \u00b7 exposure time ~~1\u20136 hours (typically 3\u20135 h at "
            "55 \u00b0C; up to 12\u201324 h at lower temperature)~~, followed by "
            "**aeration/degassing for 8\u201312 hours or more** (up to 7 days at room "
            "temperature) to remove residues."],
           ["**Uses**",
            "**Sterilization of heat- and moisture-sensitive articles:** ^^plastic and "
            "rubber disposables (syringes, catheters, endotracheal and tracheostomy tubes), "
            "heart\u2013lung machine and dialyser components, respirators and anaesthetic "
            "equipment, prosthetic implants and heart valves, pacemakers, "
            "fibre-optic endoscopes, cystoscopes, delicate and lensed instruments, "
            "surgical sutures and dressings, single-use medical devices, "
            "bone and tissue grafts, powders, some pharmaceuticals, glassware, "
            "clothing, blankets, mattresses, books, documents, laboratory equipment and "
            "cardiac catheters^^. It is the standard low-temperature industrial and "
            "hospital-CSSD gaseous process."],
           ["**Advantages**",
            "**Sterilizes at low temperature** \u2014 nothing is damaged by heat \u00b7 "
            "**excellent penetration** through paper, cardboard, plastic wrapping, fabric "
            "and lumens, so items can be sterilized **inside their final packaging** \u00b7 "
            "**non-corrosive** to metals and lenses \u00b7 compatible with almost all "
            "materials \u00b7 highly reliable and validatable."],
           ["**Disadvantages and hazards**",
            "^^Highly toxic, mutagenic and CARCINOGENIC^^ (leukaemia, lymphoma; strict "
            "occupational exposure limits) \u00b7 **irritant to skin, eyes and airways, "
            "causing burns, blistering and vesication, headache, nausea and vomiting** "
            "\u00b7 **explosive and inflammable** \u00b7 **very slow \u2014 a long cycle "
            "plus a long compulsory aeration period**, so turnaround is poor \u00b7 "
            "**leaves toxic residues** (EtO, ethylene chlorohydrin and ethylene glycol) that "
            "have caused haemolysis, tracheal and laryngeal burns and anaphylaxis, so "
            "**aeration is mandatory** \u00b7 **absorbed by many plastics and rubber** "
            "\u00b7 **expensive** equipment and gas \u00b7 must not be used for materials "
            "that adsorb it (e.g. some polystyrene) \u00b7 requires trained staff, "
            "monitoring and good ventilation."],
           ["**Sterility control**",
            "**Biological indicator: spores of ~~__Bacillus atrophaeus__~~** (formerly "
            "__B. subtilis__ var. __niger__), placed inside a test pack \u2014 the same "
            "organism used for dry heat. Chemical indicators and residual-gas analysis are "
            "also used."]],
          header_fill=SH_HEADER_BLUE)

    h3(doc, "15.12.2  Other Gaseous Agents")
    table(doc,
          ["Agent", "Conditions", "Uses", "Comments"],
          [["**Formaldehyde gas**",
            "See \u00a715.4.1; > 60% RH, > 20 \u00b0C, 12\u201324 hours",
            "Fumigation of theatres, wards, laboratories, safety cabinets; "
            "disinfection of bedding and books; **LTSF sterilization at 73\u201380 \u00b0C**",
            "Sporicidal but **poor penetration**, intensely irritant, carcinogenic, and "
            "leaves a paraformaldehyde residue; needs ammonia neutralisation."],
           ["**Beta-propiolactone (BPL)**",
            "**0.2% (2 mg/L or \u2248 4\u20135 ml per m\u00b3)** for fumigation; "
            "0.05\u20130.2% in solution; \u2248 2 hours at 24\u201330 \u00b0C with high "
            "humidity",
            "**Fumigation of rooms and laboratories**; **inactivation of viruses in "
            "vaccine production \u2014 rabies, influenza and some inactivated vaccines**; "
            "sterilization of tissue grafts, bone and arterial grafts, and of serum",
            "**More potent than formaldehyde and EtO and leaves less residue**, and is "
            "rapidly hydrolysed to harmless lactic acid; but it has ^^poor penetrating "
            "power and is CARCINOGENIC^^, which limits its use."],
           ["**Hydrogen peroxide gas plasma**",
            "**Vaporised H\u2082O\u2082 (\u2248 58%) excited by radiofrequency or microwave "
            "energy into a low-temperature plasma of free radicals; 45\u201375 minutes at "
            "40\u201350 \u00b0C**",
            "**Sterilization of heat- and moisture-sensitive instruments** \u2014 rigid and "
            "flexible endoscopes, cameras, cables, batteries, plastics and delicate "
            "instruments (the **STERRAD** system)",
            "**Rapid, low temperature, no toxic residue** (breaks down to water and oxygen), "
            "**no aeration needed**, environmentally safe \u2014 an excellent modern "
            "alternative to EtO. **Cannot be used for cellulose (paper, linen, gauze), "
            "powders, liquids or long narrow lumens**, and is expensive; needs special "
            "non-cellulosic (Tyvek) wrap."],
           ["**Hydrogen peroxide vapour (VHP) / fogging**",
            "30\u201335% H\u2082O\u2082 aerosolised into a sealed room",
            "**Terminal decontamination of operation theatres, ICUs, isolation rooms and "
            "safety cabinets** \u2014 the modern replacement for formaldehyde fumigation",
            "Short cycle, rapid re-occupancy, no carcinogenic residue; needs a sealed room "
            "and a validated machine."],
           ["**Ozone**", "6\u201312% in oxygen, \u2248 30\u201340 \u00b0C",
            "Low-temperature sterilization chambers; water treatment",
            "Powerful oxidiser, no residue; oxidises and damages some polymers, rubber and "
            "copper; toxic to inhale."],
           ["**Chlorine dioxide gas**", "Generated on site",
            "Room and equipment decontamination, water treatment",
            "Sporicidal, effective at low concentration; explosive at high concentration, "
            "must be generated on site."],
           ["**Propylene oxide, methyl bromide**", "Similar to EtO",
            "Fumigation of foodstuffs, spices, grain and packaging",
            "Less active than EtO; residues are a concern; methyl bromide is being phased "
            "out (ozone-depleting)."],
           ["**Propylene / ethylene glycol vapour**", "Aerosolised into air",
            "**Air disinfection** of enclosed spaces", "Low toxicity; largely historical."]],
          header_fill=SH_HEADER_TEAL)

    h2(doc, "15.13  Summary \u2014 Choosing a Chemical Agent")
    table(doc,
          ["Purpose", "Agent of choice"],
          [["**Hand hygiene \u2014 routine (clean hands)**",
            "**Alcohol-based hand rub (60\u201380%)** for 20\u201330 seconds"],
           ["**Hand hygiene \u2014 visibly soiled hands**",
            "**Soap and water** for 40\u201360 seconds (alcohol does not work through dirt); "
            "also mandatory for __C. difficile__ and spore risk"],
           ["**Surgical hand scrub**",
            "**4% chlorhexidine gluconate** or **7.5% povidone-iodine** detergent scrub, or "
            "an alcohol-based surgical rub"],
           ["**Pre-operative skin preparation**",
            "**2% chlorhexidine in 70% alcohol** (first choice) or **10% "
            "povidone-iodine**"],
           ["**Skin before injection / venepuncture**", "**70% alcohol swab**, allowed to dry"],
           ["**Endoscopes and other heat-sensitive semi-critical instruments**",
            "**2% alkaline glutaraldehyde (20 min)**, 0.55% OPA or 0.2% peracetic acid"],
           ["**Blood and body-fluid spills**",
            "**1% sodium hypochlorite (10 000 ppm)** \u2014 cover, leave 10 minutes, then "
            "clean"],
           ["**Floors, walls, sinks, bed-pans and general surfaces**",
            "**Phenolic (Lysol 2\u20135%) or 0.1% hypochlorite or a QAC-detergent**"],
           ["**Laboratory discard jars**",
            "**5% phenol or 1\u20135% hypochlorite**, with overnight contact"],
           ["**Drinking water**",
            "**Chlorine** \u2014 minimum free residual **0.5 mg/L after 1 hour** contact"],
           ["**Operation theatre / room decontamination**",
            "**Hydrogen peroxide vapour or fogging** (formaldehyde fumigation is the older "
            "method)"],
           ["**Heat-sensitive plastics, rubber, prostheses and lensed instruments "
            "(sterilization)**",
            "**Ethylene oxide** or **hydrogen peroxide gas plasma**"],
           ["**Wounds and burns**",
            "**Povidone-iodine**, silver sulphadiazine (burns), acriflavine, "
            "hydrogen peroxide for cleaning; **1\u20132% acetic acid for "
            "__Pseudomonas__**"],
           ["**Mucous membranes and eye**",
            "**Povidone-iodine (2.5\u20135%)**, 0.2% chlorhexidine mouthwash; "
            "**never alcohol or phenol**"]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 15.3  Agent of choice for each purpose")

    box(doc, "highyield",
        ["^^70% alcohol > 100% alcohol^^ because water is needed for protein denaturation.",
         "^^QACs are inactivated by soap; chlorhexidine and hypochlorites by organic matter; "
         "glutaraldehyde and phenolics are relatively resistant to organic matter.^^",
         "**Alkylating agents** = formaldehyde, glutaraldehyde, ethylene oxide, "
         "beta-propiolactone. **Oxidising agents** = hydrogen peroxide, peracetic acid, "
         "halogens, KMnO\u2084, ozone, plasma.",
         "**Not sporicidal:** alcohols, QACs, chlorhexidine, phenols (ordinary strengths), "
         "dyes. **Sporicidal:** glutaraldehyde (prolonged), formaldehyde, EtO, "
         "beta-propiolactone, peracetic acid, high-strength hypochlorite and hydrogen "
         "peroxide."])

    chapter_end(doc)



# ===========================================================================
# CHAPTER 16
# ===========================================================================
def chapter_16(doc):
    chapter_title(doc, 16,
                  "Sterilization of Syringes, Glasswares, Apparatus and Hospital Articles")

    para(doc, "This chapter answers the practical question the examiner most often asks: "
              "**'which method for which article?'** The governing rule is always the same "
              "\u2014 ^^clean first, then choose the mildest method that will reliably "
              "sterilize without damaging the article.^^")

    h2(doc, "16.1  The Universal Sequence of Reprocessing")
    table(doc,
          ["Step", "What is done", "Why"],
          [["**1.  Decontamination / pre-cleaning**",
            "Immediately after use, immerse the article in water with a detergent or an "
            "enzymatic cleaner (or 0.5% hypochlorite where indicated). Never allow blood and "
            "protein to dry on the instrument.",
            "Protects the handler and prevents organic matter from drying and hardening."],
           ["**2.  Cleaning**",
            "Manual scrubbing with a brush under water, or an **ultrasonic cleaner** or "
            "**automated washer-disinfector**. Dismantle all detachable parts, open hinges "
            "and box-joints, and **flush all lumens**.",
            "^^The most important single step.^^ No sterilant can be relied upon through "
            "dirt; organic matter shields organisms and neutralises chemicals."],
           ["**3.  Rinsing and drying**",
            "Rinse in clean (preferably distilled or de-ionised) water and dry completely.",
            "Residual detergent interferes with disinfectants; water dilutes chemical agents "
            "and causes corrosion and wet packs."],
           ["**4.  Inspection and maintenance**",
            "Check for cleanliness, damage, cracks, blunt edges and function; lubricate "
            "hinged instruments.",
            "A damaged or dirty instrument must not be packed."],
           ["**5.  Packing and labelling**",
            "Wrap in the appropriate material \u2014 paper, muslin, crepe, non-woven wrap, "
            "**peel pouches** or metal drums/canisters. Label with the contents, the date of "
            "sterilization, the expiry date and the load/batch number, and attach a "
            "**chemical indicator**.",
            "Maintains sterility until use and provides traceability."],
           ["**6.  Sterilization**",
            "By the method appropriate to the article (see \u00a716.6).",
            "\u2014"],
           ["**7.  Cooling, drying and storage**",
            "Allow to cool and dry; store in a clean, dry, dust-free, closed cupboard, "
            "above floor level, away from sinks and traffic; practise **first-in "
            "first-out** stock rotation.",
            "**A wet or torn pack is a contaminated pack.** Sterility is "
            "**event-related**, not merely time-related."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 16.1  The seven steps of reprocessing")

    h2(doc, "16.2  Sterilization of Syringes and Needles")
    h3(doc, "16.2.1  Glass (Re-usable) Syringes")
    numbered(doc, [
        "**Immediately after use**, flush the syringe and needle several times with cold "
        "water (**cold, not hot** \u2014 hot water coagulates blood and protein inside the "
        "barrel), then immerse in a detergent solution.",
        "**Dismantle** the syringe \u2014 separate the **barrel from the plunger** and "
        "remove the needle. A syringe must **never be sterilized assembled**, because "
        "differential expansion of barrel and plunger can crack the glass and steam or hot "
        "air cannot reach the ground-glass surfaces.",
        "**Clean** thoroughly with a brush and detergent, paying attention to the nozzle; "
        "use an ultrasonic cleaner if available. Rinse in distilled water and **dry "
        "completely**.",
        "**Pack** the barrel and plunger separately \u2014 in a **paper wrap, a muslin "
        "pack, a metal syringe canister or an aluminium/metal box**, together with the "
        "needle in its own container.",
        "**Sterilize** by either method:",
        "     \u2022  ^^Hot air oven \u2014 160 \u00b0C for 1\u20132 hours^^ "
        "(the preferred method for glass syringes, since it leaves them dry and does not "
        "corrode the needle), **or**",
        "     \u2022  ^^Autoclave \u2014 121 \u00b0C at 15 psi for 15\u201320 minutes^^ "
        "(barrel and plunger separated, wrapped in muslin).",
        "Allow the oven to **cool below 60 \u00b0C before opening**, or let the autoclaved "
        "pack dry, before removing the syringes.",
        "**Assemble aseptically** only at the moment of use, handling the plunger by its "
        "end and the needle by its hub.",
        "**In an emergency only**, syringes and needles may be **boiled at 100 \u00b0C for "
        "at least 20\u201330 minutes** (add 2% sodium bicarbonate to prevent rusting). This "
        "is **disinfection, not sterilization** \u2014 spores and hepatitis B virus may "
        "survive, so it is **not acceptable for routine injections**.",
    ])

    box(doc, "highyield",
        ["^^Glass syringes: hot air oven at 160 \u00b0C for 1\u20132 hours, with the barrel "
         "and plunger separated^^ \u2014 the classic answer.",
         "^^Disposable plastic syringes and needles: gamma radiation (Cobalt-60, 2.5 Mrad / "
         "25 kGy) or ethylene oxide, done by the manufacturer inside the sealed pack.^^",
         "**Boiling is NOT sterilization** and must not be used for syringes as a routine."])

    h3(doc, "16.2.2  Disposable Plastic Syringes and Needles")
    bullets(doc, [
        "Made of polypropylene or polyethylene, which are **destroyed by heat**; they are "
        "therefore sterilized **at the factory, inside their sealed individual packs**, by "
        "^^gamma irradiation from Cobalt-60 at 2.5 Mrad (25 kGy)^^ or by **ethylene oxide**.",
        "They are **strictly single-use**. **Auto-disable (AD) syringes**, which lock after "
        "one use, and **re-use prevention (RUP)** and **sharps-injury-prevention** syringes "
        "are mandated for immunisation and therapeutic injections under the "
        "**WHO/Government of India injection-safety policy**.",
        "The pack must be checked before use for **intactness, dryness, the sterilization "
        "indicator and the expiry date**; a torn, wet or expired pack must be discarded.",
        "**After use:** ^^never recap, bend or break the needle by hand^^. Cut the hub with "
        "a **needle/hub cutter or needle destroyer at the point of generation**, put the "
        "**needle and sharps into the white translucent puncture-proof container** and the "
        "**plastic barrel into the red bag/container** after disinfection "
        "(see Chapter 17).",
        "**Never re-sterilize a disposable syringe** \u2014 heat distorts it, and it is "
        "impossible to clean reliably.",
    ])

    h2(doc, "16.3  Sterilization of Glasswares")
    h3(doc, "16.3.1  Cleaning of Glassware")
    bullets(doc, [
        "**New glassware** is alkaline; it should be soaked in **1\u20132% hydrochloric "
        "acid or dilute nitric acid overnight**, then rinsed thoroughly in tap water and "
        "finally in distilled water.",
        "**Used glassware** should first be **decontaminated** \u2014 discarded cultures and "
        "contaminated tubes are **autoclaved at 121 \u00b0C for 30\u201360 minutes** or "
        "immersed in a **disinfectant discard jar overnight** \u2014 **before** being "
        "washed.",
        "Wash with a **detergent or soap solution** and a brush, then rinse repeatedly in "
        "tap water and finally **two or three times in distilled water**.",
        "Greasy or heavily soiled glassware is soaked in **chromic acid (dichromate) "
        "cleaning solution** \u2014 potassium dichromate in concentrated sulphuric acid "
        "\u2014 or in an alkaline hypochlorite solution, then rinsed exhaustively. "
        "**Chromic acid is highly corrosive: wear gloves, apron and eye protection, and "
        "always add acid to water, never water to acid.**",
        "**Pipettes** are dropped **tip upwards** into a **pipette jar containing "
        "disinfectant** immediately after use, then washed in a pipette washer.",
        "**Dry** completely in a drying oven or inverted on a rack before sterilization.",
        "Glassware is considered clean when water **drains evenly without leaving droplets "
        "or streaks** on the inner surface.",
    ])

    h3(doc, "16.3.2  Sterilization of Glassware")
    table(doc,
          ["Article", "Preparation", "Method"],
          [["**Test tubes, culture tubes**",
            "Plug the mouth with **non-absorbent cotton wool**, or fit a metal/plastic cap; "
            "bundle and wrap in paper.",
            "**Hot air oven, 160 \u00b0C for 2 hours** (or autoclave 121 \u00b0C/15 min if "
            "they contain media)."],
           ["**Petri dishes**",
            "Stack in **metal canisters or cylindrical tins**, or wrap in stout paper "
            "(a set of 4\u20136 dishes per pack).",
            "**Hot air oven, 160 \u00b0C for 2 hours.** (Disposable plastic petri dishes are "
            "gamma-irradiated by the maker.)"],
           ["**Pipettes (graduated, Pasteur, bacteriological)**",
            "Plug the mouthpiece end with cotton wool; place in a **copper or aluminium "
            "pipette canister** (tip first) or wrap in paper.",
            "**Hot air oven, 160 \u00b0C for 2 hours.**"],
           ["**Flasks, conical flasks, bottles, measuring cylinders (non-graduated), "
            "funnels**",
            "Plug or cap the mouth; wrap the neck in paper; caps must be **loosened** if "
            "autoclaved.",
            "**Hot air oven, 160 \u00b0C for 2 hours**, or **autoclave** if they contain "
            "aqueous media/solutions."],
           ["**Glass syringes**", "Barrel and plunger separated (see \u00a716.2.1).",
            "**Hot air oven 160 \u00b0C/1\u20132 h**, or autoclave."],
           ["**Glass slides and cover slips**",
            "Clean, degrease in alcohol or ether, dry.",
            "**Flaming**, or hot air oven; for used slides, immerse in disinfectant and then "
            "autoclave/discard."],
           ["**Volumetric and graduated glassware** \u2014 volumetric flasks, burettes, "
            "graduated cylinders, calibrated pipettes",
            "\u2014",
            "^^Do NOT use the hot air oven^^ \u2014 the high temperature can distort the "
            "glass and **destroy the calibration**. Use **autoclaving at 121 \u00b0C**, "
            "**chemical disinfection (70% alcohol, glutaraldehyde)** or aseptic rinsing "
            "with a sterile solvent, according to the requirement."],
           ["**Sintered glass filters, glass filter holders**",
            "Clean by back-flushing and soaking in cleaning solution.",
            "**Autoclave, 121 \u00b0C for 15\u201320 minutes.**"],
           ["**Glass ampoules and vials (sealed, containing solutions)**",
            "\u2014",
            "**Autoclave** in the final container, or **filter-sterilize and fill "
            "aseptically** if the contents are heat-labile; empty vials by dry heat "
            "(depyrogenation at **250 \u00b0C for 30 minutes** or 180 \u00b0C for 3 hours "
            "to destroy endotoxin/pyrogens)."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 16.2  Glassware and its sterilization")

    box(doc, "note",
        ["**Why is glassware sterilized by dry heat rather than steam?** Because it is "
         "**heat-stable and moisture-sensitive** \u2014 dry heat leaves it **completely dry** "
         "and ready for use, avoids water spotting, and penetrates the closed canisters and "
         "plugged tubes in which glassware is packed.",
         "**Depyrogenation** (removal of bacterial endotoxin) requires much harsher dry heat "
         "than sterilization \u2014 ~~250 \u00b0C for 30 min~~ \u2014 because endotoxin is "
         "far more heat-stable than the organism itself. Autoclaving does **not** destroy "
         "pyrogens."])

    h2(doc, "16.4  Sterilization of Apparatus, Instruments and Other Hospital Articles")
    table(doc,
          ["Article / apparatus", "Recommended method", "Notes and cautions"],
          [["**Stainless-steel surgical instruments** \u2014 forceps, artery clamps, "
            "retractors, bowls, kidney trays",
            "**Autoclave, 121 \u00b0C/15 psi/15\u201320 min**, or **134 \u00b0C/3\u00bd min** "
            "in a pre-vacuum sterilizer",
            "Open all hinges and box-joints; do not nest bowls tightly; lubricate hinged "
            "instruments after cleaning."],
           ["**Sharp cutting instruments** \u2014 scalpels, blades, scissors, needles, "
            "trocars, dental burs",
            "**Hot air oven (160 \u00b0C/2 h)**, or a **chemical sterilant "
            "(2% glutaraldehyde, 10 h)**; autoclaving is acceptable in modern practice but "
            "repeated cycles dull the edge",
            "^^Repeated moist heat blunts and corrodes cutting edges^^ \u2014 a classic "
            "examination point. Protect tips with silicone guards."],
           ["**Rubber goods** \u2014 surgical gloves, tubing, catheters, drains, bungs, "
            "closures, mackintosh, hot-water bottles",
            "**Autoclave at 115\u2013121 \u00b0C for 15\u201330 min** (a lower temperature "
            "and shorter cycle than for metal), or **ethylene oxide**; new disposables are "
            "**gamma-irradiated**",
            "Rubber **perishes, becomes sticky and loses elasticity** with repeated or "
            "excessive heat; powder gloves lightly, pack them without folding sharply, and "
            "**never use dry heat**. Do not exceed 5\u20136 cycles."],
           ["**Plastic and polythene articles** \u2014 tubing, cannulae, endotracheal and "
            "tracheostomy tubes, suction catheters, urine bags, three-way taps",
            "**Ethylene oxide**, **gamma radiation** (industrial), **hydrogen peroxide gas "
            "plasma**, or **2% glutaraldehyde / LTSF** for re-usable items; "
            "**autoclavable plastics** (polypropylene, PTFE, polycarbonate) may be "
            "autoclaved at 121 \u00b0C",
            "Polystyrene, PVC and polyethylene **melt or distort with heat**. Check the "
            "manufacturer's instructions for every device."],
           ["**Flexible fibre-optic endoscopes** \u2014 gastroscope, colonoscope, "
            "bronchoscope, cystoscope, duodenoscope",
            "**High-level disinfection with 2% alkaline glutaraldehyde for 20 min**, "
            "**0.55% OPA for 5\u201312 min**, or **0.2% peracetic acid** in an automated "
            "endoscope reprocessor; **EtO or H\u2082O\u2082 plasma** when sterilization is "
            "required",
            "**Never autoclave** \u2014 heat destroys the fibre-optic bundles, lens cement "
            "and seals. **Meticulous manual cleaning and brushing of all channels first**, "
            "then a **leak test**; afterwards **rinse with sterile water, flush with "
            "alcohol and dry**, and hang vertically uncoiled. Inadequately dried endoscopes "
            "have caused __Pseudomonas__ and __Mycobacterium__ outbreaks."],
           ["**Rigid endoscopes, laparoscopes, arthroscopes and their cables**",
            "**Autoclave if labelled autoclavable**; otherwise **EtO or hydrogen peroxide "
            "plasma**, or glutaraldehyde",
            "Check with the manufacturer; lensed instruments tolerate EtO and plasma well."],
           ["**Anaesthetic and respiratory equipment** \u2014 face masks, corrugated tubing, "
            "reservoir bags, laryngoscope blades, airways, ventilator circuits",
            "**Autoclave (121 \u00b0C)** or **pasteurising washer-disinfector at "
            "73\u201380 \u00b0C** or **2% glutaraldehyde**; **EtO** for delicate parts; "
            "single-use circuits and **bacterial/viral filters** are now preferred",
            "Laryngoscope blades are **semi-critical \u2014 they need HLD as a minimum**; "
            "the handle needs low-level disinfection. Dry thoroughly before reassembly."],
           ["**Surgical dressings, gauze, cotton, gowns, drapes, linen, caps, masks, towels**",
            "**Autoclave \u2014 pre-vacuum porous-load cycle, 134 \u00b0C for "
            "3\u20133\u00bd min**, or 121 \u00b0C for 15\u201330 min in drums with the "
            "**vents open**",
            "Pack loosely; check the **Bowie\u2013Dick test** daily; **packs must be dry** "
            "on removal. Do not use dry heat \u2014 cloth and paper char above 160 \u00b0C."],
           ["**Culture media** \u2014 nutrient broth and agar, blood agar base, MacConkey, "
            "peptone water",
            "**Autoclave, 121 \u00b0C/15 psi/15\u201320 min**",
            "Special cases: **media with sugars, gelatin, milk or DCA \u2014 free steam at "
            "100 \u00b0C or tyndallisation**; **egg/serum media (LJ, Dorset, "
            "L\u00f6ffler's) \u2014 inspissation at 80\u201385 \u00b0C \u00d7 30 min "
            "\u00d7 3 days**; **urea broth, sera and antibiotic-containing media \u2014 "
            "membrane filtration (0.22 \u00b5m)**; **blood, serum and antibiotic supplements "
            "\u2014 added aseptically to the cooled sterile base at 45\u201350 \u00b0C**."],
           ["**Heat-labile solutions** \u2014 sera, vaccines, toxins, antibiotic, vitamin "
            "and hormone solutions, IV fluids with labile drugs",
            "**Membrane filtration through 0.22 \u00b5m**, with aseptic filling under "
            "**laminar air flow**",
            "Validate the filter (bubble-point test); remember that **viruses, mycoplasma "
            "and pyrogens pass through**."],
           ["**Oils, fats, waxes, greases, liquid paraffin, ointment bases, glycerol, "
            "dusting and sulphonamide powders**",
            "^^Hot air oven, 160 \u00b0C for 2 hours^^ (or 150 \u00b0C for 1 h for some oils)",
            "**Steam cannot penetrate anhydrous and oily materials** \u2014 therefore dry "
            "heat is the only heat option. This is a very common MCQ."],
           ["**Bed-pans, urinals, sputum mugs, kidney dishes, feeding utensils, "
            "measuring jugs**",
            "**Washer-disinfector at 80\u201390 \u00b0C**, boiling, or chemical disinfection "
            "with **1% hypochlorite or a phenolic**", "Non-critical items; cleaning is the "
            "main requirement."],
           ["**Thermometers (clinical)**",
            "Wipe clean, then immerse in **70% alcohol or 2% glutaraldehyde for "
            "10\u201320 minutes**, rinse and dry; use individual or "
            "disposable-sheath thermometers",
            "**Never boil or autoclave a mercury thermometer** \u2014 it will burst. Mercury "
            "thermometers are being replaced by digital ones (Minamata Convention)."],
           ["**Blood-pressure cuff, stethoscope, patient trolley, bed rails, furniture, "
            "floors, walls**",
            "**Low-level disinfection** \u2014 detergent cleaning, 70% alcohol wipe for the "
            "stethoscope diaphragm, phenolic or QAC for surfaces",
            "Non-critical items; **damp dusting only \u2014 never dry sweeping**."],
           ["**Mattresses, pillows, blankets, bedding, books, leather, documents**",
            "**Ethylene oxide**, **formaldehyde fumigation**, sunlight and airing; washable "
            "covers laundered at \u2265 71 \u00b0C",
            "Impervious mattress covers are strongly preferred so that surface disinfection "
            "suffices."],
           ["**Operation theatre \u2014 room, air and surfaces**",
            "Routine **wet mopping and cleaning with a detergent-disinfectant**; "
            "terminal cleaning weekly; **HEPA-filtered laminar air flow with 20\u201325 air "
            "changes per hour and positive pressure**; **UV lamps** when unoccupied; "
            "**hydrogen peroxide vapour/fogging** or **formaldehyde fumigation** for "
            "terminal decontamination; environmental (settle-plate) surveillance",
            "Modern practice relies chiefly on **ventilation, HEPA filtration, discipline "
            "and cleaning** rather than on routine fumigation."],
           ["**Hands of the surgeon and staff**",
            "**Surgical scrub with 4% chlorhexidine or 7.5% povidone-iodine for "
            "3\u20135 minutes**, or an alcohol-based surgical rub; routine care by "
            "**alcohol-based hand rub (20\u201330 s)** or **soap and water "
            "(40\u201360 s)**",
            "^^WHO 'My 5 Moments for Hand Hygiene': (1) before touching a patient, "
            "(2) before a clean/aseptic procedure, (3) after body-fluid exposure risk, "
            "(4) after touching a patient, (5) after touching patient surroundings.^^"],
           ["**Patient's skin and mucosa**",
            "**Povidone-iodine, chlorhexidine\u2013alcohol, 70% alcohol**; "
            "**never phenol, formaldehyde, glutaraldehyde or hypochlorite on tissue**",
            "See Table 15.3."],
           ["**Excreta, sputum, pus, urine, vomit, blood spills**",
            "**Cover a spill with absorbent material, pour 1% hypochlorite (or bleaching "
            "powder), leave 10 minutes, then remove with gloves and clean**; sputum and "
            "faeces \u2014 **5% phenol or 1\u20132% hypochlorite for 1\u20132 hours**, or "
            "autoclave/incinerate",
            "Use gloves, mask, apron and eye protection; treat all body fluids as "
            "potentially infectious (**standard precautions**)."],
           ["**Drinking water**",
            "**Chlorination** (free residual chlorine \u2265 0.5 mg/L after 1 h), "
            "**boiling for 5\u201310 minutes** (the most reliable household method), "
            "filtration, **UV**, ozonation, **SODIS**",
            "For wells, use **bleaching powder with Horrock's apparatus** to find the dose."],
           ["**Milk**", "**Pasteurisation** \u2014 63 \u00b0C/30 min or 72 \u00b0C/"
            "15\u201320 s; UHT", "Checked by the **phosphatase test**."],
           ["**Air**",
            "**HEPA filtration and laminar flow**, ventilation and air changes, **UV "
            "lamps**, chemical aerosols (glycol vapour), dust control",
            "Air-borne organisms travel on dust and droplet nuclei."]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 16.3  Article-wise method of choice")

    h2(doc, "16.5  The Central Sterile Supply Department (CSSD)")
    bullets(doc, [
        "A **single, centralised department** that receives, cleans, packs, sterilizes, "
        "stores and issues all sterile supplies for the whole hospital. Centralisation gives "
        "**better quality control, trained staff, proper monitoring, economy and safety**.",
        "**Layout \u2014 strict one-way (unidirectional) flow from dirty to clean, with "
        "physical separation of zones:** "
        "``receiving & decontamination (dirty) \u2192 washing/ultrasonic/washer-disinfector "
        "\u2192 drying & inspection \u2192 packing & assembly (clean) \u2192 sterilization "
        "\u2192 sterile storage \u2192 issue``. Air pressure is **negative in the "
        "decontamination zone and positive in the clean and sterile zones**.",
        "**Equipment:** washer-disinfectors, ultrasonic cleaners, drying cabinets, sealing "
        "machines, **pre-vacuum steam sterilizers**, hot air ovens, low-temperature "
        "sterilizers (EtO or H\u2082O\u2082 plasma), and trolleys.",
        "**Quality assurance:** daily **Bowie\u2013Dick test**, physical printouts for "
        "every cycle, **chemical indicators in and on every pack**, **weekly (or daily) "
        "biological indicators**, load documentation and **traceability of each pack to the "
        "patient**, plus planned preventive maintenance and validation of every sterilizer.",
        "**Shelf life** depends on the wrap and the storage conditions and is now regarded "
        "as **event-related** \u2014 a pack remains sterile until its integrity is breached "
        "(wet, torn, dropped, opened). Indicative periods: single muslin wrap \u2248 1 week; "
        "double wrap \u2248 7\u201312 weeks; **sealed peel pouches \u2248 6\u201312 "
        "months**.",
        "**Staff safety:** personal protective equipment in the decontamination zone, "
        "**hepatitis B immunisation**, sharps safety, EtO and glutaraldehyde exposure "
        "monitoring, and training.",
    ])

    h2(doc, "16.6  Ready Reckoner \u2014 Article versus Method")
    table(doc,
          ["Method", "Articles"],
          [["**Red heat**", "Inoculating loops and wires, tips of forceps, needles, searing "
            "spatulas"],
           ["**Flaming**", "Mouths of culture tubes, glass slides, cover slips, scalpels"],
           ["**Incineration**", "Soiled dressings, cotton swabs, anatomical and pathological "
            "waste, animal carcasses, placenta, laboratory cultures, expired and cytotoxic "
            "drugs, plaster casts"],
           ["**Hot air oven (160 \u00b0C/2 h)**",
            "**Glassware** (test tubes, petri dishes, pipettes, flasks), **glass syringes**, "
            "metal instruments, sharp cutting instruments, **oils, fats, waxes, liquid "
            "paraffin, glycerol, dusting and sulphonamide powders**, ointment bases, swabs"],
           ["**Autoclave (121 \u00b0C/15 psi/15 min)**",
            "**Culture media**, aqueous and parenteral solutions, **surgical instruments**, "
            "**rubber goods and gloves (115\u2013121 \u00b0C)**, glassware, "
            "autoclavable plastics, **contaminated/discarded cultures and media "
            "(30\u201360 min)**, laboratory waste, sintered glass filters"],
           ["**Autoclave (134 \u00b0C/3\u00bd min, pre-vacuum)**",
            "**Surgical dressings, gowns, drapes, linen, wrapped instrument trays** "
            "(porous loads); **134 \u00b0C for 18 min for prions**"],
           ["**Free steam 100 \u00b0C / tyndallisation**",
            "Culture media containing **sugars, gelatin, milk, DCA, selenite F**"],
           ["**Inspissation (80\u201385 \u00b0C \u00d7 30 min \u00d7 3 days)**",
            "**L\u00f6wenstein\u2013Jensen medium, Dorset egg medium, L\u00f6ffler's serum "
            "slope**"],
           ["**Pasteurisation**", "Milk (63 \u00b0C/30 min or 72 \u00b0C/15\u201320 s); "
            "respiratory equipment (73\u201380 \u00b0C)"],
           ["**Gamma radiation (2.5 Mrad / 25 kGy)**",
            "**Disposable plastic syringes and needles, IV and blood-transfusion sets, "
            "catheters, urine bags, surgical gloves, sutures, petri dishes, bone and "
            "tissue grafts, heart valves, prostheses, adhesive dressings** (industrial, "
            "in the final pack)"],
           ["**Ultraviolet radiation**",
            "**Air and exposed surfaces** \u2014 operation theatres, laminar-flow hoods, "
            "biological safety cabinets, entry vestibules, water treatment"],
           ["**Filtration (0.22 \u00b5m membrane)**",
            "**Sera, vaccines, toxins, antibiotic, vitamin and hormone solutions, "
            "urea broth, heat-labile parenteral and ophthalmic solutions, tissue-culture "
            "media**"],
           ["**HEPA filtration**",
            "**Air** \u2014 operation theatres, laminar air flow, biological safety "
            "cabinets, clean rooms"],
           ["**Ethylene oxide**",
            "**Plastics and rubber disposables, heart\u2013lung machine, dialysers, "
            "prosthetic implants and heart valves, pacemakers, endoscopes, "
            "delicate and lensed instruments, catheters, sutures, "
            "powders, books, blankets, mattresses**"],
           ["**Hydrogen peroxide gas plasma**",
            "Heat- and moisture-sensitive **endoscopes, cameras, cables, batteries, "
            "delicate instruments** (not cellulose, liquids or powders)"],
           ["**2% glutaraldehyde**",
            "**Flexible endoscopes, cystoscopes, anaesthetic and respiratory equipment, "
            "plastic and rubber goods, dialysers, thermometers, lensed and "
            "sharp instruments**"],
           ["**70% alcohol**",
            "**Skin before injection**, clinical thermometers, stethoscope diaphragm, "
            "rubber stoppers of vials, small clean surfaces"],
           ["**1% hypochlorite**",
            "**Blood and body-fluid spills**, plastic biomedical waste, surfaces, "
            "laboratory discard jars (1\u20135%)"],
           ["**5% phenol / 2\u20135% Lysol**",
            "**Sputum, faeces, urine, pus**, laboratory discard jars, floors, drains, "
            "bed-pans, ambulances"]],
          header_fill=SH_HEADER_PURPLE,
          caption="Table 16.4  Method \u2192 Article ready reckoner (revise this table last)")

    chapter_end(doc)



# ===========================================================================
# CHAPTER 17
# ===========================================================================
def chapter_17(doc):
    chapter_title(doc, 17,
                  "Disposal of Contaminated Media and Biomedical Waste Management")

    h2(doc, "17.1  Disposal of Contaminated Culture Media and Laboratory Material")
    para(doc, "Used culture media, plates and specimens carry an enormous bioburden of live, "
              "often pathogenic organisms. The cardinal rule is: ^^decontaminate FIRST, "
              "then discard^^. Contaminated material must **never** be washed, thrown away "
              "or poured down a sink before it has been made safe.")

    table(doc,
          ["Material", "Method of decontamination", "Then"],
          [["**Used culture plates, slopes, broths and contaminated media**",
            "^^Autoclave at 121 \u00b0C (15 psi) for 30\u201360 minutes^^ \u2014 a longer "
            "holding time than the routine 15-minute cycle because the bioburden is very "
            "high and the load is bulky. Place the plates in an **autoclavable bag or a "
            "leak-proof metal discard bin**, not stacked tightly.",
            "After autoclaving: the agar is melted and poured off (into a collection "
            "container, **not down the drain, since agar solidifies and blocks the pipes**); "
            "**glass petri dishes are washed and re-sterilized**; "
            "**disposable plastic plates are shredded and disposed of as red-category "
            "waste** (or, if the rules of the establishment require, as yellow-category "
            "microbiology waste for incineration)."],
           ["**Media that cannot be autoclaved, or where no autoclave is available**",
            "**Incineration** (the method of choice for microbiology and biotechnology "
            "waste under the Indian rules), or **chemical disinfection** by immersing in "
            "**1\u20135% sodium hypochlorite or 5% phenol for a minimum of 1\u20132 hours, "
            "preferably overnight**.",
            "Drain the disinfectant to the effluent treatment plant; dispose of the solids "
            "in the appropriate colour-coded bag."],
           ["**Discard jars for pipettes, slides, tubes and small articles**",
            "Jars kept at every bench containing **1\u20135% hypochlorite, 5% phenol or "
            "2% Lysol**, into which the article is **completely immersed immediately after "
            "use** (pipettes tip-upward) and left **overnight**. The solution must be "
            "**changed daily** and must never be merely topped up.",
            "Autoclave the jar and contents, then wash the glassware."],
           ["**Specimens \u2014 blood, serum, urine, stool, sputum, CSF, swabs**",
            "**Autoclave (121 \u00b0C/30\u201360 min)** or add a disinfectant "
            "(**1% hypochlorite or 5% phenol, 1\u20132 hours**); highly infectious specimens "
            "are **incinerated**.",
            "Liquid residues to the ETP; containers as per colour code."],
           ["**Stock cultures, reference strains and vaccine residues; cultures of "
            "Biosafety Level 3\u20134 agents**",
            "**Autoclave (121 \u00b0C for 60 min) on site** \u2014 mandatory "
            "**pre-treatment before the waste leaves the laboratory**; then incinerate.",
            "^^The BMW Rules require that laboratory and microbiology waste, blood samples "
            "and blood bags be **disinfected by autoclaving, microwaving or hydroclaving "
            "ON SITE** before being handed over for final disposal.^^"],
           ["**Sharps contaminated in the laboratory** \u2014 broken glass, slides, "
            "capillary tubes, scalpels",
            "Never handled by hand; swept up with a brush and dustpan or forceps into a "
            "**puncture-proof container**, then **autoclaved or chemically disinfected**.",
            "Contaminated **broken glass \u2192 blue** container; **metal sharps and needles "
            "\u2192 white** translucent puncture-proof container."],
           ["**Liquid waste from the laboratory and from washing**",
            "**Chemical pre-treatment with hypochlorite (for blood-containing effluent) "
            "and/or autoclaving**, then discharged to the **effluent treatment plant "
            "(ETP)** and sewer, conforming to the prescribed effluent standards "
            "(pH 6.5\u20139.0, BOD, COD, suspended solids, oil and grease, "
            "bio-assay limits).",
            "**Never discharge untreated infectious liquid, or chemicals such as chromic "
            "acid, mercury or cytotoxic residues, into the sewer.**"],
           ["**Animal carcasses, tissues and anatomical waste**",
            "**Incineration** (or deep burial where permitted).",
            "Yellow category."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 17.1  Disposal of contaminated media and laboratory material")

    box(doc, "highyield",
        ["^^Contaminated / discarded culture media are autoclaved at 121 \u00b0C for "
         "30\u201360 minutes before disposal^^ \u2014 note that this is **longer** than the "
         "15-minute cycle used to sterilize fresh media.",
         "**Laboratory and microbiology waste must be pre-treated (autoclaved, microwaved or "
         "hydroclaved) on site** before it leaves the laboratory \u2014 a specific "
         "requirement of the BMW Rules, 2016.",
         "**Molten agar must never be poured down the sink** \u2014 it solidifies and blocks "
         "the drain."])

    h2(doc, "17.2  Biomedical Waste \u2014 Definition and Magnitude")
    defn(doc, "Biomedical waste (BMW Rules, 2016)",
         "Any waste which is **generated during the diagnosis, treatment or immunisation of "
         "human beings or animals, or in research activities pertaining thereto, or in the "
         "production or testing of biologicals**, or in any health camp, including the "
         "categories mentioned in Schedule I of the Rules.")
    bullets(doc, [
        "The governing law in India is the ^^Bio-Medical Waste Management Rules, 2016^^ "
        "(notified on 28 March 2016 under the **Environment (Protection) Act, 1986**), as "
        "**amended in 2018 and 2019**. They replaced the Bio-Medical Waste (Management and "
        "Handling) Rules, 1998.",
        "Of the total waste generated in a hospital, only about **15\u201325% is "
        "hazardous/infectious**; the remaining **75\u201385% is general, non-hazardous "
        "waste** similar to domestic refuse. **Mixing the two converts the whole lot into "
        "hazardous waste** \u2014 which is why **segregation at the point of generation** is "
        "the single most important step in the whole system.",
        "The regulatory authorities are the **Central Pollution Control Board (CPCB)** and "
        "the **State Pollution Control Boards / Pollution Control Committees**, which grant "
        "**authorisation**; the prescribed authority for a health-care facility is the "
        "SPCB/PCC.",
        "**Hazards of poor management:** transmission of **hepatitis B, hepatitis C and "
        "HIV** through needle-stick injury (the greatest occupational risk), other "
        "infections, injuries to waste handlers and rag-pickers, **repackaging and illegal "
        "resale of used syringes and gloves**, environmental pollution with dioxins, furans "
        "and mercury, and antimicrobial resistance.",
    ])

    h2(doc, "17.3  Colour Coding and Categories \u2014 BMW Rules, 2016")
    para(doc, "The 1998 rules had **10 categories**; the 2016 rules simplified these into "
              "**four colour-coded categories**. This table is the most examinable single "
              "item in the chapter.")
    table(doc,
          ["Colour / container", "Waste included", "Treatment and disposal"],
          [["~~YELLOW~~\n**(yellow non-chlorinated plastic bag)**",
            "**(a) Human anatomical waste** \u2014 tissues, organs, body parts, placenta. "
            "**(b) Animal anatomical waste.** "
            "**(c) Soiled waste** \u2014 items contaminated with blood, body fluids, or "
            "blood-soaked cotton, dressings, plaster casts, linen, beddings. "
            "**(d) Expired or discarded medicines** including cytotoxic drugs. "
            "**(e) Chemical waste** (solid and liquid) \u2014 discarded disinfectants, "
            "chemicals used in production of biologicals. "
            "**(f) Discarded linen, mattresses and beddings contaminated with blood or body "
            "fluid.** "
            "**(g) Microbiology, biotechnology and other clinical laboratory waste** \u2014 "
            "**blood bags, laboratory cultures, stocks of micro-organisms, live or "
            "attenuated vaccines, culture dishes, devices used to transfer cultures.**",
            "**Incineration** (\u2265 1200 \u00b0C for cytotoxic waste), **plasma "
            "pyrolysis** or **deep burial** (deep burial only in towns with a population "
            "below 5 lakh and in rural areas). "
            "**Laboratory, microbiology, blood-sample and blood-bag waste must first be "
            "pre-treated on site by autoclaving/microwaving/hydroclaving.** "
            "Chemical liquid waste \u2192 pre-treatment then ETP. "
            "**Cytotoxic waste \u2192 incineration at \u2265 1200 \u00b0C, or return to the "
            "manufacturer, or encapsulation.** **Never** autoclave or land-fill cytotoxic "
            "waste."],
           ["~~RED~~\n**(red non-chlorinated plastic bag or container)**",
            "**Contaminated recyclable waste generated from disposable items** \u2014 "
            "**tubing, bottles, intravenous tubes and sets, catheters, urine bags, "
            "syringes (without needles and with the fixed needle cut off), vacutainers with "
            "the needle cut, and gloves.**",
            "**Autoclaving, microwaving or hydroclaving**, followed by **mutilation / "
            "shredding**, and then sent to a **registered / authorised recycler** or for "
            "energy recovery. **Treated waste must not be sent to a landfill.**"],
           ["~~WHITE (translucent)~~\n**(puncture-proof, leak-proof, tamper-proof "
            "container)**",
            "**Waste sharps including metals** \u2014 **needles, syringes with fixed "
            "needles, needles from needle-tip cutters or burners, scalpels, blades, "
            "and any contaminated sharp object that may cause puncture or cut**, including "
            "both used and discarded/unused sharps.",
            "**Autoclaving or dry-heat sterilization** followed by **shredding, mutilation, "
            "or encapsulation in a metal container or cement concrete**, and finally "
            "**disposal in a sharps pit, a concrete sharps pit, or sent to a metal "
            "smelter/authorised recycler**."],
           ["~~BLUE~~\n**(cardboard box with a blue marking, containing a puncture-proof "
            "container)**",
            "**(a) Glassware** \u2014 **broken, discarded and contaminated glass, including "
            "medicine vials and ampoules** (except those contaminated with cytotoxic "
            "drugs, which go to yellow). "
            "**(b) Metallic body implants.**",
            "**Disinfection by soaking in 1% hypochlorite, or autoclaving / microwaving / "
            "hydroclaving**, then sent for **recycling** to an authorised glass or metal "
            "recycler."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 17.2  The four colour-coded categories (BMW Rules, 2016)")

    box(doc, "mnemonic",
        ["^^**Y**ellow = burn it^^ (incinerate) \u00b7 ^^**R**ed = **R**ecycle the plastic^^ "
         "\u00b7 ^^**W**hite = the sharps that make you bleed^^ \u00b7 "
         "^^**B**lue = **B**ottles, **B**roken glass and **B**ody implants^^.",
         "**Key discriminators:** a syringe **with its needle still attached \u2192 WHITE**; "
         "a syringe **whose needle has been cut off \u2192 RED**. "
         "A **glass vial \u2192 BLUE**; a **cytotoxic-contaminated vial \u2192 YELLOW**. "
         "**Gloves \u2192 RED.** **Placenta and soiled dressings \u2192 YELLOW.** "
         "**Laboratory cultures \u2192 YELLOW** (after on-site pre-treatment)."])

    h2(doc, "17.4  Treatment Technologies and Their Standards")
    table(doc,
          ["Technology", "Operating standard", "Used for / remarks"],
          [["**Incineration**",
            "**Primary chamber 800 \u00b1 50 \u00b0C**; **secondary chamber "
            "1050 \u00b1 50 \u00b0C** with a **gas residence time of at least 2 seconds**; "
            "stack height \u2265 30 m; continuous emission monitoring; "
            "**\u2265 1200 \u00b0C for cytotoxic waste**",
            "**Yellow category** \u2014 anatomical, soiled, expired medicines, laboratory "
            "waste. ^^Chlorinated plastics (PVC), mercury, radioactive material, "
            "halogenated chemicals and pressurised containers must NEVER be incinerated^^ "
            "\u2014 they generate **dioxins and furans** or explode. Ash is disposed of in "
            "a secured landfill."],
           ["**Autoclaving**",
            "**Gravity flow:** 121 \u00b0C & 15 psi for **60 min**, or 135 \u00b0C & 31 psi "
            "for **45 min**, or 149 \u00b0C & 52 psi for **30 min**. "
            "**Vacuum type:** 121 \u00b0C & 15 psi for **45 min**. Validated "
            "**weekly with __Geobacillus stearothermophilus__ spores** (a 4-log\u2081\u2080 "
            "reduction is required) and monitored with chemical indicators for every batch.",
            "**Red and white categories, and on-site pre-treatment of laboratory waste.** "
            "Not for anatomical, cytotoxic, volatile chemical or radioactive waste."],
           ["**Microwaving**",
            "Frequency **2450 MHz**, wavelength 12.24 cm; the waste must reach a minimum of "
            "**97.5 \u00b0C** throughout for **at least 30 minutes**; a 4-log reduction of "
            "__B. atrophaeus__ spores must be demonstrated",
            "Alternative to autoclaving for red/white waste. **Not for anatomical, "
            "cytotoxic, radioactive or large metal items.**"],
           ["**Hydroclaving**",
            "Similar to autoclaving but with continuous mechanical mixing and fragmentation "
            "of the waste (e.g. 121 \u00b0C for 20 min, 111 \u00b0C for 30 min)",
            "Combined treatment and volume reduction."],
           ["**Chemical disinfection**",
            "**1% sodium hypochlorite** (or an equivalent), with adequate contact time and "
            "full immersion",
            "Blue-category glassware, liquid waste, spills, and surfaces. Note that "
            "**chemical treatment of plastics before shredding is now discouraged in favour "
            "of autoclaving**."],
           ["**Deep burial**",
            "A pit **1.5\u20132 m deep**, half filled with waste, then covered with "
            "**lime** and finally with **at least 50 cm of soil**; sited away from "
            "habitation and from any water source, on impermeable soil with a low water "
            "table, fenced and with records maintained",
            "^^Permitted ONLY for towns with a population of less than 5 lakh and for rural "
            "areas^^, and only for yellow-category anatomical waste where no CBWTF is "
            "accessible."],
           ["**Plasma pyrolysis / gasification**",
            "Very high temperature (thousands of \u00b0C) in an oxygen-starved environment, "
            "which breaks the waste into elemental gases and slag",
            "An environmentally superior alternative to incineration; permitted for "
            "yellow-category waste."],
           ["**Shredding / mutilation / encapsulation / inertisation**",
            "Mechanical destruction of form so that items **cannot be reused**; "
            "encapsulation in a metal drum or cement concrete; inertisation by mixing with "
            "cement and lime",
            "**Mandatory after disinfection of red and white waste**, to prevent illegal "
            "repackaging and resale. Encapsulation and sharps pits are used for sharps and "
            "for cytotoxic residues."],
           ["**Sharps pit**",
            "A circular or rectangular **concrete-lined, covered pit** into which "
            "disinfected sharps are dropped through a pipe",
            "For sharps in small facilities without access to a CBWTF."],
           ["**Common Bio-medical Waste Treatment Facility (CBWTF)**",
            "A shared, authorised facility to which member health-care establishments hand "
            "over their segregated waste; it must be located within a prescribed distance "
            "and collect waste **daily**",
            "^^Every health-care facility must use a CBWTF where one is available within 75 "
            "km; only then may it install its own captive treatment equipment.^^"]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 17.3  Treatment technologies and prescribed standards")

    h2(doc, "17.5  Handling Rules, Duties and Documentation")
    h3(doc, "17.5.1  Segregation, Packaging, Transport and Storage")
    bullets(doc, [
        "**Segregation at the point of generation** into the correct colour-coded container "
        "is the **responsibility of the person generating the waste** \u2014 never of the "
        "sweeper. Bins must be placed **at the bedside/point of use**, foot-operated and "
        "lidded, lined with the correct non-chlorinated bag, and **filled only to "
        "three-quarters**.",
        "Bags and containers must carry the ^^biohazard symbol^^ (yellow, red and white "
        "categories) or the ^^cytotoxic hazard symbol^^ for cytotoxic waste, together with "
        "a label showing the **date, waste category, sender's name, address and contact "
        "details**.",
        "**Bar-coding and global positioning system (GPS) tracking** of bags and of "
        "collection vehicles were made **mandatory** by the 2016 Rules.",
        "**No untreated biomedical waste may be stored beyond ~~48 hours~~**; if longer "
        "storage is unavoidable, the prescribed authority must be informed and the waste "
        "kept refrigerated.",
        "**Transport** within the facility is by **covered, dedicated, labelled, "
        "leak-proof wheeled trolleys** (never by hand or chute) along a **defined route "
        "away from patient-care areas**; off-site transport is only in **authorised, "
        "labelled vehicles** with the manifest system.",
        "**Untreated waste must not be mixed with municipal solid waste**, and **no "
        "biomedical waste may be given to a rag-picker or an unauthorised person**.",
    ])

    h3(doc, "17.5.2  Needle and Sharps Safety")
    bullets(doc, [
        "^^Never recap, bend, break or manipulate a used needle by hand, and never pass a "
        "sharp from hand to hand.^^ Use a **needle/hub cutter or needle destroyer at the "
        "point of generation**.",
        "Dispose of sharps **immediately after use, by the user**, into a **puncture-proof, "
        "leak-proof, tamper-proof white container** placed within arm's reach; **never "
        "overfill beyond three-quarters** and never reach into the container.",
        "Prefer **auto-disable (AD), retractable and safety-engineered devices** and "
        "**needle-free connectors**.",
        "**All health-care staff must be immunised against hepatitis B** and trained "
        "annually.",
        "**After a needle-stick injury:** do **not** squeeze or suck the wound; "
        "**wash immediately with soap and running water** (flush mucosa/eyes with water or "
        "saline); **report at once** and record the incident; assess the source patient; "
        "and start ^^post-exposure prophylaxis (PEP)^^ \u2014 for **HIV, ideally within "
        "2 hours and certainly within 72 hours**, a 28-day course of antiretrovirals; for "
        "**hepatitis B**, hepatitis B immunoglobulin plus vaccine as indicated by the "
        "vaccination and antibody status; follow-up testing at 6 weeks, 3 months and "
        "6 months.",
    ])

    h3(doc, "17.5.3  Duties of the Occupier and Records")
    bullets(doc, [
        "Obtain and renew **authorisation** from the SPCB/PCC; every facility with beds must "
        "be authorised, and a bed-less clinic requires a one-time authorisation.",
        "Ensure **segregation, pre-treatment, safe storage, transport and handing over to a "
        "CBWTF**; **establish a Bar-Code system**; provide **training to all staff at "
        "induction and annually**, and maintain training records.",
        "Provide **personal protective equipment** (gloves, masks, aprons, gowns, boots, "
        "goggles), **immunise all workers against hepatitis B and tetanus**, and arrange "
        "**health check-ups**.",
        "Constitute a **Bio-medical Waste Management Committee** (mandatory for facilities "
        "with 30 beds or more) which meets at least **every six months**.",
        "Maintain **daily records** of waste generated category-wise, and submit an "
        "**annual report to the prescribed authority by 30 June** for the preceding "
        "calendar year.",
        "**Report any major accident** involving biomedical waste immediately, and maintain "
        "an accident register; display the **monthly record on the website** where "
        "applicable.",
        "**Phase out chlorinated plastic bags, gloves and blood bags** (a requirement "
        "introduced by the 2016 Rules) and **stop the use of mercury** equipment.",
        "Ensure that liquid waste is **pre-treated and meets the effluent discharge "
        "standards** before release.",
    ])

    h2(doc, "17.6  Spill Management and Standard Precautions")
    numbered(doc, [
        "**Restrict access** to the area and put on **PPE** \u2014 gloves, mask, apron, and "
        "eye protection.",
        "**Cover the spill** with absorbent material (paper towels, sawdust or absorbent "
        "granules) to prevent aerosolisation and spread.",
        "**Pour a disinfectant** \u2014 **1% sodium hypochlorite (10 000 ppm)** \u2014 from "
        "the **periphery towards the centre** and leave for **at least 10 minutes** "
        "(20\u201330 minutes for a large spill).",
        "**Remove** the absorbed material with forceps or a scoop (never with bare hands; "
        "pick up any glass with a dustpan and brush) and place it in the **yellow bag**.",
        "**Clean** the area with detergent and water, then **disinfect again** and allow to "
        "dry.",
        "**Discard** the PPE appropriately, **wash hands**, and **record the incident**; "
        "replenish the spill kit.",
    ])
    bullets(doc, [
        "**Standard (universal) precautions** apply to **every patient, at all times, "
        "regardless of diagnosis**, on the principle that **all blood and body fluids are "
        "potentially infectious**. They comprise: **hand hygiene**, **appropriate PPE**, "
        "**safe injection practice and sharps handling**, **safe handling of contaminated "
        "equipment, linen and surfaces**, **respiratory hygiene and cough etiquette**, "
        "**patient placement**, and **waste management**.",
        "The **single most effective measure** for preventing health-care-associated "
        "infection remains ^^hand hygiene^^.",
    ])

    h2(doc, "17.7  Pharmacy-Specific Disposal")
    table(doc,
          ["Item", "Correct disposal"],
          [["**Expired, unused, damaged and returned medicines**",
            "**Yellow category \u2014 incineration** (or encapsulation/inertisation). "
            "They must **never** be resold, given away, flushed down a drain or thrown into "
            "municipal waste. Records of destruction must be maintained and, for scheduled "
            "drugs, the prescribed procedure and witnesses followed."],
           ["**Cytotoxic and antineoplastic drugs, their vials, spillage and "
            "contaminated PPE**",
            "**Yellow category with the cytotoxic hazard label \u2014 incineration at "
            "\u2265 1200 \u00b0C**, or **return to the manufacturer**, or encapsulation. "
            "^^Never autoclave, never landfill, never put a cytotoxic vial in the blue "
            "bin.^^ Prepare only in a **Class II B2 biological safety cabinet** with "
            "full PPE, using a closed-system transfer device, and keep a spill kit."],
           ["**Narcotic and psychotropic (NDPS) drugs**",
            "Destroyed only in the presence of the **authorised officer/committee** under "
            "the NDPS Rules, with a certificate of destruction; recorded in the narcotic "
            "register."],
           ["**Empty vials and ampoules (non-cytotoxic)**",
            "**Blue category** \u2014 disinfect and send for glass recycling. Vials that "
            "contained live or attenuated **vaccines** are **yellow** (laboratory/biological "
            "waste)."],
           ["**Half-used vials with residual drug, and reconstituted antibiotics**",
            "Discard the residue as **chemical/pharmaceutical waste \u2014 yellow**; the "
            "glass then goes to blue after rinsing where permissible."],
           ["**Mercury thermometers, sphygmomanometers and dental amalgam**",
            "**Never incinerate.** Collect spilled mercury with a mercury spill kit into a "
            "**sealed, labelled, unbreakable container under water** and hand over to an "
            "authorised hazardous-waste handler; phase out mercury devices."],
           ["**Chemicals \u2014 chromic acid, solvents, reagents, disinfectant concentrates**",
            "**Yellow category chemical waste**; neutralise or pre-treat where specified and "
            "hand over to an authorised handler. **Never pour concentrated chemicals down "
            "the sink.**"],
           ["**Radiopharmaceuticals**",
            "Governed **not** by the BMW Rules but by the **Atomic Energy Regulatory Board "
            "(AERB)** \u2014 decay-in-storage, then disposal under AERB authorisation."],
           ["**Batteries, e-waste and pressurised containers (aerosol inhalers, cylinders)**",
            "Separate streams under the **E-Waste and Battery Waste Management Rules**; "
            "**pressurised containers must never be incinerated** \u2014 they explode."]],
          header_fill=SH_HEADER_GREEN)

    box(doc, "highyield",
        ["^^BMW Rules 2016: 4 colour categories \u2014 Yellow, Red, White (translucent), "
         "Blue.^^ The 1998 rules had **10 categories**.",
         "**Storage limit for untreated waste = 48 hours.** **Annual report due by "
         "30 June.** **BMW committee mandatory for \u2265 30 beds.**",
         "**Incinerator: primary 800 \u00b1 50 \u00b0C, secondary 1050 \u00b1 50 \u00b0C, "
         "gas retention \u2265 2 seconds; cytotoxic \u2265 1200 \u00b0C.**",
         "**BMW autoclave: 121 \u00b0C/15 psi/60 min (gravity) or 45 min (vacuum).** "
         "**Microwave: 2450 MHz, \u2265 97.5 \u00b0C, 30 min.**",
         "**Deep burial: only for population < 5 lakh and rural areas; pit 1.5\u20132 m "
         "deep with lime and \u2265 50 cm soil cover.**"])

    chapter_end(doc)


# ===========================================================================
# CHAPTER 18
# ===========================================================================
def chapter_18(doc):
    chapter_title(doc, 18, "Quick Revision \u2014 Master Tables and Ready Reckoner")

    para(doc, "Revise this chapter last, on the day before the examination. Everything here "
              "has already been explained in the preceding chapters; this is pure recall.")

    h2(doc, "18.1  Temperature and Time \u2014 The Numbers That Must Be Automatic")
    table(doc,
          ["Process", "Temperature", "Time / condition"],
          [["**Autoclave \u2014 standard**", "**121 \u00b0C** at **15 psi** "
            "(1.05 kg/cm\u00b2)", "**15\u201320 minutes**"],
           ["Autoclave \u2014 rapid", "126 \u00b0C at 20 psi", "10 minutes"],
           ["Autoclave \u2014 pre-vacuum porous load", "134 \u00b0C at 30 psi",
            "3\u20133\u00bd minutes"],
           ["Autoclave \u2014 prions (CJD)", "134 \u00b0C", "18 minutes"],
           ["Autoclave \u2014 discarded cultures / contaminated media", "121 \u00b0C",
            "**30\u201360 minutes**"],
           ["Autoclave \u2014 biomedical waste (gravity)", "121 \u00b0C at 15 psi",
            "**60 minutes**"],
           ["Autoclave \u2014 rubber goods", "115\u2013121 \u00b0C", "15\u201330 minutes"],
           ["**Hot air oven \u2014 standard**", "**160 \u00b0C**", "**2 hours**"],
           ["Hot air oven \u2014 alternatives", "170 \u00b0C / 180 \u00b0C / 150 \u00b0C",
            "1 hour / 30 minutes / 2\u00bd hours"],
           ["Hot air oven \u2014 glass syringes", "160 \u00b0C", "1\u20132 hours"],
           ["Depyrogenation (destruction of endotoxin)", "250 \u00b0C", "30 minutes"],
           ["**Incineration**", "Primary **800 \u00b1 50 \u00b0C**; secondary "
            "**1050 \u00b1 50 \u00b0C**", "Gas retention \u2265 2 seconds; cytotoxic "
            "\u2265 1200 \u00b0C"],
           ["Infrared", "180 \u00b0C", "7\u00bd\u201310 minutes"],
           ["**Pasteurisation \u2014 Holder (LTLT)**", "**63 \u00b0C**", "**30 minutes**"],
           ["**Pasteurisation \u2014 Flash (HTST)**", "**72 \u00b0C**",
            "**15\u201320 seconds**"],
           ["Pasteurisation \u2014 UHT", "125\u2013150 \u00b0C", "1\u20135 seconds"],
           ["**Inspissation** (LJ medium)", "**80\u201385 \u00b0C**",
            "**30 min \u00d7 3 successive days**"],
           ["**Tyndallisation**", "**100 \u00b0C** (free steam)",
            "**20\u201345 min \u00d7 3 successive days**"],
           ["Steam at atmospheric pressure (Koch/Arnold)", "100 \u00b0C", "90 minutes"],
           ["**Boiling**", "**100 \u00b0C**", "**10\u201330 minutes** (+2% "
            "NaHCO\u2083)"],
           ["Vaccine bath", "60 \u00b0C", "1 hour"],
           ["Serum bath / complement inactivation", "56 \u00b0C", "1 hour / 30 minutes"],
           ["Low-temperature steam formaldehyde (LTSF)", "73\u201380 \u00b0C",
            "\u2248 2 hours"],
           ["Microwave (BMW)", "\u2265 97.5 \u00b0C at 2450 MHz", "30 minutes"],
           ["**Ethylene oxide**", "**37\u201363 \u00b0C** (usually 55\u201360 \u00b0C), "
            "RH **30\u201360%**, 450\u20131200 mg/L",
            "**1\u20136 hours** + aeration 8\u201312 h or more"],
           ["Hydrogen peroxide gas plasma", "40\u201350 \u00b0C", "45\u201375 minutes"],
           ["**Gamma radiation**", "Ambient (\u2018cold\u2019)",
            "**2.5 Mrad = 25 kGy** from **Cobalt-60**"],
           ["**UV radiation**", "\u2014", "**253.7 nm**, surface/air only"],
           ["**Glutaraldehyde 2% \u2014 HLD**", "20\u201325 \u00b0C", "**20\u201345 minutes**"],
           ["**Glutaraldehyde 2% \u2014 sterilization**", "20\u201325 \u00b0C",
            "**3\u201310 hours**"],
           ["Ortho-phthalaldehyde 0.55%", "20\u201325 \u00b0C", "5\u201312 minutes"],
           ["Formaldehyde fumigation", "> 20 \u00b0C, RH > 60\u201370%",
            "Sealed **12\u201324 hours**, then neutralise with ammonia"],
           ["Hand rub / hand wash", "\u2014",
            "Alcohol rub **20\u201330 s**; soap and water **40\u201360 s**; surgical scrub "
            "**3\u20135 min**"]],
          header_fill=SH_HEADER_BLUE, align_center_cols=[],
          caption="Table 18.1  Master temperature\u2013time table")

    h2(doc, "18.2  Concentrations to Remember")
    table(doc,
          ["Agent", "Concentration", "Use"],
          [["Ethyl alcohol", "**70%** (range 60\u201390%)", "Skin antiseptic, hand rub"],
           ["Isopropyl alcohol", "60\u201380%", "Skin, surfaces"],
           ["Formalin", "**37\u201340% formaldehyde** solution; **10% formalin** for fixation",
            "Fixative, fumigation"],
           ["Glutaraldehyde", "**2%** alkaline (pH 7.5\u20138.5)", "Endoscopes"],
           ["Ortho-phthalaldehyde", "0.55%", "Endoscopes"],
           ["Phenol", "1\u20135% (**5%** for discard jars)", "Excreta, discard jars"],
           ["Lysol / cresol", "2\u20135%", "Floors, drains, bed-pans"],
           ["Chloroxylenol (Dettol)", "4.8% concentrate, diluted", "Domestic antiseptic"],
           ["Chlorhexidine gluconate", "**0.5% in alcohol**; **2\u20134% scrub**; "
            "0.2% mouthwash", "Skin, hands, mouth"],
           ["Hexachlorophene", "3%", "Surgical scrub (restricted)"],
           ["Sodium hypochlorite", "**1% (10 000 ppm)** spills; 5% discard jars; "
            "0.1% surfaces", "Spills, waste, surfaces"],
           ["Bleaching powder", "**33% available chlorine** (fresh)", "Water, excreta"],
           ["Drinking-water chlorination", "**Free residual 0.5 mg/L after 1 h** "
            "(\u2265 0.7 in epidemics)", "Water supply"],
           ["Tincture of iodine", "2% iodine in 50% alcohol", "Skin"],
           ["**Povidone-iodine**", "**10% (= 1% available iodine)**; 7.5% scrub; "
            "2.5% ophthalmic", "Skin, mucosa, wounds"],
           ["Hydrogen peroxide", "**3%** wounds; 6\u20137.5% HLD; 30\u201335% vapour",
            "Wounds, surfaces, rooms"],
           ["Peracetic acid", "0.2\u20130.35%", "Endoscopes, dialysers"],
           ["Potassium permanganate", "1:1000 \u2013 1:10 000", "Wells, dressings, gargles"],
           ["Silver nitrate", "**1%** (Cred\u00e9's); 0.5% burns", "Ophthalmia neonatorum"],
           ["Mercuric chloride", "1:500 \u2013 1:1000", "Obsolete disinfectant"],
           ["Thiomersal", "1:10 000", "Preservative in biologicals"],
           ["Cetrimide / benzalkonium (QAC)", "0.1\u20132%", "Surfaces, skin, preservative"],
           ["Gentian violet", "1%", "Oral thrush, skin"],
           ["Acriflavine", "0.1%", "Wounds, burns"],
           ["Beta-propiolactone", "0.2%", "Fumigation, vaccines"],
           ["Acetic acid", "1\u20132%", "__Pseudomonas__ in burns, ear, urine"]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 18.2  Concentrations of chemical agents")

    h2(doc, "18.3  Who's Who \u2014 Eponyms and Names")
    table(doc,
          ["Name", "Contribution"],
          [["**Joseph Lister** (1867)",
            "Introduced **carbolic acid (phenol)** into surgery \u2014 the **father of "
            "antiseptic surgery**."],
           ["**Louis Pasteur**",
            "**Pasteurisation**; disproved spontaneous generation; the hot air oven bears "
            "his name; rabies and anthrax vaccines."],
           ["**Robert Koch**",
            "**Koch's steamer** (free steam at 100 \u00b0C); Koch's postulates; "
            "the Koch\u2013Henle method of inspissation."],
           ["**John Tyndall**", "**Tyndallisation** \u2014 intermittent sterilization."],
           ["**Charles Chamberland**",
            "The **Chamberland (porcelain) candle filter**, graded L1\u2013L13."],
           ["**Ignaz Semmelweis**",
            "Introduced **hand washing with chlorinated lime** in obstetrics \u2014 the "
            "pioneer of hand hygiene."],
           ["**Earle H. Spaulding**",
            "The **critical / semi-critical / non-critical** classification of instruments."],
           ["**Rideal and Walker**",
            "The **phenol coefficient** test (without organic matter)."],
           ["**Chick and Martin**",
            "The phenol coefficient test **in the presence of organic matter**."],
           ["**Kelsey and Sykes / Kelsey and Maurer**",
            "The **capacity** test and the **in-use** test for disinfectants."],
           ["**Cred\u00e9**", "**1% silver nitrate** eye drops for ophthalmia neonatorum."],
           ["**Florence Nightingale**",
            "Hospital hygiene, ventilation and sanitation; founder of modern nursing."],
           ["**Berkefeld**", "The **kieselguhr candle filter** \u2014 grades V, N, W."],
           ["**Seitz**", "The **asbestos pad filter**."],
           ["**Bowie and Dick**",
            "The **Bowie\u2013Dick test** for steam penetration in a pre-vacuum autoclave."],
           ["**Browne**", "**Browne's tubes** \u2014 chemical indicators that turn green."],
           ["**Horrock**", "**Horrock's apparatus** \u2014 determination of the chlorine "
            "demand of well water."]],
          header_fill=SH_HEADER_GREEN)

    h2(doc, "18.4  One-Line Facts Most Often Asked")
    bullets(doc, [
        "**Most reliable and most widely used method of sterilization** \u2192 "
        "**autoclaving (moist heat under pressure)**.",
        "**Most reliable monitor of sterilization** \u2192 **biological indicator**.",
        "**Most resistant form of microbial life** \u2192 **prions**, then **bacterial "
        "spores**.",
        "**Most resistant organism to radiation** \u2192 **viruses**.",
        "**Most heat-resistant milk pathogen** \u2192 **__Coxiella burnetii__**.",
        "**Commonest cause of autoclave failure** \u2192 **failure to remove air**.",
        "**True index of autoclave performance** \u2192 **temperature**, not pressure.",
        "**Method for oils, fats, waxes and powders** \u2192 **dry heat (hot air oven)**.",
        "**Method for disposable plastic syringes** \u2192 **gamma radiation**.",
        "**Method for glass syringes** \u2192 **hot air oven 160 \u00b0C/1\u20132 h, barrel "
        "and plunger separated**.",
        "**Method for heat-labile sera and vaccines** \u2192 **membrane filtration "
        "(0.22 \u00b5m)**.",
        "**Method for endoscopes** \u2192 **2% glutaraldehyde**.",
        "**Method for prosthetic implants, pacemakers and heart\u2013lung machine** \u2192 "
        "**ethylene oxide**.",
        "**Method for L\u00f6wenstein\u2013Jensen medium** \u2192 **inspissation**.",
        "**Method for media containing sugar or gelatin** \u2192 **tyndallisation / free "
        "steam**.",
        "**Best method for blood spills** \u2192 **1% sodium hypochlorite**.",
        "**Best single measure to prevent hospital infection** \u2192 **hand hygiene**.",
        "**First and most important step before any sterilization** \u2192 **cleaning**.",
        "**Sterility assurance level required** \u2192 **10\u207b\u2076**.",
        "**Sterilising-grade filter pore size** \u2192 **0.22 \u00b5m**.",
        "**HEPA filter efficiency** \u2192 **99.97% of particles \u2265 0.3 \u00b5m**.",
        "**Alcohol concentration of choice** \u2192 **70%**, because water is needed for "
        "protein denaturation.",
        "**Disinfectant inactivated by soap** \u2192 **quaternary ammonium compounds** "
        "(and chlorhexidine).",
        "**Disinfectant least affected by organic matter** \u2192 **glutaraldehyde** "
        "(and phenolics).",
        "**Agent that is carcinogenic yet widely used as a gaseous sterilant** \u2192 "
        "**ethylene oxide** (also formaldehyde and beta-propiolactone).",
        "**Colour bag for a used syringe with the needle cut off** \u2192 **red**; "
        "**with the needle attached** \u2192 **white**.",
        "**Colour bag for a placenta** \u2192 **yellow**; **for a glass vial** \u2192 "
        "**blue**; **for gloves** \u2192 **red**.",
        "**Maximum storage time for untreated biomedical waste** \u2192 **48 hours**.",
    ])

    h2(doc, "18.5  Glossary of Terms")
    table(doc,
          ["Term", "One-line meaning"],
          [["Asepsis", "Practices that keep organisms away from the article or tissue."],
           ["Antisepsis", "Destroying or inhibiting organisms on living tissue."],
           ["Bactericidal", "Kills bacteria."],
           ["Bacteriostatic", "Inhibits multiplication without killing."],
           ["Bioburden", "Number and type of organisms present before treatment."],
           ["Biofilm", "Community of organisms in a polysaccharide matrix on a surface; "
            "highly resistant."],
           ["Cleaning", "Physical removal of soil and organisms."],
           ["Decontamination", "Making an article safe to handle."],
           ["Depyrogenation", "Destruction of bacterial endotoxin (250 \u00b0C/30 min)."],
           ["Disinfection", "Destruction of vegetative pathogens; spores may survive."],
           ["D-value", "Time or dose for a 1-log (90%) reduction."],
           ["Fumigation", "Disinfection of an enclosed space by a gas or vapour."],
           ["Germicide", "Any agent that kills micro-organisms."],
           ["HLD", "High-level disinfection \u2014 kills all but large numbers of spores."],
           ["Oligodynamic action", "Antimicrobial action of very low concentrations of heavy "
            "metals."],
           ["Pasteurisation", "Heating below 100 \u00b0C to kill specified pathogens without "
            "sterilizing."],
           ["Preservative", "Prevents microbial spoilage of a product during storage."],
           ["Pyrogen", "Fever-producing substance, chiefly bacterial endotoxin; heat-stable "
            "and not removed by filtration."],
           ["SAL", "Sterility assurance level; required value 10\u207b\u2076."],
           ["Sanitisation", "Reduction of organisms to a publicly safe level."],
           ["Sporicidal", "Kills bacterial spores."],
           ["Sterilant", "Chemical capable of complete sterilization."],
           ["Sterilization", "Complete destruction or removal of ALL microbial life, "
            "including spores."],
           ["Substantivity", "Persistence of an antiseptic's activity on the skin "
            "(e.g. chlorhexidine)."],
           ["Terminal disinfection", "Disinfection after the patient has been removed."],
           ["Tyndallisation", "Free steam 100 \u00b0C for 20\u201345 min on 3 successive "
            "days."],
           ["Z-value", "Temperature change producing a tenfold change in D-value."]],
          header_fill=SH_HEADER_PURPLE)

    box(doc, "note",
        "**Final revision strategy:** on the last day read only "
        "^^Table 10.1 (definitions), Table 10.4 (resistance ladder), Table 10.6 (biological "
        "indicators), Table 12.3 (pressure\u2013temperature\u2013time), Table 12.4 "
        "(dry vs moist heat), Table 15.3 (agent of choice), Table 16.4 (article \u2192 "
        "method), Table 17.2 (colour coding), and Tables 18.1\u201318.2 (numbers)^^. "
        "For Part I, read Table 3.1 (principles), Tables 8.1\u20138.4 (methods and AV aids) "
        "and Tables 9.1\u20139.2 (dates).")

    chapter_end(doc, last=True)
