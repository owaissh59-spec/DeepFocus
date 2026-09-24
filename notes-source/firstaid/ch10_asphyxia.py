# -*- coding: utf-8 -*-
"""Chapter 10 - Asphyxia."""


def render(b):
    b.chapter(
        "Asphyxia",
        "Meaning and causes of asphyxia, its stages and signs, general "
        "management, and the first aid of drowning, hanging, strangulation, "
        "suffocation, gas poisoning, smoke inhalation, traumatic asphyxia, "
        "asthma and hyperventilation.",
        syllabus=[
            "Asphyxia \u2014 definition, causes and classification, stages, "
            "signs and symptoms, general principles of treatment.",
            "First aid in drowning, hanging, strangulation, throttling, "
            "suffocation, smothering, gas and smoke inhalation, traumatic "
            "asphyxia, choking, asthma, croup and hyperventilation.",
        ])

    # ------------------------------------------------------------------
    b.h2("Meaning and Definition")
    b.box("DEFINITION", [
        "**Asphyxia** (Greek *a* = without, *sphyxis* = pulse) is the condition "
        "in which the **supply of oxygen to the blood and tissues is cut off or "
        "greatly reduced, with an accumulation of carbon dioxide in the body**, "
        "because of **interference with breathing**.",
        "Other names: **suffocation**; the state of oxygen lack in the tissues is "
        "**hypoxia/anoxia**, and the state of excess carbon dioxide is "
        "**hypercapnia**.",
        "Asphyxia is the **commonest cause of preventable death** in first aid "
        "\u2014 and the first aider's first duty (the \u2018A\u2019 and "
        "\u2018B\u2019 of DRABC) is to correct it.",
    ], kind="def")
    b.p("Death from asphyxia occurs in **3\u20135 minutes**; the **brain** is "
        "the first organ to suffer because it has no store of oxygen.")

    # ------------------------------------------------------------------
    b.h2("Causes and Classification of Asphyxia")
    b.table(
        ["Group", "Mechanism", "Examples"],
        [["**1. Obstruction of the air passages (mechanical)**",
          "Air cannot reach the lungs",
          "**Choking** on food or a foreign body; **the tongue falling back in "
          "an unconscious casualty** (commonest of all); swelling of the throat "
          "in burns, scalds of the mouth, **anaphylaxis**, croup, diphtheria; "
          "blood, vomit or water in the airway; **drowning**; **hanging, "
          "strangulation, throttling**"],
         ["**2. Closure of the external openings (smothering)**",
          "Mouth and nose blocked from outside",
          "Pillow, plastic bag, cloth, hand over the face; a baby sleeping face "
          "down or overlaid by an adult; sand, grain, earth or a landslide "
          "burying the face"],
         ["**3. Compression of the chest (traumatic asphyxia)**",
          "The chest cannot expand",
          "Crushing by a wall, vehicle, machinery or earth; being crushed in a "
          "**stampede or crowd**; being pinned under a heavy weight"],
         ["**4. Lack of oxygen in the surrounding air (atmospheric/environmental)**",
          "The air itself is deficient in oxygen or contains a poisonous gas",
          "**Confined spaces** \u2014 wells, tanks, silos, sewers, mines, ship "
          "holds; **carbon monoxide** from charcoal fires, geysers, car exhaust; "
          "**LPG, CNG, sewer gas (H\u2082S), ammonia, chlorine**; **smoke** in a "
          "fire; high altitude; deep-sea diving accidents"],
         ["**5. Paralysis of the respiratory centre or muscles**",
          "The brain or nerves cannot drive breathing",
          "**Electric shock and lightning**; poisoning by **opium/morphine, "
          "barbiturates, alcohol, organophosphates, cobra venom**; severe **head "
          "or spinal injury**; stroke; tetanus; poliomyelitis; **status "
          "epilepticus**"],
         ["**6. Disease of the lungs and circulation**",
          "Gas exchange in the lungs fails",
          "Severe **asthma**, pneumonia, pulmonary oedema, collapsed lung "
          "(**pneumothorax**), pleural effusion, emphysema, pulmonary embolism, "
          "heart failure, severe anaemia"]],
        weights=[3.0, 2.8, 7.0], size=8.6)

    # ------------------------------------------------------------------
    b.h2("Stages, Signs and Symptoms")
    b.table(
        ["Stage", "What happens", "Signs"],
        [["**1. Stage of dyspnoea (breathlessness)**",
          "Rising CO\u2082 stimulates the respiratory centre",
          "**Rapid, deep, noisy and difficult breathing**; distress and anxiety; "
          "rapid pulse; casualty fights for air, uses the neck and shoulder "
          "muscles, and cannot speak in full sentences"],
         ["**2. Stage of convulsions**",
          "Oxygen lack begins to affect the brain",
          "**Blueness (cyanosis)** of the lips, ear lobes, tongue and nail beds; "
          "congested, swollen face with **prominent veins**; **bloodshot, "
          "bulging eyes**; frothing at the mouth; **convulsions and involuntary "
          "passing of urine/stool**; loss of consciousness"],
         ["**3. Stage of exhaustion / apnoea**",
          "The respiratory centre becomes paralysed",
          "Breathing becomes **slow, shallow, gasping (agonal) and then stops**; "
          "pulse becomes feeble and irregular; **pupils dilate and become "
          "fixed**; muscles relax; **cardiac arrest and death**"]],
        weights=[3.0, 3.4, 6.4])
    b.bullets([
        "**Cardinal signs of asphyxia** \u2014 **difficult noisy breathing, "
        "cyanosis (blueness), congested swollen face, frothing at the mouth, "
        "restlessness and fighting for breath, falling level of consciousness, "
        "and finally stoppage of breathing**.",
        "In **carbon monoxide poisoning** the skin may be **cherry-red instead "
        "of blue** \u2014 a classical exception.",
        "In **anaemia or severe blood loss**, cyanosis may not be evident even "
        "with severe hypoxia.",
    ])

    # ------------------------------------------------------------------
    b.h2("General Principles of Treatment")
    b.numbered([
        "**Remove the cause of asphyxia, or the casualty from the cause** "
        "\u2014 taking care of your own safety (gas, fire, electricity, water, "
        "confined space).",
        "**Open and clear the airway** \u2014 head tilt\u2013chin lift; remove "
        "vomit, blood, weed, dentures, foreign bodies.",
        "**Give fresh air / oxygen** \u2014 loosen tight clothing at the neck, "
        "chest and waist; keep bystanders away so that air circulates.",
        "**Start artificial respiration at once** if breathing has stopped, and "
        "**full CPR** if there is no pulse.",
        "Once breathing returns, place the casualty in the **recovery position** "
        "and keep him warm.",
        "**Treat the associated injuries** \u2014 burns, fractures, wounds "
        "\u2014 and **treat for shock**.",
        "**Monitor** breathing, pulse and consciousness continuously; breathing "
        "may stop again.",
        "**Send every casualty to hospital**, even if he recovers \u2014 "
        "**secondary (delayed) lung oedema** may develop hours later, especially "
        "after drowning or smoke/gas inhalation.",
    ])

    # ------------------------------------------------------------------
    b.h2("Drowning")
    b.p("**Drowning** is asphyxia caused by the **immersion of the mouth and "
        "nose in a liquid**. Even a few centimetres of water in a bucket or tub "
        "can drown an infant.")
    b.table(
        ["Term / type", "Meaning"],
        [["**Wet drowning**", "Water is actually inhaled into the lungs "
                             "(about 85\u201390 % of cases) \u2192 washes away "
                             "surfactant, causes lung oedema"],
         ["**Dry drowning**", "Sudden **spasm of the larynx (laryngospasm)** on "
                              "contact with water stops breathing; **little or "
                              "no water enters the lungs** (10\u201315 %)"],
         ["**Secondary (delayed) drowning**", "Deterioration with breathlessness "
                                              "and lung oedema **1\u201372 "
                                              "hours after** apparently "
                                              "successful rescue \u2014 the "
                                              "reason every near-drowning "
                                              "casualty must go to hospital"],
         ["**Immersion syndrome**", "Sudden cardiac arrest from **vagal "
                                    "inhibition** on plunging into very cold "
                                    "water"],
         ["**Near-drowning**", "Survival after a drowning episode"],
         ["Fresh water vs sea water", "Fresh water is **hypotonic** \u2014 "
                                      "absorbed into the blood, may haemolyse "
                                      "RBCs; sea water is **hypertonic** "
                                      "\u2014 draws fluid into the alveoli. "
                                      "First aid is the **same** for both"]],
        weights=[3.0, 9.6])
    b.h3("Rescue \u2014 protect yourself first")
    b.bullets([
        "**\u2018REACH \u2013 THROW \u2013 ROW \u2013 GO\u2019** is the order of "
        "rescue: **reach** out with a stick, rope or clothing; **throw** a rope, "
        "float, tube, empty bottle or plank; **row** a boat; and only as a last "
        "resort **go** (swim) \u2014 and only if you are a trained swimmer.",
        "Never jump in alone if you cannot swim well; take a float with you; "
        "approach the casualty from behind.",
        "**Suspect a spinal injury** in a diving accident \u2014 support the "
        "head and neck in line and float the casualty out on his back.",
        "Keep the casualty **horizontal** while lifting him from the water if "
        "possible (vertical lifting can cause collapse).",
    ])
    b.h3("First aid for a drowning casualty")
    b.numbered([
        "Get the casualty out of the water as quickly and safely as possible; "
        "**if he is not breathing, give 5 rescue breaths even in shallow "
        "water**.",
        "Lay him on his **back on a firm surface, head slightly lower** if "
        "possible, and **clear the mouth** of weed, sand, vomit and dentures.",
        "**Open the airway and check breathing.** If absent, begin **CPR with "
        "5 initial rescue breaths, then 30 : 2**. Call 112/108 (if alone, give "
        "**1 minute of CPR first**, then call).",
        "**Do NOT waste time trying to drain water from the lungs** \u2014 do "
        "not hold the casualty upside down, do not press on the abdomen, do not "
        "use the Heimlich manoeuvre for water.",
        "**Expect vomiting** \u2014 turn the head to one side, clear the mouth "
        "and continue.",
        "As soon as breathing returns, place in the **recovery position** and "
        "**treat for hypothermia** \u2014 remove wet clothing, dry the casualty, "
        "wrap in blankets, protect from wind; handle gently.",
        "**Give nothing by mouth** while unconscious; when fully conscious, warm "
        "sweet drinks may be given.",
        "**Send every casualty to hospital**, even one who appears fully "
        "recovered \u2014 because of **secondary drowning**.",
        "In cold-water drowning, **continue resuscitation for a long time** "
        "\u2014 survival has followed 30\u201360 minutes of submersion in cold "
        "water, especially in children.",
    ])

    # ------------------------------------------------------------------
    b.h2("Hanging, Strangulation and Throttling")
    b.table(
        ["Term", "Meaning"],
        [["**Hanging**", "Constriction of the neck by a ligature, the "
                        "**weight of the body** providing the force"],
         ["**Strangulation**", "Constriction of the neck by a ligature or other "
                               "force **other than the body weight** (rope, "
                               "scarf, wire, cord round a baby's neck)"],
         ["**Throttling (manual strangulation)**", "Constriction of the neck by "
                                                   "**hands**"],
         ["**Mugging**", "Constriction by a forearm across the throat from behind"]],
        weights=[3.4, 9.2])
    b.bullets([
        "Signs: **a mark, groove or bruising round the neck**; congested, "
        "swollen, blue face; **bloodshot eyes with tiny haemorrhages "
        "(petechiae)**; protruding tongue; froth at the mouth; unconsciousness; "
        "absent or gasping breathing; possible **fracture of the cervical "
        "spine or larynx**.",
    ])
    b.numbered([
        "**Take the weight of the body at once** and **cut or remove the "
        "constriction immediately** \u2014 cut **above the knot** and "
        "**preserve the knot for the police** (it is a medico-legal case).",
        "**Support the head and neck** \u2014 assume a **spinal injury** and do "
        "not bend the neck.",
        "Lay the casualty down, **open the airway (jaw thrust)** and check "
        "breathing; start **CPR** if needed.",
        "If breathing, place in the **recovery position** and watch continuously "
        "\u2014 **swelling of the throat can obstruct the airway even hours "
        "later**.",
        "**Do not disturb the scene** more than necessary; note the position of "
        "the body and the time; **inform the police**.",
        "**Every casualty must go to hospital**, however well he seems.",
    ])

    # ------------------------------------------------------------------
    b.h2("Suffocation and Smothering")
    b.bullets([
        "Causes: a **plastic bag or sheet over the face**, a pillow or cloth, a "
        "hand, a baby's face pressed into soft bedding or overlaid by a sleeping "
        "adult, being buried under **sand, grain, earth or a landslide**, and "
        "being trapped in a **collapsed building or a refrigerator/box**.",
        "Treatment: **remove the obstruction from the face at once**; clear the "
        "mouth and nose of sand, mud or vomit; open the airway; start artificial "
        "respiration/CPR if needed; treat injuries; recovery position; hospital.",
        "In burial under earth or grain, **clear the chest as well as the face** "
        "so that the chest can expand, and expect crush injury.",
        "**Prevention:** keep plastic bags away from children, never let a baby "
        "sleep on a soft pillow or with a plastic sheet, remove doors from "
        "disused refrigerators, and fence wells and sand pits.",
    ])

    # ------------------------------------------------------------------
    b.h2("Asphyxia from Gases, Fumes and Smoke")
    b.table(
        ["Gas / fume", "Source and features", "First aid"],
        [["**Carbon monoxide (CO)**", "Charcoal *angeethi*/*sigri* and gas "
                                     "geysers in closed rooms, car exhaust, "
                                     "coal stove, fire smoke. Colourless and "
                                     "**odourless**; binds haemoglobin **200"
                                     "\u2013250 times** more strongly than "
                                     "oxygen. Features: headache, giddiness, "
                                     "nausea, confusion, **cherry-red skin**, "
                                     "collapse; whole families are affected "
                                     "together",
          "Ventilate the room from outside; **switch off the source**; drag the "
          "casualty into fresh air (do not enter without protection); give "
          "**100 % oxygen** if available; CPR if needed; hospital \u2014 may "
          "need hyperbaric oxygen"],
         ["**LPG / CNG / cooking gas**", "Leaking cylinder or pipe; heavier than "
                                         "air (LPG) so it collects near the "
                                         "floor; **explosion risk**",
          "**Do not switch on or off any light or fan and do not strike a "
          "match**; open doors and windows, close the cylinder valve, remove the "
          "casualty into fresh air, call the fire brigade/gas agency"],
         ["**Sewer gas (hydrogen sulphide)**", "Manholes, septic tanks, drains; "
                                              "smell of **rotten eggs** which "
                                              "quickly deadens the sense of "
                                              "smell; causes instant collapse",
          "**Never enter** a manhole/tank to rescue without breathing apparatus "
          "and a lifeline \u2014 many would-be rescuers die; call the fire "
          "brigade; ventilate; haul the casualty out with a rope and harness; "
          "give oxygen and CPR"],
         ["**Smoke (fire)**", "Hot smoke, soot, CO and cyanide; burns of the "
                             "airway. Features: **soot round the mouth and "
                             "nose, singed nasal hairs, hoarse voice, "
                             "barking cough, black sputum, breathlessness**",
          "Move to fresh air (crawl low under smoke); sit the casualty up; "
          "**oxygen**; watch for **airway swelling** \u2014 transfer urgently; "
          "treat burns"],
         ["**Chlorine, ammonia, nitrous fumes, pesticide fumes**",
          "Industrial leaks, swimming-pool chemicals, cold storages, spraying in "
          "closed spaces; intense irritation of eyes and throat, coughing, "
          "choking, pulmonary oedema",
          "Move upwind and uphill; wash eyes and skin with plenty of water; sit "
          "the casualty up; oxygen; **strict rest** and hospital (oedema may be "
          "delayed 6\u201324 hours)"],
         ["**Confined spaces \u2014 wells, silos, tanks, holds, mines**",
          "Air deficient in oxygen or full of CO\u2082/methane; a candle will not "
          "burn in it",
          "**Never enter alone or without breathing apparatus and a lifeline.** "
          "Test the atmosphere, ventilate, wear a harness, have two persons "
          "outside; remove the casualty and resuscitate in the open air"]],
        weights=[2.6, 5.4, 5.0], size=8.4)
    b.box("RESCUER SAFETY IN GAS ATMOSPHERES", [
        "**More rescuers die in confined-space accidents than victims.** Never "
        "enter a well, tank, manhole or gas-filled room without **breathing "
        "apparatus, a safety harness and lifeline, and at least two attendants "
        "outside**.",
        "Take a **deep breath and hold it** only for a very brief snatch rescue "
        "close to the entrance \u2014 never rely on it.",
        "**Do not use a naked flame** to test or light a gas-filled space; "
        "switch nothing on or off.",
        "Bring the casualty into **fresh air** before beginning any treatment.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Traumatic Asphyxia and Other Causes")
    b.dl([
        ("Traumatic asphyxia (crush asphyxia)",
         "Prolonged crushing of the chest or abdomen \u2014 a wall, vehicle, "
         "earth fall or **crowd stampede**. Signs: **deep blue-purple "
         "congestion of the face, neck and upper chest with bloodshot eyes**, "
         "while the skin below the crush is normal. Treatment: relieve the "
         "pressure, note the time, give oxygen, treat for shock and crush "
         "injury, urgent transfer."),
        ("Choking", "The commonest cause of sudden asphyxia in a conscious "
                    "person \u2014 see Chapter 4 (back blows, abdominal "
                    "thrusts, CPR if unconscious)."),
        ("Anaphylaxis / burns of the airway", "Swelling of the tongue and throat "
                                              "closes the airway \u2014 "
                                              "**adrenaline** and urgent "
                                              "transfer; sit the casualty up."),
        ("Asthma attack", "Spasm and swelling of the bronchi \u2014 "
                          "**difficulty in breathing out, wheeze, use of "
                          "accessory muscles, inability to speak in "
                          "sentences**. First aid: **sit the casualty up "
                          "leaning slightly forward**, keep calm, help him use "
                          "his own **reliever (blue salbutamol) inhaler "
                          "\u2014 2 puffs, repeat every 2 minutes up to 10 "
                          "puffs**, loosen clothing, fresh air; call the "
                          "ambulance if there is no relief in 5\u201310 "
                          "minutes, if speech is impossible, or if the casualty "
                          "becomes exhausted or blue. **Never make an asthmatic "
                          "lie flat.**"),
        ("Croup / diphtheria (children)", "Barking cough, hoarse voice, noisy "
                                          "breathing (stridor) \u2014 sit the "
                                          "child up, calm him, provide humid "
                                          "air (steam from a hot shower in the "
                                          "bathroom), **never examine the "
                                          "throat with a spoon**, urgent "
                                          "medical help."),
        ("Hyperventilation", "Over-breathing from anxiety or panic \u2014 "
                             "dizziness, tingling of the hands and lips, cramps "
                             "of the hands and feet (tetany), a feeling of "
                             "suffocation. First aid: **be firm and reassuring, "
                             "lead the casualty to a quiet place, ask him to "
                             "breathe slowly (e.g. in for 4, out for 6)**; "
                             "breathing into cupped hands may help. "
                             "**Do not use a paper bag** (obsolete and "
                             "dangerous) and always exclude a genuine cause "
                             "such as asthma, diabetes or a heart problem."),
        ("High altitude / mountain sickness",
         "Thin air \u2014 headache, breathlessness, nausea, sleeplessness; "
         "**descend at once**, rest, oxygen if available."),
    ])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Asphyxia = **interference with breathing causing oxygen lack and "
        "CO\u2082 accumulation**; death in **3\u20135 minutes**.",
        "Six groups of causes: **airway obstruction, smothering, chest "
        "compression, bad atmosphere, paralysis of the respiratory centre, and "
        "lung disease**.",
        "Three stages: **dyspnoea \u2192 convulsions \u2192 exhaustion/apnoea**; "
        "cardinal signs are **noisy difficult breathing, cyanosis, congested "
        "face and froth at the mouth**.",
        "Treatment principle: **remove the cause \u2192 clear and open the "
        "airway \u2192 fresh air/oxygen \u2192 artificial respiration/CPR "
        "\u2192 recovery position \u2192 hospital**.",
        "In **carbon monoxide** poisoning the skin is **cherry-red**, not blue; "
        "CO binds haemoglobin **200\u2013250 times** more strongly than oxygen.",
        "Drowning: rescue order **reach\u2013throw\u2013row\u2013go**; give "
        "**5 rescue breaths first**; **never try to drain water from the lungs**; "
        "always hospitalise (**secondary drowning**).",
        "Hanging/strangulation: **take the weight, cut above the knot, preserve "
        "the knot, suspect a neck injury, inform the police**.",
        "**Never enter a well, tank or manhole** without breathing apparatus and "
        "a lifeline.",
        "Asthma: **sit up, own blue inhaler 2 puffs**, never lie flat; "
        "hyperventilation: reassure and slow the breathing, no paper bag.",
    ])
