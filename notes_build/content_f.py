"""Chapters 22-24 : The Hospital Services, Preparation for Special Treatment,
Child Birth and Its Management.  Plus the rapid-revision appendix."""


def chapter_22(b):
    b.chapter(22, "The Hospital Services",
              "Types and organisation of hospitals, departments, pharmacy services, committees and the health-care delivery system of India")

    b.section_h("22.1", "The Hospital — Definition and Functions")
    b.box("def", ["__Hospital__ (WHO) — 'an integral part of the social and medical organisation, the function of which is to provide for the population complete health care, both curative and preventive, and whose out-patient services reach out to the family in its home environment; the hospital is also a centre for the training of health workers and for bio-social research.'"])
    b.sub("Functions of a hospital")
    b.bullets([
        "__Curative__ — diagnosis and treatment of the sick (out-patient, in-patient, emergency, intensive and surgical care).",
        "__Preventive and promotive__ — immunisation, antenatal and child care, family planning, health education, screening, infection control, nutrition and rehabilitation services.",
        "__Training and education__ — of doctors, nurses, pharmacists, technicians and other health workers, and of the community.",
        "__Research__ — clinical, epidemiological and operational research; clinical trials.",
        "__Rehabilitation and referral__ — physiotherapy, occupational therapy, prosthetics, and referral linkage with peripheral institutions.",
    ])

    b.section_h("22.2", "Classification of Hospitals")
    b.table(
        ["Basis", "Types"],
        [["__Ownership / control__", "__Government__ (central, state, local body, railway, ESI, defence, public sector); __private__ (for profit, corporate, nursing home); __voluntary/charitable/mission trust__; __autonomous__ (AIIMS, PGI)"],
         ["__System of medicine__", "Allopathic; __AYUSH__ — Ayurveda, Yoga and Naturopathy, Unani, Siddha, Homoeopathy"],
         ["__Clinical scope__", "__General__ (all common specialities); __Specialised/special__ (paediatric, maternity, cancer, TB, mental, eye, ENT, infectious disease, orthopaedic); __Teaching__; __Isolation__"],
         ["__Size (number of beds)__", "__Small under 100 beds • Medium 100-300 • Large 300-500 • Very large/tertiary over 500 beds__"],
         ["__Level of care__", "__Primary__ (first contact — sub-centre, PHC, dispensary); __Secondary__ (referral, basic specialities — CHC, sub-district and district hospital); __Tertiary__ (super-speciality, teaching, research — medical college and regional institutes)"],
         ["__Length of stay / purpose__", "Short-stay and acute care; long-stay and chronic care; day-care/ambulatory surgery; hospice"]],
        caption="Table 22.1  Classification of hospitals")
    b.box("num", [
        "Recommended bed strength: about __1 bed per 1000 population__ (WHO indicative norm); __85% bed occupancy__ is considered efficient.",
        "__Bed distribution norm (approximate)__ — medicine 25-30%, surgery 20-25%, obstetrics and gynaecology 15-20%, paediatrics 10-15%, with the rest for other specialities; __ICU beds about 5-10%__ of total beds.",
        "Space norms: __7-10 sq m (about 80-100 sq ft) of floor space per bed in a general ward__ with a __2.25 m (7 ft) centre-to-centre distance between beds__ and 1.2-2.4 m of circulation space; about __100-150 sq ft per bed__ including ancillary areas.",
    ])

    b.section_h("22.3", "Organisation and Departments of a Hospital")
    b.table(
        ["Group", "Departments / services"],
        [["__Clinical (patient care) services__", "__Out-patient department (OPD)__ — the 'shop window' of the hospital, with registration, consultation rooms, injection room, dressing room, minor OT, sample collection and a pharmacy counter; __In-patient (wards)__ — general, private, ICU/CCU/NICU/PICU, isolation, burns, post-operative; __Emergency/casualty__ — 24 hours, with triage (__red = immediate, yellow = urgent, green = non-urgent/walking, black = dead or expectant__), resuscitation bay, observation beds, ambulance bay and a disaster plan; __Operation theatre complex__; __Labour room and maternity__; __Speciality clinics__ (diabetes, ART, DOTS, immunisation, well-baby, family planning)"],
         ["__Diagnostic (supportive) services__", "Clinical laboratory (pathology, biochemistry, microbiology, haematology, serology, histopathology), __radiology and imaging__ (X-ray, ultrasound, CT, MRI, mammography), __blood bank__, ECG/EEG/echocardiography, pulmonary function laboratory, nuclear medicine, endoscopy"],
         ["__Therapeutic support__", "__Pharmacy__, physiotherapy and occupational therapy, dietetics/kitchen, dialysis unit, radiotherapy, speech therapy, prosthetics and orthotics"],
         ["__Nursing service__", "Headed by the Nursing Superintendent → Deputy/Assistant Nursing Superintendent → Ward Sister/Sister-in-charge → Staff Nurse → Nursing Aide; responsible for 24-hour patient care, ward management, supplies, records, staff duty rosters and training"],
         ["__Administrative services__", "Medical Superintendent/Director, hospital administrator, personnel/human resources, accounts and billing, stores and purchase, medical records department (MRD), public relations, security, transport, legal cell"],
         ["__Utility / engineering services__", "__CSSD (Central Sterile Supply Department)__, laundry, kitchen, housekeeping, maintenance (electrical, plumbing, biomedical engineering), generator and UPS, water supply and storage, oxygen manifold/plant, medical gas pipeline, air conditioning, fire fighting, waste management and mortuary"]],
        caption="Table 22.2  Hospital departments and services")
    b.bullets([
        "__CSSD__ — receives, cleans, packs, sterilises, stores and issues all sterile supplies; the flow is strictly __one-way from the dirty (receiving) zone → cleaning → packing → sterilising → sterile store → issue__, with no crossing of clean and dirty traffic; it maintains sterilisation records, indicators and recall procedures.",
        "__Medical Records Department__ — maintains, codes (__ICD__), stores and retrieves case records; supplies statistics and medico-legal documents; records are usually retained for __5-10 years (longer for medico-legal, paediatric and maternity records)__; confidentiality is paramount.",
    ])

    b.section_h("22.4", "Hospital Pharmacy Services")
    b.bullets([
        "__Functions__ — procurement, storage and inventory control of drugs; __dispensing to out-patients and in-patients__; sterile manufacturing where permitted (IV fluids, TPN, eye drops, cytotoxic reconstitution); drug distribution to wards; __drug information and patient counselling__; participation in ward rounds and in therapeutic drug monitoring; __ADR monitoring (pharmacovigilance)__; education and training; and maintaining statutory records and licences.",
        "__Drug distribution systems__ — (1) __floor/ward stock system__ (bulk supply to the ward; economical but with high wastage and error risk), (2) __individual prescription order system__ (each order dispensed separately; safer but slow), (3) __unit dose dispensing system__ (each dose separately packed and labelled for a patient for 24 hours — the __safest, least wasteful and most accurate system__, and the one that reduces medication errors most), and (4) combination/satellite pharmacy and automated dispensing cabinets.",
        "__Inventory control__ — __ABC analysis__ (A = 10% of items using 70% of the budget, needing tight control), __VED analysis__ (Vital, Essential, Desirable), EOQ (economic order quantity), lead time, buffer/safety stock, reorder level, __FEFO/FIFO__ issue, bin and stock cards, periodic physical stock verification, expiry monitoring and near-expiry redistribution, and cold-chain and narcotic records.",
        "__Hospital formulary__ — a continuously revised, authoritative list of the drugs approved for use in the hospital with essential prescribing information, prepared and maintained by the __Pharmacy and Therapeutics Committee (PTC)__ and based on the NLEM/WHO essential medicines concept; it promotes rational, economical and standardised prescribing.",
        "__Pharmacist's ward-level roles__ — reconciling medication at admission and discharge, checking prescriptions for dose, interaction, duplication and allergy, advising on dilution, compatibility and rate of IV drugs, monitoring high-alert drugs and narrow-index drugs, educating nurses and patients, and reporting errors and reactions.",
    ])

    b.section_h("22.5", "Hospital Committees")
    b.table(
        ["Committee", "Main functions"],
        [["__Pharmacy and Therapeutics Committee (PTC)__", "Develops and revises the __hospital formulary__ and drug policy; evaluates requests for new drugs; promotes rational prescribing; reviews ADRs and medication errors; plans drug-use evaluation and staff education. Chaired usually by a senior physician with the __pharmacist as secretary__"],
         ["__Hospital Infection Control Committee (HICC)__", "Surveillance of hospital-acquired infection; infection-control policies, hand-hygiene and isolation protocols; antibiotic policy and stewardship; outbreak investigation; staff health and immunisation; waste management audit; training"],
         ["__Bio-medical Waste Management Committee__", "Segregation, colour coding, storage, transport, treatment and records as per the BMW Rules, 2016; staff training and annual returns"],
         ["__Other committees__", "Hospital management/governing council, quality assurance and patient safety, transfusion (blood bank) committee, ethics committee (for research and clinical trials), medical audit and mortality review, disaster management, purchase and condemnation, grievance/patient-welfare committee, fire and safety, and death review committee"]],
        caption="Table 22.3  Important hospital committees")

    b.section_h("22.6", "Health Care Delivery System in India")
    b.table(
        ["Level / institution", "Population covered (plain / hilly-tribal)", "Staff and services"],
        [["__Village level__", "1000 / -", "__ASHA (Accredited Social Health Activist) — 1 per 1000__ population, a village woman volunteer with performance-based incentives; Anganwadi worker (__1 per 400-800__ under ICDS); trained dai; village health, sanitation and nutrition committee"],
         ["__Sub-centre / Health and Wellness Centre (the most peripheral contact point)__", "__5000 / 3000__",
          "__1 ANM/MPW (Female) + 1 MPW (Male)__ (now also a Community Health Officer under Ayushman Bharat HWC); maternal and child health, immunisation, family planning, ORS and basic drugs, referral, and health education"],
         ["__Primary Health Centre (PHC)__", "__30 000 / 20 000__ (covering about 6 sub-centres)",
          "__1 medical officer + 14-15 paramedical staff, 4-6 beds__; OPD, basic laboratory, MCH and immunisation, family welfare, national programmes, referral and supervision of sub-centres"],
         ["__Community Health Centre (CHC) / First Referral Unit__", "__1 20 000 / 80 000__ (covering 4 PHCs)",
          "__4 specialists — physician, surgeon, obstetrician-gynaecologist and paediatrician — with 21 paramedical staff and 30 beds__, operation theatre, labour room, X-ray, laboratory and blood storage; a __First Referral Unit__ must provide 24-hour emergency obstetric care, newborn care and blood storage"],
         ["__Sub-divisional / Taluka hospital__", "About 5-6 lakh", "50-100 beds with basic specialities"],
         ["__District hospital__", "Whole district (10-30 lakh)", "__200-500 beds__ (about 1 bed per 1000 population of the district); all basic and some super-specialities; the secondary-level apex of the district"],
         ["__Medical college / regional and national institutes__", "Region/state/country", "Tertiary and super-speciality care, teaching and research (AIIMS, PGIMER, NIMHANS, JIPMER, CMC)"]],
        caption="Table 22.4  Health care infrastructure in rural India")
    b.box("num", [
        "__Key ratios to remember:__ ASHA 1:1000 • Sub-centre 1:5000 (3000 hilly) • PHC 1:30 000 (20 000 hilly) • CHC 1:1 20 000 (80 000 hilly) • Anganwadi 1:400-800 • one sub-centre for every 3-5 villages, and 6 sub-centres per PHC, 4 PHCs per CHC.",
        "__Ayushman Bharat (2018)__ has two pillars: __(1) Health and Wellness Centres (HWCs)__ — 1.5 lakh sub-centres and PHCs upgraded to provide comprehensive primary health care with a __Community Health Officer__, and __(2) Pradhan Mantri Jan Arogya Yojana (PM-JAY)__ — health insurance cover of __Rs 5 lakh per family per year__ for secondary and tertiary hospitalisation for the bottom 40% of the population (and for all aged 70+).",
    ])

    b.section_h("22.7", "National Health Programmes (quick list)")
    b.table(
        ["Programme", "Focus"],
        [["__National Health Mission (NHM, 2013)__ = NRHM (2005) + NUHM (2013)", "Umbrella mission for rural and urban health; ASHA, Janani Suraksha Yojana, mobile medical units, RBSK, RKSK"],
         ["__NTEP (formerly RNTCP)__", "Tuberculosis — DOTS, Ni-kshay, TB-free India by 2025"],
         ["__NACP__", "HIV/AIDS — ICTC, ART centres, blood safety, targeted intervention"],
         ["__NVBDCP__", "Vector-borne diseases — malaria, dengue, chikungunya, filariasis, kala-azar, Japanese encephalitis"],
         ["__NLEP__", "Leprosy — MDT, disability prevention"],
         ["__NPCB&VI__", "Blindness and visual impairment — cataract surgery, school eye screening, eye banks"],
         ["__RMNCH+A / RCH__", "Reproductive, maternal, newborn, child and adolescent health; JSY, JSSK, LaQshya, SUMAN, Mission Parivar Vikas"],
         ["__UIP / Mission Indradhanush__", "Universal immunisation coverage"],
         ["__NPCDCS / NP-NCD__", "Cancer, diabetes, cardiovascular disease and stroke — screening and NCD clinics"],
         ["__NMHP / DMHP__", "Mental health; Tele-MANAS"],
         ["__NPHCE__", "Health care of the elderly"],
         ["__POSHAN Abhiyaan, ICDS, Anaemia Mukt Bharat, NIDDCP, Mid-day meal__", "Nutrition, anaemia, iodine deficiency"],
         ["__Swachh Bharat Mission, Jal Jeevan Mission__", "Sanitation and safe drinking water"],
         ["__NTCP, National Deworming Day, Pulse Polio, IDSP, PMSMA, Ayushman Bharat Digital Mission__", "Tobacco control, deworming, polio, surveillance, antenatal care, digital health"]],
        caption="Table 22.5  Major national health programmes")

    b.section_h("22.8", "Quality, Safety and Patient Rights")
    b.bullets([
        "__Accreditation__ — __NABH__ (National Accreditation Board for Hospitals and Healthcare Providers, under the Quality Council of India) for hospitals and blood banks; __NABL__ for laboratories; __JCI__ internationally; __Kayakalp__ and __LaQshya__ awards for cleanliness and labour-room quality; __IPHS (Indian Public Health Standards)__ for public facilities.",
        "__Patient safety goals__ — correct patient identification, effective communication (SBAR, read-back of verbal orders), safety of high-alert medications, correct-site surgery (WHO checklist), reduction of health-care-associated infection, reduction of the risk of falls, and reporting of incidents and near misses in a __blame-free culture__.",
        "__Patient's Charter of Rights (NHRC/Ministry of Health)__ — right to information, records and reports, second opinion, emergency care, informed consent, confidentiality and privacy (a __female attendant during examination of a female patient__), transparency in rates and choice of pharmacy/laboratory, non-discrimination, safety and quality care, protection from unnecessary procedures, and a grievance-redressal mechanism.",
        "__Hospital statistics to know__ — __bed occupancy rate__ = (occupied bed days / available bed days) × 100; __average length of stay__ = total patient days / number of discharges; __bed turnover rate__; __gross and net death rate__; __hospital infection rate__; and the maternal and perinatal mortality audit.",
    ])

    b.box("recap", [
        "* Levels of care: primary (sub-centre, PHC), secondary (CHC, district hospital), tertiary (medical college, institutes).",
        "* Norms: ASHA 1:1000, sub-centre 1:5000 (3000 hilly), PHC 1:30 000 (20 000 hilly), CHC 1:1 20 000 (80 000 hilly); CHC has 4 specialists and 30 beds; PHC 1 doctor and 4-6 beds.",
        "* Triage colours: red immediate, yellow urgent, green non-urgent, black dead/expectant.",
        "* CSSD works one-way from dirty to sterile; MRD keeps records 5-10 years and uses ICD coding.",
        "* Unit dose dispensing is the safest drug distribution system; ABC and VED analysis for inventory; FEFO for issue.",
        "* PTC prepares the hospital formulary (pharmacist = secretary); HICC controls hospital infection and antibiotic policy.",
        "* Ayushman Bharat = Health and Wellness Centres + PM-JAY (Rs 5 lakh per family per year).",
        "* NABH accredits hospitals, NABL laboratories; bed occupancy rate = occupied bed days / available bed days × 100.",
    ])


def chapter_23(b):
    b.chapter(23, "Preparation of the Patient for Special Treatment and Investigations",
              "Patient preparation, articles, positioning and after care for common diagnostic and therapeutic procedures")

    b.section_h("23.1", "General Principles of Preparing a Patient for Any Procedure")
    b.numbered([
        "__Verify the order__ and the correct patient, procedure, site and side; check that the __consent__ form is signed where required.",
        "__Explain__ the purpose, the procedure, the sensations to expect, the duration, the position to be maintained and what is expected of the patient — a well-informed patient co-operates and needs less sedation.",
        "Check for __allergies (especially to iodine, contrast media, latex and local anaesthetics), pregnancy, current medicines (anticoagulants, antiplatelets, metformin before contrast, insulin), renal function before contrast, and any implant/pacemaker/metal before MRI__.",
        "Carry out the specific __preparation__ — fasting, bowel preparation, bladder emptying or filling, skin preparation, hair removal, pre-medication, and stopping or adjusting drugs as ordered.",
        "Record __baseline vital signs and weight__; remove dentures, jewellery and metal objects as appropriate; dress the patient in a gown.",
        "Arrange the __articles/sterile tray__ and the specimen containers with labels and forms; ensure good light, privacy and a warm room.",
        "__Position__ the patient correctly and support him; maintain privacy and drape properly; stay with the patient and observe him __during__ the procedure (vital signs, colour, breathing, pain, fainting), and reassure him.",
        "__After care__ — the prescribed position and rest, observation of vital signs and of the puncture/biopsy site for bleeding, pain relief, food and fluids when allowed, prompt despatch of specimens, and __complete documentation__ (procedure, time, operator, specimen sent, amount and character of fluid removed, complications and the patient's condition).",
        "Know and watch for the __specific complications__ of each procedure and report them at once."
    ])

    b.section_h("23.2", "Blood, Urine and Other Laboratory Investigations")
    b.table(
        ["Investigation", "Preparation", "Points"],
        [["__Fasting blood sugar / lipid profile__", "__8-12 hours of fasting__ (water allowed); no food, tea, coffee or smoking; usual drugs as advised",
          "Collect early morning; for the __oral glucose tolerance test__ take a fasting sample, give 75 g of glucose in 250-300 mL water, then sample at 1 and 2 hours; the patient must sit quietly and not eat, smoke or walk about"],
         ["__Post-prandial blood sugar__", "Sample exactly __2 hours after a meal or after the glucose load__", "Note the exact time of the meal"],
         ["__HbA1c, renal and liver function, electrolytes, complete blood count__", "Usually no fasting needed", "Correct tube and order of draw (Chapter 13)"],
         ["__Blood culture__", "At the onset of fever/chill, __before antibiotics__, 2 sets from 2 sites", "Meticulous skin antisepsis"],
         ["__24-hour urine, mid-stream urine, stool, sputum__", "See Chapter 13", "Correct container, preservative and timing"],
         ["__Urea breath test / occult blood__", "Stop antibiotics and proton-pump inhibitors as advised / meat-free and iron-free diet for 3 days", "Follow the laboratory instruction sheet"]],
        caption="Table 23.1  Common laboratory investigations")

    b.section_h("23.3", "Radiological and Imaging Investigations")
    b.table(
        ["Investigation", "Preparation", "After care / notes"],
        [["__Plain X-ray (chest, bone)__", "Remove metal objects, jewellery and clothing with buttons/zips from the field; __protect the gonads and enquire about pregnancy__; the patient holds his breath as instructed",
          "No special after care; lead apron for staff and for the escort"],
         ["__Plain X-ray abdomen (KUB)__", "Bowel preparation (laxative the night before) and an empty bladder", "-"],
         ["__Barium meal / swallow (upper GI)__", "__Nil by mouth for 6-8 hours (from midnight)__; no smoking; remove dentures; explain that the barium tastes chalky",
          "__Plenty of fluids and a laxative afterwards__ to clear the barium; warn the patient that the __stools will be white/chalky for 1-3 days__; report constipation or abdominal pain (risk of impaction)"],
         ["__Barium enema (large bowel)__", "__Low-residue diet for 1-2 days, clear liquids the day before, laxative and cleansing enema until the returns are clear__; nil by mouth after midnight",
          "Barium is expelled with a cleansing enema/laxative afterwards; give fluids and rest; watch for perforation (severe pain), and never do it soon after a bowel biopsy"],
         ["__Intravenous pyelography/urography (IVP/IVU)__", "__Consent; check the creatinine and the history of iodine/contrast allergy__; laxative the night before; __nil by mouth for 6-8 hours (fluid restriction as ordered for a better picture)__; empty the bladder before",
          "__Push fluids afterwards to flush out the contrast__; observe for a __contrast reaction (itching, rash, sneezing, wheeze, hypotension — keep the emergency tray and adrenaline ready)__ and for urine output; __withhold metformin for 48 hours__ as per the local protocol"],
         ["__Ultrasound — abdomen__", "__Nil by mouth for 6-8 hours__ (no gas-forming food) for the gall bladder and abdomen", "No after care; harmless, no radiation"],
         ["__Ultrasound — pelvis (transabdominal) / obstetric__", "__Full bladder__ — the patient drinks 3-4 glasses of water 1 hour before and does __not__ void", "Allow voiding immediately afterwards"],
         ["__CT scan__", "Consent for contrast; nil by mouth 4-6 hours if contrast is used; check the creatinine and allergy; remove metal; oral contrast may be given in divided doses before the scan",
          "Push fluids if contrast was used; observe for a reaction; the patient must lie still; explain the noise and the enclosed space"],
         ["__MRI__", "__The key question: any metal?__ __Contraindicated with a cardiac pacemaker, implanted defibrillator, cochlear implant, metallic intra-ocular foreign body, or certain clips and pumps__; remove __all__ metal — jewellery, hair pins, watch, coins, credit cards, hearing aid, dentures, patches, prosthesis; warn about the __loud knocking noise (ear plugs are given)__ and the narrow tunnel (sedation for claustrophobia); the patient must lie absolutely still for 30-60 minutes",
          "No radiation; contrast (gadolinium) needs a renal check; observe after sedation"],
         ["__Mammography__", "Best done in the week after menstruation; __no talcum powder, deodorant or lotion on the breast or axilla__ on the day; warn about the compression discomfort", "Screening from 40-50 years; teach breast self-examination"],
         ["__Radio-isotope (nuclear) scan, PET, DEXA__", "As per the department's instruction; fasting for some; the isotope is given orally or IV at a set time before the scan",
          "The patient may be mildly radioactive for some hours — __push fluids, flush the toilet twice, wash hands, and avoid close contact with pregnant women and infants__ for the stated period"]],
        caption="Table 23.2  Radiological investigations")

    b.section_h("23.4", "Endoscopic Procedures")
    b.table(
        ["Procedure", "Preparation", "After care"],
        [["__Upper GI endoscopy (gastroscopy)__", "Consent; __nil by mouth 6-8 hours__; remove dentures; local anaesthetic throat spray and/or sedation; explain that he will not be able to talk during it and may gag",
          "__Nil by mouth until the gag reflex returns (1-2 hours)__ — then start with sips of water; watch for __bleeding, perforation (severe pain, fever, surgical emphysema) and aspiration__; a sore throat is common; do not allow driving after sedation"],
         ["__Colonoscopy / sigmoidoscopy__", "Consent; __clear liquid diet for 1-2 days, full bowel preparation (polyethylene glycol) the evening before, nil by mouth 6-8 hours__; sedation; left lateral position",
          "Rest; expect abdominal cramps and flatus (walking helps); resume diet when alert; report __severe pain, distension, bleeding or fever (perforation)__"],
         ["__Bronchoscopy__", "Consent; __nil by mouth 6-8 hours__; remove dentures; pre-medication (atropine, sedative) and local anaesthesia; explain the procedure and mouth breathing",
          "__Nil by mouth 2 hours or until the cough and gag reflexes return__; semi-Fowler's position; observe for haemoptysis, dyspnoea, stridor, subcutaneous emphysema and fever; save the sputum for cytology/culture; mild blood-streaked sputum after a biopsy is expected"],
         ["__Cystoscopy__", "Consent; the bladder may need to be full or empty as instructed; fasting if under general anaesthesia; lithotomy position; strict asepsis",
          "Push fluids; warn about __burning on micturition and slightly blood-tinged urine for a day or two__; a warm sitz bath and analgesia help; report retention, heavy bleeding, clots or fever"],
         ["__Laparoscopy / hysteroscopy / ERCP__", "As for surgery — consent, fasting, skin and bowel preparation, anaesthetic assessment",
          "Post-anaesthetic care; shoulder-tip pain from residual gas after laparoscopy is common and relieved by ambulation; watch for bleeding, and for pancreatitis after ERCP"]],
        caption="Table 23.3  Endoscopic procedures")

    b.section_h("23.5", "Aspirations, Punctures and Biopsies")
    b.table(
        ["Procedure", "Position and preparation", "Articles", "After care and complications"],
        [["__Lumbar puncture__ (CSF)", "Consent; empty the bladder; __lateral (side-lying) position at the edge of the bed with the back arched, knees drawn up to the chest and the chin tucked down ('fetal/knee-chest' position)__, or sitting leaning forward; the site is the __L3-L4 or L4-L5 interspace__ (below the end of the cord); local anaesthesia; the nurse supports the patient and holds the position, and helps him keep still",
          "Sterile LP set with a spinal needle and manometer, local anaesthetic, antiseptic, gloves, drape, __3 numbered sterile tubes__, dressing",
          "__Lie flat (prone or supine without a pillow) for 4-6 hours (some units 6-24 h) and push fluids__ to prevent a __post-puncture headache__ (relieved by lying flat, fluids and analgesia); observe the site for leakage, and the vital signs, neurological status and movement of the limbs; complications — headache, backache, infection/meningitis, bleeding, nerve injury and __herniation ('coning') if the intracranial pressure is raised — LP is contraindicated in raised ICP with papilloedema__; send the tubes at once"],
         ["__Pleural aspiration (thoracentesis) / intercostal drain__", "Consent; __sitting up leaning forward over a table or a chair back with the arms supported__ (or lying on the unaffected side); chest X-ray or ultrasound first; the patient must __not cough or move__ during needle insertion and must hold his breath when told",
          "Sterile thoracentesis set, 50 mL syringe, three-way tap, specimen bottles, local anaesthetic, dressing, and a drainage bottle with underwater seal if a tube is to be inserted",
          "__Not more than 1-1.5 L should be removed at one sitting__ (risk of re-expansion pulmonary oedema and hypotension); observe the respiration, pulse, BP, SpO2 and for cough, chest pain, faintness, bleeding or __subcutaneous emphysema__; chest X-ray afterwards to exclude __pneumothorax__; position on the unaffected side; record the amount, colour and character of the fluid"],
         ["__Abdominal paracentesis (ascitic tap)__", "Consent; __empty the bladder (essential — risk of bladder puncture)__; measure the abdominal girth and weight; __upright/semi-Fowler's or sitting position__; the site is usually in the left iliac fossa/mid-line below the umbilicus",
          "Sterile paracentesis set/trocar and cannula, drainage bag, measuring jar, specimen bottles, abdominal binder",
          "__Drain slowly__ (rapid removal of a large volume causes hypotension and shock; albumin cover is given for large-volume taps); measure the girth, weight, BP and pulse before, during and after; apply a sterile dressing and a binder; watch for leakage, bleeding, hypotension and peritonitis; record the volume and appearance"],
         ["__Pericardiocentesis__", "Emergency procedure for tamponade; semi-Fowler's; ECG monitoring", "Sterile set, ECG monitor, defibrillator ready", "Continuous cardiac monitoring; watch for arrhythmia and recurrence of tamponade"],
         ["__Bone marrow aspiration / trephine biopsy__", "Consent; site — __posterior superior iliac spine (or sternum in adults, tibia in infants)__; prone or lateral position; local anaesthesia with sedation in children; explain the brief but sharp suction pain",
          "Sterile marrow needle set, slides, specimen bottles", "__Pressure over the site for 5-10 minutes__ and a sterile pressure dressing; lie on the site for a while; observe for bleeding (especially if the platelets are low) and infection; analgesia"],
         ["__Liver / kidney / lung / lymph node biopsy__", "Consent; __check platelets, PT/INR and bleeding time and the blood group__; fasting 6-8 h; position — supine with the right side slightly raised for the liver (prone for the kidney); the patient __holds his breath in expiration__ for the liver biopsy as instructed",
          "Sterile biopsy set, specimen containers with fixative, dressings",
          "__Bed rest 6-24 hours; liver biopsy — lie on the RIGHT side for 2 hours (to compress the site) then supine__; monitor pulse and BP every 15-30 minutes for 2 hours then hourly; watch for __pain, bleeding/haemorrhage, shock, bile leak or peritonitis (liver), haematuria (kidney) and pneumothorax (lung)__; avoid lifting and straining for a week"],
         ["__Joint aspiration, pleural biopsy, fine-needle aspiration cytology, Pap smear, amniocentesis__", "Correct position, strict asepsis, consent and specimen labelling",
          "As appropriate", "Pap smear: not during menstruation, no douching, intercourse or vaginal medication for 48 hours before; lithotomy position. Amniocentesis: after 15 weeks, empty bladder, ultrasound guidance, anti-D for Rh-negative mothers, rest and observe for leakage, bleeding and contractions"]],
        caption="Table 23.4  Aspirations, punctures and biopsies")

    b.section_h("23.6", "Cardiac, Neurological and Functional Tests")
    b.table(
        ["Test", "Preparation and points"],
        [["__ECG__", "No special preparation; the patient relaxes, does not talk or move; skin cleaned and gel applied; correct lead placement (Chapter 20)"],
         ["__Exercise (treadmill) stress test__", "__Light meal 2-3 hours before, comfortable clothes and shoes__; withhold beta blockers/digoxin as advised; no smoking or caffeine; written consent; the emergency trolley and defibrillator must be ready; stop the test for chest pain, marked ST change, a fall in BP, arrhythmia or exhaustion"],
         ["__Echocardiography / Holter monitoring__", "No preparation; for Holter — keep a symptom diary, do not bathe or remove the electrodes"],
         ["__Cardiac catheterisation / coronary angiography__", "__Consent, nil by mouth 6-8 hours, check the creatinine and contrast allergy, shave and prepare both groins/wrist, record the peripheral pulses, and withhold metformin__; explain the flushing sensation with contrast. __After:__ __bed rest with the limb straight and immobile (4-6 hours after a femoral puncture)__, pressure dressing/compression device, __check the puncture site for bleeding or haematoma and the distal pulse, colour, warmth and sensation every 15-30 minutes__, push fluids to clear the contrast, monitor ECG and vital signs, and report bleeding, severe back pain, chest pain or a cold pulseless limb at once"],
         ["__EEG__", "__Wash the hair, no oil, gel or spray__; light meal (do not starve — hypoglycaemia alters the record); avoid tea, coffee and cola; sedatives and antiepileptics withheld only if specifically ordered; sleep deprivation may be requested; explain that it is painless and that no current passes into the body; after — wash the hair"],
         ["__Pulmonary function test / spirometry__", "No heavy meal or tight clothing; withhold the bronchodilator for 4-6 hours if a reversibility test is planned; no smoking for 24 hours; demonstrate the maximum forced blow; sitting upright with a nose clip"],
         ["__Mantoux (tuberculin) test__", "__0.1 mL of PPD (5 TU) intradermally on the flexor surface of the left forearm, raising a 6-10 mm wheal__; mark the site; __read the induration (not the redness) after 48-72 hours__; __induration of 10 mm or more is positive__ (5 mm in HIV/immunocompromised); do not scratch, rub or cover the site"],
         ["__Skin allergy testing__", "Stop antihistamines 3-7 days before; keep adrenaline ready; observe for 30 minutes"],
         ["__Dialysis, radiotherapy and chemotherapy preparation__", "See Chapters 17 and 20"]],
        caption="Table 23.5  Cardiac, neurological and functional tests")

    b.box("recap", [
        "* Always: consent, explanation, check allergies (iodine/contrast/latex), fasting, position, privacy, specimen labelling, vital signs and documentation.",
        "* Barium meal: NPO 6-8 h, laxative and fluids afterwards, white stools for 1-3 days. Barium enema: full bowel prep.",
        "* IVP/CT/angiography with contrast: check creatinine and allergy, withhold metformin, push fluids afterwards, watch for a contrast reaction.",
        "* Pelvic/obstetric ultrasound: full bladder. Abdominal ultrasound: NPO 6-8 h.",
        "* MRI: absolutely no metal; contraindicated with a pacemaker, cochlear implant or metallic eye foreign body; loud noise, lie still.",
        "* Endoscopy/bronchoscopy: NPO until the gag reflex returns; watch for bleeding and perforation.",
        "* Lumbar puncture: lateral fetal position, L3-L4/L4-L5, lie flat 4-6 h with fluids, headache is the commonest complication; contraindicated in raised ICP.",
        "* Thoracentesis: sitting leaning forward; do not remove more than 1-1.5 L; chest X-ray afterwards for pneumothorax.",
        "* Paracentesis: empty the bladder first, drain slowly, measure the girth and weight.",
        "* Liver biopsy: check clotting, hold breath in expiration, then lie on the RIGHT side for 2 hours; bed rest 6-24 h.",
        "* Angiography: bed rest with the limb straight, check the puncture site and distal pulses every 15-30 min.",
        "* Mantoux: 0.1 mL PPD intradermal, read the induration at 48-72 h; 10 mm or more is positive.",
    ])



def chapter_24(b):
    b.chapter(24, "Child Birth and Its Management",
              "Antenatal care, normal labour and delivery, care of the newborn, postnatal care, complications and family planning")

    b.section_h("24.1", "Basic Obstetric Terms")
    b.table(
        ["Term", "Meaning"],
        [["__Gravida / Para__", "Number of pregnancies (including the present one) / number of deliveries after viability. ~Primigravida~ = pregnant for the first time; ~multigravida~; ~nullipara~ = never delivered; ~grand multipara~ = 5 or more deliveries"],
         ["__Obstetric formula (GPLA)__", "Gravida, Para, Living children, Abortions"],
         ["__Antenatal / Intranatal / Postnatal (puerperium)__", "Before delivery / during labour / after delivery (__the puerperium lasts 6 weeks__)"],
         ["__Viability / Term / Preterm / Post-term__", "Viability from __28 weeks (WHO 22 weeks)__; __term = 37-42 completed weeks__ (full term 39-40+6); preterm under 37 weeks; post-term over 42 weeks"],
         ["__Abortion / Still birth / Live birth__", "Loss of pregnancy before 20-28 weeks (or fetus under 500 g) / birth of a dead fetus after viability / birth showing any sign of life"],
         ["__Lie, presentation, position, attitude, engagement__", "Relation of the fetal long axis to the uterus / the part occupying the lower pole (__cephalic/vertex is normal, about 96%__; breech, shoulder, face, brow) / relation of the denominator to the maternal pelvis / relation of the fetal parts to each other / passage of the widest diameter of the presenting part through the pelvic brim"],
         ["__Quickening / Lightening__", "First perception of fetal movement (__18-20 weeks in a primigravida, 16-18 in a multigravida__) / the sensation of relief as the head descends 2-3 weeks before term"],
         ["__Show / Liquor / Vernix / Caput / Moulding__", "Blood-stained mucus discharge at the onset of labour / amniotic fluid (about __1000 mL at term__) / the greasy coat on the newborn's skin / oedematous swelling of the scalp / overlapping of the skull bones during descent"],
         ["__Lochia__", "Vaginal discharge in the puerperium: __lochia rubra (red, days 1-4), lochia serosa (pinkish-brown, days 5-9), lochia alba (pale white, days 10-15 up to 3-6 weeks)__"],
         ["__Involution__", "Return of the uterus to the non-pregnant size: __the fundus falls about 1-1.25 cm (one finger breadth) per day — at the umbilicus immediately after delivery, midway on day 6, and not palpable per abdomen by day 12-14__; weight falls from 1000 g to 60-80 g by 6 weeks"],
         ["__Colostrum__", "The thick yellowish first milk (first 2-4 days) — rich in protein, vitamin A and __antibodies (IgA)__; the baby's 'first immunisation'"]],
        caption="Table 24.1  Obstetric terminology")

    b.section_h("24.2", "Diagnosis of Pregnancy and Calculation of the Due Date")
    b.bullets([
        "__Presumptive symptoms__ — amenorrhoea, nausea and morning sickness (6-14 weeks), frequency of micturition, breast tenderness and tingling, fatigue, quickening.",
        "__Probable signs__ — enlargement of the abdomen, __Hegar's sign__ (softening of the isthmus, 6-10 weeks), __Goodell's sign__ (softening of the cervix), __Chadwick's/Jacquemier's sign__ (bluish discolouration of the vagina), __Osiander's sign__, __Braxton Hicks contractions__, __Piskacek's sign__, and a __positive urine hCG test__.",
        "__Positive (certain) signs__ — __fetal heart sounds (audible with a stethoscope from 18-20 weeks, by Doppler from 10-12 weeks; rate 110-160/min)__, palpation of fetal parts and movements by the examiner, and __ultrasound visualisation (cardiac activity from 6-7 weeks)__.",
        "__Naegele's rule__ — __expected date of delivery (EDD) = first day of the last menstrual period + 9 calendar months + 7 days__ (or − 3 months + 7 days + 1 year); assumes a regular 28-day cycle. ~Example: LMP 10 January 2026 → EDD 17 October 2026.~",
        "__Height of the fundus__ — __12 weeks: just palpable above the symphysis • 16 weeks: midway between the symphysis and the umbilicus • 20-22 weeks: at the umbilicus • 28 weeks: 2-3 finger breadths above the umbilicus • 32 weeks: midway between the umbilicus and the xiphisternum • 36 weeks: at the level of the xiphisternum • 40 weeks: falls back to the 32-week level (as the head engages)__. After 24 weeks, the __symphysio-fundal height in cm is approximately equal to the weeks of gestation__ (± 2 cm).",
        "__Weight gain in pregnancy__ — total __10-12 kg__ (about 1 kg in the first trimester and then __350-400 g per week__); a gain of over 3 kg in a month or a sudden gain suggests fluid retention/pre-eclampsia.",
    ])

    b.section_h("24.3", "Antenatal Care")
    b.bullets([
        "__Objectives__ — to promote and maintain the health of mother and fetus, to detect and treat complications early (__'high-risk approach'__), to prepare the mother for labour, lactation and child care, to reduce maternal and perinatal mortality, and to motivate for family planning.",
        "__Schedule of visits__ — the Government of India recommends __at least 4 antenatal visits__ (1st within 12 weeks/as soon as pregnancy is suspected — registration, 2nd at 14-26 weeks, 3rd at 28-34 weeks, 4th at 36 weeks to term); the WHO 2016 model recommends __8 contacts__. Additionally a monthly visit up to 28 weeks, fortnightly to 36 weeks and weekly thereafter in the traditional schedule; __PMSMA__ provides a fixed-day assured check-up on the 9th of every month.",
        "__At each visit__ — __weight, blood pressure, pallor, oedema, urine for protein and sugar, abdominal palpation (fundal height, lie, presentation, fetal heart rate), fetal movements__, and enquiry about complaints and danger signs; counselling on diet, rest, hygiene, breast care, delivery planning and danger signs.",
        "__Investigations__ — haemoglobin, blood group and Rh, blood sugar (__oral glucose tolerance test/DIPSI for gestational diabetes__), urine routine and culture, __HIV, VDRL/syphilis and HBsAg screening__, thyroid profile, ultrasound (dating in the 1st trimester, anomaly scan at 18-20 weeks, growth scan in the 3rd trimester), and malaria/other tests as indicated.",
        "__Prophylaxis and supplements__ — __iron and folic acid: folic acid 400-500 micrograms daily from the pre-conception period through the first trimester (prevents neural tube defects); then 1 tablet of iron-folic acid (60 mg elemental iron + 500 mcg folic acid) daily for at least 180 days in pregnancy and 180 days postpartum__ (2 tablets daily if anaemic); __calcium 500 mg twice daily (total 1 g) for 180 days__ in pregnancy and 180 days after; __albendazole 400 mg once after the first trimester__; __Td (tetanus-diphtheria) 2 doses 4 weeks apart with a booster if the last dose was within 3 years__.",
        "__Advice__ — a balanced diet with __an extra 350 kcal and 15-23 g of protein daily__, plenty of fluids and fibre; 8 hours of sleep with 2 hours of rest in the day; light exercise and walking; no heavy lifting or strenuous work; bathing daily with breast and perineal hygiene; loose clothing and low-heeled footwear; __no smoking, alcohol, tobacco or self-medication__; dental care; travel avoided in late pregnancy; sexual activity is permitted except with a history of abortion, bleeding or ruptured membranes; teach breast feeding and colostrum.",
        "__Minor ailments__ — morning sickness (small dry frequent meals, avoid fatty food, get up slowly), heartburn (small meals, propped up, antacid), constipation (fibre, fluids, exercise), backache (posture, firm mattress), leg cramps (calcium, stretching), varicose veins and piles (elevation, stockings), oedema of the feet (rest with legs raised — but exclude pre-eclampsia), frequency of urine (exclude urinary infection), white discharge (hygiene; exclude infection).",
    ])
    b.box("caution", [
        "__Danger signs in pregnancy — the mother must report IMMEDIATELY:__",
        "* __Bleeding per vaginum__ at any time • __leaking of watery fluid__ • foul-smelling discharge",
        "* __Severe headache, blurred vision, spots before the eyes, epigastric pain, convulsions__ (pre-eclampsia/eclampsia) • __swelling of the face and hands__",
        "* __Reduced or absent fetal movements__ • severe abdominal pain • high fever with chills",
        "* Persistent vomiting • severe breathlessness or palpitation • burning micturition or no urine • jaundice",
        "* Labour pains before 37 weeks (preterm labour).",
    ])
    b.sub("High-risk pregnancy — identify and refer")
    b.bullets([
        "Age __under 18 or over 35__ years; height under 145 cm; weight under 45 kg; grand multipara (5 or more); short birth interval.",
        "__Anaemia (Hb under 11 g/dL; severe under 7)__, __pre-eclampsia/hypertension__, diabetes, heart disease, tuberculosis, HIV, hypothyroidism, epilepsy, jaundice, renal disease, asthma, Rh-negative mother.",
        "__Malpresentation (breech, transverse), multiple pregnancy, polyhydramnios, antepartum haemorrhage (placenta praevia, abruptio), intrauterine growth restriction, post-term, preterm labour, premature rupture of membranes__.",
        "__Bad obstetric history__ — previous caesarean section, stillbirth, neonatal death, abortion, prolonged or obstructed labour, post-partum haemorrhage, eclampsia, or a baby with a congenital anomaly.",
    ])

    b.section_h("24.4", "Labour")
    b.box("def", ["__Labour__ — the series of physiological events by which the products of conception (fetus, placenta and membranes) are expelled from the uterus through the birth canal after 28 weeks of gestation. __Normal (eutocia) labour__ is spontaneous in onset at term, with a single fetus in vertex presentation, completed vaginally without complication within 18 hours, and with no harm to mother or baby."])
    b.sub("Signs of the onset of labour")
    b.bullets([
        "__True labour pains__ — regular, rhythmic uterine contractions that __increase in frequency, duration and intensity__, felt from the back going to the front and down the thighs, __not relieved by rest or sedation__, associated with __progressive cervical dilatation and effacement__, and with a 'show'.",
        "__False labour__ — irregular, brief, unpredictable pains felt mostly in the abdomen and groin, __relieved by walking or sedation__, with __no cervical change__ (Braxton Hicks contractions).",
        "Other signs — __lightening, show (blood-stained mucus plug), and sometimes rupture of the membranes__ with a gush of clear fluid.",
    ])
    b.table(
        ["Stage", "Definition and duration", "Nursing / midwifery care"],
        [["__First stage — dilatation__", "From the onset of true labour to __full dilatation of the cervix (10 cm)__. Latent phase (0-4 cm) and active phase (4-10 cm). __Primigravida about 12 hours (6-18); multigravida about 6-8 hours__ (cervical dilatation in the active phase at least __1 cm/hour__)",
          "Admit and reassure; take the history and examine (vital signs, abdominal palpation, __fetal heart rate every 30 minutes in the active phase__, contractions every 30 minutes for 10 minutes, vaginal examination 4-hourly under strict asepsis); __start the partograph__; encourage __ambulation and an upright/left lateral position__; allow light fluids/oral intake as per protocol; encourage __voiding every 2 hours (a full bladder delays labour)__; provide breathing and relaxation techniques, back rub and continuous companionship (__birth companion__); no routine enema, no routine shaving, no fundal pressure; give analgesia as ordered; keep the delivery tray, resuscitation equipment and radiant warmer ready"],
         ["__Second stage — expulsion__", "From full dilatation to the __delivery of the baby__. __Primigravida up to 1-2 hours (2-3 with epidural); multigravida 30 minutes-1 hour__",
          "__Fetal heart rate every 5 minutes (or after every contraction)__; the mother bears down only __with__ the contractions once she has the urge; position of choice (dorsal, left lateral or squatting); clean the perineum and drape; __support the perineum and control the delivery of the head between contractions to prevent a tear__; feel for a cord round the neck; wipe the baby's face, and clear the airway only if needed; allow restitution and external rotation, then deliver the shoulders (anterior first) and the trunk; __note the exact time of birth__; __episiotomy only if indicated (not routine)__; place the baby on the mother's abdomen/chest for __skin-to-skin contact__, dry and cover the head"],
         ["__Third stage — placental__", "From the birth of the baby to the __expulsion of the placenta and membranes__. __5-15 minutes (up to 30 minutes)__",
          "__Active management of the third stage of labour (AMTSL) — (1) uterotonic within 1 minute of birth: oxytocin 10 IU IM (the drug of choice), (2) controlled cord traction with counter-pressure on the uterus (Brandt-Andrews), and (3) uterine massage after delivery of the placenta__; __delayed cord clamping (1-3 minutes)__ then cut with a sterile blade; examine the placenta and membranes for completeness and the cord for 3 vessels; measure the blood loss (__normal up to 500 mL vaginally__); inspect the perineum and repair any tear; check that the uterus is __hard and well contracted__"],
         ["__Fourth stage — immediate recovery__", "The first __1-2 hours__ after delivery — the period of greatest risk of __post-partum haemorrhage__",
          "Check __pulse, BP, uterine tone (fundal height and firmness), amount of bleeding and the pad, and the bladder every 15 minutes for the first hour__ and every 30 minutes for the second; massage the uterus if soft; encourage voiding; __initiate breast feeding within the first hour__; keep the mother and baby together, warm and observed; give fluids and food; record everything"]],
        caption="Table 24.2  The stages of labour")
    b.box("num", [
        "__Preparation for a home delivery — the '5 CLEANS' (to prevent sepsis and tetanus):__  __clean hands, clean delivery surface, clean blade (for cutting the cord), clean cord tie, and clean cord stump (nothing applied)__.",
        "__A home delivery kit (Dai kit/DDK)__ contains: soap, a new blade, sterile cord ties/clamp, clean sheet, gauze, gloves, a mucus extractor, and a plastic sheet — plus a clean warm cloth for the baby, a bowl, and a torch.",
        "__Refer for institutional delivery__: this is now the norm (__JSY/JSSK__ provide cash assistance and free delivery, drugs, diagnostics, diet, blood and transport). Home delivery should be conducted only by a trained person with a clear referral plan.",
    ])

    b.section_h("24.5", "Care of the Newborn")
    b.numbered([
        "__Immediate care — the 'warm chain' and airway__: receive the baby in a __warm, clean, dry pre-warmed towel__; __dry thoroughly (including the head) and remove the wet cloth__; keep the baby __skin-to-skin on the mother's chest__ and cover both; delay the bath for at least __24 hours (6 hours minimum)__; keep the room warm (25-28 °C) and free of draughts.",
        "__Assess breathing and cry immediately__; clear the mouth then the nose gently only if there is obstruction; __if the baby does not breathe or cry within the 'golden minute', start bag-and-mask ventilation with room air/oxygen__ (most babies need only drying and stimulation — flicking the soles and rubbing the back).",
        "__Apgar score__ at __1 and 5 minutes__ (each of 5 signs scored 0, 1 or 2 — __heart rate, respiratory effort, muscle tone, reflex irritability (grimace) and colour__; maximum 10): __7-10 normal, 4-6 moderate depression, 0-3 severe depression needing active resuscitation__.",
        "__Cord care__ — clamp/tie and cut with a sterile blade after 1-3 minutes; leave the stump __clean, dry and uncovered; apply nothing__ (no ash, oil, powder or dung); it falls off in __5-10 days__; report redness, swelling, pus or bleeding (__omphalitis__).",
        "__Eye care__ — wipe each eye with a separate sterile swab from the inner to the outer canthus; prophylactic antibiotic eye drops/ointment as per policy.",
        "__Vitamin K 1 mg intramuscularly__ (0.5 mg if under 1 kg) into the antero-lateral thigh to prevent haemorrhagic disease of the newborn.",
        "__Identification__ — two labels/name bands with the mother's name and details, applied before the baby leaves the delivery area; record the __time of birth, sex, weight, length, head circumference and any anomaly__.",
        "__Breast feeding__ — initiate __within 1 hour__ (skin-to-skin helps); give __colostrum__; exclusive breast feeding on demand; __no water, honey, ghutti, sugar water or formula__; teach correct position and attachment; expect __6-8 wet nappies a day__ once the milk is established.",
        "__Examination and observation__ — check for congenital anomalies (cleft lip and palate, imperforate anus, spina bifida, talipes, undescended testis, hip dislocation), the passage of __urine within 48 hours and meconium within 24 hours__, temperature, colour (jaundice, cyanosis, pallor), respiration (30-60/min), activity and reflexes (rooting, sucking, swallowing, grasp, Moro, stepping, Babinski).",
        "__Immunisation at birth__ — __BCG, OPV-0 and hepatitis B birth dose__ (Chapter 14); record in the immunisation card and register the birth.",
        "__Teach the mother the newborn danger signs__ (Chapter 21) and about warmth, hygiene, exclusive breast feeding, cord care, immunisation and follow-up (__home visits on days 1, 3, 7, 14, 21, 28 and 42 under HBNC__)."
    ])
    b.box("clinical", [
        "__Physiological (normal) findings in a newborn that alarm parents:__ milia, Mongolian spots, erythema toxicum, vernix, caput succedaneum, swollen breasts and a little milk secretion, __pseudo-menstruation and vaginal discharge in girls__, physiological weight loss up to 10% in the first week, and __physiological jaundice appearing after 24 hours, peaking on days 3-5 and clearing by 10-14 days__.",
        "__Abnormal — report at once:__ __jaundice within the first 24 hours__, or jaundice of the palms and soles, or persisting beyond 2 weeks; cephalhaematoma that is enlarging; no urine in 48 h or no meconium in 24 h; a single umbilical artery; and any of the newborn danger signs.",
    ])

    b.section_h("24.6", "Postnatal (Puerperal) Care")
    b.bullets([
        "__Observation__ — for the first 2 hours: pulse, BP, uterine tone, bleeding and the bladder every 15-30 minutes; then temperature, pulse, respiration and BP __4-6 hourly for 24 hours and twice daily thereafter__; watch the __fundal height (involution), the character and odour of the lochia, the perineum/stitches, the breasts and nipples, the calves, and the bladder and bowel__.",
        "__Rest, mobility and hygiene__ — __early ambulation__ (within 6-8 hours of a normal delivery) to prevent thrombosis and to help bladder and bowel function; adequate sleep and rest; daily bath; __perineal care with front-to-back cleaning and a change of pad every 4-6 hours (or sooner)__; sitz bath for perineal discomfort.",
        "__Diet__ — a normal balanced diet with __an extra 600 kcal and 19-25 g of protein__ during the first 6 months of lactation, plenty of fluids (2-3 L), iron, folic acid and calcium continued for __180 days__, and no dietary taboos.",
        "__Breast care and feeding__ — wash with plain water (no soap on the nipples), support with a well-fitting brassiere, correct attachment to prevent cracked nipples, feed on demand from both breasts, express milk if the breasts are full, and manage __engorgement (frequent feeding, warm compress before and cold after, expression) and cracked nipple (correct attachment, express a little milk over the nipple, continue feeding)__; __mastitis__ (painful red hot segment with fever) — continue feeding/expressing, warm compresses, analgesia and antibiotics; a __breast abscess__ needs drainage.",
        "__Bladder and bowel__ — encourage voiding within 6 hours (watch for retention and for urinary infection); prevent constipation with fluids, fibre and mobility.",
        "__Postnatal exercises and advice__ — deep breathing, leg and abdominal exercises, __pelvic floor (Kegel) exercises__; avoid heavy lifting for 6 weeks; resume sexual activity when comfortable (usually after 6 weeks/after the lochia stops) __with contraception__; postnatal check-up at 6 weeks; register the birth; complete the baby's immunisation.",
        "__Psychological care__ — 'postpartum blues' are common in the first week and transient; watch for __postnatal depression (persistent sadness, crying, inability to care for the baby)__ and for __puerperal psychosis (confusion, delusions, risk to self and baby — a psychiatric emergency needing admission and never leaving mother and baby unsupervised)__.",
        "__Home visits__ — the ASHA/ANM visits on __days 1, 3, 7, 14, 21, 28 and 42__ under Home-Based Newborn Care to check the mother and the baby and to reinforce teaching.",
    ])

    b.section_h("24.7", "Complications of Labour and the Puerperium")
    b.table(
        ["Complication", "Features", "Management / nursing action"],
        [["__Post-partum haemorrhage (PPH)__ — the __leading cause of maternal death in India__",
          "__Blood loss over 500 mL after vaginal delivery (over 1000 mL after caesarean) or any loss causing haemodynamic change__; __primary__ (within 24 h; causes — the __'4 T's: Tone (atonic uterus — the commonest, about 70-80%), Trauma (tear, rupture), Tissue (retained placenta), Thrombin (coagulopathy)__) and __secondary__ (after 24 h to 6 weeks — retained bits, infection)",
          "__Call for help; massage/rub up the uterus with one hand and support it bimanually; empty the bladder (catheterise); give oxytocin 10 IU IM/IV infusion (or misoprostol, methylergometrine, carboprost as ordered); two large IV lines with rapid crystalloid; oxygen; keep the patient flat and warm; group and cross-match and arrange blood; monitor pulse, BP and blood loss continuously (weigh the pads); explore for tears and retained placenta; bimanual compression, aortic compression, uterine balloon tamponade or surgery if it continues__; strict records"],
         ["__Pre-eclampsia and eclampsia__", "__Pre-eclampsia: BP 140/90 or more after 20 weeks with proteinuria__ (± headache, blurred vision, epigastric pain, oedema, hyper-reflexia). __Eclampsia: convulsions__",
          "Regular BP and urine protein checks at every visit; __a quiet, darkened room with padded side rails, nothing by mouth, airway and suction ready, lateral position during a fit, never restrain, never leave alone__; __magnesium sulphate as the drug of choice__ (monitor the __respiratory rate above 12-16/min, urine output above 30 mL/h and the patellar/knee reflex before every dose; keep calcium gluconate 10% as the antidote__); antihypertensives (labetalol, nifedipine, hydralazine); strict intake-output; prepare for delivery (the definitive treatment); continue observation for 48 hours after delivery (fits can occur postpartum)"],
         ["__Obstructed and prolonged labour__", "Labour over 18-24 hours with no progress, a Bandl's ring, a tense tender uterus, a distended bladder, maternal exhaustion and dehydration, and fetal distress",
          "__Recognise early with the partograph and refer immediately__; do not give oxytocin at a peripheral centre; IV fluids, catheterisation, monitor the fetal heart, prepare for caesarean section; watch for rupture of the uterus, fistula, sepsis and PPH"],
         ["__Antepartum haemorrhage__", "__Placenta praevia — painless, causeless, recurrent bright red bleeding with a soft uterus; abruptio placentae — painful bleeding with a tense tender uterus and fetal distress__",
          "__Never do a vaginal examination at home or without ultrasound localisation in suspected placenta praevia__; absolute bed rest, IV line, group and cross-match, monitor the mother and the fetal heart, and transfer urgently to a facility with blood and operating facilities"],
         ["__Puerperal sepsis__", "__Fever of 38 °C or more on any 2 of the first 10 days after delivery (excluding the first 24 h)__, with offensive lochia, lower abdominal pain, a subinvoluted tender uterus, and a discharging perineal wound",
          "Prevented by the __5 cleans, aseptic technique, avoiding unnecessary vaginal examinations, treating anaemia, and early management of prolonged rupture of membranes__; isolate, take swabs and blood cultures, give antibiotics, fluids and analgesia, continue breast feeding if possible, encourage the Fowler's position for drainage, and observe for septic shock and thrombophlebitis"],
         ["__Preterm labour and premature rupture of membranes__", "Contractions before 37 weeks / leaking of fluid before labour",
          "Bed rest, __sterile pad and no vaginal examination or douching__, note the colour and odour of the fluid, monitor the temperature and the fetal heart, tocolytics, __antenatal corticosteroids (dexamethasone/betamethasone) to mature the fetal lungs__ and antibiotics as ordered; refer where newborn care is available"],
         ["__Other__", "Cord prolapse (__knee-chest or exaggerated Sims' position, keep the cord moist and warm, do not handle it, give oxygen and transfer immediately for caesarean__); breech and malpresentation; twin delivery; shoulder dystocia; uterine inversion; amniotic fluid embolism; deep vein thrombosis; retention of urine; abortion and ectopic pregnancy",
          "Recognise, give first aid, and refer urgently — the __key nursing skill is early recognition and prompt referral with a written note, an IV line running and an escort__"]],
        caption="Table 24.3  Obstetric emergencies and complications")

    b.section_h("24.8", "Family Planning (Contraception)")
    b.table(
        ["Method", "Description", "Points"],
        [["__Natural / fertility awareness__", "Calendar (rhythm), basal body temperature, cervical mucus (Billings), symptothermal, standard-days method with CycleBeads",
          "No cost or side effects but a high failure rate; needs regular cycles and co-operation; the fertile period is about days 8-19 of a 28-day cycle (ovulation on day 14 ± 2)"],
         ["__Lactational amenorrhoea method (LAM)__", "Protective only if __all three__ apply: the baby is under 6 months, is __exclusively breast fed day and night__, and the mother has __not resumed menstruation__", "About 98% effective when all three conditions hold"],
         ["__Barrier__", "__Condom (Nirodh)__, female condom, diaphragm, cervical cap, spermicide",
          "The condom is the only method that also __protects against sexually transmitted infections and HIV__; use a new one each time, check the expiry, store away from heat, and hold the rim while withdrawing"],
         ["__Intrauterine device (IUD)__", "__Copper T 380A (effective 10 years), Cu 375 (5 years), post-partum IUCD, and the hormonal LNG-IUS (Mirena, 5 years)__",
          "Long acting, reversible, highly effective; inserted preferably during menstruation, immediately post-partum (within 48 h) or 6 weeks after delivery; teach the patient to check the thread and to report the __'PAINS' warning signs — Period late/abnormal bleeding, Abdominal pain or pain with intercourse, Infection/abnormal discharge, Not feeling well or fever and chills, String missing or longer/shorter__; side effects — heavier periods and cramps; contraindicated in pregnancy, sepsis, unexplained bleeding, distorted uterus and active pelvic infection"],
         ["__Hormonal — combined oral pills (Mala-N/Mala-D)__", "__21 hormone tablets + 7 iron tablets__; start on the __5th day of the cycle__ and take __one tablet daily at the same time__",
          "Highly effective if taken regularly; __if one pill is missed, take it as soon as remembered and the next at the usual time; if 2 or more are missed, take one daily and use a condom for 7 days__; ~contraindicated in pregnancy, breast feeding (under 6 months), over 35 with smoking, hypertension, heart disease, thrombosis, migraine with aura, liver disease and breast cancer~; benefits — regular lighter periods, less dysmenorrhoea, protection against ovarian and endometrial cancer"],
         ["__Progestogen-only__", "Mini-pill, __injectable DMPA (Antara — every 3 months)__, __Chhaya (centchroman/ormeloxifene — a non-hormonal weekly pill: twice weekly for 12 weeks then once weekly)__, implants",
          "Safe in lactation; irregular spotting or amenorrhoea is common and is not harmful — counsel beforehand; return of fertility may be delayed after DMPA"],
         ["__Emergency contraception__", "__Levonorgestrel 1.5 mg as a single dose, as early as possible and within 72 hours__ (or a copper IUD within 5 days)",
          "Not for regular use; does not protect against infection; may cause nausea and a change in the next period; ~it is not an abortion pill~"],
         ["__Permanent (sterilisation)__", "__Female: minilap or laparoscopic tubectomy (also post-partum)__; __Male: vasectomy — simpler, safer and quicker (NSV — no-scalpel vasectomy)__",
          "Informed written consent, eligibility as per the standards (age, number of living children), and counselling that it is __permanent__; after vasectomy, __another method must be used for 3 months or 20 ejaculations__ (sperm are still present); a post-operative check and care of the site; the __couple must be told it is not reversible__"]],
        caption="Table 24.4  Methods of contraception")
    b.bullets([
        "__Eligible couple__ — a married couple in which the wife is in the reproductive age group (__15-45 years__); a __couple protection rate__ is the percentage of eligible couples effectively protected by any method.",
        "__Legal points__ — __Medical Termination of Pregnancy Act, 1971 (amended 2021)__: termination up to __20 weeks on the opinion of one registered medical practitioner, 20-24 weeks for specified categories on the opinion of two__, and beyond 24 weeks only with a Medical Board's approval for substantial fetal abnormality; only the __woman's own consent__ is needed (guardian's if she is under 18 or mentally ill); the provider's and the woman's identity are confidential. The __PCPNDT Act, 1994__ prohibits __prenatal sex determination and disclosure of the sex of the fetus__ — a punishable offence; every ultrasound centre must display the notice and maintain Form F records.",
        "__Schemes__ — __Janani Suraksha Yojana (JSY)__ — cash assistance for institutional delivery; __Janani Shishu Suraksha Karyakram (JSSK)__ — free delivery, caesarean section, drugs, diagnostics, diet, blood and transport for the mother and the sick newborn; __PMSMA__ — assured antenatal check-up on the 9th of each month; __SUMAN, LaQshya, Mission Parivar Vikas, Pradhan Mantri Matru Vandana Yojana__ (maternity benefit).",
    ])

    b.box("recap", [
        "* EDD by Naegele's rule = LMP + 9 months + 7 days. Fundus: at the umbilicus at 20-22 weeks, xiphisternum at 36 weeks; SFH in cm = weeks after 24 weeks.",
        "* Antenatal: at least 4 visits (WHO 8 contacts); IFA and calcium for 180 days + 180 days; albendazole after the first trimester; 2 doses of Td 4 weeks apart; extra 350 kcal and 15-23 g protein; weight gain 10-12 kg.",
        "* Danger signs: bleeding, leaking, severe headache/blurred vision, convulsions, reduced fetal movements, fever, severe pain.",
        "* Stages of labour: I dilatation (primi about 12 h, multi 6-8 h, active phase 1 cm/h); II expulsion (primi 1-2 h, multi 30-60 min, FHR every 5 min); III placental (5-15 min, AMTSL with oxytocin 10 IU IM within 1 minute); IV first 1-2 hours — watch for PPH.",
        "* 5 cleans: clean hands, surface, blade, cord tie, cord stump. Normal blood loss up to 500 mL.",
        "* Newborn: dry and keep warm, skin-to-skin, Apgar at 1 and 5 min (7-10 normal), delayed cord clamping, nothing on the cord, vitamin K 1 mg IM, breast feed within 1 hour, BCG + OPV-0 + hepatitis B at birth; bath after 24 hours.",
        "* Physiological jaundice appears after 24 hours and clears by 10-14 days; jaundice in the first 24 hours is always abnormal.",
        "* Lochia rubra 1-4 days, serosa 5-9, alba 10-15; fundus falls about 1 cm/day and is impalpable by day 12-14; puerperium = 6 weeks.",
        "* PPH is the leading cause of maternal death — the 4 T's (Tone is commonest); massage the uterus, empty the bladder, oxytocin, IV fluids, arrange blood.",
        "* Eclampsia: magnesium sulphate — check the respiratory rate, urine output and knee reflex; antidote calcium gluconate.",
        "* Copper T 380A lasts 10 years; combined pill started on day 5; emergency contraception within 72 hours; vasectomy needs another method for 3 months.",
        "* MTP Act 1971/2021 (20 weeks — one doctor; 20-24 weeks — two; woman's consent only); PCPNDT Act 1994 bans sex determination.",
    ])


def appendix(b):
    b.chapter("A", "Rapid Revision — The Last-Night Sheet",
              "The most frequently asked facts, figures and one-liners from the whole syllabus")

    b.section_h("A.1", "Vital Signs and Normal Values")
    b.table(
        ["Parameter", "Normal value"],
        [["Temperature (oral / axillary / rectal)", "37 °C (98.6 °F) / 0.5 °C less / 0.5 °C more; hyperpyrexia above 41 °C, hypothermia below 35 °C"],
         ["Pulse — adult / newborn", "60-100 (average 72) / 120-160 per minute"],
         ["Respiration — adult / newborn", "12-20 / 30-60 per minute; pulse : respiration = 4-5 : 1"],
         ["Blood pressure / SpO2", "Under 120/80 mmHg; pulse pressure 30-40; MAP 70-105 / SpO2 95-100%"],
         ["Urine output", "1-2 mL/kg/h (30-60 mL/h; 1500 mL/day); oliguria under 400 mL/day"],
         ["Fluid requirement", "2-3 L/day (30-35 mL/kg)"],
         ["Blood volume / Cardiac output", "5-6 L (70-80 mL/kg) / 4-6 L per minute"],
         ["Haemoglobin (men / women / pregnancy)", "13-17 / 12-15 g/dL; anaemia in pregnancy below 11 g/dL"],
         ["WBC / Platelets", "4000-11 000 /mm3 / 1.5-4.5 lakh /mm3"],
         ["Fasting blood sugar / HbA1c", "70-100 mg/dL (diabetes 126+) / under 5.7% (diabetes 6.5%+)"],
         ["Sodium / Potassium", "135-145 / 3.5-5.0 mEq/L"],
         ["Urea / Creatinine / Bilirubin", "15-40 / 0.6-1.2 / 0.3-1.2 mg/dL"],
         ["GCS", "3 (worst) to 15; 8 or less = coma"]],
        caption="Table A.1  Numbers you must not forget", align_center_cols=(1,))

    b.section_h("A.2", "Timings and Intervals")
    b.bullets([
        "__Turn the patient__ every 2 hours • __back care__ 2-4 hourly • __mouth care of the unconscious__ 2 hourly.",
        "__Hand wash__ 20-40 seconds (alcohol rub 20-30 s) • __surgical scrub__ 3-5 minutes.",
        "__Thermometer__: oral 2-3 min, axillary 3-5 min, rectal 1-2 min.",
        "__Autoclave__ 121 °C/15 lb/15-20 min • __hot air oven__ 160 °C/2 h • __boiling__ 20-30 min.",
        "__Suction__ 10-15 seconds per pass • __hot water bag__ 50-60 °C (adult) • __sitz bath__ 40-43 °C for 15-20 min.",
        "__Enema__ 500-1000 mL at 40.5-43 °C, can 45-50 cm high, tube 7.5-10 cm, retain 5-15 min.",
        "__Flatus tube__ 20-30 min • __ice bag / hot application__ 20-30 min • __mustard plaster__ 15-20 min.",
        "__Transfusion__: start within 30 min of issue, slow for the first 15 min, complete within 4 hours.",
        "__Fasting before anaesthesia__: clear fluids 2 h, breast milk 4 h, light meal 6 h, heavy meal 8 h.",
        "__PEP for HIV__: within 2 hours (max 72 h), for 28 days • __HBIG__ within 24 hours.",
        "__CPR__: 30:2, 100-120 compressions/min, 5-6 cm deep, change compressor every 2 min, adrenaline every 3-5 min.",
        "__Mantoux__ read at 48-72 hours; 10 mm induration = positive.",
        "__Suture removal__: face 3-5 days, trunk 7-10 days, over joints/leg 10-14 days.",
    ])

    b.section_h("A.3", "'Firsts', 'Commonests' and 'Bests'")
    b.table(
        ["Question", "Answer"],
        [["Single most important measure to prevent infection", "__Hand hygiene__"],
         ["Commonest site of pressure sore / in a sitting patient", "__Sacrum__ / __ischial tuberosity__"],
         ["Commonest hospital-acquired infection", "__Catheter-associated urinary tract infection__"],
         ["Most reliable and commonest method of hospital sterilisation", "__Autoclaving__"],
         ["Most heat-sensitive vaccine / most freeze-sensitive", "__OPV__ / __hepatitis B, DPT, TT (adsorbed vaccines)__"],
         ["Safest and commonest route of drug administration / fastest", "__Oral__ / __intravenous__"],
         ["Safest IM site in an adult / in an infant", "__Ventrogluteal__ / __vastus lateralis__"],
         ["Commonest cause of a fatal transfusion reaction", "__Clerical error causing ABO incompatibility__"],
         ["Commonest transfusion reaction", "__Febrile non-haemolytic reaction__"],
         ["Universal donor of red cells / of plasma", "__O negative__ / __AB__"],
         ["Commonest type of shock", "__Hypovolaemic__"],
         ["Leading cause of maternal death in India", "__Post-partum haemorrhage__"],
         ["Commonest cause of PPH", "__Atonic uterus (Tone)__"],
         ["Commonest cause of delayed wound healing", "__Infection__"],
         ["Commonest early post-operative fever (day 1-2)", "__Atelectasis (Wind)__"],
         ["Commonest psychosis / commonest cause of dementia", "__Schizophrenia__ / __Alzheimer's disease__"],
         ["Strongest predictor of suicide", "__A previous attempt__"],
         ["First antibody produced in infection / crosses the placenta", "__IgM__ / __IgG__"],
         ["Reference protein with the highest biological value", "__Egg (100)__"],
         ["Commonest nutritional deficiency in the world", "__Iron deficiency anaemia__"],
         ["Best position for an unconscious patient / for dyspnoea", "__Lateral (recovery)__ / __Fowler's or orthopnoeic__"],
         ["Best method to confirm a nasogastric tube position at the bedside", "__pH of the aspirate (5.5 or less)__; X-ray is the gold standard"],
         ["Drug of choice in anaphylaxis / in eclampsia / in cholera", "__Adrenaline IM__ / __magnesium sulphate__ / __ORS and fluids__"],
         ["Safest drug distribution system in a hospital", "__Unit dose dispensing__"],
         ["Most strictly controlled drug schedule", "__Schedule X__"]],
        caption="Table A.2  One-line answers that repeat every year")

    b.section_h("A.4", "Important Days and Landmarks")
    b.table(
        ["Day", "Date", "Day", "Date"],
        [["World Health Day", "7 April", "International Nurses Day", "12 May"],
         ["World Red Cross Day", "8 May", "World No Tobacco Day", "31 May"],
         ["World Blood Donor Day", "14 June", "World Population Day", "11 July"],
         ["World Breastfeeding Week", "1-7 August", "National Nutrition Week", "1-7 September"],
         ["World Pharmacists Day", "25 September", "World Heart Day", "29 September"],
         ["International Day of Older Persons", "1 October", "World Mental Health Day", "10 October"],
         ["Global Handwashing Day", "15 October", "World Diabetes Day", "14 November"],
         ["World AIDS Day", "1 December", "World Tuberculosis Day", "24 March"],
         ["World Cancer Day", "4 February", "World Kidney Day", "2nd Thursday of March"]],
        caption="Table A.3  Health days")
    b.bullets([
        "__Florence Nightingale__ 1820-1910, Crimean War 1854-56, first nursing school 1860 • __Red Cross__ (Henri Dunant) 1863, __Indian Red Cross 1920__ • __ICN 1899__ • __TNAI 1908__ • __INC Act 1947__ (constituted 1949) • __WHO 1948__ • __Pharmacy Act 1948__ • __Drugs and Cosmetics Act 1940/Rules 1945__ • __NDPS Act 1985__ • __UIP 1985__ • __NMHP 1982__ • __NRHM 2005__ • __Mental Healthcare Act 2017__ • __Ayushman Bharat 2018__ • __BMW Rules 2016__.",
        "__Smallpox eradicated 1980__ (last case in India 1975) • __India polio-free 27 March 2014__ • __maternal and neonatal tetanus eliminated 2015__.",
    ])

    b.section_h("A.5", "Colour Codes and Mnemonics")
    b.bullets([
        "__Bio-medical waste__ — __Yellow__: anatomical, soiled, expired drugs, laboratory waste (incinerate) • __Red__: recyclable plastics (autoclave and shred) • __White__: sharps • __Blue__: glass and metal implants • __Black__: general waste.",
        "__Gas cylinders__ — __oxygen: black with a white shoulder__ • nitrous oxide: blue • carbon dioxide: grey • entonox: blue with blue-and-white quarters.",
        "__ECG limb leads__ — RA red, LA yellow, LL green, RL black ('__R__ide __Y__our __G__reen __B__ike').",
        "__Triage__ — red immediate, yellow urgent, green minor, black dead/expectant.",
        "__ADPIE__ — nursing process • __ABC__ — airway, breathing, circulation • __RICE__ — rest, ice, compression, elevation • __FAST__ — face, arm, speech, time (stroke) • __SBAR__ — situation, background, assessment, recommendation • __PQRST__ — pain assessment • __5 W's__ — post-operative fever • __4 T's__ — causes of PPH • __5 P's__ — pain, pallor, paraesthesia, pulselessness, paralysis • __5 CLEANS__ — home delivery • __3 D's__ — pellagra (dermatitis, diarrhoea, dementia) • __5 moments__ — hand hygiene • __PAINS__ — IUD warning signs • __CAUTION__ — cancer warning signs.",
    ])

    b.box("recap", [
        "Read this appendix the night before the examination, then re-read the __'Chapter at a Glance'__ box at the end of every chapter. Those boxes together contain nearly every fact that has ever been asked from the Home Nursing section.",
        "Pay special attention to: __numbers and timings, positions, colour codes, drug schedules, immunisation, the cold chain, sterilisation temperatures, transfusion rules, obstetric figures, and the 'commonest/best/first' one-liners.__",
    ])
