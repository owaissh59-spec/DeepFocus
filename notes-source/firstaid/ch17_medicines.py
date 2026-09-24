# -*- coding: utf-8 -*-
"""Chapter 17 - Use of Common Medicines."""


def render(b):
    b.chapter(
        "Use of Common Medicines",
        "Drugs and dosage forms, routes of administration, the rules of giving "
        "medicine, groups of common medicines with their uses, doses, cautions "
        "and side effects, storage, and the dangers of self-medication.",
        syllabus=[
            "Use of common medicines \u2014 definitions, dosage forms, routes of "
            "administration, rules and precautions for giving medicines, "
            "weights and measures, storage and expiry.",
            "Common groups \u2014 analgesics and antipyretics, antiseptics and "
            "disinfectants, antacids, antihistamines, ORS, antibiotics, "
            "antidiarrhoeals, ointments, drops, inhalers and emergency drugs "
            "used in first aid.",
        ])

    # ------------------------------------------------------------------
    b.h2("Basic Terms")
    b.table(
        ["Term", "Meaning"],
        [["**Drug**", "Any substance used in the diagnosis, prevention, "
                     "treatment or cure of disease, or to alter a body function"],
         ["**Medicine**", "A drug prepared in a form fit for administration to "
                          "man (tablet, syrup, injection)"],
         ["**Dose**", "The measured quantity of a medicine to be taken at one "
                      "time; **daily dose** = total in 24 hours"],
         ["**Prescription**", "A written order of a registered medical "
                              "practitioner for a medicine (**Rx**)"],
         ["**Over-the-counter (OTC)**", "Medicines that may be sold without a "
                                        "prescription \u2014 e.g. paracetamol, "
                                        "antacids, ORS, calamine"],
         ["**Schedule H / H1 drug**", "Indian drug law: medicines (most "
                                      "antibiotics, sedatives) that may be sold "
                                      "**only on a doctor's prescription**; "
                                      "marked with **Rx** and a red line on the "
                                      "pack"],
         ["**Generic and brand name**", "Generic = the drug's own name "
                                        "(paracetamol); brand = a company's name "
                                        "(Crocin, Calpol). Generic medicines are "
                                        "cheaper and equally effective"],
         ["**Side effect / adverse reaction**", "An unwanted effect of a medicine "
                                                "taken in the correct dose"],
         ["**Allergy to a medicine**", "Rash, itching, swelling, wheeze or "
                                       "collapse after a drug \u2014 must be "
                                       "**recorded and never given again**"],
         ["**Antidote**", "A substance that counteracts a poison"],
         ["**Expiry date**", "The date after which the medicine must **not** be "
                             "used \u2014 it may be ineffective or harmful"],
         ["**Placebo**", "An inactive preparation given for its psychological "
                         "effect"]],
        weights=[3.4, 9.2])

    # ------------------------------------------------------------------
    b.h2("Dosage Forms and Routes of Administration")
    b.table(
        ["Route", "Forms used", "Notes"],
        [["**Oral (by mouth)**", "Tablet, capsule, syrup, suspension, powder, "
                                "granules, drops, lozenge, ORS",
          "Commonest, safest and cheapest; **never give anything by mouth to an "
          "unconscious, drowsy, convulsing or vomiting casualty**"],
         ["**Sub-lingual (under the tongue)**", "Nitroglycerine/sorbitrate "
                                               "tablet or spray",
          "Very rapid absorption \u2014 used in **angina/heart attack**"],
         ["**Topical (on the skin)**", "Ointment, cream, lotion, gel, powder, "
                                       "paint, spray",
          "For local action \u2014 antiseptics, calamine, burn creams; wash the "
          "hands after applying"],
         ["**Inhalation**", "Metered-dose inhaler, rotahaler, nebuliser, oxygen",
          "**Asthma reliever (salbutamol)**; acts within minutes"],
         ["**Instillation (drops)**", "Eye, ear and nose drops",
          "Check the label \u2014 **eye drops must never be an ear preparation**; "
          "use a separate dropper; discard 4 weeks after opening"],
         ["**Rectal**", "Suppository, enema",
          "Paracetamol suppository in a vomiting child; diazepam for a "
          "prolonged fit (medical direction)"],
         ["**Injection (parenteral)**", "Intramuscular (IM), intravenous (IV), "
                                        "subcutaneous (SC), intradermal (ID)",
          "**Not for a first aider** \u2014 the only exception is the "
          "casualty's own **adrenaline auto-injector (IM in the outer thigh)** "
          "in anaphylaxis"]],
        weights=[2.6, 4.2, 6.0], size=8.8)
    b.h3("Weights, measures and common abbreviations")
    b.table(
        ["Measure / abbreviation", "Equivalent / meaning"],
        [["1 teaspoon (tsp)", "**5 ml**"],
         ["1 dessertspoon", "10 ml"],
         ["1 tablespoon (tbsp)", "**15 ml**"],
         ["1 cup / glass", "About 200\u2013250 ml"],
         ["1 gram (g)", "1,000 milligram (mg)"],
         ["1 litre", "1,000 ml"],
         ["15\u201316 drops", "About 1 ml (with a standard dropper)"],
         ["**OD / BD / TDS / QID**", "Once / twice / three times / four times a "
                                     "day"],
         ["**SOS / PRN**", "\u2018If necessary\u2019 \u2014 only when required"],
         ["**HS**", "At bedtime"],
         ["**AC / PC**", "Before food / after food"],
         ["**STAT**", "At once, immediately"],
         ["**IM / IV / SC / PO**", "Intramuscular / intravenous / subcutaneous / "
                                   "by mouth"]],
        weights=[4.4, 6.2])

    # ------------------------------------------------------------------
    b.h2("Rules and Precautions for Giving Medicines")
    b.box("THE \u2018FIVE RIGHTS\u2019 OF GIVING MEDICINE", [
        "**Right patient** \u2014 confirm the name; never give one person's "
        "medicine to another.",
        "**Right drug** \u2014 read the **label three times**: when you take it "
        "out, before you pour, and when you put it back. Never give a medicine "
        "from an unlabelled or doubtful container.",
        "**Right dose** \u2014 measure exactly with a marked spoon, cup or "
        "syringe; a child's dose is by **age/weight**, never a guess.",
        "**Right route** \u2014 oral, topical, inhaled, drops; an ear drop is "
        "never put in the eye.",
        "**Right time** \u2014 with or without food, at the correct intervals, "
        "for the full course.",
        "Add a sixth: **Right documentation** \u2014 record what was given, how "
        "much and when.",
    ], kind="key")
    b.numbered([
        "A first aider gives **only simple, well-known medicines**, and only to "
        "a **fully conscious** casualty who can swallow. He **never prescribes, "
        "never injects, and never gives a prescription-only (Schedule H) drug**.",
        "**Ask about allergies** (especially to penicillin, sulpha and aspirin) "
        "and about medicines already being taken, **before** giving anything.",
        "**Check the expiry date** and the appearance \u2014 discard discoloured, "
        "cracked, damp, sticky or foul-smelling medicines and cloudy solutions.",
        "**Give with plenty of water** (a full glass), sitting or standing "
        "\u2014 never lying flat; do not crush or open a capsule or an "
        "enteric-coated tablet unless told to.",
        "**Never give anything by mouth** to an unconscious, semi-conscious, "
        "convulsing casualty, to one with an abdominal injury, or when an "
        "operation is likely.",
        "Be extra careful with **children, pregnant and breast-feeding women, "
        "the elderly, and casualties with liver, kidney, heart, asthma or "
        "ulcer disease**.",
        "**Do not mix medicines with alcohol**; warn about drowsiness (do not "
        "drive) with antihistamines and sedatives.",
        "**Complete the full course** of an antibiotic even if the casualty "
        "feels better, and never share or reuse left-over antibiotics.",
        "**Record and report any side effect** and stop the medicine if a rash, "
        "swelling or breathlessness appears \u2014 it may be the start of "
        "**anaphylaxis**.",
        "**Store** medicines in a **cool, dry, dark place, locked and out of "
        "the reach of children**; keep the ones needing refrigeration (insulin, "
        "some eye drops, vaccines) at **2\u20138 \u00b0C**; keep them in their "
        "original containers with the labels intact.",
        "**Dispose** of expired medicines safely \u2014 do not throw them where "
        "children, animals or water sources can reach them; return them to a "
        "pharmacy if possible.",
    ])

    # ------------------------------------------------------------------
    b.h2("Common Medicines Used in First Aid")
    b.h3("A. Analgesics (pain relievers) and antipyretics (fever reducers)")
    b.table(
        ["Medicine", "Use and adult dose", "Cautions and side effects"],
        [["**Paracetamol (acetaminophen)** \u2014 Crocin, Dolo, Calpol",
          "**The safest first-aid analgesic and antipyretic** \u2014 fever, "
          "headache, body ache, toothache, mild pain. Adult **500 mg\u20131 g "
          "every 6\u20138 hours; maximum 3\u20134 g in 24 hours**. "
          "Child **10\u201315 mg/kg per dose**",
          "Overdose causes **fatal liver damage** with very few early symptoms "
          "\u2014 never exceed the dose, never combine two brands containing "
          "paracetamol; avoid in liver disease and with alcohol"],
         ["**Aspirin (acetyl-salicylic acid)** \u2014 Disprin, Ecosprin",
          "Pain, fever, inflammation; **300 mg chewed at once in a suspected "
          "heart attack**; low dose (75\u2013150 mg) daily for heart protection "
          "(on medical advice)",
          "**Never give to a child under 16** (risk of **Reye's syndrome**), nor "
          "in **peptic ulcer, bleeding disorders, dengue, asthma or aspirin "
          "allergy**; causes gastric irritation and bleeding; not to be given in "
          "**stroke** or in a bleeding casualty"],
         ["**Ibuprofen / diclofenac (NSAIDs)** \u2014 Brufen, Voveran",
          "Pain and inflammation of sprains, strains, backache, toothache, joint "
          "pain, period pain; ibuprofen **200\u2013400 mg 8-hourly after food**",
          "**Take after food**; avoid in ulcer, asthma, kidney disease, "
          "pregnancy, dehydration and in those on blood thinners; may cause "
          "acidity and bleeding"],
         ["**Antispasmodic** \u2014 dicyclomine, hyoscine (Cyclopam, Buscopan)",
          "Colicky abdominal pain, period pain",
          "**Never give in undiagnosed abdominal pain** (it masks appendicitis "
          "and other surgical emergencies); causes dry mouth and blurred vision"]],
        weights=[3.0, 5.0, 4.6], size=8.6)
    b.h3("B. Antiseptics and disinfectants")
    b.table(
        ["Preparation", "Use", "Points to remember"],
        [["**Povidone-iodine (Betadine) 5\u201310 %**", "Cleaning skin and "
                                                       "wounds, dog bites, minor "
                                                       "cuts, before dressing",
          "The most useful all-round antiseptic; avoid in iodine allergy, "
          "thyroid disease, large raw areas and in newborns"],
         ["**Chlorhexidine (Savlon) / cetrimide**", "Cleaning wounds and skin, "
                                                    "washing hands",
          "Mild and non-irritant; dilute as directed; do not use in the eye or "
          "ear"],
         ["**Spirit / 70 % alcohol, alcohol swabs**", "Skin disinfection before "
                                                     "injection; cleaning "
                                                     "instruments",
          "**Never pour on an open wound** \u2014 intensely painful and damages "
          "tissue; inflammable"],
         ["**Hydrogen peroxide 3 %**", "Cleaning dirty or infected wounds, "
                                       "loosening crusts, mouth wash (diluted)",
          "Foams on contact; do not use on healing tissue or in deep closed "
          "wounds"],
         ["**Potassium permanganate (KMnO\u2084, \u2018pink lotion\u2019)**",
          "Weak solution (1:10,000, a pale pink colour) for soaking infected "
          "wounds, ulcers and fungal infections of the feet",
          "**Crystals are corrosive and poisonous** \u2014 must be fully "
          "dissolved; stains skin and clothes"],
         ["**Tincture iodine / gentian violet**", "Old-fashioned wound paints",
          "Painful on raw surfaces; largely replaced by povidone-iodine"],
         ["**Soap and clean running water**", "**The best and most important "
                                             "\u2018antiseptic\u2019** for any "
                                             "wound or bite",
          "15 minutes of washing for an animal bite or chemical contamination"],
         ["**Bleaching powder / sodium hypochlorite**", "**Disinfectant** for "
                                                       "floors, toilets, "
                                                       "utensils, water and "
                                                       "spills of blood or "
                                                       "vomit",
          "A **disinfectant kills germs on objects**; an **antiseptic is used on "
          "living tissue** \u2014 do not confuse the two"]],
        weights=[3.0, 4.6, 5.0], size=8.6)
    b.h3("C. Medicines for allergy, stomach and bowel")
    b.table(
        ["Medicine", "Use and dose", "Cautions"],
        [["**Antihistamines** \u2014 chlorpheniramine (Avil) 4 mg, cetirizine "
          "10 mg, loratadine 10 mg",
          "Itching, urticaria/hives, insect stings, allergic rash, hay fever, "
          "mild allergic reaction; **one tablet at night** (cetirizine) or "
          "**8-hourly** (chlorpheniramine)",
          "Cause **drowsiness** (do not drive or operate machinery); "
          "**antihistamines are NOT a substitute for adrenaline in "
          "anaphylaxis**; avoid with alcohol"],
         ["**Antacids** \u2014 magnesium/aluminium hydroxide gel, "
          "calcium carbonate; **ranitidine, omeprazole/pantoprazole**",
          "Heartburn, acidity, gastritis; antacid gel **2 teaspoons after meals "
          "and at bedtime**",
          "**Chest pain is not always acidity** \u2014 think of a heart attack; "
          "antacids interfere with the absorption of other medicines (give "
          "2 hours apart)"],
         ["**ORS (oral rehydration salts)**",
          "**The most important medicine in diarrhoea, vomiting, heat "
          "exhaustion, cholera and burns.** One sachet in **1 litre** of clean "
          "water; give **frequent small sips** after every loose stool "
          "(50\u2013200 ml in children, freely in adults)",
          "Use within **24 hours** of mixing; never make it stronger or weaker; "
          "never use hot water or add sugar/salt to a ready sachet; continue "
          "breast-feeding"],
         ["**Zinc tablets (20 mg)**", "With ORS in childhood diarrhoea for "
                                     "**14 days** \u2014 reduces severity and "
                                     "recurrence", "Give as advised by a doctor"],
         ["**ORS alternatives / home fluids**", "Rice water (*kanji*), lemon "
                                               "water with salt and sugar, "
                                               "coconut water, buttermilk, dal "
                                               "water, curd",
          "Avoid aerated drinks and very sweet juices (they worsen diarrhoea)"],
         ["**Anti-emetic** \u2014 domperidone, ondansetron, promethazine",
          "Vomiting, motion sickness (promethazine/dimenhydrinate 30\u201360 "
          "minutes before travel)",
          "Only on medical advice in children; drowsiness"],
         ["**Anti-diarrhoeal** \u2014 loperamide",
          "Adult travellers' diarrhoea only",
          "==Never give to children==, and never in **dysentery (blood/mucus in "
          "the stool) or high fever** \u2014 it can be dangerous. **Fluid "
          "replacement, not a \u2018stopping\u2019 medicine, is the treatment "
          "of diarrhoea**"],
         ["**Laxative** \u2014 isabgol (psyllium husk), lactulose, bisacodyl",
          "Occasional constipation, with plenty of water and fibre",
          "**Never give a laxative in abdominal pain, vomiting or suspected "
          "appendicitis or obstruction**; avoid habitual use"],
         ["**Oral glucose / sugar / glucose gel / honey**",
          "**Hypoglycaemia**, exhaustion, heat illness \u2014 3\u20134 "
          "teaspoons of glucose or sugar in water",
          "**Only to a fully conscious casualty who can swallow**"]],
        weights=[3.0, 4.8, 4.8], size=8.4)
    b.h3("D. Skin preparations, drops and emergency medicines")
    b.table(
        ["Preparation", "Use", "Cautions"],
        [["**Silver sulphadiazine cream (Silverex)**", "**Burns and scalds** "
                                                      "\u2014 after cooling, on "
                                                      "medical advice",
          "Not on the face; do not apply to a fresh burn before cooling; avoid in "
          "sulpha allergy"],
         ["**Calamine lotion**", "Itching, sunburn, prickly heat, insect bites, "
                                 "chickenpox", "Soothing and safe; shake well; do "
                                               "not apply to broken skin"],
         ["**Antibiotic ointment** \u2014 framycetin, neomycin\u2013bacitracin, "
          "mupirocin", "Minor infected cuts, grazes and boils",
          "Thin layer; stop if a rash develops; **never** put antibiotic ointment "
          "in the eye unless it is an eye preparation"],
         ["**Antifungal cream/powder** \u2014 clotrimazole",
          "Ringworm, athlete's foot, intertrigo", "Apply for 2\u20134 weeks and "
                                                 "keep the area dry"],
         ["**Analgesic balm / spray, ice/hot packs**",
          "Muscle ache, sprains, backache", "**Not** on broken skin, burns or the "
                                           "eyes; use cold for the first "
                                           "48 hours"],
         ["**Eye drops/ointment** \u2014 lubricant drops, antibiotic drops",
          "Dry, irritated eye; minor conjunctivitis (on medical advice)",
          "**Never use steroid drops without a doctor**; discard 4 weeks after "
          "opening; do not touch the dropper to the eye"],
         ["**Ear drops** \u2014 olive oil, wax-softening drops",
          "Softening wax, an insect in the ear", "Not if there is a discharge or "
                                                "a suspected perforation"],
         ["**Nasal drops/spray** \u2014 saline, xylometazoline",
          "Blocked nose", "Decongestant sprays must not be used for more than "
                          "3\u20135 days (rebound congestion); not for infants"],
         ["**Salbutamol inhaler (blue reliever)**",
          "**Asthma attack** \u2014 help the casualty take **his own** inhaler: "
          "**2 puffs, repeated every 2 minutes up to 10 puffs**; use a spacer if "
          "available",
          "Causes tremor and palpitation; if there is no relief in 5\u201310 "
          "minutes \u2192 **ambulance**"],
         ["**Nitroglycerine / sorbitrate (sub-lingual tablet or spray)**",
          "**Angina/heart attack** \u2014 help the casualty take **his own** "
          "tablet under the tongue", "Causes headache and a fall in blood "
                                     "pressure; the casualty must be sitting; "
                                     "not if the BP is low"],
         ["**Adrenaline auto-injector (EpiPen)**", "**Anaphylaxis** \u2014 "
                                                  "**0.3\u20130.5 mg IM into "
                                                  "the outer thigh** (child "
                                                  "0.15 mg)",
          "**The life-saving drug of anaphylaxis**; a second dose may be given "
          "after 5\u201315 minutes; hospital always"],
         ["**Smelling salts (sal volatile)**", "Traditionally used for **faintness "
                                              "in a conscious casualty**",
          "**Never** hold under the nose of an unconscious casualty; fresh air "
          "and lying down are better"],
         ["**Oral rehydration, glucose, salt** ", "See above",
          "The commonest and most useful \u2018medicines\u2019 in the first-aid "
          "box"]],
        weights=[3.0, 4.8, 4.8], size=8.4)
    b.h3("E. Antibiotics, anti-malarials and vaccines \u2014 what a first aider "
         "should know")
    b.bullets([
        "**Antibiotics (amoxicillin, azithromycin, cefixime, ciprofloxacin, "
        "metronidazole, doxycycline)** are **prescription-only** medicines. A "
        "first aider **does not start antibiotics**; his duty is to clean and "
        "cover the wound and refer.",
        "Rules when a doctor has prescribed them: **take the full course, at the "
        "correct intervals, with water, and do not stop when you feel better; "
        "never share or re-use them; never take a left-over antibiotic for a new "
        "illness**. Misuse causes **antibiotic resistance**, the greatest "
        "threat in modern medicine.",
        "Watch for **allergy (rash, swelling, breathlessness \u2014 especially "
        "with penicillins)**, and for diarrhoea or fungal infection after a "
        "course.",
        "**Metronidazole must never be taken with alcohol**; "
        "**tetracycline/doxycycline** must be avoided in children and pregnancy "
        "and not taken with milk; **ciprofloxacin** is avoided in growing "
        "children.",
        "**Anti-malarials (chloroquine, artemisinin combinations, primaquine)** "
        "are given only after a **blood test** \u2014 fever with chills in a "
        "malarious area must be tested, not treated blindly.",
        "**Tetanus toxoid (TT) and anti-rabies vaccine** are the two "
        "immunisations a first aider must remember to arrange \u2014 for wounds "
        "and for animal bites respectively.",
        "**Vitamins and tonics** are not a treatment for illness; iron and folic "
        "acid for anaemia and vitamin D/calcium for bone health are used on "
        "medical advice. Iron is taken **after food** and stains the stools "
        "black.",
    ])

    # ------------------------------------------------------------------
    b.h2("Dangers of Self-Medication")
    b.box("WHY SELF-MEDICATION IS DANGEROUS", [
        "It **masks the real disease** \u2014 a painkiller hides appendicitis, "
        "an antacid hides a heart attack, an anti-diarrhoeal hides dysentery.",
        "**Wrong drug, wrong dose, wrong duration** \u2014 leading to failure of "
        "treatment or to poisoning (paracetamol and liver failure being the "
        "classic example).",
        "**Allergic and adverse reactions**, including fatal anaphylaxis.",
        "**Drug interactions** with medicines already being taken.",
        "**Antibiotic resistance** and **habit formation** (sedatives, "
        "painkillers, cough syrups).",
        "**Delay in seeking proper medical help** \u2014 often the real cause of "
        "death.",
        "**Golden rule for the first aider:** *give only simple, familiar "
        "remedies to a fully conscious casualty, in the correct dose \u2014 and "
        "when in doubt, give nothing and refer.*",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Medicines for the First-Aid Box \u2014 Summary List")
    b.table(
        ["Purpose", "Medicine"],
        [["Pain and fever", "**Paracetamol** tablets; aspirin (adults, for "
                            "suspected heart attack); ibuprofen"],
         ["Wound care", "**Povidone-iodine** solution/ointment, chlorhexidine, "
                        "hydrogen peroxide, spirit swabs, antibiotic ointment"],
         ["Allergy and itching", "**Antihistamine tablets**, calamine lotion, "
                                 "the casualty's own **adrenaline "
                                 "auto-injector**"],
         ["Dehydration", "**ORS sachets**, glucose powder, zinc tablets "
                         "(children)"],
         ["Acidity", "Antacid gel or tablets"],
         ["Burns", "Silver sulphadiazine cream, non-adherent dressings"],
         ["Eye", "Sterile eye wash/saline, eye pads"],
         ["Faintness", "Glucose/sugar; smelling salts"],
         ["Fungal/skin", "Clotrimazole cream, antiseptic powder"],
         ["Others", "Thermometer, gloves, torch, scissors, notebook, list of "
                    "emergency numbers, first-aid manual"]],
        weights=[3.4, 8.8])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "A first aider gives **only simple medicines to a fully conscious "
        "casualty** \u2014 he never prescribes, never injects and never gives "
        "Schedule H drugs.",
        "**Five rights:** right **patient, drug, dose, route and time** "
        "(+ record).",
        "**Paracetamol** is the safest analgesic/antipyretic: **500 mg\u20131 g "
        "6\u20138 hourly, maximum 3\u20134 g/day**; overdose destroys the "
        "**liver**.",
        "**Aspirin: 300 mg chewed in a suspected heart attack**; "
        "**never under 16 years (Reye's syndrome)**, never in ulcer, dengue or "
        "stroke.",
        "**ORS = 1 sachet in 1 litre** of clean water, used within **24 hours**; "
        "it is the treatment of diarrhoea \u2014 **loperamide is never given to "
        "children**.",
        "**Adrenaline (0.3\u20130.5 mg IM in the outer thigh)** is the drug of "
        "choice in **anaphylaxis**; antihistamines are not a substitute.",
        "**Asthma** \u2192 the casualty's own **blue salbutamol inhaler, 2 puffs "
        "up to 10**; **angina** \u2192 his own sub-lingual nitroglycerine.",
        "**Antiseptic** is used on living tissue, a **disinfectant** on objects; "
        "**soap and running water** is the best wound cleanser.",
        "**Never** give an antispasmodic or laxative in undiagnosed abdominal "
        "pain; **never** use medicines past their **expiry date**.",
        "Store medicines **cool, dry, dark, labelled, locked and out of "
        "children's reach**; complete every antibiotic course.",
    ])
