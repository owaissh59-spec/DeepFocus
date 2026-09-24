# -*- coding: utf-8 -*-
"""Chapter 7 - Shock."""


def render(b):
    b.chapter(
        "Shock",
        "Meaning and mechanism, all types of shock, stages, signs and symptoms, "
        "general and specific management, anaphylaxis and the difference between "
        "shock and fainting.",
        syllabus=[
            "Shock \u2014 definition, types (hypovolaemic, cardiogenic, "
            "neurogenic, anaphylactic, septic, psychogenic), causes, stages, "
            "signs and symptoms and complete first-aid management.",
            "Anaphylactic shock and the use of adrenaline; difference between "
            "shock and fainting; position of the casualty and the \u2018nothing "
            "by mouth\u2019 rule.",
        ])

    # ------------------------------------------------------------------
    b.h2("Meaning and Mechanism")
    b.box("DEFINITION", [
        "**Shock** is a **condition of acute circulatory failure in which the "
        "flow of oxygenated blood through the tissues becomes inadequate to "
        "maintain normal cell function** \u2014 in simple words, "
        "*\u2018insufficient blood is reaching the vital organs\u2019*.",
        "Shock is **not** the same as fright or emotional \u2018shock\u2019; it "
        "is a **progressive, life-threatening physical state** that will end in "
        "death if not reversed.",
        "It is produced whenever there is (a) **loss of blood or fluid volume**, "
        "(b) **failure of the heart to pump**, or (c) **excessive widening of "
        "the blood vessels**. Blood pressure = cardiac output \u00d7 peripheral "
        "resistance; shock follows a fall in either factor.",
    ], kind="def")
    b.p("As blood flow falls, the body compensates through **adrenaline**: the "
        "heart beats faster, the skin vessels constrict (**pale, cold, clammy "
        "skin**), breathing quickens and fluid is drawn from the tissues "
        "(**thirst**). If the cause continues, compensation fails, blood "
        "pressure falls, the brain and kidneys suffer, and the process becomes "
        "**irreversible**.")

    # ------------------------------------------------------------------
    b.h2("Classification of Shock")
    b.table(
        ["Type", "Mechanism", "Common causes"],
        [["**Hypovolaemic (oligaemic) shock** \u2014 the commonest type",
          "**Loss of blood, plasma or body fluid** \u2192 reduced circulating "
          "volume",
          "**Haemorrhage** (external or internal), **burns and scalds** "
          "(plasma loss), severe **vomiting and diarrhoea** (cholera, "
          "gastro-enteritis), excessive sweating, crush injury, intestinal "
          "obstruction, peritonitis, diabetic coma (dehydration)"],
         ["**Cardiogenic shock**", "**Failure of the heart to pump** effectively",
          "**Heart attack (myocardial infarction)**, severe arrhythmias, heart "
          "failure, cardiac tamponade, myocarditis, poisoning of the heart, "
          "electric shock"],
         ["**Neurogenic (vasogenic) shock**", "Loss of nervous control of the "
                                              "vessel walls \u2192 sudden "
                                              "**widespread vasodilatation**",
          "**Spinal cord injury** (above T6), severe **head injury**, severe "
          "pain, spinal anaesthesia"],
         ["**Anaphylactic shock**", "Severe, generalised **allergic reaction** "
                                    "with massive vasodilatation and leaking "
                                    "capillaries",
          "**Bee/wasp stings, penicillin and other drugs, peanuts, egg, fish, "
          "shellfish, latex, vaccines, radiological dyes**"],
         ["**Septic (toxic) shock**", "**Bacterial toxins** in the blood damage "
                                      "vessels and cause dilatation and leakage",
          "Severe infection \u2014 septicaemia, peritonitis, infected wounds, "
          "burns, septic abortion, pneumonia"],
         ["**Obstructive shock**", "Mechanical **obstruction to blood flow** in "
                                   "or around the heart",
          "**Tension pneumothorax**, cardiac tamponade, massive pulmonary "
          "embolism"],
         ["**Psychogenic shock (fainting/syncope)**", "Temporary reflex "
                                                     "**vagal** slowing of the "
                                                     "heart and dilatation of "
                                                     "vessels \u2192 transient "
                                                     "reduction of blood to the "
                                                     "brain",
          "Fear, pain, sight of blood, bad news, prolonged standing, hot crowded "
          "rooms, hunger"]],
        weights=[3.0, 4.0, 5.6], size=8.6)
    b.h3("Primary and secondary shock")
    b.table(
        ["Primary (neurogenic/psychogenic) shock", "Secondary (true) shock"],
        [["Occurs **immediately** at the time of injury or fright.",
          "Develops **gradually, minutes to hours** after the injury."],
         ["Due to a **nervous reflex** \u2014 pain, fear, sight of blood.",
          "Due to **actual loss of blood or fluid**, or to toxins."],
         ["Usually **mild and temporary** \u2014 fainting; recovers when the "
          "casualty lies down.",
          "**Progressive and dangerous** \u2014 needs urgent treatment and "
          "often surgery/transfusion."],
         ["Skin is pale and moist, pulse slow then normal.",
          "Skin cold and clammy, pulse **rapid and thready**, BP falling."]],
        weights=[6.4, 6.4], first_bold=False)
    b.box("CAUSES OF SHOCK \u2014 QUICK LIST FOR REVISION", [
        "**Loss of body fluid** \u2014 haemorrhage, burns, vomiting, diarrhoea, "
        "excessive sweating, crush injury.",
        "**Heart conditions** \u2014 heart attack, heart failure, arrhythmia.",
        "**Severe pain and fear**; extensive injury, multiple fractures.",
        "**Infection and poisoning**; **allergy (anaphylaxis)**.",
        "**Spinal or severe head injury**; **electric shock**; heat stroke; "
        "hypoglycaemia; abdominal emergencies.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Stages of Shock")
    b.table(
        ["Stage", "What happens", "Clinical picture"],
        [["**1. Compensated (initial / non-progressive)**",
          "Adrenaline maintains blood pressure by a faster heart rate and "
          "constricted skin vessels",
          "Casualty is **alert or anxious**, skin pale and cool, pulse fast, "
          "**blood pressure still normal**, thirst; urine output falling"],
         ["**2. Decompensated (progressive)**",
          "Compensation fails; blood pressure falls; vital organs become starved "
          "of oxygen",
          "**Restless, confused, drowsy**; skin cold, clammy, grey-blue; pulse "
          "**very rapid and weak**; **BP low**; breathing rapid and shallow "
          "(air hunger); very little urine"],
         ["**3. Irreversible (refractory)**",
          "Cell and organ death; heart and brain damage cannot be reversed even "
          "if the cause is treated",
          "**Unconscious**, pulse and BP unrecordable, breathing irregular "
          "\u2192 **cardiac arrest and death**"]],
        weights=[3.0, 4.6, 5.0])

    # ------------------------------------------------------------------
    b.h2("Signs and Symptoms of Shock")
    b.table(
        ["System", "Signs and symptoms"],
        [["**Skin**", "**Pale (pallor), cold, clammy skin with sweating**; "
                      "blue-grey (cyanosed) lips, ears and nail beds; "
                      "**capillary refill more than 2 seconds**"],
         ["**Pulse**", "**Rapid, weak and thready**; later slow, irregular and "
                       "finally imperceptible at the wrist"],
         ["**Breathing**", "**Rapid, shallow, sighing or gasping (\u2018air "
                           "hunger\u2019)**; yawning"],
         ["**Blood pressure**", "**Falling** \u2014 systolic below 90 mm Hg is a "
                                "danger sign"],
         ["**Brain / behaviour**", "Giddiness and faintness, **restlessness and "
                                   "anxiety**, \u2018feeling of impending "
                                   "doom\u2019, confusion, dimness of vision, "
                                   "noises in the ears, drowsiness \u2192 "
                                   "**unconsciousness**"],
         ["**Digestive**", "**Intense thirst**, nausea and vomiting"],
         ["**Eyes**", "Sunken, dull eyes with dark rings; **dilated pupils**"],
         ["**Kidneys**", "**Reduced or absent urine output** (< 30 ml/hour)"],
         ["**Temperature**", "Subnormal; the casualty **feels cold and may "
                             "shiver**"]],
        weights=[2.8, 9.8])
    b.box("MNEMONIC FOR THE SIGNS OF SHOCK \u2014 \u2018COLD AND CLAMMY\u2019",
          [
        "**C** \u2013 **C**old, clammy, pale skin",
        "**O** \u2013 **O**liguria (little urine)",
        "**L** \u2013 **L**ow blood pressure",
        "**D** \u2013 **D**izziness, drowsiness, dimness of vision",
        "**A** \u2013 **A**nxiety and restlessness",
        "**N** \u2013 **N**ausea and vomiting",
        "**D** \u2013 **D**ry mouth and intense **thirst**",
        "**Plus:** rapid weak pulse and rapid shallow breathing \u2014 the two "
        "most reliable early signs.",
    ], kind="mnemonic")

    # ------------------------------------------------------------------
    b.h2("First-Aid Management of Shock")
    b.p("The golden rule is: ==treat the cause, and treat the casualty at the "
        "same time==. Shock cannot be reversed at the scene unless the cause "
        "(usually bleeding) is controlled.")
    b.numbered([
        "**Treat the cause** \u2014 stop bleeding, cool burns, relieve pain, "
        "give the adrenaline auto-injector in anaphylaxis, treat the heart "
        "attack, immobilise fractures.",
        "**Lay the casualty down** on a blanket, with the **head low and turned "
        "to one side** (to prevent inhalation of vomit).",
        "**Raise the legs 20\u201330 cm (8\u201312 inches)** \u2014 the "
        "\u2018shock position\u2019 \u2014 so that blood drains towards the "
        "heart and brain. **Do not raise the legs** if there is a fracture of "
        "the leg, a head, chest or abdominal injury, or a suspected spinal "
        "injury.",
        "**Loosen tight clothing** at the neck, chest and waist.",
        "**Keep the casualty warm** \u2014 cover with a blanket or coat, over "
        "and under him. **Do NOT use hot-water bottles, heaters, massage or a "
        "fire** \u2014 direct heat brings blood to the skin and away from the "
        "vital organs.",
        "**Reassure constantly** \u2014 a calm confident manner reduces fear, "
        "pain and the adrenaline response.",
        "**Give NOTHING by mouth** \u2014 no water, tea, food, medicine or "
        "alcohol (the casualty may need an anaesthetic, may vomit and inhale, or "
        "may have an abdominal injury). If very thirsty, **moisten the lips** "
        "with a wet cloth. *Exception:* in **burns** or where transport will be "
        "very long, small sips of **water/ORS** may be allowed to a fully "
        "conscious casualty.",
        "**Do not allow the casualty to move, sit up, smoke or walk.**",
        "**Monitor and record** breathing, pulse and level of response every "
        "**10 minutes** (5 minutes if severe).",
        "**Arrange urgent transport** to hospital, in the lying position, "
        "without jolting, and stay with the casualty. Be ready to start **CPR**.",
    ])
    b.box("SHOCK \u2014 DO'S AND DON'TS AT A GLANCE", [
        "**DO** lay flat, raise the legs, keep warm, reassure, give oxygen if "
        "trained, and treat the cause.",
        "**DON'T** give anything by mouth; **DON'T** apply direct heat; "
        "**DON'T** let the casualty sit up or move; **DON'T** leave the casualty "
        "alone.",
        "**DON'T** give alcohol (it dilates vessels and worsens shock) or any "
        "sedative/painkiller on your own.",
        "**DON'T** raise the legs in a head, chest, abdominal, spinal or leg "
        "injury \u2014 keep the casualty flat instead.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Anaphylactic Shock (Anaphylaxis)")
    b.p("A **severe, sudden and potentially fatal allergic reaction** affecting "
        "the whole body, usually within **seconds to 30 minutes** of exposure. "
        "It is a **medical emergency** \u2014 death may occur in minutes from "
        "airway swelling or circulatory collapse.")
    b.table(
        ["Common triggers", "Signs and symptoms"],
        [["**Insect stings** \u2014 bee, wasp, hornet, ant",
          "**Airway:** swelling of the lips, tongue, throat and face; hoarseness; "
          "**difficulty in breathing and swallowing**; wheeze and stridor"],
         ["**Drugs** \u2014 penicillin and other antibiotics, aspirin, NSAIDs, "
          "anaesthetics, vaccines, X-ray contrast dyes",
          "**Skin:** widespread red blotchy rash, **hives (urticaria)**, "
          "itching, flushing, swelling around the eyes"],
         ["**Foods** \u2014 peanuts and tree nuts, egg, milk, fish, shellfish, "
          "soy, wheat, sesame",
          "**Circulation:** **rapid weak pulse, falling blood pressure**, pallor, "
          "collapse, unconsciousness"],
         ["**Others** \u2014 latex, pollen, exercise, cold, idiopathic",
          "**Gut:** nausea, vomiting, abdominal cramps, diarrhoea; also anxiety "
          "and a feeling of impending doom"]],
        weights=[5.4, 7.4], first_bold=False)
    b.numbered([
        "**Remove the trigger** if possible (scrape out a bee sting, stop the "
        "drug/food).",
        "**Call an ambulance immediately** \u2014 say the word "
        "\u2018anaphylaxis\u2019.",
        "**Give adrenaline (epinephrine) without delay** using the casualty's "
        "**auto-injector (EpiPen)** into the **outer middle third of the thigh**, "
        "through clothing if necessary, holding it in place for about 3 seconds "
        "(new devices) to 10 seconds (older devices). Adult dose **0.3\u20130.5 "
        "mg (1:1000)**; child **0.15 mg**. A **second dose may be given after "
        "5\u201315 minutes** if there is no improvement.",
        "**Position:** if breathing is the main problem, let the casualty **sit "
        "up**; if he feels faint or is shocked, **lay him flat with the legs "
        "raised**; if unconscious and breathing, use the **recovery position**. "
        "**Never let an anaphylactic casualty stand or walk suddenly.**",
        "**Loosen tight clothing**; help with the casualty's own inhaler if he is "
        "asthmatic; give **nothing by mouth**.",
        "**Monitor** continuously and be ready to begin **CPR** \u2014 cardiac "
        "arrest can follow within minutes.",
        "**Every casualty must go to hospital** even if he recovers, because the "
        "reaction can **return after a few hours (biphasic reaction)**.",
    ])
    b.box("WHY ADRENALINE?", [
        "It **constricts blood vessels** (raises blood pressure), **relaxes the "
        "air passages** (relieves wheeze) and **reduces swelling** \u2014 "
        "reversing all the dangerous effects at once.",
        "It is the **drug of choice** and must be given **early**; "
        "antihistamines and steroids are secondary and act too slowly.",
        "Route for anaphylaxis = **intramuscular, in the outer thigh** "
        "(not intravenous by a first aider).",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Points Special to Other Types of Shock")
    b.table(
        ["Type", "Additional first-aid points"],
        [["**Haemorrhagic / hypovolaemic**", "Control bleeding **first** \u2014 "
                                            "nothing else works until the "
                                            "bleeding stops; immobilise "
                                            "fractures; keep flat with legs "
                                            "raised"],
         ["**Burn shock**", "Cool the burn, cover it, and give small sips of "
                            "water or **ORS** if fully conscious; expect shock "
                            "in any burn over 15 %"],
         ["**Cardiogenic (heart attack)**", "**Half-sitting position** (not flat, "
                                            "as breathing is difficult), "
                                            "absolute rest, loosen clothing, "
                                            "reassure; give **one dispersible "
                                            "aspirin 300 mg to chew** if the "
                                            "casualty is conscious and not "
                                            "allergic; help with his own "
                                            "nitroglycerine spray/tablet; be "
                                            "ready for CPR"],
         ["**Neurogenic / spinal**", "**Do not move** the casualty; support the "
                                     "head and neck in line with the body; keep "
                                     "flat; keep warm"],
         ["**Septic**", "Suspect when shock follows infection, a wound, an "
                        "abortion or burns with **fever or a very low "
                        "temperature**; urgent hospital transfer \u2014 "
                        "antibiotics are needed"],
         ["**Psychogenic (fainting)**", "Lay the casualty down and **raise the "
                                        "legs**; fresh air; loosen clothing; "
                                        "recovery is usually within a few "
                                        "minutes; sips of water only after full "
                                        "recovery"]],
        weights=[3.0, 9.6])

    # ------------------------------------------------------------------
    b.h2("Shock versus Fainting \u2014 the Classical Difference")
    b.table(
        ["Point", "Fainting (syncope)", "Shock (true/secondary)"],
        [["Cause", "Temporary reduction of blood flow to the brain \u2014 fear, "
                   "pain, standing long, heat, hunger, sight of blood",
          "Actual failure of circulation \u2014 bleeding, fluid loss, heart "
          "failure, allergy, infection"],
         ["Onset", "**Sudden**, often with warning (giddiness, nausea, "
                   "blurring)", "**Gradual and progressive**, often after injury"],
         ["Duration", "**Brief** \u2014 a few seconds to 2 minutes",
          "Prolonged; worsens unless treated"],
         ["Pulse", "**Slow and weak** at first, then normal",
          "**Rapid, weak and thready**, getting worse"],
         ["Skin", "Pale, cool, moist \u2014 but recovers colour quickly",
          "**Pale, cold, clammy** and **stays** so"],
         ["Blood pressure", "Falls briefly, then returns to normal",
          "**Progressively falls**"],
         ["Consciousness", "Brief complete loss, then **rapid full recovery**",
          "Restless \u2192 confused \u2192 drowsy \u2192 unconscious"],
         ["Response to lying down with legs raised",
          "**Recovers quickly and completely**",
          "Little or no improvement \u2014 needs hospital treatment"],
         ["Danger", "Usually harmless (danger is from the fall)",
          "**Life-threatening**"]],
        weights=[2.4, 5.0, 5.2])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Shock = **acute failure of circulation** with inadequate oxygen supply "
        "to the tissues; the commonest type is **hypovolaemic**.",
        "Types: **hypovolaemic, cardiogenic, neurogenic, anaphylactic, septic, "
        "obstructive, psychogenic**.",
        "Cardinal signs: **pale, cold, clammy skin + rapid weak thready pulse + "
        "rapid shallow breathing + thirst + restlessness + falling BP**.",
        "Position of a shocked casualty = **flat, head low and turned to one "
        "side, legs raised 20\u201330 cm**.",
        "**Keep warm with a blanket \u2014 never with direct heat**; "
        "**nothing by mouth**; never give alcohol.",
        "Monitor pulse, breathing and response every **10 minutes**; treat the "
        "cause first.",
        "**Anaphylaxis** \u2192 **adrenaline 0.5 mg IM in the outer thigh** at "
        "once, call the ambulance, sit up if breathless / lie flat if faint, "
        "hospital even after recovery.",
        "**Heart attack (cardiogenic shock)** \u2192 half-sitting, rest, "
        "**300 mg aspirin chewed**, ready for CPR.",
        "**Fainting** recovers within minutes on lying down; **true shock does "
        "not** \u2014 that is the examination difference.",
    ])
