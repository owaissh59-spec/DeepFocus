# -*- coding: utf-8 -*-
"""Chapter 1 - Outline of First Aid."""


def render(b):
    b.part("PART I", "Foundations of First Aid")
    b.chapter(
        "Outline of First Aid",
        "Meaning, aims, principles, scope, golden rules, duties of a first aider, "
        "triage, the first-aid kit, medico-legal aspects and emergency helplines.",
        syllabus=[
            "Outline of the First-Aid \u2014 definition, aims, objects, scope and "
            "limitations of first aid.",
            "Principles, golden rules, qualities and responsibilities of a first aider; "
            "DRABC approach, primary and secondary survey, triage.",
            "First-aid kit, personal protection, medico-legal aspects, consent, "
            "Good Samaritan law, emergency numbers and records.",
        ])

    # ------------------------------------------------------------------
    b.h2("Meaning and Definition of First Aid")
    b.p("The term *First Aid* is made of two words \u2014 **First**, meaning the "
        "earliest or initial help, and **Aid**, meaning help or assistance. "
        "It therefore means the ==first help given to a sick or injured person "
        "before the arrival of qualified medical assistance==.")
    b.box("STANDARD DEFINITIONS (learn at least one word-perfect)", [
        "**First aid** is the *immediate*, *temporary* and *skilled* assistance "
        "given to a person who has suddenly fallen ill or met with an accident, "
        "using the material available at hand, until the services of a doctor are "
        "obtained or during transport to hospital.",
        "**St. John Ambulance definition:** \u201cFirst aid is the skilled "
        "application of accepted principles of treatment on the occurrence of an "
        "accident or in the case of sudden illness, using facilities or materials "
        "available at the time.\u201d",
        "**First aider:** a person who has received a certificate from an "
        "authorised/recognised training body (St. John Ambulance, Indian Red "
        "Cross Society, etc.) certifying competence to give first aid.",
        "**Key words in every definition:** *immediate* \u2013 *temporary* \u2013 "
        "*skilled* \u2013 *on the spot* \u2013 *with available material* \u2013 "
        "*till medical help arrives*.",
    ], kind="def")
    b.p("First aid is therefore **not** a substitute for medical treatment; it is "
        "the vital bridge between the moment of injury and definitive medical "
        "care. Deaths in the first few minutes after an accident are usually due "
        "to three correctable causes \u2014 ==airway obstruction, severe bleeding "
        "and shock== \u2014 all of which lie within the power of a trained first "
        "aider.")

    b.h3("Related terms you must be able to distinguish")
    b.table(
        ["Term", "What it means"],
        [["First aid", "Immediate, temporary, skilled help with available "
                       "material; ends when qualified help takes over."],
         ["Home nursing", "Continued care of a sick person at home after the "
                          "doctor's advice; long-term, not an emergency skill."],
         ["Emergency care / EMS", "Organised pre-hospital system (ambulance, "
                                  "paramedics, control room) that continues what "
                                  "the first aider began."],
         ["Triage", "Sorting of many casualties according to severity so that "
                    "the most urgent are treated first."],
         ["Golden hour", "The first 60 minutes after serious injury \u2014 "
                         "definitive treatment within this hour gives the best "
                         "chance of survival."],
         ["Platinum ten minutes", "The first 10 minutes of the golden hour, in "
                                  "which the casualty should be assessed, "
                                  "stabilised and moved."],
         ["Bystander / Good Samaritan", "An untrained onlooker who helps; "
                                        "protected by law in India (see 1.14)."]],
        weights=[3.2, 9.5])

    # ------------------------------------------------------------------
    b.h2("Aims and Objects of First Aid")
    b.p("The aims are classically remembered as the ==THREE P's==. Every "
        "examination asks these, usually as \u2018the first aim of first aid "
        "is\u2026\u2019 \u2014 the answer is always **to preserve/save life**.")
    b.table(
        ["The 3 P's", "Aim", "How it is achieved in practice"],
        [["1. Preserve life",
          "To save life \u2014 the **first and foremost** aim (of the casualty, "
          "of bystanders and of the first aider himself).",
          "Open the airway, give rescue breaths and chest compressions, arrest "
          "severe bleeding, treat shock."],
         ["2. Prevent worsening",
          "To prevent the condition from becoming worse (prevent further injury "
          "and complications).",
          "Immobilise fractures, cover wounds, do not move unnecessarily, "
          "prevent infection, keep the casualty warm and reassured."],
         ["3. Promote recovery",
          "To promote recovery and reduce the period of illness or disability.",
          "Relieve pain and anxiety, handle gently, position comfortably, arrange "
          "early and correct transport to hospital."]],
        weights=[2.6, 5.0, 6.6])
    b.h3("Expanded list of objects (St. John Ambulance)")
    b.numbered([
        "To **sustain life** \u2014 maintain airway, breathing and circulation.",
        "To **prevent deterioration** of the casualty's condition.",
        "To **relieve pain** and suffering, and to give reassurance.",
        "To **prevent infection** of wounds.",
        "To **prevent shock**, or to treat it if already present.",
        "To **arrange removal** of the casualty to shelter, home or hospital by "
        "the most suitable method.",
        "To **hand over** the casualty to a doctor/hospital with a clear report "
        "of what was found and what was done.",
        "To **stay with** the casualty until responsibility is properly handed "
        "over.",
    ])

    # ------------------------------------------------------------------
    b.h2("Scope and Limitations of First Aid")
    b.h3("Scope (what a first aider does)")
    b.bullets([
        "Assesses the scene for danger and makes it safe.",
        "Assesses the casualty (primary and secondary survey) and diagnoses the "
        "condition as far as possible from history, signs and symptoms.",
        "Gives immediate, appropriate treatment on the spot with whatever material "
        "is available (improvisation is a core first-aid skill).",
        "Decides priorities when there are several casualties (triage).",
        "Arranges safe transport and hands over the casualty with a report.",
        "Prevents infection and cross-infection; protects himself/herself.",
        "Gives psychological support \u2014 reassurance is a genuine treatment.",
    ])
    b.h3("Limitations (what a first aider must NOT do)")
    b.box("LIMITS OF FIRST AID \u2014 VERY COMMONLY ASKED", [
        "First aid is **temporary**, not definitive treatment; it ends the moment "
        "qualified medical help takes charge.",
        "A first aider must **not diagnose disease, prescribe medicines or give "
        "injections**.",
        "Must not attempt to reduce a fracture or dislocation, or push back "
        "protruding organs/bone ends.",
        "Must not give anything by mouth to an unconscious, semi-conscious, "
        "convulsing or abdominal-injury casualty.",
        "Must not exceed training, and must not delay professional help by "
        "over-treating.",
        "Must not discuss the casualty's condition with bystanders/press "
        "(confidentiality), nor accept a fee for first aid.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("General Principles of First Aid")
    b.p("These principles govern every emergency, whatever the cause:")
    b.numbered([
        "**Be calm, quick and methodical** \u2014 do not panic; panic spreads.",
        "**Make the area safe** before touching the casualty (electricity, gas, "
        "traffic, fire, water, collapsing structures). *Safety order:* self \u2192 "
        "scene \u2192 casualty.",
        "**Remove the casualty from danger, or the danger from the casualty** \u2014 "
        "whichever is quicker and safer.",
        "**Treat the most urgent condition first** \u2014 the order of priority is "
        "==Airway \u2192 Breathing \u2192 Circulation (bleeding) \u2192 "
        "Shock \u2192 fractures \u2192 minor injuries== (\u2018treat the worst "
        "first\u2019).",
        "**Handle gently**; do not move the casualty more than necessary, and "
        "never move a suspected spine injury without support.",
        "**Reassure** the casualty and the relatives; never say the injury looks "
        "bad, never allow the casualty to see his own wound if avoidable.",
        "**Loosen tight clothing** at neck, chest and waist; remove only as much "
        "clothing as necessary (tear along the seam).",
        "**Do not allow crowding**; disperse onlookers and use them for errands "
        "(calling ambulance, fetching blankets).",
        "**Guard against and treat shock** in every serious injury \u2014 keep the "
        "casualty warm, lying down, head low.",
        "**Nothing by mouth** if unconscious, if surgery/anaesthesia is likely, or "
        "in abdominal injury.",
        "**Arrange transport** by the most suitable means, in the correct "
        "position, without haste and without jolting.",
        "**Record and report** \u2014 note the time, findings, treatment given and "
        "hand over to the doctor.",
        "**Do not attempt too much**; do only what is necessary and stop when "
        "help arrives.",
    ])
    b.box("THE FOUR VITAL FIRST-AID ACTIONS (the \u2018big four\u2019 that save "
          "lives)", [
        "Restore **breathing** (open the airway, artificial respiration).",
        "Restore **circulation** (CPR / chest compressions).",
        "**Arrest severe bleeding**.",
        "**Treat shock** and poisoning promptly.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Golden Rules, Do's and Don'ts")
    b.table(
        ["DO (Golden Rules)", "DO NOT"],
        [["Keep yourself safe first; wear gloves if available.",
          "Do not rush in blindly \u2014 a dead rescuer helps nobody."],
         ["Shout for help and telephone 112/108 early.",
          "Do not waste time looking for perfect equipment \u2014 improvise."],
         ["Check response \u2014 airway \u2014 breathing \u2014 bleeding, in that "
          "order.", "Do not treat a minor wound while the airway is blocked."],
         ["Stop severe bleeding at once by direct pressure and elevation.",
          "Do not apply a tourniquet routinely."],
         ["Lay the casualty down; loosen tight clothes; cover to keep warm.",
          "Do not give alcohol, and do not apply hot-water bottles directly."],
         ["Turn an unconscious, breathing casualty into the recovery position.",
          "Do not give food or drink to an unconscious casualty."],
         ["Immobilise fractures before moving the casualty.",
          "Do not try to straighten (reduce) a fracture or dislocation."],
         ["Cover wounds with a clean sterile dressing.",
          "Do not touch the wound, wash it with unclean water, or breathe over it."],
         ["Reassure constantly; stay with the casualty.",
          "Do not allow the casualty to walk or to be crowded around."],
         ["Hand over with a clear verbal and written report.",
          "Do not exceed your training or delay medical help."]],
        weights=[6.4, 6.4], first_bold=False)

    # ------------------------------------------------------------------
    b.h2("Qualities of a Good First Aider")
    b.p("A frequently asked list. Remember the memory aid below.")
    b.box("MNEMONIC \u2014 \u2018A GOOD FIRST AIDER IS COOL PRO\u2019", [
        "**C** \u2013 **C**alm, confident and composed (does not panic).",
        "**O** \u2013 **O**bservant \u2014 notices signs, hazards and clues at "
        "the scene.",
        "**O** \u2013 **O**rganised and methodical; sets priorities.",
        "**L** \u2013 **L**eadership \u2014 takes charge, directs bystanders.",
        "**P** \u2013 **P**erceptive, **P**rompt and **P**ractical "
        "(improvises with what is at hand).",
        "**R** \u2013 **R**esourceful, **R**esponsible and **R**eassuring "
        "(tactful, sympathetic, gentle).",
        "**O** \u2013 **O**bjective \u2014 keeps within limits, knows when to "
        "stop, and maintains **confidentiality**.",
    ], kind="mnemonic")
    b.bullets([
        "Additional qualities regularly listed in textbooks: *gentle*, *tactful*, "
        "*sympathetic*, *cheerful*, *dexterous (skilful hands)*, *explicit "
        "speech*, *good memory*, *personal hygiene*, *up-to-date knowledge* and "
        "*regular refresher training*.",
        "A first aider should **retrain/refresh every 2\u20133 years**, because "
        "guidelines (especially CPR) change.",
    ])

    # ------------------------------------------------------------------
    b.h2("Duties and Responsibilities of a First Aider")
    b.numbered([
        "**Assess the situation** quickly and calmly \u2014 what happened, how "
        "many casualties, what are the dangers?",
        "**Protect** the casualty and others from further danger.",
        "**Prevent infection** \u2014 wash hands, wear gloves, do not cough over "
        "wounds.",
        "**Assess the casualty** \u2014 primary survey (DRABC) then secondary "
        "survey (head-to-toe) and history.",
        "**Give immediate treatment** according to priority.",
        "**Arrange for medical aid / ambulance** \u2014 or send a bystander with "
        "a clear message.",
        "**Arrange removal** to hospital, home or shelter in the correct "
        "position.",
        "**Remain with the casualty** until handed over to a responsible person.",
        "**Report** all findings and treatment; make a written record; "
        "**maintain confidentiality**.",
        "**Reassure** relatives and protect the casualty's belongings (hand over "
        "valuables to police/relatives with witnesses).",
    ])
    b.box("WHAT INFORMATION MUST BE GIVEN WHEN CALLING AN AMBULANCE?", [
        "Your **name and telephone number** (so the control room can call back).",
        "**Exact location** with landmarks, and the best route/approach.",
        "**What happened** (type of accident/illness) and **when** it happened.",
        "**Number, sex and approximate age** of casualties.",
        "**Nature of injuries** and the condition of each casualty "
        "(conscious? breathing? bleeding? trapped?).",
        "**Hazards still present** \u2014 fire, gas, live wires, chemicals, "
        "traffic.",
        "**Never hang up first** \u2014 let the control room end the call, and "
        "repeat the address before ringing off.",
    ], kind="note")

    # ------------------------------------------------------------------
    b.h2("Approaching an Emergency: the DRABC / DRSABCD Action Plan")
    b.p("The action plan is the single most important sequence in first aid. Two "
        "forms are taught; both are correct and examinable.")
    b.table(
        ["Letter", "Stands for", "What you actually do"],
        [["D", "Danger", "Check for danger to yourself, bystanders and casualty. "
                         "Remove danger or casualty."],
         ["R", "Response", "Shake gently and shout \u2014 \u2018Are you all "
                           "right? Open your eyes!\u2019 Use the **AVPU** scale "
                           "(Alert, Voice, Pain, Unresponsive)."],
         ["S", "Send/Shout for help", "Shout for help; ask a bystander to dial "
                                      "112/108 and fetch an AED."],
         ["A", "Airway", "Open the airway \u2014 **head tilt + chin lift** "
                         "(jaw thrust if spinal injury suspected). Clear visible "
                         "obstruction; remove loose dentures."],
         ["B", "Breathing", "**Look, listen and feel** for normal breathing for "
                            "up to **10 seconds**. Gasping (agonal breathing) is "
                            "NOT normal breathing."],
         ["C", "Circulation / CPR", "If not breathing normally \u2192 start CPR "
                                    "30:2. If breathing \u2192 check and control "
                                    "severe bleeding, then recovery position."],
         ["D", "Defibrillation / Disability",
          "Attach an **AED** as soon as available; otherwise assess "
          "**D**isability (pupils, limb movement) and **D**eformity."],
         ["E", "Exposure / Examine",
          "Expose and examine the whole body for hidden injuries, then cover to "
          "prevent hypothermia."]],
        weights=[1.1, 3.0, 9.0], align=["c", "l", "l"])

    b.h3("Primary survey versus secondary survey")
    b.table(
        ["", "Primary survey", "Secondary survey"],
        [["Purpose", "Detect and treat immediately life-threatening conditions.",
          "Detect all other injuries and illnesses once life-threats are "
          "controlled."],
         ["Sequence", "D-R-A-B-C (+D, E)",
          "History \u2192 Signs & Symptoms \u2192 head-to-toe examination "
          "\u2192 vital signs"],
         ["Time taken", "Seconds to 1\u20132 minutes.", "3\u20135 minutes."],
         ["Repeat", "Immediately if the casualty deteriorates.",
          "Vital signs every 10 minutes (every 5 if serious)."]],
        weights=[1.8, 5.4, 6.0])

    b.h3("History taking \u2014 the AMPLE and SAMPLE rules")
    b.table(
        ["SAMPLE (symptoms & history)", "AMPLE (pre-hospital hand-over)"],
        [["**S** \u2013 Signs and symptoms", "**A** \u2013 Allergies"],
         ["**A** \u2013 Allergies", "**M** \u2013 Medicines being taken"],
         ["**M** \u2013 Medication", "**P** \u2013 Past illness / pregnancy"],
         ["**P** \u2013 Past medical history", "**L** \u2013 Last meal (time of "
                                               "last food/drink)"],
         ["**L** \u2013 Last meal", "**E** \u2013 Events leading to the injury"],
         ["**E** \u2013 Events leading to the incident", "\u2014"]],
        weights=[6.4, 6.4], first_bold=False)
    b.p("Information is gathered from **three sources**: the casualty (*subjective* "
        "= symptoms), your own examination (*objective* = signs) and the "
        "bystanders/scene (*history*).")

    b.h3("Signs and symptoms \u2014 know the difference")
    b.table(
        ["Symptoms (subjective)", "Signs (objective)"],
        [["Felt and described **by the casualty** \u2014 pain, nausea, giddiness, "
          "thirst, numbness, weakness, cold feeling.",
          "Found **by the first aider** using sight, hearing, touch and smell "
          "\u2014 pallor, bleeding, swelling, deformity, sweating, rapid pulse, "
          "vomiting, smell of alcohol/petrol on breath."]],
        weights=[6.4, 6.4], first_bold=False)

    b.h3("Normal vital signs (to be memorised \u2014 asked every year)")
    b.table(
        ["Vital sign", "Normal adult", "Child (1\u201312 yr)", "Infant (<1 yr)"],
        [["Pulse rate", "60\u2013100 beats/min (average 72)", "80\u2013120/min",
          "100\u2013160/min"],
         ["Respiratory rate", "12\u201320 breaths/min (average 16\u201318)",
          "20\u201330/min", "30\u201360/min"],
         ["Blood pressure", "120/80 mm Hg", "~100/65 mm Hg", "~80/50 mm Hg"],
         ["Body temperature", "98.4\u00b0F / 37\u00b0C (range 97\u201399\u00b0F)",
          "Same", "Same"],
         ["SpO\u2082 (oxygen saturation)", "95\u2013100 %", "95\u2013100 %",
          "95\u2013100 %"],
         ["Capillary refill", "< 2 seconds", "< 2 seconds", "< 2 seconds"],
         ["Pupils", "Equal, round, react to light (3\u20135 mm)", "Same", "Same"]],
        weights=[3.0, 4.6, 2.6, 2.6])

    # ------------------------------------------------------------------
    b.h2("Triage \u2014 Sorting Multiple Casualties")
    b.p("*Triage* (French **trier** = to sort) is the classification of casualties "
        "according to the urgency of their need for treatment when resources are "
        "limited. The rule is: ==do the most for the most==.")
    b.table(
        ["Priority", "Colour tag", "Category", "Examples"],
        [["Priority 1 (P1)", "**RED**", "Immediate / critical \u2014 treat first",
          "Airway obstruction, severe external bleeding, tension pneumothorax, "
          "shock, unconscious casualty who is breathing, chest injuries"],
         ["Priority 2 (P2)", "**YELLOW**", "Urgent \u2014 treatment can wait "
                                           "1\u20132 hours",
          "Closed fractures of long bones, moderate burns without airway "
          "involvement, abdominal injury with stable vitals, back injuries"],
         ["Priority 3 (P3)", "**GREEN**", "Delayed / minor \u2014 \u2018walking "
                                          "wounded\u2019",
          "Minor cuts, sprains, small burns, minor fractures of hand/foot, "
          "anxiety states"],
         ["Priority 4 (P4)", "**BLACK / WHITE**", "Expectant or dead",
          "No breathing even after the airway is opened; injuries incompatible "
          "with life (massive head injury)"]],
        weights=[2.0, 1.9, 3.6, 7.2])
    b.bullets([
        "**START triage** = *Simple Triage And Rapid Treatment* \u2014 assesses "
        "**RPM**: **R**espiration (>30/min = red), **P**erfusion (capillary refill "
        ">2 s or absent radial pulse = red) and **M**ental status (cannot obey "
        "commands = red). Each casualty should be sorted in **under 60 seconds**.",
        "First step of START: ask everyone who can walk to move to a marked area "
        "\u2014 they are automatically **GREEN**.",
        "Triage must be **repeated** (dynamic), because a casualty's category can "
        "change.",
        "In a mass-casualty situation, the first aider does only two things while "
        "triaging: **open the airway** and **stop major bleeding**.",
    ])

    # ------------------------------------------------------------------
    b.h2("The First-Aid Box / Kit")
    b.p("A first-aid box should be made of metal or strong plastic, be dust- and "
        "damp-proof, be clearly marked with a **white cross on a green "
        "background** (the international first-aid sign), be kept in a known, "
        "easily reachable place, and be checked and restocked regularly by a "
        "named person.")
    b.table(
        ["Group", "Contents", "Chief uses"],
        [["Dressings",
          "Sterile gauze pieces, non-adherent (paraffin) dressings, cotton wool, "
          "adhesive dressings (Band-Aid), eye pads, sterile pads",
          "Cover wounds, absorb blood and discharge, control bleeding"],
         ["Bandages",
          "Roller (cotton) bandages 2.5/5/7.5/10 cm, triangular bandages, crepe "
          "(elastic) bandage, adhesive plaster tape, safety pins, clips",
          "Hold dressings, support and immobilise, make slings"],
         ["Antiseptics",
          "Povidone-iodine (Betadine) solution/ointment, chlorhexidine, "
          "70 % alcohol/spirit swabs, hydrogen peroxide, potassium permanganate, "
          "savlon/dettol",
          "Clean skin and wounds, prevent infection"],
         ["Instruments",
          "Blunt-nosed scissors, tweezers/forceps, safety pins, disposable "
          "gloves, torch, thermometer, tourniquet (for medical use only), "
          "resuscitation face-shield/pocket mask, kidney tray",
          "Cutting, removal of splinters, protection, examination, safe rescue "
          "breathing"],
         ["Medicines (basic)",
          "Paracetamol, ORS sachets, antiseptic cream, oral antihistamine "
          "(cetirizine/chlorpheniramine), antacid, soda bicarb, glucose, "
          "smelling salts (sal volatile), calamine lotion, silver-sulphadiazine "
          "cream",
          "Fever and pain, dehydration, allergy, acidity, burns, faint, stings"],
         ["Records & misc.",
          "Notebook and pencil, first-aid manual, list of emergency numbers, "
          "cotton sling, plastic bags, blanket/space blanket, drinking water, "
          "hand sanitiser",
          "Record keeping, warmth, waste disposal, hygiene"]],
        weights=[1.9, 6.2, 4.6])
    b.box("KIT RULES \u2014 EXAM POINTS", [
        "International first-aid symbol: ==white cross on green background== "
        "(green = safety). The **red cross on white** is the protective emblem of "
        "the Red Cross and must not be used on ordinary kits.",
        "The box must contain **no loose tablets**, no expired items, and must be "
        "**locked away from children but never locked to the user**.",
        "Contents must be checked **after every use** and at least once a month; "
        "a checklist is kept inside the lid.",
        "Factories Act, 1948 (Sec. 45): a first-aid box for **every 150 workers**, "
        "in charge of a trained person, available during working hours; "
        "an ambulance room is required where **more than 500 workers** are "
        "employed.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Personal Protection and Infection Control for the First Aider")
    b.bullets([
        "**Universal (standard) precautions:** treat every casualty's blood and "
        "body fluid as potentially infectious (HIV, hepatitis B and C).",
        "**Hand hygiene:** wash with soap and running water for 40\u201360 seconds "
        "before and after every casualty; alcohol rub (20\u201330 s) if hands are "
        "not visibly soiled.",
        "**Barriers:** disposable gloves, plastic apron, eye protection, "
        "face-shield or pocket mask for rescue breathing.",
        "**Avoid** direct mouth-to-mouth contact if a barrier is available; "
        "compression-only CPR is acceptable for an untrained/unwilling rescuer.",
        "**Cover your own cuts** with a waterproof dressing before giving first "
        "aid.",
        "**Never re-cap or re-use needles**; dispose of sharps in a puncture-proof "
        "container; soiled dressings go into a sealed plastic bag "
        "(yellow bag \u2192 incineration).",
        "**Needle-stick / splash injury:** wash immediately with soap and water "
        "(do not squeeze or scrub, do not use bleach on the wound), irrigate eyes "
        "with water, report at once and seek **post-exposure prophylaxis (PEP) "
        "within 2 hours** (not later than 72 hours).",
    ])

    # ------------------------------------------------------------------
    b.h2("The Chain of Survival and the Golden Hour")
    b.table(
        ["Link", "Action", "Why it matters"],
        [["1. Early recognition and call for help",
          "Recognise cardiac arrest / serious injury and dial 112 or 108.",
          "Nothing else can start until help is summoned."],
         ["2. Early CPR", "Immediate bystander chest compressions.",
          "Doubles or triples survival; buys time for the brain "
          "(irreversible damage after 3\u20134 minutes without oxygen)."],
         ["3. Early defibrillation", "Use an AED within 3\u20135 minutes.",
          "Survival falls by ==7\u201310 % for every minute== of delay in "
          "defibrillation."],
         ["4. Early advanced care", "Paramedics, drugs, airway, hospital ICU.",
          "Stabilises the heart rhythm and treats the cause."],
         ["5. Post-resuscitation care / rehabilitation",
          "Targeted temperature management, intensive care, rehabilitation.",
          "Preserves brain function and quality of life."]],
        weights=[3.0, 5.2, 5.6])
    b.box("TIME FACTS THAT ARE ASKED AGAIN AND AGAIN", [
        "**Golden hour** \u2014 first **60 minutes** after major trauma; "
        "definitive care within it markedly improves survival.",
        "**Platinum 10 minutes** \u2014 ideal on-scene time for a critical trauma "
        "casualty.",
        "**Brain damage** begins after **3\u20134 minutes** of complete oxygen "
        "deprivation; it is usually irreversible after **8\u201310 minutes**.",
        "**Breathing check** during DRABC: not more than **10 seconds**.",
        "**Clinical death** = stopped breathing and circulation (reversible); "
        "**biological/brain death** = irreversible death of brain cells.",
        "Survival from cardiac arrest without CPR falls by about "
        "**7\u201310 % per minute**.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Medico-Legal Aspects of First Aid")
    b.h3("Consent")
    b.table(
        ["Type of consent", "Meaning / when used"],
        [["Expressed (informed) consent",
          "The conscious, mentally sound adult casualty **says or nods** that he "
          "accepts help. Always introduce yourself, say you are trained, and ask "
          "permission."],
         ["Implied consent",
          "Assumed when the casualty is **unconscious, confused, seriously "
          "injured or a minor with no guardian present** \u2014 the law presumes "
          "a reasonable person would want life-saving help (doctrine of "
          "emergency)."],
         ["Consent for a minor",
          "Taken from the parent/guardian; if absent, implied consent applies. "
          "In India, valid consent age for medical treatment is **18 years** "
          "(12 years for examination)."],
         ["Refusal of consent",
          "A competent adult may refuse first aid. Do not force treatment; "
          "record the refusal, ask a witness to sign, and call the ambulance "
          "anyway."]],
        weights=[3.2, 9.4])
    b.h3("Duties, negligence and protection in law")
    b.dl([
        ("Duty of care", "A legal/ethical obligation to act; it applies to a "
                         "designated workplace first aider on duty. An ordinary "
                         "bystander in India has a moral duty and is protected "
                         "when he helps."),
        ("Standard of care", "You are judged by what a **reasonable person with "
                             "the same training** would have done in the same "
                             "circumstances \u2014 not by the outcome."),
        ("Negligence", "Failure to give the expected standard of care, causing "
                       "harm. Four elements: **duty, breach, causation, "
                       "damage**."),
        ("Abandonment", "Leaving a casualty before handing over to someone of "
                        "equal or greater ability \u2014 a punishable act."),
        ("Confidentiality", "Information about the casualty must not be revealed "
                            "to the press, employer or onlookers; give it only to "
                            "the doctor, ambulance staff or police."),
        ("Good Samaritan protection (India)",
         "Supreme Court guidelines (2016) and **Section 134A of the Motor "
         "Vehicles (Amendment) Act, 2019** protect a bystander who helps a road "
         "accident victim: he **cannot** be held civilly or criminally liable, "
         "cannot be forced to reveal his identity, and cannot be detained or "
         "asked to pay for treatment."),
        ("Duty of the hospital", "Every hospital (government or private) must "
                                 "give immediate emergency treatment to an "
                                 "accident victim \u2014 *Parmanand Katara v. "
                                 "Union of India* (1989): **saving life takes "
                                 "precedence over all formalities and police "
                                 "procedures**."),
        ("Preserving evidence", "At a crime scene, disturb as little as possible; "
                                "note the original position of the casualty and "
                                "objects; hand over removed clothing to the "
                                "police."),
    ])
    b.h3("Records and reporting")
    b.bullets([
        "Keep a **first-aid register/accident report** noting: date and time of "
        "incident, name/age/sex, what happened, findings (signs and symptoms), "
        "vital signs with times, treatment given, time of calling help, to whom "
        "the casualty was handed over, and your name and signature.",
        "Records are needed for insurance, workmen's compensation, police enquiry "
        "and for later medical care. Write facts only \u2014 no opinions.",
    ])

    # ------------------------------------------------------------------
    b.h2("Emergency Telephone Numbers in India")
    b.table(
        ["Number", "Service"],
        [["**112**", "All-in-one national emergency helpline (ERSS) \u2014 "
                     "police, fire, ambulance, disaster"],
         ["**108**", "Free emergency ambulance (EMRI) \u2014 accident/medical "
                     "emergency"],
         ["**102**", "Free ambulance for pregnant women, mothers and infants "
                     "(JSSK)"],
         ["**100 / 112**", "Police"],
         ["**101**", "Fire brigade"],
         ["**104**", "Health advice / medical helpline"],
         ["**1098**", "CHILDLINE \u2014 children in distress"],
         ["**1091**", "Women's helpline; **181** women in distress"],
         ["**1073 / 1033**", "Road accident / national highway helpline"],
         ["**14567**", "Senior citizen (Elderline) helpline"],
         ["**1800-11-6117**", "National Poisons Information Centre, AIIMS "
                              "New Delhi (24 \u00d7 7)"],
         ["**14416 / 1800-891-4416**", "Tele-MANAS mental-health helpline; "
                                       "**9152987821** iCALL"],
         ["**1070 / 1077**", "State / district disaster management control room"],
         ["**1962**", "Animal ambulance / veterinary helpline"]],
        weights=[2.6, 9.8], first_bold=False)

    # ------------------------------------------------------------------
    b.h2("History and Organisations of First Aid (General Awareness)")
    b.table(
        ["Fact", "Detail"],
        [["Who coined the term \u2018first aid\u2019",
          "**Johannes Friedrich August von Esmarch** (German surgeon) \u2014 "
          "*erste hilfe*; he also introduced the **Esmarch bandage** "
          "(triangular bandage) and is called the *father of first aid*."],
         ["Esmarch triangular bandage", "A triangular cloth bandage; the "
                                        "standard first-aid bandage even today."],
         ["Red Cross founded", "**1863**, Geneva, by **Jean Henri Dunant** "
                               "(first Nobel Peace Prize, 1901). Emblem: red "
                               "cross on white \u2014 the reverse of the Swiss "
                               "flag."],
         ["First Geneva Convention", "**1864** \u2014 protection of the wounded "
                                     "in war."],
         ["St. John Ambulance Association", "Founded **1877** in England; the "
                                            "pioneer of organised first-aid "
                                            "training and certification."],
         ["Indian Red Cross Society", "Established **1920** (Indian Red Cross "
                                      "Society Act XV of 1920); President of "
                                      "India is its President."],
         ["World First Aid Day", "**Second Saturday of September** every year "
                                 "(started 2000 by IFRC)."],
         ["World Red Cross Day", "**8 May** \u2014 Henri Dunant's birthday."],
         ["World Health Day / WHO", "**7 April**; WHO founded 1948, "
                                    "headquarters Geneva."],
         ["Ambulance", "From Latin *ambulare* (to walk). Modern ambulance "
                       "service traces to the Napoleonic surgeon "
                       "**Dominique-Jean Larrey**, who introduced field "
                       "ambulances and battlefield triage."],
         ["Modern CPR", "Mouth-to-mouth ventilation revived by **Peter Safar** "
                        "and James Elam (1950s); closed-chest compression by "
                        "**Kouwenhoven, Jude and Knickerbocker (1960)**; "
                        "Safar is called the *father of CPR*."],
         ["Florence Nightingale", "Founder of modern nursing (Crimean War, "
                                  "\u2018Lady with the Lamp\u2019); "
                                  "International Nurses Day **12 May**."]],
        weights=[3.2, 9.4])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "First aid = **immediate, temporary, skilled** help with **available "
        "material** until medical aid arrives.",
        "Aims = **3 P's**: Preserve life (first aim), Prevent worsening, Promote "
        "recovery.",
        "Action plan = **D-R-S-A-B-C-D**; treatment priority = **airway \u2192 "
        "breathing \u2192 bleeding \u2192 shock**.",
        "Breathing is checked for a maximum of **10 seconds**; brain damage starts "
        "in **3\u20134 minutes**.",
        "Triage colours = **RED (immediate) \u2013 YELLOW (urgent) \u2013 GREEN "
        "(delayed) \u2013 BLACK (dead/expectant)**.",
        "First-aid symbol = **white cross on green**; Red Cross emblem = **red "
        "cross on white**.",
        "Ambulance = **108**; universal emergency = **112**; poison information = "
        "**1800-11-6117**.",
        "Term \u2018first aid\u2019 coined by **Esmarch**; Red Cross founded by "
        "**Henri Dunant (1863)**; St. John Ambulance **1877**; Indian Red Cross "
        "**1920**.",
        "Never give **anything by mouth** to an unconscious casualty; never "
        "**reduce** a fracture or dislocation; never **exceed your training**.",
    ])
