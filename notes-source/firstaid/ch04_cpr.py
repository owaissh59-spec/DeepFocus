# -*- coding: utf-8 -*-
"""Chapter 4 - Cardio-Pulmonary Resuscitation (CPR)."""


def render(b):
    b.chapter(
        "Cardio-Pulmonary Resuscitation (CPR)",
        "Basic Life Support: recognition of cardiac arrest, high-quality chest "
        "compressions, rescue breathing, the AED, CPR in children and infants, "
        "choking, the recovery position and special situations.",
        syllabus=[
            "Cardio-pulmonary resuscitation \u2014 meaning, indications, "
            "complete step-by-step technique in adults, children and infants; "
            "one- and two-rescuer CPR; compression-only CPR.",
            "Automated External Defibrillator, recovery position, choking "
            "(Heimlich manoeuvre), complications, when to start and when to stop, "
            "and CPR in special situations.",
        ])

    # ------------------------------------------------------------------
    b.h2("Meaning and Definitions")
    b.box("DEFINITIONS", [
        "**CPR (cardio-pulmonary resuscitation)** \u2014 an emergency "
        "life-saving procedure combining **chest compressions** (to circulate "
        "blood artificially) with **rescue breathing** (to oxygenate the blood), "
        "performed when the heart and breathing have stopped. "
        "*Cardio* = heart, *pulmonary* = lungs, *resuscitation* = revival.",
        "**Cardiac arrest** \u2014 sudden and complete cessation of effective "
        "pumping by the heart; the casualty is **unresponsive, not breathing "
        "normally and has no pulse**.",
        "**Respiratory arrest** \u2014 breathing has stopped but the heart is "
        "still beating (it will stop within minutes if untreated).",
        "**Basic Life Support (BLS)** \u2014 the whole set of skills that "
        "maintain airway, breathing and circulation without drugs or advanced "
        "equipment: recognition, calling for help, CPR and AED use.",
        "**Advanced Cardiac Life Support (ACLS)** \u2014 BLS plus drugs, "
        "advanced airways, manual defibrillation and monitoring, by trained "
        "medical teams.",
        "**Defibrillation** \u2014 delivery of a controlled electric shock to "
        "restore a normal heart rhythm in ventricular fibrillation.",
    ], kind="def")
    b.p("CPR does **not usually restart the heart by itself**; it keeps oxygenated "
        "blood flowing to the **brain and heart muscle** until a defibrillator "
        "and advanced care arrive. Good CPR provides only about **25\u201333 % "
        "of the normal cardiac output** \u2014 which is why it must be of "
        "high quality and started at once.")

    # ------------------------------------------------------------------
    b.h2("Causes and Recognition of Cardiac Arrest")
    b.table(
        ["Cardiac causes", "Non-cardiac causes"],
        [["**Heart attack (myocardial infarction)** \u2014 the commonest cause "
          "in adults", "**Asphyxia** \u2014 choking, drowning, strangulation, "
                       "smoke inhalation"],
         ["Ventricular fibrillation and other arrhythmias",
          "**Electrocution** and lightning strike"],
         ["Heart failure, cardiomyopathy, valve disease",
          "Severe **haemorrhage and shock**"],
         ["Blunt injury over the chest (commotio cordis)",
          "**Poisoning and drug overdose**"],
         ["Congenital heart disease (in the young)",
          "**Head injury**, stroke, severe **allergy (anaphylaxis)**, "
          "hypothermia, severe **hypoglycaemia**, electrolyte disturbance"]],
        weights=[6.2, 6.6], first_bold=False)
    b.bullets([
        "In **adults** cardiac arrest is usually **cardiac (a rhythm problem)** "
        "\u2014 therefore **compressions and early defibrillation** come first.",
        "In **children and infants** it is usually **respiratory (asphyxial)** "
        "\u2014 therefore **breaths matter as much as compressions**, and CPR "
        "begins with **5 rescue breaths** in the European/Indian sequence.",
    ])
    b.h3("Signs of cardiac arrest \u2014 how to recognise it in seconds")
    b.table(
        ["Sign", "How to check"],
        [["**Unresponsiveness**", "Shake the shoulders gently and shout "
                                  "\u2018Are you all right?\u2019 \u2014 no "
                                  "reply, no movement"],
         ["**Absent or abnormal breathing**", "Look for chest movement, listen "
                                              "and feel at the mouth for "
                                              "**not more than 10 seconds**. "
                                              "**Agonal gasping** (occasional "
                                              "noisy gasps) is *not* normal "
                                              "breathing \u2014 treat as "
                                              "cardiac arrest"],
         ["**Absent pulse**", "Carotid pulse in adults/children, brachial or "
                              "femoral in infants \u2014 checked only by "
                              "trained rescuers, for **\u2264 10 seconds**. "
                              "**Laypersons should not delay CPR to feel for a "
                              "pulse**"],
         ["Other signs", "Deathly pale or blue-grey (cyanosed) skin; **widely "
                         "dilated pupils** not reacting to light; no heart "
                         "sounds; sometimes a brief seizure at the onset"]],
        weights=[3.4, 9.2])

    # ------------------------------------------------------------------
    b.h2("The Chain of Survival and When to Start CPR")
    b.p("CPR is begun in **any** unresponsive casualty who is **not breathing "
        "normally**. Do not wait for a pulse check, and do not wait for the "
        "ambulance.")
    b.table(
        ["Start CPR when", "Do NOT start / stop CPR when"],
        [["Casualty is unresponsive **and** not breathing normally (or only "
          "gasping).", "There are **obvious signs of irreversible death** "
                       "\u2014 rigor mortis, decomposition, decapitation, "
                       "injuries incompatible with life, dependent lividity."],
         ["After a drowning, electrocution, choking, poisoning or lightning "
          "strike with no breathing.",
          "The casualty **starts to breathe normally, coughs or moves** "
          "\u2014 turn into the recovery position and monitor."],
         ["Cardiac arrest in a **hypothermic** casualty \u2014 continue for "
          "longer (\u2018nobody is dead until warm and dead\u2019).",
          "**Qualified help takes over**, or a valid \u2018do not resuscitate\u2019 "
          "order exists."],
         ["Cardiac arrest in pregnancy, in trauma, in a child \u2014 always.",
          "The **rescuer is exhausted** or the **scene becomes unsafe**."]],
        weights=[6.4, 6.4], first_bold=False)
    b.box("CRITICAL TIME FACTS", [
        "Chances of survival fall by **7\u201310 % for every minute** without "
        "CPR and defibrillation.",
        "**Brain damage** starts within **3\u20134 minutes** of arrest and is "
        "usually irreversible by **8\u201310 minutes**.",
        "Immediate bystander CPR **doubles to triples** survival.",
        "The target is **CPR within 4 minutes** and **defibrillation within 8 "
        "minutes** (ideally 3\u20135).",
        "Interruptions in compressions must be kept to **less than 10 seconds**; "
        "\u2018chest compression fraction\u2019 should exceed **60 %** of the "
        "time.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Adult CPR \u2014 Step-by-Step Procedure")
    b.p("The modern sequence is **C-A-B (Compressions \u2013 Airway \u2013 "
        "Breathing)**, adopted in 2010 in place of the older A-B-C, so that "
        "compressions are not delayed.")
    b.numbered([
        "**D \u2014 Danger.** Make sure it is safe for you (traffic, live wires, "
        "gas, water). Wear gloves if available.",
        "**R \u2014 Response.** Tap the shoulders and shout. If there is no "
        "response, the casualty is unconscious.",
        "**S \u2014 Shout / Send for help.** Shout for a bystander; get someone "
        "to **dial 112 / 108** and **fetch an AED**. If alone with a phone, put "
        "it on **speaker** and call while starting CPR. For an adult, "
        "**call first**; for a child or a drowning casualty, **give 1 minute of "
        "CPR first, then call** (\u2018phone fast\u2019).",
        "**Position the casualty** \u2014 flat on the **back on a firm, hard "
        "surface** (the floor, not a bed), arms by the side; kneel beside the "
        "chest. Loosen tight clothing and expose the chest.",
        "**Check breathing** \u2014 open the airway with **head tilt\u2013chin "
        "lift** and look, listen and feel for **\u2264 10 seconds**. Gasping = "
        "no breathing.",
        "**C \u2014 Start 30 chest compressions.** Place the **heel of one hand "
        "on the centre of the chest (lower half of the sternum)**, the other hand "
        "on top with fingers interlocked; keep **arms straight, elbows locked, "
        "shoulders directly above the hands**, and compress using the weight of "
        "your upper body from the hips.",
        "**A \u2014 Open the Airway** again by head tilt\u2013chin lift "
        "(jaw thrust if spinal injury is suspected); remove any visible "
        "obstruction, loose dentures or vomit.",
        "**B \u2014 Give 2 rescue breaths.** Pinch the nose, seal your mouth "
        "over the casualty's mouth (or use a pocket mask/face shield) and blow "
        "steadily for about **1 second** until the chest rises. Allow the chest "
        "to fall, then give the second breath. Each breath \u2248 500\u2013600 ml "
        "\u2014 just enough for a **visible chest rise**.",
        "**Continue cycles of 30 : 2** without interruption. Change rescuers "
        "**every 2 minutes (about 5 cycles)** to avoid fatigue, taking less than "
        "10 seconds to change over.",
        "**Attach the AED as soon as it arrives** and follow its voice prompts.",
        "**Continue until** the casualty breathes normally, qualified help takes "
        "over, or you are physically exhausted.",
    ])
    b.h3("The five components of high-quality CPR (the numbers to memorise)")
    b.table(
        ["Component", "Adult standard"],
        [["**Rate of compressions**", "**100\u2013120 per minute** "
                                      "(\u2248 2 per second)"],
         ["**Depth of compressions**", "**5\u20136 cm (2\u20132.4 inches)** "
                                       "\u2014 at least \u2153 of the chest "
                                       "depth"],
         ["**Compression : ventilation ratio**", "**30 : 2** (one or two "
                                                 "rescuers in an adult)"],
         ["**Recoil**", "Allow **complete chest recoil** after each compression; "
                        "do not lean on the chest"],
         ["**Interruptions**", "**Minimise** \u2014 no pause longer than "
                               "**10 seconds**"],
         ["Hand position", "Heel of the hand on the **lower half of the "
                           "sternum** (centre of the chest, between the nipples)"],
         ["Rescue breath volume/time", "Chest just rises; **1 second** per "
                                       "breath; avoid over-inflation"],
         ["Cycles per 2 minutes", "About **5 cycles** of 30 : 2"],
         ["Rescuer change", "Every **2 minutes**, in **< 10 seconds**"]],
        weights=[4.2, 8.4])
    b.box("COMMON MISTAKES THAT MAKE CPR USELESS", [
        "Compressing **too slowly, too shallowly** or in the **wrong place** "
        "(over the xiphoid or the ribs).",
        "**Leaning** on the chest so that it does not recoil \u2014 the heart "
        "cannot refill.",
        "**Bent elbows** \u2014 wastes energy and reduces depth.",
        "Long pauses for pulse checks, moving the casualty, or fumbling with the "
        "AED.",
        "**Over-ventilation** (too many, too forceful breaths) \u2014 causes "
        "stomach inflation, vomiting and raises pressure in the chest, reducing "
        "blood flow.",
        "CPR on a **soft surface (bed, sofa)** or with the casualty sitting.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Compression-Only (Hands-Only) CPR")
    b.bullets([
        "If a rescuer is **untrained, unwilling or unable to give rescue "
        "breaths**, he should give **continuous chest compressions at "
        "100\u2013120/min without pauses**.",
        "This is as effective as standard CPR in the **first few minutes** of an "
        "adult cardiac arrest witnessed by a bystander.",
        "Hands-only CPR is **not suitable** for: **children and infants**, "
        "**drowning**, **choking**, **drug overdose**, and arrests that are "
        "**not witnessed** \u2014 all of these are asphyxial and need breaths.",
        "Telephone-guided (dispatcher-assisted) CPR is recommended \u2014 the "
        "ambulance control room will guide a bystander.",
    ])

    # ------------------------------------------------------------------
    b.h2("CPR in Children and Infants")
    b.p("A **newborn** is up to 1 month, an **infant** under 1 year, a **child** "
        "from 1 year to puberty; from puberty onwards adult technique is used.")
    b.table(
        ["Point", "Adult", "Child (1 yr \u2013 puberty)", "Infant (< 1 yr)"],
        [["Hands used", "**Two hands** (heel of one, other on top)",
          "**One or two hands** (one hand is enough in a small child)",
          "**Two fingers** (one rescuer) or **two thumbs encircling** "
          "(two rescuers)"],
         ["Site", "Lower half of the sternum, centre of the chest",
          "Lower half of the sternum",
          "**Just below the nipple line**, on the lower sternum"],
         ["Depth", "**5\u20136 cm**", "**About 5 cm / \u2153 of chest depth**",
          "**About 4 cm / \u2153 of chest depth**"],
         ["Rate", "100\u2013120/min", "100\u2013120/min", "100\u2013120/min"],
         ["Ratio (single rescuer)", "**30 : 2**", "**30 : 2**", "**30 : 2**"],
         ["Ratio (two healthcare rescuers)", "30 : 2", "**15 : 2**",
          "**15 : 2**"],
         ["Initial breaths", "None (start compressions)",
          "**5 rescue breaths first** (ERC/Indian practice)",
          "**5 rescue breaths first**; puffs from the cheeks only"],
         ["Airway opening", "Head tilt + chin lift",
          "Head tilt + chin lift", "**Neutral position** \u2014 do **not** "
                                   "over-extend the neck"],
         ["Rescue breath technique", "Mouth-to-mouth, nose pinched",
          "Mouth-to-mouth", "**Mouth-to-mouth-and-nose** (cover both) or "
                            "mouth-to-nose"],
         ["Pulse check point", "**Carotid**", "Carotid or femoral",
          "**Brachial** (inner upper arm) or femoral"],
         ["When to call help if alone", "**Call first**, then CPR",
          "**CPR for 1 minute (5 cycles), then call**",
          "**CPR for 1 minute, then call**"],
         ["AED", "Adult pads and energy", "Paediatric pads/attenuator if "
                                          "available (1\u20138 yr)",
          "Manual defibrillator preferred; AED with paediatric pads if needed"]],
        weights=[2.5, 3.4, 3.5, 3.6], size=8.4)
    b.box("PAEDIATRIC POINTS THAT ARE ASKED", [
        "In children, cardiac arrest is usually due to **respiratory causes** "
        "\u2014 so open the airway and give **5 initial rescue breaths**.",
        "Compress with **two fingers** in an infant (single rescuer) and with "
        "the **two-thumb encircling technique** when two rescuers are present.",
        "Never use full adult force on a child; depth is **one-third of the "
        "chest** in both children and infants.",
        "**Newborn resuscitation** uses a ratio of **3 : 1** with a rate of "
        "120 events/min, and the **head is kept in a neutral position**.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("One-Rescuer versus Two-Rescuer CPR")
    b.table(
        ["Feature", "One rescuer", "Two rescuers"],
        [["Ratio (adult)", "30 : 2", "30 : 2"],
         ["Ratio (child/infant, healthcare providers)", "30 : 2", "**15 : 2**"],
         ["Roles", "Same rescuer compresses and ventilates",
          "One compresses, the other manages the airway and breaths and watches "
          "for chest rise"],
         ["Change over", "Rest is impossible \u2014 fatigue sets in within "
                         "1\u20132 minutes",
          "**Change every 2 minutes**, taking less than 10 seconds"],
         ["Advantage", "Can be started immediately by anyone",
          "Better quality, less fatigue, faster AED use and better monitoring"]],
        weights=[3.2, 4.4, 5.0])

    # ------------------------------------------------------------------
    b.h2("Rescue Breathing (Ventilation) Technique")
    b.bullets([
        "**Mouth-to-mouth** \u2014 the standard: head tilt\u2013chin lift, pinch "
        "the nose, wide seal over the mouth, blow for **1 second** watching the "
        "chest rise, release and let the chest fall.",
        "**Mouth-to-nose** \u2014 used when the mouth is injured, jaw is clenched "
        "(trismus), the mouth cannot be sealed, or in rescue from water.",
        "**Mouth-to-mouth-and-nose** \u2014 in **infants**.",
        "**Mouth-to-stoma** \u2014 in a casualty with a tracheostomy/laryngectomy "
        "opening in the neck; seal the mouth and nose.",
        "**Mouth-to-mask / face shield** \u2014 preferred for protection against "
        "infection; the one-way valve prevents contact with vomit and blood.",
        "**Bag-valve-mask (Ambu bag)** \u2014 by trained rescuers; two-person "
        "technique gives a better seal; can deliver **100 % oxygen**.",
        "If the chest does **not** rise: **re-check the head tilt, re-seal the "
        "mouth, look for an obstruction** \u2014 but do **not** give more than "
        "**2 attempts** before resuming compressions.",
        "**Gastric inflation** from forceful breaths causes vomiting and "
        "aspiration \u2014 if vomiting occurs, turn the head to the side, clear "
        "the mouth and continue.",
    ])

    # ------------------------------------------------------------------
    b.h2("The Automated External Defibrillator (AED)")
    b.p("An AED is a portable device that analyses the heart rhythm and, if a "
        "**shockable rhythm (ventricular fibrillation or pulseless ventricular "
        "tachycardia)** is present, delivers an electric shock. It is designed to "
        "be used by laypersons and **will not shock a casualty who does not need "
        "it**.")
    b.numbered([
        "Switch the AED on as soon as it arrives; **continue CPR while the pads "
        "are being attached**.",
        "Bare and dry the chest. Attach the pads: one **below the right collar "
        "bone**, the other on the **left side of the chest below the armpit "
        "(mid-axillary line)** \u2014 the *anterolateral* position.",
        "Ensure nobody is touching the casualty; say **\u2018Stand clear!\u2019** "
        "while the machine analyses.",
        "If a shock is advised, press the **shock button** (or it may be "
        "automatic), then **resume compressions immediately** for 2 minutes "
        "before the next analysis.",
        "If **no shock is advised**, resume CPR at once.",
        "Leave the pads attached and the AED on until help arrives.",
    ])
    b.table(
        ["Situation", "AED precaution"],
        [["Wet chest / casualty in water", "Drag clear of water and **dry the "
                                           "chest** before applying pads"],
         ["Hairy chest", "Shave or wipe quickly, or press the pads firmly; a "
                         "spare set of pads may be needed"],
         ["Medication patch on the chest", "**Remove the patch** and wipe the "
                                           "skin"],
         ["Pacemaker or implanted defibrillator (a lump under the skin)",
          "Place the pad **at least 8\u201312 cm (3\u20135 in) away** from the "
          "device"],
         ["Metal jewellery / metal surface", "Remove necklaces near the pads; "
                                             "move the casualty off a metal "
                                             "sheet; do **not** touch the "
                                             "casualty during the shock"],
         ["Child 1\u20138 years", "Use **paediatric pads/attenuator**; if not "
                                  "available, adult pads may be used"],
         ["Infant < 1 year", "A manual defibrillator is preferred; an AED may be "
                             "used if nothing else is available"],
         ["Pregnancy / trauma", "AED is used normally \u2014 it is safe"],
         ["Oxygen flowing", "Move the oxygen mask/tubing at least 1 m away "
                            "before the shock (fire risk)"]],
        weights=[4.2, 8.4])
    b.bullets([
        "The most common rhythm in a witnessed adult cardiac arrest is "
        "**ventricular fibrillation**, and the only effective treatment for it is "
        "**defibrillation**.",
        "**Non-shockable rhythms** \u2014 asystole and pulseless electrical "
        "activity (PEA); these need CPR and drugs, not a shock.",
        "A **precordial thump** is no longer recommended in first aid.",
    ])

    # ------------------------------------------------------------------
    b.h2("The Recovery Position")
    b.p("Used for an **unconscious casualty who is breathing normally** and has "
        "no injury preventing it. It keeps the airway open by letting the tongue "
        "fall forward and allows vomit, blood and saliva to drain out of the "
        "mouth.")
    b.numbered([
        "Kneel beside the casualty; remove spectacles and bulky objects from the "
        "pockets.",
        "Straighten the legs; place the **arm nearer to you at right angles to "
        "the body, elbow bent, palm upwards**.",
        "Bring the **far arm across the chest** and hold the back of the hand "
        "against the near cheek.",
        "With the other hand, **grasp the far leg above the knee and pull it up**, "
        "keeping the foot on the ground.",
        "Pull on the far leg and **roll the casualty towards you** onto the side.",
        "Adjust the upper leg so that the **hip and knee are bent at right "
        "angles**.",
        "**Tilt the head back** gently to keep the airway open, and make sure the "
        "**mouth points slightly downwards**.",
        "Cover with a blanket, **monitor breathing continuously**, and "
        "**change sides every 30 minutes** to prevent pressure injury.",
    ])
    b.box("POSITION OF THE CASUALTY \u2014 A FAVOURITE EXAM TABLE", [
        "**Unconscious but breathing** \u2192 **recovery (lateral) position**.",
        "**Cardiac arrest** \u2192 flat on the **back on a hard surface**.",
        "**Shock** \u2192 lying flat, **legs raised 20\u201330 cm**, head low "
        "and turned to one side.",
        "**Fainting** \u2192 lie down and raise the legs; or sit with the head "
        "between the knees.",
        "**Breathlessness, heart attack, asthma, chest injury** \u2192 "
        "**sitting up / half-sitting (Fowler's)**, supported, leaning slightly "
        "forward.",
        "**Head injury / suspected spinal injury** \u2192 **do not move**; "
        "keep flat and support the head in line with the body.",
        "**Abdominal injury / after abdominal pain** \u2192 lying on the back "
        "with **knees drawn up** and supported.",
        "**Snake bite / bleeding limb** \u2192 keep the affected part **below "
        "heart level** for a snake bite, and **raised** for bleeding.",
        "**Pregnant casualty** \u2192 **left lateral** position.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Choking (Foreign-Body Airway Obstruction)")
    b.p("Choking is the mechanical obstruction of the airway by a foreign body "
        "\u2014 the commonest cause of accidental death in small children "
        "(sweets, peanuts, coins, balloons, small toys) and a frequent cause of "
        "adult death at meals (meat, bones, dentures) and with alcohol.")
    b.table(
        ["Mild (partial) obstruction", "Severe (complete) obstruction"],
        [["Casualty **can speak, cough and breathe**",
          "**Cannot speak, cough, cry or breathe**"],
         ["Coughing is **effective** and forceful",
          "Cough is silent or absent; wheezy, gasping attempts at breathing"],
         ["Casualty is distressed but not blue",
          "Clutches the throat (**universal sign of choking**), face becomes "
          "**red then blue-grey (cyanosed)**, eyes bulging, then loses "
          "consciousness"],
         ["**Treatment:** encourage him to **cough**; do nothing else; stay with "
          "him and watch",
          "**Treatment:** 5 **back blows** \u2192 5 **abdominal thrusts** "
          "(Heimlich) \u2192 repeat; if unconscious, start **CPR**"]],
        weights=[6.4, 6.4], first_bold=False)
    b.h3("Treatment of severe choking \u2014 conscious adult or child (over 1 yr)")
    b.numbered([
        "Stand at the side and slightly behind; support the chest with one hand "
        "and **lean the casualty well forward**.",
        "Give up to **5 sharp back blows** between the shoulder blades with the "
        "heel of your hand. Check after each blow.",
        "If unsuccessful, give up to **5 abdominal thrusts (Heimlich "
        "manoeuvre)**: stand behind, put both arms round the upper abdomen, make "
        "a fist and place the thumb side **midway between the navel and the "
        "lower end of the breast bone**, grasp it with the other hand and pull "
        "**sharply inwards and upwards**.",
        "Continue alternating **5 back blows and 5 abdominal thrusts**; recheck "
        "the mouth after each cycle and remove any visible object with the "
        "fingers (**never blind finger-sweeps**).",
        "If the casualty becomes **unconscious**, lower him carefully to the "
        "ground, call 112/108 and **begin CPR starting with chest "
        "compressions** \u2014 compressions may expel the object.",
        "**Every casualty who has received abdominal thrusts must be seen by a "
        "doctor**, because of the risk of internal injury.",
    ])
    b.table(
        ["Special group", "Modified technique"],
        [["**Infant under 1 year**", "**NO abdominal thrusts.** Lay the baby "
                                     "face down along your forearm with the "
                                     "head low, supporting the jaw \u2192 "
                                     "**5 back blows** between the shoulder "
                                     "blades \u2192 turn face up \u2192 **5 "
                                     "chest thrusts** with two fingers on the "
                                     "lower sternum. Repeat; call for help; "
                                     "start CPR if unresponsive."],
         ["**Pregnant woman or very obese adult**", "Use **chest thrusts** "
                                                    "(hands on the lower half "
                                                    "of the sternum) instead of "
                                                    "abdominal thrusts."],
         ["**Casualty in a wheelchair or unable to stand**", "Apply abdominal "
                                                             "thrusts from "
                                                             "behind the chair, "
                                                             "or lay him down "
                                                             "and use the heel "
                                                             "of the hand on the "
                                                             "upper abdomen."],
         ["**Self-treatment (alone)**", "Give yourself abdominal thrusts with "
                                        "your own fist, or press the upper "
                                        "abdomen sharply against a **hard edge "
                                        "\u2014 a chair back, table or railing**."],
         ["**Unconscious casualty**", "Chest compressions (CPR) generate higher "
                                      "airway pressure than abdominal thrusts "
                                      "\u2014 **start CPR**."]],
        weights=[3.4, 9.2])
    b.box("REMEMBER", [
        "The **Heimlich manoeuvre = abdominal thrusts**, described by "
        "**Dr. Henry Heimlich (1974)**.",
        "**Never** slap the back of a person who is coughing effectively while "
        "sitting upright, and never give abdominal thrusts to an **infant**.",
        "**Never do a blind finger sweep** \u2014 it may push the object deeper.",
        "A choking child should never be held upside down and shaken.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("CPR in Special Situations")
    b.table(
        ["Situation", "Modification"],
        [["**Drowning**", "The arrest is **asphyxial**: give **5 rescue "
                          "breaths/2 minutes of CPR before calling for help** if "
                          "alone; rescue breathing may be started in shallow "
                          "water; do **not** try to drain water from the lungs; "
                          "expect vomiting."],
         ["**Electrocution / lightning**", "**Switch off the current first**; do "
                                           "not touch the casualty until the "
                                           "supply is isolated. Cardiac arrest "
                                           "is common \u2014 CPR and early AED; "
                                           "treat burns at entry and exit "
                                           "points."],
         ["**Trauma**", "Control catastrophic bleeding first, protect the "
                        "cervical spine with manual in-line support, use "
                        "**jaw thrust** to open the airway."],
         ["**Pregnancy (after 20 weeks)**", "Compress **slightly higher on the "
                                            "sternum**; have someone **displace "
                                            "the uterus to the left** manually; "
                                            "transport urgently \u2014 saving "
                                            "the mother saves the baby."],
         ["**Hypothermia / cold water drowning**", "Handle gently; **continue CPR "
                                                   "for much longer** and warm "
                                                   "the casualty \u2014 "
                                                   "\u2018not dead until warm "
                                                   "and dead\u2019."],
         ["**Poisoning / overdose**", "Avoid mouth-to-mouth contact if a "
                                      "corrosive or organophosphate poison is "
                                      "on the lips \u2014 use a **mask or "
                                      "compression-only CPR**."],
         ["**Choking-related arrest**", "Start with compressions; check the "
                                        "mouth for the dislodged object after "
                                        "each cycle."],
         ["**Suspected spinal injury**", "Open the airway with a **jaw thrust** "
                                         "and keep the head in line; log-roll "
                                         "with helpers if the casualty must be "
                                         "turned."],
         ["**COVID-19 / infectious risk**", "Place a cloth over the mouth and "
                                            "nose, use **compression-only CPR** "
                                            "with a mask on the rescuer, and use "
                                            "the AED normally."]],
        weights=[3.2, 9.4], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Signs of Effective CPR, Complications and After-Care")
    b.table(
        ["Signs that CPR is effective", "Complications of CPR"],
        [["Chest visibly rises with each rescue breath.",
          "**Fracture of ribs or sternum** (commonest, especially in the "
          "elderly)"],
         ["A carotid/femoral pulse can be felt with each compression.",
          "**Vomiting and aspiration** of stomach contents"],
         ["Skin colour improves; cyanosis lessens.",
          "Injury to the **liver, spleen or stomach** from thrusts placed too "
          "low (over the xiphoid)"],
         ["Pupils begin to constrict and react to light.",
          "**Pneumothorax**, lung contusion, fat embolism"],
         ["Spontaneous breathing, coughing, movement or a return of "
          "consciousness = **ROSC (return of spontaneous circulation)**.",
          "Gastric distension from over-ventilation; bruising of the chest wall"]],
        weights=[6.4, 6.4], first_bold=False)
    b.bullets([
        "**Complications must never stop you from giving CPR** \u2014 "
        "\u2018a broken rib is better than a dead casualty\u2019.",
        "After ROSC: place in the **recovery position**, keep warm, give oxygen "
        "if trained, monitor breathing and pulse continuously, keep nil by mouth "
        "and arrange **urgent hospital transfer** \u2014 arrest may recur.",
        "Record the **time of arrest, the time CPR was begun, the number of "
        "shocks and the time of ROSC** for the doctor.",
        "Rescuers should be offered emotional support afterwards \u2014 "
        "resuscitation is stressful even when successful.",
    ])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "CPR sequence is **C-A-B**; start on any unresponsive casualty who is "
        "**not breathing normally**.",
        "Adult: **rate 100\u2013120/min, depth 5\u20136 cm, ratio 30 : 2**, "
        "full recoil, pauses **< 10 s**, change rescuer every **2 minutes**.",
        "Child: depth **\u2153 of chest (\u2248 5 cm)**; Infant: **two fingers, "
        "4 cm**, **5 breaths first**, brachial pulse; two professional rescuers "
        "use **15 : 2**.",
        "Hand position = **lower half of the sternum**; infant = **just below "
        "the nipple line**.",
        "**AED pads:** below the right collar bone and on the left mid-axillary "
        "line; resume compressions immediately after the shock.",
        "**Choking:** conscious \u2192 **5 back blows + 5 abdominal thrusts**; "
        "infant \u2192 **back blows + chest thrusts, never abdominal**; "
        "unconscious \u2192 **CPR**.",
        "**Recovery position** for the unconscious casualty who is breathing; "
        "change sides every 30 minutes.",
        "Brain damage in **3\u20134 minutes**; survival falls **7\u201310 % per "
        "minute**; defibrillation is the definitive treatment of **ventricular "
        "fibrillation**.",
        "Commonest complication of CPR = **fractured ribs**; commonest fatal "
        "error = **not starting CPR at all**.",
    ])
