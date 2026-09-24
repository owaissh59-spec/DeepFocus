# -*- coding: utf-8 -*-
"""Chapter 14 - Poisons including Food Poisoning."""


def render(b):
    b.chapter(
        "Poisons including Food Poisoning",
        "Classification of poisons, routes of entry, general principles of "
        "management, individual poisons and their antidotes, alcohol and drug "
        "poisoning, food poisoning and its prevention.",
        syllabus=[
            "Poisons \u2014 definition, classification, routes of entry, "
            "general signs and symptoms, general first-aid management, when to "
            "induce vomiting and when not.",
            "Individual poisons \u2014 corrosives, kerosene and petroleum, "
            "insecticides, dhatura, opium, sedatives, alcohol, paracetamol, "
            "aspirin, carbon monoxide, rat poison and aluminium phosphide, plant "
            "poisons, and their antidotes.",
            "Food poisoning \u2014 types, causes, incubation period, signs, "
            "first aid, ORS and prevention; botulism and mushroom poisoning.",
        ])

    # ------------------------------------------------------------------
    b.h2("Definition and Classification of Poisons")
    b.box("DEFINITIONS", [
        "A **poison** is **any substance which, when taken into or applied to the "
        "body in sufficient quantity, damages health or destroys life** by its "
        "chemical action.",
        "**Toxicology** is the study of poisons; an **antidote** is a substance "
        "that counteracts a poison; the **lethal dose** is the smallest amount "
        "that can kill.",
        "Poisoning may be **accidental** (commonest in children), **suicidal** "
        "(commonest in adults in India \u2014 insecticides and medicines), "
        "**homicidal**, or **occupational/environmental**.",
        "**Every case of poisoning is a medico-legal case** \u2014 preserve the "
        "container, the vomit and any remaining substance, and inform the police "
        "where suicide or homicide is suspected.",
    ], kind="def")
    b.table(
        ["Basis", "Classes and examples"],
        [["**Action on the body**",
          "**1. Corrosives** \u2014 destroy tissue on contact: strong acids "
          "(sulphuric, nitric, hydrochloric, **carbolic acid/phenol**) and "
          "strong alkalis (caustic soda/potash, ammonia, lime, drain cleaner).  "
          "**2. Irritants** \u2014 inflame the gut: arsenic, copper sulphate, "
          "zinc, croton oil, cantharides, food poisons.  "
          "**3. Systemic / neurotics** \u2014 act on the nervous system: opium, "
          "dhatura, alcohol, barbiturates, organophosphates, strychnine, snake "
          "venom.  "
          "**4. Cardiac poisons** \u2014 oleander, aconite, digitalis, nicotine.  "
          "**5. Asphyxiants** \u2014 carbon monoxide, carbon dioxide, cyanide, "
          "hydrogen sulphide."],
         ["**Route of entry**", "**Ingested** (swallowed \u2014 commonest), "
                                "**inhaled** (gases, fumes, vapours), "
                                "**absorbed** through the skin, eyes or mucous "
                                "membrane (insecticides, phenol), **injected** "
                                "(drugs, stings, bites)"],
         ["**Source**", "**Household** (bleach, detergent, acid, kerosene, "
                        "camphor, naphthalene, phenyl), **agricultural** "
                        "(pesticides, weed killers, rat poison), "
                        "**medicinal** (overdose of tablets), **industrial** "
                        "(lead, mercury, arsenic, solvents), **plant and "
                        "animal** (dhatura, oleander, mushroom, snake, "
                        "scorpion), **food** (bacterial and chemical)"],
         ["**Speed of action**", "**Acute** (single large dose \u2014 rapid "
                                 "effects) and **chronic** (small repeated "
                                 "doses \u2014 lead, arsenic, mercury)"]],
        weights=[2.6, 10.0], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Recognition \u2014 General Signs and Symptoms")
    b.table(
        ["Route", "Typical signs and symptoms"],
        [["**Swallowed**", "Burns, stains or blisters **round the mouth and "
                           "lips**; **peculiar smell of the breath** (kerosene, "
                           "alcohol, insecticide, bitter almonds); nausea, "
                           "vomiting, abdominal pain, diarrhoea; burning pain "
                           "from mouth to stomach; drowsiness, delirium, "
                           "convulsions, unconsciousness; shock"],
         ["**Inhaled**", "Breathlessness, cough, tightness of the chest, "
                         "**cyanosis (or cherry-red skin in CO poisoning)**, "
                         "headache, giddiness, confusion, collapse; often "
                         "**several people affected together**"],
         ["**Absorbed (skin/eye)**", "Redness, burning, blistering, swelling, "
                                     "itching or numbness of the contaminated "
                                     "area; sweating; later systemic effects"],
         ["**Injected**", "Puncture marks, local pain and swelling; rapid "
                          "systemic effects; syringes or needles nearby"],
         ["**Clues at the scene**", "Open bottles, blister packs, tablets, a "
                                    "suicide note, a farm sprayer, a smell in "
                                    "the room, vomit, spilt liquid, a "
                                    "**charcoal fire or gas geyser** in a "
                                    "closed room"]],
        weights=[2.8, 9.8])
    b.box("PUPIL SIGNS \u2014 A GIFT TO THE EXAMINER", [
        "**Pin-point (constricted) pupils** \u2192 **opium/morphine/heroin**, "
        "**organophosphate insecticides**, mushroom (muscarine), some sedatives.",
        "**Widely dilated pupils** \u2192 **dhatura/atropine/belladonna**, "
        "cocaine, amphetamine, **alcohol**, antihistamines, cyanide, deep "
        "unconsciousness and cardiac arrest.",
        "**Cherry-red skin** \u2192 **carbon monoxide**; **blue (cyanosed)** "
        "\u2192 asphyxiant poisons; **yellow (jaundiced)** \u2192 phosphorus, "
        "paracetamol, mushroom (late).",
        "**Smell of the breath:** bitter almonds \u2192 **cyanide**; garlic "
        "\u2192 **phosphorus/arsenic/aluminium phosphide**; kerosene \u2192 "
        "petroleum; acetone/sweet \u2192 diabetic coma; alcohol \u2192 ethanol "
        "(but beware \u2014 a drunk man may also be injured or hypoglycaemic).",
    ], kind="exam")

    # ------------------------------------------------------------------
    b.h2("General First-Aid Management of Poisoning")
    b.p("The **four aims** are: (1) **remove the poison or the casualty from "
        "it**, (2) **prevent further absorption**, (3) **maintain the vital "
        "functions (airway, breathing, circulation)**, and (4) **get the "
        "casualty and the poison to hospital quickly**.")
    b.numbered([
        "**Protect yourself first** \u2014 wear gloves; do not touch a corrosive "
        "or insecticide with bare hands; ventilate a gas-filled room from "
        "outside; never enter a confined space without breathing apparatus.",
        "**Remove the casualty from the poison**, or the poison from the "
        "casualty \u2014 fresh air for gases, remove contaminated clothing, "
        "wash the skin with plenty of water and soap for **at least 15\u201320 "
        "minutes**, irrigate eyes with running water for 20 minutes.",
        "**Assess DRABC.** If unconscious but breathing \u2192 **recovery "
        "position** (this also helps vomit to drain). If not breathing \u2192 "
        "**CPR**, using a **face mask or shield** if there is poison on the lips "
        "(never mouth-to-mouth with corrosives, cyanide or "
        "organophosphates).",
        "**Ask what, when, how much and why** \u2014 and **keep the evidence**: "
        "container, label, tablets, plant, vomit. This is the single most useful "
        "thing you can do for the doctor.",
        "**Do NOT induce vomiting** (see below) and do **not** give salt water, "
        "mustard water or any \u2018universal antidote\u2019.",
        "**If the poison is corrosive** and the casualty is fully conscious, wash "
        "the mouth out and give **small sips of cold water or milk** to dilute "
        "and soothe (about 250 ml in an adult; some authorities allow milk or "
        "water only if hospital is more than 30 minutes away).",
        "**Nothing by mouth** in an unconscious, convulsing or drowsy casualty.",
        "**Keep the casualty warm and quiet**, treat for shock, and **monitor "
        "breathing, pulse and level of response every 10 minutes**.",
        "**Telephone 112/108 and the poison information centre "
        "(1800-11-6117, AIIMS)** for advice; transport to hospital at once, in "
        "the recovery position, with a written note of the time and amount "
        "taken.",
        "For **suspected suicide**, stay with the casualty, remove any remaining "
        "tablets or poison out of reach, be non-judgemental, and inform the "
        "police/family; arrange psychiatric help afterwards.",
    ])
    b.box("VOMITING \u2014 WHEN NEVER TO INDUCE IT", [
        "**Modern rule: a first aider should NOT induce vomiting at all.** "
        "Gastric lavage and activated charcoal are hospital procedures.",
        "It is **absolutely forbidden** when the poison is: "
        "**(a) a corrosive** (acid or alkali \u2014 it will burn the gullet "
        "again and may perforate it); "
        "**(b) a petroleum product** (kerosene, petrol, diesel, thinner, "
        "furniture polish \u2014 it will be inhaled and cause fatal "
        "**chemical pneumonitis**); "
        "**(c) phenol/carbolic acid**; "
        "**(d)** the casualty is **unconscious, drowsy or convulsing**; "
        "**(e)** the casualty is a **pregnant woman, a heart patient or a very "
        "young child**.",
        "**Never use salt water** to induce vomiting \u2014 it can itself kill "
        "by salt poisoning.",
        "If the casualty vomits **on his own**, turn the head to the side, keep "
        "the airway clear and **save a sample of the vomit** for the hospital.",
    ], kind="warn")

    # ------------------------------------------------------------------
    b.h2("Individual Poisons \u2014 Recognition and First Aid")
    b.table(
        ["Poison", "Signs and symptoms", "First aid / antidote"],
        [["**Strong acids** (sulphuric, nitric, hydrochloric \u2014 *tezaab*)",
          "Burning pain from mouth to stomach; **stains and burns round the "
          "mouth** (black/brown with sulphuric, yellow with nitric); vomiting of "
          "blood-stained material; difficulty in swallowing and speaking; shock",
          "**Never induce vomiting, never give sodium bicarbonate** (gas may "
          "rupture the stomach). Wash the mouth; give **small sips of cold water "
          "or milk**; wash contaminated skin with copious water for 20 min; "
          "airway care; urgent hospital"],
         ["**Strong alkalis** (caustic soda/potash, lime, ammonia, drain and "
          "oven cleaner)",
          "Soapy, slippery burns round the mouth; severe burning pain; vomiting; "
          "swelling of the throat with airway obstruction",
          "**Never induce vomiting, never give an acid (vinegar/lemon)**. Sips of "
          "cold water or milk; watch the airway closely; urgent hospital"],
         ["**Carbolic acid / phenol / dettol-type disinfectants**",
          "**Smell of phenol**, white burns round the mouth, painless numbness of "
          "the mouth, vomiting, giddiness, **dark (smoky) urine**, collapse",
          "No vomiting; wipe and wash the mouth and skin (**with vegetable oil "
          "or plenty of water**); airway care; hospital"],
         ["**Kerosene, petrol, diesel, thinner, turpentine, furniture polish**",
          "Smell of the fluid, burning of the mouth and throat, vomiting, "
          "**coughing and rapid breathing** (aspiration into the lungs), fever, "
          "drowsiness, fits",
          "==Absolutely NO vomiting== (aspiration is the killer). Keep the "
          "casualty **upright and calm**, give nothing by mouth, remove "
          "soaked clothing, oxygen if trained; urgent hospital"],
         ["**Organophosphate / carbamate insecticides** (malathion, parathion, "
          "monocrotophos, dimethoate \u2014 the commonest serious poisoning in "
          "rural India)",
          "**Pin-point pupils**, **excessive salivation, sweating, tears and "
          "urination**, vomiting, abdominal colic, diarrhoea, **muscle "
          "twitching and weakness**, **slow pulse**, frothing at the mouth, "
          "**smell of the insecticide/garlic**, difficulty in breathing, "
          "convulsions, coma (remember **SLUDGE**: Salivation, Lacrimation, "
          "Urination, Defaecation, Gastric cramps, Emesis)",
          "**Remove all contaminated clothing and wash the skin and hair "
          "thoroughly with soap and water** (wear gloves \u2014 it is absorbed "
          "through skin); airway suction/positioning; **do not do "
          "mouth-to-mouth**; rush to hospital \u2014 the antidote is "
          "**atropine (+ pralidoxime)**"],
         ["**Dhatura, belladonna, atropine, *Datura* seeds** (often used "
                                                              "criminally)",
          "**Widely dilated pupils and blurred vision**, dry hot flushed skin, "
          "**dry mouth**, fast pulse, high temperature, **delirium, "
          "hallucinations and excitement** (\u2018mad as a hatter, red as a "
          "beet, dry as a bone, blind as a bat, hot as a hare\u2019), retention "
          "of urine, coma",
          "Airway and cooling measures; protect the excited casualty from injury; "
          "hospital (antidote **physostigmine**; sedation)"],
         ["**Opium, morphine, heroin, codeine (opioids)**",
          "**Pin-point pupils**, drowsiness \u2192 coma, **slow shallow "
          "breathing**, cyanosis, cold clammy skin, needle marks, slow pulse",
          "Airway and **artificial respiration** (breathing stops before the "
          "heart); recovery position; hospital \u2014 antidote **naloxone**"],
         ["**Barbiturates, benzodiazepines and sleeping tablets**",
          "Drowsiness, slurred speech, unsteadiness, slow shallow breathing, "
          "coma; empty blister packs nearby",
          "Airway, recovery position, artificial respiration if needed; keep the "
          "strips for the doctor; hospital (antidote for benzodiazepines is "
          "**flumazenil**)"],
         ["**Alcohol (ethyl)**", "Smell of drink, flushed face, unsteady gait, "
                                "slurred speech, excitement then drowsiness, "
                                "vomiting, **dilated pupils**, deep noisy "
                                "breathing, coma with **hypoglycaemia and "
                                "hypothermia**",
          "Recovery position, keep **warm** (the casualty loses heat rapidly), "
          "never leave him alone or let him \u2018sleep it off\u2019 unattended; "
          "**never assume it is only drink** \u2014 look for head injury and low "
          "blood sugar; hospital if unconscious"],
         ["**Methyl alcohol (methanol, spurious liquor)**",
          "Vomiting, abdominal pain, **blurring of vision and blindness**, deep "
          "rapid breathing (acidosis), coma \u2014 often **several victims "
          "together**",
          "Urgent hospital \u2014 the antidote is **ethanol/fomepizole** and "
          "dialysis; save the bottle; inform authorities"],
         ["**Paracetamol overdose**", "Very few symptoms for the first "
                                     "24\u201348 hours, then nausea, vomiting "
                                     "and **liver failure with jaundice** "
                                     "\u2014 dangerous because it looks "
                                     "harmless at first",
          "**Hospital at once, even if the casualty feels well** \u2014 the "
          "antidote **N-acetylcysteine** must be given within 8\u201310 hours"],
         ["**Aspirin (salicylate) overdose**", "Ringing in the ears and "
                                              "deafness, nausea and vomiting, "
                                              "**deep rapid breathing**, "
                                              "sweating, fever, confusion, "
                                              "bleeding from the stomach",
          "Hospital urgently; sips of water/milk if fully conscious; keep the "
          "packet"],
         ["**Iron tablets (common in children)**", "Vomiting of blood, diarrhoea, "
                                                  "abdominal pain, shock, later "
                                                  "liver damage",
          "Hospital at once (antidote **desferrioxamine**); count the missing "
          "tablets"],
         ["**Carbon monoxide**", "Headache, giddiness, nausea, weakness, "
                                "confusion, **cherry-red skin**, collapse; "
                                "**whole family affected**; source = charcoal "
                                "*angeethi*, gas geyser, car exhaust",
          "Ventilate and remove to **fresh air** (protect yourself), "
          "**100 % oxygen** if available, CPR if needed; hospital \u2014 may "
          "need **hyperbaric oxygen**"],
         ["**Cyanide** (industrial, silver polish, bitter almonds, some seeds)",
          "**Smell of bitter almonds**, sudden giddiness, headache, gasping "
          "breathing, **bright red skin**, convulsions, instant collapse",
          "Fresh air, **do not do direct mouth-to-mouth** (use a mask/bag), "
          "oxygen, immediate hospital \u2014 antidote kit (hydroxocobalamin, "
          "sodium thiosulphate/nitrite)"],
         ["**Aluminium phosphide (Celphos, \u2018rice tablet\u2019, wheat pill)**",
          "**Garlic-like smell of the breath**, vomiting, severe **abdominal "
          "pain, intractable shock**, difficulty in breathing \u2014 very "
          "**high mortality; no antidote**",
          "Do **not** induce vomiting; nothing by mouth; airway and oxygen; "
          "**immediate** hospital; keep the tablet/wrapper; ventilate the room "
          "(phosphine gas is released and can affect the rescuer)"],
         ["**Rat poison (zinc/barium phosphide, warfarin-type)**",
          "Vomiting, abdominal pain, garlic smell (phosphide) or **bleeding from "
          "the gums, nose and in urine** (warfarin type)",
          "Hospital; **vitamin K** is the antidote for warfarin-type poisons; "
          "keep the packet"],
         ["**Naphthalene balls, camphor, phenyl (household)**",
          "Vomiting, abdominal pain, excitement, **convulsions** (camphor), "
          "dark urine and anaemia (naphthalene)",
          "Nothing by mouth if fitting; recovery position; hospital"],
         ["**Copper sulphate (*neela thotha*)**", "Metallic taste, **blue-green "
                                                 "vomit**, burning abdominal "
                                                 "pain, jaundice, kidney "
                                                 "failure",
          "Nothing by mouth; hospital urgently"],
         ["**Plant poisons \u2014 oleander (*kaner*), aconite, castor seed, "
          "abrus, yellow oleander seeds**",
          "Vomiting, abdominal pain, **slow or irregular pulse and heart block** "
          "(oleander/aconite), tingling and numbness of the mouth (aconite), "
          "collapse",
          "Nothing by mouth; complete rest lying down; **cardiac monitoring "
          "needed** \u2014 rush to hospital with a sample of the plant/seed"],
         ["**Lead, arsenic, mercury (chronic/occupational)**",
          "Colicky abdominal pain, constipation, anaemia, **blue line on the "
          "gums** and wrist drop (lead); vomiting, rice-water stools, garlic "
          "breath (arsenic); tremor, salivation, mental changes (mercury)",
          "Remove from exposure, wash the skin, hospital for chelation "
          "(**BAL, EDTA, penicillamine**)"]],
        weights=[2.9, 4.8, 4.5], size=8.2)

    # ------------------------------------------------------------------
    b.h2("Common Antidotes \u2014 Quick Table")
    b.table(
        ["Poison", "Antidote"],
        [["Organophosphate insecticide", "**Atropine** + pralidoxime (2-PAM)"],
         ["Opium / morphine / heroin", "**Naloxone**"],
         ["Paracetamol", "**N-acetylcysteine** (oral methionine)"],
         ["Benzodiazepines", "**Flumazenil**"],
         ["Dhatura / atropine", "**Physostigmine / neostigmine**"],
         ["Cyanide", "**Hydroxocobalamin, sodium nitrite + sodium "
                     "thiosulphate**"],
         ["Carbon monoxide", "**Oxygen** (100 %, hyperbaric if severe)"],
         ["Methanol / ethylene glycol", "**Ethanol or fomepizole**"],
         ["Iron", "**Desferrioxamine**"],
         ["Lead / arsenic / mercury", "**BAL (dimercaprol), EDTA, "
                                      "penicillamine**"],
         ["Warfarin / rat poison", "**Vitamin K** (+ fresh frozen plasma)"],
         ["Snake venom", "**Polyvalent anti-snake venom (ASV)**"],
         ["Aluminium phosphide", "**None** \u2014 supportive treatment only"],
         ["General adsorbent (many swallowed poisons)",
          "**Activated charcoal** \u2014 hospital use only, not for corrosives, "
          "petroleum, iron, alcohol or cyanide"]],
        weights=[4.6, 6.0])

    # ------------------------------------------------------------------
    b.h2("Food Poisoning")
    b.box("DEFINITION", [
        "**Food poisoning** is an **acute illness of the stomach and intestine "
        "caused by eating food or drinking water contaminated with bacteria, "
        "their toxins, viruses, parasites, chemicals or natural poisons**.",
        "It usually causes **vomiting, diarrhoea and abdominal pain** within a "
        "few hours of the meal, and **often affects several people who ate the "
        "same food** \u2014 an outbreak.",
        "The chief danger is **dehydration and shock**, especially in children, "
        "the elderly and the sick.",
    ], kind="def")
    b.h3("Types and causes")
    b.table(
        ["Type", "Organism / agent", "Incubation", "Typical source and features"],
        [["**Bacterial \u2014 toxin type**", "***Staphylococcus aureus***",
          "**1\u20136 hours** (very short)",
          "Cream cakes, custard, milk products, cooked meat handled by a person "
          "with a boil or septic finger. **Severe vomiting and cramps, little or "
          "no fever**"],
         ["**Bacterial \u2014 infective type**", "***Salmonella***",
          "**12\u201336 hours**",
          "Under-cooked **egg, poultry, meat**, unpasteurised milk. Fever, "
          "abdominal pain, diarrhoea, vomiting, headache"],
         ["", "***Clostridium perfringens***", "8\u201322 hours",
          "Meat and gravy kept warm for long. Cramps and diarrhoea; vomiting "
          "unusual"],
         ["", "***Bacillus cereus***", "1\u20135 h (vomiting type) or "
                                       "8\u201316 h (diarrhoeal type)",
          "**Re-heated/left-over rice**, pasta"],
         ["", "***E. coli*** (ETEC, O157)", "12\u201372 hours",
          "Contaminated water, salad, under-cooked minced meat. Watery or bloody "
          "diarrhoea"],
         ["", "***Vibrio cholerae***", "Hours\u20135 days",
          "Contaminated water \u2014 **painless profuse \u2018rice-water\u2019 "
          "stools**, rapid dehydration and collapse"],
         ["", "***Shigella*** (bacillary dysentery)", "1\u20133 days",
          "Person-to-person, water, flies \u2014 **blood and mucus in the "
          "stool**, fever, tenesmus"],
         ["", "***Clostridium botulinum*** (**botulism**)",
          "**12\u201336 hours**",
          "**Improperly canned, tinned, bottled or fermented food**; the toxin "
          "attacks nerves \u2014 **double vision, drooping eyelids, dry mouth, "
          "difficulty in speaking and swallowing, descending paralysis and "
          "paralysis of breathing**. Little or no diarrhoea. **Highly fatal "
          "\u2014 needs antitoxin and ventilation**"],
         ["**Viral**", "Rotavirus, Norovirus, Hepatitis A and E",
          "1\u20133 days (hepatitis 2\u20136 weeks)",
          "Water, shellfish, food handled by an infected person; vomiting and "
          "watery diarrhoea; hepatitis A/E \u2192 jaundice"],
         ["**Parasitic**", "*Entamoeba histolytica*, *Giardia*, tapeworm, "
                           "roundworm", "Days\u2013weeks",
          "Contaminated water and raw vegetables \u2014 chronic loose stools, "
          "cramps, weight loss"],
         ["**Chemical**", "Insecticide residues, **metal contamination (zinc, "
                          "copper, tin from utensils)**, food colours, "
                          "adulterants, **argemone oil in mustard oil "
                          "(epidemic dropsy)**",
          "Minutes\u2013hours", "Metallic taste, vomiting, cramps; specific "
                                "features by chemical"],
         ["**Natural toxins**", "**Poisonous mushrooms**, red kidney beans "
                                "(raw), *khesari dal* (**lathyrism**), fish "
                                "toxins (scombroid, puffer fish), sprouted "
                                "potato (solanine), **aflatoxin from mouldy "
                                "groundnut/maize**",
          "Hours\u2013days", "Vomiting and cramps; mushroom may cause liver and "
                             "kidney failure after 6\u201324 hours; aflatoxin "
                             "causes liver damage"]],
        weights=[2.6, 3.1, 2.1, 5.0], size=8.0)
    b.h3("Signs and symptoms")
    b.bullets([
        "**Nausea and repeated vomiting**, **abdominal pain and cramps**, "
        "**diarrhoea** (watery, or with blood and mucus), flatulence.",
        "Fever, headache, malaise, weakness and muscle aches.",
        "**Signs of dehydration** \u2014 intense thirst, dry mouth and tongue, "
        "sunken eyes, loss of skin elasticity (pinched skin stays up), **sunken "
        "fontanelle in a baby**, little or no urine, irritability, drowsiness; "
        "in severe cases **shock** with a rapid weak pulse and cold clammy skin.",
        "**Several people affected after the same meal** \u2014 the hallmark of "
        "an outbreak.",
    ])
    b.h3("First aid for food poisoning")
    b.numbered([
        "**Rest** the casualty lying down, with a bowl and towel at hand; "
        "reassure him.",
        "**Give plenty of fluid in small, frequent sips** \u2014 the mainstay of "
        "treatment. Best is **ORS (oral rehydration solution)**: one WHO sachet "
        "in **1 litre of clean water**; alternatively home-made \u2014 "
        "**1 teaspoon (a pinch, ~2.6 g) of salt + 6 teaspoons (~27 g) of sugar "
        "in 1 litre of boiled cooled water**, or rice water (*kanji*), lemon "
        "water, coconut water, buttermilk, dal water.",
        "Give ORS **after every loose stool**: about 50\u2013100 ml for a small "
        "child, 100\u2013200 ml for an older child and **as much as an adult "
        "wants**.",
        "**Do not give** aerated drinks, very sweet drinks, strong tea or coffee, "
        "alcohol, milk in large amounts, or any **anti-diarrhoeal medicine on "
        "your own** (they can be dangerous, especially in children and in "
        "dysentery).",
        "Once vomiting stops, offer **light bland food** \u2014 rice, khichdi, "
        "banana, toast, curd, boiled potato (the \u2018BRAT\u2019 idea); "
        "continue breast-feeding a baby throughout.",
        "**Keep a sample of the suspected food, the vomit and the stool** for "
        "examination, and note what was eaten, when and by whom.",
        "**Maintain strict hygiene** \u2014 wash hands, disinfect the toilet, "
        "keep the casualty's utensils separate.",
        "**Call a doctor / go to hospital** if: the casualty is a **baby, a small "
        "child, elderly, pregnant or already ill**; there is **blood in the stool "
        "or vomit**; **high fever**; **severe or continuous vomiting** so that "
        "fluids cannot be kept down; **signs of dehydration or shock**; symptoms "
        "last **more than 2\u20133 days**; there are **nervous symptoms (double "
        "vision, difficulty in swallowing or breathing, weakness)** suggesting "
        "**botulism**; or **mushroom or chemical poisoning** is suspected.",
        "If the casualty becomes unconscious \u2014 **recovery position**, "
        "nothing by mouth, call an ambulance.",
        "**Notify** the health authority if many people are affected (a public "
        "health emergency), e.g. after a marriage feast or in a hostel.",
    ])
    b.box("PREVENTION OF FOOD POISONING \u2014 THE FIVE KEYS (WHO)", [
        "**1. Keep clean** \u2014 wash hands with soap before cooking and eating "
        "and after using the toilet; keep the kitchen, utensils and cloths "
        "clean; keep flies, rats and pets away; a food handler with diarrhoea, "
        "a boil or a septic finger **must not handle food**.",
        "**2. Separate raw and cooked food** \u2014 use different knives and "
        "boards; store raw meat below cooked food in the refrigerator.",
        "**3. Cook thoroughly** \u2014 especially meat, poultry, eggs and "
        "seafood; the centre should reach **70 \u00b0C**; re-heat leftovers "
        "until piping hot, and **never re-heat rice more than once**.",
        "**4. Keep food at safe temperatures** \u2014 do not leave cooked food at "
        "room temperature for more than **2 hours**; keep hot food above "
        "**60 \u00b0C** and cold food below **5 \u00b0C**; the **danger zone is "
        "5\u201360 \u00b0C**; thaw frozen food in the refrigerator, not on the "
        "counter.",
        "**5. Use safe water and raw materials** \u2014 boiled or treated water, "
        "pasteurised milk, washed fruit and vegetables, no bulging or rusted "
        "tins, no food past its **expiry date**, no cut fruit or uncovered food "
        "from the roadside.",
        "Cover food, cover water containers, use a ladle (not hands) to serve, "
        "and never taste food that smells or looks doubtful \u2014 "
        "**\u2018when in doubt, throw it out\u2019**.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("Prevention of Poisoning in General")
    b.bullets([
        "Keep **all medicines, insecticides, kerosene, acids, phenyl and "
        "cleaning agents locked away, out of the reach and sight of children**, "
        "and never in a cupboard with food.",
        "**Never store a poison in a soft-drink, water or milk bottle**, and "
        "never remove the original label.",
        "Read the label and dose **before** giving any medicine; never take "
        "medicine in the dark; never take someone else's prescription; discard "
        "expired medicines safely.",
        "**Never call medicine \u2018sweets\u2019** to persuade a child; use "
        "child-resistant caps.",
        "Follow the instructions when spraying pesticides \u2014 wear protective "
        "clothing, a mask and gloves, spray downwind, do not eat or smoke while "
        "spraying, and wash thoroughly afterwards.",
        "Ensure **ventilation** when using charcoal fires, gas geysers, paints "
        "and solvents; service gas appliances; fit a CO alarm if possible.",
        "Keep the numbers of the hospital, ambulance (**108**) and the "
        "**National Poisons Information Centre (1800-11-6117)** near the "
        "telephone.",
    ])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Poison = substance that **damages health or destroys life by chemical "
        "action**; routes = **swallowed, inhaled, absorbed, injected**.",
        "Classes = **corrosive, irritant, systemic/neurotic, cardiac, "
        "asphyxiant**.",
        "**Never induce vomiting** \u2014 above all with **corrosives, kerosene/"
        "petroleum, phenol**, or in an **unconscious or convulsing** casualty; "
        "**never use salt water**.",
        "**Always save the container, tablets, plant and vomit** \u2014 and treat "
        "every poisoning as a **medico-legal case**.",
        "**Pin-point pupils** = opium or organophosphate; **dilated pupils** = "
        "dhatura/atropine, alcohol; **cherry-red skin** = carbon monoxide; "
        "**garlic breath** = aluminium phosphide/phosphorus; **bitter almonds** "
        "= cyanide.",
        "Organophosphate poisoning \u2192 **SLUDGE signs**, wash the skin, "
        "antidote **atropine**; opioid \u2192 **naloxone**; paracetamol \u2192 "
        "**N-acetylcysteine**; CO \u2192 **oxygen**.",
        "**Aluminium phosphide (Celphos) has no antidote** and a very high "
        "mortality.",
        "Food poisoning is commonest from **Staphylococcus (1\u20136 h, "
        "vomiting)** and **Salmonella (12\u201336 h, fever)**; **botulism** "
        "(canned food) causes **paralysis and double vision**.",
        "Treatment of food poisoning = **rest + ORS in small frequent sips**; "
        "**ORS = 1 sachet in 1 litre** of clean water, or 1 tsp salt + 6 tsp "
        "sugar per litre.",
        "Prevention = **WHO five keys**: keep clean, separate raw and cooked, "
        "cook thoroughly, keep at safe temperature (danger zone **5\u201360 "
        "\u00b0C**), use safe water and raw material.",
    ])
