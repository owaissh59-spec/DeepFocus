# -*- coding: utf-8 -*-
"""Chapter 5 - Wounds."""


def render(b):
    b.part("PART III", "Injuries, Bleeding and Shock")
    b.chapter(
        "Wounds",
        "Classification and types of wounds, signs, general and special "
        "management, wound healing and its complications, tetanus, minor wounds, "
        "and burns and scalds.",
        syllabus=[
            "Wounds \u2014 definition, classification, types (incised, "
            "lacerated, contused, abrasion, punctured, gunshot, penetrating, "
            "avulsion, amputation, crush), signs and symptoms and first-aid "
            "management of each.",
            "Wound healing, infection, tetanus and gas gangrene; special wounds "
            "of the scalp, eye, chest and abdomen; minor wounds; burns and "
            "scalds.",
        ])

    # ------------------------------------------------------------------
    b.h2("Definition and Classification")
    b.box("DEFINITION", [
        "A **wound** is a **break in the continuity of the skin, mucous "
        "membrane or the surface of any tissue of the body**, through which blood "
        "escapes and germs may enter.",
        "Every wound therefore carries **three dangers**: **(1) bleeding, "
        "(2) infection and (3) shock** \u2014 together with possible damage to "
        "deeper structures (nerves, tendons, vessels, bones, organs).",
    ], kind="def")
    b.table(
        ["Basis of classification", "Types"],
        [["**Skin intact or broken**", "**Open wound** (skin broken \u2014 cut, "
                                      "abrasion, puncture) and **Closed wound** "
                                      "(skin unbroken \u2014 bruise, "
                                      "contusion, internal injury)"],
         ["**Cause**", "Mechanical (cut, blow, crush), thermal (burn, scald, "
                       "frostbite), chemical (acid, alkali), electrical, "
                       "radiational, bite"],
         ["**Depth / structures involved**", "Superficial (skin only), deep "
                                             "(muscle, vessel, nerve), "
                                             "penetrating (enters a cavity), "
                                             "perforating (enters and comes out)"],
         ["**Contamination**", "**Clean** (surgical), **contaminated** (dirty, "
                               "soil, rust), **infected** (pus present)"],
         ["**Bleeding**", "External (visible) and internal (concealed)"],
         ["**Healing**", "Healing by **first intention** (clean edges, "
                         "stitched) and by **second intention** (gaping/infected, "
                         "heals with a scar)"]],
        weights=[3.4, 9.2])

    # ------------------------------------------------------------------
    b.h2("Types of Wounds \u2014 Complete Table")
    b.table(
        ["Type of wound", "How caused", "Features", "Special danger"],
        [["**Incised (clean cut)**", "Sharp edge \u2014 knife, razor, glass, "
                                     "blade",
          "**Clean, straight edges**; bleeds **freely and profusely** because "
          "vessels are cut straight across",
          "**Severe bleeding**; deep cut may divide tendons and nerves"],
         ["**Lacerated (tear)**", "Blunt force, machinery, barbed wire, animal "
                                  "claws, fall on rough ground",
          "**Ragged, irregular, torn edges**; bleeds **less** than an incised "
          "wound", "**Greater risk of infection**; more tissue destruction"],
         ["**Abrasion (graze)**", "Rubbing or sliding \u2014 fall on a road, "
                                  "friction burn",
          "Only the **superficial skin is scraped off**; raw, painful, oozing "
          "surface with embedded dirt",
          "**Infection and tattooing** by grit; very painful"],
         ["**Contusion (bruise) \u2014 a closed wound**",
          "Blunt blow, fall, crush",
          "Skin **unbroken**; bleeding into the tissues \u2192 swelling, "
          "discoloration (red \u2192 purple \u2192 blue \u2192 green \u2192 "
          "yellow), pain, tenderness",
          "May conceal a **fracture or internal injury**"],
         ["**Punctured (stab)**", "Nail, needle, spike, knife, bayonet, fork, "
                                  "thorn, injection",
          "**Small external opening but deep track**; little external bleeding",
          "**Deep infection, especially TETANUS and gas gangrene**; may injure "
          "internal organs \u2192 internal bleeding"],
         ["**Gunshot (bullet/firearm)**", "Bullet, pellet, blast fragment",
          "**Small entry wound, larger ragged exit wound** (entry may show "
          "burning/blackening); may be blind (no exit)",
          "**Massive internal damage, foreign bodies, infection**; medico-legal "
          "case \u2014 inform police"],
         ["**Penetrating / perforating**", "Sharp or high-velocity object",
          "Penetrating \u2014 object **enters a body cavity** (chest, abdomen, "
          "skull); perforating \u2014 **enters and leaves**",
          "Injury to the heart, lung, gut, liver \u2192 **internal haemorrhage "
          "and shock**"],
         ["**Avulsion / degloving**", "Machinery, road accident, animal bite",
          "A **flap of skin or tissue is torn away** or peeled off, partly or "
          "completely", "Heavy bleeding; tissue may die \u2014 preserve the flap"],
         ["**Amputation (traumatic)**", "Machine, railway, road accident, blast",
          "A part (finger, hand, limb, ear) is **completely severed**",
          "Severe bleeding and shock; the **part may be re-implanted if properly "
          "preserved**"],
         ["**Crush injury**", "Heavy weight, building collapse, vehicle wheel",
          "Extensive damage of muscle with swelling; skin may look almost normal",
          "**Crush syndrome** \u2014 release of muscle toxins (myoglobin, "
          "potassium) \u2192 kidney failure and cardiac arrest"],
         ["**Bite wound (animal/human)**", "Dog, cat, monkey, snake, human teeth",
          "Punctured + lacerated wound with saliva contamination",
          "**Rabies**, tetanus, severe infection; human bites are the most "
          "heavily infected of all"],
         ["**Burn and scald wound**", "Dry heat/flame (burn), moist heat/steam "
                                      "(scald), chemicals, electricity, "
                                      "radiation",
          "Redness, blisters, charring; loss of skin",
          "Fluid loss \u2192 **shock**, infection, airway burn"]],
        weights=[2.6, 3.0, 4.2, 3.4], size=8.4)
    b.box("MOST-ASKED DISCRIMINATORS", [
        "Wound with **clean, straight edges that bleeds most profusely** = "
        "**incised**.",
        "Wound with **ragged torn edges and greater risk of infection** = "
        "**lacerated**.",
        "Wound with a **small opening but deep track \u2014 highest risk of "
        "tetanus** = **punctured**.",
        "**Closed** wound = **contusion (bruise)**.",
        "**Superficial** wound with only skin scraped off = **abrasion**.",
        "Wound in which **entry is small and exit large** = **gunshot**.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Signs and Symptoms of a Wound")
    b.table(
        ["Symptoms (told by the casualty)", "Signs (seen by the first aider)"],
        [["Pain at the site, often throbbing",
          "**Bleeding** \u2014 arterial, venous or capillary"],
         ["Faintness, giddiness, thirst", "Visible **break in the skin**, gaping "
                                          "of the edges"],
         ["Feeling of cold and weakness",
          "Swelling, bruising, discoloration"],
         ["Nausea and restlessness", "Loss of function of the part; deformity if "
                                     "a bone is broken"],
         ["Anxiety and fear", "**Signs of shock** \u2014 pale, cold clammy skin, "
                              "rapid weak pulse, rapid shallow breathing"],
         ["\u2014", "Foreign bodies, dirt, glass in the wound; escape of tissue "
                    "fluid or organs"]],
        weights=[6.4, 6.4], first_bold=False)

    # ------------------------------------------------------------------
    b.h2("General First-Aid Management of Wounds")
    b.numbered([
        "**Reassure** the casualty and lay him down (this alone prevents "
        "fainting).",
        "**Wash your hands** and wear gloves; do not touch the wound.",
        "**Expose the wound** \u2014 remove or cut clothing as necessary, "
        "without dragging.",
        "**Control the bleeding** \u2014 direct pressure over a dressing, "
        "**elevate** the part, and rest. (See Chapter 6.)",
        "**Do not remove** a blood clot or a foreign body that is deeply "
        "embedded; do not probe the wound.",
        "**Clean a minor wound** with clean running water or normal saline, "
        "washing **from the centre outwards**; dry with a sterile swab and apply "
        "an antiseptic (povidone-iodine) around \u2014 **not into** \u2014 the "
        "wound.",
        "**Cover with a sterile dressing** larger than the wound and bandage "
        "firmly but not tightly.",
        "**Immobilise and support** the injured part (a sling for the arm, "
        "splint for the leg); keep the part **raised** if possible.",
        "**Treat for shock** \u2014 keep the casualty warm, flat, legs raised, "
        "and give **nothing by mouth** (moisten the lips if thirsty).",
        "**Seek medical help** and ensure **anti-tetanus prophylaxis**.",
        "Record the time, the appearance of the wound and the treatment given.",
    ])
    b.box("WOUNDS THAT MUST ALWAYS BE SEEN BY A DOCTOR", [
        "Bleeding that cannot be controlled, or **spurting** bleeding.",
        "A wound that **gapes** and needs stitching, or is longer than 2\u20133 cm.",
        "**Deep, punctured, crushed or bite** wounds; any dirty wound "
        "contaminated with soil, dung or rust.",
        "Wounds with an **embedded foreign body**, glass or grit that cannot be "
        "flushed out.",
        "Wounds over a **joint, on the face, palm, sole or genitals**, or with "
        "loss of feeling/movement (nerve or tendon injury).",
        "Any wound in a **diabetic, an elderly person, or anyone on "
        "blood-thinning medicine**, and any wound showing **signs of infection**.",
        "Wounds where **tetanus immunisation is not up to date**.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Wound Healing and Its Complications")
    b.h3("Phases of healing")
    b.table(
        ["Phase", "Time", "What happens"],
        [["1. Haemostasis", "Seconds to minutes", "Vessels constrict; platelets "
                                                  "plug; fibrin clot forms"],
         ["2. Inflammatory", "0\u20133 days", "Redness, heat, swelling, pain; "
                                             "white cells clear bacteria and "
                                             "debris"],
         ["3. Proliferative", "3 days\u20133 weeks", "New capillaries, "
                                                     "granulation tissue, "
                                                     "collagen; edges contract; "
                                                     "epithelium grows over"],
         ["4. Maturation (remodelling)", "3 weeks\u20132 years", "Scar forms, "
                                                                 "shrinks and "
                                                                 "pales; regains "
                                                                 "up to 80 % of "
                                                                 "original "
                                                                 "strength"]],
        weights=[3.0, 2.8, 6.8])
    b.table(
        ["Factors that promote healing", "Factors that delay healing"],
        [["Clean wound with apposed edges; good blood supply",
          "**Infection**, foreign body, dead tissue (slough)"],
         ["Rest and immobilisation of the part",
          "Movement, repeated trauma, poor blood supply"],
         ["Good nutrition \u2014 **protein, vitamin C, vitamin A, zinc, iron**",
          "Malnutrition, anaemia, **deficiency of vitamin C (scurvy)**"],
         ["Youth and general good health", "**Diabetes mellitus**, obesity, old "
                                           "age, cancer, kidney/liver disease"],
         ["Proper dressing and moist wound environment",
          "**Smoking**, steroids, chemotherapy, radiotherapy; oedema"]],
        weights=[6.4, 6.4], first_bold=False)
    b.h3("Complications of wounds")
    b.table(
        ["Complication", "Points to remember"],
        [["**Haemorrhage**", "Primary (at the time of injury), **reactionary** "
                             "(within 24 hours, as BP rises) and **secondary** "
                             "(after 7\u201310 days, due to infection)"],
         ["**Shock**", "From blood and fluid loss or from pain"],
         ["**Infection**", "Signs: **increasing pain, redness, heat, swelling, "
                           "pus, foul smell, red streaks up the limb "
                           "(lymphangitis), tender swollen glands, fever and "
                           "malaise**"],
         ["**Tetanus (lock-jaw)**", "See below \u2014 the most feared "
                                    "complication of a dirty punctured wound"],
         ["**Gas gangrene**", "*Clostridium perfringens* in deep crushed, "
                              "dirty wounds \u2014 foul-smelling gas in "
                              "tissues, crackling under the skin, rapidly "
                              "fatal"],
         ["**Septicaemia / toxaemia**", "Spread of germs or toxins into the "
                                        "blood \u2014 high fever, rigors, "
                                        "collapse"],
         ["**Gangrene**", "Death of tissue from loss of blood supply "
                          "(too-tight bandage, tourniquet left on, crush, "
                          "diabetes)"],
         ["**Scar, keloid and contracture**", "Excessive scar tissue; "
                                              "contracture across a joint "
                                              "limits movement"],
         ["**Damage to deeper structures**", "Nerve (numbness, paralysis), "
                                             "tendon (loss of movement), "
                                             "vessel, bone (compound fracture), "
                                             "organ"]],
        weights=[3.2, 9.4])
    b.h3("Tetanus \u2014 must-know facts")
    b.table(
        ["Point", "Detail"],
        [["Organism", "***Clostridium tetani*** \u2014 an **anaerobic, "
                      "spore-forming bacillus** found in soil, dust, dung and "
                      "rusty metal"],
         ["Entry", "Deep **punctured** wounds, dirty lacerations, burns, animal "
                   "bites, the umbilical stump of a newborn (tetanus "
                   "neonatorum)"],
         ["Incubation period", "**7\u201310 days** (range 3 days \u2013 3 weeks); "
                              "the shorter the period, the worse the prognosis"],
         ["Toxin", "**Tetanospasmin** \u2014 acts on the nervous system"],
         ["Features", "**Lock-jaw (trismus)**, stiff neck, **risus sardonicus** "
                      "(fixed grin), painful generalised muscle spasms, arching "
                      "of the back (**opisthotonos**), spasm of respiratory "
                      "muscles \u2192 death; spasms provoked by light, noise or "
                      "touch"],
         ["First-aid prevention", "Thorough cleaning of every wound, removal of "
                                  "dirt and dead tissue, leaving deep wounds "
                                  "**open (not sealed)**, and prompt medical "
                                  "referral"],
         ["Immunisation", "**Tetanus toxoid (TT)** \u2014 active immunity, part "
                          "of DPT in infancy with boosters; a booster is given "
                          "if the last dose was **more than 5 years** ago "
                          "(10 years for a clean minor wound). **ATS / tetanus "
                          "immunoglobulin** gives immediate passive immunity in "
                          "an unimmunised casualty"]],
        weights=[2.8, 9.8])

    # ------------------------------------------------------------------
    b.h2("Special Wounds and Their Management")
    b.h3("Wound with an embedded foreign body")
    b.bullets([
        "**Do not remove** a large or deeply embedded object \u2014 it may be "
        "plugging a bleeding vessel.",
        "Control bleeding by pressing **on either side** of the object, not over "
        "it.",
        "Build up a **ring pad** (or two rolled bandages) around the object, "
        "higher than the object, and bandage over the pads so that no pressure "
        "falls on the object itself.",
        "If the object is very long, support it; do not let it move. Arrange "
        "urgent hospital transfer and note the time.",
        "Small surface splinters and grit may be picked out with sterilised "
        "tweezers in the direction of entry.",
    ])
    b.h3("Scalp wounds")
    b.bullets([
        "Bleed **profusely** because the scalp is very vascular and its vessels "
        "cannot retract; the wound edges gape.",
        "Apply a **sterile pad with firm direct pressure** and bandage; do not "
        "press hard if you suspect an underlying **depressed skull fracture** "
        "\u2014 use a ring pad instead.",
        "Look for signs of **head injury** (unconsciousness, vomiting, "
        "bleeding/CSF from ear or nose, unequal pupils) \u2014 all such "
        "casualties go to hospital.",
    ])
    b.h3("Eye wounds")
    b.bullets([
        "Lay the casualty on his **back**, keep the head still, and tell him not "
        "to move the eyes.",
        "Cover with a **sterile eye pad or clean dressing**; do not apply "
        "pressure and do not try to remove an embedded object.",
        "**Never** wash out a penetrating eye injury, never remove a protruding "
        "object, never allow rubbing, and never apply ointment.",
        "Cover **both** eyes if possible (movement of one eye moves the other), "
        "and transfer lying down to an eye hospital.",
        "For a loose particle: flush with clean water from the inner to the outer "
        "corner, or lift it off with a moist swab; for chemical splash, "
        "**irrigate with running water for at least 20 minutes**.",
    ])
    b.h3("Chest wounds (penetrating / \u2018sucking\u2019 wound)")
    b.bullets([
        "A penetrating chest wound may **suck air into the chest cavity** with "
        "each breath (open pneumothorax), collapsing the lung.",
        "Signs: **bubbling/hissing/sucking sound at the wound, frothy blood, "
        "extreme breathlessness, blue lips, coughing of bright red frothy "
        "blood**, and later a rapid weak pulse with distended neck veins.",
        "Treatment: **cover the wound immediately with the palm of your gloved "
        "hand**, then apply a **sterile pad covered with plastic/cling film, "
        "taped on three sides only** so that air can escape but not enter "
        "(\u2018flutter valve\u2019).",
        "Place the casualty in a **half-sitting position, leaning towards the "
        "injured side**, support the arm in a sling, treat for shock and call an "
        "ambulance urgently. Do **not** give anything by mouth.",
        "If breathing worsens after sealing (tension pneumothorax), **release "
        "the dressing** at once.",
    ])
    b.h3("Abdominal wounds with protruding intestine (evisceration)")
    b.bullets([
        "Lay the casualty **on his back with knees bent and supported** to "
        "relax the abdominal wall.",
        "**Do NOT try to push the organs back** and **do not touch them**.",
        "Cover the protruding organs with a **large sterile dressing moistened "
        "with clean water/saline, then a plastic sheet or cling film**, and fix "
        "loosely \u2014 the object is to keep them **moist and clean**.",
        "**Nothing by mouth** \u2014 not even water (surgery will be needed); "
        "moisten the lips only.",
        "If the casualty coughs or vomits, support the abdomen with your hands "
        "over the dressing.",
        "Treat for shock and arrange **immediate** hospital transport.",
    ])
    b.h3("Amputation and avulsion \u2014 care of the severed part")
    b.numbered([
        "Control bleeding of the stump with **direct pressure and elevation**; "
        "cover with a bulky sterile dressing and bandage firmly. A tourniquet is "
        "used **only** if bleeding is life-threatening and uncontrollable.",
        "**Preserve the amputated part** \u2014 do **not** wash it with "
        "antiseptic or water and do **not** put it directly on ice.",
        "Wrap the part in a **clean, dry (or lightly moistened saline) gauze**, "
        "place it in a **clean plastic bag**, seal it, and put that bag in "
        "**another container of ice and water (cold, about 4 \u00b0C)**.",
        "Label with the casualty's name and the time of injury and send it **with "
        "the casualty** to hospital.",
        "Re-implantation is possible for up to about **6 hours (12\u201318 hours "
        "if well cooled)**; for the avulsed flap, replace it in position and "
        "cover.",
    ])
    b.h3("Crush injury")
    b.bullets([
        "Release the casualty as quickly as possible if trapped for **less than "
        "15 minutes**; if trapped longer, **do not release without medical "
        "help** if it can be avoided \u2014 sudden release floods the blood with "
        "toxins (**crush syndrome**) and can cause cardiac arrest and kidney "
        "failure.",
        "Support and immobilise the part, treat bleeding and shock, keep the "
        "casualty warm and note the **exact time of the crush** and of release.",
        "Watch for swelling and loss of pulse distally (**compartment "
        "syndrome**) \u2014 remove tight clothing, jewellery and bandages.",
    ])
    b.h3("Gunshot and blast wounds")
    b.bullets([
        "Treat as a **penetrating wound**: control bleeding, cover entry **and "
        "exit** wounds, immobilise, treat shock, urgent transport.",
        "Do not probe for the bullet; do not remove clothing unnecessarily "
        "\u2014 **preserve evidence** and **inform the police** (medico-legal "
        "case).",
        "Blast injuries may cause hidden **lung, ear and abdominal** damage even "
        "without external wounds.",
    ])

    # ------------------------------------------------------------------
    b.h2("Minor Wounds \u2014 Practical First Aid")
    b.table(
        ["Condition", "Management"],
        [["**Small cut / abrasion**", "Wash hands, clean with running water or "
                                     "saline, dry, apply antiseptic and an "
                                     "adhesive dressing; check tetanus status"],
         ["**Blister (friction)**", "**Do not prick** an intact blister; cover "
                                    "with a soft padded dressing. If burst, "
                                    "clean, do not remove the loose skin and "
                                    "cover"],
         ["**Splinter**", "Clean the area, sterilise tweezers, grasp the splinter "
                          "close to the skin and pull out **along the line of "
                          "entry**; if it is deep, broken off or under a nail "
                          "\u2014 leave it and refer"],
         ["**Fish hook**", "If the barb is exposed, cut it off and back the hook "
                           "out; if not, **leave it in**, pad round it and "
                           "refer"],
         ["**Torn or crushed nail**", "Cover with a dressing, support the finger "
                                      "and refer; a **blood blister under a nail "
                                      "(subungual haematoma)** needs medical "
                                      "release"],
         ["**Bruise / contusion**", "**RICE** \u2014 Rest, **Ice** (cold "
                                    "compress for 10\u201320 minutes wrapped in "
                                    "cloth), **Compression** with a crepe "
                                    "bandage, **Elevation**. Never massage a "
                                    "fresh bruise"],
         ["**Graze with embedded grit**", "Flush with plenty of clean water; do "
                                          "not scrub; cover with a non-adherent "
                                          "dressing"]],
        weights=[3.0, 9.6])

    # ------------------------------------------------------------------
    b.h2("Burns and Scalds")
    b.p("A **burn** is an injury caused by **dry heat** (flame, hot metal, "
        "sun, friction, electricity, radiation); a **scald** is caused by "
        "**moist heat** (boiling water, steam, hot oil, tea). The first-aid "
        "treatment of both is the same.")
    b.h3("Classification by depth")
    b.table(
        ["Degree", "Old name", "Layers involved", "Appearance and features"],
        [["**First degree**", "Superficial", "Epidermis only",
          "**Red, dry, painful**, no blister; heals in 3\u20137 days without a "
          "scar (e.g. sunburn)"],
         ["**Second degree**", "Partial thickness", "Epidermis + part of dermis",
          "**Blisters, moist, red, very painful**; heals in 2\u20133 weeks, may "
          "scar"],
         ["**Third degree**", "Full thickness", "Whole skin (\u00b1 fat)",
          "**White, waxy, brown or charred, dry and leathery; PAINLESS** "
          "(nerve endings destroyed); needs grafting"],
         ["**Fourth degree**", "\u2014", "Muscle, tendon, bone",
          "Charred, blackened; often after electrical burns \u2014 amputation "
          "may be needed"]],
        weights=[2.4, 2.4, 3.0, 5.0])
    b.h3("Extent \u2014 the Rule of Nines (adult)")
    b.table(
        ["Body part", "% of body surface"],
        [["Head and neck", "**9 %**"],
         ["Each arm (front + back)", "**9 %** each (total 18 %)"],
         ["Front of trunk (chest + abdomen)", "**18 %**"],
         ["Back of trunk", "**18 %**"],
         ["Each leg", "**18 %** each (total 36 %)"],
         ["Perineum / genitals", "**1 %**"],
         ["Palm of the casualty's own hand", "**1 %** \u2014 useful for small, "
                                             "patchy burns"],
         ["Child modification", "Head **18 %**, each leg **14 %** (a child's head "
                                "is relatively larger)"]],
        weights=[4.6, 4.4])
    b.box("WHEN IS A BURN \u2018SERIOUS\u2019? (send to hospital)", [
        "Any burn over **more than 10 % of the body in a child or 15\u201320 % "
        "in an adult** (some texts: >9 % child, >18 % adult).",
        "**All third-degree (full-thickness) burns**, however small.",
        "Burns of the **face, neck, mouth or throat** (airway risk), **hands, "
        "feet, genitals** or across a **joint**.",
        "**Circumferential** burns (right round a limb or the chest).",
        "**Electrical, chemical, inhalation and blast** burns.",
        "Burns in **infants, the elderly, pregnant women** and in casualties "
        "with diabetes, heart or lung disease.",
        "Any burn with **shock**, or with suspected non-accidental injury.",
    ], kind="exam")
    b.h3("First aid for burns and scalds \u2014 step by step")
    b.numbered([
        "**Stop the burning process** \u2014 remove the casualty from danger or "
        "the danger from the casualty. Smother flames with a blanket; make the "
        "casualty **STOP, DROP, WRAP and ROLL** on the ground; switch off the "
        "current in an electrical burn.",
        "**Cool the burn with cool (not ice-cold) running water for at least "
        "10\u201320 minutes** \u2014 this is the single most useful measure and "
        "is worthwhile up to 3 hours after the injury. Use clean water; never "
        "use ice, butter, oil, toothpaste, mud, ink, turmeric, cow dung or "
        "leaves.",
        "**Remove rings, watches, bangles, belts and tight clothing** from the "
        "area before it swells, but **never remove clothing stuck to the burn**.",
        "**Cover** the burn with a **sterile non-adherent dressing, clean "
        "plastic (cling film) or a clean cotton sheet** \u2014 lengthwise, not "
        "wound round the limb. For a burnt hand, a clean plastic bag may be "
        "used.",
        "**Do not break blisters**, do not apply any ointment, powder or lotion, "
        "and do not use cotton wool or fluffy dressings.",
        "**Treat for shock** \u2014 lay the casualty down, raise the legs, keep "
        "him warm (burns lose heat), reassure, and **give frequent small sips of "
        "cool water or ORS** if he is fully conscious and the burn is not going "
        "to need immediate surgery.",
        "**Monitor the airway** \u2014 hoarse voice, cough, soot round the mouth "
        "or nose, singed nasal hair and breathing difficulty mean **inhalation "
        "injury**: give oxygen if trained and transport at once, sitting up.",
        "Arrange **urgent hospital transfer** for all serious burns; keep the "
        "burnt part **elevated** where possible and record the time, cause, "
        "extent and depth.",
    ])
    b.table(
        ["Special burn", "Additional first aid"],
        [["**Chemical burn**", "Wear gloves; **brush off dry powder first**, "
                               "then flood with copious running water for "
                               "**at least 20 minutes**; remove contaminated "
                               "clothing while flooding; do **not** attempt to "
                               "neutralise acid with alkali or vice-versa; "
                               "identify the chemical for the hospital"],
         ["**Chemical in the eye**", "Irrigate the eye with gently running water "
                                     "for 20 minutes, holding the lids open, "
                                     "with the **affected eye lower** so that "
                                     "the chemical does not run into the other "
                                     "eye; cover and refer"],
         ["**Electrical burn**", "**Isolate the current first**. Look for "
                                 "**entry and exit wounds** (both must be "
                                 "dressed), expect **deep tissue damage, "
                                 "fractures and cardiac arrest**; all "
                                 "electrical burns need hospital assessment"],
         ["**Inhalation / airway burn**", "Move to fresh air, sit the casualty "
                                          "up, loosen clothing, give oxygen if "
                                          "trained, watch for swelling of the "
                                          "throat; transport urgently \u2014 "
                                          "the airway can close within minutes"],
         ["**Sunburn**", "Move into the shade, cool the skin with water or cool "
                         "compresses, give sips of water, apply calamine or "
                         "after-sun lotion; do not break blisters"],
         ["**Friction burn**", "Treat as an abrasion plus a burn \u2014 cool and "
                               "cover"],
         ["**Radiation burn**", "Remove contaminated clothing, wash the skin, "
                                "cover and refer; protect yourself"]],
        weights=[3.0, 9.6])
    b.box("BURNS \u2014 THE CLASSICAL \u2018NEVER\u2019 LIST", [
        "**Never** apply ice or ice-cold water directly (causes further tissue "
        "damage).",
        "**Never** apply oil, ghee, butter, toothpaste, turmeric, ink, mud, cow "
        "dung, egg white, leaves or any home remedy.",
        "**Never** prick or break blisters, and never peel off dead skin.",
        "**Never** use cotton wool, fluffy or adhesive dressings on a burn.",
        "**Never** remove clothing that is stuck to the burn.",
        "**Never** give alcohol, and never give anything by mouth to an "
        "unconscious or severely burnt casualty awaiting surgery.",
        "**Never** cough or breathe over a burn \u2014 burnt skin has lost its "
        "barrier to infection.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Wound = break in the continuity of skin/mucous membrane; three dangers "
        "= **bleeding, infection, shock**.",
        "**Incised** \u2192 bleeds most; **lacerated** \u2192 most infected "
        "edges; **punctured** \u2192 tetanus risk; **contusion** \u2192 closed "
        "wound; **abrasion** \u2192 superficial only.",
        "Treatment order: **stop bleeding \u2192 prevent infection \u2192 "
        "immobilise \u2192 treat shock \u2192 refer**.",
        "Tetanus: ***Clostridium tetani***, anaerobic spore-former, incubation "
        "**7\u201310 days**, toxin **tetanospasmin**, signs **trismus, risus "
        "sardonicus, opisthotonos**.",
        "**Sucking chest wound** \u2192 seal with plastic **taped on three "
        "sides**, half-sitting, leaning to the injured side.",
        "**Protruding intestine** \u2192 knees bent, cover with moist sterile "
        "dressing, **never push back**, nothing by mouth.",
        "**Amputated part** \u2192 dry sterile wrap \u2192 sealed plastic bag "
        "\u2192 bag in ice water; **never directly on ice**.",
        "Burns: cool with running water for **10\u201320 minutes**, cover with "
        "cling film, **never** apply oil/ice/toothpaste, never prick blisters.",
        "**Rule of nines:** head 9, each arm 9, each leg 18, front trunk 18, "
        "back 18, perineum 1; palm = 1 %; in a child, head 18 and each leg 14.",
        "Third-degree burn is **painless, white or charred and dry** \u2014 "
        "always needs hospital care.",
    ])
