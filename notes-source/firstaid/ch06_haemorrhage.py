# -*- coding: utf-8 -*-
"""Chapter 6 - Haemorrhage (Bleeding)."""


def render(b):
    b.chapter(
        "Haemorrhage (Bleeding)",
        "Types of bleeding, effects of blood loss, natural arrest of "
        "haemorrhage, control of external bleeding, pressure points, "
        "tourniquets, internal bleeding and bleeding from special sites.",
        syllabus=[
            "Haemorrhage \u2014 definition, classification (arterial, venous, "
            "capillary; external, internal, concealed; primary, reactionary, "
            "secondary), signs and symptoms, effects of blood loss.",
            "Control of bleeding \u2014 direct and indirect pressure, pressure "
            "points, pressure bandage, tourniquet; internal haemorrhage; "
            "bleeding from the nose, ear, mouth, lung, stomach, varicose veins "
            "and tooth socket.",
        ])

    # ------------------------------------------------------------------
    b.h2("Definition and Classification")
    b.box("DEFINITION", [
        "**Haemorrhage** means the **escape of blood from a ruptured or cut "
        "blood vessel** (*haima* = blood, *rhegnumi* = to burst forth). "
        "**Severe bleeding is second only to airway obstruction as a cause of "
        "preventable death** and must be controlled immediately.",
        "The average adult has **5\u20136 litres** of blood (about 8 % of body "
        "weight; 70\u201380 ml/kg). A **child** has about 2\u20132.5 litres and "
        "an **infant** only about **250\u2013350 ml** \u2014 so even a small loss "
        "is dangerous in a baby.",
    ], kind="def")
    b.table(
        ["Basis", "Types"],
        [["**Source (type of vessel)**", "**Arterial, venous** and "
                                        "**capillary** bleeding"],
         ["**Site**", "**External** (visible, from a wound) and **internal** "
                      "(concealed \u2014 into a body cavity or tissues). "
                      "Internal bleeding may become **revealed** when blood "
                      "appears at a natural opening (nose, mouth, ear, urine, "
                      "stool, vagina)"],
         ["**Time of occurrence**", "**Primary** \u2014 at the moment of injury; "
                                    "**Reactionary (intermediate)** \u2014 "
                                    "within **24 hours**, when blood pressure "
                                    "rises, a clot is dislodged or a ligature "
                                    "slips; **Secondary** \u2014 after "
                                    "**7\u201314 days**, due to **infection** "
                                    "eroding a vessel"],
         ["**Amount**", "Mild, moderate and severe (life-threatening/"
                        "catastrophic)"]],
        weights=[3.2, 9.4])
    b.h3("Arterial, venous and capillary bleeding \u2014 the master comparison")
    b.table(
        ["Feature", "Arterial", "Venous", "Capillary"],
        [["Source", "Cut **artery** \u2014 carries blood from the heart",
          "Cut **vein** \u2014 carries blood towards the heart",
          "Ruptured **capillaries**"],
         ["Colour of blood", "**Bright red (scarlet)** \u2014 oxygenated",
          "**Dark red (bluish/purple)** \u2014 deoxygenated",
          "Bright to dark red, mixed"],
         ["Flow", "**Spurts in jets, synchronised with each heart beat**; "
                  "pulsating", "**Steady, copious, welling-up flow**; may gush "
                               "but does not spurt", "**Slow oozing** from the "
                                                     "whole raw surface"],
         ["Pressure", "High \u2014 difficult to control",
          "Low \u2014 easier to control", "Very low"],
         ["Danger", "**Greatest** \u2014 rapid, massive loss; death in minutes "
                    "from a large artery",
          "Serious if a large vein; **air may be sucked into a neck vein "
          "(air embolism)**",
          "Usually slight, but large grazes can lose much fluid; risk of "
          "infection"],
         ["Example", "Wound of the femoral, brachial or carotid artery",
          "Bleeding varicose vein, cut on the back of the hand",
          "Graze, abrasion, shallow cut"],
         ["Control", "**Direct pressure**, elevation, pressure point; "
                     "tourniquet only as a last resort",
          "Direct pressure and **elevation** (very effective)",
          "Direct pressure and a simple dressing"]],
        weights=[2.1, 3.9, 3.6, 3.2], size=8.6)

    # ------------------------------------------------------------------
    b.h2("Effects of Blood Loss")
    b.table(
        ["Blood lost", "Approximate volume (adult)", "Effects"],
        [["**Up to 500 ml (10 %)**", "Half a litre \u2014 the amount given by a "
                                    "blood donor",
          "Usually no symptoms; quickly replaced by the body"],
         ["**500\u20131,000 ml (10\u201320 %)**", "Up to 1 litre",
          "Slight rise in pulse rate, pallor, mild thirst and giddiness; "
          "**compensated \u2014 blood pressure still normal**"],
         ["**1,000\u20131,500 ml (20\u201330 %)**", "1\u20131.5 litres",
          "**Definite shock** \u2014 pulse rapid and weak, cold clammy skin, "
          "thirst, restlessness, rapid breathing, falling blood pressure, "
          "reduced urine"],
         ["**1,500\u20132,000 ml (30\u201340 %)**", "1.5\u20132 litres",
          "**Severe shock** \u2014 marked pallor, air hunger, confusion, "
          "systolic BP below 90, feeble pulse, cold extremities"],
         ["**More than 2,000 ml (> 40 %)**", "Over 2 litres",
          "**Profound, often fatal shock** \u2014 unconsciousness, absent "
          "peripheral pulses, cardiac arrest"]],
        weights=[2.8, 3.4, 6.4])
    b.bullets([
        "A loss of about **one-third of the blood volume may be fatal** if it is "
        "rapid and untreated.",
        "**Rapid** loss is far more dangerous than the same loss occurring "
        "slowly, because there is no time for compensation.",
        "Children, the elderly and thin persons tolerate blood loss poorly.",
        "The body compensates by **constricting skin vessels (pallor), "
        "increasing the heart rate, increasing breathing and shifting fluid from "
        "the tissues** \u2014 these are exactly the signs of shock.",
    ])
    b.h3("Signs and symptoms of severe bleeding")
    b.table(
        ["Symptoms (complained of)", "Signs (observed)"],
        [["Faintness and giddiness", "Visible bleeding, blood-soaked clothing"],
         ["**Thirst** (a very important symptom)",
          "**Pale, cold, clammy (sweating) skin**; blue lips"],
         ["Nausea, sometimes vomiting", "**Rapid, weak, thready pulse** (later "
                                       "imperceptible)"],
         ["Restlessness, anxiety, \u2018feeling of impending doom\u2019",
          "**Rapid, shallow, sighing breathing (air hunger)**, yawning"],
         ["Dimness of vision, noises in the ears",
          "Dilated pupils; sunken eyes with dark rings"],
         ["Feeling cold, weakness", "Falling blood pressure, reduced urine "
                                    "output, restlessness \u2192 confusion "
                                    "\u2192 unconsciousness"]],
        weights=[6.0, 6.8], first_bold=False)

    # ------------------------------------------------------------------
    b.h2("How the Body Arrests Bleeding Naturally")
    b.numbered([
        "**Retraction and contraction** of the cut vessel ends (an artery "
        "retracts into its sheath and its muscular wall constricts).",
        "**Fall in blood pressure** as blood is lost, which slows the flow.",
        "**Platelets adhere** to the damaged wall and form a plug.",
        "**Clotting (coagulation)** \u2014 prothrombin \u2192 thrombin, then "
        "**fibrinogen \u2192 fibrin**, forming a mesh that traps blood cells; "
        "normal clotting time **3\u20138 minutes**.",
        "Clot retraction and, finally, organisation of the clot by fibrous "
        "tissue.",
    ])
    b.p("**Clotting needs vitamin K, calcium, platelets and clotting factors.** "
        "It is delayed in haemophilia, in liver disease, in patients on "
        "**aspirin, heparin or warfarin**, and when a wound is repeatedly "
        "disturbed \u2014 which is why a dressing once applied should **not** be "
        "removed.")

    # ------------------------------------------------------------------
    b.h2("Control of External Bleeding \u2014 the Practical Sequence")
    b.box("MNEMONIC: \u2018S-E-R\u2019 / \u2018R-E-D\u2019 \u2014 THE THREE "
          "PILLARS", [
        "**R**est \u2014 lay the casualty **down** with the head low; rest "
        "reduces the pulse rate and the force of bleeding.",
        "**E**levation \u2014 **raise the bleeding part above the level of the "
        "heart** (unless a fracture is suspected) to reduce the blood flow into "
        "it.",
        "**D**irect pressure \u2014 press **firmly on the wound** over a sterile "
        "dressing, with the fingers or palm, for **at least 10 minutes without "
        "releasing**.",
    ], kind="mnemonic")
    b.numbered([
        "**Lay the casualty down** and reassure him; call for help (112/108).",
        "**Expose the wound** and look for embedded foreign bodies.",
        "**Apply direct pressure** with a sterile dressing (or your gloved hand, "
        "or the casualty's own hand) for **10 minutes continuously**.",
        "**Elevate** the injured part and support it.",
        "Apply a **pressure (firm) dressing**: pad + bandage, tight enough to "
        "stop bleeding but not to cut off circulation; **check the pulse "
        "beyond** it.",
        "If blood soaks through, **do not remove the dressing** \u2014 add "
        "another pad on top and bandage more firmly. If it soaks through a second "
        "time, remove them and re-apply accurate direct pressure over the "
        "bleeding point.",
        "**Indirect pressure** at a **pressure point** may be used for a short "
        "time (**not more than 10\u201315 minutes**) when direct pressure fails "
        "on a limb.",
        "**Immobilise** the part (sling or splint) \u2014 movement restarts "
        "bleeding.",
        "**Treat for shock**: keep flat, legs raised, warm (cover with a "
        "blanket), loosen tight clothing, **nothing by mouth**, and reassure.",
        "**Monitor** breathing, pulse and level of response every 10 minutes and "
        "record; be ready to give CPR.",
        "For **catastrophic limb bleeding that cannot be controlled**, apply "
        "**wound packing with a haemostatic dressing** or a **tourniquet** "
        "(see below), and get the casualty to hospital urgently.",
    ])
    b.h3("Pressure points (indirect digital pressure)")
    b.p("A pressure point is a place where a **main artery runs close to the "
        "skin over a bone**, so that it can be pressed against the bone to stop "
        "the flow beyond. Pressure is applied with the **thumb or fingers** "
        "and cannot be maintained for long.")
    b.table(
        ["Artery", "Where to press", "Controls bleeding from"],
        [["**Temporal**", "In front of the ear, against the skull",
          "Scalp and temple"],
         ["**Facial**", "On the lower border of the jaw, about 3 cm in front of "
                        "its angle", "Face, cheek and lip"],
         ["**Carotid**", "Side of the neck, beside the windpipe, pressing "
                         "backwards \u2014 **never press both sides and never "
                         "press longer than necessary**",
          "Severe bleeding from the neck (last resort)"],
         ["**Subclavian**", "Behind the middle of the collar bone, pressing "
                            "downwards and backwards against the first rib",
          "Shoulder and upper arm"],
         ["**Brachial**", "On the **inner side of the upper arm**, in the groove "
                          "between the biceps and triceps, pressing the artery "
                          "against the humerus",
          "Forearm and hand (the classical arm pressure point)"],
         ["**Radial / Ulnar**", "At the wrist, thumb side and little-finger side",
          "Hand and palm"],
         ["**Femoral**", "In the **groin**, at the mid-point of the fold, "
                         "pressing firmly **backwards against the pelvis** with "
                         "the thumbs or heel of the hand",
          "Thigh and the whole lower limb (the most important pressure point)"],
         ["**Popliteal**", "Behind the knee", "Leg below the knee"],
         ["**Posterior tibial / Dorsalis pedis**", "Behind the inner ankle / "
                                                   "front of the ankle",
          "Foot"],
         ["**Abdominal aorta**", "Firm pressure through the abdominal wall "
                                 "(medical use only)",
          "Massive pelvic/lower-limb bleeding"]],
        weights=[2.6, 5.0, 5.0])
    b.h3("The tourniquet \u2014 rules and dangers")
    b.table(
        ["Point", "Detail"],
        [["**What it is**", "A firm band applied round a **limb** to compress "
                            "all vessels and completely stop the blood flow "
                            "beyond it"],
         ["**When justified**", "Only for **life-threatening limb bleeding that "
                                "cannot be stopped** by direct pressure and "
                                "packing; **traumatic amputation**; a trapped or "
                                "multiple-casualty situation where the rescuer "
                                "cannot maintain pressure"],
         ["**Where applied**", "**5 cm above the wound** (never over a joint), "
                               "on a single bone segment (upper arm or thigh); "
                               "**never on the forearm or lower leg** if it can "
                               "be avoided; never over a fracture"],
         ["**How applied**", "Wide (at least 5 cm) flat band or a commercial "
                             "windlass tourniquet, tightened just enough to stop "
                             "the bleeding and abolish the distal pulse; padded "
                             "underneath if improvised"],
         ["**Documentation**", "**Write the time of application on the "
                               "casualty's forehead or on a label** and tell "
                               "the ambulance staff; the tourniquet must be "
                               "**clearly visible** \u2014 never covered by a "
                               "bandage or clothing"],
         ["**Time limit**", "It should **not be left on for more than 1\u20132 "
                            "hours**; do **not** loosen and re-tighten it "
                            "periodically in first aid \u2014 releasing it "
                            "restarts bleeding and can cause shock. Only a "
                            "doctor should release it"],
         ["**Dangers**", "**Gangrene** and loss of the limb, nerve and muscle "
                         "damage, crush-type toxic release on removal, severe "
                         "pain, and renewed bleeding if it slips; it may also "
                         "increase bleeding if too loose (it then blocks only "
                         "the veins)"],
         ["**Improvised**", "A **narrow-fold triangular bandage, belt, tie or "
                            "cloth** with a stick twisted into it (windlass) "
                            "\u2014 **never use wire, rope, string or a thin "
                            "cord**"]],
        weights=[2.6, 10.0])
    b.box("MODERN PRACTICE POINT", [
        "For ordinary bleeding the tourniquet is **obsolete** \u2014 direct "
        "pressure, elevation and a pressure dressing control almost all "
        "bleeding.",
        "But in **catastrophic haemorrhage** (blast, amputation, severe "
        "machinery injury) a correctly applied tourniquet is **life-saving**; "
        "the modern rule is \u2018**life before limb**\u2019.",
        "**Wound packing** (pushing a haemostatic or plain gauze firmly into a "
        "deep wound and holding pressure for 3 minutes) is used for junctional "
        "wounds (groin, armpit, neck) where a tourniquet cannot be applied.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Internal (Concealed) Haemorrhage")
    b.p("Bleeding into a body cavity or into the tissues, where it cannot be "
        "seen. It is **dangerous precisely because it is hidden** \u2014 "
        "suspect it in every serious injury and in any casualty with "
        "**unexplained shock**.")
    b.table(
        ["Causes", "Sites"],
        [["Blunt injury to the chest or abdomen (road accident, fall, blow, "
          "crush)", "**Chest** \u2014 haemothorax; **abdomen** \u2014 rupture of "
                    "the **liver, spleen, kidney**, mesenteric vessels"],
         ["Fracture of large bones (femur may bleed 1\u20132 litres; pelvis "
          "2\u20133 litres)", "Thigh, pelvis, retroperitoneum"],
         ["Rupture of an aneurysm, ectopic pregnancy, peptic ulcer",
          "Abdomen, pelvis, gastro-intestinal tract"],
         ["Bleeding disorders, anticoagulant drugs",
          "Brain (**intracranial haemorrhage**), joints, muscles"],
         ["Penetrating wounds, stab and gunshot injuries",
          "Any cavity \u2014 skull, chest, abdomen, pelvis"]],
        weights=[6.2, 6.6], first_bold=False)
    b.h3("Signs of internal bleeding")
    b.bullets([
        "**All the signs of shock without visible blood loss** \u2014 pale, "
        "cold, clammy skin; rapid weak pulse; rapid shallow breathing; thirst; "
        "restlessness; giddiness; falling level of consciousness.",
        "**Pain, tenderness, rigidity or guarding** of the abdomen; "
        "**distension**; \u2018board-like\u2019 abdomen.",
        "Pattern **bruising** (seat-belt mark, tyre mark), swelling of a limb, "
        "deformity.",
        "**Revealed** internal bleeding \u2014 blood at a natural opening: "
        "**haemoptysis** (coughed-up bright red frothy blood \u2014 lung), "
        "**haematemesis** (vomited blood, dark like coffee grounds \u2014 "
        "stomach), **malaena** (black tarry stool \u2014 upper gut), "
        "**haematuria** (blood in urine \u2014 kidney/bladder), bleeding from "
        "the ear or nose (**skull fracture**), vaginal bleeding "
        "(pregnancy/uterine).",
        "**Air hunger** \u2014 restless gasping for air \u2014 is a grave sign.",
    ])
    b.h3("First aid for internal bleeding")
    b.numbered([
        "**Lay the casualty down**, head low and turned to one side; **raise the "
        "legs** (shock position) unless there is a head or chest injury or a leg "
        "fracture.",
        "**Loosen** tight clothing at the neck, chest and waist.",
        "**Keep warm** with a blanket, but do **not** use hot-water bottles "
        "(they dilate skin vessels and worsen shock).",
        "**Give nothing by mouth** \u2014 no water, no food, no medicine, no "
        "alcohol. Moisten the lips with a wet cloth.",
        "**Do not apply any external pressure** on the abdomen or chest; do not "
        "massage.",
        "**Immobilise fractures** \u2014 this greatly reduces internal blood loss.",
        "**Record and monitor** the pulse, breathing and level of response every "
        "**10 minutes** (every 5 minutes if serious); note the time.",
        "Arrange the **most urgent possible transport** to hospital \u2014 "
        "internal bleeding needs surgery. Preserve any vomited or passed blood "
        "for the doctor.",
        "Be prepared to give **CPR**.",
    ])

    # ------------------------------------------------------------------
    b.h2("Bleeding from Special Sites")
    b.table(
        ["Site / type", "Recognition", "First aid"],
        [["**Nose (epistaxis)**", "Bleeding from one or both nostrils; may "
                                  "follow a blow, picking, sneezing, high BP or "
                                  "heat",
          "**Sit up, head bent slightly forward**; **pinch the soft part of the "
          "nose for 10 minutes** continuously, breathe through the mouth; cold "
          "compress over the nose; do not blow the nose for 4 hours. Refer if "
          "bleeding lasts more than **20\u201330 minutes**, is very heavy, or "
          "follows a head injury (may be **CSF/skull fracture**)"],
         ["**Ear**", "Blood or straw-coloured fluid from the ear canal",
          "**Never plug the ear.** Cover lightly with a sterile pad, lay the "
          "casualty in the **recovery position with the bleeding ear "
          "downwards** so that it drains; refer at once (suspect **fractured "
          "base of skull** or a ruptured eardrum)"],
         ["**Mouth / tooth socket**", "Bleeding after extraction, cut lip or "
                                      "tongue",
          "Sit up with the head forward; place a **thick gauze pad on the socket "
          "and ask the casualty to bite firmly for 10\u201320 minutes**; do not "
          "rinse the mouth, do not suck or probe the socket, avoid hot drinks; "
          "refer if it continues"],
         ["**Lung (haemoptysis)**", "**Bright red, frothy blood coughed up**, "
                                    "breathlessness",
          "Half-sitting position, leaning to the affected side; loosen clothing; "
          "reassure; **nothing by mouth**; urgent hospital transfer; do not let "
          "the casualty talk"],
         ["**Stomach (haematemesis)**", "**Vomited blood \u2014 bright red or "
                                        "dark \u2018coffee-ground\u2019**, "
                                        "often with abdominal pain and black "
                                        "tarry stools",
          "Lay flat with head turned to one side, knees bent; **nothing by "
          "mouth**; keep the vomit for the doctor; treat shock; urgent transfer"],
         ["**Varicose vein (leg)**", "Profuse, dark, welling bleeding from the "
                                     "leg of an elderly person",
          "Lay the casualty down and **raise the leg high** (well above the "
          "heart), apply firm direct pressure with a pad and bandage; remove "
          "garters/tight clothing; refer"],
         ["**Palm of the hand**", "Deep cut with heavy bleeding; often a divided "
                                  "tendon",
          "Place a pad in the palm, ask the casualty to **clench the fist over "
          "the pad**, bandage the fist tightly, and support in an **elevation "
          "sling**"],
         ["**Scalp**", "Profuse bleeding from a vascular gaping wound",
          "Firm direct pressure with a sterile pad and bandage; use a **ring "
          "pad** if a depressed fracture is suspected; refer"],
         ["**Vaginal / obstetric**", "Bleeding in pregnancy, after childbirth or "
                                     "from injury",
          "Lay down, knees raised, place a sanitary pad (do **not** pack the "
          "vagina), keep warm, nothing by mouth, **urgent** transfer; save all "
          "pads and clots"],
         ["**Amputation / catastrophic limb bleeding**", "Spurting blood, part "
                                                        "severed",
          "Direct pressure/packing; if uncontrolled apply a **tourniquet**, note "
          "the time, preserve the severed part, treat shock, urgent transfer"],
         ["**Bleeding from a stoma or under a nail**", "Local ooze",
          "Gentle direct pressure with a sterile pad; refer if persistent"]],
        weights=[2.6, 3.8, 6.2], size=8.6)

    # ------------------------------------------------------------------
    b.h2("Blood Replacement \u2014 What the First Aider Should Know")
    b.bullets([
        "Lost blood is finally replaced in hospital by **intravenous fluids "
        "(normal saline, Ringer lactate) and blood transfusion** \u2014 never by "
        "anything given by mouth at the scene.",
        "**Blood groups:** A, B, AB, O with Rh factor. **O negative = universal "
        "donor; AB positive = universal recipient.** Cross-matching is "
        "essential; a mismatched transfusion causes a fatal reaction.",
        "A healthy donor of 18\u201365 years weighing over **45\u201350 kg** can "
        "give **350\u2013450 ml** every **3 months** (men) / 4 months (women). "
        "**World Blood Donor Day \u2014 14 June**; National Voluntary Blood "
        "Donation Day \u2014 1 October.",
        "Autologous transfusion = the patient's own blood; **massive "
        "transfusion** = replacement of the whole blood volume in 24 hours.",
    ])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "**Arterial** = bright red, spurting in jets; **venous** = dark red, "
        "steady flow; **capillary** = slow ooze.",
        "Time types: **primary** (at once), **reactionary** (within 24 h), "
        "**secondary** (7\u201314 days, due to infection).",
        "Adult blood volume **5\u20136 litres**; loss of **1\u20131.5 litres** "
        "causes definite shock; loss of **one-third** may be fatal.",
        "Control = **Rest + Elevation + Direct pressure** for **10 minutes**; "
        "then a pressure dressing.",
        "**Never remove a blood-soaked dressing** \u2014 add another pad over it.",
        "Chief pressure points: **brachial** (arm, inner upper arm against the "
        "humerus) and **femoral** (groin, against the pelvis).",
        "Tourniquet = **last resort only**, **5 cm above the wound**, note the "
        "**time**, keep it **visible**, never loosen in first aid.",
        "Internal bleeding = **shock without visible blood**; treat with the "
        "shock position, warmth, **nothing by mouth** and urgent transfer.",
        "**Epistaxis** \u2192 sit up, head forward, pinch the soft part for "
        "10 minutes. **Bleeding ear** \u2192 never plug; lie with that ear "
        "**downwards**.",
        "**Haemoptysis** = coughed bright frothy blood (lung); **haematemesis** "
        "= vomited coffee-ground blood (stomach); **malaena** = black tarry stool.",
    ])
