# -*- coding: utf-8 -*-
"""Chapter 12 - Unconsciousness and Fainting."""


def render(b):
    b.part("PART V", "Medical Emergencies and Poisoning")
    b.chapter(
        "Unconsciousness and Fainting",
        "Levels of consciousness, the AVPU scale and Glasgow Coma Scale, all "
        "causes of unconsciousness, general care of the unconscious casualty, "
        "fainting, head injury, stroke, diabetic emergencies and heart attack.",
        syllabus=[
            "Unconsciousness \u2014 definition, degrees/levels, causes, signs "
            "and symptoms, general first-aid management, monitoring and "
            "transport.",
            "Fainting \u2014 causes, warning signs, treatment and prevention; "
            "recovery position; special causes of unconsciousness \u2014 head "
            "injury (concussion and compression), stroke, diabetic coma and "
            "hypoglycaemia, heart attack and infantile convulsions.",
        ])

    # ------------------------------------------------------------------
    b.h2("Consciousness and Unconsciousness")
    b.box("DEFINITIONS", [
        "**Consciousness** is the state of being **awake and aware of oneself "
        "and one's surroundings**, and of responding normally to stimuli. It "
        "depends on an intact **brain (cerebrum + brain stem)** receiving a "
        "constant supply of **oxygen and glucose**.",
        "**Unconsciousness** is a condition in which the casualty is "
        "**insensible \u2014 unaware of himself and of his surroundings \u2014 "
        "and does not respond to stimuli such as speech, touch or pain**, "
        "because of interruption of normal brain activity.",
        "**Coma** is deep, prolonged unconsciousness from which the casualty "
        "cannot be roused.",
        "**Why it is dangerous:** the unconscious casualty **loses the cough and "
        "swallowing reflexes and muscle tone**, so the **tongue falls back** and "
        "blocks the airway, and vomit or blood may be inhaled. "
        "==Unconsciousness itself can kill through the airway== \u2014 which is "
        "why airway care always comes first.",
    ], kind="def")

    # ------------------------------------------------------------------
    b.h2("Levels (Degrees) of Consciousness")
    b.table(
        ["Level", "Description"],
        [["**Fully conscious (alert)**", "Awake, aware, oriented in time, place "
                                        "and person; answers questions "
                                        "correctly"],
         ["**Confused / disoriented**", "Awake but muddled, cannot answer "
                                        "correctly, restless"],
         ["**Drowsy (somnolent)**", "Sleepy but can be roused by speech, and "
                                    "then answers slowly"],
         ["**Stupor**", "Roused only by **painful** stimuli; responds by "
                        "groaning or withdrawing"],
         ["**Coma (unconscious)**", "Cannot be roused at all; no response to "
                                    "voice or pain; reflexes are lost"]],
        weights=[3.2, 9.4])
    b.h3("The AVPU scale \u2014 the first aider's quick check")
    b.table(
        ["Letter", "Meaning", "How tested"],
        [["**A**", "**Alert**", "Eyes open spontaneously; talks normally"],
         ["**V**", "Responds to **Voice**", "Opens the eyes or moves when spoken "
                                            "to loudly"],
         ["**P**", "Responds to **Pain**", "Moves or groans only when pinched on "
                                           "the ear lobe/shoulder or when the "
                                           "nail bed is pressed"],
         ["**U**", "**Unresponsive**", "No response of any kind \u2014 a true "
                                       "coma"]],
        weights=[1.2, 3.2, 8.2])
    b.h3("The Glasgow Coma Scale (GCS) \u2014 for reference")
    b.table(
        ["Eye opening (E) \u2014 4", "Verbal response (V) \u2014 5",
         "Motor response (M) \u2014 6"],
        [["4 Spontaneous", "5 Oriented", "6 Obeys commands"],
         ["3 To speech", "4 Confused conversation", "5 Localises pain"],
         ["2 To pain", "3 Inappropriate words", "4 Withdraws from pain"],
         ["1 No eye opening", "2 Incomprehensible sounds", "3 Abnormal flexion"],
         ["", "1 No verbal response", "2 Abnormal extension"],
         ["", "", "1 No motor response"]],
        weights=[4.2, 4.4, 4.2], first_bold=False)
    b.bullets([
        "**Total = 3 (worst) to 15 (normal).** GCS **13\u201315** = mild, "
        "**9\u201312** = moderate, **8 or less = severe head injury/coma** "
        "(such a casualty cannot protect his own airway).",
        "A **falling level of response** is the most important single sign of a "
        "worsening head injury \u2014 record it with the **time** every 10 "
        "minutes.",
    ])

    # ------------------------------------------------------------------
    b.h2("Causes of Unconsciousness")
    b.box("MNEMONIC 1 \u2014 \u2018FISH SHAPED\u2019 (St John Ambulance)", [
        "**F** \u2013 **F**ainting",
        "**I** \u2013 **I**nfantile convulsions",
        "**S** \u2013 **S**hock",
        "**H** \u2013 **H**ead injury",
        "**S** \u2013 **S**troke (cerebro-vascular accident)",
        "**H** \u2013 **H**eart attack",
        "**A** \u2013 **A**sphyxia",
        "**P** \u2013 **P**oisoning (including alcohol and drugs)",
        "**E** \u2013 **E**pilepsy",
        "**D** \u2013 **D**iabetes (hypoglycaemia or diabetic coma)",
    ], kind="mnemonic")
    b.box("MNEMONIC 2 \u2014 \u2018AEIOU-TIPS\u2019 (medical practice)", [
        "**A** \u2013 **A**lcohol and drug intoxication",
        "**E** \u2013 **E**pilepsy, **E**lectrolyte disorder, **E**ncephalopathy",
        "**I** \u2013 **I**nsulin (hypoglycaemia) and diabetic coma",
        "**O** \u2013 **O**pium/**O**verdose of drugs, **O**xygen lack",
        "**U** \u2013 **U**raemia (kidney failure) and other metabolic causes",
        "**T** \u2013 **T**rauma (head injury), **T**umour, **T**emperature "
        "(heat stroke, hypothermia)",
        "**I** \u2013 **I**nfection (meningitis, malaria, encephalitis, "
        "septicaemia)",
        "**P** \u2013 **P**oisoning, **P**sychiatric (hysteria)",
        "**S** \u2013 **S**troke, **S**hock, **S**yncope, **S**eizure",
    ], kind="mnemonic")

    # ------------------------------------------------------------------
    b.h2("General Management of an Unconscious Casualty")
    b.p("Whatever the cause, the **treatment of unconsciousness is the same**. "
        "The priority is the **airway**.")
    b.numbered([
        "**Check for danger**, then check the **response** (shake and shout, "
        "AVPU).",
        "**Shout for help; ask a bystander to dial 112/108.**",
        "**Open the airway** \u2014 head tilt and chin lift (jaw thrust if a "
        "spinal injury is suspected); **clear the mouth** of vomit, blood, "
        "loose dentures or food.",
        "**Check breathing** for up to **10 seconds**. If absent or abnormal "
        "\u2192 **start CPR**. If present \u2192 go on.",
        "**Control any severe bleeding** and treat obvious serious injuries.",
        "**Place the casualty in the recovery position** (unless a spinal injury "
        "is suspected, when the head is held in line and the casualty is "
        "log-rolled only with helpers).",
        "**Loosen tight clothing** at the neck, chest and waist; remove "
        "spectacles and dentures.",
        "**Keep the casualty warm** with a blanket over and under him, and "
        "protect him from the sun and rain.",
        "==Give NOTHING by mouth== \u2014 no water, no food, no tablets; the "
        "casualty cannot swallow and will choke.",
        "**Do not leave the casualty alone**; do not attempt to rouse him by "
        "slapping, shaking, shouting, or throwing water on the face; do not give "
        "smelling salts to an unconscious casualty.",
        "**Look for clues to the cause** \u2014 medical bracelet or card "
        "(diabetes, epilepsy, allergy), medicines or an inhaler in the pocket, "
        "needle marks, smell of the breath (alcohol, acetone, kerosene, "
        "insecticide), injuries, pupil size, and the story of bystanders. Keep "
        "any container, tablet strip or vomit for the doctor.",
        "**Monitor and record every 10 minutes** \u2014 level of response "
        "(AVPU), breathing rate, pulse rate, pupils, colour and temperature; "
        "note the **time** of every change.",
        "**Arrange urgent transport** to hospital in the recovery position, on a "
        "stretcher, and hand over a written report.",
    ])
    b.box("THE FOUR \u2018NEVERS\u2019 OF UNCONSCIOUSNESS", [
        "**Never** give anything by mouth.",
        "**Never** leave the casualty lying on his back, unattended.",
        "**Never** try to wake him up forcibly, and never put a pillow under the "
        "head (it bends the neck and blocks the airway).",
        "**Never** assume alcohol is the cause \u2014 a \u2018drunk\u2019 may in "
        "fact have a head injury, hypoglycaemia or a stroke.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Fainting (Syncope)")
    b.box("DEFINITION", [
        "**Fainting** is a **brief and temporary loss of consciousness caused by "
        "a momentary reduction of the blood supply to the brain**, from which "
        "the casualty recovers quickly and completely when he lies down.",
        "Mechanism: a **reflex (vagal) slowing of the heart with dilatation of "
        "the blood vessels**, so that blood pools in the legs and abdomen and "
        "the brain is briefly starved of oxygen \u2014 also called "
        "**psychogenic, primary or neurogenic shock**.",
    ], kind="def")
    b.h3("Causes of fainting")
    b.bullets([
        "**Emotional** \u2014 fear, fright, anxiety, bad news, the **sight of "
        "blood or of an injection**, severe pain.",
        "**Postural** \u2014 **standing still for a long time** (parades, "
        "queues, guard duty), or **standing up suddenly** after lying or "
        "sitting long (postural hypotension), especially in the elderly.",
        "**Environmental** \u2014 a **hot, crowded, ill-ventilated room**, "
        "prolonged sun exposure.",
        "**Physical** \u2014 **hunger, fatigue, exhaustion, dehydration, "
        "sleeplessness, low blood pressure, anaemia**, after an illness or a hot "
        "bath, straining at stool, severe coughing, pregnancy.",
        "**Medical** \u2014 heart disease and irregular rhythms, blood loss, "
        "hypoglycaemia, some medicines (for blood pressure), and after taking "
        "alcohol.",
    ])
    b.h3("Signs and symptoms")
    b.table(
        ["Warning (premonitory) symptoms", "Signs during the faint"],
        [["Giddiness and light-headedness; \u2018everything going black\u2019",
          "**Pale, cold, moist (clammy) skin**; sweating"],
         ["Blurring or dimness of vision, spots before the eyes",
          "**Slow, weak pulse** (this is characteristic \u2014 compare with the "
          "rapid pulse of true shock)"],
         ["Ringing in the ears, nausea, yawning",
          "Shallow breathing; brief loss of consciousness (seconds to about "
          "2 minutes)"],
         ["Weakness of the legs, a feeling of falling",
          "The casualty **falls to the ground** \u2014 the fall itself may cause "
          "injury; there may be a few twitches"],
         ["Sweating, feeling hot then cold",
          "**Rapid, complete recovery once flat**, with no confusion afterwards"]],
        weights=[6.2, 6.6], first_bold=False)
    b.h3("First aid for fainting")
    b.numbered([
        "**If the casualty feels faint** (still conscious): make him **sit or "
        "lie down at once** and **raise the legs above the level of the heart** "
        "(20\u201330 cm), or sit him with the **head bent forward between the "
        "knees**.",
        "**If the casualty has fainted**: lay him flat on his back, **raise and "
        "support the legs**.",
        "**Ensure plenty of fresh air** \u2014 open windows and doors, ask "
        "onlookers to move back, fan the casualty.",
        "**Loosen tight clothing** at the neck, chest and waist.",
        "**Check breathing**; if it is absent or abnormal, treat as cardiac "
        "arrest and start CPR. If the casualty does not regain consciousness "
        "within **1\u20132 minutes**, treat him as an **unconscious casualty** "
        "\u2014 recovery position and call an ambulance.",
        "**On recovery**, reassure him, help him to sit up **gradually**, and "
        "give **sips of cool water** (sweet drinks if he is hungry or diabetic). "
        "Do not let him stand up suddenly or walk away at once.",
        "Look for and treat any **injury caused by the fall**, and find out the "
        "cause.",
        "**Refer to a doctor** if the faint was prolonged, if there were "
        "convulsions, if it happened while lying down or during exercise, if "
        "there was chest pain or palpitation, if the casualty is elderly or "
        "pregnant, or if fainting is recurrent \u2014 these suggest a heart or "
        "brain cause.",
    ])
    b.box("PREVENTION OF FAINTING \u2014 AND WHAT NOT TO DO", [
        "**Do not** crowd round the casualty, do not raise the head, do not "
        "make him sit or stand, and **do not throw water on the face** or slap "
        "him.",
        "**Do not** give anything by mouth while he is unconscious.",
        "Prevention: avoid standing still for long (flex the calf muscles and "
        "shift weight), get up slowly, eat and drink regularly, avoid hot "
        "crowded places, sit down at the first warning sign.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Head Injury \u2014 Concussion and Compression")
    b.table(
        ["Point", "Concussion (cerebral concussion)",
         "Compression (cerebral compression)"],
        [["Nature", "**\u2018Shaking up\u2019 of the brain** \u2014 a temporary "
                    "and **reversible** disturbance of brain function",
          "**Pressure on the brain** from bleeding, a depressed fracture, "
          "swelling or a tumour \u2014 **serious and progressive**"],
         ["Onset", "**Immediately** after the blow",
          "May develop **minutes, hours or even days after** the injury "
          "(after a lucid interval)"],
         ["Consciousness", "**Brief loss** (seconds to a few minutes) with "
                           "**complete recovery**",
          "**Deteriorating** level of response \u2014 drowsy \u2192 confused "
          "\u2192 unconscious"],
         ["Pupils", "Equal and reacting", "**Unequal \u2014 one pupil dilated "
                                          "and not reacting** to light"],
         ["Pulse", "Rapid and weak at first, becoming normal",
          "**Slow and full/bounding**"],
         ["Breathing", "Shallow", "**Noisy, snoring, slow and irregular**"],
         ["Face and skin", "Pale, cold, clammy",
          "**Flushed, hot, dry**; temperature rises"],
         ["Other features", "Giddiness, nausea, vomiting, headache, **loss of "
                            "memory of the event (amnesia)**, mild confusion "
                            "\u2014 the casualty may say \u2018what "
                            "happened?\u2019 repeatedly",
          "**Severe headache, vomiting, fits, weakness or paralysis on one "
          "side, rising blood pressure**"],
         ["Outcome", "Usually recovers fully, but **must be watched for 24 "
                     "hours** and taken to hospital if any warning sign appears",
          "**A surgical emergency** \u2014 needs immediate hospital treatment"]],
        weights=[2.0, 5.2, 5.6], size=8.8)
    b.h3("First aid in head injury")
    b.numbered([
        "Assume that **every casualty with a head injury may also have a neck "
        "(cervical spine) injury** \u2014 support the head in line with the body "
        "and do not move him unnecessarily.",
        "Maintain the **airway and breathing**; place an unconscious but "
        "breathing casualty in the **recovery position** with support to the head "
        "and neck; be ready for CPR.",
        "**Control scalp bleeding** with direct pressure over a dressing "
        "(use a **ring pad** if a depressed fracture is suspected).",
        "**Never plug the ear or nose** if blood or clear fluid escapes; cover "
        "lightly and let it drain, with the affected ear **downwards**.",
        "**Give nothing by mouth**; do not give aspirin (it increases bleeding).",
        "**Record the level of response (AVPU/GCS), pupils, pulse and breathing "
        "every 10 minutes** with the time \u2014 this record is invaluable to "
        "the doctor.",
        "Arrange **urgent hospital transfer** for anyone who has been "
        "unconscious, has vomited more than once, has a severe headache, fits, "
        "weakness, unequal pupils, bleeding from the ear/nose, a wound of the "
        "scalp, or who is on blood-thinning medicine, elderly or intoxicated.",
        "Advise a casualty with even a minor head injury to be **observed for "
        "24\u201348 hours** and to return at once if headache, vomiting, "
        "drowsiness, double vision or confusion develops.",
    ])

    # ------------------------------------------------------------------
    b.h2("Stroke (Cerebro-Vascular Accident)")
    b.bullets([
        "**Stroke** = sudden interruption of the blood supply to a part of the "
        "brain, either by a **clot (ischaemic \u2014 about 80 %)** or by "
        "**bleeding (haemorrhagic \u2014 about 20 %)**. A **TIA (transient "
        "ischaemic attack, \u2018mini-stroke\u2019)** produces the same signs, "
        "which clear within 24 hours \u2014 but it is a serious warning.",
        "Risk factors: **high blood pressure (the most important)**, diabetes, "
        "smoking, high cholesterol, heart disease, obesity, alcohol, age, "
        "family history.",
    ])
    b.box("RECOGNITION \u2014 THE \u2018F-A-S-T\u2019 TEST", [
        "**F \u2013 Face**: has the face **fallen on one side**? Can the casualty "
        "smile? Is the mouth or eye drooping?",
        "**A \u2013 Arms**: can he **raise both arms** and keep them up?",
        "**S \u2013 Speech**: is his speech **slurred or muddled**? Can he "
        "understand you?",
        "**T \u2013 Time**: **Time to call 112/108 at once** \u2014 note the "
        "**time when the symptoms began** (clot-dissolving treatment works "
        "only within about 4\u00bd hours).",
        "Other signs: sudden **weakness or numbness of one side**, loss of "
        "vision, severe sudden headache ('the worst headache of my life'), "
        "giddiness, loss of balance, confusion, dribbling, loss of bladder "
        "control, unequal pupils, unconsciousness.",
    ], kind="exam")
    b.numbered([
        "**Call an ambulance immediately** and say that you suspect a stroke.",
        "If conscious: lay the casualty down with the **head and shoulders "
        "slightly raised and supported**, head turned to the side; loosen "
        "clothing; reassure him \u2014 he may understand everything even if he "
        "cannot speak.",
        "If unconscious but breathing: **recovery position, paralysed side "
        "uppermost**.",
        "**Nothing by mouth** \u2014 not even water or medicine (swallowing is "
        "unsafe).",
        "Wipe away dribbling; keep the airway clear; monitor every 10 minutes; "
        "be ready for CPR.",
        "**Do not** give aspirin (unlike a heart attack) \u2014 the stroke may "
        "be haemorrhagic.",
    ])

    # ------------------------------------------------------------------
    b.h2("Diabetic Emergencies")
    b.table(
        ["Point", "Hypoglycaemia (low blood sugar) \u2014 the true emergency",
         "Hyperglycaemia / diabetic ketoacidosis (high blood sugar)"],
        [["Cause", "**Too much insulin**, missed meal, unaccustomed exercise, "
                   "alcohol, vomiting",
          "**Too little insulin**, infection, over-eating, undiagnosed diabetes"],
         ["Onset", "**Sudden \u2014 minutes**", "**Gradual \u2014 hours to "
                                               "days**"],
         ["Skin", "**Pale, cold, profusely sweating**",
          "**Warm, dry, flushed**; dry tongue"],
         ["Breathing", "Normal or shallow, rapid",
          "**Deep, rapid, sighing (Kussmaul)** breathing with a "
          "**sweet acetone/nail-polish smell of the breath**"],
         ["Pulse", "Rapid, strong (\u2018bounding\u2019)",
          "Rapid and weak"],
         ["Behaviour", "**Confused, aggressive, trembling, behaving as if "
                       "drunk**, hungry, headache, blurred vision, fits, then "
                       "unconsciousness",
          "Extreme **thirst**, frequent passing of urine, nausea and vomiting, "
          "abdominal pain, weakness, drowsiness \u2192 coma"],
         ["First aid (conscious)", "**Give sugar at once** \u2014 3\u20134 "
                                   "teaspoons of sugar or glucose in water, a "
                                   "sweet drink, glucose gel, honey, 3\u20134 "
                                   "sweets or biscuits; repeat in 10\u201315 "
                                   "minutes if no improvement; then give a "
                                   "starchy snack. Improvement is usually "
                                   "dramatic",
          "**Do not give sugar.** Help the casualty take his own insulin if he "
          "is able, give sips of water, and **arrange hospital care urgently**"],
         ["First aid (unconscious)", "**Nothing by mouth** \u2014 recovery "
                                     "position, call an ambulance immediately "
                                     "(hospital gives IV glucose/glucagon)",
          "Recovery position, call an ambulance immediately"]],
        weights=[2.2, 5.4, 5.2], size=8.6)
    b.box("THE GOLDEN RULE OF DIABETIC EMERGENCIES", [
        "If you are **not sure** whether the blood sugar is high or low in a "
        "**conscious** casualty, **give sugar**: it will save a hypoglycaemic "
        "casualty within minutes and will do little harm to a hyperglycaemic one "
        "in the short term.",
        "**Hypoglycaemia is the greater and more immediate danger** \u2014 it can "
        "cause permanent brain damage within an hour.",
        "**Never** give anything by mouth to an unconscious diabetic, and never "
        "inject insulin yourself.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Heart Attack, Angina and Cardiac Emergencies")
    b.table(
        ["", "Angina pectoris", "Heart attack (myocardial infarction)"],
        [["Cause", "Temporary lack of blood to the heart muscle on exertion",
          "**Sudden blockage of a coronary artery** \u2014 part of the heart "
          "muscle dies"],
         ["Pain", "Central chest pain/tightness brought on by **exertion or "
                  "emotion**, relieved by **rest in a few minutes** and by the "
                  "casualty's own tablet/spray",
          "**Severe crushing, vice-like central chest pain, often at rest**, "
          "lasting more than 15\u201320 minutes and **not relieved by rest**"],
         ["Radiation", "May spread to the left arm, jaw or neck",
          "Spreads to the **left arm (or both arms), neck, jaw, back or upper "
          "abdomen**"],
         ["Other signs", "Breathlessness, anxiety",
          "**Ashen grey, cold clammy skin, profuse sweating, nausea and "
          "vomiting, breathlessness, giddiness, irregular pulse, a feeling of "
          "impending death**; may collapse suddenly with **cardiac arrest**"],
         ["First aid", "**Stop the activity and sit the casualty down**; help "
                       "him take his own nitroglycerine tablet/spray; if the "
                       "pain persists beyond 10\u201315 minutes treat it as a "
                       "heart attack",
          "**Call 112/108 at once**; sit the casualty in a **half-sitting "
          "(W-position) posture** with the knees bent and supported; loosen "
          "clothing; **give one 300 mg dispersible aspirin to chew slowly** "
          "(if conscious, not allergic, and over 16); help with his own "
          "nitroglycerine; keep him calm and still; **be ready to start CPR** "
          "and use an AED"]],
        weights=[1.8, 5.2, 5.8], size=8.6)
    b.bullets([
        "**Never** allow a casualty with chest pain to walk, drive or exert "
        "himself; **never** leave him alone.",
        "\u2018Silent\u2019 heart attacks with little or no pain occur in "
        "**diabetics, the elderly and women** \u2014 breathlessness, fainting or "
        "sudden sweating may be the only sign.",
        "**Cardiac arrest** (no response, no normal breathing) \u2192 immediate "
        "**CPR and AED** (Chapter 4).",
    ])

    # ------------------------------------------------------------------
    b.h2("Infantile (Febrile) Convulsions")
    b.bullets([
        "Occur in children of **6 months to 5\u20136 years** with a **rapidly "
        "rising fever** (from any infection).",
        "Signs: **violent twitching of the face and limbs, stiffness with "
        "arching of the back, clenched fists, holding of the breath with a red "
        "or blue face, rolled-up eyes, frothing at the mouth, hot flushed skin "
        "and sweating**; the child may pass urine.",
        "**First aid:** protect the child from injury (put soft padding around, "
        "never restrain); **do not put anything in the mouth**; remove clothing "
        "and bedding to **cool the child**; sponge with tepid (not cold) water; "
        "when the fit stops, place him in the **recovery position**; give "
        "**paracetamol** when he is fully awake and able to swallow; and "
        "**always seek medical advice**.",
        "**Call an ambulance** if the fit lasts more than 5 minutes, if fits "
        "recur, if the child does not regain consciousness, if it is his first "
        "fit, or if a rash or neck stiffness suggests **meningitis**.",
    ])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Unconsciousness = **insensibility with no response to stimuli**; the "
        "danger is the **airway** \u2014 the tongue falls back.",
        "Levels: alert \u2192 confused \u2192 drowsy \u2192 stupor \u2192 coma; "
        "quick scale **AVPU**; detailed scale **GCS (3\u201315; \u2264 8 = "
        "severe)**.",
        "Causes mnemonic = **FISH SHAPED** or **AEIOU-TIPS**.",
        "Management of every unconscious casualty: **airway \u2192 breathing "
        "\u2192 bleeding \u2192 recovery position \u2192 warmth \u2192 nothing "
        "by mouth \u2192 monitor every 10 minutes \u2192 hospital**.",
        "**Fainting** = brief loss of consciousness from reduced blood to the "
        "brain, with a **slow weak pulse**; lay flat and **raise the legs**; "
        "recovery in 1\u20132 minutes.",
        "**Concussion** = temporary, recovers, **equal pupils, rapid pulse**; "
        "**compression** = progressive, **unequal pupils, slow full pulse, "
        "noisy breathing** \u2014 a surgical emergency.",
        "**Stroke** \u2192 **FAST** test, note the time, nothing by mouth, "
        "**no aspirin**, recovery position with the paralysed side uppermost.",
        "**Hypoglycaemia** \u2014 sudden, pale, sweating, aggressive \u2192 "
        "**give sugar**; **hyperglycaemia** \u2014 gradual, dry, flushed, "
        "acetone breath, deep breathing \u2192 **hospital**.",
        "**Heart attack** \u2192 half-sitting, **300 mg aspirin chewed**, call "
        "112/108, ready for CPR; **angina** is relieved by rest and the "
        "casualty's own spray.",
        "**Febrile convulsion** \u2192 protect from injury, cool the child, "
        "nothing in the mouth, recovery position afterwards.",
    ])
