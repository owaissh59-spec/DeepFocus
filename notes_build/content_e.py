"""Chapters 18-21 : Preparation of the Patient for Operation and After Care,
Shock and Blood Transfusion, Special Treatment, Nursing in Special Diseases."""


def chapter_18(b):
    b.chapter(18, "Preparation of the Patient for Operation and the After Care",
              "Pre-operative assessment and preparation, consent, the operation theatre, post-operative care and complications")

    b.section_h("18.1", "Classification of Surgery")
    b.table(
        ["Basis", "Types"],
        [["__Urgency__", "__Emergency__ (immediately, to save life — ruptured spleen, perforation, obstructed labour, extradural haematoma); __Urgent__ (within 24-48 h — acute appendicitis, fracture fixation); __Elective/planned__ (at a convenient time — hernia, cataract, cholelithiasis); __Optional__ (at the patient's choice — cosmetic surgery)"],
         ["__Purpose__", "__Diagnostic__ (biopsy, laparotomy), __Curative/ablative__ (appendicectomy), __Reconstructive/restorative__ (skin graft, joint replacement), __Palliative__ (colostomy for inoperable cancer, debulking), __Cosmetic__, __Transplant__"],
         ["__Degree of risk__", "__Major__ (long duration, body cavity opened, high blood loss, vital organ involved — gastrectomy, craniotomy, open heart surgery) and __Minor__ (short, local or regional anaesthesia, low risk — incision and drainage, biopsy, dilatation and curettage)"],
         ["__Access__", "Open, __minimally invasive (laparoscopic/endoscopic — less pain, small scar, early discharge)__, robotic, day-care surgery"]],
        caption="Table 18.1  Classification of surgical procedures")

    b.section_h("18.2", "Pre-operative Assessment and Investigations")
    b.bullets([
        "__History__ — the presenting illness; previous surgery and anaesthesia (and any problem with it); __allergies (drug, latex, iodine, food)__; current medicines (especially __anticoagulants, antiplatelets, insulin, steroids, antihypertensives, oral contraceptives, herbal products__); tobacco, alcohol and drug use; co-morbidity (diabetes, hypertension, heart, lung, kidney, liver or thyroid disease, epilepsy, bleeding disorder); last menstrual period and possible pregnancy; family history of anaesthetic problems (malignant hyperthermia, pseudocholinesterase deficiency).",
        "__Physical assessment__ — weight and height, vital signs and SpO2, general condition, nutrition and hydration, level of consciousness, examination of the chest and heart, condition of the mouth and teeth (__loose teeth, dentures, caps — a risk during intubation__), the operative site and skin condition, peripheral veins, mobility, and pressure areas.",
        "__Routine investigations__ — haemoglobin, total and differential count, platelets, __blood grouping and cross-matching__, bleeding and clotting time/PT-INR, blood sugar, blood urea and creatinine, serum electrolytes, urine routine, chest X-ray, __ECG (over 40 years or with cardiac disease)__, HIV/HBsAg as per policy; plus special tests — pulmonary function tests, echocardiogram, liver function tests, ultrasound, CT, thyroid profile as indicated.",
        "__Anaesthetic assessment__ — ASA physical status grading (I healthy → V moribund; E for emergency), airway assessment (__Mallampati grade__), and the anaesthesia plan (general, regional/spinal/epidural, local, sedation).",
    ])

    b.section_h("18.3", "Informed Consent")
    b.bullets([
        "Consent must be __informed, written, voluntary, and obtained before any sedation__; it is the __surgeon's/doctor's duty__ to explain the diagnosis, the procedure, the alternatives, the benefits and the risks. The __nurse's role is to witness the signature, confirm that the patient has understood, and ensure the form is complete__ and in the file.",
        "Valid consent requires an adult of __18 years or more__ who is __conscious and of sound mind__. For a __minor (under 18)__, the __parent or legal guardian__ signs; for an unconscious or mentally incapable patient, the next of kin; in a __life-threatening emergency with no relative available, life-saving treatment may be given without consent__ (documented as such by two doctors).",
        "Special consents are needed for __sterilisation (with the spouse's knowledge as per programme rules), medical termination of pregnancy (the woman's own consent; guardian if under 18 or mentally ill), organ donation, high-risk surgery, blood transfusion, anaesthesia, photography and research__.",
        "Consent may be __withdrawn at any time__; a refusal must be documented and reported. Consent must be signed, dated and timed, with the procedure written in full (no abbreviations) and the side/site specified.",
    ])

    b.section_h("18.4", "Pre-operative Preparation")
    b.sub("A. Psychological preparation")
    b.bullets([
        "Allow the patient to __express his fears__ (fear of death, pain, disfigurement, anaesthesia, cancer, dependence, loss of job); answer honestly and simply; never dismiss the fear.",
        "__Explain the routine__ — the time of surgery, fasting, pre-medication, where he will wake up, tubes and drains he may find, the likely pain and its relief, the recovery room, and the expected length of stay.",
        "__Pre-operative teaching (proved to reduce complications)__ — __deep breathing and coughing exercises with splinting of the wound, incentive spirometry, leg and ankle exercises, turning in bed, early ambulation, use of the pain scale and how to ask for analgesia__.",
        "Involve the family; arrange a visit by the anaesthetist and a religious/spiritual visit if desired; ensure a good night's sleep (a sedative may be prescribed).",
    ])
    b.sub("B. Physical preparation (the day before and the day of surgery)")
    b.numbered([
        "__Nutrition and hydration__ — correct anaemia, hypoproteinaemia and dehydration; an IV line/fluids as ordered.",
        "__Fasting (nil by mouth)__ — modern guidelines: __clear fluids up to 2 hours, breast milk 4 hours, light meal/formula 6 hours, and fatty/fried food or a heavy meal 8 hours before anaesthesia__; traditionally 'nothing after midnight'. Put up an 'NPO' board, remove the water jug, and inform the patient and family why (risk of __aspiration/Mendelson's syndrome__).",
        "__Bowel preparation__ — a laxative the night before or an enema/suppository as ordered (essential for bowel, rectal and gynaecological surgery); full mechanical bowel preparation with polyethylene glycol for colorectal surgery; not routinely needed for other operations.",
        "__Bladder__ — ask the patient to __void immediately before going to theatre__; catheterise only if ordered (pelvic, prolonged or major surgery).",
        "__Skin preparation__ — bath or shower with soap (or chlorhexidine) __the night before and on the morning__ of surgery; __hair removal only if necessary and then with a clipper or depilatory cream, immediately before surgery, never with a razor the night before__ (shaving causes micro-abrasions and raises the infection rate); clean the umbilicus; the site is painted with antiseptic in the theatre.",
        "__Removal of prostheses and personal items__ — dentures, contact lenses, spectacles, hearing aid (may be retained till the anaesthetic room if needed), wigs, hair pins, __all jewellery (a ring that will not come off is taped)__, nail polish and make-up (they hide cyanosis and interfere with the pulse oximeter); valuables are listed and handed over to the relatives or the security custody __against a signature__.",
        "__Dress__ — clean theatre gown, cap; anti-embolism stockings if ordered.",
        "__Medication__ — give the __prescribed pre-medication at the exact time__ (sedative/anxiolytic, analgesic, anticholinergic to dry secretions, H2 blocker or proton-pump inhibitor and antacid to reduce gastric acid, antiemetic, __prophylactic antibiotic within 60 minutes of the incision__); continue essential drugs (antihypertensives, antiepileptics, thyroid, cardiac drugs) with a sip of water as advised; __stop/adjust as ordered: warfarin and antiplatelets (5-7 days before, bridged with heparin if needed), metformin, insulin (dose adjusted with sugar monitoring), oral contraceptives (4 weeks before major surgery)__; steroid cover for a patient on long-term steroids.",
        "__Final check-list before transfer__ — identity band, consent form signed, correct site marked, allergies noted, investigation reports and cross-matched blood available, vital signs recorded, fasting confirmed, bladder emptied, prostheses removed, pre-medication given and recorded, case notes and X-rays with the patient, and a completed __WHO Surgical Safety Checklist ('Sign in')__.",
        "Transfer on a trolley with side rails up, covered warmly, accompanied by the nurse and the notes; hand over verbally to the theatre nurse and sign the transfer record."
    ])
    b.box("hy", [
        "__The WHO Surgical Safety Checklist__ has three parts: __'Sign In' (before anaesthesia), 'Time Out' (before the skin incision — the whole team stops and confirms the patient, site and procedure), and 'Sign Out' (before the patient leaves the theatre — instrument, sponge and needle counts, specimen labelling, equipment problems).__ It is designed to prevent __wrong patient, wrong site and wrong procedure surgery, and retained instruments__.",
    ])

    b.section_h("18.5", "The Operation Theatre and the Immediate Peri-operative Period")
    b.bullets([
        "__Zones of the theatre__ — ~outer/protective zone~ (reception, changing rooms, offices), ~clean zone~ (pre-anaesthetic room, recovery, scrub area, CSSD interface), ~aseptic/sterile zone~ (operating room) and ~disposal/dirty zone~. Traffic and clothing rules are stricter as one moves inwards.",
        "Theatre environment — __positive pressure, laminar air flow with HEPA filtration, 15-25 air changes/hour, temperature 20-24 °C, humidity 50-60%__, seamless washable floors and walls, shadowless light, no fans, minimum staff and minimum door opening.",
        "__Theatre team__ — surgeon, assistant, anaesthetist, __scrub nurse (sterile — handles instruments, counts sponges and needles)__, __circulating nurse (unsterile — fetches supplies, positions the patient, documents, connects equipment, counts with the scrub nurse)__, technician and attendant.",
        "__Nursing responsibilities in the theatre__ — check the patient's identity, consent and site; safe __positioning__ (protect the eyes, nerves and pressure points, pad the bony points, secure the limbs, avoid hyperextension — ~brachial plexus and common peroneal nerve injury and pressure sores are real risks~); apply the diathermy plate correctly to dry, shaved, clean skin; prevent __hypothermia__ (warm blankets, warmed fluids, forced-air warmer) and maintain sterile technique; __count and record sponges, instruments, needles and blades before, during and at the end__; label and despatch specimens correctly; record the blood loss, fluids and drugs given; complete the operation and anaesthesia records.",
        "__Types of anaesthesia__ — __general__ (unconscious: induction, maintenance, reversal; airway secured with a tube or supraglottic device), __regional__ (spinal, epidural, nerve block — the patient is awake; watch for hypotension, headache, and the level of the block; the patient must lie flat as instructed after a spinal anaesthetic), __local__ (infiltration, topical) and __sedation__. Complications of anaesthesia: aspiration, laryngospasm, hypoxia, hypotension, arrhythmia, __malignant hyperthermia (a rare emergency — dantrolene)__, awareness, nerve injury, post-dural-puncture headache, and post-operative nausea and vomiting.",
    ])

    b.section_h("18.6", "Post-operative (After) Care")
    b.sub("A. Immediate care — in the recovery room / on return to the ward")
    b.numbered([
        "Receive the patient with a full __handover__ from the anaesthetist/theatre nurse: the procedure done, the anaesthetic used, blood loss and replacement, drugs given, drains and tubes, the condition during surgery and any special instruction.",
        "__Position__ — for the unconscious patient, the __lateral or semi-prone (recovery) position with the head turned to one side and no pillow__, to maintain the airway and prevent aspiration; once awake, position as per the surgery (semi-Fowler's after abdominal or chest surgery; flat after spinal anaesthesia; head elevated after craniotomy or thyroid surgery; affected limb elevated after limb surgery).",
        "__A-B-C first__ — patency of the __airway__ (look for snoring, stridor, obstruction by the tongue or secretions; use suction and an airway; jaw thrust), __breathing__ (rate, depth, SpO2, oxygen by mask/nasal prongs), and __circulation__ (pulse, BP, colour, capillary refill, bleeding).",
        "__Monitor and record vital signs every 15 minutes until stable (then half-hourly, hourly and 4-hourly)__: temperature, pulse, respiration, BP, SpO2, level of consciousness, pain score, and pupils in neurosurgical cases.",
        "__Check the wound and dressings__ for bleeding or soakage (mark the extent and note the time), the drains (type, patency, character and amount of drainage), the IV line and infusion, the urinary catheter and the hourly output, and the nasogastric tube and aspirate.",
        "Keep the patient __warm__, keep the side rails up, __never leave an unconscious patient alone__, and keep suction and oxygen at the bedside.",
        "Assess and relieve __pain__ (scheduled analgesia, patient-controlled analgesia or epidural as ordered) and __nausea__; observe for the return of the gag, swallowing and cough reflexes before giving anything orally.",
        "Discharge from recovery only when the patient is awake and responding, with a stable airway, stable vital signs, controlled pain and no active bleeding (a scoring system such as the __Aldrete score__ is used)."
    ])
    b.sub("B. Continuing post-operative care")
    b.bullets([
        "__Respiratory__ — __deep breathing and coughing every 1-2 hours with the wound splinted, incentive spirometry, early mobilisation__, nebulisation and chest physiotherapy as ordered, adequate analgesia so that the patient can breathe deeply, oxygen as prescribed.",
        "__Circulatory__ — __leg and ankle exercises hourly, early ambulation, anti-embolism stockings and prescribed heparin prophylaxis__; observe for calf pain and swelling (DVT); change position slowly (postural hypotension).",
        "__Fluid and electrolytes__ — strict intake-output record, IV fluids as prescribed, oral fluids started when bowel sounds return and the patient is fully awake, progressing __clear fluids → full fluids → soft diet → normal diet__; report a urine output of less than 30 mL/hour.",
        "__Nutrition__ — high protein, high calorie, vitamin C rich diet for healing once oral feeding is allowed; supplements or enteral/parenteral feeding for major surgery.",
        "__Elimination__ — watch for __retention of urine__ (should void within 6-8 hours; a distended bladder, restlessness and frequent small voiding suggest retention — try privacy, a warm bedpan, the sound of running water, standing/sitting position, then catheterise if ordered); prevent constipation (fluids, fibre, mobility, prescribed laxative); note the first passage of flatus and stool (return of peristalsis).",
        "__Wound care__ — keep the dressing dry and intact, aseptic dressing change as ordered, observe for bleeding, discharge, redness, gaping and smell; care of drains, tubes and the stoma; suture removal at the proper time (Chapter 8).",
        "__Comfort, hygiene and mobility__ — mouth care, bed bath, back care and 2-hourly position change, progressive ambulation (sit up on day 0-1, stand and walk as permitted), physiotherapy.",
        "__Psychological support and health education__ — explain the progress, involve the family, prepare for discharge.",
        "__Discharge advice (write it down)__ — wound and stitch care and the date of removal, hygiene, bathing, the medicines with doses and duration, diet, activity restriction (lifting, driving, work, sexual activity), exercises, the danger signs to return for (__fever, increasing pain, bleeding, discharge, swelling, breathlessness, vomiting, no urine or stool, gaping of the wound__), the follow-up date, and whom to contact in an emergency.",
    ])

    b.section_h("18.7", "Post-operative Complications")
    b.table(
        ["Complication", "When it occurs", "Signs", "Prevention and nursing action"],
        [["__Airway obstruction / hypoxia__", "Immediate", "Snoring or stridor, in-drawing, restlessness, cyanosis, falling SpO2",
          "Lateral position, suction, jaw thrust, oral airway, oxygen; call for help"],
         ["__Haemorrhage / reactionary bleeding__", "Within 24 h (secondary after 7-14 days from infection)",
          "Soaked dressing, blood in the drain, __rising pulse with falling BP__, cold clammy pale skin, restlessness, thirst, low urine output",
          "Check the wound and drain frequently, apply pressure, raise the foot end, keep flat, oxygen, fast IV fluids, __inform the surgeon at once__, send for blood, prepare for re-exploration"],
         ["__Shock__", "Immediate to 48 h", "See Chapter 19", "Monitor vital signs, fluids, oxygen, treat the cause"],
         ["__Post-operative nausea and vomiting__", "First 24-48 h", "Nausea, retching, vomiting", "Antiemetics, avoid early oral intake, head to one side, mouth care"],
         ["__Atelectasis and chest infection/pneumonia__", "__Day 1-3 (the commonest cause of early post-operative fever)__",
          "Fever, tachypnoea, cough, reduced breath sounds, falling SpO2",
          "__Deep breathing, coughing, spirometry, early ambulation, position change, no smoking, good analgesia__, chest physiotherapy, antibiotics as ordered"],
         ["__Wound infection__", "__Day 3-7__", "Fever, throbbing pain, redness, swelling, heat, purulent discharge, raised white cell count",
          "Aseptic dressing, hand hygiene, prophylactic antibiotic, nutrition, control of blood sugar; send pus for culture; report"],
         ["__Wound dehiscence and evisceration__", "__Day 5-10__", "A sudden 'give way' feeling, serosanguineous (pink) discharge, gaping, protruding bowel",
          "Prevent by nutrition, splinting during coughing, avoiding straining and distension; if it happens — __lie the patient flat with knees bent, cover with sterile saline-soaked gauze, do not push the bowel back, keep NPO, inform the surgeon immediately__"],
         ["__Paralytic ileus__", "Day 1-3", "Abdominal distension, absent bowel sounds, no flatus, vomiting", "NPO and nasogastric decompression, correct electrolytes (especially potassium), early mobilisation, avoid excess opioids, flatus tube as ordered"],
         ["__Retention of urine__", "First 6-12 h", "No voiding in 6-8 h, suprapubic fullness and tenderness, restlessness, frequent small voids",
          "Privacy, upright position, warm bedpan, running water, ambulation; catheterise only if ordered"],
         ["__Urinary tract infection__", "Day 3-5", "Fever, burning, frequency, cloudy urine", "Early removal of the catheter, closed drainage, perineal hygiene, 2-3 L fluid"],
         ["__Deep vein thrombosis and pulmonary embolism__", "__Day 3-10__ (may be later)",
          "DVT — unilateral calf pain, swelling, warmth, tenderness; __PE — sudden dyspnoea, chest pain, tachycardia, collapse, falling SpO2 (an emergency)__",
          "__Leg exercises, early ambulation, hydration, stockings, prophylactic heparin__; if suspected — __do not massage__, keep the patient at rest, give oxygen, inform the doctor at once"],
         ["__Pressure sores, constipation, hiccups, parotitis, thrombophlebitis at the IV site__", "Any time", "As described in earlier chapters",
          "2-hourly turning, skin and mouth care, fluids and fibre, care of the IV site"],
         ["__Post-operative fever — a useful framework__", "'The 5 W's'",
          "__Wind (atelectasis/pneumonia, day 1-2) → Water (urinary infection, day 3-5) → Wound (infection, day 5-7) → Walking (DVT, day 5-10) → Wonder drugs (drug or transfusion reaction, any day)__",
          "Identify the cause; a low-grade fever in the first 24 h is usually atelectasis or the inflammatory response to surgery"]],
        caption="Table 18.2  Post-operative complications")

    b.box("recap", [
        "* Fasting: clear fluids 2 h, breast milk 4 h, light meal 6 h, heavy/fatty meal 8 h before anaesthesia.",
        "* Hair removal with a clipper immediately before surgery — never a razor the night before; bath with soap/chlorhexidine.",
        "* Consent: informed, written, voluntary, before sedation; the doctor explains, the nurse witnesses; 18 years and above; guardian for minors; emergency life-saving treatment may proceed without consent.",
        "* Remove dentures, jewellery, nail polish, contact lenses; void before theatre; prophylactic antibiotic within 60 min of the incision.",
        "* WHO checklist: Sign In, Time Out (before incision), Sign Out (counts and specimens).",
        "* Post-op: unconscious → lateral/recovery position, no pillow; vital signs every 15 min until stable; ABC first.",
        "* Report a urine output under 30 mL/h; expect voiding within 6-8 hours.",
        "* Complications by day: atelectasis 1-3, wound infection 3-7, dehiscence 5-10, DVT 3-10; secondary haemorrhage 7-14 days.",
        "* Post-op fever 5 W's: Wind, Water, Wound, Walking, Wonder drugs.",
        "* Evisceration: flat with knees bent, sterile saline gauze, do not push back, NPO, call the surgeon.",
    ])


def chapter_19(b):
    b.chapter(19, "Shock and Blood Transfusion",
              "Types and stages of shock, its management, blood groups and components, transfusion procedure and reactions")

    b.section_h("19.1", "Shock — Definition and Types")
    b.box("def", ["__Shock__ — a life-threatening state of __acute circulatory failure__ in which the tissue perfusion is inadequate to meet the metabolic needs of the cells, leading to cellular hypoxia, anaerobic metabolism, lactic acidosis, cell death and multi-organ failure. ~It is not merely low blood pressure — shock may exist with a normal BP (compensated shock).~"])
    b.table(
        ["Type of shock", "Mechanism", "Causes", "Distinguishing features"],
        [["__Hypovolaemic__ (the commonest)", "Loss of circulating volume → reduced preload",
          "__Haemorrhage__ (trauma, surgery, gastro-intestinal bleeding, post-partum haemorrhage, ruptured ectopic), __plasma loss__ (burns), __fluid loss__ (severe vomiting, diarrhoea, cholera, diabetic ketoacidosis, heat stroke, third-space loss)",
          "Cold clammy pale skin, collapsed veins, low JVP, thirst, rapid weak pulse, low BP, oliguria"],
         ["__Cardiogenic__", "Failure of the heart as a pump → reduced cardiac output",
          "__Myocardial infarction__, arrhythmia, myocarditis, valve rupture, cardiomyopathy, drug overdose (beta blocker)",
          "Cold skin with __raised JVP, crepitations/pulmonary oedema, gallop rhythm__, chest pain; ~fluids must be given with great caution~"],
         ["__Obstructive__", "Mechanical obstruction to filling or outflow",
          "__Cardiac tamponade, massive pulmonary embolism, tension pneumothorax__",
          "Raised JVP, distant heart sounds, pulsus paradoxus, tracheal shift and absent breath sounds (pneumothorax) — needs immediate decompression"],
         ["__Distributive — septic__", "Widespread vasodilatation and capillary leak from infection",
          "__Gram-negative and gram-positive sepsis__, pneumonia, urinary or biliary sepsis, meningococcaemia, post-abortal and puerperal sepsis",
          "__Warm, flushed, dry skin with a bounding pulse in the early ('warm') stage__, fever or hypothermia, confusion, high or low white count, raised lactate; later cold and clammy"],
         ["__Distributive — anaphylactic__", "Type I hypersensitivity with massive histamine release",
          "__Drugs (penicillin, NSAIDs, contrast), vaccines, insect sting, food (nuts, egg, shellfish), latex, blood products__",
          "__Sudden onset within minutes__: itching, urticaria, angioedema of the lips and tongue, hoarseness, stridor, wheeze, abdominal cramps, collapse"],
         ["__Distributive — neurogenic__", "Loss of sympathetic tone → vasodilatation",
          "__Spinal cord injury above T6__, spinal anaesthesia, severe pain, fright, brain injury",
          "__Hypotension with a warm dry skin and a paradoxically slow pulse (bradycardia)__"],
         ["__Endocrine__", "Hormone deficiency", "Addisonian crisis, myxoedema coma, thyroid storm", "Treated with the specific hormone"]],
        caption="Table 19.1  Classification of shock")

    b.section_h("19.2", "Stages and Clinical Features of Shock")
    b.table(
        ["Stage", "Features"],
        [["__1. Initial / compensated (non-progressive)__", "Cardiac output falls but compensatory mechanisms (sympathetic drive, tachycardia, vasoconstriction, renin-angiotensin) maintain the BP: __restlessness and anxiety, tachycardia, cool pale skin, slight rise in diastolic BP with a narrow pulse pressure, thirst, reduced urine output__. ~This is the stage to recognise and treat — the BP may still be normal.~"],
         ["__2. Progressive (decompensated)__", "Compensation fails: __falling systolic BP (under 90 mmHg), rapid thready pulse, cold clammy sweating skin, mottling, rapid shallow breathing, confusion or drowsiness, marked oliguria (under 30 mL/h), metabolic acidosis__"],
         ["__3. Refractory / irreversible__", "Prolonged hypoxia → cell death, __multi-organ dysfunction (acute kidney injury, ARDS, liver failure, disseminated intravascular coagulation), unresponsive hypotension despite treatment__, coma and death"]],
        caption="Table 19.2  Stages of shock")
    b.box("num", [
        "__Classes of haemorrhagic shock (adult, 70 kg with about 5 L blood volume):__",
        "* __Class I__ — loss up to 15% (750 mL): pulse under 100, BP normal, slight anxiety.",
        "* __Class II__ — 15-30% (750-1500 mL): __pulse 100-120__, BP normal but narrow pulse pressure, respiration 20-30, urine 20-30 mL/h, anxious.",
        "* __Class III__ — 30-40% (1500-2000 mL): __pulse over 120, BP falls__, respiration 30-40, urine 5-15 mL/h, confused — needs blood.",
        "* __Class IV__ — over 40% (over 2000 mL): pulse over 140 and feeble, BP very low or unrecordable, negligible urine, lethargic/unconscious — immediate transfusion and surgery.",
        "__Shock index = pulse rate ÷ systolic BP__ (normal 0.5-0.7; above 0.9-1.0 suggests significant shock).",
    ])

    b.section_h("19.3", "Management of Shock")
    b.numbered([
        "__Call for help__ and treat it as an emergency; do not leave the patient.",
        "__Airway and breathing__ — clear the airway, give __high-flow oxygen (10-15 L/min by mask with a reservoir)__, assist ventilation if needed, monitor SpO2.",
        "__Position__ — lay the patient __flat with the legs raised about 20-30 cm (passive leg raising)__, or in the shock position; ~the head-down Trendelenburg position is no longer recommended~; __sit the patient up if there is pulmonary oedema (cardiogenic shock) or severe breathlessness__; recovery position if unconscious and breathing.",
        "__Circulation__ — secure __two large-bore IV cannulae (14-16 G)__; take blood for grouping and cross-matching, haemoglobin, electrolytes, sugar, lactate and culture; give __warmed crystalloid (normal saline or Ringer lactate) 500-1000 mL rapidly (20 mL/kg in children)__ and reassess; give __blood for haemorrhagic shock__ (and control the bleeding — direct pressure, elevation, tourniquet as a last resort, surgery).",
        "__Treat the cause__ — stop the bleeding; __adrenaline IM for anaphylaxis__; antibiotics within the first hour and source control for sepsis; needle decompression for tension pneumothorax; pericardiocentesis for tamponade; reperfusion for myocardial infarction; atropine and vasopressors for neurogenic shock; hydrocortisone for adrenal crisis.",
        "__Drugs as prescribed__ — vasopressors/inotropes (noradrenaline, dopamine, dobutamine, adrenaline) through a central line with continuous monitoring; sodium bicarbonate for severe acidosis; analgesia given cautiously in small IV doses.",
        "__Monitor__ — pulse, BP, respiration, SpO2, temperature, level of consciousness and capillary refill every 5-15 minutes; ECG; __hourly urine output through a catheter (aim above 0.5 mL/kg/h)__; central venous pressure if available; blood gases and lactate.",
        "__Keep the patient warm__ (blankets, warmed fluids — ~hypothermia worsens coagulopathy~) but do not overheat or use hot water bottles (they cause vasodilatation and burns).",
        "__Nil by mouth__; nothing to drink even if the patient is thirsty (moisten the lips); insert a nasogastric tube if ordered.",
        "__Reassure__ the conscious patient, explain briefly, keep the family informed, and __record everything with times__ (fluids, drugs, output, observations)."
    ])
    b.box("caution", [
        "__In shock, do NOT:__ give anything by mouth • give alcohol • apply external heat or a hot water bag • sit the patient up (except in cardiogenic shock/pulmonary oedema) • leave the patient alone • give a large dose of intramuscular or oral analgesia (absorption is unreliable) • delay treatment waiting for investigations.",
        "__Fainting (syncope) is NOT shock__ — it is a transient reflex fall in cerebral perfusion; the patient recovers within a minute or two when laid flat with the legs raised. Shock is progressive and needs active treatment.",
    ])

    b.section_h("19.4", "Blood Groups and Compatibility")
    b.table(
        ["Blood group", "Antigen on the red cell", "Antibody in the plasma", "Can receive red cells from", "Can donate red cells to", "Frequency (India, approx.)"],
        [["__A__", "A", "Anti-B", "A, O", "A, AB", "22%"],
         ["__B__", "B", "Anti-A", "B, O", "B, AB", "33%"],
         ["__AB__", "A and B", "None", "__A, B, AB, O (universal recipient)__", "AB only", "7%"],
         ["__O__", "None", "Anti-A and anti-B", "O only", "__A, B, AB, O (universal donor)__", "37%"]],
        caption="Table 19.3  The ABO system", align_center_cols=(1, 2, 5))
    b.bullets([
        "__ABO groups__ were discovered by __Karl Landsteiner (1900, Nobel Prize 1930)__; the __Rh factor__ (D antigen) by Landsteiner and Wiener (1940).",
        "__Rh positive__ = D antigen present (about __94-95% of Indians__); __Rh negative__ = absent. An Rh-negative person must receive Rh-negative blood.",
        "__O negative__ is the __universal donor__ of packed red cells (best for emergencies); __AB positive__ is the universal recipient of red cells. For __plasma__ the reverse is true — __AB plasma is the universal donor plasma__.",
        "__Haemolytic disease of the newborn (erythroblastosis fetalis)__ — an Rh-negative mother carrying an Rh-positive fetus forms anti-D antibodies which destroy fetal red cells in a subsequent pregnancy; prevented by giving __anti-D immunoglobulin (Rh immunoglobulin) 300 micrograms IM within 72 hours__ of delivery, abortion, ectopic pregnancy, amniocentesis or antepartum bleeding (and routinely at 28 weeks).",
        "Every unit must be __grouped and cross-matched__ (compatibility testing); in a dire emergency, group-specific or O-negative blood may be given while the cross-match is completed.",
    ])

    b.section_h("19.5", "Blood Components, Storage and Indications")
    b.table(
        ["Component", "Storage and shelf life", "Volume / effect", "Indications"],
        [["__Whole blood__", "__2-6 °C (ideally 4 °C) for 35-42 days__ in CPDA-1/additive solution",
          "About 350-450 mL; raises haemoglobin by about 1 g/dL per unit",
          "Massive acute haemorrhage with hypovolaemia, exchange transfusion"],
         ["__Packed red cells (PRBC)__", "2-6 °C, 35-42 days", "About 200-300 mL; __1 unit raises Hb by about 1 g/dL or the haematocrit by 3%__",
          "__The commonest component used__ — symptomatic anaemia, Hb under 7-8 g/dL, surgical loss, thalassaemia, chronic renal disease"],
         ["__Fresh frozen plasma (FFP)__", "__−30 °C or below for 1 year__; once thawed, use within 4-6 hours (24 h at 2-6 °C)",
          "200-250 mL; supplies all clotting factors", "Multiple coagulation factor deficiency, liver disease, DIC, warfarin reversal with bleeding, massive transfusion"],
         ["__Platelet concentrate__", "__20-24 °C (room temperature) with continuous gentle agitation, for only 5 days__ (~never refrigerate~)",
          "50-70 mL per unit; raises the count by about 5000-10 000/µL",
          "Platelet count under 10 000-20 000/µL, or under 50 000 with bleeding or before surgery; dengue with bleeding; leukaemia and chemotherapy"],
         ["__Cryoprecipitate__", "−30 °C, 1 year", "10-20 mL; rich in __factor VIII, von Willebrand factor, fibrinogen and factor XIII__",
          "Haemophilia A, von Willebrand disease, hypofibrinogenaemia, DIC"],
         ["__Others__", "As labelled", "Factor VIII/IX concentrate, albumin, immunoglobulin, granulocytes",
          "Haemophilia, hypoalbuminaemia, immunodeficiency"]],
        caption="Table 19.4  Blood components")
    b.box("num", [
        "__Anticoagulant-preservative solutions__ — __CPD (citrate-phosphate-dextrose) 21 days, CPDA-1 (with adenine) 35 days, and additive solutions (SAGM) 42 days__; the citrate binds calcium to prevent clotting.",
        "Blood must be transported in a __validated cold box/blood transport box at 2-10 °C__ and must __never be kept in a domestic or ward refrigerator__; if a unit has been out of controlled storage for __more than 30 minutes__ it should not be returned to stock.",
        "__Blood donor criteria (India)__ — age __18-65 years__, weight __45-50 kg or more__, __haemoglobin at least 12.5 g/dL__, pulse and BP normal, temperature normal, no infection or risk behaviour, no major surgery or tattoo in the past 6-12 months, not pregnant or lactating, __interval between whole-blood donations: 3 months (12 weeks) for men and women__ (some guidelines: 90 days); one donation is 350 or 450 mL; the donor rests and takes fluids afterwards. __World Blood Donor Day — 14 June__ (Karl Landsteiner's birthday); __National Voluntary Blood Donation Day — 1 October__.",
        "__Mandatory screening of every unit__ — __HIV 1 and 2, hepatitis B (HBsAg), hepatitis C, syphilis (VDRL) and malaria__ (plus grouping, Rh typing and antibody screening).",
    ])

    b.section_h("19.6", "Procedure of Blood Transfusion — Nursing Responsibilities")
    b.numbered([
        "Confirm the __written order and the informed consent__; explain the procedure and the reason to the patient; record __baseline vital signs (temperature, pulse, respiration, BP) immediately before starting__ — if the patient is febrile, inform the doctor before proceeding.",
        "__Check the unit with a second qualified person at the bedside__ and match against the patient and the records: __the patient's name and hospital number, the blood group and Rh of the patient and of the unit, the unit/bag number, the cross-match report, the expiry date, and the appearance of the bag__ (~return the unit if there is any clot, discolouration, haemolysis (pink/brown plasma), gas bubbles, leakage or damage~). Both persons sign.",
        "Secure a __large-bore cannula (18-20 G in an adult)__; use a __fresh blood administration set with a 170-200 micron filter__; prime with __normal saline only__.",
        "__Never add any drug or solution to blood, and never use dextrose (haemolysis) or Ringer lactate (the calcium causes clotting) in the same line__; flush with normal saline before and after.",
        "__Start the transfusion within 30 minutes of the unit leaving the blood bank__; do not warm it routinely (use an approved blood warmer only for massive or rapid transfusion, exchange transfusion or in the presence of cold agglutinins — ~never warm blood in hot water, a microwave or on a radiator~).",
        "__Run slowly for the first 15 minutes (about 1-2 mL/min / 20 drops per minute) and stay with the patient__ — most severe reactions appear in this period; then adjust to the prescribed rate. __One unit is completed within 4 hours__ (usually 2-3 hours); discard any unit hanging for more than 4 hours.",
        "__Monitor__ vital signs before, __15 minutes after starting, then every 30-60 minutes__ during, at the end, and 1 hour after the transfusion; observe continuously for the signs of a reaction and record everything (time started, rate, unit number, volume, observations, time completed).",
        "Teach the patient and family to __report immediately__ any chills, itching, rash, back or chest pain, breathlessness, headache, giddiness or a feeling that 'something is wrong'.",
        "After completion: flush with saline, remove and dispose of the bag and set as per policy (many hospitals retain the bag for 24 hours in case of a delayed reaction), record the final vital signs, and continue to observe.",
        "__Special care__ — in cardiac, renal, elderly and paediatric patients transfuse slowly with strict intake-output monitoring (risk of overload); in children the volume is calculated (usually __10-15 mL/kg of packed cells__) and given with a pump/burette."
    ])

    b.section_h("19.7", "Transfusion Reactions")
    b.table(
        ["Reaction", "Cause", "Signs and time of onset", "Management"],
        [["__Acute haemolytic reaction__ (the most dangerous)", "__ABO incompatibility — usually a clerical/identification error__",
          "Within minutes: __fever with chills, burning along the vein, pain in the loin/back and chest, flushing, restlessness, hypotension, tachycardia, dyspnoea, bleeding from puncture sites (DIC), dark/red urine (haemoglobinuria), oliguria and renal failure__",
          "__STOP the transfusion immediately__ • keep the line open with __normal saline through a new set__ • maintain the airway and give oxygen • call the doctor • monitor vital signs and urine output • send the bag, the giving set, fresh blood samples and a urine specimen to the blood bank/laboratory • treat shock and protect the kidneys (fluids, diuretics as ordered) • complete an incident/reaction report"],
         ["__Febrile non-haemolytic reaction__ (the commonest)", "Recipient antibodies against donor white cells/cytokines",
          "Rise of temperature of __1 °C or more__ with chills and rigor, usually 30 min-2 h after starting; no haemolysis",
          "Stop or slow the transfusion and inform the doctor; give an antipyretic (paracetamol, ~not aspirin if the platelet count is low~); use leucocyte-depleted blood in future; rule out haemolysis and sepsis first"],
         ["__Allergic / urticarial reaction__", "Plasma proteins", "__Itching, urticaria (hives), flushing__ without fever, within minutes",
          "Stop temporarily, give an antihistamine as ordered; if the symptoms settle completely the transfusion may be restarted slowly (for mild urticaria only)"],
         ["__Anaphylactic reaction__", "IgA deficiency with anti-IgA, severe hypersensitivity",
          "Within seconds-minutes: __angioedema, stridor, wheeze, severe dyspnoea, hypotension, collapse__",
          "__Stop at once; adrenaline 1:1000, 0.5 mL IM; oxygen; fluids; hydrocortisone and antihistamine; airway support__"],
         ["__Transfusion-associated circulatory overload (TACO)__", "Too rapid or too large a volume, especially in the elderly, infants, and cardiac or renal patients",
          "__Dyspnoea, orthopnoea, cough with frothy sputum, raised JVP, crepitations, raised BP, headache__, within hours",
          "__Stop or slow the transfusion, sit the patient upright with the legs dependent__, give oxygen, give the prescribed diuretic (frusemide), monitor; prevent by slow transfusion and packed cells"],
         ["__TRALI (transfusion-related acute lung injury)__", "Donor antibodies against recipient leucocytes",
          "Acute hypoxia with __bilateral pulmonary infiltrates within 6 hours, but a normal JVP/no overload__",
          "Stop, give oxygen and ventilatory support; ~diuretics do not help~; report to the blood bank"],
         ["__Bacterial contamination / septic reaction__", "Contaminated unit (especially platelets stored at room temperature)",
          "__High fever with rigor, vomiting, severe hypotension and collapse soon after starting__",
          "Stop at once, take blood cultures from the patient and the bag, start broad-spectrum antibiotics and treat shock"],
         ["__Air embolism__", "Air entering the line", "Sudden dyspnoea, chest pain, cyanosis, hypotension, 'mill-wheel' murmur",
          "Clamp the line, place the patient __on the left side with the head down (Durant's position)__, give oxygen, call for help"],
         ["__Citrate toxicity / hypocalcaemia and hyperkalaemia__", "Massive or rapid transfusion (citrate binds calcium; stored cells leak potassium)",
          "Perioral and finger tingling, tremor, muscle twitching, arrhythmia, prolonged QT", "Slow the rate; calcium gluconate as prescribed; monitor ECG and electrolytes"],
         ["__Hypothermia and coagulopathy__", "Cold blood given rapidly in large volume", "Shivering, arrhythmia, bleeding", "Use a blood warmer for massive transfusion; keep the patient warm"],
         ["__Delayed reactions__", "Alloantibodies, iron overload, transmitted infection",
          "__Delayed haemolysis (5-10 days: falling Hb, mild jaundice), transfusion-transmitted infection (hepatitis B/C, HIV, syphilis, malaria, CMV), iron overload (haemosiderosis) in multiply transfused patients (thalassaemia), post-transfusion purpura, graft-versus-host disease__",
          "Screening of donors and units, leucodepletion and irradiation where indicated, iron chelation (deferasirox/desferrioxamine), follow-up testing"]],
        caption="Table 19.5  Transfusion reactions — recognise, stop, report")
    b.box("hy", [
        "__The first three actions in ANY suspected transfusion reaction:__  __(1) STOP the transfusion immediately__  __(2) keep the vein open with normal saline using a new administration set__  __(3) inform the doctor and the blood bank, and monitor the vital signs.__  Then send the bag, set, blood and urine samples for investigation and complete a reaction report.",
        "__The commonest cause of a fatal transfusion reaction is a clerical error__ — the wrong unit given to the wrong patient. Hence the __two-person bedside identity check__ is the single most important safety step.",
    ])

    b.box("recap", [
        "* Shock = inadequate tissue perfusion; types: hypovolaemic (commonest), cardiogenic, obstructive, distributive (septic, anaphylactic, neurogenic), endocrine.",
        "* Early/compensated shock: restlessness, tachycardia, cool skin, narrow pulse pressure, thirst, low urine — BP may still be normal.",
        "* Warm dry skin with hypotension = early septic (or neurogenic, with bradycardia) shock; raised JVP with crepitations = cardiogenic.",
        "* Management: oxygen, flat with legs raised, two large IV lines, crystalloid then blood, treat the cause, keep warm, NPO, hourly urine output; no external heat, no oral fluids.",
        "* Class III haemorrhage = 30-40% loss (pulse over 120 with falling BP) and needs blood.",
        "* O negative = universal donor of red cells; AB positive = universal recipient; AB plasma = universal donor plasma.",
        "* Storage: whole blood/PRBC 2-6 °C for 35-42 days; platelets 20-24 °C with agitation for 5 days; FFP −30 °C for 1 year.",
        "* Donor: 18-65 years, 45-50 kg, Hb 12.5 g/dL, every 3 months; mandatory screening for HIV, HBsAg, HCV, syphilis and malaria.",
        "* Transfusion: two-person bedside check, normal saline only, filter set, start within 30 min, slow for the first 15 min, complete within 4 hours, vital signs at 15 min then half-hourly.",
        "* Never add a drug to blood; never use dextrose or Ringer lactate in the blood line.",
        "* Any reaction: STOP → saline through a new set → inform the doctor and blood bank; ABO incompatibility is the most dangerous and is usually a clerical error; TACO → sit up and give a diuretic.",
    ])



def chapter_20(b):
    b.chapter(20, "Special Treatment",
              "Oxygen therapy, suction, CPR, tracheostomy, catheter and stoma care, dialysis, physiotherapy and other special procedures")

    b.section_h("20.1", "Oxygen Therapy")
    b.bullets([
        "__Oxygen is a drug__ — it must be prescribed with the __device, flow rate/concentration, and the target saturation__, and its effect must be recorded.",
        "__Indications__ — hypoxaemia (__SpO2 below 90-94%__), respiratory distress, pneumonia, asthma, COPD exacerbation, pulmonary oedema, heart failure, myocardial infarction, shock, severe anaemia, carbon monoxide poisoning, post-anaesthesia, and during resuscitation.",
        "__Target saturation__ — __94-98% for most patients__, but __88-92% for a patient with COPD/chronic type-II respiratory failure__ (high-flow oxygen can abolish the hypoxic drive and cause carbon dioxide narcosis).",
    ])
    b.table(
        ["Device", "Flow rate", "Approximate FiO2", "Notes"],
        [["__Nasal cannula (prongs)__", "1-6 L/min", "24-44% (about 4% per litre)", "Comfortable, the patient can eat and talk; drying above 4 L/min (humidify); check the nostrils and behind the ears for pressure"],
         ["__Simple face mask__", "5-10 L/min", "40-60%", "__Never run below 5 L/min__ (rebreathing of CO2); interferes with eating and speaking"],
         ["__Venturi (air-entrainment) mask__", "As marked on the valve (colour-coded)", "__Fixed, accurate 24, 28, 31, 35, 40, 60%__", "__The device of choice in COPD__ because the concentration is exact"],
         ["__Partial rebreathing mask__", "6-10 L/min", "60-80%", "Bag must not collapse completely on inspiration"],
         ["__Non-rebreathing mask (with reservoir)__", "__10-15 L/min__", "__60-95% (up to 100%)__", "For emergencies, trauma, shock, carbon monoxide poisoning; keep the reservoir bag inflated"],
         ["__Head box / oxygen hood / incubator__", "As ordered", "Variable", "Neonates and infants"],
         ["__High-flow nasal oxygen, CPAP, BiPAP, ventilator__", "Up to 60 L/min", "21-100%", "Severe hypoxia, type-II failure, sleep apnoea, ARDS, COVID-19; needs monitoring and skilled staff"]],
        caption="Table 20.1  Oxygen delivery devices")
    b.box("caution", [
        "__Safety with oxygen (it supports combustion — it does not burn itself but makes everything else burn fiercely):__",
        "* __NO smoking, no naked flame, no spark, no electrical appliance, no oil, grease, petroleum jelly, alcohol rub or aerosol__ near the patient or the cylinder; put up 'Oxygen in use — no smoking' signs.",
        "* Cylinders __upright, chained/secured, in a cool ventilated place__; check the contents and the flow meter; never use a faulty regulator; do not use a lubricant on the valve.",
        "* __Hazards of oxygen therapy__ — drying and crusting of the mucosa, nasal and facial pressure sores, infection from a contaminated humidifier, __oxygen toxicity__ (over 50% for over 24-48 h: substernal pain, cough, atelectasis, ARDS), __carbon dioxide narcosis in COPD__, __retinopathy of prematurity and bronchopulmonary dysplasia in newborns__, and absorption atelectasis.",
        "* Change the humidifier water (sterile water) and the tubing as per policy; give frequent mouth and nasal care; monitor SpO2 and the level of consciousness.",
    ])

    b.section_h("20.2", "Suction, Nebulisation and Chest Physiotherapy")
    b.bullets([
        "__Suction__ — to clear secretions from the mouth, pharynx, trachea or an artificial airway when the patient cannot cough effectively. __Pressure: adults 100-150 mmHg, children 95-110, infants 50-95 mmHg__. Use a __sterile catheter (not more than half the diameter of the airway)__, pre-oxygenate, insert __without suction__, apply suction __intermittently while withdrawing with a rotating movement, for not more than 10-15 seconds at a time__, allow the patient to recover for 30 seconds to 1 minute between passes, and __suction the mouth last__. Observe for hypoxia, bradycardia (vagal), arrhythmia, trauma and bleeding; record the amount and character of the secretions.",
        "__Nebulisation__ — see Chapter 11; keep the mask snug, tap the chamber, complete in 10-15 minutes, do mouth care afterwards, and clean and dry the chamber and tubing after each use.",
        "__Chest physiotherapy__ — __postural drainage__ (positioning the affected lobe uppermost for 10-20 minutes, best done __before meals or 1-2 hours after, and never immediately after food__; contraindicated in raised intracranial pressure, unstable spine, haemoptysis and severe dyspnoea), __percussion (clapping with cupped hands) and vibration__ over the affected segment during expiration (~not over the spine, breasts, kidneys or a fractured rib~), followed by __huffing and coughing__; used in bronchiectasis, cystic fibrosis, lung abscess, atelectasis and retained secretions.",
        "__Breathing exercises__ — __diaphragmatic (abdominal) breathing, pursed-lip breathing (for COPD), segmental breathing, incentive spirometry (10 breaths every hour while awake)__, blowing bubbles/a balloon for children.",
    ])

    b.section_h("20.3", "Cardiopulmonary Resuscitation (CPR) and Basic Life Support")
    b.numbered([
        "__Check for danger, then check responsiveness__ (shake and shout); if unresponsive, __shout for help/activate the emergency response__ and get the defibrillator/crash cart.",
        "__Check breathing and the carotid pulse simultaneously for not more than 10 seconds__; gasping (agonal breathing) counts as not breathing.",
        "If there is no pulse, start __chest compressions immediately (C-A-B sequence)__ on a firm flat surface: heel of the hand on the __lower half of the sternum (centre of the chest between the nipples)__, other hand on top, arms straight, shoulders over the hands; __depth 5-6 cm in an adult (about one-third of the chest depth — 5 cm in a child, 4 cm in an infant); rate 100-120 per minute__; allow __complete recoil__ and minimise interruptions (less than 10 seconds).",
        "__Compression : ventilation ratio = 30 : 2__ for adults (single or two rescuers) and for children/infants with a single rescuer; __15 : 2 for children and infants with two rescuers__; with an advanced airway, give continuous compressions with __1 breath every 6 seconds (10/min)__.",
        "Open the airway with __head tilt-chin lift__ (jaw thrust if a spinal injury is suspected); give each rescue breath over __1 second, just enough to make the chest rise__ (avoid over-ventilation); use a bag-valve-mask with oxygen as soon as available.",
        "__Attach the AED/defibrillator as soon as it arrives__ and follow its prompts; __defibrillate shockable rhythms (ventricular fibrillation and pulseless ventricular tachycardia) at once__, then resume compressions immediately for 2 minutes before rechecking. ~Asystole and pulseless electrical activity are not shockable.~",
        "__Change the compressor every 2 minutes__ (or every 5 cycles) to avoid fatigue; give __adrenaline 1 mg IV every 3-5 minutes__ and other drugs as directed; treat the reversible causes (__the 4 H's and 4 T's — Hypoxia, Hypovolaemia, Hypo/hyperkalaemia and metabolic, Hypothermia; Tension pneumothorax, Tamponade, Toxins, Thrombosis__).",
        "Continue until spontaneous circulation returns, a doctor decides to stop, or the rescuer is exhausted; after the return of circulation give __post-resuscitation care__ (airway, oxygen targeted to 94-98%, 12-lead ECG, temperature management, transfer to intensive care) and __record the whole event with times__.",
        "For an __infant__: 2 fingers (single rescuer) or the 2-thumb encircling technique (two rescuers) just below the inter-nipple line; check the __brachial__ pulse. In __drowning and in children__, hypoxia is the usual cause, so begin with 5 rescue breaths (A-B-C) as per the paediatric/drowning guideline.",
        "__Choking (foreign body obstruction)__ — if the patient can cough, encourage coughing; if the obstruction is complete in a __conscious adult/child: 5 back blows between the shoulder blades then 5 abdominal thrusts (Heimlich manoeuvre)__, repeating until relieved; for an __infant: 5 back blows with the baby prone head-down on the forearm, then 5 chest thrusts (never abdominal thrusts)__; for a pregnant or obese person use chest thrusts; if the patient becomes unconscious, start CPR."
    ])

    b.section_h("20.4", "Tracheostomy and Airway Care")
    b.bullets([
        "__Tracheostomy__ — a surgical opening in the trachea (usually between the 2nd and 3rd/4th tracheal rings) with a tube in place; done for __upper airway obstruction, prolonged ventilation, retained secretions, head and neck surgery, and to reduce dead space__.",
        "__Bedside articles that must always be ready__ — suction apparatus with catheters, __a spare tracheostomy tube of the same size and one a size smaller__, tracheal dilator and spare tapes, sterile gloves and dressing tray, normal saline, humidified oxygen, resuscitation bag, and a pair of scissors.",
        "__Care__ — strict asepsis; __suction only when needed__ (see 20.2); keep the inner tube clean (remove, clean with saline and a brush, and replace as per policy); clean the stoma with saline and apply a keyhole dressing, changing it when soiled; secure the tapes with __one finger's space__ and change them with a second person holding the tube; keep the air __humidified__ (the upper airway is bypassed); mouth care 2-4 hourly; keep the patient in the semi-Fowler's position.",
        "__Communication__ — the patient __cannot speak__ with a cuffed tube: provide a pen and paper, a picture/alphabet board, a bell and agreed signs; explain and reassure; never leave the call bell out of reach.",
        "__Emergency__ — if the tube is blocked, suction and, if necessary, remove the inner tube; __if the tube is accidentally displaced, hold the stoma open with the tracheal dilator, give oxygen, call for help and re-insert the spare tube__; watch for __bleeding, subcutaneous emphysema, infection, tube blockage, displacement, stenosis and tracheo-oesophageal fistula__.",
    ])

    b.section_h("20.5", "Care of Tubes, Drains and Stomas")
    b.table(
        ["Device", "Key nursing points"],
        [["__Nasogastric (Ryle's) tube__", "See Chapter 9 — confirm the position before each use, flush, oral and nasal hygiene, secure the tape, measure the aspirate, keep the head elevated"],
         ["__Urinary catheter__", "See Chapter 11 — closed drainage, bag below bladder level, meatal care, adequate fluids, early removal"],
         ["__Intercostal (chest) drain with underwater seal__",
          "The bottle is kept __always below the level of the chest and upright__; the tube tip must remain under water; look for __swinging of the fluid level with respiration (means it is patent) and bubbling (means an air leak)__; never lift the bottle above the chest; __never clamp a bubbling chest drain__ (risk of tension pneumothorax) except briefly to change the bottle as instructed; keep two clamps and a bottle of sterile water at the bedside for accidental disconnection (submerge the tube end in sterile water); if the tube comes out, __cover the site with an occlusive dressing sealed on three sides__ and call for help at once; measure and record the drainage; encourage deep breathing and arm exercises"],
         ["__Wound drains (Redivac, Penrose, T-tube)__", "Chapter 8 — secure, keep below the wound, measure, asepsis, report a sudden change"],
         ["__Colostomy / ileostomy__",
          "Observe the __stoma colour (should be pink/red and moist — report a dusky, black or retracted stoma)__; measure and cut the appliance to fit (about 2-3 mm larger than the stoma); protect the surrounding skin with a barrier; empty the bag when __one-third to half full__; change the appliance when there is leakage or as scheduled; note the output (ileostomy output is liquid and continuous with high sodium and fluid loss; colostomy output is more formed); teach the patient self-care, diet (chew well, avoid gas-forming, odour-producing and obstructing foods such as nuts, popcorn and raw vegetables initially, drink 2-3 L), how to recognise problems, and where to obtain supplies; provide strong psychological support (body image, odour, work and sexual concerns) and refer to a stoma nurse/support group; colostomy irrigation as taught"],
         ["__Central venous catheter / PICC__", "Strict asepsis, transparent dressing, flush as per protocol, never leave a lumen open to air, observe for infection and thrombosis, measure CVP as ordered"]],
        caption="Table 20.2  Care of tubes, drains and stomas")

    b.section_h("20.6", "Dialysis")
    b.table(
        ["Point", "__Haemodialysis__", "__Peritoneal dialysis__"],
        [["Principle", "Blood is pumped through an artificial kidney (dialyser) where diffusion, osmosis and ultrafiltration occur across a semipermeable membrane", "The patient's own __peritoneum__ acts as the semipermeable membrane; dialysate is instilled into the peritoneal cavity, dwells, and is drained"],
         ["Access", "__Arteriovenous fistula (the preferred long-term access), AV graft, or a temporary central venous catheter__", "Tenckhoff catheter in the abdominal wall"],
         ["Schedule", "3-4 hours, 2-3 times a week in a dialysis unit", "CAPD — 4-5 exchanges a day at home, or by a machine at night (APD)"],
         ["Nursing care", "__Never use the fistula arm for BP, injections, IV lines or blood sampling; check the bruit and thrill daily; no tight clothing, watch or heavy lifting on that arm__; weigh before and after (the weight difference = fluid removed); monitor BP and for cramps, hypotension, headache and disequilibrium; restrict fluid, sodium, potassium and phosphate; give drugs after dialysis if they are dialysable; check for bleeding from the puncture sites (heparin is used)",
          "__Strict asepsis at every exchange (peritonitis is the main complication — cloudy outflow, abdominal pain and fever)__; warm the dialysate to body temperature; record the inflow, dwell and outflow volumes and the fluid balance; the outflow should be clear; observe the exit site; higher protein loss so a high-protein diet is needed; watch for hyperglycaemia, constipation and hernia"],
         ["Diet", "Low protein is ~not~ required once on dialysis — 1.0-1.2 g/kg protein; restrict potassium, sodium, phosphate and fluid", "1.2-1.5 g/kg protein (loss in dialysate); more liberal potassium"]],
        caption="Table 20.3  Haemodialysis and peritoneal dialysis")

    b.section_h("20.7", "Physiotherapy, Traction and Rehabilitation Modalities")
    b.table(
        ["Modality", "Description and nursing points"],
        [["__Exercises__", "__Passive__ (done by the nurse/therapist for a paralysed or unconscious patient), __active assisted, active, active resisted, and isometric__ (muscle contracted without joint movement — used inside a cast); range-of-motion exercises 2-3 times a day to all joints; ~stop if there is pain or resistance~"],
         ["__Heat modalities__", "Infrared, short-wave diathermy, ultrasound, paraffin wax bath, hot packs — for chronic pain and stiffness; __contraindicated over a metal implant/pacemaker (diathermy), in acute inflammation, malignancy, impaired sensation and pregnancy__"],
         ["__Cold and hydrotherapy__", "Ice packs and cryotherapy for acute injury and spasticity; whirlpool bath and pool exercise for weight-relieved movement"],
         ["__Electrotherapy__", "__TENS (transcutaneous electrical nerve stimulation)__ for pain, faradic and galvanic stimulation for denervated muscle, biofeedback"],
         ["__Massage__", "Effleurage, petrissage, tapotement, friction — improves circulation and relieves spasm; __never massage over a suspected DVT, acute inflammation, infection, fracture, tumour or thrombophlebitis__"],
         ["__Traction__", "__Skin traction__ (Buck's extension, Russell, Bryant's — used in children under 2 years and under 12-14 kg, with both legs suspended and the buttocks just clear of the bed) and __skeletal traction__ (Steinmann pin, Kirschner wire, Thomas splint, halo). __Nursing care:__ the weights must __hang free and never touch the floor or the bed__ and must __never be removed or lifted without an order__; the ropes must run freely in the pulleys and not be frayed; maintain the correct line of pull and __counter-traction (never let the foot piece rest against the pulley)__; keep the patient in correct alignment; check the pin site daily for infection and give pin-site care; assess __neurovascular status (the 5 P's) at least every 4 hours__; prevent complications of immobility — pressure sores (especially at the heel and sacrum), foot drop (footboard/splint), constipation, chest infection and DVT; give a fracture bedpan; encourage exercises of the free joints and quadriceps drill"],
         ["__Walking aids and gait training__", "Chapter 15 — crutches, walker, stick; teach the correct height and gait; 'up with the good, down with the bad' on stairs"],
         ["__Occupational therapy, speech therapy, prosthetics and orthotics__", "Restore function and independence; splints to prevent contracture; artificial limb after amputation with stump care (bandaging, exercises, prevention of flexion contracture and phantom pain)"]],
        caption="Table 20.4  Physiotherapy and rehabilitation")

    b.section_h("20.8", "Other Special Treatments")
    b.table(
        ["Treatment", "Nursing points"],
        [["__ECG recording__", "Explain; the patient lies still and relaxed, not talking or moving; expose the chest, clean the skin, apply gel; __limb leads — RA red, LA yellow, LL green, RL black ('Ride Your Green Bike')__; chest leads V1-V2 at the 4th intercostal space either side of the sternum, V4 at the 5th intercostal space in the mid-clavicular line, V3 between V2 and V4, V5 and V6 in the anterior and mid-axillary line at the level of V4; label the strip with the name, date and time; report ~ST elevation, wide QRS, ventricular ectopics, VT/VF, absent P waves or bradycardia~ at once"],
         ["__Radiotherapy__", "__Do not wash off the skin markings__; wash the area gently with plain water only, pat dry, no soap, powder, deodorant, perfume, adhesive tape, hot water bag or ice on the treated area; wear loose cotton clothes; protect from sunlight; report skin breakdown; for a patient with an __internal (sealed) source__ — limit the time spent close by, keep the maximum distance, use shielding, no pregnant staff or visitors or children, do not handle a dislodged source with the hands (use forceps and a lead container), and follow the radiation safety officer's instructions"],
         ["__Chemotherapy__", "See Chapter 17; antiemetics, mouth care, monitor blood counts, neutropenic precautions, protect from infection, report fever immediately"],
         ["__Mechanical ventilation__", "Explain and reassure; check the alarms, settings and the cuff pressure; ensure humidification; suction as needed; oral care with chlorhexidine; __head of the bed 30-45° to prevent ventilator-associated pneumonia__; sedation and pain relief; DVT and stress-ulcer prophylaxis; communication board; never silence an alarm without checking the patient; keep a resuscitation bag ready"],
         ["__Defibrillation and cardiac monitoring__", "Ensure no one is touching the patient or the bed ('all clear'), the chest is dry, oxygen is moved away, and the pads/paddles are correctly placed (right of the sternum below the clavicle and the left mid-axillary line at the 5th space); resume compressions immediately after the shock"],
         ["__Phototherapy (neonatal jaundice)__", "Baby naked except for eye pads and a small nappy; lamp at the prescribed distance; turn the baby 2-hourly; monitor temperature, weight, hydration and stool; continue feeding; measure bilirubin as ordered"],
         ["__Hot/cold and other applications__", "Chapter 11"]],
        caption="Table 20.5  Miscellaneous special treatments")

    b.box("recap", [
        "* Oxygen is a prescribed drug; target SpO2 94-98% (88-92% in COPD, where a Venturi mask is preferred); non-rebreathing mask at 10-15 L/min for emergencies; simple mask never below 5 L/min.",
        "* Oxygen hazards: drying, infection, oxygen toxicity above 50%, CO2 narcosis in COPD, retinopathy of prematurity; no flame, oil or spark.",
        "* Suction: sterile catheter, 100-150 mmHg in adults, 10-15 seconds per pass, suction only on withdrawal, mouth last.",
        "* CPR: C-A-B, compressions 5-6 cm at 100-120/min, ratio 30:2 (15:2 for two-rescuer paediatric), change compressor every 2 min, adrenaline 1 mg every 3-5 min, defibrillate VF/pulseless VT only.",
        "* Choking: 5 back blows + 5 abdominal thrusts (adult/child); back blows + chest thrusts for an infant (never abdominal).",
        "* Tracheostomy: keep a spare tube and tracheal dilator at the bedside; humidify; provide a means of communication.",
        "* Chest drain: keep below the chest, upright, tip under water; swinging = patent, bubbling = air leak; never clamp a bubbling drain; if it falls out, seal on three sides.",
        "* Stoma: pink and moist is normal; empty the bag at one-third to half full.",
        "* Fistula arm: no BP, no injection, no IV, no blood sampling; check the bruit and thrill. Peritoneal dialysis: cloudy outflow = peritonitis.",
        "* Traction weights hang free and are never removed; check the neurovascular status 4-hourly.",
        "* ECG leads: RA red, LA yellow, LL green, RL black. Radiotherapy: never wash off the markings; no soap, powder or heat on the site.",
    ])



def chapter_21(b):
    b.chapter(21, "Nursing in Special Diseases",
              "Disease-wise nursing care of common medical, surgical, paediatric and emergency conditions")

    b.section_h("21.1", "Respiratory Diseases")
    b.table(
        ["Condition", "Key features", "Nursing care"],
        [["__Pneumonia__", "High fever with chills, cough with __rusty sputum__, pleuritic chest pain, rapid shallow breathing, crepitations; in children — fast breathing and chest in-drawing",
          "__Semi-Fowler's position__, oxygen as prescribed, plenty of fluids (3 L), light nourishing diet, antibiotics on time, antipyretics, chest physiotherapy and deep breathing, teach cough etiquette, mouth care, monitor temperature, respiration, SpO2 and the character of the sputum, sputum for culture, prevent cross-infection and spread"],
         ["__Bronchial asthma__", "Episodic wheeze, dry cough (often at night), chest tightness, prolonged expiration, use of accessory muscles; __a silent chest, exhaustion, cyanosis, inability to speak or a falling SpO2 indicate a life-threatening attack__",
          "Sit the patient upright leaning forward, reassure and stay with him, give __oxygen and nebulised salbutamol/ipratropium__ and steroids as prescribed, monitor peak flow and SpO2, __identify and remove the trigger__ (dust, smoke, pollen, cold air, exercise, aspirin/NSAIDs, beta blockers, stress), teach the correct __inhaler technique with a spacer, the difference between reliever and preventer, rinse the mouth after steroid inhalers__, and give a written action plan; avoid sedatives"],
         ["__COPD__", "Chronic productive cough, progressive breathlessness, barrel chest, pursed-lip breathing, cor pulmonale",
          "__Controlled oxygen (target 88-92%, Venturi mask)__, pursed-lip and diaphragmatic breathing, __stop smoking (the single most important measure)__, energy conservation, small frequent high-calorie meals, pulmonary rehabilitation, influenza and pneumococcal vaccination, inhaler technique, watch for CO2 narcosis (drowsiness, headache, flapping tremor)"],
         ["__Pulmonary tuberculosis__", "Cough over 2 weeks, evening fever, night sweats, weight loss, haemoptysis",
          "__Airborne precautions__ (well-ventilated room, N95 for staff, mask for the patient, cough hygiene, sputum in a covered container), __DOTS adherence__ (Chapter 17), high-protein high-calorie diet, side-effect education, contact screening, Ni-kshay registration, address stigma and nutritional support"],
         ["__Haemoptysis / pulmonary oedema__", "Coughing up blood / __severe breathlessness with pink frothy sputum and crepitations__",
          "Haemoptysis: sit up, reassure, ice-cold sips, save and measure the blood, nil by mouth, inform the doctor. Pulmonary oedema: __sit upright with the legs dependent, high-flow oxygen, IV frusemide, morphine, nitrates as ordered__, strict output monitoring, no oral fluids"]],
        caption="Table 21.1  Nursing in respiratory disease")

    b.section_h("21.2", "Cardiovascular Diseases")
    b.table(
        ["Condition", "Key features", "Nursing care"],
        [["__Acute myocardial infarction__", "__Severe crushing retrosternal pain lasting over 20 minutes, radiating to the left arm, jaw or back, not relieved by rest or nitrates__, with sweating, nausea, vomiting, breathlessness, anxiety and a sense of impending death; may be __silent in diabetics and the elderly__",
          "__Absolute bed rest with a cardiac chair position__; __oxygen if hypoxic__; __chew soluble aspirin 300 mg__, sublingual nitrate, and morphine/analgesia as prescribed; secure an IV line; __12-lead ECG within 10 minutes__ and continuous cardiac monitoring; prepare for thrombolysis or angioplasty; keep the defibrillator and emergency drugs ready; watch for __arrhythmia (the commonest cause of early death), heart failure, shock and cardiac arrest__; keep the patient calm and undisturbed; light diet, avoid straining (stool softener), monitor intake-output; later — graded mobilisation and cardiac rehabilitation, and education on diet, exercise, smoking cessation, weight and drug adherence"],
         ["__Congestive heart failure__", "Breathlessness, orthopnoea, paroxysmal nocturnal dyspnoea, fatigue, __pedal oedema, raised JVP, tender hepatomegaly, basal crepitations, rapid weight gain__",
          "__Fowler's/cardiac position__, rest with restricted activity, oxygen, __low-salt diet and fluid restriction__, __daily weight at the same time (a gain of 1 kg = 1 L of fluid)__, strict intake-output, small frequent meals, prevention of constipation and DVT, skin care of oedematous areas, give digoxin after __checking the pulse (hold if under 60)__, watch for digoxin toxicity (nausea, vomiting, visual halos, arrhythmia) and for hypokalaemia with diuretics, teach the patient to weigh daily and report a gain of 2 kg in 2-3 days"],
         ["__Hypertension__", "Usually symptomless ('the silent killer'); headache, giddiness, epistaxis; __hypertensive emergency — BP over 180/120 with chest pain, breathlessness, visual or neurological symptoms__",
          "Correct BP measurement technique in both arms, __low-salt DASH diet__, weight reduction, regular exercise, stop smoking and limit alcohol, stress management, __emphasise lifelong drug adherence even when feeling well__, teach home monitoring and to report side effects (dry cough with ACE inhibitors, ankle swelling, postural giddiness — rise slowly), and screen for target-organ damage"],
         ["__Rheumatic fever / rheumatic heart disease__", "Follows streptococcal sore throat; migratory polyarthritis, carditis, chorea, subcutaneous nodules, erythema marginatum (__Jones criteria__)",
          "Complete bed rest during active carditis, joint support and analgesia, __long-term penicillin prophylaxis (secondary prophylaxis)__, dental hygiene and antibiotic cover for procedures, treat sore throats promptly in the family"],
         ["__Varicose veins / DVT__", "Dilated tortuous veins, aching, pigmentation, venous ulcer / unilateral calf pain, swelling and warmth",
          "__Elevation, compression stockings, avoid prolonged standing__, exercise, skin and ulcer care. DVT — __bed rest as ordered, elevation, never massage the leg__, anticoagulants with monitoring, measure the calf circumference, watch for __pulmonary embolism (sudden dyspnoea and chest pain — an emergency)__"]],
        caption="Table 21.2  Nursing in cardiovascular disease")

    b.section_h("21.3", "Neurological Conditions")
    b.table(
        ["Condition", "Key features", "Nursing care"],
        [["__Unconscious patient (any cause)__", "No response to stimuli; assess with the GCS; causes — head injury, stroke, poisoning, hypoglycaemia, uraemia, hepatic failure, epilepsy, meningitis, hypoxia",
          "__Priorities: airway, breathing, circulation.__ __Lateral/recovery position with the head turned, suction ready, nothing by mouth__; oxygen; 2-hourly position change and pressure-area care; __eye care (pad and artificial tears to prevent corneal ulcer)__; mouth care 2-hourly; catheter or condom drainage with output charting; bowel care; nasogastric feeding; passive exercises and correct limb positioning with splints and a footboard; side rails up and never leave alone; observe and record __GCS, pupils, vital signs and limb movement__; __talk to the patient by name and explain every procedure (hearing may be intact)__; never discuss the prognosis at the bedside; involve and support the family"],
         ["__Stroke (cerebrovascular accident)__", "__Sudden__ weakness or numbness of one side, facial droop, slurred speech or aphasia, visual loss, severe headache, loss of balance; __act FAST — Face, Arm, Speech, Time__ (thrombolysis is possible within 4.5 hours)",
          "Urgent transfer for CT; maintain the airway and __nil by mouth until a swallow assessment is done (aspiration risk)__; head of the bed elevated 30°; monitor neurological status, BP and blood sugar; position the affected limbs correctly with support to prevent __contracture, shoulder subluxation and foot drop__; passive then active exercises from day 1; approach from the unaffected side and place articles there; feed on the unaffected side with thickened fluids; communicate patiently with an aphasic patient (simple questions, picture board, do not shout or complete his sentences); bladder and bowel training; early physiotherapy, speech and occupational therapy; prevent pressure sores and DVT; support the family and teach home care"],
         ["__Epilepsy / convulsion__", "Aura, then tonic-clonic movements with loss of consciousness, tongue bite, incontinence, cyanosis, followed by post-ictal confusion and sleep; __status epilepticus = a seizure over 5 minutes or repeated seizures (an emergency)__",
          "__During the fit: stay with the patient, note the time and describe the seizure, protect the head (a pillow), remove nearby objects, loosen tight clothing, turn the patient on the side, do NOT restrain, do NOT put anything (spoon, cloth, finger) in the mouth, do NOT give fluids__; after the fit — recovery position, suction, oxygen, allow him to sleep, reorient, check for injury, record everything. __Prevention:__ regular medication (never stop suddenly), adequate sleep, avoid alcohol and triggers (flashing lights, fever in children), padded side rails, avoid swimming alone, driving and climbing heights, MedicAlert identification, counselling on marriage, pregnancy and occupation; __drug points__ — phenytoin gum hypertrophy, carbamazepine rash, valproate teratogenicity"],
         ["__Meningitis / raised intracranial pressure__", "Fever with severe headache, photophobia, __neck stiffness, Kernig's and Brudzinski's signs__, vomiting, rash (meningococcal); ICP — headache, __projectile vomiting, papilloedema, falling consciousness, Cushing's reflex (rising BP with slow pulse), unequal pupils__",
          "__Quiet, darkened room__, head elevated 30° with the neck in neutral alignment, avoid straining, coughing and neck flexion, droplet precautions for meningococcal disease and chemoprophylaxis of contacts, neurological observation, seizure precautions, fluid balance, antibiotics on time, assist with lumbar puncture and position the patient flat afterwards, monitor for complications (deafness, fits, hydrocephalus)"],
         ["__Head injury__", "Loss of consciousness, vomiting, __CSF leak from the nose or ear__, battle sign, boggy swelling, amnesia",
          "Airway, cervical spine protection, oxygen, GCS and pupil chart, head elevation, __nothing packed in the ear or nose and no nasogastric tube if a base-of-skull fracture is suspected__, avoid morphine (it masks pupils), report any deterioration at once"],
         ["__Paraplegia / spinal cord injury__", "Loss of power and sensation below the level, bladder and bowel involvement",
          "__Log-rolling with the spine in a straight line__, pressure-area care, bladder (intermittent catheterisation) and bowel programme, prevention of contractures and DVT, watch for __autonomic dysreflexia__ (sudden severe hypertension with headache and flushing, usually from a blocked catheter or constipation — sit the patient up and remove the cause), physiotherapy and rehabilitation, psychological support"]],
        caption="Table 21.3  Nursing in neurological conditions")

    b.section_h("21.4", "Endocrine, Renal and Gastro-intestinal Conditions")
    b.table(
        ["Condition", "Key features", "Nursing care"],
        [["__Diabetes mellitus__", "Polyuria, polydipsia, polyphagia, weight loss, fatigue, delayed healing, recurrent infection",
          "__Diet (fixed timing and carbohydrate), exercise, drugs, monitoring and education — the 5 pillars__; teach __self-monitoring of blood glucose, insulin injection technique and site rotation, storage of insulin, sick-day rules, and above all foot care__ (Chapter 5); screen for retinopathy, nephropathy and neuropathy; never miss a meal after insulin"],
         ["__Hypoglycaemia (under 70 mg/dL) — an emergency__", "__Sudden__ sweating, tremor, palpitation, hunger, pallor, confusion, irritability, slurred speech, fits, coma",
          "__Conscious: give 15-20 g of fast-acting glucose at once__ (3-4 teaspoons of sugar or glucose in water, or 100-150 mL of juice/soft drink), recheck after 15 minutes, repeat if needed, then give a complex carbohydrate snack. __Unconscious: nothing by mouth — give IV 25% dextrose (or glucagon IM)__ and inform the doctor; find and correct the cause (missed meal, excess insulin, unusual exercise, alcohol)"],
         ["__Diabetic ketoacidosis / hyperglycaemia__", "Gradual onset: polyuria, thirst, vomiting, abdominal pain, __Kussmaul breathing with an acetone smell__, dehydration, drowsiness, high sugar with ketones",
          "IV fluids (normal saline), __insulin infusion__, potassium replacement with monitoring, hourly sugar and output, watch the level of consciousness and the ECG, treat the precipitating infection, strict records"],
         ["__Thyroid disorders__", "__Hyperthyroidism__ — weight loss with good appetite, tremor, palpitation, heat intolerance, sweating, goitre, exophthalmos, diarrhoea. __Hypothyroidism__ — weight gain, cold intolerance, constipation, dry skin, hoarse voice, bradycardia, puffy face, slow thinking",
          "Hyper: cool quiet room, high-calorie high-protein diet, no tea/coffee, eye care for proptosis, monitor pulse and weight, watch for __thyroid storm__; after thyroidectomy — semi-Fowler's position, watch for __bleeding, respiratory obstruction, hoarseness (recurrent laryngeal nerve) and tetany (parathyroid injury — keep calcium gluconate ready)__. Hypo: warmth, high-fibre diet, gradual lifelong thyroxine on an empty stomach, monitor pulse and weight"],
         ["__Chronic kidney disease / acute kidney injury__", "Oliguria, oedema, hypertension, nausea, itching, sallow skin, uraemic breath, anaemia, fits in advanced uraemia",
          "__Strict intake-output and daily weight__; fluid, sodium, potassium, phosphate and protein restriction as ordered (Chapter 9); skin care for pruritus (no soap, emollients, short nails); oral care; watch for __hyperkalaemia (arrhythmia) and fluid overload__; check the drug doses (many need adjustment) and avoid nephrotoxic drugs (NSAIDs, aminoglycosides, contrast); care of the dialysis access; anaemia and calcium management; psychological support and diet counselling"],
         ["__Urinary tract infection / renal stone__", "Burning micturition, frequency, urgency, suprapubic or loin pain, fever; stone — severe colicky loin-to-groin pain with haematuria and vomiting",
          "__Plenty of fluids (3 L/day)__, complete the antibiotic course, perineal hygiene (front to back), void after intercourse, do not hold urine, warm applications and analgesia for colic, __strain all urine for the stone__, measure output, diet advice as per the stone type, and encourage follow-up"],
         ["__Peptic ulcer / gastritis__", "Epigastric burning pain related to meals, nausea, heartburn; complications — haematemesis, melaena, perforation (sudden severe pain with a rigid abdomen)",
          "Small frequent bland meals, avoid chilli, spices, coffee, alcohol, smoking and NSAIDs, complete the anti-~H. pylori~ regimen, teach the danger signs; for bleeding — nil by mouth, IV line, monitor vital signs and stool, save the vomitus"],
         ["__Viral hepatitis / cirrhosis with ascites__", "Jaundice, anorexia, nausea, dark urine, tender liver / distended abdomen, spider naevi, oedema, bleeding tendency, drowsiness (encephalopathy)",
          "Rest, __high-carbohydrate low-fat diet, absolutely no alcohol__, standard precautions with blood and body fluids, skin care for pruritus, measure the abdominal girth and weight daily, low salt and fluid restriction for ascites, __watch for bleeding and for encephalopathy (flapping tremor, confusion — restrict protein, give lactulose, prevent constipation)__, avoid sedatives and hepatotoxic drugs, assist with paracentesis"],
         ["__Acute diarrhoea and cholera__", "Frequent loose stools, vomiting, cramps, dehydration", "__ORS and zinc, continue feeding/breast feeding__ (Chapter 13), IV Ringer lactate for severe dehydration, strict intake-output and weight, perineal care, enteric precautions and disinfection of excreta, hand hygiene teaching, notify as required"]],
        caption="Table 21.4  Nursing in endocrine, renal and gastro-intestinal disease")

    b.section_h("21.5", "Surgical, Orthopaedic and Emergency Conditions")
    b.table(
        ["Condition", "Key features", "First aid and nursing care"],
        [["__Burns__", "Classified by depth (superficial/epidermal, superficial and deep partial-thickness, full-thickness) and by extent — __'rule of nines' in adults__ (head 9%, each arm 9%, each leg 18%, front of trunk 18%, back 18%, perineum 1%; the __palm of the patient's hand = about 1%__); in children use the Lund-Browder chart",
          "__First aid: stop the burning, remove the person from danger, cool the burn with clean running water for 20 minutes (not ice), remove rings, watches and burnt non-adherent clothing, cover with a clean dry non-fluffy cloth or cling film__; ~never apply toothpaste, ink, oil, butter, mud, kerosene, or burst blisters~. __Hospital care:__ airway assessment (suspect inhalation injury with facial burns, singed nostril hair, soot or hoarseness), __IV fluid resuscitation by the Parkland formula — 4 mL x body weight (kg) x %TBSA of Ringer lactate in 24 hours, half in the first 8 hours from the time of the burn__, urinary catheter with hourly output (aim 0.5-1 mL/kg/h), strict asepsis and barrier nursing, analgesia before dressings, __tetanus prophylaxis__, __high-protein high-calorie diet (up to 3000-5000 kcal)__, nasogastric feeding if needed, positioning and splinting to prevent contracture, early physiotherapy, watch for __hypovolaemic shock (first 48 h), infection/sepsis, Curling's ulcer, acute kidney injury and compartment syndrome__, and give strong psychological support for disfigurement"],
         ["__Fracture__", "Pain, tenderness, swelling, deformity, loss of function, abnormal mobility and crepitus; open (compound) fracture has a wound",
          "__First aid: do not move the part unnecessarily, control bleeding, cover an open wound with a sterile dressing, immobilise the joint above and below with a padded splint in the position found, elevate, apply cold, check the distal pulse and sensation, and transport carefully__. Ward care: traction or cast care (Chapters 12, 20), __neurovascular checks (the 5 P's) 2-4 hourly__, elevation, analgesia, exercises of free joints and isometric exercises, prevention of the complications of immobility, high-protein calcium-rich diet, watch for __compartment syndrome, fat embolism (dyspnoea, confusion, petechiae 24-72 h after a long-bone fracture), DVT, infection/osteomyelitis, delayed or non-union and avascular necrosis__"],
         ["__Haemorrhage and wounds__", "Arterial (bright red spurting), venous (dark, steady flow), capillary (oozing); internal bleeding shows as shock without visible blood",
          "__Direct pressure over the wound with a clean pad, elevation of the part, rest, pressure bandage, tourniquet only for a life-threatening limb bleed (note the time)__; treat for shock, nil by mouth, IV line, group and cross-match, monitor vital signs; nose bleed — sit up leaning forward, pinch the soft part of the nose for 10-15 minutes, cold compress, do not tilt the head back"],
         ["__Poisoning__", "Depends on the agent; note the container, tablets, smell and vomitus",
          "__Remove the person from the source, maintain the airway (lateral position), keep the vomitus and container for identification, do NOT induce vomiting__ (never in corrosive, kerosene/petroleum or unconscious patients), gastric lavage only on the doctor's order within an hour with airway protection; specific antidotes (Chapter 10); for __organophosphate (pesticide) poisoning__ — remove contaminated clothes, wash the skin, atropine and pralidoxime, watch secretions; for snake bite — reassure, immobilise the limb below heart level, __do not cut, suck, apply a tourniquet or ice__, transport urgently for antivenom"],
         ["__Heat stroke and hypothermia__", "Heat stroke: temperature above 40 °C, __hot dry skin, confusion or coma__. Hypothermia: below 35 °C, shivering (may be absent), confusion, bradycardia",
          "Heat stroke — move to a cool place, remove clothes, __rapid cooling with tepid sponging and fans, ice packs to the axillae and groins__, IV fluids, monitor continuously. Hypothermia — gradual passive rewarming with blankets, warm drinks if conscious, warmed IV fluids, handle gently (risk of arrhythmia)"],
         ["__Cancer (any site)__", "Warning signs — __the 'CAUTION' list: Change in bowel or bladder habit, A sore that does not heal, Unusual bleeding or discharge, Thickening or lump, Indigestion or difficulty in swallowing, Obvious change in a wart or mole, Nagging cough or hoarseness__",
          "Pain relief (WHO ladder), nutrition, mouth care, care during chemotherapy and radiotherapy (Chapters 17, 20), prevention of infection, stoma and wound care, honest communication, body-image and psychological support, palliative and terminal care, family support, and screening/early detection education (self breast examination, Pap smear, oral examination, tobacco cessation)"],
         ["__HIV/AIDS__", "See Chapter 14", "__Standard precautions for all patients (not special isolation)__, strict __confidentiality and no discrimination__, ART adherence counselling, nutrition, prevention and early treatment of opportunistic infections, skin and mouth care, safe sex and needle education, PPTCT, family and community counselling, and support for the care-giver"],
         ["__Anaemia / thalassaemia__", "Pallor, fatigue, breathlessness on exertion, palpitation, koilonychia, glossitis",
          "Iron/folate therapy with teaching (take with vitamin C, not with tea, milk or antacids; black stools are normal), iron-rich diet, rest with graded activity, transfusion care and __iron chelation in thalassaemia__, deworming, education on menstrual and dietary causes, and antenatal supplementation"],
         ["__Arthritis (rheumatoid and osteoarthritis)__", "Joint pain and stiffness; RA — symmetrical small joints with morning stiffness over 30 min; OA — weight-bearing joints, pain on use",
          "Rest during the acute phase with splints in a functional position, __heat or cold application__, gentle range-of-motion and isometric exercises, joint protection and energy conservation, weight reduction, assistive devices, correct posture, analgesics/NSAIDs after food (watch for gastric bleeding), teach about methotrexate being __weekly__, and maintain independence in daily activities"]],
        caption="Table 21.5  Nursing in surgical, orthopaedic and emergency conditions")

    b.section_h("21.6", "Paediatric Nursing Highlights")
    b.table(
        ["Topic", "Points"],
        [["__Normal newborn__", "Weight __2.5-3.5 kg__ (low birth weight under 2.5 kg), length 50 cm, head circumference 33-35 cm; pulse __120-160/min__, respiration __30-60/min__, temperature 36.5-37.5 °C; loses up to 10% of birth weight in the first week and regains it by 10-14 days; __doubles the birth weight by 5 months, triples it by 1 year__; passes meconium within 24 h and urine within 48 h"],
         ["__Developmental milestones__", "__Social smile 2 months • holds head steady/neck control 3 months • rolls over 5 months • sits without support 6-8 months • crawls 9 months • stands with support 9-10 months • walks alone 12-15 months • says 'mama/dada' 9-12 months • 2-3 word sentences 2 years • dry by day 2-3 years__"],
         ["__Breast feeding__", "__Exclusive breast feeding for the first 6 months__ (no water, honey, or 'ghutti'); initiate __within 1 hour of a normal birth (colostrum is the first immunisation)__; feed on demand, 8-12 times a day; correct positioning and attachment (chin touching the breast, mouth wide open, lower lip turned out, more areola visible above than below); complementary feeding from __6 months__ with continued breast feeding up to 2 years; advantages — perfect nutrition, antibodies (IgA), bonding, cheap, prevents infection and allergy, contraceptive effect for the mother, reduces breast and ovarian cancer"],
         ["__Diarrhoea in children__", "ORS + __zinc for 14 days__ + continued feeding (Chapter 13); assess dehydration by the WHO chart; do not give antidiarrhoeals or antibiotics routinely"],
         ["__Pneumonia in children__", "__Fast breathing__ by age cut-off and __chest in-drawing__ (Chapter 6); refer urgently if there is in-drawing, inability to drink, convulsions, lethargy or stridor at rest; oral amoxicillin for non-severe pneumonia"],
         ["__Malnutrition__", "__Severe acute malnutrition: weight-for-height below −3 SD, MUAC under 11.5 cm (6-59 months), or bilateral pitting oedema__; treat at a Nutrition Rehabilitation Centre with F-75/F-100 therapeutic feeds, correction of hypoglycaemia, hypothermia, dehydration and infection, micronutrients, and catch-up growth with follow-up; growth monitoring with the __Mother and Child Protection card__"],
         ["__Care of the low birth weight/preterm baby__", "__Warmth (kangaroo mother care, skin-to-skin), exclusive breast milk (expressed if needed by spoon/paladai/tube), infection prevention (hand washing), monitoring of weight, temperature and feeding, and early recognition of danger signs__; watch for hypothermia, hypoglycaemia, jaundice, apnoea and infection"],
         ["__Danger signs in a newborn/child (refer urgently)__", "Not feeding well or unable to drink or breast feed, lethargy or unconsciousness, convulsions, fast or difficult breathing with in-drawing or grunting, __hypothermia or fever__, persistent vomiting, umbilical redness or discharge with skin pustules, yellow palms and soles (jaundice), bulging fontanelle, blood in the stool"],
         ["__Hospitalised child__", "Allow a parent to stay (prevent separation anxiety), explain in age-appropriate language, use play therapy, never threaten with an injection, allow choices, maintain the routine and schooling, minimise painful procedures and use topical anaesthesia, correct drug dose by weight, safety (cot sides, no small objects), and involve the mother in care"]],
        caption="Table 21.6  Paediatric nursing highlights")

    b.box("recap", [
        "* Pneumonia: rusty sputum, semi-Fowler's, fluids, oxygen; asthma: sit up, nebulise salbutamol, no sedatives, teach inhaler with spacer; COPD: target SpO2 88-92%.",
        "* MI: chew aspirin 300 mg, ECG within 10 min, absolute rest, monitor for arrhythmia (commonest early cause of death).",
        "* Heart failure: daily weight (1 kg = 1 L fluid), low salt, check pulse before digoxin (hold if under 60).",
        "* Stroke: act FAST, thrombolysis within 4.5 h, nil by mouth until swallow assessed, approach from the unaffected side.",
        "* Seizure: never restrain, never put anything in the mouth, time the fit, side position afterwards.",
        "* Unconscious: lateral position, eye care, mouth care 2-hourly, 2-hourly turning, talk to the patient.",
        "* Hypoglycaemia (under 70): conscious — 15-20 g glucose orally; unconscious — IV 25% dextrose.",
        "* Burns: cool with running water for 20 min, cover; Parkland formula 4 mL x kg x %TBSA of Ringer lactate in 24 h, half in the first 8 h; rule of nines; palm = 1%.",
        "* Fracture: splint the joints above and below in the position found; neurovascular checks; watch for compartment syndrome and fat embolism.",
        "* Poisoning: airway, keep the container/vomitus, never induce vomiting in corrosive/kerosene/unconscious cases; snake bite — immobilise, no tourniquet or cutting.",
        "* Newborn: 2.5-3.5 kg, pulse 120-160, respiration 30-60; exclusive breast feeding for 6 months, initiate within 1 hour; social smile 2 months, sits 6-8 months, walks 12-15 months.",
    ])
