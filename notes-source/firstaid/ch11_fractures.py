# -*- coding: utf-8 -*-
"""Chapter 11 - Fractures and Dislocations."""


def render(b):
    b.chapter(
        "Fractures and Dislocations",
        "Types and signs of fractures, general and special management, splints "
        "and immobilisation, fractures of individual bones, dislocations, "
        "sprains and strains.",
        syllabus=[
            "Fractures \u2014 definition, causes, classification and types, "
            "signs and symptoms, complications and complete first-aid "
            "management; splints and immobilisation.",
            "Fractures of the skull, jaw, spine, ribs, collar bone, arm, "
            "forearm, hand, pelvis, thigh, knee, leg and foot.",
            "Dislocation \u2014 definition, common sites, signs, management; "
            "sprain and strain and the RICE treatment; difference between "
            "fracture, dislocation, sprain and strain.",
        ])

    # ------------------------------------------------------------------
    b.h2("Definition and Causes of Fracture")
    b.box("DEFINITION", [
        "A **fracture** is a **break or crack in the continuity of a bone** "
        "(or of a cartilage).",
        "**Causes \u2014 three mechanisms:**  "
        "**(1) Direct violence** \u2014 the bone breaks at the exact spot where "
        "the force is applied (a blow, a bullet, a wheel passing over a limb).  "
        "**(2) Indirect violence** \u2014 the bone breaks at a distance from the "
        "point of impact (falling on the outstretched hand breaks the **collar "
        "bone or wrist**; falling from a height on the feet fractures the "
        "**spine**).  "
        "**(3) Muscular action** \u2014 a violent muscle pull snaps the bone "
        "(fracture of the **patella** or of a vertebral process while throwing, "
        "or during a fit).",
        "Contributory factors: **old age and osteoporosis, rickets, bone "
        "tumour/cyst, long-standing disease (pathological fracture), repeated "
        "stress (stress fracture in athletes and soldiers), and the softness of "
        "a child's bone (greenstick)**.",
    ], kind="def")

    # ------------------------------------------------------------------
    b.h2("Types of Fracture")
    b.table(
        ["Type", "Description", "Significance"],
        [["**Simple (closed) fracture**", "The bone is broken but the **skin "
                                         "over it is intact** \u2014 no wound "
                                         "communicating with the fracture",
          "Less risk of infection; still bleeds internally"],
         ["**Compound (open) fracture**", "There is a **wound leading down to "
                                         "the fracture**, or the bone end "
                                         "protrudes through the skin; may also "
                                         "communicate with a body cavity",
          "**More dangerous** \u2014 severe bleeding and a high risk of "
          "**infection, including tetanus and gas gangrene**"],
         ["**Complicated fracture**", "The fracture is associated with **injury "
                                     "to an important structure** \u2014 a "
                                     "large blood vessel, nerve, joint, or an "
                                     "organ such as the brain, lung, liver, "
                                     "spleen, bladder or spinal cord",
          "Needs the most urgent hospital care; may cause paralysis or internal "
          "bleeding"],
         ["**Comminuted fracture**", "The bone is broken into **more than two "
                                     "pieces (crushed/splintered)**",
          "Common in crush and road injuries; difficult to set"],
         ["**Greenstick fracture**", "An **incomplete** break \u2014 the bone "
                                     "bends and cracks on one side only, like a "
                                     "green twig",
          "Occurs **only in children**, whose bones are soft and elastic"],
         ["**Impacted fracture**", "One broken end is **driven firmly into the "
                                   "other**",
          "Common at the neck of the femur and the wrist in the elderly; may "
          "allow limited use, so it is easily missed"],
         ["**Depressed fracture**", "A piece of bone is **driven inwards**",
          "Typically of the **skull** \u2014 presses on the brain"],
         ["**Transverse / oblique / spiral fracture**", "The line of break runs "
                                                       "straight across / "
                                                       "obliquely / in a spiral "
                                                       "round the bone",
          "Spiral fractures follow a **twisting** force"],
         ["**Avulsion fracture**", "A fragment is **pulled off** by a tendon or "
                                   "ligament", "Seen at the ankle, finger and "
                                               "pelvis"],
         ["**Pathological fracture**", "A **diseased bone** (tumour, cyst, "
                                       "tuberculosis, osteoporosis) breaks with "
                                       "little or no force",
          "Suspect in the elderly or in cancer patients"],
         ["**Stress (fatigue) fracture**", "A hairline crack from **repeated "
                                           "overuse**", "Long marches, running, "
                                                        "sports \u2014 the "
                                                        "metatarsals and tibia"],
         ["**Fissured / hairline fracture**", "A mere crack, with no "
                                              "displacement", "Easily missed on "
                                                              "examination"],
         ["**Fracture-dislocation**", "A fracture close to a joint **with "
                                      "dislocation** of that joint",
          "Shoulder, ankle, hip \u2014 needs hospital reduction"]],
        weights=[3.0, 5.0, 4.6], size=8.6)
    b.box("MOST-ASKED DISTINCTIONS", [
        "Skin **intact** = **simple/closed**; skin **broken over the fracture** "
        "= **compound/open** \u2014 the most dangerous because of infection and "
        "bleeding.",
        "Bone in **more than two pieces** = **comminuted**.",
        "Fracture **only in children, bone bent and cracked on one side** = "
        "**greenstick**.",
        "Fracture with **injury to a nerve, vessel or organ** = **complicated**.",
        "One end **driven into the other** = **impacted**; piece **driven "
        "inwards** = **depressed** (skull).",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Signs and Symptoms of a Fracture")
    b.p("Learn the table below; of all the signs, ==deformity, crepitus, "
        "unnatural movement and loss of function are the most significant==, "
        "while **localised tenderness is the most constant**.")
    b.table(
        ["Sign / symptom", "Explanation"],
        [["**Pain and tenderness**", "Sharp pain at the site, made worse by "
                                    "movement; **localised tenderness on gentle "
                                    "pressure** is the most reliable sign"],
         ["**Loss of power / function**", "The casualty cannot use the part, "
                                          "cannot bear weight or lift the limb"],
         ["**Swelling and bruising**", "From bleeding into the tissues; appears "
                                       "within minutes to hours and may mask "
                                       "deformity"],
         ["**Deformity**", "The limb looks **bent, twisted, shortened or out of "
                           "the normal line**; compare with the sound limb"],
         ["**Crepitus (bony grating)**", "A grating sound or feeling when the "
                                         "broken ends rub \u2014 **never test "
                                         "for it deliberately**, it causes pain "
                                         "and further damage"],
         ["**Irregularity**", "A step, gap or bony point felt along the bone; "
                              "the bone end may be visible in an open fracture"],
         ["**Unnatural movement**", "Movement where there should be none"],
         ["**Signs of shock**", "Pale, cold, clammy skin with a rapid weak pulse "
                                "\u2014 marked in fractures of the femur and "
                                "pelvis"],
         ["**History / the casualty's own account**", "A snap may have been "
                                                     "heard or felt; the "
                                                     "mechanism of injury "
                                                     "suggests the fracture"]],
        weights=[3.4, 9.2])
    b.box("REMEMBER", [
        "**Always suspect a fracture** if the mechanism of injury or the "
        "casualty's account suggests one \u2014 **treat as a fracture until "
        "an X-ray proves otherwise**.",
        "A fracture is **not** necessarily painful at first (shock, alcohol, an "
        "impacted fracture), and the casualty may even walk on a fractured bone.",
        "**Never move a casualty to look for a fracture** and never test the "
        "movement of a suspected fracture.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Complications of Fractures")
    b.table(
        ["Immediate / early", "Late"],
        [["**Severe bleeding** \u2014 a fractured femur can bleed 1\u20132 "
          "litres, the pelvis 2\u20133 litres", "**Delayed union, non-union or "
                                                "mal-union** of the bone"],
         ["**Shock** \u2014 from blood loss and pain",
          "**Stiffness of joints, muscle wasting, shortening** of the limb"],
         ["**Injury to nerves** \u2014 numbness, tingling, paralysis "
          "(e.g. radial nerve with a humerus fracture)",
          "**Avascular necrosis** (death of bone \u2014 head of the femur, "
          "scaphoid)"],
         ["**Injury to blood vessels** \u2014 loss of pulse, cold pale limb "
          "\u2192 **gangrene**", "**Osteomyelitis** (bone infection) after an "
                                 "open fracture"],
         ["**Injury to organs** \u2014 brain (skull), lung (ribs), bladder and "
          "urethra (pelvis), spinal cord (spine)",
          "**Myositis ossificans, arthritis** of the neighbouring joint"],
         ["**Infection, tetanus and gas gangrene** in open fractures",
          "**Volkmann's ischaemic contracture** (after elbow fractures)"],
         ["**Fat embolism** \u2014 fat from the marrow enters the blood, causing "
          "breathlessness and confusion 24\u201372 hours later",
          "**Compartment syndrome** \u2014 increasing pain, tense swelling, "
          "numbness, loss of pulse; an emergency"],
         ["**Crush syndrome** and kidney failure after prolonged compression",
          "**Deep-vein thrombosis and pulmonary embolism** from immobility"]],
        weights=[6.4, 6.4], first_bold=False, size=8.8)

    # ------------------------------------------------------------------
    b.h2("General First-Aid Management of Fractures")
    b.box("GOLDEN RULES OF FRACTURE FIRST AID", [
        "**\u2018Treat the casualty where he lies\u2019** \u2014 do not move him "
        "unless there is danger, and never until the fracture is immobilised.",
        "**Steady and support** the injured part with your hands at once, above "
        "and below the fracture, until it is immobilised.",
        "**Immobilise the fracture before moving the casualty**; immobilise "
        "**the joints above and below** the fracture.",
        "**Never attempt to reduce (set) a fracture** or push a protruding bone "
        "back.",
        "**Never test for crepitus**, never make the casualty walk or move the "
        "part to \u2018see if it is broken\u2019.",
        "**Treat bleeding and cover open wounds first**, then immobilise.",
        "**Nothing by mouth** \u2014 surgery and anaesthesia are likely.",
    ], kind="warn")
    b.numbered([
        "**Reassure** the casualty and tell him to keep still.",
        "**Steady and support** the injured limb with your hands; a helper "
        "maintains gentle support throughout.",
        "**Check and treat the airway, breathing and severe bleeding first** "
        "(a fracture is never treated before a life-threat).",
        "**Open (compound) fracture:** cover the wound with a **sterile "
        "dressing**, control bleeding by pressure **around** the wound, place a "
        "**ring pad** round any protruding bone and bandage over the pads "
        "\u2014 **never press on the bone end** and never push it in.",
        "**Immobilise** the fracture in the most comfortable position: by "
        "**bandaging the injured limb to a sound part of the body** (arm to "
        "chest, injured leg to the sound leg) or by applying a **splint**.",
        "Apply **broad-fold bandages above and below the fracture \u2014 never "
        "over it**; tie the knots on the **uninjured side** (or over the splint).",
        "**Pad hollows and bony points** (ankle, knee, armpit, between the "
        "legs) with cotton wool, folded cloth or a small cushion.",
        "**Raise and support** the injured part after immobilising, where "
        "possible, to reduce swelling; apply a **cold compress** over a closed "
        "fracture through cloth.",
        "**Check the circulation beyond the bandages** immediately and every 10 "
        "minutes \u2014 feel the pulse, look for pallor, blueness, coldness, "
        "tingling and numbness; **loosen at once** if any of these appear.",
        "**Treat for shock** \u2014 lie the casualty down, keep him warm, "
        "reassure; do **not** raise the legs if a leg is fractured.",
        "**Transport** carefully, on a stretcher for lower-limb, pelvic, spinal "
        "or multiple fractures; record the time and findings, and hand over to "
        "the doctor.",
    ])
    b.h3("Splints \u2014 the rules of immobilisation")
    b.bullets([
        "A **splint** is a rigid or semi-rigid support applied to hold a "
        "fractured bone still. **Types:** wooden (Thomas splint, Cramer wire, "
        "Bohler), inflatable (air splint), moulded plastic/vacuum splints, "
        "cardboard, and the **body's own \u2018anatomical splint\u2019** (the "
        "sound limb or the trunk).",
        "**Improvised splints:** umbrella, walking stick, broom, cricket bat, "
        "bamboo, rolled newspaper or magazine, thick cardboard, wooden plank, "
        "pillow, folded blanket, rifle, hockey stick.",
        "**A splint must be: (a) rigid, (b) well padded, (c) long enough to "
        "immobilise the joints above and below the fracture, and (d) applied "
        "over clothing** and secured firmly with broad bandages \u2014 but not "
        "so tightly as to stop circulation.",
        "**Never apply a bandage directly over the fracture site**; use at least "
        "**two** ties, one above and one below the fracture.",
        "Check the **colour, warmth, sensation and pulse** of the fingers/toes "
        "before and after splinting.",
        "In the field, **body bandaging** (tying the injured limb to the trunk or "
        "to the sound limb) is usually quicker and sufficient.",
    ])

    # ------------------------------------------------------------------
    b.h2("Fractures of Individual Bones")
    b.table(
        ["Fracture", "Recognition", "First aid"],
        [["**Skull (vault and base)**",
          "Wound or bruise of the scalp, soft/boggy swelling or a depression; "
          "**bleeding or clear straw-coloured fluid (CSF) from the ear or "
          "nose**; **bruising round the eyes (\u2018panda eyes\u2019) or behind "
          "the ear (Battle's sign)**; blood-shot eye; unconsciousness, unequal "
          "pupils, vomiting, fits; deteriorating level of response",
          "Do **not** press on the injury; use a **ring pad** for scalp "
          "bleeding; if unconscious and breathing, **recovery position with the "
          "bleeding ear downwards**; **never plug the ear or nose**; keep the "
          "head and neck in line; nothing by mouth; monitor level of response "
          "every 10 minutes; urgent hospital transfer"],
         ["**Lower jaw (mandible)**",
          "Pain on speaking and swallowing, dribbling of blood-stained saliva, "
          "irregular teeth or a step in the jaw line, difficulty in opening or "
          "closing the mouth",
          "**Do not bandage the jaw if the casualty is drowsy or bleeding into "
          "the mouth** (risk of choking); let him support the jaw with a soft "
          "pad in his own hand; if fully conscious apply a **narrow-fold bandage "
          "under the chin and over the top of the head**; sit him up with the "
          "head forward to let blood and saliva drain; nothing by mouth"],
         ["**Spine (vertebral column) \u2014 the most dangerous fracture**",
          "Fall from a height, diving accident, heavy blow on the back, road "
          "accident. **Pain in the neck or back, tenderness over the spine; "
          "loss of feeling, tingling or \u2018pins and needles\u2019; weakness "
          "or paralysis of the limbs; inability to move the legs; loss of "
          "control of bladder and bowel; difficulty in breathing** (high "
          "cervical injury)",
          "==Do NOT move the casualty at all== unless life is in danger. "
          "**Steady and support the head in the neutral position** with both "
          "hands (manual in-line stabilisation), place rolled blankets/sandbags "
          "along the body, maintain the airway with a **jaw thrust**, and wait "
          "for the ambulance. If the casualty must be turned or lifted, use the "
          "**log-roll with 4\u20135 helpers and a scoop/spine board**, keeping "
          "the **head, neck and trunk in one straight line**"],
         ["**Ribs (and flail chest)**",
          "Sharp pain at the site, worse on breathing, coughing or moving; "
          "shallow breathing; tenderness; in **multiple fractures**, "
          "**paradoxical breathing** (the injured part moves **in** on "
          "inspiration and **out** on expiration); coughing of frothy blood "
          "means lung injury",
          "Simple fracture: support the arm of the injured side in an **arm "
          "sling** and let the casualty **sit in the position he finds easiest**; "
          "do **not** strap the chest tightly. Multiple/flail/penetrating "
          "injury: **half-sitting, leaning towards the injured side**, cover any "
          "open wound (three-sided dressing), oxygen if trained, urgent "
          "transfer; nothing by mouth"],
         ["**Collar bone (clavicle)** \u2014 the commonest fracture",
          "Fall on the shoulder or outstretched hand; pain, the casualty "
          "**supports the elbow of the affected side and leans the head "
          "towards it**; swelling or a step felt over the collar bone; shoulder "
          "appears dropped",
          "Place the arm of the injured side in an **elevation sling** (or a "
          "**St John/arm sling** if elevation is too painful), and secure the "
          "arm to the chest with a **broad-fold bandage** tied on the sound "
          "side; pad the armpit"],
         ["**Upper arm (humerus)**",
          "Pain, swelling, deformity of the upper arm; the arm cannot be raised; "
          "may injure the **radial nerve** (wrist drop)",
          "Pad the armpit, support the forearm in a **collar-and-cuff sling** so "
          "that the weight of the arm acts as traction, and secure the upper arm "
          "to the chest with a broad-fold bandage above and below the fracture; "
          "a padded splint may be added on the outer side"],
         ["**Forearm (radius and ulna) and wrist**",
          "Pain, swelling, deformity; a **\u2018dinner-fork\u2019 deformity at "
          "the wrist (Colles' fracture)** in the elderly after a fall on the "
          "outstretched hand",
          "Support the forearm with a **well-padded splint from elbow to "
          "fingers** (rolled newspaper/magazine is ideal), bandage above and "
          "below, and place the arm in an **arm sling with the hand slightly "
          "raised**; remove rings and bangles"],
         ["**Hand and fingers**",
          "Swelling, bruising, deformity, inability to move the fingers; often "
          "crush injury",
          "Remove rings at once; place a soft pad in the palm, wrap the hand in "
          "a soft dressing and support in an **elevation sling**; a finger may "
          "be strapped to its neighbour ('buddy strapping')"],
         ["**Pelvis**",
          "Crush injury or fall; pain in the groin, hip or back, worse on "
          "movement; inability to stand or walk; **blood-stained urine or "
          "inability to pass urine** (bladder/urethral injury); severe **shock** "
          "from heavy internal bleeding",
          "**Do not move unnecessarily and do not test the movement of the "
          "legs.** Lay the casualty **flat on his back**, place padding between "
          "the knees and tie the **knees and ankles together** with broad and "
          "narrow bandages, or use a pelvic binder/folded sheet round the "
          "pelvis; treat for **shock**; nothing by mouth; stretcher transport "
          "only"],
         ["**Thigh (femur)**",
          "Severe pain, marked deformity with the **leg turned outwards and "
          "shortened**, inability to move the leg, **severe shock** from "
          "internal bleeding of 1\u20132 litres",
          "Steady the limb with gentle traction if trained; place the sound leg "
          "beside it with padding between the legs; tie **figure-of-eight at the "
          "ankles and feet, then broad bandages above and below the fracture, at "
          "the knees and thighs**; ideally apply a **long splint from the armpit "
          "to beyond the foot** (Thomas splint in ambulance use); treat shock; "
          "stretcher transport"],
         ["**Knee and patella**",
          "Pain, swelling, inability to straighten or bear weight; the kneecap "
          "may be felt in two pieces with a gap",
          "**Do not force the knee straight** \u2014 immobilise in the position "
          "found, with a padded splint behind the leg from buttock to heel; "
          "raise and support the limb; cold compress; stretcher transport"],
         ["**Leg (tibia and fibula)**",
          "Pain, swelling, deformity; often an **open fracture** because the "
          "tibia lies just under the skin",
          "Dress any wound first; splint from above the knee to beyond the foot, "
          "or bandage to the sound leg with padding between; raise the limb; "
          "stretcher transport"],
         ["**Ankle and foot**",
          "Pain, swelling, bruising, inability to bear weight; difficult to "
          "distinguish from a severe sprain",
          "Remove the shoe only if it can be done easily; support the foot and "
          "ankle with a **pillow or blanket splint bandaged in figure-of-eight "
          "turns**; raise the limb; cold compress; do **not** let the casualty "
          "walk"]],
        weights=[2.6, 5.2, 6.0], size=8.4)

    # ------------------------------------------------------------------
    b.h2("Dislocation")
    b.box("DEFINITION", [
        "A **dislocation (luxation)** is the **displacement of one or more bones "
        "from their normal position at a joint**, with tearing or stretching of "
        "the capsule and ligaments.",
        "A **subluxation** is a **partial or incomplete** dislocation.",
        "Caused by **indirect violence, a wrench or a sudden muscular action**; "
        "it may **recur** easily once the ligaments have been stretched "
        "(recurrent dislocation of the shoulder).",
    ], kind="def")
    b.bullets([
        "**Commonest sites:** the **shoulder** (the most frequently dislocated "
        "joint, because it is the most mobile), then the **fingers and thumb, "
        "jaw (mandible), elbow, patella, hip** (needs great force) and the "
        "**vertebrae** (very dangerous \u2014 may damage the cord).",
        "A **pulled elbow (radial head subluxation)** is common in small "
        "children who are jerked up by one arm.",
    ])
    b.h3("Signs and symptoms of dislocation")
    b.bullets([
        "**Severe sickening pain** at the joint, and a feeling that the joint is "
        "\u2018out\u2019.",
        "**Marked deformity** \u2014 the joint looks abnormal, with an unusual "
        "prominence or hollow; compare with the other side.",
        "**Complete loss of movement (fixed joint)** \u2014 movement is "
        "impossible and any attempt causes intense pain.",
        "**Swelling, bruising and tenderness** around the joint; the limb may "
        "look **longer or shorter**.",
        "**No crepitus** and **no unnatural mobility** (unlike a fracture); "
        "possible numbness or loss of pulse if a nerve or vessel is compressed.",
    ])
    b.h3("First aid for a dislocation")
    b.numbered([
        "**Never attempt to reduce (put back) a dislocation** \u2014 nerves and "
        "vessels may be trapped, and there may also be a fracture.",
        "**Support and immobilise the joint in the most comfortable position** "
        "\u2014 an arm sling or collar-and-cuff for the shoulder or elbow; a "
        "padded splint for a knee; soft padding and a bandage for a finger.",
        "Use a **cold compress/ice pack wrapped in cloth** for 10\u201320 "
        "minutes to reduce pain and swelling.",
        "**Do not move the joint** and do not let the casualty try to use it.",
        "**Check the circulation and sensation** beyond the joint; loosen any "
        "bandage that tightens with swelling; remove rings.",
        "**Nothing by mouth** (an anaesthetic is likely), treat for shock, and "
        "arrange hospital transfer for X-ray and reduction.",
    ])
    b.h3("Fracture versus dislocation \u2014 comparison")
    b.table(
        ["Point", "Fracture", "Dislocation"],
        [["What is injured", "The **bone** is broken",
          "The **joint** \u2014 bone ends are displaced"],
         ["Site", "Anywhere along a bone", "**Only at a joint**"],
         ["Deformity", "Present, along the bone; limb may be shortened",
          "**Marked, at the joint**, with abnormal contour"],
         ["Movement", "Painful; **unnatural movement possible**",
          "**Movement impossible** \u2014 joint fixed"],
         ["Crepitus", "**Present** (do not test for it)", "**Absent**"],
         ["Pain", "Severe, at the fracture site",
          "Severe, sickening, at the joint"],
         ["Length of limb", "Usually **shortened**",
          "May be **lengthened or shortened**"],
         ["Recurrence", "Does not recur after healing",
          "**May recur** (habitual dislocation)"],
         ["Treatment", "Immobilise; do not reduce",
          "Immobilise in a comfortable position; do not reduce"]],
        weights=[2.4, 5.2, 5.0])

    # ------------------------------------------------------------------
    b.h2("Sprain and Strain")
    b.table(
        ["", "Sprain", "Strain"],
        [["Definition", "**Injury (stretching or tearing) of the ligaments and "
                        "tissues round a joint**, caused by a sudden wrench or "
                        "twist",
          "**Over-stretching or tearing of a muscle or its tendon** from a "
          "sudden violent or unaccustomed effort"],
         ["Common sites", "**Ankle** (commonest), wrist, knee, thumb, shoulder",
          "Back, thigh (hamstring), calf, shoulder"],
         ["Signs", "Pain and tenderness **around the joint**, swelling, bruising, "
                   "difficulty and pain on movement, but **some movement is "
                   "possible**",
          "Sudden sharp pain **in the muscle**, tenderness, stiffness, cramp, "
          "swelling, bruising, loss of power"],
         ["First aid", "**RICE** (below) and referral if severe \u2014 it may "
                       "really be a fracture", "**RICE**, rest of the muscle, "
                                               "gentle support, gradual return "
                                               "to activity"]],
        weights=[1.8, 5.4, 5.6])
    b.box("THE RICE (or PRICE / RICER) TREATMENT \u2014 FOR ALL SPRAINS, "
          "STRAINS AND BRUISES", [
        "**P \u2013 Protect** the injured part from further injury.",
        "**R \u2013 Rest** the part; stop the activity at once; do not walk on a "
        "sprained ankle.",
        "**I \u2013 Ice**: apply a cold compress or an ice pack **wrapped in a "
        "cloth (never directly on the skin)** for **10\u201320 minutes, "
        "repeated every 2\u20133 hours** for the first 24\u201348 hours.",
        "**C \u2013 Compression**: apply a **crepe/elastic bandage** in "
        "figure-of-eight turns, firm but not tight, extending well above and "
        "below the joint.",
        "**E \u2013 Elevation**: raise and support the limb **above the level of "
        "the heart** to reduce swelling.",
        "**R \u2013 Referral** for X-ray if pain is severe, weight-bearing is "
        "impossible, there is marked deformity or swelling, or there is no "
        "improvement.",
        "**Avoid H-A-R-M for the first 48\u201372 hours: H**eat, **A**lcohol, "
        "**R**unning/exercise and **M**assage \u2014 all increase bleeding and "
        "swelling.",
    ], kind="mnemonic")
    b.h3("Quick comparison of the four bone-and-joint injuries")
    b.table(
        ["Injury", "Structure damaged", "Key feature"],
        [["**Fracture**", "Bone", "Crepitus, deformity, unnatural movement, "
                                 "point tenderness"],
         ["**Dislocation**", "Joint (bone ends displaced)",
          "Joint fixed and deformed, no crepitus"],
         ["**Sprain**", "**Ligament** round a joint",
          "Pain and swelling round the joint, some movement possible"],
         ["**Strain**", "**Muscle or tendon**",
          "Sudden pain in the muscle during effort, cramp, weakness"]],
        weights=[2.4, 4.0, 6.2])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Fracture = break in the continuity of a bone; caused by **direct, "
        "indirect** violence or **muscular action**.",
        "**Simple** = skin intact; **compound/open** = wound over the fracture "
        "(most dangerous); **comminuted** = more than two pieces; **greenstick** "
        "= children only; **complicated** = nerve/vessel/organ injured.",
        "Signs: **pain, tenderness, swelling, deformity, loss of function, "
        "crepitus, irregularity, unnatural movement, shock** \u2014 never test "
        "for crepitus.",
        "Golden rules: **treat where he lies, steady and support, immobilise "
        "joints above and below, never reduce, bandage above and below \u2014 "
        "never over the fracture, check circulation, nothing by mouth**.",
        "**Collar bone** \u2192 elevation sling; **humerus** \u2192 "
        "collar-and-cuff sling; **forearm/wrist** \u2192 padded splint + arm "
        "sling; **femur** \u2192 long splint/tie to the sound leg + treat shock; "
        "**pelvis** \u2192 tie knees and ankles, flat, stretcher.",
        "**Spinal injury** \u2192 do **not** move; support the head in line; "
        "log-roll with helpers; jaw thrust for the airway.",
        "**Skull fracture** \u2192 CSF/blood from ear or nose, panda eyes, "
        "Battle's sign; **never plug the ear**; recovery position with the "
        "bleeding ear down.",
        "Dislocation = displacement at a **joint**; commonest = **shoulder**; "
        "**movement impossible, no crepitus**; never reduce it.",
        "**Sprain = ligament; strain = muscle/tendon**; both treated by "
        "**RICE**, and avoid **HARM** for 48\u201372 hours.",
    ])
