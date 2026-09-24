# -*- coding: utf-8 -*-
"""Chapter 15 - Common Conditions."""


def render(b):
    b.part("PART VI", "Common Conditions and Bites")
    b.chapter(
        "Common Conditions",
        "Foreign bodies in the ear, eye and nose; cramps; frost-bite and other "
        "cold injuries; heat disorders; bites and stings; epistaxis; snake bite "
        "and dog bite.",
        syllabus=[
            "Common conditions \u2014 **foreign body in ear, eye and nose; "
            "cramps; frost-bite; bites and stings; epistaxis; snake bite; dog "
            "bite**.",
            "Related emergencies of heat and cold \u2014 heat cramps, heat "
            "exhaustion, heat stroke, hypothermia and chilblains.",
        ])

    # ------------------------------------------------------------------
    b.h2("Foreign Body in the Ear")
    b.table(
        ["Point", "Detail"],
        [["Common objects", "**Children:** beads, seeds, grain, paper, cotton, "
                            "small toys, pencil lead, pebbles. "
                            "**Adults:** cotton-bud tips, ear-rings, insects "
                            "(ants, mosquitoes, cockroaches), water, wax"],
         ["Signs and symptoms", "**Pain, blocked feeling, deafness on that side, "
                                "buzzing or noise in the ear** (live insect), "
                                "giddiness, discharge or bleeding if the canal "
                                "or drum is injured; the child may keep "
                                "touching the ear"],
         ["First aid", "**Do NOT try to remove the object**; never probe with a "
                       "hair pin, matchstick, tweezers, ear bud or any "
                       "instrument \u2014 you will push it deeper and may "
                       "**rupture the eardrum**.  \u2022  Reassure the casualty "
                       "and keep the head **tilted with the affected ear "
                       "downwards** \u2014 a loose object may fall out.  "
                       "\u2022  For an **insect**, sit the casualty with the "
                       "head tilted, affected ear up, and **gently pour "
                       "lukewarm water, olive oil, glycerine or coconut oil** "
                       "into the ear to float or kill the insect; then tilt the "
                       "ear down. (**Never** put liquid in if there is a "
                       "discharge, a suspected perforation or a vegetable "
                       "object.)  \u2022  Never put water in for **seeds, "
                       "grains or peas** \u2014 they swell.  "
                       "\u2022  Take the casualty to a **doctor/ENT "
                       "specialist**"],
         ["Prevention", "Keep small objects away from children; teach children "
                        "never to put anything in the ear; do not use cotton buds "
                        "or hairpins to clean ears"]],
        weights=[2.6, 10.0])

    # ------------------------------------------------------------------
    b.h2("Foreign Body in the Eye")
    b.bullets([
        "Common objects: **dust, grit, sand, eyelash, insect, husk, metal or "
        "glass fragment, chemical splash, coal dust**.",
        "Signs: **pain and grittiness, redness, watering, blinking and spasm of "
        "the lids (blepharospasm), inability to open the eye, blurred vision, "
        "sensitivity to light**.",
    ])
    b.h3("First aid for a loose particle")
    b.numbered([
        "**Tell the casualty not to rub the eye** \u2014 rubbing drives the "
        "particle in and scratches the cornea.",
        "Wash your hands; sit the casualty facing the light and gently separate "
        "the lids with the finger and thumb.",
        "Look for the particle: on the white of the eye, under the lower lid "
        "(pull the lower lid down) or under the upper lid (ask the casualty to "
        "look down while you lift the lid or draw the upper lid over a match "
        "stick/cotton bud).",
        "**Irrigate the eye with clean water or sterile saline** poured from the "
        "**inner corner (nose side) outwards** so that the water does not run "
        "into the other eye; or use an **eye bath/eye cup**. Ask the casualty to "
        "**blink under water**.",
        "If the particle is visible and loose, **lift it off gently with the "
        "corner of a clean moist cloth, a cotton bud or the tip of a clean "
        "handkerchief**.",
        "If it does not come out, **cover the eye with an eye pad and refer to a "
        "doctor**.",
    ])
    b.box("NEVER \u2014 IN EYE INJURIES", [
        "**Never rub** the eye or let the casualty rub it.",
        "**Never try to remove**: an object **sticking to or embedded in** the "
        "eyeball, an object on the **cornea (the coloured part)**, a **metal or "
        "glass splinter**, or anything that has **penetrated** the eye.",
        "**Never apply pressure** on an injured eyeball, and never apply "
        "ointment, oil, kajal, breast milk or any home remedy.",
        "In a **penetrating injury**: lay the casualty on his back, ask him to "
        "keep both eyes still, **cover the injured eye lightly with a sterile "
        "pad or a paper/plastic cup taped over it (no pressure)** \u2014 cover "
        "the other eye too if possible \u2014 and take him **lying down** to an "
        "eye hospital. Nothing by mouth.",
        "For a **chemical splash**: **irrigate continuously with plenty of "
        "running water for at least 20 minutes**, holding the lids open, with "
        "the affected eye **lower**; then cover and refer. Do not try to "
        "neutralise the chemical.",
        "For **arc-eye/snow blindness/welder's flash** (burning, gritty, "
        "watering eyes hours after exposure): cover both eyes with soft pads, "
        "rest in a darkened room, and refer.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Foreign Body in the Nose")
    b.bullets([
        "Usually in **small children** \u2014 beads, buttons, seeds, paper, "
        "pieces of sponge, small batteries, peanuts; sometimes an insect in "
        "adults.",
        "Signs: **blockage and noisy breathing through one nostril, a "
        "blood-stained or foul-smelling discharge from that nostril (a classical "
        "sign of a long-standing foreign body)**, pain, swelling, sneezing.",
        "First aid: **Do not attempt to remove it** and **do not probe with "
        "tweezers, pins or fingers**; **keep the child calm**, tell him to "
        "**breathe through the mouth**, and ask an older child to **blow the "
        "nose gently once** while the other nostril is pressed closed. Do not "
        "let him sniff inwards. **Take the child to a doctor/ENT specialist "
        "\u2014 without delay if the object is a button battery** (it burns the "
        "tissue within hours) **or if breathing is affected**.",
        "**Danger:** the object may be inhaled into the air passage and cause "
        "choking; a battery or a nut can cause severe damage and infection.",
    ])

    # ------------------------------------------------------------------
    b.h2("Cramps")
    b.box("DEFINITION", [
        "A **cramp** is a **sudden, involuntary, painful and prolonged "
        "contraction (spasm) of a muscle or group of muscles**, which becomes "
        "hard and knotted and cannot be relaxed voluntarily.",
    ], kind="def")
    b.table(
        ["Causes", "Common sites"],
        [["**Loss of salt and water** through profuse sweating (hot work, "
          "fever, heavy exercise) \u2014 **heat cramps**",
          "**Calf** (commonest), foot, thigh, hamstring"],
         ["**Unaccustomed or prolonged exercise**, poor warm-up, fatigue, "
          "swimming in cold water", "Hand and finger (writer's cramp), "
                                    "abdominal muscles"],
         ["**Repeated occupational movements**; sitting or lying in an awkward "
          "position (night cramps in bed)", "Neck, back"],
         ["**Loss of fluid by vomiting or diarrhoea** (cholera cramps), "
          "dialysis", "Whole limbs"],
         ["**Deficiency of calcium, magnesium, potassium or sodium**; pregnancy; "
          "some medicines (diuretics); poor circulation in the elderly",
          "Any muscle"]],
        weights=[7.4, 5.4], first_bold=False)
    b.h3("First aid for cramps")
    b.numbered([
        "**Stretch the affected muscle gently** and hold it \u2014 this is the "
        "quickest relief. For a **calf cramp**: straighten the knee and "
        "**pull the foot and toes firmly upwards towards the shin** (or have the "
        "casualty stand and press the heel down). For a **thigh (hamstring) "
        "cramp**: straighten the knee and raise the leg. For a **foot cramp**: "
        "stand on the ball of the foot, or pull the toes up. For a **hand cramp**: "
        "straighten the fingers and press the palm flat on a hard surface.",
        "**Massage the muscle firmly** towards the heart after the spasm eases, "
        "and apply gentle **warmth** (a warm compress) \u2014 or a cold compress "
        "if the muscle is strained.",
        "**Rest** the muscle, then move it gently; do not resume hard work "
        "immediately.",
        "**Give fluids** \u2014 **cool water or ORS/lightly salted water or "
        "lemon water with a pinch of salt** (about \u00bd teaspoon of salt per "
        "litre) if cramps are due to heat and sweating.",
        "**Refer to a doctor** if cramps are severe, frequent, unexplained, "
        "accompanied by swelling/redness (may be **deep-vein thrombosis**), or "
        "occur with abdominal cramps and vomiting.",
    ])
    b.p("**Prevention:** warm up and stretch before exercise, drink enough "
        "water and take adequate salt in hot weather, keep a balanced diet rich "
        "in calcium, potassium and magnesium (bananas, milk, green vegetables), "
        "avoid sudden unaccustomed effort, and stretch the calves before "
        "sleeping.")

    # ------------------------------------------------------------------
    b.h2("Frost-Bite and Cold Injuries")
    b.box("DEFINITION", [
        "**Frost-bite** is the **freezing of the tissues of the exposed parts of "
        "the body** (fingers, toes, nose, ears, cheeks, chin) on exposure to "
        "extreme cold, in which ice crystals form in the tissues and the blood "
        "supply is cut off \u2014 it may end in **gangrene**.",
        "It is common in **high altitudes, snow-bound areas, mountaineers, "
        "soldiers (Siachen/Kargil), and in anyone exposed to cold with wet "
        "clothing, wind, tight boots, alcohol or poor circulation**.",
    ], kind="def")
    b.table(
        ["Stage", "Features"],
        [["**1. Frost-nip (mildest, reversible)**", "Skin becomes **white and "
                                                   "numb**; no ice in the "
                                                   "tissue; recovers completely "
                                                   "on warming"],
         ["**2. Superficial frost-bite (1st\u20132nd degree)**",
          "**\u2018Pins and needles\u2019 then complete numbness**; skin "
          "**hard, waxy white, cold and stiff on the surface but soft "
          "underneath**; on re-warming it becomes red, swollen, painful and "
          "**blistered**"],
         ["**3. Deep frost-bite (3rd\u20134th degree)**",
          "Whole part **solid, hard like wood, white or blue-grey, completely "
          "numb, no movement**; later becomes **black and mummified "
          "(gangrene)**; may need amputation"]],
        weights=[3.4, 9.2])
    b.h3("First aid for frost-bite")
    b.numbered([
        "**Move the casualty into shelter and out of the cold and wind.**",
        "**Remove wet or tight clothing, boots, gloves, rings, bangles and "
        "watches** from the affected part before it swells; handle the part "
        "**very gently**.",
        "**Warm the part with body heat first** \u2014 put frost-bitten fingers "
        "**in the casualty's own armpit or groin, or in your hands**; cover the "
        "nose, ears or cheeks with warm dry hands.",
        "**Re-warm by immersing the part in warm water at 37\u201340 \u00b0C "
        "(body temperature \u2014 comfortably warm to your elbow, never hot) for "
        "about 20\u201340 minutes**, until the skin becomes soft, red and "
        "sensation returns. Keep changing the water to maintain the temperature. "
        "**Do this only if there is no chance of the part re-freezing.**",
        "**Dry gently, apply a loose sterile dressing, separate the fingers and "
        "toes with dry gauze**, raise the part on a pillow and keep it warm.",
        "**Give warm sweet drinks** if the casualty is conscious; give "
        "paracetamol for pain (thawing is very painful).",
        "**Treat for hypothermia** as well \u2014 it is usually present and is "
        "the greater danger.",
        "**Arrange hospital transfer**; the casualty should **not walk** on "
        "frost-bitten feet.",
    ])
    b.box("FROST-BITE \u2014 THE \u2018NEVERS\u2019", [
        "**Never rub or massage** the frozen part, and **never rub it with snow** "
        "\u2014 the ice crystals tear the tissues.",
        "**Never use direct or dry heat** \u2014 no fire, stove, heater, "
        "hot-water bottle, radiator, exhaust or hot water above 40 \u00b0C: the "
        "numb skin is burnt without the casualty feeling it.",
        "**Never break blisters** and never apply ointment.",
        "**Never let the part thaw and re-freeze** \u2014 that causes far more "
        "damage than remaining frozen; if the casualty must still be moved "
        "through the cold, **keep the part frozen** and re-warm at the "
        "destination.",
        "**Never give alcohol or tobacco** \u2014 alcohol dilates skin vessels "
        "and increases heat loss; nicotine constricts vessels.",
        "**Never allow the casualty to walk** on thawed frost-bitten feet.",
    ], kind="warn")
    b.h3("Other cold injuries")
    b.table(
        ["Condition", "Features and first aid"],
        [["**Chilblains**", "Small, itchy, red-purple painful swellings on the "
                            "fingers, toes, heels, nose or ears after exposure "
                            "to cold and damp. Warm the part slowly, keep it "
                            "dry, apply calamine or a soothing cream, do **not** "
                            "scratch or apply direct heat; wear warm socks and "
                            "gloves"],
         ["**Trench foot (immersion foot)**", "Prolonged standing in cold water "
                                             "or wet boots without freezing "
                                             "\u2014 the foot becomes white, "
                                             "numb, swollen and later painful "
                                             "and red. Dry and warm the feet, "
                                             "raise them, do not rub, change "
                                             "socks frequently, refer"],
         ["**Hypothermia**", "**Fall of the body's core temperature below "
                             "35 \u00b0C (95 \u00b0F)**. Causes: exposure to "
                             "cold, wind and rain, immersion in cold water, "
                             "inadequate clothing, alcohol, exhaustion; the "
                             "**elderly and infants** are especially "
                             "vulnerable.  **Signs:** shivering (which "
                             "**stops** as it becomes severe), cold pale dry "
                             "skin, apathy, confusion, slurred speech, "
                             "clumsiness and stumbling, slow shallow breathing, "
                             "**slow weak pulse**, drowsiness \u2192 "
                             "unconsciousness \u2192 cardiac arrest.  "
                             "**First aid:** move to shelter, **remove wet "
                             "clothing and dry the casualty**, wrap in blankets/"
                             "sleeping bag with a hat, insulate from the ground, "
                             "**re-warm gradually** (body heat, warm room, "
                             "covered warm water bottles on the trunk \u2014 "
                             "not the limbs), give **warm sweet drinks** if "
                             "fully conscious, **handle very gently** (rough "
                             "handling can stop the heart), and transport "
                             "**horizontally** to hospital.  "
                             "**Never:** rub the skin, give alcohol, use direct "
                             "strong heat, put the casualty in a hot bath, or "
                             "let him walk or exercise. **Remember \u2018nobody "
                             "is dead until warm and dead\u2019** \u2014 "
                             "continue CPR for a long time"]],
        weights=[2.6, 10.0], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Heat Disorders (for comparison)")
    b.table(
        ["", "Heat cramps", "Heat exhaustion", "Heat stroke (sun stroke)"],
        [["Cause", "Loss of **salt and water** in sweat",
          "Loss of **salt and water**, with dehydration",
          "**Failure of the heat-regulating centre** \u2014 sweating stops and "
          "the body cannot lose heat"],
         ["Temperature", "Normal", "Normal or slightly raised (up to 40 \u00b0C)",
          "**Very high \u2014 above 40 \u00b0C (104 \u00b0F)**"],
         ["Skin", "Normal, sweating", "**Pale, cold, clammy, sweating "
                                      "profusely**",
          "**Hot, flushed, dry \u2014 sweating absent**"],
         ["Pulse", "Normal", "**Rapid and weak**", "**Rapid and full/bounding**"],
         ["Other signs", "Painful muscle spasms, especially in the legs and "
                         "abdomen",
          "Headache, giddiness, nausea, cramps, weakness, thirst, fainting, "
          "confusion", "**Severe headache, restlessness and confusion \u2192 "
                       "fits \u2192 unconsciousness**; noisy breathing"],
         ["First aid", "Rest in a cool place, stretch and massage the muscle, "
                       "give **ORS/salted water**",
          "Lie down in a cool shady place, **raise the legs**, loosen clothing, "
          "give **ORS or lightly salted water in sips**, fan and sponge; refer "
          "if no improvement",
          "==A medical emergency== \u2014 call an ambulance; move to a cool "
          "place, **remove outer clothing, cool rapidly** by sponging with cold "
          "water, wrapping in a cold wet sheet, ice packs in the armpits, groin "
          "and neck, and fanning; stop cooling when the temperature falls to "
          "about 38 \u00b0C; recovery position if unconscious; **nothing by "
          "mouth if not fully conscious**; monitor continuously"]],
        weights=[1.7, 3.4, 3.8, 3.9], size=8.4)

    # ------------------------------------------------------------------
    b.h2("Bites and Stings (Insects and Other Creatures)")
    b.h3("Insect stings \u2014 bee, wasp, hornet, ant")
    b.table(
        ["Point", "Detail"],
        [["Signs", "Sharp pain, redness, **local swelling and itching**; a "
                   "**sting may be left in the skin by a honey bee** (wasps and "
                   "hornets do not leave the sting)"],
         ["First aid", "**Scrape the sting out sideways with the edge of a blunt "
                       "knife, a credit card or a fingernail \u2014 do not use "
                       "tweezers or squeeze it**, which injects more venom.  "
                       "\u2022 Wash with soap and water.  "
                       "\u2022 Apply a **cold compress/ice wrapped in cloth for "
                       "10\u201320 minutes** to reduce pain and swelling; "
                       "calamine lotion or a soothing antihistamine cream may "
                       "be used.  "
                       "\u2022 **Raise** the part; remove rings if the hand is "
                       "stung.  "
                       "\u2022 An oral **antihistamine** and paracetamol may be "
                       "given for itching and pain.  "
                       "\u2022 Watch for **30 minutes** for signs of allergy"],
         ["When it is an emergency", "**(a) Anaphylaxis** \u2014 swelling of the "
                                     "face, lips or tongue, wheeze, difficulty "
                                     "in breathing or swallowing, widespread "
                                     "rash, collapse \u2192 **adrenaline "
                                     "auto-injector + call 112/108** "
                                     "(Chapter 7).  "
                                     "**(b) Sting inside the mouth or throat** "
                                     "\u2192 swelling can block the airway: "
                                     "give the casualty **ice to suck or cold "
                                     "water to sip** and call an ambulance.  "
                                     "**(c) Multiple stings** (bee/hornet "
                                     "swarm) \u2192 hospital"],
         ["Prevention", "Avoid bright clothes, perfumes and sweet foods "
                        "outdoors; do not disturb hives or nests; keep food "
                        "covered; use screens and repellents; shake out shoes "
                        "and clothes in outdoor camps"]],
        weights=[2.6, 10.0])
    b.h3("Other bites and stings")
    b.table(
        ["Creature", "Features", "First aid"],
        [["**Scorpion**", "**Intense burning pain and numbness** at the site "
                          "(often the hand or foot), local swelling, sweating, "
                          "salivation, vomiting, restlessness; in children "
                          "\u2014 rapid pulse, breathlessness, fits and "
                          "collapse (Indian red scorpion is dangerous)",
          "Reassure and keep the casualty still; wash the site; **cold "
          "compress** to relieve pain; immobilise and **keep the part below "
          "heart level**; give paracetamol; **no tourniquet, no cutting, no "
          "sucking**; **take to hospital at once, especially a child** (pain "
          "relief and prazosin may be needed)"],
         ["**Spider / centipede**", "Local pain, redness, swelling; rarely "
                                    "cramps, sweating and fever",
          "Wash, cold compress, elevate, analgesic; refer if there are general "
          "symptoms or the spider was dangerous"],
         ["**Mosquito, bug, flea, mite**", "Itchy red papules; danger is the "
                                           "**disease transmitted** \u2014 "
                                           "malaria, dengue, chikungunya, "
                                           "filaria, typhus",
          "Calamine or antihistamine cream, avoid scratching; use repellents, "
          "nets and screens; watch for **fever** and see a doctor"],
         ["**Tick and leech**", "Attached to the skin, painless, engorged",
          "**Tick:** grasp close to the skin with fine tweezers and pull "
          "**straight out** without twisting; do not burn it or apply "
          "kerosene/petrol; wash and disinfect; save the tick and watch for "
          "fever/rash. **Leech:** do not pull it off \u2014 apply salt, "
          "vinegar, lemon or a flame near it so that it drops off; then dress "
          "the bleeding point"],
         ["**Jellyfish / stingray / catfish (marine)**", "Severe burning pain, "
                                                        "linear weals, swelling; "
                                                        "collapse in severe "
                                                        "cases",
          "Get the casualty out of the water; **pour sea water (not fresh "
          "water) over a jellyfish sting and remove tentacles with gloves/a "
          "stick**; **immerse a stingray/fish sting in hot water (45 \u00b0C) "
          "for 30\u201390 minutes**; treat pain and refer"],
         ["**Human bite**", "Punctured/lacerated wound, heavily infected",
          "Wash thoroughly with soap and running water for 5 minutes, cover "
          "with a sterile dressing and **always refer** \u2014 antibiotics and "
          "tetanus prophylaxis are needed"],
         ["**Monkey, cat, bat, jackal, mongoose bite/scratch**",
          "Wound; **all are rabies-prone**",
          "Treat exactly like a **dog bite** (below) \u2014 wash, dress, "
          "hospital for anti-rabies treatment"]],
        weights=[2.5, 4.4, 5.7], size=8.4)

    # ------------------------------------------------------------------
    b.h2("Epistaxis (Nose Bleed)")
    b.box("DEFINITION AND CAUSES", [
        "**Epistaxis** is **bleeding from the nose**, usually from the rich "
        "network of vessels in the **front lower part of the nasal septum "
        "(Little's area / Kiesselbach's plexus)**.",
        "**Local causes:** **nose picking** (commonest in children), a blow on "
        "the nose, **fracture of the nose or of the base of the skull**, "
        "violent sneezing or nose blowing, foreign body, dryness of the air, "
        "infection (cold, sinusitis), polyp or tumour.",
        "**General causes:** **high blood pressure** (common in the elderly), "
        "heat and sun exposure, high altitude, **blood disorders (haemophilia, "
        "leukaemia, low platelets, dengue)**, liver disease, vitamin C or K "
        "deficiency, **medicines \u2014 aspirin, warfarin and other blood "
        "thinners**.",
    ], kind="def")
    b.h3("First aid")
    b.numbered([
        "**Sit the casualty down with the head bent slightly FORWARD** over a "
        "bowl \u2014 never tilt the head back (blood then runs into the throat, "
        "causing swallowing of blood, vomiting and possible choking).",
        "**Pinch the soft part of the nose (just below the bony bridge) firmly "
        "between the thumb and index finger and hold it continuously for 10 "
        "minutes**, without releasing to check.",
        "Tell the casualty to **breathe through the mouth** and to **spit out** "
        "any blood in the mouth rather than swallow it.",
        "Apply a **cold compress or ice pack over the bridge of the nose and the "
        "back of the neck**; loosen tight clothing at the neck.",
        "After 10 minutes, release gently. **If the bleeding continues, pinch "
        "for two further periods of 10 minutes.**",
        "When the bleeding stops, tell the casualty to **rest quietly, avoid "
        "blowing, picking or sniffing the nose, avoid hot drinks, alcohol, "
        "smoking and exertion for at least 4 hours (ideally 12\u201324 hours)**, "
        "and to sleep with the head slightly raised.",
        "**Seek medical help if:** bleeding lasts **more than 20\u201330 "
        "minutes** or is very heavy; it recurs repeatedly; it follows a "
        "**head injury** (the fluid may be **CSF** \u2014 suspect a fractured "
        "base of skull: do **not** pinch or plug the nose, cover lightly and "
        "let it drain); the casualty is on **blood thinners** or has a bleeding "
        "disorder, high blood pressure, or becomes pale, faint or shocked; or "
        "the casualty is a small child or elderly.",
    ])
    b.box("EPISTAXIS \u2014 REMEMBER", [
        "**Head FORWARD, not backward** \u2014 the single most-asked point.",
        "**Pinch the soft part for a full 10 minutes** \u2014 do not keep "
        "letting go.",
        "**Do not plug the nose with cotton wool** in first aid, and never plug "
        "it after a head injury.",
        "Do not let the casualty lie down flat or talk, laugh or cough.",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("Snake Bite")
    b.p("India has about 300 species of snakes, of which around **60 are "
        "venomous**. The **\u2018big four\u2019** responsible for almost all "
        "deaths are the **Indian cobra, common krait, Russell's viper and "
        "saw-scaled viper**. Most bites occur on the **legs and hands** of "
        "farmers and villagers, at night and in the monsoon.")
    b.table(
        ["Feature", "Venomous (poisonous) snake bite", "Non-venomous bite"],
        [["Fang marks", "**Two distinct puncture marks (fang marks)**, sometimes "
                        "one", "A **row of small teeth marks (horse-shoe "
                               "shape)**, no fang punctures"],
         ["Local reaction", "Severe burning pain, rapid **swelling, "
                            "discoloration, bleeding and blistering** (vipers); "
                            "little local change with a krait/cobra neurotoxic "
                            "bite", "Slight pain, minimal swelling"],
         ["General effects", "Present \u2014 see below", "**Absent** (only fear "
                                                        "and anxiety)"],
         ["Progress", "Symptoms **worsen** with time", "No progression"]],
        weights=[2.2, 5.4, 5.0])
    b.table(
        ["Type of venom", "Snakes", "Signs and symptoms"],
        [["**Neurotoxic** (acts on nerves)", "**Cobra, krait, sea snake, coral "
                                            "snake**",
          "**Drooping of the eyelids (ptosis), blurred/double vision, "
          "dribbling of saliva, difficulty in speaking and swallowing, weakness "
          "of the neck (\u2018broken neck sign\u2019), paralysis of limbs**, "
          "and finally **paralysis of the breathing muscles** \u2014 death from "
          "respiratory failure. A krait bite may be almost painless and is often "
          "noticed only in the morning with **abdominal pain and paralysis**"],
         ["**Vasculotoxic / haemotoxic** (acts on blood and vessels)",
          "**Russell's viper, saw-scaled viper, pit viper**",
          "**Severe local pain, rapid swelling, blistering and tissue death; "
          "bleeding from the gums, nose, wound and in urine and vomit; "
          "non-clotting blood; shock and kidney failure**"],
         ["**Myotoxic** (acts on muscle)", "Sea snakes",
          "Muscle pain and stiffness, dark urine, kidney failure"]],
        weights=[2.8, 3.2, 6.6], size=8.6)
    b.h3("First aid for snake bite \u2014 the modern protocol")
    b.numbered([
        "**Reassure the casualty** \u2014 about 70 % of bites are by "
        "non-venomous snakes and even venomous bites are often \u2018dry\u2019. "
        "**Fear itself can kill.** Keep him calm and still.",
        "**Immobilise the bitten limb** with a **splint and a sling/bandage, "
        "exactly as for a fracture**, and keep it **at or slightly below the "
        "level of the heart**. Movement pumps venom into the circulation.",
        "**Remove rings, bangles, watches, anklets and tight clothing or "
        "footwear** from the bitten limb before swelling starts.",
        "**Wash/wipe the bite gently with soap and water** (do not scrub) and "
        "cover it with a **clean dry dressing**.",
        "**Transport the casualty to hospital as quickly and as gently as "
        "possible** \u2014 preferably carried on a stretcher or a vehicle, "
        "**never walking or running**. ==Anti-snake venom (ASV) is the only "
        "effective treatment== and is available only in hospital.",
        "**Monitor breathing continuously** and be ready to give **artificial "
        "respiration/CPR** \u2014 in a cobra or krait bite, breathing may stop "
        "before the casualty reaches hospital.",
        "If possible, **note the description of the snake** (or photograph it "
        "from a safe distance). **Never try to catch or kill the snake**, but if "
        "it has already been killed, take it along carefully.",
        "**Nothing by mouth** \u2014 no food, no alcohol, no aspirin, no "
        "sedative, no stimulant.",
    ])
    b.box("SNAKE BITE \u2014 THE \u2018NEVERS\u2019 (all classical exam points)",
          [
        "**Never apply a tight tourniquet** \u2014 it causes gangrene and does "
        "not stop venom spread. (A **broad crepe pressure-immobilisation "
        "bandage**, as for a sprain, may be applied over the whole limb with a "
        "splint in a confirmed neurotoxic bite where transport is long \u2014 "
        "but only if trained; it must never be a narrow tight band.)",
        "**Never cut, slash, incise or scarify** the wound.",
        "**Never suck the venom out** with the mouth or with any device.",
        "**Never apply potassium permanganate, chillies, cow dung, herbs, "
        "kerosene, ice or a \u2018snake stone\u2019**, and never cauterise the "
        "wound.",
        "**Never give alcohol, aspirin or sedatives**, and never let the casualty "
        "walk.",
        "**Never rely on a snake charmer, mantra, tantrik or traditional "
        "healer** \u2014 the delay kills. Go straight to a hospital that has "
        "**ASV**.",
        "**Never wash away all traces** vigorously \u2014 gentle cleaning only "
        "(a swab may help identify the venom).",
    ], kind="warn")
    b.p("**Prevention:** wear **shoes and long trousers** in fields and at "
        "night, carry a **torch**, do not put hands into holes, grain stores, "
        "wood piles or under stones, **sleep on a cot under a mosquito net** "
        "(kraits bite sleepers on the floor), clear rubbish and rat holes round "
        "the house, and never handle or tease a snake.")

    # ------------------------------------------------------------------
    b.h2("Dog Bite and Rabies")
    b.table(
        ["Point", "Detail"],
        [["The danger", "**Rabies (hydrophobia)** \u2014 a **viral disease of "
                        "the brain that is almost 100 % fatal once symptoms "
                        "appear, but is completely preventable** by prompt "
                        "wound care and vaccination. India accounts for a large "
                        "share of the world's rabies deaths, and **dogs cause "
                        "about 95 %** of them"],
         ["Virus and spread", "**Rabies (Lyssa) virus**, present in the "
                              "**saliva** of an infected animal; enters through "
                              "a **bite, scratch, or a lick on broken skin or "
                              "mucous membrane**. Animals involved: **dog, cat, "
                              "monkey, jackal, fox, mongoose, bat, cattle, "
                              "horse** (**rodents like rats and squirrels, and "
                              "birds, do not transmit rabies**)"],
         ["Incubation period", "Usually **1\u20133 months** (range 5 days to "
                               "1 year or more) \u2014 shorter when the bite is "
                               "on the **face, head, neck or hands** or is "
                               "deep/multiple"],
         ["Features in the animal", "Change in behaviour, restlessness, "
                                    "**biting without provocation, drooling of "
                                    "saliva, hoarse bark, refusal of food and "
                                    "water, paralysis, death within 10 days**"],
         ["Features in man", "Pain, tingling or itching at the healed bite site; "
                             "fever, headache, anxiety; then **hydrophobia "
                             "(painful spasm of the throat at the sight or "
                             "thought of water)**, excessive salivation, "
                             "spasms, terror, delirium, paralysis, coma and "
                             "death"]],
        weights=[2.8, 9.8])
    b.h3("First aid for an animal bite \u2014 what you do decides the outcome")
    b.numbered([
        "==Wash the wound immediately and thoroughly with plenty of soap and "
        "running water for at least 15 minutes== \u2014 this is the **single "
        "most important step** and removes/kills much of the virus. Wash all "
        "bite and scratch sites.",
        "**Apply an antiseptic** \u2014 **povidone-iodine (Betadine)**, or 70 % "
        "alcohol/spirit, after washing.",
        "**Control bleeding** with direct pressure and cover with a **clean, "
        "loose, sterile dressing**.",
        "**Do NOT**: suture or tightly close the wound at once, apply chillies, "
        "lime, turmeric, oil, herbs, cow dung, kerosene, plaster or any "
        "irritant; do not cauterise; do not massage the wound; do not cover it "
        "with an air-tight dressing.",
        "**Take the casualty to a hospital/health centre at once** for:  "
        "\u2022 **Anti-rabies vaccine (ARV)** \u2014 modern cell-culture "
        "vaccine given **intramuscularly on days 0, 3, 7, 14 (and 28)** "
        "(Essen schedule), or intradermally as per the centre's protocol;  "
        "\u2022 **Rabies immunoglobulin (RIG)** infiltrated **around the "
        "wound** in **Category III** exposures (deep/multiple bites, bites on "
        "the head, face, neck, hands or genitals, licks on broken skin, bat "
        "exposure);  "
        "\u2022 **Tetanus prophylaxis** and **antibiotics** as required.",
        "**Observe the animal for 10 days** if it can be safely confined; if it "
        "remains healthy, the course may be modified by the doctor. If the "
        "animal is stray, unknown, dead, or behaving abnormally, "
        "**complete the full course**.",
        "**Never delay** vaccination to \u2018see what happens\u2019 \u2014 once "
        "symptoms begin, rabies cannot be cured.",
    ])
    b.table(
        ["WHO category", "Type of exposure", "Treatment"],
        [["**Category I**", "Touching or feeding an animal; **licks on intact "
                           "skin**", "**No treatment** (wash the area)"],
         ["**Category II**", "**Nibbling of uncovered skin; minor scratches or "
                            "abrasions without bleeding**",
          "Wash + **vaccine**"],
         ["**Category III**", "**Single or multiple transdermal bites, "
                             "scratches with bleeding; licks on broken skin or "
                             "mucous membrane; contact with bats**",
          "Wash + **vaccine + rabies immunoglobulin (RIG)**"]],
        weights=[2.4, 6.0, 4.2])
    b.p("**Prevention:** vaccinate pet dogs and cats yearly, control and "
        "sterilise stray dogs, do not tease or feed stray animals, teach "
        "children not to approach strange dogs, never disturb a feeding or "
        "sleeping dog or a bitch with pups, and report bites promptly. "
        "**World Rabies Day \u2014 28 September.**")

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "**Foreign body in ear/nose:** never probe \u2014 refer to a doctor; for "
        "an **insect in the ear** float it out with warm oil or water; "
        "**never use water for seeds** (they swell).",
        "**Foreign body in the eye:** never rub; irrigate from the **inner to "
        "the outer corner**; never remove an embedded or corneal object; "
        "**chemical splash \u2192 20 minutes of running water**.",
        "**Cramps:** stretch the muscle (calf \u2192 straighten the knee and "
        "pull the toes up), massage, warmth and **ORS/salted water**.",
        "**Frost-bite:** re-warm with **water at 37\u201340 \u00b0C**; "
        "**never rub, never use dry heat, never break blisters, never let it "
        "re-freeze**.",
        "**Hypothermia** = core temperature **below 35 \u00b0C**; re-warm "
        "gradually, handle gently, warm sweet drinks, no alcohol.",
        "**Heat stroke** \u2014 **hot dry skin, no sweating, temperature above "
        "40 \u00b0C, confusion** \u2192 cool rapidly, emergency; **heat "
        "exhaustion** \u2014 pale, clammy, sweating \u2192 ORS and rest.",
        "**Bee sting** \u2192 **scrape the sting out sideways**, cold compress; "
        "watch for **anaphylaxis**; sting in the mouth \u2192 ice to suck + "
        "ambulance.",
        "**Scorpion sting** \u2192 pain relief, cold compress, immobilise, "
        "hospital (especially a child); **no tourniquet, no cutting**.",
        "**Epistaxis** \u2192 **sit up, head forward, pinch the soft part for "
        "10 minutes**, cold compress, no blowing for 4 hours.",
        "**Snake bite** \u2192 **reassure, immobilise like a fracture, keep the "
        "limb at/below heart level, rush to hospital for ASV**; "
        "**no tourniquet, no cutting, no sucking, no alcohol, no traditional "
        "healers**.",
        "**Dog bite** \u2192 **wash with soap and running water for 15 "
        "minutes**, antiseptic, loose dressing, **anti-rabies vaccine (days 0, "
        "3, 7, 14, 28) + RIG for Category III** + tetanus cover.",
    ])
