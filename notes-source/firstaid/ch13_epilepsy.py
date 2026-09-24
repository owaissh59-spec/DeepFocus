# -*- coding: utf-8 -*-
"""Chapter 13 - Epilepsy and Hysteria."""


def render(b):
    b.chapter(
        "Epilepsy and Hysteria",
        "Epilepsy \u2014 causes, types of seizure, the phases of a major fit, "
        "first aid, status epilepticus; hysteria \u2014 features, management and "
        "the classical differences from an epileptic fit.",
        syllabus=[
            "Epilepsy \u2014 definition, causes, types (major and minor), aura, "
            "phases of a fit, signs and symptoms, complete first aid, status "
            "epilepticus and when to call an ambulance.",
            "Hysteria \u2014 definition, causes, signs and symptoms, first-aid "
            "management, and the difference between an epileptic and a "
            "hysterical fit.",
        ])

    # ------------------------------------------------------------------
    b.h2("Epilepsy \u2014 Meaning and Causes")
    b.box("DEFINITIONS", [
        "**Epilepsy** is a **chronic disorder of the brain characterised by "
        "recurrent (two or more) unprovoked seizures**, caused by sudden, "
        "excessive and disorderly electrical discharges of the brain cells.",
        "A **seizure (fit, convulsion)** is the **event** \u2014 a sudden burst "
        "of abnormal electrical activity producing involuntary movements, "
        "abnormal sensations, or loss of consciousness. A person may have a "
        "**single provoked seizure** (fever, head injury, low sugar, poison) "
        "**without having epilepsy**.",
        "**Aura** \u2014 a brief warning sensation felt by some casualties just "
        "before a fit: a strange smell or taste, flashing lights, a rising "
        "feeling in the stomach, giddiness or a sense of fear. It gives the "
        "casualty time to lie down.",
        "**Ictal** = during the fit; **post-ictal** = the period of recovery "
        "after it.",
    ], kind="def")
    b.table(
        ["Group of causes", "Examples"],
        [["**Idiopathic / primary (commonest)**", "No demonstrable cause; often "
                                                 "begins in childhood or "
                                                 "adolescence; hereditary "
                                                 "tendency"],
         ["**Structural brain disease**", "**Head injury** and birth injury, "
                                         "brain tumour, stroke, scar from an "
                                         "old injury or operation, cerebral "
                                         "palsy, congenital malformation"],
         ["**Infections**", "Meningitis, encephalitis, cerebral malaria, "
                            "**neurocysticercosis (pork tapeworm \u2014 a very "
                            "common cause in India)**, brain abscess, "
                            "tuberculoma"],
         ["**Metabolic / toxic**", "**Low blood sugar (hypoglycaemia)**, low "
                                   "calcium or sodium, kidney and liver "
                                   "failure, **alcohol and drug withdrawal**, "
                                   "poisoning (lead, insecticides, camphor), "
                                   "high fever in children, eclampsia of "
                                   "pregnancy, oxygen lack (asphyxia, cardiac "
                                   "arrest)"],
         ["**Precipitating (trigger) factors**", "Missed anti-epileptic "
                                                 "medicine (the commonest "
                                                 "trigger), lack of sleep, "
                                                 "fatigue, stress, **flashing "
                                                 "or flickering lights**, "
                                                 "television/video games, "
                                                 "alcohol, menstruation, fever, "
                                                 "hunger"]],
        weights=[3.2, 9.4])

    # ------------------------------------------------------------------
    b.h2("Types of Seizure")
    b.table(
        ["Type", "Features"],
        [["**Generalised tonic-clonic (major fit, \u2018grand mal\u2019)**",
          "The classical fit \u2014 sudden loss of consciousness with stiffening "
          "and then jerking of the whole body; the type described in every "
          "first-aid syllabus"],
         ["**Absence seizure (minor fit, \u2018petit mal\u2019)**",
          "Chiefly in children \u2014 a **sudden, brief (5\u201330 second) "
          "\u2018blank stare\u2019** with stopping of activity, fluttering "
          "eyelids and slight twitching of the lips or fingers; **no fall, no "
          "convulsion**, and the child resumes what he was doing as if nothing "
          "happened. Often mistaken for day-dreaming or inattention"],
         ["**Myoclonic seizure**", "Sudden brief jerks of the arms or legs, "
                                   "usually without loss of consciousness"],
         ["**Atonic (\u2018drop attack\u2019)**", "Sudden loss of muscle tone "
                                                 "\u2014 the casualty collapses "
                                                 "limply; injuries are common"],
         ["**Tonic seizure**", "Generalised stiffening only"],
         ["**Focal (partial) seizure \u2014 simple**", "Twitching or abnormal "
                                                      "sensation in one part "
                                                      "(hand, face) with "
                                                      "**consciousness "
                                                      "preserved**"],
         ["**Focal seizure \u2014 complex (psychomotor)**", "Altered awareness "
                                                          "with **automatic "
                                                          "behaviour** \u2014 "
                                                          "lip smacking, "
                                                          "chewing, plucking at "
                                                          "clothes, aimless "
                                                          "wandering; the "
                                                          "casualty appears "
                                                          "dazed and does not "
                                                          "remember it"],
         ["**Status epilepticus**", "**A fit lasting more than 5 minutes, or "
                                    "repeated fits without recovery of "
                                    "consciousness in between** \u2014 a "
                                    "**life-threatening emergency**"],
         ["**Febrile convulsion**", "Fit provoked by high fever in a child of "
                                    "6 months to 6 years \u2014 not epilepsy"]],
        weights=[3.2, 9.4], size=8.8)

    # ------------------------------------------------------------------
    b.h2("Phases of a Major (Tonic-Clonic) Fit")
    b.table(
        ["Phase", "Duration", "What is seen"],
        [["**1. Aura (warning)**", "Seconds", "Strange smell, taste, sound, "
                                             "light, giddiness, epigastric "
                                             "sensation or fear \u2014 present "
                                             "in only some casualties"],
         ["**2. Tonic phase**", "**10\u201330 seconds**",
          "**Sudden loss of consciousness and a fall** (the casualty may utter a "
          "sharp \u2018**epileptic cry**\u2019 as air is forced out); the whole "
          "body becomes **rigid**, the back arches, the jaws clench, the "
          "**breathing stops** and the face and lips become **blue "
          "(cyanosed)**; the pupils dilate"],
         ["**3. Clonic (convulsive) phase**", "**1\u20132 minutes (rarely up to "
                                             "5)**",
          "**Violent jerking movements** of the limbs and body; noisy difficult "
          "breathing; **frothing or foaming at the mouth**, often blood-stained "
          "from a **bitten tongue**; the eyes roll up; **involuntary passing of "
          "urine (sometimes stool)**; profuse sweating"],
         ["**4. Post-ictal (recovery) phase**", "**Minutes to hours**",
          "The muscles relax and breathing becomes normal; the casualty is "
          "**deeply unconscious, then dazed, confused, exhausted, with headache "
          "and muscle aches**; he **does not remember the fit**; he may fall "
          "into a deep sleep for several hours; occasionally there is "
          "**automatic behaviour** or temporary weakness of a limb"]],
        weights=[3.0, 2.6, 7.2])

    # ------------------------------------------------------------------
    b.h2("First Aid During and After an Epileptic Fit")
    b.h3("What to DO")
    b.numbered([
        "**Stay calm, note the time** the fit began and stay with the casualty "
        "throughout.",
        "**Protect him from injury** \u2014 clear away furniture, hot objects, "
        "sharp objects, glass and spectacles; **place something soft under the "
        "head** (a folded coat, cushion or your hands); loosen tight clothing at "
        "the neck.",
        "**Let the fit take its course** \u2014 do not interfere with the "
        "movements.",
        "**Ask onlookers to move back** and protect the casualty's **privacy and "
        "dignity** (cover him if he has passed urine).",
        "**When the jerking stops**, open the airway, check breathing and place "
        "him in the **recovery position**; wipe away froth and saliva.",
        "**Note the details for the doctor** \u2014 what happened before the fit, "
        "which part started moving first, how long it lasted, whether he passed "
        "urine or bit his tongue, and how long the recovery took.",
        "**Stay until he is fully recovered and oriented** \u2014 reassure him "
        "gently, tell him where he is, and let him rest or sleep; arrange for "
        "someone to take him home.",
        "Treat any **injury** sustained in the fall.",
    ])
    b.box("WHAT NEVER TO DO DURING A FIT \u2014 GUARANTEED EXAM QUESTION", [
        "**Do NOT put anything in the mouth** \u2014 no spoon, no cloth, no "
        "finger, no key, no wooden stick. It breaks teeth, injures the mouth and "
        "may block the airway. (The old teaching about preventing tongue biting "
        "is **wrong and dangerous**.)",
        "**Do NOT restrain the casualty** or try to hold down the limbs \u2014 it "
        "causes fractures and dislocations.",
        "**Do NOT move** the casualty unless he is in danger (fire, water, "
        "traffic, machinery).",
        "**Do NOT throw water on the face**, slap, shake or shout at him.",
        "**Do NOT give anything by mouth** \u2014 no water, no tablets \u2014 "
        "until he is **fully conscious** and able to swallow.",
        "**Do NOT try to bring him round** with smelling salts or by making him "
        "smell an onion or a shoe.",
        "**Do NOT leave him alone** while he is drowsy or confused.",
    ], kind="warn")
    b.h3("When to call an ambulance (112 / 108)")
    b.bullets([
        "The fit lasts **more than 5 minutes** (status epilepticus) or fits "
        "**recur one after another** without full recovery.",
        "It is the casualty's **first known fit**, or the cause is unknown.",
        "The casualty is **injured** in the fit, or has **breathing "
        "difficulty** after it.",
        "He **does not regain consciousness** within 10\u201315 minutes, or "
        "remains confused for a long time.",
        "The casualty is **pregnant**, **diabetic**, **elderly**, a **child**, or "
        "the fit happened **in water**.",
        "There is a **head injury**, high fever with a rash or stiff neck "
        "(**meningitis**), or a known poisoning/overdose.",
    ])
    b.h3("Minor fits (absence seizures)")
    b.bullets([
        "Remove any source of danger; **do not interrupt or shake** the casualty.",
        "Talk to him quietly, stay with him until he is fully alert, and "
        "reassure him \u2014 he may not know he has had an attack.",
        "Guide him gently away from danger if he wanders; advise medical "
        "assessment, especially in a child whose \u2018day-dreaming\u2019 is "
        "frequent.",
    ])
    b.h3("Living with epilepsy \u2014 advice the first aider can give")
    b.bullets([
        "**Take the medicines regularly and never stop them suddenly**; keep a "
        "record of fits.",
        "**Get enough sleep**, avoid alcohol and avoid known triggers such as "
        "flickering lights and computer/TV strain.",
        "**Avoid dangerous situations** \u2014 swimming alone, climbing heights, "
        "cooking on an open flame, operating machinery, and driving (until "
        "certified fit).",
        "**Take showers rather than baths**, keep bathroom doors unlocked, use "
        "guards on fires and heaters.",
        "**Carry a medical card or bracelet** and tell friends, teachers and "
        "colleagues what to do.",
    ])

    # ------------------------------------------------------------------
    b.h2("Hysteria (Conversion / Dissociative Disorder)")
    b.box("DEFINITION", [
        "**Hysteria** is a **psychological (functional) disorder in which "
        "emotional conflict is unconsciously converted into physical symptoms** "
        "\u2014 fits, paralysis, blindness, aphonia (loss of voice), "
        "over-breathing or dramatic collapse \u2014 **without any organic "
        "disease of the body**.",
        "It is not pretending (that is **malingering**, which is conscious). The "
        "casualty genuinely experiences the symptoms, but they **serve a purpose "
        "\u2014 attention, escape or sympathy** and are almost always produced "
        "**in the presence of other people**.",
        "Commoner in **young women and adolescents**, in emotional, suggestible "
        "personalities and after a quarrel, bereavement, fright, examination "
        "stress or family conflict.",
    ], kind="def")
    b.h3("Signs and symptoms of a hysterical attack")
    b.bullets([
        "**Dramatic, theatrical behaviour** \u2014 shouting, screaming, crying, "
        "laughing, abusing, tearing clothes or hair, rolling on the ground.",
        "**Apparent fit**: wild, purposeless, **thrashing and writhing "
        "movements** that are **not the regular jerking of epilepsy**; arching "
        "of the back; the attack **worsens when watched** and stops when the "
        "audience leaves.",
        "**Consciousness is not truly lost** \u2014 the eyelids resist opening "
        "and flutter, the pupils react normally, and the casualty avoids being "
        "hurt (the arm held above the face does not fall on it).",
        "**No injury, no tongue bite, no passing of urine, no cyanosis**, and "
        "**no true post-ictal confusion or sleep**.",
        "Other presentations: **over-breathing (hyperventilation) with tingling "
        "and cramp of the hands, a lump in the throat (globus), sudden inability "
        "to speak, walk, see or move a limb**, with normal reflexes.",
        "The attack occurs **only before an audience** and often has an obvious "
        "**emotional trigger**.",
    ])
    b.h3("First aid for hysteria")
    b.numbered([
        "**Be firm, calm, kind and confident** \u2014 neither scold nor "
        "sympathise excessively.",
        "**Remove the audience** \u2014 ask onlookers to leave quietly; this "
        "alone often ends the attack.",
        "**Protect the casualty from injury** but do **not** restrain him "
        "forcibly.",
        "**Speak quietly and reassuringly**, addressing the casualty by name; "
        "ask simple questions and give simple instructions (\u2018breathe slowly "
        "with me\u2019).",
        "Do **not** slap, shake, shout at, throw water over or otherwise "
        "humiliate the casualty; these worsen the attack and are "
        "unprofessional.",
        "Do **not** discuss the emotional cause in front of others; do not give "
        "medicines.",
        "**Never assume hysteria until all physical causes are excluded** "
        "\u2014 always check the **airway, breathing, pulse, pupils and blood "
        "sugar**. Epilepsy, hypoglycaemia, head injury, poisoning, tetany and "
        "heart disease can all look \u2018hysterical\u2019.",
        "After the attack, allow the casualty to rest, and **advise medical / "
        "psychiatric assessment and counselling** \u2014 the underlying stress "
        "needs treatment; attacks are otherwise likely to recur.",
    ])

    # ------------------------------------------------------------------
    b.h2("Epileptic Fit versus Hysterical Fit \u2014 the Classical Table")
    b.table(
        ["Point", "Epileptic fit", "Hysterical fit"],
        [["Nature", "**Organic** \u2014 abnormal electrical discharge in the "
                    "brain", "**Functional/psychological** \u2014 emotional in "
                             "origin"],
         ["Onset", "**Sudden**, any time, may be preceded by an **aura**",
          "Gradual, **after an emotional upset**, and always with an "
          "**audience**"],
         ["Time and place", "**Anywhere, any time, even during sleep or when "
                            "alone**", "**Only in the presence of others**, "
                                       "never during sleep"],
         ["Cry", "A sharp **\u2018epileptic cry\u2019** at the onset",
          "Continuous shouting, screaming, crying or talking"],
         ["Fall", "Falls **suddenly and heavily**, and may be **injured**",
          "Sinks down carefully in a **safe place \u2014 rarely injured**"],
         ["Consciousness", "**Truly lost**", "**Not truly lost** \u2014 aware of "
                                             "the surroundings"],
         ["Movements", "**Regular, rhythmic tonic then clonic** convulsions",
          "**Irregular, purposeless, dramatic thrashing**, resisting help"],
         ["Eyes and pupils", "Eyes roll up; **pupils dilated and not reacting**; "
                             "eyelids can be opened easily",
          "Eyelids **tightly closed, flutter and resist opening**; **pupils "
          "normal and reacting**"],
         ["Face", "**Blue (cyanosed)**, congested", "Normal colour or flushed"],
         ["Tongue bite", "**Common** \u2014 blood-stained froth", "**Never**"],
         ["Incontinence", "**Passing of urine (and sometimes stool) is common**",
          "**Absent**"],
         ["Duration", "**1\u20132 minutes**, then deep sleep",
          "**Prolonged \u2014 may last many minutes to hours**, and stops when "
          "the audience leaves"],
         ["After the fit", "**Confused, exhausted, headache, muscle pain, deep "
                           "sleep; no memory of the fit**",
          "**Recovers abruptly and completely**; **often remembers** the event; "
          "no true sleep"],
         ["Response to a firm word or removing the audience", "**None**",
          "**Attack subsides**"],
         ["Self-injury / dangerous acts", "May burn or injure himself",
          "**Avoids injury** \u2014 will not let a raised arm fall on his own "
          "face"]],
        weights=[2.2, 5.2, 5.4], size=8.4)

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Epilepsy = **recurrent unprovoked seizures** from abnormal electrical "
        "discharges of the brain; a **single** provoked fit is not epilepsy.",
        "Major fit phases: **aura \u2192 tonic (10\u201330 s, rigid, blue, "
        "breathing stops) \u2192 clonic (1\u20132 min, jerking, froth, tongue "
        "bite, incontinence) \u2192 post-ictal (confusion, sleep, no memory)**.",
        "Commonest trigger = **missed medicine**; commonest identifiable cause in "
        "India = **neurocysticercosis**.",
        "**Never put anything in the mouth, never restrain, never throw water, "
        "never give anything by mouth till fully conscious.**",
        "**Status epilepticus = fit > 5 minutes or repeated fits** \u2014 call an "
        "ambulance at once.",
        "After the fit \u2192 **recovery position**, note the timing and details, "
        "stay until fully oriented.",
        "**Absence (petit mal)** = brief blank stare in children, no fall, no "
        "convulsion.",
        "**Hysteria** = emotional conflict converted into physical symptoms; "
        "occurs **only before an audience**; **no tongue bite, no incontinence, "
        "no cyanosis, no injury, pupils normal**.",
        "Management of hysteria = **firm, calm reassurance + remove the "
        "audience**; never slap or throw water; always exclude physical "
        "causes first.",
    ])
