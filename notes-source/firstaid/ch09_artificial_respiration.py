# -*- coding: utf-8 -*-
"""Chapter 9 - Different Methods of Artificial Respiration."""


def render(b):
    b.part("PART IV", "Breathing Emergencies and Bone Injuries")
    b.chapter(
        "Different Methods of Artificial Respiration",
        "Expired-air (mouth-to-mouth, mouth-to-nose, mouth-to-stoma) methods, "
        "the manual methods of Schafer, Holger Nielsen, Sylvester and Eve, "
        "mechanical methods, their technique, rates, advantages and drawbacks.",
        syllabus=[
            "Different methods of artificial respiration \u2014 classification, "
            "indications, complete technique of each method with rates, "
            "advantages, disadvantages and choice of method.",
            "Signs of effectiveness, complications, when to start and when to "
            "stop, and artificial respiration in special situations.",
        ])

    # ------------------------------------------------------------------
    b.h2("Meaning, Aim and Indications")
    b.box("DEFINITION", [
        "**Artificial respiration (artificial ventilation)** is the "
        "**procedure by which air is made to enter and leave the lungs of a "
        "casualty whose natural breathing has stopped or is failing**, in order "
        "to supply oxygen to the blood and remove carbon dioxide, until natural "
        "breathing returns.",
        "It is also called **rescue breathing**, **artificial ventilation** or "
        "(when combined with chest compressions) part of **CPR**.",
        "**Aim:** to keep the vital organs \u2014 especially the **brain** "
        "\u2014 supplied with oxygen. **Time is everything:** breathing must be "
        "restored within **3\u20134 minutes** to avoid brain damage.",
    ], kind="def")
    b.h3("Indications \u2014 when is artificial respiration needed?")
    b.bullets([
        "**Asphyxia from any cause** \u2014 drowning, choking, hanging, "
        "strangulation, suffocation, smothering, crush of the chest.",
        "**Electric shock and lightning**.",
        "**Gas and fume poisoning** \u2014 carbon monoxide, LPG, sewer gas, "
        "smoke inhalation.",
        "**Poisoning** by drugs that depress the respiratory centre \u2014 "
        "opium/morphine, barbiturates, alcohol, organophosphates, snake venom "
        "(cobra).",
        "**Head and spinal injury**, stroke, cardiac arrest.",
        "**Diseases and conditions** \u2014 severe asthma, status epilepticus, "
        "polio, tetanus, anaphylaxis.",
        "**Newborn babies who fail to breathe** after birth (asphyxia "
        "neonatorum).",
    ])
    b.p("Artificial respiration is needed whenever breathing has stopped "
        "(**apnoea**). If the **heart has also stopped**, artificial respiration "
        "alone is useless \u2014 it must be combined with **chest "
        "compressions (CPR)**.")

    # ------------------------------------------------------------------
    b.h2("Classification of the Methods")
    b.table(
        ["Group", "Methods", "Remarks"],
        [["**A. Expired-air (mouth-to-\u2026) methods** \u2014 *direct methods*",
          "1. Mouth-to-mouth\n2. Mouth-to-nose\n3. Mouth-to-mouth-and-nose "
          "(infants)\n4. Mouth-to-stoma\n5. Mouth-to-mask / face shield",
          "**The methods of choice** \u2014 most effective, can be started "
          "anywhere, deliver **16 % oxygen** and a large volume, and allow the "
          "rescuer to watch the chest"],
         ["**B. Manual (indirect / pressure) methods**",
          "1. **Schafer's** prone-pressure method\n2. **Holger Nielsen's** "
          "back-pressure arm-lift method\n3. **Sylvester's** chest-pressure "
          "arm-lift method\n4. **Eve's rocking** method\n5. Nielsen\u2013"
          "Callaghan and other historical variants",
          "**Obsolete as first choice**; used only when mouth-to-mouth is "
          "**impossible** (severe facial injury, corrosive poison on the lips, "
          "gas contamination, rescuer unable to make a seal)"],
         ["**C. Mechanical methods**",
          "Bag-valve-mask (Ambu bag), pocket mask with oxygen, mechanical "
          "ventilator, anaesthetic machine, historical **Pulmotor** and "
          "**iron lung (tank respirator)**",
          "Used by trained personnel and in hospital; deliver controlled "
          "volumes and up to **100 % oxygen**"]],
        weights=[3.0, 4.6, 5.0], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Expired-Air Methods \u2014 Technique")
    b.h3("Preparation common to all methods")
    b.numbered([
        "Remove the casualty from danger (and the danger from the casualty).",
        "Lay him **flat on the back on a firm surface**; loosen clothing at the "
        "neck, chest and waist.",
        "**Clear the mouth and throat** \u2014 turn the head to one side, hook "
        "out vomit, weed, sand, blood, broken/loose dentures and food with two "
        "fingers wrapped in cloth. Well-fitting dentures are left in place.",
        "**Open the airway** \u2014 one hand on the forehead to tilt the head "
        "back, two fingers under the chin to lift it (**head tilt\u2013chin "
        "lift**). Use a **jaw thrust** without head tilt if a neck injury is "
        "suspected.",
        "**Check breathing** for not more than **10 seconds** \u2014 look, "
        "listen and feel.",
    ])
    b.h3("1. Mouth-to-mouth respiration (the \u2018kiss of life\u2019)")
    b.numbered([
        "Kneel beside the casualty's head. Keep the airway open with head "
        "tilt\u2013chin lift.",
        "**Pinch the soft part of the nose** closed with the thumb and index "
        "finger and let the mouth fall open.",
        "Take a normal breath, place your **lips widely around the casualty's "
        "open mouth making an air-tight seal**.",
        "**Blow steadily for about 1 second**, watching the chest rise "
        "(\u2248 500\u2013600 ml \u2014 enough for a **visible chest rise**, no "
        "more).",
        "Lift your mouth away, turn your head to watch the **chest fall** and "
        "breathe in again.",
        "Give **2 breaths**, then 30 chest compressions if there is no pulse; "
        "if the heart is beating and only breathing has stopped, continue at "
        "**10\u201312 breaths per minute (1 breath every 5\u20136 seconds) in an "
        "adult** and **12\u201320 per minute (1 every 3 seconds) in a child or "
        "infant**.",
        "Re-check for normal breathing and circulation after every **1\u20132 "
        "minutes** (about 10 breaths).",
        "If the chest does not rise: **re-adjust the head tilt, check the seal, "
        "look for an obstruction** \u2014 do not attempt more than 2 breaths "
        "before resuming compressions.",
    ])
    b.h3("2. Mouth-to-nose respiration")
    b.bullets([
        "**Indications:** injury of the mouth or lips, **jaw clenched or wired "
        "(trismus)**, mouth cannot be sealed (a small child's or a very large "
        "adult's), rescue from water, corrosive poison on the mouth, and when "
        "the rescuer's mouth is smaller than the casualty's.",
        "**Technique:** close the mouth by pressing the chin upwards, seal your "
        "lips round the **nose** and blow. Open the mouth during expiration to "
        "let air escape (the soft palate may act as a valve).",
        "Slightly more difficult and slower, but equally effective.",
    ])
    b.h3("3. Mouth-to-mouth-and-nose (for infants and small babies)")
    b.bullets([
        "Keep the head in a **neutral** position \u2014 do **not** over-extend "
        "the neck.",
        "Cover the **whole of the baby's mouth and nose** with your mouth "
        "(or seal the nose and use the mouth alone in a bigger child).",
        "Blow **only the air held in your cheeks (small puffs)** for about 1 "
        "second, just enough to make the chest rise; give **5 initial breaths** "
        "and then **12\u201320 breaths per minute**.",
        "**Never blow hard into a baby's lungs** \u2014 they can be torn "
        "(barotrauma).",
    ])
    b.h3("4. Mouth-to-stoma and 5. mouth-to-mask")
    b.bullets([
        "**Mouth-to-stoma:** for a casualty who has had a **laryngectomy or "
        "tracheostomy** (a hole in the front of the neck). Seal the casualty's "
        "**mouth and nose** with your hand and blow directly into the stoma "
        "after wiping it clean.",
        "**Mouth-to-mask / face shield:** a transparent mask with a **one-way "
        "valve** \u2014 avoids direct contact with the casualty's mouth, "
        "protects from infection and vomit, and allows **supplementary oxygen**. "
        "This is the recommended method for trained first aiders.",
    ])
    b.box("ADVANTAGES OF EXPIRED-AIR METHODS OVER MANUAL METHODS", [
        "Deliver a **much larger volume of air (500\u2013800 ml)** compared with "
        "100\u2013300 ml by manual methods.",
        "Can be given in **any position** \u2014 in water, in a confined space, "
        "on a stretcher, while the casualty is being extricated.",
        "The rescuer **sees, hears and feels** the effectiveness (chest rise) "
        "immediately.",
        "**No equipment** is needed and one rescuer can also give chest "
        "compressions.",
        "Can be **combined with chest compressions** \u2014 manual methods "
        "cannot.",
        "Expired air still contains **16 % oxygen** and 4 % CO\u2082, enough to "
        "oxygenate the casualty's blood.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Manual Methods of Artificial Respiration")
    b.p("These older methods work by alternately **compressing and expanding the "
        "chest from the outside**. They are much less efficient and are now used "
        "only when mouth-to-mouth is impossible \u2014 but they are **regularly "
        "asked in examinations**, so learn the positions, the movements and the "
        "rates.")
    b.h3("1. Schafer's method (prone-pressure method)")
    b.table(
        ["Point", "Detail"],
        [["Position of casualty", "**Prone (face down)**, head turned to one "
                                 "side, one arm extended above the head, the "
                                 "other bent with the hand under the cheek; a "
                                 "folded blanket under the chest"],
         ["Position of rescuer", "**Astride or kneeling beside the casualty's "
                                 "thighs**, facing the head"],
         ["Movement", "Place the palms on the **lower ribs on either side of the "
                      "spine** (over the loins), thumbs almost touching, arms "
                      "**straight**. Swing forward with the weight of the body, "
                      "pressing steadily downwards and inwards for about "
                      "**2\u20133 seconds (expiration)**, then swing back "
                      "releasing the pressure completely for **2\u20133 seconds "
                      "(inspiration)**"],
         ["Rate", "**12\u201315 cycles per minute**"],
         ["Advantages", "Simple, needs no assistance, useful in drowning because "
                        "the prone position lets **water, vomit and weed drain "
                        "out** of the mouth"],
         ["Disadvantages", "**Only expiration is active** (inspiration is "
                           "passive) so the air exchanged is small "
                           "(100\u2013300 ml); cannot be used with a chest, "
                           "spine or abdominal injury or in pregnancy; the "
                           "airway is not under direct control; no chest "
                           "compressions possible"]],
        weights=[2.8, 9.8])
    b.h3("2. Holger Nielsen's method (back-pressure arm-lift method)")
    b.table(
        ["Point", "Detail"],
        [["Position of casualty", "**Prone**, arms bent with the hands one over "
                                 "the other **under the forehead**, head turned "
                                 "slightly to one side"],
         ["Position of rescuer", "**Kneeling on one knee at the casualty's "
                                 "head**, the other foot beside his elbow"],
         ["Movement (4 phases)", "**(a)** Place your palms on the casualty's "
                                 "**shoulder blades**, thumbs touching; "
                                 "**(b)** rock forward with straight arms and "
                                 "press steadily downwards \u2014 "
                                 "**expiration**; **(c)** rock back, slide the "
                                 "hands to just above the elbows; **(d)** "
                                 "**raise the arms upwards and towards you "
                                 "until resistance is felt** \u2014 this "
                                 "expands the chest, giving **inspiration** "
                                 "\u2014 then lower the arms"],
         ["Rate", "**12 complete cycles per minute** (about 5 seconds per cycle)"],
         ["Advantages", "**Both inspiration and expiration are active** "
                        "\u2014 therefore **more efficient than Schafer's**; "
                        "drainage of fluid from the mouth is still possible; "
                        "less tiring for the rescuer"],
         ["Disadvantages", "Cannot be used if the **arms or shoulders are "
                           "injured**, or with chest/spinal injuries; the "
                           "rescuer must be at the casualty's head; still far "
                           "less effective than mouth-to-mouth"]],
        weights=[2.8, 9.8])
    b.h3("3. Sylvester's method (chest-pressure arm-lift method)")
    b.table(
        ["Point", "Detail"],
        [["Position of casualty", "**Supine (on the back)**, with a folded "
                                 "blanket or cushion under the shoulders so "
                                 "that the head is **slightly lower** and the "
                                 "neck extended; the tongue must be drawn "
                                 "forward and the mouth cleared"],
         ["Position of rescuer", "**Kneeling at the casualty's head**, facing "
                                 "his feet"],
         ["Movement", "Grasp the casualty's wrists and **cross them over the "
                      "lower chest, pressing firmly downwards** \u2014 "
                      "**expiration** (2 seconds); then **sweep the arms "
                      "outwards, upwards and backwards above the head** as far "
                      "as possible \u2014 **inspiration** (2\u20133 seconds)"],
         ["Rate", "**12 cycles per minute**"],
         ["Advantages", "Useful when the casualty **cannot be turned prone** "
                        "\u2014 e.g. injuries of the back or when found lying "
                        "on the back; both phases active; the face is visible"],
         ["Disadvantages", "**Danger of the tongue falling back** and of "
                           "**inhaling vomit or water**, because the casualty is "
                           "on his back \u2014 hence unsuitable for drowning "
                           "unless an assistant holds the tongue/head; cannot "
                           "be used with chest, rib or arm injuries"]],
        weights=[2.8, 9.8])
    b.h3("4. Eve's rocking method")
    b.table(
        ["Point", "Detail"],
        [["Principle", "The casualty is **strapped to a stretcher or see-saw "
                       "frame pivoted at its centre** and rocked head-down and "
                       "foot-down; the **weight of the abdominal organs moves "
                       "the diaphragm** up and down, causing expiration and "
                       "inspiration"],
         ["Movement / angle", "Tilted about **45\u00b0 head-down (expiration)** "
                              "and **45\u00b0 foot-down (inspiration)**"],
         ["Rate", "**10\u201312 rocks per minute**"],
         ["Advantages", "Very **little effort for the rescuer** \u2014 can be "
                        "continued for hours; **drains fluid from the air "
                        "passages**, so it was widely used in drowning and in "
                        "poliomyelitis; the casualty can be transported while "
                        "being ventilated"],
         ["Disadvantages", "**Needs special apparatus (stretcher/rocking "
                           "board)**; unsuitable for chest, spine or abdominal "
                           "injuries and in pregnancy; slow to set up"]],
        weights=[2.8, 9.8])
    b.h3("5. Mechanical methods")
    b.bullets([
        "**Bag-valve-mask (Ambu bag)** \u2014 self-inflating bag with a "
        "non-rebreathing valve and mask; delivers 400\u2013600 ml per squeeze and "
        "up to **100 % oxygen** with a reservoir; best used by **two rescuers** "
        "(one holds the mask with both hands, the other squeezes).",
        "**Pocket mask with oxygen inlet** \u2014 simple, effective, protects the "
        "rescuer.",
        "**Mechanical ventilator** \u2014 hospital machine giving controlled "
        "volume, rate and oxygen concentration through an endotracheal tube.",
        "**Historical:** the **Pulmotor** (an early automatic resuscitator) and "
        "the **iron lung/tank respirator** (negative-pressure chamber used in "
        "polio epidemics).",
        "**Oxygen cylinders with masks** are *not* artificial respiration "
        "\u2014 they only enrich the air of a casualty who is still breathing.",
    ])

    # ------------------------------------------------------------------
    b.h2("Comparison of All Methods \u2014 Master Table")
    b.table(
        ["Method", "Position of casualty", "Rate/min", "Air moved", "Chief use"],
        [["**Mouth-to-mouth**", "Supine", "**10\u201312** (adult), 12\u201320 "
                                        "(child)", "**500\u2013800 ml**",
          "**Method of choice** in all cases"],
         ["Mouth-to-nose", "Supine", "10\u201312", "500\u2013800 ml",
          "Mouth injured, jaw clenched, rescue in water"],
         ["Mouth-to-mouth-and-nose", "Supine, neutral head", "12\u201320",
          "Cheek puffs only", "**Infants** under 1 year"],
         ["Mouth-to-stoma", "Supine", "10\u201312", "500\u2013800 ml",
          "Tracheostomy/laryngectomy"],
         ["**Schafer's** (prone pressure)", "**Prone**", "**12\u201315**",
          "100\u2013300 ml", "Drowning, when mouth-to-mouth impossible"],
         ["**Holger Nielsen's** (back pressure\u2013arm lift)", "**Prone**",
          "**12**", "300\u2013500 ml", "Best of the manual methods"],
         ["**Sylvester's** (chest pressure\u2013arm lift)", "**Supine**",
          "**12**", "300\u2013500 ml", "When the casualty cannot be turned prone"],
         ["**Eve's rocking**", "Strapped to a rocking stretcher", "**10\u201312**",
          "Variable", "Prolonged ventilation, drainage of fluid"],
         ["Bag-valve-mask", "Supine", "10\u201312 (1 squeeze every 5\u20136 s)",
          "400\u2013600 ml + O\u2082", "Trained rescuers, ambulance"]],
        weights=[3.2, 2.8, 2.2, 2.2, 3.4], size=8.4)

    # ------------------------------------------------------------------
    b.h2("Effectiveness, Complications and Stopping")
    b.table(
        ["Signs that it is working", "Complications and errors"],
        [["The **chest rises and falls** with each breath.",
          "**Gastric distension** from blowing too hard or too fast \u2192 "
          "vomiting and **aspiration**"],
         ["Colour improves \u2014 blueness of lips and face disappears.",
          "**Over-inflation** \u2192 rupture of alveoli (barotrauma), especially "
          "in children"],
         ["The pulse becomes stronger and more regular.",
          "**Failure of the chest to rise** \u2014 blocked airway, poor seal, "
          "insufficient head tilt"],
         ["**Spontaneous breathing, coughing, swallowing or movement** returns.",
          "**Cross-infection** \u2014 use a face shield/pocket mask"],
         ["Pupils constrict and consciousness begins to return.",
          "Rescuer **hyperventilation and giddiness** from blowing too hard/fast"]],
        weights=[6.2, 6.6], first_bold=False)
    b.bullets([
        "**When breathing returns:** stop ventilating, place the casualty in the "
        "**recovery position**, keep him warm, watch him continuously (breathing "
        "may stop again) and send him to hospital.",
        "**Continue artificial respiration until** natural breathing returns, "
        "qualified help takes over, the casualty's heart stops (then start full "
        "CPR), or you are exhausted \u2014 **never abandon a casualty because "
        "\u2018enough time has passed\u2019**. In drowning, electrocution, "
        "lightning and hypothermia, prolonged efforts have succeeded after an "
        "hour or more.",
        "**Never give artificial respiration to a casualty who is breathing "
        "normally**; and never delay it to look for equipment.",
    ])
    b.box("SPECIAL SITUATIONS", [
        "**Drowning** \u2014 begin rescue breaths as soon as the airway is "
        "clear, even while still in shallow water; do **not** waste time trying "
        "to expel water from the lungs; expect vomiting.",
        "**Corrosive poison or contact poison (organophosphate) on the mouth** "
        "\u2014 do not do direct mouth-to-mouth; use a **mask, bag-valve device "
        "or a manual method**.",
        "**Gas-filled space** \u2014 remove the casualty into fresh air first; "
        "never enter without protection.",
        "**Suspected spinal injury** \u2014 open the airway with a **jaw "
        "thrust**, keeping the head in line.",
        "**Facial injury/severe bleeding from the mouth** \u2014 use "
        "mouth-to-nose or a manual method, keeping the airway clear.",
        "**Newborn baby** \u2014 gentle puffs at **30\u201360 per minute**; "
        "resuscitation ratio for a newborn is **3 compressions : 1 breath**.",
    ], kind="note")

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Aim of artificial respiration = to **supply oxygen to the brain** "
        "within **3\u20134 minutes**.",
        "**Mouth-to-mouth is the method of choice** \u2014 largest volume, no "
        "equipment, can be combined with chest compressions; rate **10\u201312/"
        "min** in adults (1 breath every 5\u20136 seconds).",
        "**Schafer's** \u2014 prone, pressure over the loins, **12\u201315/min**, "
        "only expiration active.",
        "**Holger Nielsen's** \u2014 prone, **back pressure + arm lift**, "
        "**12/min**, the **most efficient manual method**.",
        "**Sylvester's** \u2014 supine, **chest pressure + arm lift**, "
        "**12/min**, risk of the tongue falling back and of aspiration.",
        "**Eve's rocking** \u2014 rocking stretcher at 45\u00b0, **10\u201312/"
        "min**, least tiring and drains fluid.",
        "**Infants** \u2014 mouth-to-mouth-and-nose with **cheek puffs**, "
        "neutral head, 12\u201320/min; newborn ratio **3 : 1**.",
        "Expired air contains **16 % oxygen** \u2014 that is why expired-air "
        "methods work.",
        "Commonest complication = **stomach inflation and vomiting** from too "
        "forceful breaths.",
    ])
