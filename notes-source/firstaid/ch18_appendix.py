# -*- coding: utf-8 -*-
"""Appendix - Quick Reference and Revision Section."""


def render(b):
    b.chapter(
        "Quick Reference and Rapid Revision",
        "Glossary and abbreviations, all normal values, position chart, master "
        "list of do's and don'ts, all mnemonics, antidote chart, records and "
        "reports, fire and disaster basics, and a chapter-wise list of "
        "one-line facts for the last day before the examination.",
        tag="APPENDIX")

    # ------------------------------------------------------------------
    b.h2("Glossary of First-Aid and Medical Terms")
    b.table(
        ["Term", "Meaning", "Term", "Meaning"],
        [["Abrasion", "Graze; scraping off of the skin surface", "Hypoxia",
          "Lack of oxygen in the tissues"],
         ["Amnesia", "Loss of memory", "Hypothermia",
          "Core body temperature below 35 \u00b0C"],
         ["Anaphylaxis", "Severe generalised allergic reaction", "Incision",
          "Clean cut by a sharp object"],
         ["Angina", "Chest pain from reduced blood flow to the heart muscle",
          "Ischaemia", "Reduced blood supply to a part"],
         ["Anoxia", "Complete absence of oxygen", "Laceration",
          "Tear with ragged edges"],
         ["Antidote", "Substance that counteracts a poison", "Lumbar",
          "Region of the lower back"],
         ["Antiseptic", "Substance that stops germs growing on living tissue",
          "Malaena", "Black tarry stool from digested blood"],
         ["Apnoea", "Absence of breathing", "Oedema",
          "Swelling from fluid in the tissues"],
         ["Asphyxia", "Oxygen lack with CO\u2082 retention from interference "
                      "with breathing", "Oliguria", "Reduced urine output"],
         ["Aspiration", "Inhalation of vomit, blood or fluid into the lungs",
          "Opisthotonos", "Arching of the back in tetanus/convulsion"],
         ["Asystole", "Complete absence of heart activity", "Pallor",
          "Paleness of the skin"],
         ["Aura", "Warning sensation before a fit", "Paraesthesia",
          "Tingling, \u2018pins and needles\u2019"],
         ["Avulsion", "Tearing away of a flap of tissue", "Perfusion",
          "Flow of blood through the tissues"],
         ["Bradycardia", "Pulse below 60/min", "Petechiae",
          "Pin-point bleeding spots in the skin"],
         ["Capillary refill", "Time for colour to return after pressing a nail "
                              "bed (normal < 2 s)", "Prognosis",
          "Expected outcome of an illness or injury"],
         ["Cardiac arrest", "Stoppage of effective heart action", "Prone",
          "Lying face downwards"],
         ["Casualty", "A person who is injured or suddenly taken ill",
          "Pyrexia", "Fever"],
         ["Cerebral", "Relating to the brain", "Reduction",
          "Setting of a fracture or dislocation (not for a first aider)"],
         ["Compression", "Pressure on the brain from bleeding or swelling",
          "Rigor", "Shivering attack with fever"],
         ["Concussion", "Temporary shaking-up of the brain", "ROSC",
          "Return of spontaneous circulation after CPR"],
         ["Contusion", "Bruise \u2014 bleeding into tissues with unbroken skin",
          "Sign", "What the first aider observes"],
         ["Crepitus", "Grating of broken bone ends", "Splint",
          "Rigid support for a fracture"],
         ["Cyanosis", "Blue discoloration from lack of oxygen", "Sprain",
          "Injury to a ligament round a joint"],
         ["Defibrillation", "Electric shock to restore a normal heart rhythm",
          "Strain", "Over-stretching of a muscle or tendon"],
         ["Dislocation", "Displacement of bones at a joint", "Stridor",
          "Harsh noisy breathing from upper-airway narrowing"],
         ["Dyspnoea", "Difficult or laboured breathing", "Supine",
          "Lying on the back"],
         ["Epistaxis", "Bleeding from the nose", "Symptom",
          "What the casualty complains of"],
         ["Fracture", "Break in the continuity of a bone", "Syncope",
          "Fainting"],
         ["Gangrene", "Death of tissue from loss of blood supply", "Tachycardia",
          "Pulse above 100/min"],
         ["Haematemesis", "Vomiting of blood", "Tetany",
          "Muscle spasms from low calcium or over-breathing"],
         ["Haematuria", "Blood in the urine", "Tourniquet",
          "Constricting band to stop limb bleeding (last resort)"],
         ["Haemoptysis", "Coughing up of blood from the lungs", "Triage",
          "Sorting of casualties by priority"],
         ["Haemorrhage", "Escape of blood from a vessel", "Trismus",
          "Lock-jaw \u2014 spasm of the jaw muscles"],
         ["Hyperglycaemia", "High blood sugar", "Unconsciousness",
          "State of not responding to stimuli"],
         ["Hypoglycaemia", "Low blood sugar (below 70 mg/dl)", "Ventricular "
                                                              "fibrillation",
          "Chaotic, ineffective quivering of the heart"]],
        weights=[2.1, 4.4, 2.1, 4.0], size=8.0, first_bold=True)

    # ------------------------------------------------------------------
    b.h2("Abbreviations Used in First Aid")
    b.table(
        ["Abbr.", "Full form", "Abbr.", "Full form"],
        [["**ABC**", "Airway, Breathing, Circulation", "**GCS**",
          "Glasgow Coma Scale"],
         ["**AED**", "Automated External Defibrillator", "**IM / IV**",
          "Intramuscular / Intravenous"],
         ["**ACLS**", "Advanced Cardiac Life Support", "**MI**",
          "Myocardial Infarction (heart attack)"],
         ["**ARV / RIG**", "Anti-Rabies Vaccine / Rabies Immunoglobulin",
          "**ORS**", "Oral Rehydration Solution"],
         ["**ASV**", "Anti-Snake Venom", "**PEP**",
          "Post-Exposure Prophylaxis"],
         ["**AVPU**", "Alert, Voice, Pain, Unresponsive", "**RICE**",
          "Rest, Ice, Compression, Elevation"],
         ["**BLS**", "Basic Life Support", "**ROSC**",
          "Return of Spontaneous Circulation"],
         ["**BP**", "Blood Pressure", "**RR**", "Respiratory Rate"],
         ["**CPR**", "Cardio-Pulmonary Resuscitation", "**SpO\u2082**",
          "Oxygen saturation of the blood"],
         ["**CSF**", "Cerebro-Spinal Fluid", "**START**",
          "Simple Triage And Rapid Treatment"],
         ["**DRABC**", "Danger, Response, Airway, Breathing, Circulation",
          "**TT**", "Tetanus Toxoid"],
         ["**EMS**", "Emergency Medical Services", "**VF**",
          "Ventricular Fibrillation"],
         ["**FAST**", "Face, Arms, Speech, Time (stroke test)", "**WHO**",
          "World Health Organization"]],
        weights=[2.1, 4.6, 2.1, 3.8], size=8.2, first_bold=False)

    # ------------------------------------------------------------------
    b.h2("All Normal Values on One Page")
    b.table(
        ["Parameter", "Adult", "Child", "Infant"],
        [["Pulse (beats/min)", "**60\u2013100** (avg 72)", "80\u2013120",
          "100\u2013160"],
         ["Respiration (breaths/min)", "**12\u201320**", "20\u201330",
          "30\u201360"],
         ["Blood pressure (mm Hg)", "**120/80**", "~100/65", "~80/50"],
         ["Temperature", "**37 \u00b0C / 98.4 \u00b0F**", "Same", "Same"],
         ["SpO\u2082", "**95\u2013100 %**", "95\u2013100 %", "95\u2013100 %"],
         ["Blood volume", "**5\u20136 litres**", "2\u20132.5 litres",
          "250\u2013350 ml"],
         ["Capillary refill", "**< 2 seconds**", "< 2 s", "< 2 s"],
         ["Urine output", "**1\u20131.5 l/day (\u2265 30 ml/h)**",
          "1\u20132 ml/kg/h", "2 ml/kg/h"],
         ["CPR compression depth", "**5\u20136 cm**", "\u2248 5 cm (\u2153 chest)",
          "\u2248 4 cm (\u2153 chest)"],
         ["CPR rate / ratio", "**100\u2013120/min; 30 : 2**",
          "100\u2013120/min; 30 : 2 (15 : 2 for 2 professionals)",
          "100\u2013120/min; 30 : 2 (15 : 2)"],
         ["Rescue breaths alone", "**10\u201312/min**", "12\u201320/min",
          "12\u201320/min"],
         ["Fasting blood sugar", "**70\u2013110 mg/dl**", "Same", "Same"],
         ["Haemoglobin", "**M 13\u201318, F 12\u201316 g/dl**",
          "11\u201316 g/dl", "14\u201320 g/dl (newborn)"],
         ["Blood pH", "**7.35\u20137.45**", "Same", "Same"],
         ["Tidal volume", "**500 ml**", "\u2014", "\u2014"],
         ["Number of bones", "**206**", "\u2014", "270\u2013300 at birth"]],
        weights=[3.2, 3.6, 3.2, 3.0], size=8.4)

    # ------------------------------------------------------------------
    b.h2("Position of the Casualty \u2014 Master Chart")
    b.table(
        ["Condition", "Correct position"],
        [["Unconscious, breathing", "**Recovery (lateral) position**"],
         ["Cardiac arrest / CPR", "**Flat on the back on a hard surface**"],
         ["Shock, bleeding, fainting", "**Flat, legs raised 20\u201330 cm**, "
                                      "head low and turned to one side"],
         ["Heart attack, angina", "**Half-sitting (W position)**, knees bent"],
         ["Asthma, breathlessness", "**Sitting up, leaning slightly forward**"],
         ["Chest injury", "**Half-sitting, leaning towards the injured side**"],
         ["Abdominal injury / pain", "**On the back, knees drawn up** and "
                                     "supported"],
         ["Head injury, stroke", "Flat with **head and shoulders slightly "
                                 "raised**; recovery position if unconscious"],
         ["Spinal injury", "**Do not move** \u2014 flat, head held in line, "
                           "spine board"],
         ["Fracture of the lower limb", "Flat, limb immobilised and supported"],
         ["Fracture of the pelvis", "Flat, knees and ankles tied with padding "
                                    "between"],
         ["Nose bleed", "**Sitting up, head bent forward**"],
         ["Snake bite", "Lying still, limb splinted **at or below heart level**"],
         ["Pregnant casualty", "**Left lateral** position"],
         ["Burns", "Flat, burnt part raised and covered"],
         ["Vomiting or bleeding into the mouth", "Head turned to the side / "
                                                "recovery position"],
         ["Heat stroke", "Flat in a cool place, clothing removed, actively "
                         "cooled"],
         ["Hypothermia", "Flat and horizontal, insulated, handled gently"]],
        weights=[4.2, 8.4])

    # ------------------------------------------------------------------
    b.h2("Master List of \u2018Never Do\u2019 Points")
    b.box("THE FIRST AIDER'S ABSOLUTE PROHIBITIONS", [
        "**Never** rush into danger \u2014 electricity, gas, fire, water, "
        "traffic, a confined space.",
        "**Never** give anything by mouth to an unconscious, drowsy, convulsing "
        "or vomiting casualty, or to one likely to need an operation.",
        "**Never** remove a blood-soaked dressing \u2014 add another pad over it.",
        "**Never** remove a deeply embedded foreign body, and never probe a wound.",
        "**Never** apply a tourniquet except for uncontrollable, "
        "life-threatening limb bleeding \u2014 and never loosen it once applied.",
        "**Never** attempt to reduce (set) a fracture or dislocation, and never "
        "test for crepitus.",
        "**Never** apply direct heat, hot-water bottles or alcohol to a shocked "
        "casualty.",
        "**Never** put anything in the mouth of a person having a fit, and never "
        "restrain him.",
        "**Never** induce vomiting in poisoning \u2014 above all with corrosives "
        "and petroleum products.",
        "**Never** apply ice, oil, butter, toothpaste or turmeric to a burn, and "
        "never prick blisters.",
        "**Never** rub a frost-bitten part or use dry heat on it, and never let "
        "it re-freeze.",
        "**Never** cut, suck or apply a tourniquet to a snake bite, and never "
        "let the casualty walk.",
        "**Never** plug the ear or nose that is bleeding after a head injury.",
        "**Never** move a suspected spinal-injury casualty without full support "
        "and helpers.",
        "**Never** exceed your training, never accept a fee, and never discuss "
        "the casualty with onlookers or the press.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("All the Mnemonics in One Place")
    b.table(
        ["Mnemonic", "Stands for", "Used for"],
        [["**3 P's**", "Preserve life, Prevent worsening, Promote recovery",
          "Aims of first aid"],
         ["**DRSABCD**", "Danger, Response, Send for help, Airway, Breathing, "
                        "Circulation/CPR, Defibrillation",
          "Action plan at every emergency"],
         ["**AVPU**", "Alert, Voice, Pain, Unresponsive",
          "Level of consciousness"],
         ["**SAMPLE**", "Signs/symptoms, Allergies, Medication, Past history, "
                        "Last meal, Events", "History taking"],
         ["**AMPLE**", "Allergies, Medicines, Past illness, Last meal, Events",
          "Hand-over to hospital"],
         ["**RPM**", "Respiration, Perfusion, Mental status",
          "START triage assessment"],
         ["**FISH SHAPED**", "Fainting, Infantile convulsions, Shock, Head "
                            "injury, Stroke, Heart attack, Asphyxia, Poisoning, "
                            "Epilepsy, Diabetes", "Causes of unconsciousness"],
         ["**AEIOU-TIPS**", "Alcohol, Epilepsy, Insulin, Overdose, Uraemia, "
                           "Trauma, Infection, Poisoning, Stroke",
          "Causes of coma"],
         ["**FAST**", "Face, Arms, Speech, Time", "Recognising a stroke"],
         ["**RICE / PRICE**", "(Protect), Rest, Ice, Compression, Elevation",
          "Sprains, strains, bruises"],
         ["**HARM**", "Heat, Alcohol, Running, Massage \u2014 to be **avoided** "
                      "for 48\u201372 hours", "After a sprain or strain"],
         ["**5 P's**", "Pain, Pallor, Pulselessness, Paraesthesia, Paralysis",
          "Signs of a too-tight bandage / circulation loss"],
         ["**SLUDGE**", "Salivation, Lacrimation, Urination, Defaecation, "
                        "Gastric cramps, Emesis",
          "Organophosphate (insecticide) poisoning"],
         ["**Reach\u2013Throw\u2013Row\u2013Go**", "Order of water rescue",
          "Drowning"],
         ["**Stop\u2013Drop\u2013Wrap\u2013Roll**", "Action when clothes catch "
                                                   "fire", "Burns"],
         ["**5 Rights**", "Right patient, drug, dose, route, time",
          "Giving medicines"],
         ["**WHO 5 Keys**", "Keep clean, separate raw/cooked, cook thoroughly, "
                            "safe temperature, safe water",
          "Preventing food poisoning"],
         ["**30/30 rule**", "Shelter if thunder < 30 s after the flash; wait "
                            "30 min after the last thunder", "Lightning safety"]],
        weights=[2.6, 5.4, 4.6], size=8.4)

    # ------------------------------------------------------------------
    b.h2("Antidotes and Specific Treatments \u2014 Ready Chart")
    b.table(
        ["Emergency", "Specific treatment / antidote"],
        [["Anaphylaxis", "**Adrenaline 0.5 mg IM (outer thigh)**"],
         ["Ventricular fibrillation / cardiac arrest", "**CPR + "
                                                       "defibrillation (AED)**"],
         ["Heart attack", "**Aspirin 300 mg chewed** + rest + hospital"],
         ["Hypoglycaemia (conscious)", "**Oral sugar/glucose**"],
         ["Asthma attack", "**Salbutamol (blue) inhaler, 2\u201310 puffs**"],
         ["Angina", "**Sub-lingual nitroglycerine**"],
         ["Snake bite", "**Anti-snake venom (ASV)** in hospital"],
         ["Dog bite", "**Wash 15 min + anti-rabies vaccine (\u00b1 RIG)**"],
         ["Dirty/punctured wound", "**Tetanus toxoid (\u00b1 immunoglobulin)**"],
         ["Organophosphate poisoning", "**Atropine + pralidoxime**"],
         ["Opioid overdose", "**Naloxone**"],
         ["Paracetamol overdose", "**N-acetylcysteine**"],
         ["Carbon monoxide poisoning", "**100 % oxygen (hyperbaric if severe)**"],
         ["Cyanide poisoning", "**Hydroxocobalamin / nitrite\u2013thiosulphate "
                               "kit**"],
         ["Iron poisoning", "**Desferrioxamine**"],
         ["Warfarin / rat poison", "**Vitamin K**"],
         ["Diarrhoea and dehydration", "**ORS (+ zinc in children)**"],
         ["Heat stroke", "**Rapid external cooling**"],
         ["Hypothermia", "**Gradual re-warming, gentle handling**"],
         ["Frost-bite", "**Re-warming in water at 37\u201340 \u00b0C**"]],
        weights=[4.6, 6.0])

    # ------------------------------------------------------------------
    b.h2("First-Aid Records and Hand-Over Report")
    b.p("Every serious case must be recorded. A simple format:")
    b.table(
        ["Item", "What to write"],
        [["Identification", "Name, age, sex, address/employee number, contact "
                            "person"],
         ["Date and time", "Time of the incident, time you arrived, time the "
                           "ambulance was called and arrived"],
         ["History", "What happened (mechanism of injury), where, how; what the "
                     "casualty and witnesses said; **SAMPLE** history"],
         ["Findings", "Level of response (AVPU), airway, breathing rate, pulse "
                      "rate and character, skin colour and temperature, pupils, "
                      "bleeding, injuries found in the head-to-toe examination"],
         ["Observations chart", "Pulse, breathing and response **repeated every "
                                "10 minutes with the time** of each reading"],
         ["Treatment given", "Dressings, bandages, splints, position, CPR (with "
                             "times), medicines given (name, dose, time), "
                             "oxygen"],
         ["Property", "Valuables, documents, dentures, spectacles handed over "
                      "\u2014 to whom and when (with a witness)"],
         ["Disposal", "Sent home / to hospital / to a doctor; by what transport; "
                      "accompanied by whom"],
         ["Signature", "Name, designation and signature of the first aider"]],
        weights=[3.0, 9.6])
    b.p("Keep the record **factual** \u2014 no opinions or blame. It may be "
        "needed for insurance, compensation or a court of law, and the "
        "information is **confidential**.")

    # ------------------------------------------------------------------
    b.h2("Fire, Rescue and Disaster \u2014 Ready Reference")
    b.table(
        ["Situation", "Action"],
        [["**Clothes on fire**", "**STOP \u2013 DROP \u2013 WRAP \u2013 ROLL**: "
                                "stop the casualty running, lay him down with "
                                "the burning side uppermost, wrap him in a "
                                "blanket/coat/rug (not nylon) and roll him on "
                                "the ground; then treat the burns"],
         ["**Fire in a building**", "Raise the alarm and call **101**; close "
                                   "doors behind you; **do not use the lift**; "
                                   "**crawl low under the smoke** keeping close "
                                   "to the floor; test doors with the back of "
                                   "the hand before opening; if trapped, "
                                   "block gaps with wet cloth and signal from a "
                                   "window"],
         ["**Types of extinguisher**", "**Water** \u2014 wood, paper, cloth "
                                       "(Class A); **foam** \u2014 flammable "
                                       "liquids (B); **CO\u2082 / dry powder** "
                                       "\u2014 **electrical (C)** and liquids; "
                                       "**wet chemical/fire blanket** \u2014 "
                                       "**cooking oil (K/F)**. ==Never use water "
                                       "on an electrical or oil fire==. Remember "
                                       "**PASS**: Pull, Aim, Squeeze, Sweep"],
         ["**Gas leak**", "Do **not** operate any switch or flame; close the "
                          "valve; open doors and windows; evacuate; call the gas "
                          "agency/fire brigade"],
         ["**Road accident**", "Park safely with hazard lights on, wear a "
                              "reflective jacket, **switch off the ignition and "
                              "apply the handbrake** of the crashed vehicle, "
                              "warn oncoming traffic, do not smoke, call "
                              "**112/108**, do not remove a helmet unless the "
                              "airway is blocked (two-rescuer removal), treat "
                              "the casualties where they lie and remember the "
                              "**Good Samaritan** protection"],
         ["**Mass casualty / disaster**", "Take charge, ensure scene safety, "
                                          "**triage (red\u2013yellow\u2013"
                                          "green\u2013black)**, set up a "
                                          "collection point, treat only airway "
                                          "and severe bleeding while triaging, "
                                          "record and transport by priority, "
                                          "inform the district control room "
                                          "(**1070/1077**)"],
         ["**Collapsed structure / confined space**", "Never enter without "
                                                     "breathing apparatus, a "
                                                     "harness and helpers; "
                                                     "beware of crush syndrome "
                                                     "on release; note the time "
                                                     "of the crush"]],
        weights=[2.8, 9.8], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Chapter-wise One-Line Facts for the Last Day")
    b.h3("Outline of first aid")
    b.bullets([
        "First aid = immediate, temporary, skilled help with available material.",
        "Aims = **preserve life (first), prevent worsening, promote recovery**.",
        "Term coined by **Esmarch**; St John Ambulance **1877**; Red Cross "
        "**1863 (Henri Dunant)**; Indian Red Cross **1920**.",
        "First-aid symbol = **white cross on green**; World First Aid Day = "
        "**2nd Saturday of September**; World Red Cross Day = **8 May**.",
        "Ambulance **108**, universal emergency **112**, fire **101**, police "
        "**100**, childline **1098**, poison information **1800-11-6117**.",
        "Triage: **red = immediate, yellow = urgent, green = delayed, black = "
        "dead/expectant**; START assesses **RPM**.",
        "Golden hour = **60 minutes**; brain damage in **3\u20134 minutes**; "
        "breathing checked for \u2264 **10 seconds**.",
        "Factories Act: first-aid box per **150 workers**; ambulance room above "
        "**500 workers**.",
    ])
    b.h3("Structure and functions of the body")
    b.bullets([
        "**206 bones** (axial 80 + appendicular 126); hand 27, foot 26; "
        "vertebrae **7-12-5-5-4**; ribs **12 pairs (7 true, 3 false, 2 "
        "floating)**.",
        "**Femur** largest, **stapes** smallest, **clavicle** most often "
        "fractured, **hyoid** has no joint, **patella** is the largest sesamoid.",
        "Heart: 4 chambers, 4 valves, pacemaker **SA node**, thickest wall "
        "**left ventricle**, cardiac output **5 l/min**.",
        "**Pulmonary artery** carries deoxygenated and **pulmonary vein** "
        "oxygenated blood.",
        "Blood = plasma **55 %** + cells; RBC life **120 days**; **O\u2212 "
        "universal donor**, **AB+ universal recipient**.",
        "Right lung **3 lobes**, left **2**; inhaled objects go to the **right** "
        "bronchus; expired air = **16 % O\u2082, 4 % CO\u2082**.",
        "Vital centres in the **medulla**; balance in the **cerebellum**; "
        "temperature in the **hypothalamus**.",
        "**12 cranial nerves** (vagus longest, trigeminal largest) and **31 "
        "pairs of spinal nerves**.",
        "**Liver** largest gland, **thyroid** largest endocrine gland, "
        "**pituitary** master gland, **skin** largest organ.",
    ])
    b.h3("Dressings and bandages")
    b.bullets([
        "Dressing touches the wound; bandage holds the dressing.",
        "Triangular bandage = **1 m square cut diagonally**; forms = open, "
        "broad, narrow.",
        "**Arm sling** \u2014 forearm/ribs; **elevation sling** \u2014 bleeding "
        "hand/collar bone; **collar-and-cuff** \u2014 humerus.",
        "Roller widths: finger 2.5, hand 5, arm 5\u20136, leg 7.5\u20139, trunk "
        "10\u201315 cm.",
        "Turns: circular, spiral, **reverse spiral (forearm/leg)**, "
        "**figure-of-eight (ankle)**, spica (shoulder/hip/thumb), recurrent "
        "(stump).",
        "Overlap **two-thirds**, bandage **below upwards**, finish with a "
        "**reef knot**, keep finger tips visible.",
    ])
    b.h3("CPR, artificial respiration and asphyxia")
    b.bullets([
        "Adult CPR: **100\u2013120/min, 5\u20136 cm, 30 : 2**, change rescuer "
        "every **2 minutes**.",
        "Infant: **two fingers, 4 cm, 5 breaths first, brachial pulse**; "
        "two professionals use **15 : 2**; newborn **3 : 1**.",
        "AED pads: **below the right collar bone + left mid-axillary line**.",
        "Choking: **5 back blows + 5 abdominal thrusts**; infants get **chest "
        "thrusts, never abdominal**; unconscious \u2192 CPR.",
        "Mouth-to-mouth **10\u201312/min**; **Schafer 12\u201315**; **Holger "
        "Nielsen 12** (best manual); **Sylvester 12**; **Eve's rocking "
        "10\u201312**.",
        "Asphyxia stages: **dyspnoea \u2192 convulsions \u2192 apnoea**; CO "
        "poisoning gives **cherry-red** skin.",
        "Drowning: **reach\u2013throw\u2013row\u2013go**, 5 rescue breaths, never "
        "drain the lungs, always hospitalise (secondary drowning).",
    ])
    b.h3("Wounds, bleeding, shock and electric shock")
    b.bullets([
        "Incised bleeds most; punctured risks **tetanus**; contusion is a "
        "**closed** wound.",
        "Tetanus: ***Clostridium tetani***, incubation **7\u201310 days**, toxin "
        "**tetanospasmin**, sign **trismus**.",
        "Bleeding control = **rest + elevation + direct pressure for 10 "
        "minutes**; pressure points **brachial** and **femoral**.",
        "Blood loss of **1\u20131.5 litres** causes definite shock; one-third "
        "loss may be fatal.",
        "Shock position = **flat, legs raised 20\u201330 cm**, warm, **nothing by "
        "mouth**.",
        "Anaphylaxis \u2192 **adrenaline IM outer thigh**; heart attack \u2192 "
        "**aspirin 300 mg chewed**.",
        "Burns: cool **10\u201320 minutes**; **rule of nines** (head 9, arm 9, "
        "leg 18, trunk 18 + 18, perineum 1); child head 18, leg 14.",
        "Electric shock: **switch off first**; **AC more dangerous than DC**; "
        "**50\u2013100 mA \u2192 VF**; high voltage \u2014 keep **18 m** away.",
    ])
    b.h3("Fractures, unconsciousness, fits and poisons")
    b.bullets([
        "Fracture types: simple, **compound (most dangerous)**, comminuted, "
        "**greenstick (children)**, complicated, impacted, depressed.",
        "Immobilise the **joints above and below**; bandage **above and below, "
        "never over** the fracture; **never reduce**.",
        "**Shoulder** is the most commonly dislocated joint; dislocation = "
        "**fixed joint, no crepitus**.",
        "**Sprain = ligament, strain = muscle/tendon**; treat by **RICE**, avoid "
        "**HARM**.",
        "Concussion = temporary with **equal pupils and rapid pulse**; "
        "compression = progressive with **unequal pupils and slow full pulse**.",
        "Fit: **never put anything in the mouth, never restrain**; status "
        "epilepticus = fit **> 5 minutes** \u2192 ambulance.",
        "Hysterical fit: **only before an audience, no tongue bite, no "
        "incontinence, no cyanosis, pupils normal**.",
        "Poisoning: **never induce vomiting** (especially corrosives and "
        "kerosene); save the container; **pin-point pupils** = opium/"
        "organophosphate, **dilated** = dhatura.",
        "Food poisoning: **Staphylococcus 1\u20136 h (vomiting)**, **Salmonella "
        "12\u201336 h (fever)**, **botulism 12\u201336 h (paralysis)**; treat "
        "with **ORS**.",
    ])
    b.h3("Common conditions, transport and medicines")
    b.bullets([
        "Epistaxis \u2192 **sit up, head forward, pinch the soft part 10 "
        "minutes**.",
        "Snake bite \u2192 **immobilise like a fracture, limb at/below heart "
        "level, hospital for ASV**; no tourniquet, no cutting, no sucking.",
        "Dog bite \u2192 **wash with soap and water 15 minutes** + vaccine on "
        "days **0, 3, 7, 14, 28** (+ RIG in Category III).",
        "Frost-bite \u2192 re-warm at **37\u201340 \u00b0C**; never rub or use "
        "dry heat; hypothermia = core temperature **< 35 \u00b0C**.",
        "Heat stroke = **hot dry skin, no sweating, > 40 \u00b0C** \u2192 cool "
        "rapidly; heat exhaustion = **pale, clammy, sweating** \u2192 ORS.",
        "Bee sting \u2192 **scrape out sideways**; sting in the mouth \u2192 ice "
        "and ambulance.",
        "Carries: **four-handed seat** (both arms usable), **three-handed** "
        "(one leg injured), **two-handed** (arms unusable), **fireman's lift** "
        "(one hand free), **chair/fore-and-aft** (stairs).",
        "Carry **feet first on the level, head first up**; bearers **break "
        "step**; **Neil Robertson stretcher** for vertical rescue.",
        "Paracetamol **500 mg\u20131 g 6-hourly (max 3\u20134 g/day)**; aspirin "
        "**never under 16** (Reye's syndrome).",
        "**ORS = 1 sachet per litre**, used within 24 hours; loperamide never in "
        "children; **5 rights** of medicine administration.",
    ])

    # ------------------------------------------------------------------
    b.h2("Last Word")
    b.box("HOW TO USE THIS BOOK IN THE FINAL WEEK", [
        "**Day 1\u20133:** read one Part a day, marking the coloured boxes only.",
        "**Day 4\u20135:** revise all the **tables** \u2014 most objective "
        "questions come straight from comparison tables (arterial vs venous, "
        "concussion vs compression, epilepsy vs hysteria, fracture vs "
        "dislocation, heat stroke vs heat exhaustion, hypoglycaemia vs "
        "hyperglycaemia).",
        "**Day 6:** revise every **Chapter Recap** and the **normal values**, "
        "**doses**, **rates** and **timings** \u2014 numbers are the easiest "
        "marks in the paper.",
        "**Day 7:** read this Appendix from beginning to end; it is the whole "
        "syllabus in miniature.",
        "In the examination, remember the three constants: **airway before "
        "everything, bleeding next, shock always** \u2014 and when two options "
        "look correct, choose the one that **protects life first and does the "
        "least to the casualty**.",
    ], kind="key")
