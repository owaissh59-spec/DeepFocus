# -*- coding: utf-8 -*-
"""Chapter 16 - Transport of Injured Persons."""


def render(b):
    b.part("PART VII", "Transport, Medicines and Quick Reference")
    b.chapter(
        "Transport of Injured Persons",
        "Principles and rules of transport, manual methods of lifting and "
        "carrying by one, two, three and four bearers, drags, stretchers and "
        "their improvisation, loading and carrying, positions for different "
        "injuries and ambulance transport.",
        syllabus=[
            "Transport of injured persons \u2014 general rules and principles, "
            "methods of carrying a casualty by one and more bearers, drags and "
            "emergency moves.",
            "Stretchers \u2014 types, testing, blanketing, loading and "
            "unloading, carrying over obstacles and stairs; positions of the "
            "casualty during transport; ambulance and hand-over.",
        ])

    # ------------------------------------------------------------------
    b.h2("Principles and General Rules of Transport")
    b.box("THE GOLDEN PRINCIPLE", [
        "==A casualty must not be moved until his injuries have been attended "
        "to and he is fit to be moved== \u2014 except when there is **immediate "
        "danger to life** (fire, explosion, gas, drowning, falling masonry, "
        "traffic, rising water or the need to reach the airway).",
        "**\u2018Treat first, transport next\u2019** \u2014 bleeding is "
        "controlled, fractures are immobilised and shock is treated **before** "
        "the journey.",
        "The object of transport is to move the casualty **to shelter or "
        "hospital without increasing the injury, without causing pain, and "
        "without risk to the bearers**.",
    ], kind="key")
    b.numbered([
        "**Decide whether the casualty needs to be moved at all**, and by what "
        "method \u2014 the method depends on the **nature and site of the "
        "injury, the weight and size of the casualty, the number of helpers, "
        "the distance and the nature of the ground**.",
        "**Explain the plan to the casualty** and to the helpers; appoint **one "
        "person as leader** who gives all the commands.",
        "**Immobilise fractures and dress wounds** before moving; support the "
        "injured part throughout.",
        "**Move the casualty feet first** on a level surface and **head first "
        "when going up** stairs, a slope or into an ambulance (the head stays "
        "higher) \u2014 except for a fracture of the lower limb going downhill, "
        "when the injured limb is kept uppermost.",
        "**Keep the casualty's body in line**; support the head and neck in any "
        "suspected spinal injury.",
        "Bearers must **step off with the same foot and break step** (not march "
        "in step) so that the stretcher does not sway; move **smoothly and "
        "slowly, without jolting**.",
        "**Watch the casualty's face continuously** for pain, vomiting or loss "
        "of consciousness; keep the airway clear.",
        "**Keep the casualty warm and covered**, and protect him from sun, rain, "
        "dust and onlookers.",
        "**Never leave the casualty alone**, and never allow him to walk or sit "
        "up if he has a serious injury or shock.",
        "**Lift with your legs, not your back** \u2014 feet apart, back "
        "straight, knees bent, casualty held close to the body, and lift on the "
        "word of command by straightening the knees.",
        "**Send a written report** with the casualty and hand him over "
        "personally to the doctor or nurse.",
    ])

    # ------------------------------------------------------------------
    b.h2("Emergency Moves and Drags (used only in immediate danger)")
    b.table(
        ["Method", "How it is done", "When used"],
        [["**Blanket (drag) lift**", "Roll the casualty gently onto a blanket "
                                    "(log-roll), gather the blanket at the head "
                                    "end and **drag him head-first** along the "
                                    "floor",
          "Unconscious or heavy casualty, smoke-filled room, narrow passage "
          "\u2014 the **safest drag for a suspected spinal injury**"],
         ["**Shoulder / armpit drag**", "Support the casualty's head on your "
                                       "forearms, pass your hands under his "
                                       "armpits, grasp his crossed forearms and "
                                       "drag him backwards",
          "Short distance over a smooth floor; no lifting equipment"],
         ["**Ankle drag**", "Grasp both ankles and pull the casualty in a "
                            "straight line", "Very short emergency distance on a "
                                             "smooth surface only \u2014 "
                                             "**never** with a head, neck or "
                                             "back injury"],
         ["**Clothes drag**", "Grasp the clothing at the shoulders/collar, "
                              "supporting the head with your forearms, and pull",
          "Rapid removal from fire, water's edge or traffic"],
         ["**Fireman's crawl**", "Tie the casualty's wrists together, put the "
                                 "loop round your neck and crawl on hands and "
                                 "knees",
          "Escape from a low, smoke-filled space"]],
        weights=[2.6, 5.2, 4.8], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Methods of Carrying by ONE Bearer")
    b.table(
        ["Method", "Technique", "Suitable for / not for"],
        [["**Human crutch (assisted walking)**", "The casualty's arm is placed "
                                                "round your neck and you hold "
                                                "his wrist; your other arm goes "
                                                "round his waist; you support "
                                                "him on the **injured side** "
                                                "and walk in step with him "
                                                "(using a stick on the sound "
                                                "side)",
          "**Conscious**, able to walk, minor injury of one leg. **Not** for "
          "serious injury, fracture of the lower limb, shock or giddiness"],
         ["**Cradle carry**", "Lift the casualty across your arms \u2014 one "
                              "arm under the knees, the other round the back",
          "**Children and light adults**"],
         ["**Pick-a-back (piggy-back)**", "The casualty, sitting on a chair or "
                                          "table, puts his arms round your neck; "
                                          "you hold his thighs and carry him on "
                                          "your back",
          "**Conscious, light** casualty who can hold on. Not for unconscious "
          "or arm-injured casualties"],
         ["**Fireman's lift (shoulder carry)**", "The casualty is drawn across "
                                                "your **shoulder**, his body "
                                                "hanging down your back, one "
                                                "arm held down in front of you "
                                                "\u2014 leaving **one of your "
                                                "hands free** to open doors or "
                                                "hold a rail",
          "**Light, unconscious or conscious** casualty; useful on a ladder or "
          "in a narrow passage. **Not** for chest, abdominal, spinal or "
          "multiple injuries, fractured ribs, breathlessness, or a heavy "
          "casualty"],
         ["**Drag methods**", "As above", "Immediate danger only"]],
        weights=[2.6, 5.2, 4.8], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Methods of Carrying by TWO or More Bearers")
    b.table(
        ["Method", "How the bearers hold", "Use"],
        [["**Two-handed seat**", "The two bearers face each other, squat on "
                                "either side of the casualty, pass their "
                                "**near** arms under his back and their "
                                "**far** arms "
                                "under his thighs, and grasp each other's "
                                "wrists (or clothing)",
          "A casualty who **cannot use his arms** or is unable to help; short "
          "distance"],
         ["**Three-handed seat**", "Each bearer grasps his own wrist with one "
                                   "hand and the other bearer's wrist with the "
                                   "other; the **fourth hand is used as a "
                                   "back-rest**",
          "A casualty with **one injured leg** \u2014 the free hand supports the "
          "injured limb"],
         ["**Four-handed seat**", "Each bearer grasps his own **left wrist with "
                                  "his right hand** and the other bearer's "
                                  "**right wrist with his left hand**, forming a "
                                  "square seat; the casualty sits on it and "
                                  "**holds the bearers' shoulders**",
          "A **conscious casualty who can use both arms** \u2014 no leg injury; "
          "for carrying over a distance"],
         ["**Fore-and-aft carry**", "One bearer lifts under the armpits from "
                                    "behind, the other holds under the knees "
                                    "\u2014 the casualty is carried lengthwise",
          "Through **narrow passages, doorways and staircases**"],
         ["**Chair carry**", "The casualty is seated on a strong chair, tied to "
                             "it, and the chair is tilted back and carried by "
                             "two bearers (one at the back holding the chair "
                             "back, one in front holding the front legs)",
          "**Conscious** casualty; **best method for stairs and narrow turns**. "
          "Not for spinal, pelvic or lower-limb fractures or an unconscious "
          "casualty"],
         ["**Three- or four-bearer lift (blanket/scoop lift)**",
          "Bearers kneel on one knee on the same side (or on both sides), slide "
          "their hands under the casualty's head/shoulders, back, hips and legs "
          "and, **on the word of command, lift together and rest him on their "
          "knees**, then stand and place him on the stretcher",
          "**Unconscious casualty, suspected fracture of the spine, pelvis or "
          "thigh** \u2014 the method of choice for placing a casualty on a "
          "stretcher"],
         ["**Log-roll**", "**Four or five bearers**; one holds the head in line "
                          "with the body and gives the commands while the others "
                          "turn the casualty as a single unit, keeping the head, "
                          "neck, trunk and legs in a straight line",
          "**Suspected spinal injury**, to place a spine board or blanket under "
          "the casualty, or to clear the airway of vomit"]],
        weights=[2.6, 5.4, 4.6], size=8.4)
    b.box("CHOOSING THE METHOD \u2014 A QUICK GUIDE", [
        "**Conscious, can walk, minor leg injury** \u2192 human crutch.",
        "**Conscious, can use both arms, must be carried some distance** \u2192 "
        "**four-handed seat**.",
        "**Conscious, one leg injured** \u2192 **three-handed seat**.",
        "**Cannot use his arms** \u2192 **two-handed seat**.",
        "**Narrow passage, stairs** \u2192 **fore-and-aft** or **chair carry**.",
        "**Unconscious, light casualty, single rescuer, immediate danger** "
        "\u2192 **fireman's lift** or a **drag**.",
        "**Spinal injury, pelvic or thigh fracture, unconscious casualty** "
        "\u2192 **stretcher with a 3\u20134 bearer lift or log-roll onto a spine "
        "board** \u2014 never a seat carry.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Stretchers")
    b.table(
        ["Type", "Description and use"],
        [["**Standard (Furley) stretcher**", "The ordinary ambulance stretcher "
                                            "\u2014 two poles with runners, "
                                            "traverse bars, a canvas bed and a "
                                            "pillow sack; about **1.9\u20132.4 m "
                                            "long**; folds lengthwise"],
         ["**Trolley (wheeled) stretcher**", "Wheeled cot used in ambulances and "
                                            "hospitals; height adjustable, with "
                                            "straps and rails"],
         ["**Scoop stretcher**", "Splits into two halves that are slid under the "
                                 "casualty from either side and clipped together "
                                 "\u2014 ideal for a **spinal injury** with "
                                 "minimum movement"],
         ["**Spinal (long) board / short board / vacuum mattress**",
          "Rigid board on to which the casualty is log-rolled and strapped, with "
          "head blocks and a cervical collar \u2014 the standard for suspected "
          "**spinal injury**"],
         ["**Neil Robertson stretcher**", "A **canvas-and-bamboo/slatted "
                                         "stretcher that wraps round the "
                                         "casualty and is lifted vertically** "
                                         "\u2014 used to remove a casualty from "
                                         "a **ship's hold, mine, tank, well, "
                                         "lift-shaft or any confined vertical "
                                         "space**"],
         ["**Paraguard / basket (Jordan frame) stretcher**", "Rigid basket "
                                                            "stretcher for "
                                                            "**mountain and "
                                                            "helicopter rescue**"],
         ["**Pole-and-canvas / Utila stretcher**", "Light folding stretcher used "
                                                  "by the armed forces and "
                                                  "civil defence"],
         ["**Improvised stretcher**", "Made from: **two strong poles/bamboos and "
                                      "a blanket** (fold the blanket round the "
                                      "poles so that the casualty's weight holds "
                                      "the ends), **two poles and two or three "
                                      "coats/jackets** (sleeves turned inside "
                                      "out and the poles passed through them), "
                                      "a **door, shutter, bench, table top, "
                                      "ladder (padded), plank, or a strong "
                                      "sheet/tarpaulin/sack** \u2014 anything "
                                      "rigid, long and strong enough"]],
        weights=[3.0, 9.6], size=8.8)
    b.box("STRETCHER RULES", [
        "**Always test an improvised stretcher** with a person of similar weight "
        "**before** putting the casualty on it.",
        "**Prepare (blanket) the stretcher** before the casualty is lifted: lay "
        "a blanket diagonally/lengthwise so that half can be wrapped over the "
        "casualty; add a pillow for the head.",
        "**Bring the stretcher to the casualty**, not the casualty to the "
        "stretcher.",
        "**Load and unload from the head or foot end** wherever possible, and "
        "always lift on the **word of command** of one leader.",
        "**Secure the casualty** with straps or broad bandages (chest, hips, "
        "knees and ankles) for a journey, on a slope, or in a helicopter.",
        "**Carry feet first on the level**, **head first up** an incline, stairs "
        "or into the ambulance, and **feet first down** \u2014 except that a "
        "casualty with a **fractured lower limb** is carried so that the "
        "**injured limb is uppermost**, i.e. **head first downhill**.",
        "**Four bearers** are ideal; **two can manage** on level ground; bearers "
        "should be of nearly equal height, and must **break step**.",
        "Keep the stretcher **horizontal at all times** \u2014 over obstacles, "
        "walls and ditches use the drill of passing the stretcher over while "
        "supporting it, never tilting it.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Position of the Casualty during Transport")
    b.table(
        ["Condition", "Position"],
        [["**Unconscious but breathing**", "**Recovery (lateral) position** "
                                          "\u2014 or supine with the head "
                                          "turned and the airway maintained, "
                                          "strapped to the stretcher"],
         ["**Shock, haemorrhage, fainting**", "**Flat on the back with the legs "
                                             "raised 20\u201330 cm**, head low "
                                             "and turned to the side"],
         ["**Head injury / stroke**", "Flat, **head and shoulders slightly "
                                      "raised**, head supported in line; "
                                      "recovery position if unconscious"],
         ["**Suspected spinal injury**", "**Flat on the back on a rigid spine "
                                         "board**, head immobilised with blocks "
                                         "and a collar, body strapped \u2014 "
                                         "moved only by log-roll or scoop"],
         ["**Chest injury / breathlessness / heart attack / asthma**",
          "**Half-sitting (Fowler's) position**, leaning towards the injured "
          "side in a chest injury"],
         ["**Abdominal injury or pain**", "On the back with the **knees drawn up "
                                          "and supported** by a pillow"],
         ["**Fracture of the lower limb**", "Flat, limb immobilised and "
                                            "supported; carried with the "
                                            "**injured limb uppermost on a "
                                            "slope**"],
         ["**Fracture of the pelvis**", "Flat on the back, knees and ankles tied "
                                        "together with padding between"],
         ["**Pregnant casualty**", "**Left lateral** position"],
         ["**Burns**", "Flat, burnt part raised, covered with a clean sheet"],
         ["**Snake bite**", "Lying still, bitten limb splinted and kept **at or "
                            "below heart level**"],
         ["**Vomiting / bleeding from the mouth**", "Head turned to the side, or "
                                                    "recovery position"]],
        weights=[4.0, 8.6])

    # ------------------------------------------------------------------
    b.h2("Ambulance Transport and Hand-Over")
    b.bullets([
        "**Call 108 (free ambulance) or 112**; give the exact location, number "
        "and condition of casualties and the hazards present (Chapter 1).",
        "Use an **ambulance** for every serious casualty. A private vehicle "
        "should be used only if no ambulance is available \u2014 and then the "
        "casualty must be **laid flat with an attendant beside him**, never "
        "propped up in a seat or carried on a two-wheeler.",
        "**Load the casualty head first** into the ambulance, secure the "
        "stretcher, keep him warm and keep the airway under observation "
        "throughout.",
        "The driver must travel **smoothly and steadily, not fast and jerky** "
        "\u2014 \u2018there is no hurry like a slow hurry\u2019; sirens and "
        "speed frighten the casualty and worsen shock.",
        "**Continue monitoring and recording** the level of response, breathing, "
        "pulse and bleeding during the journey; carry the first-aid kit within "
        "reach.",
        "**Hand over personally** to the doctor or nurse with a clear verbal and "
        "written report: **what happened, when, what you found (signs and "
        "symptoms with times), what treatment you gave, and any poison "
        "container, medicine, amputated part or belongings**.",
        "In **mass casualty and disaster** situations, transport in the order of "
        "**triage priority (red \u2192 yellow \u2192 green)**, not in the order "
        "in which casualties were found.",
        "**Air ambulance / helicopter** is used for mountains, floods and remote "
        "areas; the casualty must be **firmly strapped**, and the rescuer must "
        "approach the helicopter only **from the front, when signalled by the "
        "crew**.",
    ])
    b.box("PROTECTING THE BEARERS \u2014 CORRECT LIFTING TECHNIQUE", [
        "Stand with the **feet apart**, one foot slightly forward; **bend the "
        "knees, keep the back straight** and the head up.",
        "Get a **firm grip** and hold the load **close to the body**; do not "
        "twist while lifting.",
        "**Lift by straightening the legs**, smoothly, on the command "
        "\u2018ready \u2014 lift\u2019.",
        "**Never lift more than you can manage**; get more help, or use "
        "mechanical aids.",
        "Bearers should be of **similar height**, know their orders, and "
        "**break step** while carrying.",
    ], kind="note")

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "**Never move a casualty until his injuries are attended to** \u2014 "
        "except in immediate danger.",
        "Choice of method depends on the **injury, weight of the casualty, "
        "number of helpers, distance and ground**.",
        "**Four-handed seat** \u2192 conscious casualty who can use both arms; "
        "**three-handed seat** \u2192 one injured leg; **two-handed seat** "
        "\u2192 cannot use the arms; **human crutch** \u2192 can walk.",
        "**Fireman's lift** leaves one hand free and is for a light casualty "
        "\u2014 never for chest, abdominal or spinal injuries.",
        "**Fore-and-aft and chair carry** are best for **stairs and narrow "
        "passages**.",
        "**Spinal injury** \u2192 **log-roll onto a spine board/scoop "
        "stretcher** with 4\u20135 bearers, the head held in line.",
        "**Blanket drag** is the safest drag; **ankle drag** must never be used "
        "with a spinal injury.",
        "Carry **feet first on the level, head first going up** \u2014 but "
        "**injured limb uppermost** on a slope; bearers must **break step**.",
        "**Neil Robertson stretcher** \u2192 vertical removal from a confined "
        "space (well, ship's hold, mine).",
        "Always **test an improvised stretcher** first, keep it **horizontal**, "
        "and **hand over with a written report**.",
    ])
