# -*- coding: utf-8 -*-
"""Chapter 3 - Dressings and Bandages."""


def render(b):
    b.part("PART II", "Life-Saving Skills")
    b.chapter(
        "Dressings and Bandages",
        "Types of dressing; the triangular bandage and all its folds and slings; "
        "the cotton roller bandage and its turns; the rubber (elastic) bandage; "
        "special bandages, rules, dangers and improvisation.",
        syllabus=[
            "Dressing and Bandages \u2014 use of **triangular bandages** and "
            "**cotton roller bandage**, **rubber bandage** and **different types "
            "of dressing**.",
            "General rules of bandaging, slings, signs of a tight bandage, "
            "improvisation and care of the casualty.",
        ])

    # ------------------------------------------------------------------
    b.h2("Definitions and Purpose")
    b.box("DEFINITIONS", [
        "**Dressing** \u2014 a **protective covering applied directly over a "
        "wound or burn** to arrest bleeding, prevent infection and absorb "
        "discharge. It must be **sterile (or at least clean), absorbent, "
        "porous and larger than the wound** on all sides.",
        "**Bandage** \u2014 a **piece of cloth or material used to hold a "
        "dressing in position**, to apply pressure, to support or immobilise a "
        "part, or to prevent/reduce swelling. A bandage **never** touches the "
        "wound directly.",
        "**Pad** \u2014 thick soft material (cotton wool, folded cloth) placed "
        "over a dressing to apply pressure or to fill a hollow.",
        "**Compress** \u2014 a folded cloth applied wet: **cold compress** "
        "(sprain, bruise, nose bleed) or **hot compress** (boil, pain relief).",
    ], kind="def")
    b.table(
        ["Purpose of a DRESSING", "Purpose of a BANDAGE"],
        [["Controls bleeding by direct pressure.", "Holds the dressing or splint "
                                                   "in position."],
         ["Prevents entry of germs (prevents infection).",
          "Applies **pressure** to control bleeding."],
         ["Absorbs blood and discharge.", "Gives **support** to an injured limb "
                                          "or joint."],
         ["Protects the wound from further injury and from air/dust.",
          "**Immobilises** a fracture, dislocation or wounded part."],
         ["Relieves pain by covering exposed nerve endings.",
          "**Restricts swelling** (compression) and helps reduce it."],
         ["Promotes healing by keeping the wound moist and clean.",
          "Helps in **lifting and carrying** the casualty."]],
        weights=[6.4, 6.4], first_bold=False)

    # ------------------------------------------------------------------
    b.h2("Different Types of Dressing")
    b.table(
        ["Type of dressing", "Description", "Chief uses"],
        [["**Dry sterile (gauze) dressing**",
          "Sterile gauze squares in a sealed packet, covered with a pad of "
          "cotton wool and held by a bandage; the standard first-aid dressing",
          "Most open wounds; absorbs blood and allows the wound to breathe"],
         ["**Adhesive dressing** (Band-Aid, sticking plaster)",
          "Small gauze pad with an adhesive backing, often waterproof",
          "Small clean cuts, abrasions; no separate bandage needed"],
         ["**Sterile (standard/first field) dressing**",
          "A sterile pad already attached to a roller bandage in a sealed "
          "packet; used by the armed forces and ambulance services",
          "Bleeding wounds \u2014 quickest of all dressings; one hand can apply "
          "it"],
         ["**Non-adherent / paraffin (tulle gras) dressing**",
          "Gauze impregnated with paraffin or silicone so that it does not stick",
          "**Burns**, scalds, grazes and raw surfaces \u2014 painless to remove"],
         ["**Medicated dressing**", "Gauze soaked in an antiseptic or medicament "
                                    "(povidone-iodine, silver sulphadiazine, "
                                    "honey, framycetin)",
          "Infected wounds, ulcers, burns \u2014 on medical advice only"],
         ["**Wet (moist) dressing / compress**",
          "Cloth wrung out in cold (or warm) water or saline",
          "Cold: sprains, bruises, stings; warm: to relieve pain and soften "
          "crusts"],
         ["**Pressure dressing**", "Dressing plus a thick pad, firmly bandaged "
                                   "over the wound", "**Severe bleeding**"],
         ["**Occlusive (air-tight) dressing**",
          "Plastic sheet, cling film or a sterile pad taped on three sides "
          "(\u2018flutter valve\u2019)",
          "**Sucking chest wound** (open pneumothorax), exposed abdominal organs"],
         ["**Ring (doughnut) pad**", "A ring made by winding a narrow bandage "
                                     "round the fingers, then binding it",
          "**Embedded foreign body**, protruding bone end, fractured skull "
          "\u2014 pressure is put round, not on, the injury"],
         ["**Eye pad**", "Sterile pad with a bandage or shield",
          "Eye injuries; the **uninjured eye may also be covered** to stop "
          "movement"],
         ["**Improvised dressing**", "Clean handkerchief, freshly laundered "
                                     "linen, towel, sanitary pad, clean cloth; "
                                     "in the last resort the casualty's own "
                                     "clean clothing",
          "When no sterile dressing is at hand \u2014 remember: **any clean "
          "cover is better than none**"],
         ["**Cotton wool**", "Absorbent cotton \u2014 **never placed directly "
                             "on a wound** because its fibres stick to it",
          "Only as padding over a gauze dressing"]],
        weights=[3.0, 5.4, 4.6], first_bold=False, size=8.8)
    b.h3("Rules for applying a dressing")
    b.numbered([
        "**Wash your hands** and wear disposable gloves if available.",
        "Do not touch the wound or the surface of the dressing that will touch "
        "the wound; **hold a dressing by its edges/corners**.",
        "Do not cough, sneeze or breathe over the wound or dressing; **do not "
        "talk** over it.",
        "The dressing must **extend at least 2.5 cm (1 inch) beyond the wound** "
        "on all sides.",
        "Place the dressing **directly on the wound \u2014 do not slide it** "
        "into position.",
        "Add a pad of cotton wool over the gauze and hold it with a bandage or "
        "adhesive strapping.",
        "If blood soaks through, **do not remove the dressing** \u2014 apply "
        "another pad and bandage over it and press firmly.",
        "Do not apply cotton wool, fluffy material or antiseptic powder directly "
        "to a wound; do not use anything sticky on a burn.",
        "Never remove a dressing that has stuck to a wound \u2014 leave that to "
        "the doctor.",
        "Change dressings only when soaked, or as advised; check circulation "
        "beyond the dressing.",
    ])

    # ------------------------------------------------------------------
    b.h2("General Rules of Bandaging")
    b.numbered([
        "**Explain and reassure** \u2014 tell the casualty what you are going to "
        "do.",
        "Make the casualty **sit or lie comfortably** in a well-supported "
        "position; support the injured part while bandaging.",
        "Stand **in front of the casualty** (and on the injured side) so that "
        "you can watch his face for signs of pain.",
        "Bandage the injured part in the **position in which it is to remain** "
        "(joints slightly flexed, not fully straight).",
        "Apply from the **inner to the outer side** and from **below upwards "
        "(distal to proximal)** \u2014 towards the heart \u2014 so that blood is "
        "not trapped in the limb.",
        "Hold the **head (roll) of a roller bandage uppermost/outermost** and "
        "unroll only a little at a time, keeping the roll in the right hand for "
        "a right limb.",
        "Each turn should **overlap the previous one by about two-thirds "
        "(\u00bd\u2013\u2154)** so that no skin shows and the pressure is even.",
        "Bandage **firmly enough to control bleeding or to support, but never so "
        "tightly as to stop circulation**; avoid uneven or slack turns.",
        "**Pad hollows and bony points** (armpit, elbow, knee, ankle, between "
        "fingers) with cotton wool to prevent chafing and to spread pressure.",
        "**Leave the finger tips and toes exposed** whenever possible so that "
        "circulation can be checked.",
        "Finish off by **tucking in the end, or with a reef knot, safety pin, "
        "clip or adhesive tape**; the **knot must not lie over a wound, a bony "
        "point, or the back of a part on which the casualty will lie**.",
        "Use a **reef knot** \u2014 it is flat, secure and easy to untie.",
        "**Check circulation** immediately after applying and again every "
        "**10 minutes**; loosen at once if there are signs of tightness.",
        "Avoid bandaging **over a fresh wound with unequal pressure**; never "
        "apply a wet bandage that will shrink on drying.",
        "In fractures, bandages must be applied **above and below the fracture "
        "site \u2014 never over it**.",
        "Remove or replace a bandage that becomes loose, soiled or wet.",
    ])
    b.box("SIGNS THAT A BANDAGE IS TOO TIGHT \u2014 LOOSEN AT ONCE (mnemonic: "
          "the 5 P's + 1)", [
        "**P**ain \u2014 throbbing or increasing pain beyond the bandage.",
        "**P**allor \u2014 the part becomes pale, then **blue (cyanosed)**.",
        "**P**ulselessness \u2014 no pulse beyond the bandage.",
        "**P**araesthesia \u2014 tingling, \u2018pins and needles\u2019, "
        "numbness.",
        "**P**aralysis \u2014 inability to move the fingers or toes.",
        "**Coldness and swelling** of the part; **capillary refill of the nail "
        "bed slower than 2 seconds** (press the nail: colour should return "
        "at once).",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Types of Bandage \u2014 Overview")
    b.table(
        ["Bandage", "Material / form", "Chief use"],
        [["**Triangular bandage**", "Cotton cloth **1 m \u00d7 1 m square cut "
                                    "diagonally into two triangles**",
          "Slings, holding dressings, immobilising, improvised pads and "
          "tourniquets \u2014 the most versatile first-aid bandage"],
         ["**Roller bandage (cotton/open-weave)**",
          "A long strip of cotton, gauze or flannel rolled up; widths "
          "2.5\u201315 cm", "Holding dressings, support, pressure over a "
                            "dressing, immobilisation"],
         ["**Rubber / elastic (crepe) bandage**",
          "Woven cotton with rubber or elastic threads; stretches",
          "Firm support and compression for sprains, strains, varicose veins, "
          "swelling"],
         ["**Adhesive bandage / strapping**", "Zinc-oxide plaster, micropore "
                                              "tape, adhesive strips",
          "Fixing dressings, strapping ribs/joints, closing small wounds"],
         ["**Tubular gauze / net bandage**", "Seamless tube applied with an "
                                             "applicator", "Fingers, toes, "
                                                           "head, limbs"],
         ["**Special (shaped) bandages**", "T-bandage, four-tailed, many-tailed "
                                           "(Scultetus), suspensory, capeline",
          "Perineum, jaw, abdomen, scrotum, scalp"],
         ["**Plaster of Paris**", "Bandage impregnated with gypsum, applied wet",
          "Hospital immobilisation of fractures \u2014 **not** a first-aid "
          "measure"]],
        weights=[3.0, 4.6, 5.4], first_bold=False, size=8.8)

    # ------------------------------------------------------------------
    b.h2("The Triangular Bandage")
    b.p("Introduced by **Esmarch**, the triangular bandage is the first aider's "
        "most useful single article. It is made by cutting a **square metre of "
        "cloth (about 38\u201340 inches) diagonally**, giving two bandages; "
        "the two short sides measure about **1 m** each and the long side (base) "
        "about **1.3\u20131.4 m**.")
    b.h3("Parts of a triangular bandage")
    b.bullets([
        "**Point** \u2014 the corner opposite the base (the apex).",
        "**Base** \u2014 the longest side.",
        "**Ends (extremities)** \u2014 the two corners at either end of the base.",
        "**Sides** \u2014 the two shorter borders.",
    ])
    b.h3("The three forms (folds) of a triangular bandage")
    b.table(
        ["Form", "How it is made", "Uses"],
        [["**Open (whole) bandage**", "Used unfolded, as a triangle",
          "**Slings**; large dressings of the **scalp, chest, back, hand, foot, "
          "hip/buttock and stump**"],
         ["**Broad-fold bandage**", "Bring the **point down to the base**, then "
                                    "fold **once more** in the same direction "
                                    "\u2014 gives a band about 15\u201320 cm "
                                    "wide",
          "**Immobilising and supporting** \u2014 securing splints, tying legs "
          "together, fractures of the thigh/leg, chest and rib injuries"],
         ["**Narrow-fold bandage**", "Fold the **broad bandage once again** "
                                     "lengthwise \u2014 a band about 7\u201310 "
                                     "cm wide",
          "**Figure-of-eight bandage of the ankle/foot**, fixing dressings, "
          "improvised **tourniquet**, tying feet together, making a **ring "
          "pad**, collar-and-cuff sling"]],
        weights=[2.7, 5.0, 5.3], first_bold=False)
    b.bullets([
        "A **cravat** is another name for the narrow-fold (or broad-fold) "
        "bandage.",
        "To store a triangular bandage, fold the ends to the centre repeatedly "
        "and then fold in half \u2014 it becomes a small packet for the kit.",
        "Always finish with a **reef knot**; place a pad under the knot if it "
        "presses on a bony point.",
    ])
    b.h3("Uses of the triangular bandage \u2014 complete list")
    b.table(
        ["Application", "Method in brief"],
        [["**Arm (large/St John) sling**",
          "For injuries of the **forearm, wrist and hand**, and for fractured "
          "ribs. Support the forearm **across the chest, hand slightly higher "
          "than the elbow**. Place the open bandage between the chest and "
          "forearm, point towards the elbow of the injured side; bring the lower "
          "end up over the shoulder and tie the two ends in the **hollow above "
          "the collar bone on the injured side**; tuck or pin the point in front "
          "of the elbow. Finger tips must be visible."],
         ["**Elevation sling**",
          "For **hand injuries with bleeding, fractured collar bone, crushed "
          "hand, injured shoulder** \u2014 keeps the hand well raised to reduce "
          "bleeding and swelling. Place the casualty's forearm diagonally across "
          "the chest, **fingers towards the opposite shoulder**; lay the bandage "
          "over the forearm with one end over the sound shoulder; tuck the base "
          "under the hand and forearm; bring the lower part under the elbow and "
          "across the back; tie at the hollow of the neck; twist and tuck the "
          "point in at the elbow."],
         ["**Collar-and-cuff (clove-hitch) sling**",
          "A **narrow-fold** bandage tied as a clove hitch round the wrist and "
          "the ends taken round the neck \u2014 used for a **fractured "
          "humerus/upper arm** where the weight of the arm should hang, and when "
          "a full sling cannot be applied."],
         ["**Triangular (improvised) sling**",
          "Made with the casualty's coat, jacket, shirt front, belt, tie, "
          "scarf, dupatta or by pinning the sleeve to the clothing."],
         ["**Scalp / head dressing (capelline)**",
          "Fold a hem along the base; place the base on the forehead just above "
          "the eyebrows with the point hanging down the back; cross the ends "
          "behind the head over the point, bring them round the forehead and tie "
          "in front; then draw the point down and pin it up on top."],
         ["**Chest / back**", "Place the point over the shoulder on the injured "
                              "side, base across the chest; tie the two ends at "
                              "the back, leaving one end long, and tie that end "
                              "to the point."],
         ["**Hand**", "Lay the hand palm-down on the open bandage with the wrist "
                      "on the base and fingers towards the point; fold the point "
                      "over the back of the hand; cross the ends over the wrist "
                      "and tie."],
         ["**Foot**", "Place the foot on the centre of the bandage with the heel "
                      "towards the base; bring the point over the instep, fold "
                      "the sides over and tie the ends round the ankle."],
         ["**Knee / elbow**", "Point placed on the thigh (or upper arm), base "
                              "below the joint; cross the ends behind the joint, "
                              "bring them up and tie; bring the point down and "
                              "pin."],
         ["**Hip / buttock**", "Tie a narrow-fold bandage round the waist; apply "
                               "the open bandage with the point tucked under "
                               "the waist band and the base round the thigh."],
         ["**Shoulder**", "Point up the side of the neck, base folded over the "
                          "upper arm; tie the ends on the outer side of the arm "
                          "and fix the point under a sling."],
         ["**Stump (amputation)**", "Cover the stump with the point brought over "
                                    "the end; cross the ends round the stump and "
                                    "tie; pin the point."],
         ["**Other uses**", "As a **broad bandage** to tie splints or legs "
                            "together; as a **narrow bandage** for a "
                            "figure-of-eight ankle bandage; as a **ring pad**, "
                            "a **cold compress**, an **eye pad cover**, an "
                            "improvised **tourniquet**, a sling for carrying, "
                            "a filter/mask, and to tie a casualty to a "
                            "stretcher."]],
        weights=[2.6, 10.0], size=8.8)
    b.box("SLINGS \u2014 THE MOST-ASKED COMPARISON", [
        "**Arm sling** \u2014 supports the forearm **horizontally/slightly "
        "raised**; for forearm, wrist and hand injuries and fractured ribs; "
        "hand is **slightly above the level of the elbow**.",
        "**Elevation sling** \u2014 the hand is placed near the **opposite "
        "shoulder (well above the heart)**; for **bleeding hand injuries, "
        "fractured collar bone and injured shoulder**.",
        "**Collar-and-cuff sling** \u2014 supports only the **wrist**, letting "
        "the arm hang; for a **fractured upper arm (humerus)**.",
        "In every sling the knot is tied in the **hollow above the collar bone "
        "on the injured side** and the **finger tips are left exposed**.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("The Cotton Roller Bandage")
    b.p("A roller bandage is a strip of cotton, open-weave gauze, flannel or "
        "calico rolled into a cylinder. It is the commonest bandage for holding "
        "dressings and giving support.")
    b.h3("Parts of a roller bandage")
    b.bullets([
        "**Head (roll)** \u2014 the rolled-up portion held in the hand.",
        "**Tail (free end)** \u2014 the loose end applied first.",
        "**Body** \u2014 the portion being unrolled.",
        "A **single-headed** bandage is rolled from one end; a "
        "**double-headed** bandage is rolled from both ends towards the middle "
        "(used for the head and jaw).",
    ])
    b.h3("Standard widths \u2014 which size for which part")
    b.table(
        ["Part of the body", "Width of bandage"],
        [["Finger", "**2.5 cm (1 inch)**"],
         ["Hand", "**5 cm (2 inches)**"],
         ["Arm / forearm", "**5\u20136 cm (2\u20132\u00bd inches)**"],
         ["Leg (lower limb)", "**7.5\u20139 cm (3\u20133\u00bd inches)**"],
         ["Trunk, chest, abdomen, thigh", "**10\u201315 cm (4\u20136 inches)**"],
         ["Head / scalp", "**5\u20137.5 cm**"],
         ["Usual length", "5\u20136 metres (bandages are supplied "
                          "3\u201310 m long)"]],
        weights=[4.4, 5.0])
    b.h3("Basic turns of a roller bandage \u2014 learn the table")
    b.table(
        ["Turn", "How it is done", "Where it is used"],
        [["**Simple / circular turn**", "Turns laid exactly one over the other, "
                                        "at right angles to the limb",
          "To begin and end every bandage; for **wrist, neck and finger** and "
          "for holding a dressing on a uniform part"],
         ["**Spiral turn**", "Turns run obliquely up the limb, each overlapping "
                             "the previous by two-thirds",
          "Parts of **uniform thickness** \u2014 fingers, upper arm, trunk"],
         ["**Reverse spiral (spiral reverse)**", "Each spiral turn is **twisted "
                                                 "(reversed) on itself** with "
                                                 "the thumb to make it lie flat",
          "**Tapering (cone-shaped) parts** \u2014 **forearm and leg**"],
         ["**Figure-of-eight turn**", "Ascending and descending oblique turns "
                                      "crossing each other in the form of the "
                                      "figure 8",
          "**Joints** \u2014 elbow, knee, **ankle**, wrist; gives firm support"],
         ["**Spica**", "A modified figure-of-eight in which the turns overlap "
                       "like the husk of an ear of corn",
          "**Shoulder, hip, groin and thumb** (\u2018thumb spica\u2019)"],
         ["**Divergent spica**", "Turns pass alternately above and below the "
                                 "joint, diverging from the centre",
          "Over a **flexed elbow or knee**"],
         ["**Recurrent turn**", "Turns are carried backwards and forwards over "
                                "the end of the part and then fixed by circular "
                                "turns", "**Finger tip, stump of an amputated "
                                         "limb, head**"],
         ["**Locking/anchoring turn**", "First turn placed obliquely, its corner "
                                        "turned down and covered by the next "
                                        "turn", "To fix the beginning of any "
                                                "bandage"]],
        weights=[2.7, 5.0, 5.3], first_bold=False, size=8.8)
    b.h3("Method of applying a roller bandage")
    b.numbered([
        "Choose the **correct width** for the part; use a **firmly rolled** "
        "bandage.",
        "Face the casualty; support the limb in the position it is to remain.",
        "Hold the **roll upwards in the right hand** for a right limb and place "
        "the **outer surface of the tail on the part, below the injury**.",
        "Make **two firm circular (anchoring) turns** to fix the tail.",
        "Bandage **upwards and from within outwards**, each turn covering "
        "**two-thirds** of the previous one.",
        "Use the turn suited to the part (spiral, reverse spiral, "
        "figure-of-eight, spica or recurrent).",
        "Finish with **one or two circular turns** and fasten with a safety pin, "
        "clip, adhesive tape, or by splitting the end and tying a reef knot.",
        "**Check the circulation** of the fingers/toes at once and again after "
        "10 minutes.",
    ])
    b.h3("Particular applications")
    b.dl([
        ("Finger", "Anchor at the wrist, carry to the finger, apply spiral "
                   "turns, finish with a figure-of-eight round the wrist "
                   "(so it cannot slip off)."),
        ("Hand and wrist", "Anchor at the wrist, cross the palm, "
                           "figure-of-eight turns round the hand, leaving the "
                           "thumb free; finish at the wrist."),
        ("Elbow / knee", "Flex the joint slightly; apply a figure-of-eight or "
                         "divergent spica with the crossing over the front of "
                         "the elbow (back of the knee is padded)."),
        ("Ankle and foot", "Begin with a circular turn round the instep, carry "
                           "the bandage in **figure-of-eight turns round the "
                           "ankle** and finish above the ankle."),
        ("Leg / forearm", "Reverse spiral turns from below upwards."),
        ("Scalp / head", "Circular turns round the forehead and occiput, or a "
                         "double-headed bandage; secure at the side."),
        ("Stump", "Recurrent turns over the end, then circular turns."),
    ])

    # ------------------------------------------------------------------
    b.h2("The Rubber (Elastic / Crepe) Bandage")
    b.p("A rubber bandage is made of cotton woven with **rubber or elastic "
        "threads**, so that it **stretches and grips** the part and exerts "
        "continuous, even pressure. The historical **Esmarch's rubber bandage** "
        "was used to squeeze blood out of a limb before surgery and as a "
        "tourniquet.")
    b.h3("Uses of a rubber/elastic bandage")
    b.bullets([
        "**Firm support and compression** of a **sprain, strain or bruise** "
        "(the \u2018C\u2019 of the **RICE** treatment \u2014 Rest, Ice, "
        "Compression, Elevation).",
        "To **reduce and prevent swelling (oedema)** after injury, and to "
        "prevent re-accumulation.",
        "Support for **varicose veins**, for **thrombosis prophylaxis** and for "
        "**venous ulcers** (elastic/crepe compression bandage).",
        "Support to a **joint or muscle during and after activity**, and over a "
        "**plaster-free mild fracture** while awaiting medical help.",
        "**Firm pressure over a dressing** in bleeding, and to hold splints and "
        "dressings on rounded or moving parts (the stretch keeps it in place).",
        "Application over a **snake-bitten limb** as a *pressure immobilisation "
        "bandage* (firm, as for a sprained ankle, plus a splint) \u2014 in "
        "current practice done with a crepe/elastic bandage, **never a "
        "tourniquet**.",
        "As an **emergency tourniquet or Esmarch bandage by medical personnel** "
        "only.",
    ])
    b.h3("Advantages, precautions and dangers")
    b.table(
        ["Advantages", "Precautions / dangers"],
        [["Stretches, so it fits rounded and moving parts and does not slip.",
          "It is **easy to apply too tightly** \u2014 the commonest cause of a "
          "constricted limb; never stretch it to its full length."],
         ["Gives continuous, even and adjustable compression.",
          "Must be applied **evenly from the toes/fingers upwards**, never "
          "leaving a tight ring."],
         ["Washable and reusable.", "**Never use on an open, dirty or infected "
                                    "wound** as the only cover, and never "
                                    "directly over a burn."],
         ["Comfortable and allows some movement.",
          "**Do not leave on overnight** or during sleep; remove and re-apply "
          "every few hours; check circulation every 10\u201315 minutes at first."],
         ["Can be used over dressings and splints.",
          "Contra-indicated where circulation is already poor "
          "(arterial disease, diabetic limb) and in an **unsplinted fracture**."]],
        weights=[6.0, 6.8], first_bold=False)
    b.box("CREPE / RUBBER BANDAGE vs COTTON ROLLER BANDAGE", [
        "**Cotton roller** \u2014 non-elastic; holds dressings and gives "
        "moderate support; cheap; absorbs discharge; can loosen with movement.",
        "**Crepe / rubber** \u2014 elastic; gives **compression and firm "
        "support**; does not absorb; stays in place on joints; but carries a "
        "**greater risk of over-tightness**.",
        "For a **sprained ankle** the bandage of choice is a **crepe bandage "
        "in figure-of-eight turns**.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Special and Improvised Bandages")
    b.table(
        ["Bandage", "Shape and use"],
        [["**T-bandage (single/double T)**", "A horizontal band with one or two "
                                             "vertical tails \u2014 holds "
                                             "dressings on the **perineum, "
                                             "groin and anus**"],
         ["**Four-tailed bandage**", "A strip split at both ends \u2014 for the "
                                     "**chin/jaw, nose, back of the head, "
                                     "elbow, knee**"],
         ["**Many-tailed (Scultetus) bandage**", "Overlapping tails stitched to "
                                                 "a central band \u2014 for the "
                                                 "**abdomen and chest**, where "
                                                 "re-application must be easy"],
         ["**Capeline bandage**", "A double-headed bandage for the **scalp/whole "
                                  "head**"],
         ["**Suspensory bandage**", "Supports the **scrotum**"],
         ["**Tubular gauze**", "Seamless tube pushed on with an applicator "
                               "\u2014 fingers, toes, limbs, head"],
         ["**Adhesive strapping**", "Fixes dressings, supports sprains, strapping "
                                    "of fractured ribs (rarely used now)"],
         ["**Improvised bandages**", "Handkerchief, dupatta, scarf, necktie, "
                                     "belt, stockings, torn bed sheet, towel, "
                                     "shawl, rope (padded), bark, clothing "
                                     "\u2014 **the first aider improvises "
                                     "rather than delays**"],
         ["**Improvised splints**", "Umbrella, walking stick, broom, cricket bat, "
                                    "rolled newspaper/magazine, cardboard, "
                                    "wooden plank, pillow, folded blanket; the "
                                    "casualty's own **sound limb or the trunk** "
                                    "can also serve as a splint"]],
        weights=[3.0, 9.6])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "**Dressing touches the wound; bandage holds the dressing.** A dressing "
        "must be sterile, absorbent and larger than the wound by 2.5 cm.",
        "Triangular bandage = **1 m square cut diagonally**; parts = point, "
        "base, ends, sides; forms = **open, broad-fold, narrow-fold**.",
        "**Arm sling** \u2192 forearm/wrist/ribs; **elevation sling** \u2192 "
        "bleeding hand, fractured collar bone; **collar-and-cuff** \u2192 "
        "fractured humerus.",
        "Roller bandage widths: finger **2.5 cm**, hand **5 cm**, arm **5\u20136 "
        "cm**, leg **7.5\u20139 cm**, trunk **10\u201315 cm**.",
        "Turns: circular (start/finish), spiral (uniform part), **reverse spiral "
        "(forearm/leg)**, **figure-of-eight (joints/ankle)**, spica "
        "(shoulder/hip/thumb), recurrent (stump/finger tip).",
        "Bandage **from below upwards, inner to outer**, overlapping **two-thirds**; "
        "tie with a **reef knot**; keep finger tips visible.",
        "Tight bandage = **pain, pallor, pulselessness, paraesthesia, paralysis, "
        "coldness and blueness** \u2192 **loosen immediately**.",
        "**Rubber/crepe bandage** = compression and support (sprains, varicose "
        "veins, RICE); greatest danger is over-tightness.",
        "**Cotton wool must never be placed directly on a wound**; never remove "
        "a blood-soaked dressing \u2014 add another over it.",
    ])
