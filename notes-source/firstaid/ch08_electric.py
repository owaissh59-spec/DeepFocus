# -*- coding: utf-8 -*-
"""Chapter 8 - Electric Shock (Electrical Injuries and Lightning)."""


def render(b):
    b.chapter(
        "Electric Shock",
        "Mechanism and severity of electrical injury, low- and high-voltage "
        "accidents, lightning strike, safe rescue, complete first aid, electrical "
        "burns and prevention.",
        syllabus=[
            "Electric shock \u2014 meaning, causes, factors deciding severity, "
            "effects on the body, signs and symptoms.",
            "Safe release of the casualty from the current, first aid including "
            "resuscitation and burn care, lightning injury, and prevention / "
            "electrical safety.",
        ])

    # ------------------------------------------------------------------
    b.h2("Meaning and Mechanism")
    b.box("DEFINITION", [
        "**Electric shock** is the sudden and violent effect produced on the "
        "body when an **electric current passes through it**. The current enters "
        "at the point of contact, travels through the tissues along the path of "
        "least resistance and leaves at the point of **earthing**, causing "
        "**burns at the entry and exit points** and disturbing the nerves, "
        "muscles and heart on the way.",
        "The body is a **conductor** because it is largely water and salt; "
        "**wet skin has about 25\u2013100 times less resistance than dry skin**, "
        "so shocks are far more dangerous when the skin, floor or clothing is "
        "wet.",
        "Current follows the shortest path: **hand-to-hand or hand-to-opposite "
        "foot paths cross the heart and are the most dangerous**.",
    ], kind="def")
    b.h3("Causes of electrical injury")
    b.bullets([
        "**Domestic (low voltage \u2014 up to 1,000 V, usually 220\u2013240 V "
        "AC):** faulty wiring, bare or frayed wires, broken plugs and sockets, "
        "wet hands on switches, using electrical appliances in the bathroom, "
        "children inserting objects into sockets, defective geysers, iron, "
        "heaters and immersion rods.",
        "**Industrial and high voltage (over 1,000 V):** overhead power lines, "
        "transformers, substations, welding sets, cranes touching lines, railway "
        "overhead equipment.",
        "**Lightning:** a natural discharge of millions of volts lasting a "
        "fraction of a second.",
        "**Others:** electric fences, stun devices, medical equipment and "
        "faulty earthing.",
    ])
    b.h3("Factors that decide the severity of an electric shock")
    b.table(
        ["Factor", "Effect on severity"],
        [["**Type of current**", "**AC (alternating current) is about 3\u20135 "
                                "times more dangerous than DC** at the same "
                                "voltage, because it causes sustained muscular "
                                "contraction (\u2018locking on\u2019) and "
                                "readily provokes **ventricular fibrillation** "
                                "\u2014 DC tends to throw the casualty clear"],
         ["**Amount of current (amperage)**", "The **real killer**. About "
                                              "**1 mA** is just felt; "
                                              "**10\u201315 mA** produces "
                                              "\u2018let-go\u2019 failure "
                                              "(muscles lock on); "
                                              "**50\u2013100 mA** can cause "
                                              "**ventricular fibrillation** "
                                              "(fatal); several amperes cause "
                                              "deep burns and cardiac standstill"],
         ["**Voltage**", "Higher voltage drives more current through the body; "
                         "**high-voltage contact causes deep charring, blast "
                         "injury and may throw the casualty some distance**"],
         ["**Resistance**", "**Wet skin, sweat, water, bare feet and metal "
                            "contact reduce resistance** and increase the "
                            "current; dry skin, rubber shoes and dry clothing "
                            "protect"],
         ["**Duration of contact**", "The longer the contact, the greater the "
                                     "damage \u2014 hence the first action is "
                                     "always to **break the contact**"],
         ["**Path taken through the body**", "**Hand to hand, or hand to "
                                             "opposite foot (across the chest) "
                                             "\u2014 most dangerous** because "
                                             "the current crosses the heart; "
                                             "current through the head affects "
                                             "the brain and breathing centre"],
         ["**Area of contact and general health**", "A small contact area "
                                                    "concentrates the current; "
                                                    "children, the elderly and "
                                                    "those with heart disease "
                                                    "are more vulnerable"]],
        weights=[3.0, 9.6])

    # ------------------------------------------------------------------
    b.h2("Effects, Signs and Symptoms")
    b.table(
        ["System / part", "Effects"],
        [["**Heart**", "**Ventricular fibrillation** (the commonest cause of "
                       "death), other arrhythmias, cardiac arrest, chest pain; "
                       "arrhythmia may appear **hours later**"],
         ["**Breathing**", "**Respiratory arrest** from spasm/paralysis of the "
                           "respiratory muscles or damage to the respiratory "
                           "centre; breathing may stop while the heart still "
                           "beats"],
         ["**Muscles**", "Violent **tetanic (sustained) contraction** \u2014 the "
                         "casualty may be unable to let go of the wire; "
                         "dislocations and **fractures of the spine or limbs** "
                         "from the spasm or from a fall"],
         ["**Skin**", "**Entry and exit burns** \u2014 small, round, "
                      "**painless, charred, depressed craters**, often on the "
                      "hand (entry) and foot (exit); flash and flame burns from "
                      "arcing and burning clothing"],
         ["**Deep tissues**", "Extensive **hidden destruction** of muscle and "
                              "nerve along the current's path \u2014 the "
                              "external wound looks small but the inside is "
                              "cooked (\u2018iceberg injury\u2019)"],
         ["**Nervous system**", "Unconsciousness, confusion, fits, temporary "
                                "paralysis, loss of memory, deafness, blindness, "
                                "later neuritis"],
         ["**Kidneys**", "**Acute kidney failure** from destroyed muscle "
                         "(myoglobin) \u2014 as in crush injury"],
         ["**General**", "**Shock**, internal injuries, secondary injuries from a "
                         "fall (head injury, fractures), and psychological "
                         "shock"]],
        weights=[2.6, 10.0])
    b.p("Recognition at the scene: an **unconscious or dazed casualty near an "
        "electrical appliance, wire or pole**, with **burn marks at two points**, "
        "muscle rigidity, and often no breathing or pulse. Look also for a "
        "**fallen wire, smell of burning, blown fuse or sparking switch**.")

    # ------------------------------------------------------------------
    b.h2("First Aid \u2014 Breaking the Contact Safely")
    b.box("THE FIRST AND MOST IMPORTANT RULE", [
        "**DO NOT TOUCH THE CASUALTY UNTIL YOU ARE CERTAIN THAT THE CONTACT WITH "
        "THE CURRENT IS BROKEN.** A rescuer who touches a live casualty becomes "
        "the next casualty.",
        "First **switch off** the current at the main switch, plug, fuse or "
        "circuit breaker \u2014 this is always the best method.",
        "If the switch cannot be reached, **insulate yourself and push, pull or "
        "lever the casualty away** from the source using a **dry non-conductor**: "
        "dry wooden stick, broom handle, bamboo, plastic chair, rubber mat, thick "
        "dry newspaper, folded dry cloth, dry rope or the casualty's dry "
        "clothing.",
        "**Stand on dry insulating material** (rubber mat, thick dry newspaper, "
        "dry wooden board, rubber-soled shoes) and use **one hand only**, keeping "
        "the other hand in your pocket.",
        "**Never use anything wet or metallic**; never touch the casualty's skin "
        "or wet clothing with bare hands; never use bare hands even with a dry "
        "cloth wrapped round them if the voltage is high.",
    ], kind="warn")
    b.h3("Low-voltage accidents (household \u2014 up to 1,000 V)")
    b.numbered([
        "**Switch off** at the mains/socket, or pull out the plug \u2014 do not "
        "pull on the cable.",
        "If that is impossible, stand on dry insulating material and **use a dry "
        "wooden/plastic object to push the casualty's limb away** from the "
        "source, or to move the wire away.",
        "You may also **loop a dry rope or dry cloth round the casualty's feet or "
        "arms and drag him away**.",
        "Only then begin the **DRABC** assessment.",
    ])
    b.h3("High-voltage accidents (over 1,000 V \u2014 power lines, substations, "
         "railway lines)")
    b.numbered([
        "**Do not approach.** High voltage can **arc (jump) several metres** and "
        "the ground itself becomes live (\u2018ground current/step potential\u2019).",
        "Keep yourself and all bystanders **at least 18 metres (about 20 yards) "
        "away**, or further if instructed, until the supply authority confirms "
        "the power is **switched off and earthed**.",
        "**Telephone the electricity supply company/police/fire brigade "
        "immediately**; only they can isolate the supply.",
        "**Nothing** \u2014 not dry wood, not rubber \u2014 gives protection at "
        "these voltages.",
        "If the casualty is in a vehicle touching a line, tell the occupants "
        "**to stay inside** until the power is cut.",
        "Begin treatment only when the officials declare the line dead.",
    ])
    b.h3("If the casualty is in water or the area is flooded")
    b.bullets([
        "**Switch off the supply before entering the water** \u2014 water "
        "conducts electricity over a wide area.",
        "Do not enter water containing a live cable; use a dry non-conducting "
        "pole from dry ground.",
    ])

    # ------------------------------------------------------------------
    b.h2("First Aid After the Contact Is Broken")
    b.numbered([
        "**Check response and breathing (DRABC).** Electrocution very commonly "
        "causes **cardiac and respiratory arrest** \u2014 if the casualty is not "
        "breathing normally, **start CPR at once** and **use an AED as soon as "
        "it arrives** (the rhythm is often a shockable ventricular fibrillation).",
        "**Call 112/108** and mention electrocution, so that the ambulance brings "
        "a defibrillator.",
        "If the casualty is unconscious but breathing, place him in the "
        "**recovery position**, supporting the head and neck (assume a **spinal "
        "injury** if he fell or was thrown).",
        "**Treat the burns** \u2014 look for **both entry and exit wounds**; "
        "cool with clean water for 10\u201320 minutes if the burn is fresh and "
        "small, then cover each with a **sterile non-adherent dressing or clean "
        "cling film**. Do not apply ointment or break blisters.",
        "**Treat for shock** \u2014 lay flat, keep warm, reassure, nothing by "
        "mouth.",
        "**Immobilise** any suspected fracture or dislocation caused by the "
        "muscle spasm or fall.",
        "**Monitor** breathing, pulse and consciousness continuously \u2014 "
        "arrhythmias may occur up to 24\u201348 hours later.",
        "**Send every electrical casualty to hospital**, even if he seems "
        "perfectly well \u2014 deep tissue damage and delayed heart rhythm "
        "problems are invisible at the scene.",
    ])
    b.box("ELECTRICAL BURNS \u2014 WHY THEY ARE SPECIAL", [
        "They are usually **deep (third or fourth degree) but look small** on the "
        "surface; there is always an **entry and an exit** wound.",
        "They are often **painless** at first because the nerve endings are "
        "destroyed.",
        "The real damage is to the **muscles, nerves and vessels beneath** "
        "\u2014 hence swelling, kidney failure and amputation may follow.",
        "**Never underestimate an electrical burn**; always refer to hospital.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Lightning Strike")
    b.bullets([
        "Lightning carries **millions of volts** but lasts only a few "
        "milliseconds; it may strike directly, by side-flash from a tree, by "
        "ground current, or by contact with a struck object.",
        "Effects: instantaneous **cardiac and respiratory arrest**, "
        "unconsciousness, **fern-like (Lichtenberg) skin markings**, superficial "
        "burns, ruptured eardrums, temporary blindness or deafness, paralysis of "
        "the legs (keraunoparalysis), and injuries from being thrown.",
        "**A casualty struck by lightning carries no electric charge \u2014 he "
        "is safe to touch immediately.**",
        "**Reverse triage** applies: in a multiple lightning casualty situation, "
        "attend **first to those who appear dead** (not breathing), because they "
        "can often be revived by prompt CPR, while those who are moving and "
        "moaning will usually survive.",
        "Move everyone to safe shelter first \u2014 **lightning can strike the "
        "same place twice**.",
        "Give prolonged CPR; recovery after lightning arrest is common if CPR is "
        "started at once.",
    ])
    b.box("LIGHTNING SAFETY RULES (30/30 RULE)", [
        "If the time between the flash and the thunder is **less than 30 "
        "seconds**, the storm is within 10 km \u2014 take shelter at once; wait "
        "**30 minutes** after the last thunder before going out.",
        "**Safe places:** a substantial building with wiring and plumbing, or a "
        "closed metal-topped vehicle (windows up).",
        "**Unsafe:** open ground, hill tops, isolated trees, verandas, sheds, "
        "bus shelters, water bodies, swimming pools, metal fences, tractors and "
        "open vehicles; also avoid using corded telephones and touching plumbing.",
        "If caught in the open with no shelter: crouch on the balls of the feet, "
        "heels together, head down, hands over the ears, **do not lie flat**, "
        "and keep away from tall objects; groups should spread out.",
        "Put down umbrellas, fishing rods, golf clubs and metal tools.",
    ], kind="note")

    # ------------------------------------------------------------------
    b.h2("Prevention \u2014 Electrical Safety")
    b.bullets([
        "Have all wiring installed and repaired by a **qualified electrician**; "
        "use **ISI-marked** appliances, plugs and cables.",
        "Ensure proper **earthing** of every appliance, and fit **fuses, MCBs "
        "(miniature circuit breakers) and an ELCB/RCCB (earth-leakage circuit "
        "breaker)**.",
        "**Switch off and unplug** before repairing or cleaning any appliance; "
        "use the **\u2018lock-out, tag-out\u2019** system at work.",
        "**Never touch switches, plugs or appliances with wet hands** or while "
        "standing in water or barefoot on a wet floor; keep electrical devices "
        "out of bathrooms.",
        "Replace frayed cords; do not overload sockets or use joined/taped wires; "
        "do not run wires under carpets.",
        "Fit **safety covers on sockets** where there are small children; keep "
        "them away from appliances and cords.",
        "Keep **at least 3 metres** away from fallen overhead wires and report "
        "them; never fly kites or erect poles near power lines; do not build or "
        "climb near transformers.",
        "Display **\u2018DANGER \u2014 ELECTRIC SHOCK\u2019 notices**, keep a "
        "**dry wooden stick, rubber mat and an insulated hook** near switchboards, "
        "and put up the **first-aid chart for electric shock** at work sites.",
        "Use **dry chemical or CO\u2082 extinguishers** for electrical fires "
        "\u2014 **never water**; switch off the supply first.",
    ])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "First action in electric shock = **switch off / break the contact "
        "safely**; never touch a live casualty.",
        "**AC is more dangerous than DC**; the amount of **current (mA)** kills, "
        "not the voltage alone; **50\u2013100 mA causes ventricular "
        "fibrillation**.",
        "**Wet skin reduces resistance** and multiplies the danger; the "
        "hand-to-hand/hand-to-foot path across the heart is the most dangerous.",
        "High voltage \u2014 keep **at least 18 metres away** and wait for the "
        "supply authority; no insulator protects you.",
        "Commonest cause of death = **ventricular fibrillation** \u2192 immediate "
        "**CPR + AED**.",
        "Electrical burns have **entry and exit wounds**, are **deep but look "
        "small**, and are often **painless**.",
        "Lightning casualties **carry no charge** \u2014 safe to touch; use "
        "**reverse triage** and treat the apparently dead first.",
        "Every electrical casualty goes to **hospital** \u2014 rhythm "
        "disturbances can appear many hours later.",
        "Use **CO\u2082/dry powder** extinguishers on electrical fires, never "
        "water.",
    ])
