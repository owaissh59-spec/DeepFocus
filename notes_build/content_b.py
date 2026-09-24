"""Chapters 6-9 : Observation of the Sick, Infection, Surgical Techniques, Diet."""


def chapter_6(b):
    b.chapter(6, "Observation of the Sick",
              "General observation, vital signs, TPR charting, intake-output and interpretation of findings")

    b.section_h("6.1", "Meaning and Importance of Observation")
    b.box("def", [
        "__Observation__ — the deliberate, systematic use of all the senses (sight, hearing, smell, touch) to collect information about the patient's condition.",
        "Nightingale: ~'The most important practical lesson to be given to nurses is to teach them what to observe, how to observe, which symptoms indicate improvement and which the reverse.'~",
    ])
    b.bullets([
        "__Purposes__ — to know the patient's condition and progress, to detect complications early, to judge the effect of treatment, to plan nursing care, to give accurate reports and to keep legal records.",
        "__Methods__ — ~inspection~ (look), ~palpation~ (feel), ~percussion~ and ~auscultation~ (listen), ~olfaction~ (smell), plus talking to the patient and measuring with instruments.",
        "Observation must be __continuous, systematic, objective (facts, not guesses), accurate and promptly reported__.",
        "__Subjective data (symptoms)__ = what the patient says (pain, nausea, giddiness); __objective data (signs)__ = what the nurse sees and measures (rash, vomiting, BP 150/90).",
    ])

    b.section_h("6.2", "General (Head-to-Foot) Observation")
    b.table(
        ["What to observe", "Points to note / abnormal findings and meaning"],
        [["General appearance and build", "Well/ill-looking, obese or emaciated (cachexia), posture, hygiene, dress"],
         ["Level of consciousness", "Alert → drowsy → confused → delirious → stuporous → semi-comatose → comatose; restlessness is an early sign of hypoxia, pain, a full bladder or shock"],
         ["Face (facies)", "Anxious, pinched (peritonitis), flushed (fever), puffy (nephritis, myxoedema), 'risus sardonicus' (tetanus), mask-like (Parkinsonism)"],
         ["Skin colour", "__Pallor__ (anaemia, shock, haemorrhage); __cyanosis__ — bluish, central on the tongue/lips (heart-lung disease) or peripheral on the fingers (cold, poor circulation) — appears when SpO2 is below about 85% or 5 g/dL of reduced Hb; __jaundice__ — yellow of skin, sclera, urine (liver, bile duct, haemolysis; visible when bilirubin is over 2-3 mg/dL); __redness/erythema__, pigmentation, cherry-red (carbon monoxide)"],
         ["Skin condition", "Dryness, sweating, rash, petechiae/purpura, bruising, ulcer, oedema (press over the tibia for 5 s — pitting), turgor (pinch test — poor in dehydration), temperature, itching"],
         ["Eyes", "Sunken (dehydration), puffy lids (renal), yellow sclera, pallor of conjunctiva, pupil size and reaction (pin-point in opioid poisoning/pontine lesion; dilated fixed in death, atropine, brain damage), squint, discharge, vision"],
         ["Mouth and tongue", "Dry/coated/furred tongue (dehydration, fever), sordes, ulcers, thrush, bleeding gums, smooth red tongue (vitamin B deficiency), cracked lips, halitosis; __smell of breath__ — acetone (ketoacidosis), ammonia/urine (uraemia), foul (lung abscess), alcohol"],
         ["Neck", "Stiffness (meningitis), raised jugular veins (heart failure), goitre, lymph nodes"],
         ["Chest and breathing", "Rate, rhythm, depth, use of accessory muscles, in-drawing, wheeze, cough and sputum, chest pain, symmetry"],
         ["Abdomen", "Distension, rigidity, tenderness, visible peristalsis, bowel sounds, girth, hernia, stoma"],
         ["Limbs", "Power, movement, deformity, contracture, swelling, calf tenderness (deep vein thrombosis), colour, peripheral pulses, capillary refill (normal <2-3 s)"],
         ["Elimination", "Urine — amount, colour, deposit, smell, frequency, burning, retention or incontinence; stool — frequency, consistency, colour, blood, mucus, worms"],
         ["Sleep and behaviour", "Insomnia, disturbed sleep, irritability, depression, anxiety, hallucination, co-operation"],
         ["Appetite, thirst, weight", "Anorexia, nausea, excessive thirst (diabetes), loss or gain of weight"],
         ["Pain", "Site, onset, character, radiation, severity (0-10 scale), duration, aggravating and relieving factors"]],
        caption="Table 6.1  Systematic observation of the patient")

    b.section_h("6.3", "Vital Signs — Body Temperature")
    b.box("def", ["__Body temperature__ = balance between heat produced (metabolism, muscle activity, food, hormones) and heat lost (radiation, conduction, convection, evaporation). It is regulated by the __hypothalamus__ (the body's thermostat)."])
    b.table(
        ["Site", "Normal average", "Normal range", "Time to keep the thermometer"],
        [["__Oral (mouth)__", "37 °C / 98.6 °F", "36.4-37.2 °C (97.6-99.0 °F)", "2-3 minutes"],
         ["__Axilla (armpit)__", "36.5 °C / 97.6 °F (~0.5 °C less than oral)", "35.9-36.7 °C", "3-5 minutes (safest for children and the unconscious)"],
         ["__Rectal__", "37.5 °C / 99.6 °F (~0.5 °C more than oral)", "37.0-38.1 °C", "1-2 minutes (most accurate; lubricate and insert 2-4 cm)"],
         ["__Tympanic (ear)__", "37.5 °C", "Near core temperature", "2-5 seconds (infrared)"],
         ["__Forehead/temporal, non-contact__", "36.5-37.3 °C", "Screening only", "Instant"]],
        caption="Table 6.2  Sites for recording temperature")
    b.sub("Conversion formulae (asked very often)")
    b.box("num", [
        "__°F = (°C × 9/5) + 32__      __°C = (°F − 32) × 5/9__",
        "Useful values: 36.1 °C = 97 °F • 37 °C = 98.6 °F • 38 °C = 100.4 °F • 39 °C = 102.2 °F • 40 °C = 104 °F • 41 °C = 105.8 °F",
    ])
    b.sub("Terms and grades of temperature")
    b.table(
        ["Term", "Meaning"],
        [["__Pyrexia / fever__", "Temperature above 37.2-38 °C (99-100.4 °F)"],
         ["Low grade / moderate / high fever", "Up to 38.3 °C / 38.4-39.4 °C / above 39.5 °C"],
         ["__Hyperpyrexia__", "Above __41 °C (105.8 °F)__ — a medical emergency; may cause convulsions and brain damage"],
         ["__Hypothermia__", "Below __35 °C (95 °F)__ — newborn, elderly, exposure, drowning, hypothyroidism"],
         ["__Afebrile / apyrexia__", "Absence of fever"],
         ["Onset, fastigium (stadium), defervescence", "Beginning, highest plateau and fall of fever"],
         ["__Crisis__ / __Lysis__", "Sudden fall of temperature to normal (with sweating) / gradual fall over days"],
         ["__Constant (continuous) fever__", "Remains high, fluctuates less than 1 °C, never touches normal — lobar pneumonia, typhoid (2nd week), UTI"],
         ["__Remittent fever__", "Fluctuates more than 2 °C but never reaches normal — typhoid, infective endocarditis, sepsis"],
         ["__Intermittent fever__", "Rises and falls to normal daily; __quotidian__ = daily, __tertian__ = every 48 h (~P. vivax/ovale~), __quartan__ = every 72 h (~P. malariae~) — malaria, kala-azar, pyaemia"],
         ["__Relapsing fever__", "Febrile periods alternating with 1-2 afebrile days (~Borrelia~); __Pel-Ebstein fever__ in Hodgkin's lymphoma"],
         ["__Inverse fever__", "Temperature higher in the morning than the evening — tuberculosis"]],
        caption="Table 6.3  Types and patterns of fever")
    b.sub("Clinical thermometer and precautions")
    b.bullets([
        "A mercury clinical thermometer is graduated __35-42 °C (94-108 °F)__; it has a __constriction/kink__ above the bulb so the mercury does not fall back; it must be __shaken down below 35 °C__ before use.",
        "A __rectal thermometer has a short blunt (pear-shaped) bulb__; an oral thermometer has a long slender bulb; each patient (or each site) should have a separate thermometer, kept in a dry container or disinfectant, and wiped __from the stem towards the bulb__ before use.",
        "__Never use hot water__ to clean it (mercury expands and the bulb bursts); if a mercury thermometer breaks in the mouth, do not induce vomiting — remove the pieces, wash the mouth and inform the doctor. Digital and infrared thermometers have now replaced mercury ones (mercury is toxic and is being phased out).",
        "__Do not take an oral temperature__ in: infants and children under 5-6 years, the unconscious, confused or uncooperative, mouth breathers, oxygen mask/nasal tube, after mouth surgery or with sores in the mouth, convulsive or shivering patients. Wait __15-30 minutes__ after hot/cold drinks, food, smoking or chewing.",
        "__Avoid the rectal route__ in rectal surgery, diarrhoea, piles, cardiac patients (vagal stimulation) and newborns (risk of perforation).",
        "__Avoid the axilla__ when it is sweaty or there is local inflammation; dry the axilla and place the bulb in the centre with the arm across the chest.",
    ])
    b.sub("Factors affecting body temperature")
    b.bullets([
        "__Raise it__ — exercise, hot bath/hot weather, meals, emotion/stress, ovulation and pregnancy, infection, dehydration, hyperthyroidism, drugs (atropine), heat stroke, brain injury (hypothalamic).",
        "__Lower it__ — sleep and early morning (temperature is __lowest between 2 and 6 a.m., highest between 4 and 8 p.m.__), starvation, old age, shock, haemorrhage, hypothyroidism, cold exposure, alcohol, sedatives.",
        "__Age__ — newborns and the aged have poor temperature regulation.",
    ])
    b.sub("Nursing care in fever and in hyperpyrexia")
    b.bullets([
        "Bed rest, light clothing and light bed covers, good ventilation, cool room.",
        "__Plenty of fluids (3 L/day if allowed)__ — ORS, fruit juice, barley water; light, bland, high-calorie, easily digested food in small frequent feeds.",
        "__Tepid sponging / cold sponging__ for temperature above 39.5-40 °C: water at 27-32 °C (or tepid), long strokes to the limbs, cold compresses to the forehead, axillae and groins (over the large vessels), stop if shivering occurs; recheck the temperature after 30 minutes.",
        "Antipyretic as prescribed (__paracetamol 10-15 mg/kg per dose__ in children; maximum 4 g/day in adults); tepid sponging is an adjunct, ~never use ice-cold water or alcohol rubs~.",
        "Mouth care 2-4 hourly (dry mouth, sordes), skin care and change of damp linen after sweating, observe for __convulsions, delirium, dehydration and herpes on the lips__.",
        "Record temperature 4-hourly (2-hourly or continuously in hyperpyrexia); watch the urine output.",
    ])

    b.section_h("6.4", "Vital Signs — Pulse")
    b.box("def", ["__Pulse__ — the wave of expansion and recoil felt over a superficial artery each time the left ventricle contracts and forces blood into the already full aorta."])
    b.table(
        ["Age group", "Normal pulse (beats/min)"],
        [["Newborn (0-1 month)", "__120-160__ (up to 180 when crying)"],
         ["Infant (1-12 months)", "100-160"],
         ["Toddler (1-3 years)", "90-140"],
         ["Pre-school (3-6 years)", "80-120"],
         ["School child (6-12 years)", "75-110"],
         ["Adolescent / adult", "__60-100 (average 72)__"],
         ["Elderly", "60-100 (may be slower, less elastic vessels)"],
         ["Trained athlete", "45-60"]],
        caption="Table 6.4  Normal pulse rate by age", align_center_cols=(1,))
    b.sub("Sites for feeling the pulse")
    b.bullets([
        "__Radial__ (wrist, thumb side) — the site of routine counting; __brachial__ (inner elbow) — used for BP and for the ~infant's pulse in CPR~; __carotid__ (side of the neck) — used in ~adult CPR / collapse~; __femoral__ (groin); __popliteal__ (behind the knee); __posterior tibial and dorsalis pedis__ (foot — checked in diabetes and peripheral vascular disease); __temporal__ (in front of the ear, used in children); __apical (apex beat)__ — heard with a stethoscope at the 5th left intercostal space just inside the mid-clavicular line; __umbilical cord/brachial__ in newborns.",
        "Count for __one full minute__ (especially if irregular; 30 s × 2 is acceptable if regular) with the __first two or three fingers (never the thumb__ — it has its own pulse).",
    ])
    b.sub("Characteristics to record")
    b.table(
        ["Character", "Description and abnormalities"],
        [["__Rate__", "Beats/min. __Tachycardia__ = above 100 (fever — the pulse rises about 10 beats per 1 °F/18 beats per °C, exercise, pain, anxiety, haemorrhage, shock, anaemia, thyrotoxicosis, heart failure, atropine, adrenaline). __Bradycardia__ = below 60 (sleep, athletes, myxoedema, jaundice, raised intracranial pressure, heart block, digoxin, beta blockers, opioids)"],
         ["__Rhythm__", "Regular or irregular. __Arrhythmia/dysrhythmia__; regularly irregular (sinus arrhythmia of children), irregularly irregular (__atrial fibrillation__); __ectopic/dropped beat__"],
         ["__Volume / amplitude__", "Full and bounding (exercise, hypertension, fever), __weak, thready, feeble__ (shock, haemorrhage, heart failure, dehydration); __imperceptible__; __water-hammer/collapsing__ (aortic regurgitation); __pulsus paradoxus__ (fall in pulse volume with inspiration — cardiac tamponade, severe asthma); __pulsus alternans__ (alternating strong and weak — LV failure)"],
         ["__Tension / character__", "Compressibility of the vessel wall; hard, tortuous vessel in arteriosclerosis"],
         ["__Equality__", "Compare both sides; an absent or unequal pulse suggests embolism, aortic dissection, coarctation or a tight bandage/plaster"],
         ["__Pulse deficit__", "Apical (heart) rate minus radial rate — present in atrial fibrillation"]],
        caption="Table 6.5  Characteristics of the pulse")

    b.section_h("6.5", "Vital Signs — Respiration")
    b.table(
        ["Age", "Normal respiratory rate (breaths/min)"],
        [["Newborn", "__30-60__"], ["Infant (1-12 months)", "30-50"], ["1-3 years", "24-40"],
         ["3-6 years", "22-34"], ["6-12 years", "18-30"], ["Adolescent/adult", "__12-20 (average 16-18)__"],
         ["Elderly", "16-24"]],
        caption="Table 6.6  Normal respiratory rate", align_center_cols=(1,))
    b.bullets([
        "Count the respirations __without the patient knowing__ (while apparently still feeling the pulse), for one full minute, by watching the rise and fall of the chest or abdomen.",
        "Normal pulse : respiration ratio is about __4-5 : 1__.",
        "Observe __rate, rhythm, depth, character, sound, effort, symmetry, and the colour of the patient__.",
    ])
    b.table(
        ["Term", "Meaning"],
        [["__Eupnoea__", "Normal quiet breathing"],
         ["__Tachypnoea__ / __Bradypnoea__", "Abnormally rapid (over 20-24) / abnormally slow (under 12) breathing"],
         ["__Apnoea__", "Absence of breathing"],
         ["__Dyspnoea__", "Difficult or laboured breathing (the patient is 'short of breath')"],
         ["__Orthopnoea__", "Breathlessness on lying flat, relieved by sitting up — left heart failure"],
         ["__Paroxysmal nocturnal dyspnoea__", "Sudden night-time breathlessness waking the patient — heart failure"],
         ["__Hyperpnoea / hyperventilation__", "Deep, rapid breathing → may cause dizziness and tingling (respiratory alkalosis)"],
         ["__Hypoventilation__", "Shallow, slow breathing → CO2 retention"],
         ["__Cheyne-Stokes respiration__", "Rhythmic waxing and waning of depth with periods of apnoea — heart failure, uraemia, brain damage, terminal illness, and normally in infants"],
         ["__Kussmaul's breathing__", "Deep, sighing, rapid 'air hunger' — __diabetic ketoacidosis__ and metabolic acidosis"],
         ["__Biot's / ataxic breathing__", "Irregular breaths with irregular apnoea — meningitis, brain stem damage"],
         ["__Stertorous / snoring__", "Noisy breathing due to obstruction of the upper airway — unconscious patient, apoplexy"],
         ["__Stridor__", "Harsh, high-pitched crowing noise on inspiration — laryngeal obstruction, croup, foreign body (an emergency)"],
         ["__Wheeze / rhonchi__", "Musical whistling, mainly expiratory — asthma, bronchitis"],
         ["__Crepitations (crackles/rales)__", "Fine bubbling sounds — pneumonia, pulmonary oedema, bronchiectasis"],
         ["__Grunting, nasal flaring, chest retraction__", "Signs of respiratory distress in an __infant__ (pneumonia)"],
         ["__Asphyxia / anoxia / hypoxia / hypoxaemia__", "Failure of air exchange / absence of oxygen in tissue / reduced tissue oxygen / reduced oxygen in blood"],
         ["__Cyanosis__", "Bluish discolouration when reduced haemoglobin exceeds 5 g/dL (SpO2 under about 85%)"],
         ["__Haemoptysis / Epistaxis__", "Coughing up blood / bleeding from the nose"]],
        caption="Table 6.7  Terms describing respiration")
    b.box("num", [
        "__Pulse oximetry (SpO2)__ — normal __95-100%__; below 94% needs attention; __below 90% = hypoxia__ requiring oxygen; below 85% = severe hypoxia. Falsely low readings occur with cold hands, nail polish, poor perfusion and movement; falsely high in carbon monoxide poisoning and anaemia.",
        "WHO fast-breathing cut-offs for childhood pneumonia: __under 2 months: 60/min or more; 2-12 months: 50/min or more; 1-5 years: 40/min or more__.",
    ])

    b.section_h("6.6", "Vital Signs — Blood Pressure")
    b.box("def", [
        "__Blood pressure__ — the lateral force exerted by circulating blood on the walls of the arteries, expressed as ~systolic/diastolic~ in mmHg.",
        "__Systolic__ = maximum pressure during ventricular contraction; __diastolic__ = minimum pressure during ventricular relaxation.",
        "__Pulse pressure__ = systolic − diastolic (normally __30-40 mmHg__).  __Mean arterial pressure (MAP)__ = diastolic + 1/3 of the pulse pressure (normal __70-105 mmHg__; a MAP of at least 60-65 mmHg is needed to perfuse the organs).",
    ])
    b.table(
        ["Category (adults, ACC/AHA and JNC)", "Systolic (mmHg)", "Diastolic (mmHg)"],
        [["__Normal__", "Below 120", "and below 80"],
         ["Elevated / high-normal", "120-129", "and below 80"],
         ["__Pre-hypertension__ (JNC-7)", "120-139", "or 80-89"],
         ["__Hypertension Stage 1__", "130-139 (JNC: 140-159)", "or 80-89 (90-99)"],
         ["__Hypertension Stage 2__", "140 or more (JNC: 160+)", "or 90 or more (100+)"],
         ["__Hypertensive crisis / emergency__", "Above 180", "and/or above 120"],
         ["__Hypotension__", "Below 90", "or below 60"]],
        caption="Table 6.8  Classification of blood pressure", align_center_cols=(1, 2))
    b.sub("Technique and sources of error")
    b.bullets([
        "Instruments: __sphygmomanometer__ (mercury, aneroid or digital) and a stethoscope; the pressure is heard as __Korotkoff sounds__ — phase 1 = systolic, disappearance (phase 5) = diastolic.",
        "The patient should rest __5 minutes__, sit or lie with the arm supported at __heart level__, feet on the floor, no talking; no smoking, caffeine or exercise for 30 minutes; the __cuff bladder should cover 80% of the arm circumference and about 40% of its width__ and be placed 2.5 cm above the elbow crease, with the mercury column at eye level.",
        "Inflate 20-30 mmHg above the point where the radial pulse disappears, then deflate slowly at __2-3 mmHg per second__; wait 1-2 minutes before repeating; record the arm used and the position.",
        "__Common errors__ — cuff too narrow or loose (falsely __high__), cuff too wide (falsely low), arm below heart level (high), arm above heart level (low), rapid deflation (systolic low, diastolic high), full bladder/pain/anxiety ('white-coat' hypertension) and the ~auscultatory gap~ (missing 20-40 mmHg) leading to under-reading if the cuff is not inflated high enough.",
        "__Avoid__ the arm with an intravenous infusion, arteriovenous fistula, lymphoedema/after mastectomy, fracture, plaster, burn or paralysis.",
        "__Postural (orthostatic) hypotension__ = a fall of at least 20 mmHg systolic or 10 mmHg diastolic on standing — check in the elderly and in patients on antihypertensives or diuretics.",
    ])
    b.bullets([
        "__Causes of hypertension__ — essential (90-95%), renal disease, endocrine (phaeochromocytoma, Cushing's, Conn's), pregnancy (pre-eclampsia), coarctation, drugs (steroids, oral pills, NSAIDs), obesity, high salt, alcohol, stress.",
        "__Causes of hypotension__ — haemorrhage, shock, dehydration, myocardial infarction, sepsis, anaphylaxis, Addison's disease, over-treatment with antihypertensives, prolonged bed rest, vasovagal attack.",
    ])

    b.section_h("6.7", "The TPR Chart, Intake-Output Chart and Other Records")
    b.bullets([
        "The __TPR chart (vital signs chart)__ is a graphic sheet: __temperature is plotted as a dot joined by a blue/black line, pulse in red, and respiration as a figure or a separate line__; the time scale is usually 4-hourly (6 a.m., 10 a.m., 2 p.m., 6 p.m., 10 p.m., 2 a.m.).",
        "Routine frequency: __twice daily__ for ordinary patients, __4-hourly__ in fever, and __1-4 hourly or continuous__ for critical, post-operative and unconscious patients.",
        "__Never guess or copy previous readings__; report at once a temperature above 39 °C, pulse below 60 or above 120, respiration below 10 or above 30, systolic BP below 90, SpO2 below 90% or any sudden change.",
        "__Intake-output chart__ — intake: oral fluids, IV fluids, blood, tube feeds and medicines given in fluid; output: urine, vomit, aspirate, drainage, liquid stool, and estimated loss in sweat. Totalled every shift and over __24 hours__.",
        "__Normal fluid balance__: intake about __2500 mL/day__ (1500 mL drink + 800 mL food + 250 mL metabolic water); output — urine __1500 mL__, insensible loss through skin and lungs 800-900 mL, faeces 100-200 mL.",
        "__Normal urine output = 1-2 mL/kg/hour in adults (about 30-60 mL/hour; 1500 mL/day)__; __oliguria__ = less than 400 mL/day (or under 0.5 mL/kg/h), __anuria__ = less than 100 mL/day, __polyuria__ = more than 2500-3000 mL/day.",
        "Other records: weight chart (daily in cardiac, renal and oedema patients; a __1 kg gain = about 1 L of retained fluid__), diabetic chart, fluid-balance sheet, pain score chart, Glasgow coma scale chart, neurological observation chart, drug chart.",
    ])

    b.section_h("6.8", "Level of Consciousness — Glasgow Coma Scale")
    b.table(
        ["Response", "Score and criteria"],
        [["__Eye opening (E) — 4__", "4 spontaneous • 3 to speech • 2 to pain • 1 no response"],
         ["__Verbal response (V) — 5__", "5 oriented • 4 confused conversation • 3 inappropriate words • 2 incomprehensible sounds • 1 none"],
         ["__Motor response (M) — 6__", "6 obeys commands • 5 localises pain • 4 withdraws from pain • 3 abnormal flexion (decorticate) • 2 extension (decerebrate) • 1 none"]],
        caption="Table 6.9  Glasgow Coma Scale (GCS)")
    b.box("num", [
        "__Total GCS = 3 (worst) to 15 (fully conscious).__  Mild head injury 13-15 • Moderate 9-12 • __Severe / coma 8 or less__ (a score of 8 or below usually needs intubation).",
        "Also observe __pupils (size, equality, reaction to light)__, limb power, vital signs; __rising BP with a slow pulse and irregular breathing (Cushing's reflex) indicates rising intracranial pressure__.",
    ])

    b.section_h("6.9", "Observation of Urine, Stool, Sputum and Vomit")
    b.table(
        ["Specimen", "Normal", "Abnormal findings and significance"],
        [["__Urine__", "1200-1500 mL/day, pale straw/amber, clear, faint aromatic smell, acidic (pH 4.6-8), specific gravity 1.010-1.025, no protein, sugar, ketone, blood or pus",
          "* Concentrated dark — dehydration, fever\n* __Red/smoky__ — haematuria (stones, tumour, glomerulonephritis); __dark brown/'tea coloured'__ — jaundice/bile, myoglobin\n* __Frothy__ — albuminuria (nephrotic syndrome)\n* Milky/cloudy — pus (UTI), chyluria (filariasis)\n* __Sweet/acetone smell__ — ketosis; fishy/ammoniacal — infection\n* Painful (dysuria), frequency, urgency, retention, incontinence, dribbling, nocturia\n* Red with rifampicin, orange with pyridium, dark with metronidazole (harmless drug colouring)"],
         ["__Stool__", "1-2 formed brown stools/day, characteristic odour",
          "* __Black tarry (melaena)__ — upper GI bleeding (also harmless black with iron, bismuth, charcoal)\n* __Fresh red blood__ — piles, fissure, dysentery, lower GI bleed\n* __Clay/putty coloured with dark urine__ — obstructive jaundice\n* Rice-watery — __cholera__; blood and mucus with tenesmus — __bacillary dysentery/amoebiasis__\n* Bulky, greasy, foul, floating (steatorrhoea) — malabsorption, coeliac disease\n* Green — enteritis in infants; worms, segments of tapeworm visible\n* __Constipation, diarrhoea, incontinence, ribbon-like stool__ (obstruction)"],
         ["__Sputum__", "Nil or a little clear mucoid in the morning",
          "* Thick yellow-green — bacterial infection\n* __Rusty/blood-tinged__ — lobar pneumonia; __copious foul, in layers__ — bronchiectasis/lung abscess\n* __Blood-stained (haemoptysis)__ — tuberculosis, bronchial carcinoma, bronchiectasis\n* __Pink frothy__ — acute pulmonary oedema\n* Currant jelly — Klebsiella; thick tenacious plugs — asthma"],
         ["__Vomit__", "Nil",
          "* __Coffee-ground / red__ — haematemesis (peptic ulcer, varices)\n* __Bile stained green-yellow__ — persistent vomiting, intestinal obstruction\n* __Faecal smelling__ — low intestinal obstruction, peritonitis\n* __Projectile__ (forceful, without nausea) — raised intracranial pressure; in infants — congenital pyloric stenosis\n* Undigested food hours after a meal — gastric outlet obstruction"]],
        caption="Table 6.10  Observation of excreta and secretions")

    b.section_h("6.10", "Signs of Improvement, Deterioration and of Approaching Death")
    b.table(
        ["Improvement", "Deterioration (report at once!)"],
        [["Temperature, pulse, respiration and BP returning to normal; skin warm and dry",
          "Rising or falling temperature, weak thready rapid pulse, fall in BP, rapid shallow or irregular breathing"],
         ["Alert, oriented, interested in surroundings, sleeps well",
          "__Restlessness, confusion, drowsiness, convulsion, unconsciousness__"],
         ["Appetite returning, tongue clean and moist, bowels regular",
          "Persistent vomiting, abdominal distension, no urine (under 30 mL/h), bleeding from any site"],
         ["Good urine output, clear urine, less oedema",
          "Increasing pain, cold clammy skin, cyanosis, pallor, sweating, gasping (~air hunger~)"],
         ["Wound clean, dry and healing; pain decreasing",
          "Foul, discharging wound; spreading redness; sudden severe chest pain or breathlessness"]],
        caption="Table 6.11  Judging the course of illness")
    b.sub("Signs of approaching death and last offices")
    b.bullets([
        "__Signs__ — sunken eyes with a fixed stare and loss of the corneal reflex, dilated non-reacting pupils, pinched cold clammy skin with 'hippocratic facies', mottled and cold extremities, incontinence, weak irregular imperceptible pulse, falling BP, __Cheyne-Stokes__ then gasping respiration with noisy secretions ('death rattle'), restlessness followed by coma, loss of sphincter control; __hearing is usually the last sense to go__.",
        "__Signs of death__ — no pulse, heart sounds or respiration for a stated period, no response to any stimulus, pupils fixed and dilated, loss of all reflexes, falling body temperature (~algor mortis~), post-mortem lividity (~livor mortis~), stiffening (~rigor mortis~ begins in 2-4 hours, complete in 12 hours, passes off in 24-48 hours). __Death must be certified by a doctor.__",
        "__Last offices (care of the body)__ — record the time of death; give privacy and inform relatives kindly; wear gloves; straighten the body in the supine position with one pillow, close the eyes and mouth, remove tubes, catheters and jewellery (make an inventory before witnesses), clean the body and dress the wounds, pad the orifices, tie the limbs and jaw with a bandage, label the body (two identification tags), wrap it in a sheet as per the family's religious custom, hand over valuables against signature, complete the death record and inform the mortuary; disinfect the bed and unit (terminal disinfection). Handle the body of an infectious case as per the biosafety protocol.",
    ])

    b.box("recap", [
        "* Normal adult vital signs: T 37 °C (98.6 °F), P 60-100, R 12-20, BP under 120/80, SpO2 95-100%.",
        "* Rectal temperature 0.5 °C above oral, axillary 0.5 °C below; hyperpyrexia above 41 °C, hypothermia below 35 °C; °F = (°C × 9/5) + 32.",
        "* Fever raises the pulse about 10 beats per °F; count the pulse for 1 full minute, never with the thumb; apex beat at the 5th left intercostal space.",
        "* Fever types: continuous, remittent, intermittent (quotidian/tertian/quartan), relapsing, inverse (TB); crisis = sudden fall, lysis = gradual.",
        "* Cheyne-Stokes = heart failure/brain damage; Kussmaul = diabetic ketoacidosis; stridor = upper airway obstruction.",
        "* Urine output 1-2 mL/kg/h (30-60 mL/h); oliguria under 400 mL/day, anuria under 100 mL/day.",
        "* GCS 3-15 (E4 V5 M6); 8 or less = coma; Cushing's reflex (rising BP + slow pulse) = raised ICP.",
        "* Black tarry stool = upper GI bleed; clay stool + dark urine = obstructive jaundice; pink frothy sputum = pulmonary oedema; rusty sputum = lobar pneumonia.",
    ])



def chapter_7(b):
    b.chapter(7, "Infection",
              "Terminology, chain of infection, transmission, sterilisation and disinfection, isolation, universal precautions and waste management")

    b.section_h("7.1", "Basic Terminology")
    b.table(
        ["Term", "Definition"],
        [["__Infection__", "Entry, multiplication and establishment of a pathogenic organism in the tissues of a host, with a harmful (pathological) response"],
         ["__Contamination__", "Presence of organisms on an inanimate article, body surface or in food/water — no invasion of tissue"],
         ["__Colonisation__", "Organisms present and multiplying on a body surface without causing disease or immune response"],
         ["__Infestation__", "Lodgement and development of an ~animal parasite~ on or in the body (lice, scabies, worms)"],
         ["__Pathogen / Virulence__", "Organism capable of causing disease / the degree of its disease-producing power"],
         ["__Sepsis / Asepsis / Antisepsis__", "Presence of pus-forming organisms in blood or tissue / absence of disease-producing organisms / destruction of organisms on living tissue"],
         ["__Incubation period__", "Interval between the entry of the organism and the appearance of the first sign or symptom"],
         ["__Prodromal period__", "Interval between the earliest vague symptoms and the specific (characteristic) signs, e.g. the rash"],
         ["__Period of communicability (infectivity)__", "The time during which the patient can transmit the infection to others"],
         ["__Carrier__", "An apparently healthy person who harbours and excretes the organism. Types: __healthy, incubatory, convalescent, chronic (e.g. 'Typhoid Mary'), temporary, paradoxical, contact__"],
         ["__Reservoir / Source__", "Natural habitat where the organism lives and multiplies (man, animal, soil) / the place from which it immediately passes to the host"],
         ["__Zoonosis__", "Disease transmissible from animal to man — rabies, plague, brucellosis, anthrax, leptospirosis, bird flu, Nipah, COVID-19"],
         ["__Fomites__", "Inanimate contaminated objects — bed linen, towels, toys, utensils, door handles, stethoscope, thermometer, mobile phone"],
         ["__Vector__", "A living carrier (insect or animal) — mosquito, housefly, louse, flea, tick, sandfly; ~mechanical~ (housefly) or ~biological~ (mosquito)"],
         ["__Nosocomial / Health-care-associated infection (HAI)__", "Infection acquired __in hospital__ (appearing 48 hours or more after admission) that was not present or incubating at admission"],
         ["__Opportunistic infection__", "Infection by a normally harmless organism in an immunocompromised host (candidiasis, ~Pneumocystis~ pneumonia in AIDS)"],
         ["__Endogenous / Exogenous__", "Infection from the patient's own flora / from outside the body"],
         ["__Local / Systemic infection__", "Confined to one part (abscess) / spread through the blood stream (septicaemia)"],
         ["__Bacteraemia / Septicaemia / Toxaemia / Pyaemia__", "Bacteria in the blood without multiplying / bacteria multiplying in the blood with illness / toxins in the blood / pus-forming organisms with multiple abscesses"],
         ["__Immunity / Susceptible host__", "Power of the body to resist infection / a person lacking resistance"],
         ["__Quarantine / Isolation__", "Restriction of the movement of an ~apparently healthy contact~ for the longest incubation period / separation of an ~infected person~ for the period of communicability"],
         ["__Surveillance / Notifiable disease__", "Continuous watch over disease occurrence / a disease that must be reported to the health authority by law"],
         ["__Disinfection / Sterilisation__", "Destruction of pathogenic organisms (~not spores~) on inanimate objects / destruction of __all__ forms of microbial life __including spores__"],
         ["__Sanitisation / Decontamination__", "Reduction of microbial numbers to a safe level / removal of contamination so an article is safe to handle"]],
        caption="Table 7.1  Terminology of infection")

    b.section_h("7.2", "The Chain of Infection")
    b.table(
        ["Link", "Explanation", "How the nurse breaks it"],
        [["1. __Infectious agent__", "Bacteria, virus, fungus, protozoa, helminth, prion", "Correct diagnosis and treatment; antibiotics; disinfection and sterilisation"],
         ["2. __Reservoir__", "Man (patient, carrier), animals, soil, water, food, equipment", "Treat cases and carriers, chlorinate water, control animals, clean equipment"],
         ["3. __Portal of exit__", "Respiratory secretions, faeces, urine, blood, wound discharge, genital secretions, breast milk, placenta",
          "Cover cough, safe disposal of excreta and dressings, cover wounds"],
         ["4. __Mode of transmission__", "Contact, droplet, airborne, vehicle, vector", "__Hand hygiene__, gloves, mask, isolation, vector control, food and water hygiene"],
         ["5. __Portal of entry__", "Mouth, nose, respiratory tract, broken skin, mucous membrane, urethra, placenta, injection site, surgical wound",
          "Aseptic technique, wound care, catheter and IV care, safe injections"],
         ["6. __Susceptible host__", "Very young, aged, malnourished, immunosuppressed, diabetic, post-operative, on steroids/chemotherapy",
          "__Immunisation__, nutrition, control of diabetes, early ambulation, shortening hospital stay"]],
        caption="Table 7.2  The six links in the chain of infection")
    b.box("hy", ["__Hand hygiene is the single most effective measure to prevent the spread of infection__ — it breaks the chain at the 'mode of transmission' link. The transmission link is the easiest one to break."])

    b.section_h("7.3", "Modes of Transmission")
    b.table(
        ["Mode", "Sub-type / mechanism", "Examples"],
        [["__Contact — direct__", "Skin-to-skin, touching, kissing, sexual contact, droplet spread within 1 metre, transplacental (vertical)",
          "Scabies, impetigo, syphilis, gonorrhoea, HIV, hepatitis B, infectious mononucleosis, congenital rubella"],
         ["__Contact — indirect__", "Through fomites, contaminated hands, instruments, endoscopes, linen",
          "Staphylococcal infection, MRSA, ~Clostridioides difficile~, conjunctivitis"],
         ["__Droplet__ (large, over 5 micron, travel under 1-2 m)", "Coughing, sneezing, talking, suctioning",
          "Influenza, COVID-19, pertussis, diphtheria, mumps, rubella, meningococcus, common cold"],
         ["__Airborne__ (droplet nuclei under 5 micron, remain suspended; also dust)", "Inhalation over a long distance; needs a negative-pressure room and an N95 mask",
          "__Tuberculosis, measles, chickenpox (varicella)__, aspergillus, smallpox"],
         ["__Vehicle-borne__", "Water, food, milk, blood and blood products, IV fluids, drugs",
          "Cholera, typhoid, hepatitis A and E, polio, food poisoning, amoebiasis, brucellosis (milk), hepatitis B/C and HIV (blood)"],
         ["__Vector-borne__ — mechanical", "Organism carried on the vector's body", "Housefly: typhoid, diarrhoea, dysentery, trachoma, polio"],
         ["__Vector-borne__ — biological", "Organism multiplies/develops inside the vector",
          "__Anopheles__ mosquito: malaria • __Aedes aegypti__: dengue, chikungunya, yellow fever, Zika • __Culex__: filariasis, Japanese encephalitis • __Sandfly__: kala-azar • __Tsetse fly__: sleeping sickness • __Rat flea (Xenopsylla)__: plague • __Louse__: epidemic typhus, relapsing fever • __Tick__: KFD, Lyme disease • __Mite__: scrub typhus • __Blackfly__: onchocerciasis"],
         ["__Soil-borne__", "Spores and larvae in soil", "Tetanus, gas gangrene, anthrax, mycetoma, hookworm, ascariasis"],
         ["__Inoculation / parenteral__", "Needle-stick, sharps, transfusion, tattoo, unsafe injection, animal bite", "Hepatitis B and C, HIV, rabies, tetanus"]],
        caption="Table 7.3  Modes of transmission with classic examples")

    b.section_h("7.4", "Hospital-Acquired (Nosocomial) Infection")
    b.bullets([
        "__Commonest sites (in order)__ — __urinary tract infection (about 40%, mostly catheter-associated)__, surgical site infection, respiratory tract/ventilator-associated pneumonia, and blood stream (IV cannula) infection.",
        "__Commonest organisms__ — ~Escherichia coli~, ~Staphylococcus aureus~ (including __MRSA__), ~Pseudomonas aeruginosa~, ~Klebsiella~, ~Enterococcus~, ~Candida~, ~Clostridioides difficile~ (after antibiotics), ~Acinetobacter~.",
        "__Risk factors__ — indwelling catheter and cannula, ventilator, surgery, prolonged stay, broad-spectrum antibiotics, steroids, extremes of age, diabetes, malnutrition, overcrowding, poor hand hygiene.",
        "__Prevention__ — hand hygiene, aseptic technique, minimum use and early removal of catheters and cannulae, closed drainage systems, sterile dressings, isolation of infected patients, antibiotic stewardship (rational use), surveillance by the __hospital infection control committee__, staff training and immunisation, environmental cleaning, and safe waste disposal.",
    ])

    b.section_h("7.5", "Hand Hygiene")
    b.bullets([
        "__WHO 'My 5 Moments for Hand Hygiene'__ — (1) before touching a patient, (2) before a clean/aseptic procedure, (3) after body-fluid exposure risk, (4) after touching a patient, (5) after touching patient surroundings.",
        "__Types__ — ~social/routine hand wash~ with soap and water for __20-40 seconds__ (~40-60 s including wetting and drying~); ~hygienic hand rub~ with __alcohol-based hand rub (60-80% alcohol) for 20-30 seconds__; ~surgical scrub~ with an antiseptic (chlorhexidine 4%, povidone-iodine) for __2-5 minutes__ including the forearms up to the elbow, with a sterile brush for the nails.",
        "__WHO 6/7 steps__ — palm to palm; right palm over left dorsum and vice versa; palm to palm with fingers interlaced; backs of fingers to opposing palms; rotational rubbing of each thumb; finger tips/nails in the opposite palm; (then the wrists).",
        "__Soap and water is essential (alcohol rub is NOT enough)__ when the hands are visibly soiled, after using the toilet, and after caring for a patient with __~C. difficile~ diarrhoea or norovirus__ (spores are not killed by alcohol).",
        "Keep the nails short, remove rings and watch, dry the hands with a clean/disposable towel, and use elbow or foot-operated taps.",
    ])

    b.section_h("7.6", "Sterilisation")
    b.table(
        ["Method", "Details, temperature and time", "Used for"],
        [["__Red heat__", "Heating to red hot in a flame", "Inoculation loops, wires, needle points, forceps tips"],
         ["__Flaming__", "Passing through a flame", "Scalpels, mouth of test tubes, slides"],
         ["__Incineration (burning)__", "Complete burning to ash", "Soiled dressings, cotton, pathological waste, animal carcasses, plastic disposables"],
         ["__Hot air oven__ (dry heat)", "__160 °C for 2 hours__ (or 170 °C for 1 h) — holding time",
          "Glassware (syringes, petri dishes, test tubes), metal instruments, powders, oils, greases, sharp instruments (does not blunt them)"],
         ["__Boiling__ (disinfection, not true sterilisation)", "__100 °C for 20-30 minutes__ (add 2% sodium carbonate to raise the boiling point and prevent rusting); ~does not kill spores or hepatitis virus reliably~",
          "Home use — metal instruments, syringes, rubber goods, feeding bottles"],
         ["__Autoclave (moist heat under pressure) — the most reliable, commonest hospital method__",
          "__121 °C at 15 lb/sq inch (1.05 kg/cm2) for 15-20 minutes__, or 134 °C at 30 lb for 3-5 minutes (flash); prions need 134 °C for 18 min",
          "Surgical instruments, dressings, linen, gloves, syringes, culture media, rubber tubing; __NOT__ for oils, powders, sharp cutting edges (blunts them) or heat-labile plastics"],
         ["__Pasteurisation__", "Holder method 63 °C for 30 min; __flash (HTST) 72 °C for 15-20 seconds__; ultra-high temperature 125-150 °C for 1-4 s; then rapid cooling",
          "Milk — kills ~M. tuberculosis, Brucella, Salmonella, Coxiella~ (the test of adequacy is the ~phosphatase test~)"],
         ["__Tyndallisation (intermittent)__", "100 °C for 20 min on 3 successive days", "Media with sugar, gelatin, egg"],
         ["__Inspissation__", "80-85 °C for 30 min on 3 days", "Loeffler's serum, Lowenstein-Jensen medium"],
         ["__Filtration__", "Membrane filter (0.22 micron), candle, asbestos, sintered glass, HEPA filters for air",
          "Serum, vaccines, antibiotic solutions, IV fluids, air in theatres and laminar flow"],
         ["__Radiation — ionising (gamma, cobalt-60)__", "'Cold sterilisation', industrial", "Disposable syringes, needles, gloves, catheters, sutures, plastic ware"],
         ["__Radiation — non-ionising (UV, 254 nm)__", "Poor penetration; surface and air only",
          "Operation theatre, laboratory hoods, water treatment (does not penetrate glass or dust)"],
         ["__Gas — ethylene oxide (ETO)__", "Needs humidity and long aeration; toxic, inflammable and carcinogenic",
          "Heat-sensitive items: plastics, endoscopes, heart-lung machine, ventilator tubing, sutures, pacemakers"],
         ["__Gas — formaldehyde, hydrogen peroxide plasma, peracetic acid__", "Low-temperature methods", "Endoscopes, delicate instruments, room fumigation"],
         ["__Chemical (cold) sterilisation__", "__Glutaraldehyde 2% (Cidex)__ — 20 min for disinfection, 6-10 h for sterilisation; ortho-phthalaldehyde",
          "Endoscopes, cystoscopes, plastic and rubber goods, anaesthetic tubes"]],
        caption="Table 7.4  Methods of sterilisation (a favourite examination table)")
    b.box("num", [
        "__Autoclave = 121 °C, 15 lb/sq in, 15-20 minutes__ (moist heat, most efficient).  __Hot air oven = 160 °C for 2 hours__ (dry heat).",
        "Sterilisation controls: ~physical~ (thermocouple, gauge), ~chemical~ (Browne's tube, autoclave tape, Bowie-Dick test), ~biological~ — __~Geobacillus stearothermophilus~ for the autoclave__ and __~Bacillus atrophaeus~ (subtilis) for the hot air oven and ETO__.",
        "Order of resistance (most resistant first): __prions > bacterial spores > mycobacteria > non-lipid viruses > fungi > vegetative bacteria > lipid viruses__.",
    ])

    b.section_h("7.7", "Disinfectants and Antiseptics")
    b.table(
        ["Agent", "Strength used", "Uses and remarks"],
        [["__Alcohol__ — ethyl 70%, isopropyl 60-70%", "60-80%", "Skin before injection, thermometers, hand rub; ~not sporicidal~; needs 30 s contact; inflammable"],
         ["__Povidone-iodine (Betadine)__", "5-10% solution, 7.5% scrub", "Skin preparation before surgery, wounds, gargle; stains; avoid in newborns and iodine allergy"],
         ["__Chlorhexidine gluconate__", "0.5% in alcohol, 2-4% scrub, 0.2% mouth wash", "Surgical scrub, skin preparation (best for central lines), oral care; ~keep out of the eyes and ears~"],
         ["__Sodium hypochlorite (bleach)__", "__0.5-1%__ for surfaces and blood spills; 0.05% for clean surfaces", "Floors, spills, linen, excreta, dialysis; corrodes metal; inactivated by organic matter; ~never mix with acid or ammonia (toxic gas)~"],
         ["__Bleaching powder__", "__33% available chlorine__; 5% solution", "Excreta, latrines, wells (1 ppm residual chlorine in drinking water), drains"],
         ["__Phenol (carbolic acid) / cresol / Lysol__", "Phenol 1-2%, Lysol 2-5%", "Floors, drains, excreta; irritant, absorbed through the skin, avoid in nurseries"],
         ["__Hydrogen peroxide__", "3% (6% for disinfection)", "Wound cleaning (effervescence lifts debris), mouth wash diluted; unstable in light"],
         ["__Potassium permanganate (KMnO4)__", "1:5000 to 1:10 000", "Sitz bath, wet dressings, gargle, fungal infections of the foot, well disinfection"],
         ["__Formaldehyde / formalin__", "10% solution, 40% formalin", "Fumigation, preservation of specimens; irritant, carcinogenic"],
         ["__Glutaraldehyde 2%__", "20 min-10 h", "Endoscopes, plastic and rubber; irritant to eyes and skin"],
         ["__Quaternary ammonium compounds (cetrimide, benzalkonium)__", "0.1-1%", "Cleaning skin, floors; ~inactivated by soap~, poor against Pseudomonas and spores"],
         ["__Ethylene oxide gas__", "-", "Heat-sensitive articles (see Table 7.4)"],
         ["__Silver sulphadiazine / mupirocin__", "1% cream / 2% ointment", "Burns / staphylococcal skin infection"],
         ["__Boric acid, gentian violet, soap and water__", "-", "Eye wash (2%), oral thrush, plain mechanical cleaning"]],
        caption="Table 7.5  Common disinfectants and antiseptics")
    b.box("def", [
        "__Spaulding classification of instruments__ — ~Critical~ items enter sterile tissue or the blood stream (surgical instruments, implants, needles) and need __sterilisation__; ~Semi-critical~ items touch mucous membranes (endoscopes, laryngoscope blades, thermometers) and need __high-level disinfection__; ~Non-critical~ items touch intact skin only (BP cuff, stethoscope, bedpan) and need __low-level disinfection/cleaning__.",
    ])

    b.section_h("7.8", "Standard (Universal) Precautions and Barrier Nursing")
    b.bullets([
        "__Standard precautions__ apply to __every patient, at all times, irrespective of diagnosis__, treating all blood, body fluids, secretions, excretions (except sweat), non-intact skin and mucous membranes as potentially infectious.",
        "Components: __hand hygiene; personal protective equipment (PPE); safe injection practice; safe handling and disposal of sharps; respiratory hygiene and cough etiquette; cleaning of equipment and environment; safe handling of linen; and waste management__.",
        "__Never recap a used needle__ (if unavoidable use the one-handed scoop technique); never bend, break or hand-pass a needle; drop it directly into a __puncture-proof container__ that is sealed at three-quarters full.",
        "__Transmission-based precautions__ are added to standard precautions: ~Contact~ (gown and gloves, single room, dedicated equipment — MRSA, C. difficile, scabies); ~Droplet~ (surgical mask within 1 m, patient wears a mask when moved — influenza, pertussis, mumps, meningococcus); ~Airborne~ (__N95 respirator, negative-pressure single room with 6-12 air changes, door closed__ — tuberculosis, measles, chickenpox).",
    ])
    b.sub("Personal protective equipment — order of use")
    b.table(
        ["Step", "Donning (putting on)", "Doffing (removing)"],
        [["1", "Hand hygiene", "__Gloves__ (most contaminated — remove first)"],
         ["2", "__Gown/apron__", "Goggles/face shield"],
         ["3", "__Mask / N95 respirator__ (fit check)", "__Gown__"],
         ["4", "Goggles or face shield", "__Mask/respirator__ (by the strings, from behind)"],
         ["5", "__Gloves__ (last)", "Hand hygiene (and again after leaving the room)"]],
        caption="Table 7.6  Sequence of donning and removing PPE", align_center_cols=(0,))
    b.sub("Barrier nursing and isolation")
    b.bullets([
        "__Barrier nursing__ — nursing an infectious patient in a separate room or cubicle with a 'barrier' of gowns, masks, gloves and separate equipment, so that infection does not pass out to others.",
        "__Reverse (protective) barrier nursing__ — protecting a __highly susceptible patient__ (neutropenic, on chemotherapy, transplant recipient, extensive burns, severe combined immunodeficiency, preterm baby) from organisms brought in by staff and visitors: laminar-flow positive-pressure room, sterile linen, cooked food, no flowers or fresh fruit, no visitor with any infection.",
        "__Requirements of an isolation unit__ — single room (preferably with an ante-room and attached toilet), door kept closed with a notice, separate gowns/masks/gloves outside the door, separate linen, crockery, thermometer, BP cuff and bedpan, a bowl of disinfectant, a covered bucket for soiled linen, a hand-washing basin and a chart kept outside the room.",
        "__Concurrent disinfection__ throughout the illness and __terminal disinfection__ after discharge (see Chapter 3).",
        "Psychological care of the isolated patient is important — he feels lonely, rejected and anxious; explain the reason, visit frequently, provide a phone/TV/books, and allow limited screened visitors.",
    ])

    b.section_h("7.9", "Bio-Medical Waste Management (BMW Rules, 2016 — India)")
    b.table(
        ["Colour of bag/container", "Category of waste", "Examples", "Treatment and disposal"],
        [["__Yellow__", "Human and animal anatomical waste, soiled waste, expired/discarded medicines, chemical waste, microbiology and laboratory waste, blood bags, __used linen soiled with blood/body fluid__",
          "Placenta, body parts, dressings, cotton, plaster casts, expired drugs, blood bags, laboratory cultures",
          "__Incineration__ / plasma pyrolysis / deep burial (only in rural areas); chemical disinfection for laboratory waste"],
         ["__Red__", "Contaminated recyclable plastic waste", "Syringes without needles, IV sets and tubing, catheters, urine bags, gloves, vacutainers",
          "__Autoclave/microwave/hydroclave, then shred__ and send for recycling to a registered recycler"],
         ["__White (translucent, puncture-proof)__", "__Sharps__", "Needles, needles with fixed syringes, scalpels, blades, broken glass ampoules",
          "Autoclave or dry-heat sterilise, then shred/encapsulate/concrete pit; final disposal to a metal foundry"],
         ["__Blue (cardboard box with blue marking)__", "Glassware and metallic implants", "Broken/discarded glass bottles and vials, medicine vials, ampoules, metallic body implants",
          "__Disinfection (1% hypochlorite) or autoclaving__, then recycling"],
         ["__Black__ (~general, not bio-medical~)", "General non-infectious municipal waste", "Paper, packaging, kitchen and office waste, flowers",
          "Ordinary municipal solid waste disposal"],
         ["__Cytotoxic waste__", "Cytotoxic drugs and their containers, contaminated items", "Anticancer drug vials, syringes",
          "__Yellow bag with 'cytotoxic' label__ — incineration at 1200 °C or encapsulation; ~never landfill~"]],
        caption="Table 7.7  Bio-medical waste colour coding (very frequently asked)")
    b.box("num", [
        "* Bags must not be filled beyond __three-quarters__, must be labelled with the biohazard/cytotoxic symbol, and must be stored for __not more than 48 hours__ before treatment.",
        "* Liquid infectious waste is disinfected with __1-2% sodium hypochlorite__ before discharge into the drain.",
        "* Needles are destroyed at the point of generation with a __needle destroyer/hub cutter__.",
        "* Every health-care facility must keep records for __5 years__, report annually to the State Pollution Control Board by __30 June__, and immunise all staff against __hepatitis B and tetanus__.",
        "* Deep burial pit: __at least 2 metres deep__, away from habitation and water sources — permitted only for towns with under 5 lakh population.",
    ])

    b.section_h("7.10", "Injection Safety and Post-Exposure Prophylaxis")
    b.bullets([
        "__One needle, one syringe, one patient, one time__ — never re-use a syringe, needle or lancet, and never re-enter a single-dose vial.",
        "Reconstitute with a new needle and syringe; clean the vial top with alcohol and let it dry; avoid touching the needle or the plunger shaft.",
        "__After exposure__ (needle stick, splash to mucosa or broken skin): do not squeeze or suck the wound; __wash with soap and running water__ (mucosa and eyes with plenty of water/saline); do not use bleach or spirit on the wound; report immediately and record; test the source and the exposed person.",
        "__HIV PEP__ — start as soon as possible, ideally __within 2 hours (not later than 72 hours)__, continue __28 days__ (usually tenofovir + lamivudine + dolutegravir); test at 6 weeks, 3 and 6 months.",
        "__Hepatitis B__ — if unvaccinated, give __hepatitis B immunoglobulin (HBIG) plus the vaccine within 24 hours__ (preferably) and complete the schedule; __hepatitis C__ — no prophylaxis available, only follow-up testing.",
        "Approximate risk per percutaneous exposure: __hepatitis B 6-30%, hepatitis C 1.8%, HIV 0.3%__ (mucous membrane splash 0.09%).",
    ])

    b.box("recap", [
        "* Disinfection kills pathogens (not spores); sterilisation kills everything including spores.",
        "* Chain of infection: agent → reservoir → exit → transmission → entry → susceptible host; hand hygiene is the best single break.",
        "* Airborne (needs N95 + negative pressure): TB, measles, chickenpox. Droplet (surgical mask): influenza, pertussis, mumps, COVID.",
        "* Autoclave 121 °C/15 lb/15-20 min; hot air oven 160 °C/2 h; boiling 20-30 min; ETO for heat-sensitive items; glutaraldehyde 2% for endoscopes.",
        "* Biological indicators: G. stearothermophilus (autoclave), B. atrophaeus (hot air oven/ETO).",
        "* Commonest nosocomial infection = catheter-associated urinary tract infection.",
        "* BMW 2016: Yellow = anatomical/soiled/expired drugs (incinerate); Red = recyclable plastics (autoclave + shred); White = sharps; Blue = glass and metal implants; Black = general.",
        "* PPE: gloves last on, gloves first off. Never recap a needle.",
        "* PEP for HIV within 2 h (max 72 h) for 28 days; HBIG + vaccine within 24 h for hepatitis B.",
    ])



def chapter_8(b):
    b.chapter(8, "Surgical Techniques",
              "Asepsis, sterile technique, wounds and healing, dressings, sutures, drains and minor surgical procedures")

    b.section_h("8.1", "Medical Asepsis and Surgical Asepsis")
    b.table(
        ["Point", "__Medical asepsis (clean technique)__", "__Surgical asepsis (sterile technique)__"],
        [["Aim", "Reduce the number and spread of organisms", "__Complete absence__ of all organisms including spores"],
         ["Used in", "Routine ward work — bed making, bathing, giving oral drugs, handling bedpans", "Operation theatre, dressings, catheterisation, injections, IV cannulation, lumbar puncture, labour room"],
         ["Practices", "Hand washing, gloves, clean linen, disinfection, isolation", "Sterile gloves, sterile gown and drapes, sterile field, sterilised instruments, mask and cap"],
         ["Rule", "'Clean' and 'dirty' areas are kept separate", "Once contaminated, the article is __no longer sterile__ and must be discarded"]],
        caption="Table 8.1  Medical vs surgical asepsis")
    b.sub("Principles of the sterile field (learn these rules)")
    b.numbered([
        "A sterile object touched by an unsterile object becomes __unsterile__; when in doubt, consider it unsterile.",
        "Only sterile articles may be placed in a sterile field; the __outer 2.5 cm (1 inch) margin__ of a sterile drape is considered unsterile.",
        "A sterile field must be kept __in view__ and __above waist level__; anything below the waist or out of sight is unsterile.",
        "__Never reach across a sterile field__, never turn your back on it, and never talk, cough or sneeze over it.",
        "__Moisture carries organisms__ — a wet sterile field (strike-through) is contaminated.",
        "Air currents carry organisms — do not fan, shake linen or allow fans over the field; keep doors closed and traffic minimal.",
        "Sterile persons keep their hands __in front, between the shoulders and the waist__, and pass each other back-to-back; the gown is considered sterile only in front from the chest to the waist, and the sleeves to 5 cm above the elbow.",
        "Pour lotions without touching the container to the bowl; hold the bottle lip away from the sterile field and discard the first few drops.",
        "Check the __sterility indicator, packing integrity and expiry date__ before opening; open the first flap away from you and the last towards you.",
        "Use a __sterile transfer forceps (cheatle forceps)__ kept in a disinfectant, with the tips down; never touch the sterile item with the hands."
    ])

    b.section_h("8.2", "Surgical Hand Scrub, Gowning and Gloving")
    b.bullets([
        "__Surgical scrub__ — remove all jewellery and nail polish; wet the hands and forearms; apply an antiseptic (__chlorhexidine 4% or povidone-iodine 7.5%__); scrub with a sterile brush and follow the anatomical time or count method for __3-5 minutes__ (first scrub of the day 5 min, subsequent 3 min), cleaning the nails, all four surfaces of each finger, the palm, the back and the forearm __up to 5 cm above the elbow__; keep the __hands above the elbows__ at all times so that water runs from the clean hands towards the elbows; rinse from the finger tips downwards; dry with a sterile towel from the fingers to the elbow, using a different side for each arm.",
        "Alcohol-based surgical hand rub (with persistent activity) is an accepted alternative and is less damaging to the skin.",
        "__Closed gloving__ — the hands stay inside the gown sleeves until the gloves are drawn over the cuffs (preferred in the theatre). __Open gloving__ — the folded cuff is handled by the inside surface only (used in the ward for dressings and catheterisation).",
        "Gowning: hold the gown at the neck, let it unfold away from the body without touching anything, slip the arms in, and let the circulating nurse tie it from behind.",
        "__If a glove is punctured or touched by anything unsterile, change it at once__ — with a fresh scrub if necessary.",
    ])

    b.section_h("8.3", "Wounds — Types, Healing and Complications")
    b.table(
        ["Classification", "Types"],
        [["By skin break", "__Closed__ (contusion/bruise, haematoma) and __open__ (skin broken)"],
         ["By nature of injury", "__Incised__ (clean cut by a sharp blade — bleeds freely, heals best); __Lacerated__ (torn, ragged edges); __Abrasion__ (graze of superficial layers); __Puncture/stab__ (small entry, deep track, high infection risk — tetanus); __Penetrating and perforating__ (enters / passes through); __Contused__ (blunt, bruised); __Gunshot__; __Crush__; __Avulsion/degloving__; __Bite__ (highly infected — rabies risk)"],
         ["By degree of contamination", "__Clean__ (elective, no inflammation, no entry into the respiratory, GI or genito-urinary tract — infection rate 1-2%); __Clean-contaminated__ (controlled entry into those tracts); __Contaminated__ (fresh traumatic wound, spillage); __Dirty/infected__ (old traumatic wound, pus, perforated viscus)"],
         ["By depth", "Superficial, partial-thickness, full-thickness, deep (involving muscle, tendon, bone)"]],
        caption="Table 8.2  Classification of wounds")
    b.sub("Phases of wound healing")
    b.table(
        ["Phase", "Time", "Events"],
        [["__1. Haemostasis__", "Immediate (minutes)", "Vasoconstriction, platelet plug and clot formation"],
         ["__2. Inflammatory (lag/exudative) phase__", "Day 0-4 (up to 5)", "Vasodilatation, neutrophils and macrophages clean the wound; redness, heat, swelling, pain and loss of function"],
         ["__3. Proliferative (fibroblastic/granulation) phase__", "Day 3-21", "Fibroblasts lay collagen, new capillaries form (angiogenesis), granulation tissue and epithelialisation; wound contraction"],
         ["__4. Maturation (remodelling) phase__", "Day 21 to 1-2 years", "Collagen re-organised, scar becomes pale and strong — reaching only about __70-80% of the original strength__"]],
        caption="Table 8.3  Phases of wound healing")
    b.kv_bullets([
        ("Healing by first intention (primary union)", "clean, sutured wound with apposed edges — minimal granulation, fine scar, fastest."),
        ("Healing by second intention", "wide, infected or gaping wound left open — heals by granulation, contraction and epithelialisation, leaving a broad ugly scar."),
        ("Healing by third intention (delayed primary closure)", "wound left open for a few days until clean, then sutured."),
    ])
    b.sub("Factors influencing wound healing")
    b.table(
        ["Favourable", "Unfavourable (delay healing)"],
        [["Young age, good blood supply, adequate oxygen",
          "Old age, ischaemia (peripheral vascular disease), anaemia, hypoxia, smoking"],
         ["Good nutrition — __protein, vitamin C, vitamin A, zinc, iron__",
          "Malnutrition, protein and vitamin C deficiency (defective collagen), obesity"],
         ["Clean, moist wound; approximated edges; immobilisation and rest",
          "__Infection (the commonest cause of delay)__, foreign body, dead tissue/slough, haematoma, repeated trauma, movement"],
         ["Control of diabetes; absence of systemic disease",
          "__Diabetes mellitus__, uraemia, jaundice, malignancy, immunosuppression, radiotherapy"],
         ["No interfering drugs", "__Corticosteroids__, cytotoxic drugs, NSAIDs, anticoagulants"]],
        caption="Table 8.4  Factors affecting wound healing")
    b.sub("Complications of wounds")
    b.bullets([
        "__Haemorrhage__ — primary (at the time of injury), __reactionary__ (within 24 h, as BP rises or a ligature slips), __secondary__ (after __7-14 days__, due to infection eroding a vessel).",
        "__Infection__ — appears 3-7 days after surgery with pain, redness, swelling, heat, purulent discharge and fever; commonest organism ~Staphylococcus aureus~.",
        "__Wound dehiscence__ (bursting open of the layers, typically on the __5th-10th post-operative day__, often heralded by a serosanguineous 'pink' discharge) and __evisceration__ (protrusion of viscera — a surgical emergency: place the patient supine with knees flexed, cover the bowel with a __sterile saline-soaked dressing__, do not push it back, nil by mouth, inform the surgeon at once).",
        "__Sinus, fistula, keloid and hypertrophic scar, contracture, incisional hernia, adhesions, gangrene, tetanus, gas gangrene__.",
        "__Chronic wounds/ulcers__ — pressure sore, venous ulcer, diabetic foot ulcer, arterial ulcer.",
    ])

    b.section_h("8.4", "Dressing a Wound")
    b.sub("Purposes of a dressing")
    b.bullets([
        "To protect the wound from injury and contamination; to absorb discharge; to apply medication; to give support and immobilisation; to arrest bleeding by pressure; to keep the wound __moist and at body temperature__ (which speeds healing) and to hide disfigurement.",
    ])
    b.sub("Articles on the dressing trolley")
    b.table(
        ["Top (sterile) shelf", "Bottom (unsterile) shelf"],
        [["Sterile dressing pack — 2 pairs of artery/dissecting forceps, sponge-holding forceps, scissors, kidney tray, gallipots, cotton balls, gauze pieces, pads, drape/towel, sterile gloves, probe, sinus forceps",
          "Mackintosh and towel, bandages and adhesive plaster, scissors, bowl of antiseptic lotion (normal saline, povidone-iodine, hydrogen peroxide), prescribed ointment, paper bag/kidney tray for soiled dressings, hand sanitiser, gloves, spirit swabs, specimen container for culture, extra bandages and a waste bag, sharps container"]],
        caption="Table 8.5  Dressing trolley")
    b.sub("Procedure of a simple aseptic dressing")
    b.numbered([
        "Verify the order, explain to the patient, give an analgesic 30 min before if the dressing is painful; screen the bed; close fans and windows; do not dress during ward cleaning or bed making.",
        "__Wash hands__; clean the trolley from top to bottom with an antiseptic; arrange the articles; open the sterile pack without touching the inside.",
        "Position the patient, expose only the wound, place a mackintosh and towel under the part.",
        "Wear clean gloves and remove the outer dressing; __moisten the adherent inner layer with saline__ and remove it gently in the direction of hair growth, ~never dry-pull~; observe the amount, colour and odour of the discharge; discard into the paper bag; remove the gloves.",
        "Perform hand hygiene; wear __sterile gloves__ and arrange the sterile field.",
        "Clean the wound with saline on a swab __from the centre outwards / from the cleanest to the dirtiest area__, one swab per stroke, discarding each swab; for a drain, clean __around the drain from the inner to the outer area__. In a __sutured wound__, swab along the incision line first, then the surrounding skin.",
        "Dry, apply the prescribed medication, cover with sterile gauze and a pad __extending at least 2.5 cm beyond the wound margin__, and secure with adhesive tape (applied across, not along, the limb) or a bandage.",
        "Position the patient comfortably; remove the gloves; discard the waste in the correct colour-coded bag; wash and disinfect instruments; wash hands.",
        "__Record__ the date and time, the appearance of the wound and surrounding skin, the type and amount of discharge, the medication used, the condition of sutures/drain, the amount of drainage and the patient's response to the procedure."
    ])
    b.box("caution", [
        "* Dress __clean wounds before infected wounds__; a patient with an infected wound is dressed last, and the trolley is re-sterilised afterwards.",
        "* Never use the same swab twice; never use the same forceps for a clean and a dirty wound (use the '2 forceps technique' — one to hold the swab that touches the wound, one to hand over the material).",
        "* Do not cough, sneeze or talk over an open wound; wear a mask if you have a cold.",
        "* Never use cotton wool directly on an open wound (fibres stick); use gauze.",
    ])
    b.sub("Types of dressings")
    b.table(
        ["Dressing", "Description / indication"],
        [["Dry gauze / gauze and pad", "Clean, sutured, dry wounds"],
         ["__Wet-to-dry saline dressing__", "Mechanical debridement of sloughy wounds"],
         ["__Hydrocolloid__ (e.g. Duoderm)", "Pressure sores, minimal-exudate wounds; keeps the wound moist and can stay 3-7 days"],
         ["__Hydrogel__", "Dry, necrotic wounds; rehydrates and promotes autolytic debridement"],
         ["__Alginate (seaweed)__", "Heavily exuding wounds and cavities; also haemostatic"],
         ["__Foam__", "Moderate-to-heavy exudate; cushions pressure areas"],
         ["Transparent film (Tegaderm)", "IV sites, superficial wounds — allows inspection"],
         ["Paraffin gauze/tulle gras, silver or honey dressing", "Burns, skin graft donor sites, infected wounds"],
         ["__Pressure dressing__", "Controls bleeding and oozing after surgery"],
         ["__Negative pressure (vacuum) dressing__", "Large cavity wounds, dehiscence, diabetic foot"]],
        caption="Table 8.6  Types of dressings")

    b.section_h("8.5", "Sutures, Staples and Drains")
    b.table(
        ["Suture material", "Type", "Notes"],
        [["__Catgut__ (plain 7-10 days, chromic 14-21 days)", "Absorbable, natural", "Ligating vessels, subcutaneous tissue; now largely replaced"],
         ["__Polyglactin (Vicryl), polyglycolic acid (Dexon), poliglecaprone (Monocryl), PDS__", "Absorbable, synthetic", "Deep layers, bowel, subcuticular closure"],
         ["__Silk, linen, cotton__", "Non-absorbable, natural (braided)", "Skin, bowel, ligation; braided sutures hold knots well but harbour organisms"],
         ["__Nylon (Ethilon), polypropylene (Prolene), stainless steel__", "Non-absorbable, synthetic (monofilament)", "Skin closure, hernia mesh, tendon and vascular repair; low infection risk"],
         ["__Skin staples, adhesive strips (Steri-strips), tissue glue__", "-", "Quick skin closure; strips used after removing alternate sutures"]],
        caption="Table 8.7  Suture materials")
    b.bullets([
        "Suture __sizes__ run 5, 4, 3, 2, 1, 0, 2-0, 3-0 … 10-0; the __more zeros, the finer the thread__ (10-0 is used for eye and microvascular surgery; 1 or 2 for the abdominal wall).",
        "__Time of removal of skin sutures__: face and neck __3-5 days__; scalp, arm and hand 7-10 days; trunk/abdomen and chest __7-10 days__; back and over joints, leg and foot __10-14 days__; retention sutures 14-21 days. Children heal faster; diabetics, steroid users and the malnourished need longer.",
        "__Removing sutures__ — sterile technique with stitch scissors/blade and forceps: clean the line, lift the knot with forceps, cut the suture __close to the skin on the side away from the knot__ so that no part that was outside the skin is drawn through the tissue; pull out towards the wound; remove __alternate sutures first__ and inspect for gaping; support the wound with adhesive strips; count and record the number removed.",
        "__Drains__ — remove blood, pus, serum, bile or air and prevent collection: ~open/passive~ (corrugated rubber, Penrose, gauze wick), ~closed~ (Redivac/suction, chest tube with an underwater seal, T-tube for the bile duct, Malecot/Foley, Jackson-Pratt, Ryle's tube, Infant feeding tube). Nursing care: keep the bag __below the level of the wound__ (never raise it above), never let it kink, measure and record the drainage every shift (__report over 100 mL/hour of fresh blood or a sudden stop of drainage__), keep the site dressed and dry, never empty a chest drain bottle or clamp a chest tube without an order, and clamp before moving only if instructed.",
    ])

    b.section_h("8.6", "Common Surgical Instruments and their Use")
    b.table(
        ["Instrument", "Use"],
        [["Scalpel (BP handle No. 3/4 with blade No. 10, 11, 15, 22)", "Incising tissue"],
         ["__Artery (haemostatic) forceps — Spencer Wells, Kocher, Mosquito__", "Clamping bleeding vessels"],
         ["Dissecting forceps (toothed and non-toothed), Allis, Babcock", "Holding tissue; Babcock for bowel"],
         ["__Sponge-holding forceps (Rampley)__", "Holding swabs to paint the skin"],
         ["__Cheatle/transfer forceps__", "Lifting sterile articles from a drum"],
         ["Needle holder (Mayo-Hegar), suture needles (straight, curved, cutting, round)", "Suturing"],
         ["Scissors — Mayo (tissue), Metzenbaum (fine), stitch scissors", "Cutting tissue and sutures"],
         ["Retractors — Langenbeck, Deaver, Morris, self-retaining (Balfour)", "Holding the wound open"],
         ["Towel clips (Backhaus)", "Fixing sterile drapes"],
         ["Sinus forceps, probe, grooved director", "Exploring a sinus or abscess cavity"],
         ["Trocar and cannula, aspirating needle, syringes", "Drainage of fluid, aspiration"],
         ["__Autoclave drum, sterilisation indicator tape, kidney tray, gallipot, instrument tray__", "Sterilisation and holding"]],
        caption="Table 8.8  Basic surgical instruments")

    b.section_h("8.7", "Minor Surgical Procedures — Nursing Assistance")
    b.kv_bullets([
        ("Incision and drainage of an abscess", "explain and obtain consent; prepare local anaesthetic (lignocaine 2%), scalpel, sinus forceps, drain/wick, specimen bottle for culture and sensitivity, dressings; after care — observe bleeding, change the dressing as ordered, complete the antibiotic course, warm compresses."),
        ("Suturing of a laceration", "clean with saline, check tetanus immunisation status, assist with local anaesthesia and suturing, give wound care instructions and the date of suture removal, watch for signs of infection."),
        ("Aspiration (pleural/ascitic/joint)", "position the patient correctly, keep the specimen bottles labelled, monitor vital signs during and after, apply a sterile dressing, strict asepsis (see Chapter 23)."),
        ("Removal of a foreign body, nail avulsion, biopsy, catheterisation, venesection", "sterile tray, good light, correct position, specimen handling, documentation."),
        ("Tetanus prophylaxis in a wound", "clean wound with complete immunisation and the last dose under 5 years → nothing needed; unimmunised or dirty/deep/puncture wound → __tetanus toxoid (Td) plus tetanus immunoglobulin (TIG 250-500 IU)__ and thorough surgical toilet with antibiotics."),
    ])

    b.box("recap", [
        "* Medical asepsis = clean technique; surgical asepsis = sterile technique; the outer 1 inch of a sterile drape and anything below the waist is unsterile; moisture contaminates.",
        "* Surgical scrub 3-5 min with chlorhexidine 4% or povidone-iodine 7.5%; hands held above the elbows.",
        "* Healing phases: haemostasis → inflammatory (0-4 d) → proliferative (3-21 d) → maturation (up to 2 years, 70-80% strength).",
        "* First intention = clean sutured wound; second intention = granulation; third = delayed closure.",
        "* Infection is the commonest cause of delayed healing; vitamin C and protein are essential.",
        "* Clean the wound from the centre outwards, one swab one stroke; dress clean wounds before infected ones.",
        "* Secondary haemorrhage occurs after 7-14 days from infection; dehiscence typically on day 5-10.",
        "* Sutures: face 3-5 days, abdomen/trunk 7-10 days, over joints/leg 10-14 days; more zeros = finer suture.",
        "* Keep drainage bags below the wound; evisceration — cover with sterile saline gauze, do not push back.",
    ])



def chapter_9(b):
    b.chapter(9, "Diet",
              "Nutrients, balanced diet, therapeutic diets, feeding the helpless patient, tube and parenteral feeding")

    b.section_h("9.1", "Basic Concepts and Definitions")
    b.table(
        ["Term", "Definition"],
        [["__Food__", "Any edible substance that supplies the body with nourishment"],
         ["__Nutrient__", "A chemical component of food required for growth, repair, energy and regulation — carbohydrate, protein, fat, vitamins, minerals, water (and dietary fibre)"],
         ["__Nutrition__", "The science of food and its relationship to health — the sum of the processes of ingestion, digestion, absorption, metabolism, utilisation and excretion"],
         ["__Dietetics__", "The practical application of the principles of nutrition to feeding individuals and groups"],
         ["__Diet__", "The usual food and drink of a person"],
         ["__Therapeutic (modified) diet__", "A normal diet modified in consistency, nutrients or energy to suit a disease condition"],
         ["__Balanced diet__", "A diet that contains all nutrients in the correct proportions and amounts to meet the body's requirements, with a small margin for lean periods"],
         ["__Malnutrition__", "Any disorder of nutrition — under-nutrition, over-nutrition or imbalance"],
         ["__RDA__", "Recommended Dietary Allowance — the amount of a nutrient sufficient for nearly all (97.5%) healthy persons in a group (given by __ICMR-NIN__ in India)"],
         ["__Basal metabolic rate (BMR)__", "Energy needed at complete rest to maintain the vital functions — about __1 kcal/kg/hour__ (roughly 1600-1800 kcal/day in an adult male)"],
         ["__Anorexia / Cachexia__", "Loss of appetite / extreme wasting"]],
        caption="Table 9.1  Nutritional terminology")

    b.section_h("9.2", "The Nutrients — Functions, Sources and Deficiency")
    b.table(
        ["Nutrient", "Energy value & requirement", "Functions", "Good sources", "Deficiency"],
        [["__Carbohydrate__", "__4 kcal/g__; should give __55-60%__ of total calories",
          "Chief and cheapest source of energy; spares protein; provides fibre; needed for fat metabolism",
          "Cereals (rice, wheat, maize), millets, potato, sugar, jaggery, honey, fruits, milk (lactose)",
          "Weakness, weight loss, ketosis, marasmus"],
         ["__Protein__", "__4 kcal/g__; __10-15%__ of calories; RDA about __0.8-1 g/kg/day__ (more in illness, pregnancy, lactation, burns: 1.2-2 g/kg)",
          "Growth and repair of tissue, enzymes, hormones, antibodies, haemoglobin, plasma proteins (oncotic pressure), wound healing",
          "__Class I (complete, animal)__ — milk, egg (the reference protein, biological value 100), meat, fish, liver; __Class II (incomplete, vegetable)__ — pulses/dal, soya, nuts, cereals",
          "__Kwashiorkor__ (oedema, moon face, flaky-paint dermatosis, fatty liver, apathy, hair changes), __marasmus__ (severe wasting, under 60% weight, old-man face), poor healing, anaemia, hypoalbuminaemia, frequent infection"],
         ["__Fat__", "__9 kcal/g__ (the most concentrated); __20-30%__ of calories (visible fat 20-30 g/day)",
          "Energy store, insulation, protects organs, carries the fat-soluble vitamins A, D, E, K, supplies essential fatty acids (linoleic, alpha-linolenic), palatability",
          "Ghee, butter, oils, nuts, oil seeds, milk, egg yolk, meat, fish oil",
          "Growth retardation, dermatitis (essential fatty acid deficiency), deficiency of vitamins A, D, E, K; ~excess~ → obesity, atherosclerosis"],
         ["__Water__", "Nil calories; __2-3 L/day (30-35 mL/kg)__",
          "Solvent and transport medium, regulates temperature, lubricates, excretes waste; 60-70% of body weight",
          "Drinking water, milk, juice, soup, fruits, vegetables",
          "__Dehydration__ — thirst, dry mouth, sunken eyes, poor skin turgor, concentrated scanty urine, tachycardia, fall of BP, confusion"],
         ["__Dietary fibre__", "Nil (non-digestible); __25-40 g/day__",
          "Adds bulk, prevents constipation, lowers cholesterol and blood sugar, gives satiety, prevents colon cancer, piles and diverticulosis",
          "Whole grains, bran, oats, pulses, green leafy vegetables, fruit with skin, guava, isabgol",
          "Constipation, piles, diverticulosis, obesity, raised cholesterol"]],
        caption="Table 9.2  The macronutrients")
    b.box("num", [
        "__Energy values: carbohydrate 4 kcal/g • protein 4 kcal/g • fat 9 kcal/g • alcohol 7 kcal/g.__",
        "Egg protein has the highest __biological value (100)__ and is the reference protein; egg is a complete food except for __vitamin C and iron__ (and fibre).",
        "__1 g of nitrogen = 6.25 g of protein.__  Ideal ratio of calories: carbohydrate : protein : fat = 60 : 15 : 25 (approx).",
    ])

    b.section_h("9.3", "Vitamins")
    b.table(
        ["Vitamin", "Functions", "Sources", "Deficiency disease"],
        [["__A (retinol / beta-carotene)__ — fat soluble; RDA 600-1000 mcg",
          "Vision in dim light (rhodopsin), integrity of epithelium, immunity, growth",
          "Liver, fish liver oil, milk, butter, egg yolk; carrot, papaya, mango, green leafy vegetables (carotene)",
          "__Night blindness → conjunctival xerosis → Bitot's spots → corneal xerosis → keratomalacia (blindness)__; follicular hyperkeratosis; ~excess is teratogenic~"],
         ["__D (calciferol)__ — the 'sunshine vitamin'; 400-600 IU",
          "Absorption of calcium and phosphorus; bone mineralisation",
          "Sunlight on skin (chief source), fish liver oil, egg yolk, fortified milk",
          "__Rickets__ in children (bow legs, rickety rosary, craniotabes, pot belly, delayed closure of fontanelle), __osteomalacia__ in adults, tetany"],
         ["__E (tocopherol)__", "Antioxidant, protects cell membranes and red cells, fertility",
          "Vegetable oils, wheat germ, nuts, green leafy vegetables",
          "Haemolytic anaemia in preterm babies, neuropathy"],
         ["__K (phylloquinone)__", "Synthesis of __prothrombin and clotting factors II, VII, IX, X__",
          "Green leafy vegetables, liver; synthesised by gut bacteria",
          "__Bleeding tendency, haemorrhagic disease of the newborn__ (hence 1 mg IM at birth), prolonged prothrombin time"],
         ["__B1 (thiamine)__", "Coenzyme in carbohydrate metabolism; nerve function",
          "Whole grains, rice polishings, pulses, nuts, pork, yeast (lost in polishing rice and in cooking soda)",
          "__Beri-beri__ — ~dry~ (peripheral neuritis, burning feet, wrist drop) and ~wet~ (oedema, heart failure); __Wernicke-Korsakoff psychosis__ in alcoholics"],
         ["__B2 (riboflavin)__", "Flavoprotein coenzymes in oxidation",
          "Milk, egg, liver, green leafy vegetables, pulses",
          "__Angular stomatitis, cheilosis, glossitis, magenta tongue, photophobia, scrotal dermatitis__"],
         ["__B3 (niacin / nicotinic acid)__", "NAD/NADP coenzymes; can be made from tryptophan",
          "Liver, meat, fish, groundnut, whole grains (maize-eaters are at risk — niacin is bound)",
          "__Pellagra — the 3 D's: Dermatitis (in sun-exposed areas, Casal's necklace), Diarrhoea, Dementia__ (4th D = death)"],
         ["__B6 (pyridoxine)__", "Amino acid metabolism, haem synthesis",
          "Meat, liver, whole grains, banana, nuts",
          "Peripheral neuritis (~isoniazid therapy — hence give pyridoxine with INH~), convulsions in infants, sideroblastic anaemia"],
         ["__B9 (folic acid)__ — 200-500 mcg (pregnancy 400-600 mcg)",
          "DNA synthesis, red cell maturation, prevents neural tube defects",
          "Green leafy vegetables, liver, pulses, nuts (destroyed by cooking)",
          "__Megaloblastic anaemia, glossitis, neural tube defect (spina bifida) in the fetus__"],
         ["__B12 (cyanocobalamin)__ — 1-2 mcg",
          "DNA synthesis, myelin formation; needs __intrinsic factor__ from the stomach for absorption",
          "__Only animal foods__ — liver, meat, fish, egg, milk (strict vegans are at risk)",
          "__Pernicious (megaloblastic) anaemia__ with __subacute combined degeneration of the cord__ (glossitis, paraesthesia, ataxia)"],
         ["__C (ascorbic acid)__ — 40-80 mg",
          "Collagen formation and __wound healing__, antioxidant, __enhances iron absorption__, immunity",
          "Amla (richest), guava, citrus fruits, tomato, green chilli, sprouts, cabbage (easily destroyed by heat, light and cooking soda)",
          "__Scurvy__ — spongy bleeding gums, petechiae, subperiosteal haemorrhage, painful swollen joints, delayed wound healing, anaemia"]],
        caption="Table 9.3  Vitamins — a very high-yield table")

    b.section_h("9.4", "Minerals")
    b.table(
        ["Mineral", "Functions and requirement", "Sources", "Deficiency / excess"],
        [["__Calcium__ (RDA adult about 600-1000 mg; pregnancy/lactation 1200 mg)",
          "Bone and teeth (99%), clotting, muscle contraction, nerve conduction, enzyme action",
          "Milk and milk products, ragi, til (sesame), green leafy vegetables, small fish with bones",
          "Rickets, osteomalacia, __osteoporosis__, tetany (carpopedal spasm, positive Trousseau and Chvostek signs)"],
         ["__Phosphorus__", "Bone, ATP, nucleic acids, buffers", "Milk, cereals, pulses, meat, egg", "Rickets, weakness"],
         ["__Iron__ (RDA man 17-19 mg, woman 21-29 mg, pregnancy 27-35 mg)",
          "Haemoglobin, myoglobin, cytochromes; __haem iron (animal) is much better absorbed than non-haem (plant)__; absorption is increased by vitamin C and decreased by phytates, tannin (tea), calcium and antacids",
          "Liver, meat, fish, egg yolk, green leafy vegetables, jaggery, dates, ragi, pulses",
          "__Iron deficiency (microcytic hypochromic) anaemia__ — pallor, weakness, koilonychia, glossitis, pica; the commonest nutritional deficiency in the world"],
         ["__Iodine__ (RDA 150 mcg; pregnancy 250 mcg)",
          "Thyroid hormones T3 and T4 (growth and metabolism)",
          "__Iodised salt__, sea fish, sea weed, milk",
          "__Goitre, hypothyroidism, cretinism__ (in children — mental and physical retardation, deaf-mutism), still birth, myxoedema; ~India: iodised salt must contain at least 15 ppm iodine at the consumer level~"],
         ["__Sodium / Chloride__", "Extracellular fluid volume, osmotic pressure, nerve conduction; need under __5 g of salt (2 g sodium)/day__",
          "Common salt, processed and preserved food, papad, pickle",
          "Hyponatraemia (confusion, fits) with vomiting/diuretics; __excess → hypertension, oedema__"],
         ["__Potassium__", "Main intracellular cation; cardiac and muscle function",
          "Banana, citrus fruits, coconut water, potato, tender coconut, dal, dry fruits",
          "__Hypokalaemia__ (diarrhoea, vomiting, diuretics) → weakness, arrhythmia, ileus; __hyperkalaemia__ (renal failure) → cardiac arrest"],
         ["__Zinc__", "Wound healing, immunity, growth, taste, insulin", "Meat, liver, egg, whole grains, pulses, nuts",
          "Poor healing, growth retardation, diarrhoea, loss of taste, hypogonadism, acrodermatitis"],
         ["__Magnesium, copper, selenium, fluoride, chromium__",
          "Enzyme cofactors; fluoride prevents dental caries",
          "Green vegetables, nuts, whole grains, water",
          "Fluoride: under 0.5 ppm → dental caries; __over 1.5-2 ppm → dental and skeletal fluorosis__ (optimum in drinking water about 0.5-0.8 ppm in India)"]],
        caption="Table 9.4  Important minerals")

    b.section_h("9.5", "The Balanced Diet and the Food Groups")
    b.table(
        ["Food group (ICMR)", "Examples", "Chief nutrients supplied"],
        [["1. __Cereals, millets and pulses__", "Rice, wheat, jowar, bajra, ragi, dal, rajma", "Energy, protein, B vitamins, iron, fibre"],
         ["2. __Vegetables and fruits__", "Green leafy vegetables, roots and tubers, other vegetables, all fruits",
          "Vitamins A and C, folate, minerals, fibre, antioxidants"],
         ["3. __Milk and milk products; egg, meat and fish__", "Milk, curd, paneer, egg, chicken, fish",
          "Good-quality protein, calcium, vitamin B12, vitamin A"],
         ["4. __Oils, fats, nuts and oilseeds__", "Groundnut oil, mustard oil, ghee, butter, almond, til", "Energy, essential fatty acids, fat-soluble vitamins"],
         ["5. __Sugars__", "Sugar, jaggery, honey", "Energy only ('empty calories')"]],
        caption="Table 9.5  The five food groups")
    b.sub("Approximate daily requirement of an adult (sedentary, ICMR guidelines)")
    b.table(
        ["Food", "Amount per day"],
        [["Cereals and millets", "300-400 g (sedentary man 375 g, woman 270 g)"],
         ["Pulses", "__60-80 g__ (at least 30 g if non-vegetarian)"],
         ["Milk / curd", "__300-500 mL__"],
         ["Green leafy vegetables", "__100 g__"],
         ["Other vegetables and roots/tubers", "200 g + 100 g"],
         ["Fruits", "__100-200 g__"],
         ["Visible fat / oil", "20-30 g (up to 25 g for sedentary work)"],
         ["Sugar / jaggery", "Under 20-25 g"],
         ["Nuts and oilseeds", "20-30 g"],
         ["Egg / meat / fish (non-vegetarian)", "1 egg or 50-75 g"],
         ["Salt", "__Under 5 g__"],
         ["Water", "8-12 glasses (2-3 L)"]],
        caption="Table 9.6  Daily food guide for an adult", align_center_cols=(1,))
    b.box("num", [
        "Approximate energy requirement: __sedentary adult man 2100-2320 kcal, moderate 2700 kcal, heavy 3500 kcal__; adult woman 1900-2100 / 2200 / 2900 kcal.",
        "__Pregnancy: + 350 kcal and + 15-23 g protein__ (2nd and 3rd trimester).  __Lactation (0-6 months): + 600 kcal and + 19-25 g protein.__",
        "Body Mass Index __BMI = weight (kg) / height (m)2__:  under 18.5 = underweight • __18.5-22.9 normal (Asian)__ • 23-24.9 overweight • 25 or more = obese (WHO: 25-29.9 overweight, 30+ obese).",
        "Waist circumference of concern: __men over 90 cm, women over 80 cm__ (Asian).",
    ])

    b.section_h("9.6", "Therapeutic Diets — Modifications in Consistency")
    b.table(
        ["Diet", "Composition", "Indications"],
        [["__Clear liquid diet__", "Water, clear broth/soup without fat, strained fruit juice, barley water, whey water, coconut water, black tea, glucose water, ORS, jelly — no milk or solids; about 400-500 kcal only",
          "First 24-48 h after surgery, acute vomiting/diarrhoea, before bowel investigations, on return of bowel sounds"],
         ["__Full liquid diet__", "Everything liquid at body temperature — milk, custard, ice cream, strained soups, egg-flip, lassi, porridge, soft cereal gruel, fruit juice; can be nutritionally adequate with supplements",
          "Difficulty in chewing/swallowing, jaw wiring, oral surgery, high fever, unconscious/tube feeding, after a clear liquid diet"],
         ["__Soft / bland diet__", "Soft-cooked, low-fibre, non-spicy food — khichri, dalia, curd, banana, boiled potato, soft chapatti, custard, cooked vegetables without skin",
          "Convalescence, after surgery, peptic ulcer, gastritis, diarrhoea, elderly, small children, no teeth"],
         ["__Light / semi-solid diet__", "Between soft and normal diet, easily digestible", "Convalescent and ambulant patients"],
         ["__Regular (normal/full) diet__", "Balanced diet of the household, no restriction", "Patients with no dietary restriction"],
         ["__Mechanically altered/pureed/thickened__", "Minced, mashed, pureed or thickened with a commercial thickener",
          "__Dysphagia__ (stroke, motor neuron disease, Parkinsonism) — thin liquids are the most dangerous for aspiration"]],
        caption="Table 9.7  Diets modified in consistency")

    b.section_h("9.7", "Therapeutic Diets in Disease")
    b.table(
        ["Condition", "Diet principles", "Allow", "Avoid / restrict"],
        [["__Fever / infection__", "High calorie (2500-3000 kcal), high protein, high fluid (3 L), plenty of vitamin C; small frequent bland feeds; extra 7% calories for every 1 °F rise",
          "Milk, curd, soft khichri, egg, soup, juice, glucose water, ORS", "Heavy fried and spicy food, high fibre"],
         ["__Diabetes mellitus__", "Calorie-controlled, __high complex carbohydrate and fibre (30-40 g)__, low glycaemic index, 3 meals plus 2-3 snacks at fixed times, carbohydrate distributed evenly, weight reduction if obese; protein 15-20%, saturated fat under 7%",
          "Whole grains, millets, oats, pulses, green vegetables, fenugreek, salads, bitter gourd, whole fruit in measured amounts, artificial sweeteners",
          "__Sugar, jaggery, honey, sweets, glucose, soft drinks, fruit juice, dry fruits, banana/mango in excess, refined flour, fried food, alcohol; no skipping or delaying meals__"],
         ["__Hypertension / heart disease__", "__Low salt (under 5 g; 2-3 g in heart failure)__, low saturated fat and cholesterol, high potassium, high fibre, weight reduction, __DASH diet__",
          "Fruits, vegetables, whole grains, low-fat milk, fish, garlic, unsaturated oils",
          "Salt at the table, papad, pickles, pappadam, chips, processed and canned food, ghee/butter/vanaspati, red meat, organ meat, egg yolk (limit), coffee, alcohol, smoking"],
         ["__Myocardial infarction (first days)__", "Soft, low-calorie, low-salt, small frequent feeds, no hot/cold extremes, no straining or gas-forming food",
          "Liquids first, then soft diet", "Caffeine, heavy meals, constipating food"],
         ["__Chronic kidney disease / renal failure__", "__Low protein (0.6-0.8 g/kg, high biological value)__, low sodium, __low potassium, low phosphate__, fluid restriction as per urine output, adequate calories from carbohydrate",
          "Rice, sago, arrowroot, apple/papaya, gourd vegetables, leached (double-boiled) vegetables",
          "Banana, citrus, coconut water, dry fruits, potato, tomato, dal in excess, milk in excess, salt, nuts, chocolate, cola"],
         ["__Nephrotic syndrome__", "Normal-to-high protein (1 g/kg), __low salt__, low fat", "Egg white, fish, pulses", "Salt, fried food"],
         ["__Renal stones__", "__High fluid (3-4 L/day)__; for calcium oxalate stones, low oxalate", "Plenty of water, citrus (citrate)", "Spinach, tomato seeds, beetroot, chocolate, tea, nuts, excess salt and animal protein"],
         ["__Liver disease / hepatitis__", "__High carbohydrate, moderate protein, low fat__, no alcohol; small frequent feeds; vitamin supplements",
          "Glucose, fruit juice, rice, potato, curd, egg white", "Fried and fatty food, __alcohol strictly__, red meat"],
         ["__Hepatic coma (encephalopathy)__", "__Protein restricted (20-40 g) or vegetable protein__, high calorie, lactulose for constipation",
          "Glucose drinks, vegetable protein", "Animal protein, salt (if ascites), constipation"],
         ["__Peptic ulcer / gastritis__", "Bland, soft, small frequent meals (every 2-3 h), adequate protein, no long fasting",
          "Milk, curd, banana, boiled vegetables, soft rice", "__Chilli, spices, pickles, fried food, tea/coffee, aerated drinks, alcohol, smoking, aspirin/NSAIDs__"],
         ["__Diarrhoea__", "Fluid and electrolyte replacement with __ORS__, continue feeding (never starve), low fibre, low fat, small frequent feeds; __continue breast feeding__",
          "ORS, rice water (kanji), curd, banana, apple, boiled potato, khichri, buttermilk, coconut water",
          "Milk (if lactose intolerant), high fibre, fried, spicy, sugary drinks"],
         ["__Constipation__", "__High fibre (30-40 g) and high fluid__, regular meals and exercise",
          "Whole grains, bran, papaya, guava, figs, prunes, green vegetables, isabgol, warm water in the morning",
          "Refined flour, polished rice, low fluid, excess tea"],
         ["__Obesity__", "Calorie deficit of __500-1000 kcal/day__ for 0.5 kg/week loss; high fibre and protein, low fat and sugar; behaviour change and exercise (150 min/week)",
          "Salads, whole grains, low-fat milk, sprouts, plenty of water", "Sugar, fried food, sweets, ghee, refined flour, alcohol, snacking"],
         ["__Underweight / tuberculosis / cancer / HIV / burns__", "__High calorie (35-45 kcal/kg), high protein (1.5-2 g/kg)__, vitamins and minerals, small frequent energy-dense feeds",
          "Milk shakes, banana, egg, ghee, nuts, paneer, chicken/fish, supplements", "Bulky low-calorie food that fills the stomach"],
         ["__Gout__", "__Low purine__, high fluid, weight reduction", "Milk, egg, vegetables, cereals",
          "__Organ meat (liver, kidney, brain), red meat, sardine, shellfish, yeast extract, alcohol especially beer__, pulses in excess"],
         ["__Coeliac disease__", "__Gluten-free__", "Rice, maize, millets, potato, soya", "__Wheat, barley, rye and oats (gluten)__"],
         ["__Hyperthyroidism / Hypothyroidism__", "High calorie, high protein / calorie-controlled with adequate iodine",
          "-", "Goitrogens in excess (cabbage, cauliflower) in hypothyroidism"],
         ["__Anaemia__", "Iron and folate rich, __vitamin C with meals__ to aid absorption", "Green leafy vegetables, jaggery, dates, liver, meat, ragi, amla, sprouts",
          "__Tea and coffee with meals__ (tannins), antacids and calcium with iron"],
         ["__Pre-eclampsia in pregnancy__", "Adequate protein, moderate salt restriction, plenty of fluids, calcium",
          "Milk, fruits, vegetables", "Excess salt, processed food"]],
        caption="Table 9.8  Therapeutic diets in common diseases")

    b.section_h("9.8", "Serving Food and Feeding the Helpless Patient")
    b.bullets([
        "__Before the meal__ — remove bedpans, urinals and soiled dressings; ventilate the room; give mouth care and help with hand washing; place the patient in a __sitting or high Fowler's (at least 30-45°) position__; do not carry out treatments or investigations at meal times.",
        "Serve food __attractively, in the right quantity, at the right temperature__ (hot food hot, cold food cold), on clean crockery, with the tray checked against the diet order and the patient's name.",
        "__Feeding__ — sit at the patient's eye level, do not rush, offer small mouthfuls, tell a blind patient what is on the plate ('use the clock method'), allow the patient to hold the cup or spoon if he can, offer fluids between mouthfuls with a straw or feeding cup, give the food __on the unaffected side__ in stroke patients.",
        "__Watch for aspiration__ — coughing, choking, wet voice, drooling; keep suction ready for high-risk patients; __keep the patient sitting up for 30-60 minutes after the meal__.",
        "Encourage self-feeding with adapted spoons, plate guards and non-slip mats (rehabilitation); praise and do not hurry.",
        "__After the meal__ — mouth care, hand washing, note and record the __amount actually eaten__, and report anorexia, nausea, dysphagia or refusal; record the intake on the fluid chart.",
    ])
    b.box("clinical", ["Never feed an __unconscious patient or a patient without a gag reflex by mouth__ — the risk of aspiration pneumonia is very high. Use a nasogastric tube or intravenous route on the doctor's order."])

    b.section_h("9.9", "Tube (Enteral) Feeding")
    b.bullets([
        "__Routes__ — __nasogastric (Ryle's tube, the commonest)__, nasoduodenal/nasojejunal, __gastrostomy (PEG)__ and jejunostomy for long-term feeding (over 4-6 weeks), and oro-gastric in newborns.",
        "__Indications__ — unconscious patient, stroke with dysphagia, head and neck or oesophageal cancer, oesophageal stricture or burns, jaw fracture, severe anorexia, extensive burns, prematurity, tetanus, coma, post-operative feeding.",
        "__Tube sizes__ — adults 12-18 Fr; children 8-10 Fr; infants 5-8 Fr. Length to insert = the __NEX measurement__ (from the tip of the Nose to the Ear lobe to the Xiphisternum, about 45-55 cm in an adult).",
        "__Confirming the position (before every feed)__ — best method is __measuring the pH of the aspirate (pH 5.5 or less = gastric)__; X-ray confirmation is the gold standard at the first insertion; also check the external length mark and inspect the mouth; ~the old 'auscultate while pushing air' (whoosh) test is now considered unreliable~.",
        "__Procedure of feeding__ — sit the patient at __30-45° and keep him so for 30-60 min after the feed__; check the position and the __gastric residual volume__ (withhold and inform if it exceeds about 200-250 mL or the ordered limit; return the aspirate); feed at room/body temperature by gravity over 15-20 minutes (never force with a plunger); __flush with 30-50 mL of water before and after__ the feed and after medicines; keep the feed volume to 200-400 mL per feed, 3-6 hourly, or use a continuous pump.",
        "Give crushed/liquid medicines separately, flushing between each; never mix drugs with the feed unless permitted.",
        "__Complications__ — aspiration pneumonia (the most serious), tube blockage, displacement or coiling, diarrhoea or constipation, abdominal distension and cramps, hyperglycaemia, electrolyte imbalance, refeeding syndrome, nasal and oesophageal erosion, sinusitis and otitis.",
        "__Nursing care__ — oral and nasal hygiene twice daily, change the fixing tape daily and alternate the nostril position, watch the skin at the nostril, keep the tube capped when not in use, change the tube as per policy, and record the type, amount and tolerance of each feed.",
    ])
    b.box("caution", ["If the patient __coughs, chokes, becomes cyanosed or cannot speak__ during insertion, the tube may be in the trachea — __withdraw it at once__. Never instil anything into a tube whose position has not been confirmed."])

    b.section_h("9.10", "Parenteral Nutrition and Fluids")
    b.bullets([
        "__Total parenteral nutrition (TPN)__ — all nutrients (glucose, amino acids, lipid emulsion, electrolytes, vitamins and trace elements) given __intravenously__, usually through a __central line__ because the solution is hypertonic; peripheral partial nutrition (PPN) may be used for short periods.",
        "__Indications__ — non-functioning gut: intestinal obstruction, high-output fistula, short bowel syndrome, severe pancreatitis, prolonged ileus, severe malabsorption, major burns, hyperemesis gravidarum.",
        "__Nursing care__ — strict aseptic technique with the central line (the greatest risk is __catheter-related blood stream infection__), use a dedicated lumen, __never interrupt suddenly__ (risk of rebound hypoglycaemia — taper off), monitor blood sugar 4-6 hourly, daily weight, strict intake-output, electrolytes and liver function, watch for fluid overload, hyperglycaemia, electrolyte disturbance and __refeeding syndrome__ (low phosphate, potassium and magnesium), change the giving set every 24 hours, keep the bag refrigerated and use within 24 hours of hanging.",
        "'__If the gut works, use it__' — enteral feeding is always preferred as it is cheaper, safer and maintains the gut mucosa.",
    ])

    b.section_h("9.11", "Food Hygiene and Food Poisoning")
    b.bullets([
        "__Rules of food hygiene__ — wash hands before cooking and eating; use safe water; wash fruits and vegetables; cook food thoroughly (__above 70 °C in the centre__); eat food __freshly cooked (within 2 hours)__; store cooked food either __above 60 °C or below 5 °C__ and reheat thoroughly; keep raw and cooked food separate; keep food covered and away from flies and pets; clean kitchen surfaces; do not let an ill person (diarrhoea, skin sores) cook for others; check expiry dates and do not use swollen, dented or leaking cans.",
        "__Food poisoning__ — ~Staphylococcus aureus~ (toxin, 1-6 h, vomiting, from cream/milk/meat handled by a person with a skin lesion), ~Bacillus cereus~ (reheated rice), ~Clostridium perfringens~ (meat dishes), ~Clostridium botulinum~ (canned food — paralysis, diplopia, dysphagia; a medical emergency), ~Salmonella~ (12-36 h, egg and poultry), ~Vibrio parahaemolyticus~ (seafood), ~E. coli~, mushroom and chemical poisoning.",
        "Danger zone for bacterial multiplication in food: __5-60 °C__.",
        "__Food-borne diseases__ also include typhoid, cholera, hepatitis A and E, amoebiasis, giardiasis, taeniasis, trichinosis and brucellosis.",
    ])

    b.box("recap", [
        "* Carbohydrate 4, protein 4, fat 9 kcal/g; carbohydrate 55-60%, protein 10-15%, fat 20-30% of calories.",
        "* Egg = reference protein (biological value 100), lacks vitamin C and iron.",
        "* Vitamin A → night blindness/Bitot's spots; B1 → beri-beri; B2 → angular stomatitis; B3 → pellagra (3 D's); B12/folate → megaloblastic anaemia; C → scurvy; D → rickets/osteomalacia; K → bleeding.",
        "* Iodine deficiency → goitre/cretinism; iodised salt at least 15 ppm; fluoride over 1.5 ppm → fluorosis.",
        "* BMI = kg/m2; Asian normal 18.5-22.9. Pregnancy + 350 kcal and + 15-23 g protein; lactation + 600 kcal.",
        "* Diets: clear liquid → full liquid → soft → normal; low protein in renal failure, low purine in gout, gluten-free in coeliac, low salt in hypertension.",
        "* NG tube: NEX measurement, confirm by aspirate pH 5.5 or less, feed at 30-45°, flush 30-50 mL water, watch residual volume; aspiration is the most serious complication.",
        "* 'If the gut works, use it' — enteral nutrition is preferred over TPN; TPN needs a central line and strict asepsis.",
        "* Keep cooked food above 60 °C or below 5 °C; danger zone 5-60 °C.",
    ])
