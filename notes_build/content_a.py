"""Chapters 1-5 : Introduction to Home Nursing, The Nurse, The Sick Room,
Bed Making, Patient's Toilet."""


def chapter_1(b):
    b.chapter(1, "Introduction to Home Nursing",
              "Meaning, aims, scope, principles, historical background and basic terminology")

    b.section_h("1.1", "Nursing and Home Nursing — Meaning and Definitions")
    b.box("def", [
        "__Nursing__ (ICN) — Nursing encompasses autonomous and collaborative care of individuals of all ages, families, groups and communities, sick or well, in all settings; it includes promotion of health, prevention of illness and the care of ill, disabled and dying people.",
        "__Florence Nightingale's definition__ — \"Nursing is the act of utilising the environment of the patient to assist him in his recovery.\"",
        "__Virginia Henderson's definition__ — \"Nursing is assisting the individual, sick or well, in the performance of those activities contributing to health, its recovery or a peaceful death, that he would perform unaided if he had the necessary strength, will or knowledge.\"",
        "__Home Nursing__ — The care given to a sick, injured, convalescent, aged or disabled person ~in his own home~ by a member of the family or a trained/semi-trained attendant, under the guidance of a doctor or a qualified nurse.",
    ])
    b.bullets([
        "The word __nurse__ comes from the Latin ~nutrix~ = 'to nourish / to nurture'; ~nutricius~ means 'nourishing'.",
        "Home nursing is also called __domiciliary nursing__ or __domiciliary care__; when organised by an agency it is called ~home health care~.",
        "Home nursing is the __oldest form of nursing__ — historically all nursing was done at home by mothers and female relatives ('mother is the first nurse').",
        "In India, home nursing is taught as a part of __First Aid and Home Nursing__ by the __Indian Red Cross Society__ and __St. John Ambulance Association__.",
    ])

    b.section_h("1.2", "Aims and Objectives of Home Nursing")
    b.numbered([
        "To help the patient __regain health__ in the shortest possible time with the least expense and discomfort.",
        "To provide __comfort, safety and cleanliness__ to the patient.",
        "To prevent __complications__ (bed sores, contractures, pneumonia, constipation, deformities) and __spread of infection__ to other family members.",
        "To carry out the __doctor's instructions__ accurately — medicines, diet, rest, treatment.",
        "To __observe and report__ the patient's condition correctly.",
        "To give __psychological support__ — reduce fear, loneliness and anxiety of the patient and family.",
        "To use __available household articles__ economically by improvisation.",
        "To promote __health education__ and self-care so that the family becomes independent in caring.",
        "To assist in __rehabilitation__ and restore the patient to a useful place in family and society.",
        "To relieve the __burden on hospitals__ and to give dignified terminal (palliative) care at home.",
    ])

    b.section_h("1.3", "Need, Scope and Importance of Home Nursing")
    b.sub("Who needs home nursing?")
    b.bullets([
        "Patients with __chronic and long-term illness__ — paralysis, arthritis, cancer, tuberculosis, diabetes, chronic kidney disease.",
        "__Convalescents__ — persons recovering after acute illness, surgery or childbirth.",
        "__Aged and bedridden__ persons; physically and mentally __disabled__ persons.",
        "__Mothers and newborns__ during the ante-natal and post-natal period.",
        "Patients with __minor ailments__ (fever, cold, diarrhoea) not needing hospital admission.",
        "__Terminally ill/dying__ patients who prefer to be cared for at home (palliative and hospice care).",
        "__Infectious disease__ patients kept in home isolation (chickenpox, measles, mumps, COVID-19).",
    ])
    b.sub("Importance")
    b.bullets([
        "Hospital beds are limited and costly — most illnesses in India are actually managed at home.",
        "The home environment gives __emotional security__; recovery is faster where the patient feels loved.",
        "Reduces __hospital acquired (nosocomial) infection__ risk.",
        "Home nursing skill is a part of every citizen's __social responsibility__ and of national health programmes (ASHA, ANM, MPW home visits).",
    ])

    b.section_h("1.4", "Advantages and Limitations of Home Nursing")
    b.table(
        ["Advantages", "Limitations / Disadvantages"],
        [["Familiar, homely, affectionate atmosphere; patient is with family",
          "Trained personnel and equipment are not available"],
         ["Much cheaper than hospital care", "Emergency help may be delayed"],
         ["Less risk of cross (hospital) infection",
          "Lack of knowledge of the care-giver may lead to complications"],
         ["Individual, undivided attention; diet as per patient's taste",
          "Risk of spread of infection to other family members"],
         ["Children and elderly do not feel separated (no separation anxiety)",
          "Physical and mental strain, loss of wages for the family care-giver"],
         ["Family learns health care and becomes self-reliant",
          "Isolation, investigations, operations, oxygen, ICU care not possible at home"],
         ["Rehabilitation is easier within the family and community",
          "Improper diagnosis or self-medication may be dangerous"]],
        caption="Table 1.1  Home nursing at a glance")

    b.section_h("1.5", "Difference between Home Nursing and Hospital Nursing")
    b.table(
        ["Point", "Home Nursing", "Hospital Nursing"],
        [["Place", "Patient's own home", "Hospital ward / ICU"],
         ["Care giver", "Family member or attendant, guided by doctor/nurse",
          "Qualified, registered nurse (24 h shift duty)"],
         ["Equipment", "Improvised household articles", "Standard, sterile, modern equipment"],
         ["Cost", "Low", "High"],
         ["Supervision", "Intermittent (doctor's visit / tele-advice)", "Continuous medical supervision"],
         ["Type of patient", "Mild, chronic, convalescent, aged, terminal",
          "Acute, serious, surgical, emergency"],
         ["Records", "Simple diary / TPR note", "Elaborate legal case sheets and charts"],
         ["Infection risk", "Mainly to family members", "Cross-infection between patients"],
         ["Diet", "Home-cooked, as per liking", "Hospital diet as prescribed by dietician"]],
        caption="Table 1.2  Home nursing vs. hospital nursing")

    b.section_h("1.6", "Basic Principles of Nursing Care")
    b.kv_bullets([
        ("Safety first", "protect the patient from injury, falls, burns, infection and wrong medicine."),
        ("Cleanliness / asepsis", "hand washing before and after every procedure is the single most important measure."),
        ("Comfort", "physical (position, clean bed, relief of pain) and mental (kind words, privacy)."),
        ("Individualisation", "no two patients are alike — care is planned according to age, illness, habits and culture."),
        ("Economy", "of time, energy, money and material; improvise wherever possible."),
        ("Observation and reporting", "watch continuously, record accurately, report promptly."),
        ("Body mechanics", "correct posture and lifting technique protect the care-giver's back."),
        ("Privacy and dignity", "screen the patient, expose only the required part."),
        ("Self-care/rehabilitation", "encourage the patient to do whatever he can do himself."),
        ("Health education", "every contact is an opportunity to teach the family."),
    ])

    b.section_h("1.7", "Steps of the Nursing Process (ADPIE)")
    b.table(
        ["Step", "What is done"],
        [["1. Assessment", "Collect data — history, observation, vital signs, physical examination"],
         ["2. Diagnosis (nursing diagnosis)", "Identify the patient's problems / needs"],
         ["3. Planning", "Set priorities and goals; write the nursing care plan"],
         ["4. Implementation", "Carry out the planned nursing care"],
         ["5. Evaluation", "Judge whether the goal is achieved; modify the plan"]],
        caption="Table 1.3  The five steps of the nursing process")
    b.box("mnemonic", ["Remember __A-D-P-I-E__ : ~Assessment → Diagnosis → Planning → Implementation → Evaluation.~"])

    b.section_h("1.8", "Maslow's Hierarchy of Human Needs (basis of care priority)")
    b.table(
        ["Level (lowest first)", "Needs", "Nursing example"],
        [["1. Physiological", "Air, water, food, elimination, rest, temperature, sex, activity",
          "Oxygen, feeding, bedpan, sleep"],
         ["2. Safety and security", "Protection from injury and infection", "Side rails, asepsis, correct drug"],
         ["3. Love and belonging", "Affection, acceptance, company", "Allow visitors, talk to patient"],
         ["4. Self esteem", "Respect, recognition, independence", "Privacy, praise, self-care"],
         ["5. Self actualisation", "Achieving one's full potential", "Rehabilitation, vocation"]],
        caption="Table 1.4  Maslow's need hierarchy")
    b.box("hy", ["__Physiological needs are met first__ — of these, the need for __oxygen (air)__ is the most urgent.",
                 "Order of urgency in an emergency: __Airway → Breathing → Circulation (ABC)__."])

    b.section_h("1.9", "The Home Nursing Team and the Role of the Pharmacist")
    b.bullets([
        "__Team members__ — patient and family, doctor, nurse/ANM, pharmacist, physiotherapist, dietician, social worker, ASHA/health worker, laboratory technician.",
        "The __patient is the centre__ of the team; the family care-giver is the key worker in home nursing.",
    ])
    b.sub("Role of the pharmacist in home nursing / home health care")
    b.numbered([
        "__Dispensing__ medicines accurately with clear labelling and instructions.",
        "__Patient counselling__ — dose, timing, relation to food, duration, expected side effects, what to avoid.",
        "Advising on __storage__ (cool dry place, refrigeration of insulin/vaccines, keeping away from children).",
        "Detecting and preventing __drug interactions, duplication and polypharmacy__ in chronic and elderly patients.",
        "Supplying and teaching use of __surgical dressings, bandages, sick-room appliances, glucometers, BP instruments, nebulisers, inhalers, insulin pens__.",
        "__Reporting adverse drug reactions__ (pharmacovigilance) and discouraging self-medication and antibiotic misuse.",
        "__Health education__ — ORS preparation, immunisation, family planning, first aid, personal hygiene, safe disposal of expired drugs and sharps.",
        "Maintaining statutory __records__ for Schedule H/H1/X and narcotic drugs.",
    ])

    b.section_h("1.10", "Historical Development of Nursing (frequently asked)")
    b.table(
        ["Person / Body", "Contribution", "Year"],
        [["__Florence Nightingale__", "'The Lady with the Lamp'; founder of modern nursing; worked in the Crimean War at Scutari Barrack Hospital; opened the first nursing school at St. Thomas' Hospital, London (1860); wrote ~Notes on Nursing~; environmental theory; reduced death rate from 42% to about 2%",
          "1820-1910 (Crimean War 1854-56)"],
         ["__International Nurses Day__", "Celebrated on __12 May__ — Florence Nightingale's birthday", "12 May"],
         ["__Nightingale Pledge / Lamp__", "Lamp = symbol of nursing; the pledge is taken by student nurses", "-"],
         ["__Henri Dunant__", "Founder of the __Red Cross__ after the Battle of Solferino; wrote ~A Memory of Solferino~; first Nobel Peace Prize (1901); __World Red Cross Day 8 May__ (his birthday)",
          "1863 (ICRC)"],
         ["__Indian Red Cross Society__", "Established by an Act of Parliament; teaches First Aid and Home Nursing", "1920"],
         ["__St. John Ambulance Association (India)__", "First aid and home nursing training", "1920"],
         ["__International Council of Nurses (ICN)__", "First international organisation of nurses; HQ __Geneva__", "1899"],
         ["__Trained Nurses' Association of India (TNAI)__", "National professional body of nurses in India", "1908"],
         ["__Indian Nursing Council (INC)__", "Statutory body constituted by the Indian Nursing Council Act 1947 to maintain uniform standards of nursing education; HQ __New Delhi__",
          "Act 1947, constituted 1949"],
         ["__Dai / traditional birth attendant__", "Conducted deliveries at home in old India", "-"],
         ["__Sister Dora, Mary Seacole, Clara Barton__", "Clara Barton founded the __American Red Cross__ (1881)", "19th century"],
         ["__WHO__", "World Health Organization established; __World Health Day 7 April__", "7 April 1948"]],
        caption="Table 1.5  Landmarks in the history of nursing")

    b.section_h("1.11", "Common Nursing Terminology (must-know glossary)")
    b.table(
        ["Term", "Meaning"],
        [["Patient / client", "A person receiving health care"],
         ["Acute illness", "Sudden onset, short duration, severe"],
         ["Chronic illness", "Slow onset, long duration (more than 3 months)"],
         ["Convalescence", "Period of recovery between the end of disease and return to full health"],
         ["Prognosis", "Prediction of the probable outcome of a disease"],
         ["Diagnosis", "Identification of the disease"],
         ["Sign", "Objective evidence seen by others (rash, swelling, fever)"],
         ["Symptom", "Subjective complaint felt by the patient (pain, nausea)"],
         ["Syndrome", "A group of signs and symptoms occurring together"],
         ["Etiology", "Cause of disease"],
         ["Pathogenesis", "Mechanism by which disease develops"],
         ["Remission / Relapse", "Temporary disappearance of symptoms / return of symptoms"],
         ["Morbidity / Mortality", "Rate of sickness / rate of death in a population"],
         ["Epidemic / Endemic / Pandemic / Sporadic", "Sudden excess in an area / constantly present in an area / worldwide spread / occasional isolated cases"],
         ["Prophylaxis", "Measure taken to prevent disease"],
         ["Palliative care", "Relief of symptoms without curing the disease"],
         ["Rehabilitation", "Restoring a person to maximum usefulness"],
         ["Ambulatory patient", "A patient who is able to walk about"],
         ["Bedridden / Helpless patient", "Confined to bed / unable to do anything for himself"],
         ["Terminal illness", "Illness from which recovery is not expected"],
         ["Prone / Supine", "Lying on abdomen (face down) / lying on back (face up)"],
         ["Vital signs", "Temperature, pulse, respiration, blood pressure (± pain, SpO2)"],
         ["NPO / Nil by mouth", "Nothing to be given by mouth"],
         ["Stat / SOS / PRN", "At once / if necessary / as and when required"],
         ["Aseptic technique", "Practices that keep an area free from micro-organisms"]],
        caption="Table 1.6  Basic terminology")

    b.section_h("1.12", "Articles Required for Home Nursing (the home sick-room kit)")
    b.table(
        ["Group", "Articles"],
        [["Measuring / observation", "Clinical thermometer, watch with second hand, BP apparatus with stethoscope, weighing machine, measuring glass, torch, glucometer, pulse oximeter"],
         ["Linen", "Bed sheets, draw sheet, mackintosh/rubber sheet, pillow covers, blankets, towels, patient gowns, cotton pads"],
         ["Elimination", "Bedpan, urinal, kidney tray, sputum cup with lid, commode chair, bucket with lid, catheter and urine bag (if needed)"],
         ["Dressing / first aid", "Sterile gauze, cotton wool, roller and triangular bandages, adhesive plaster, scissors, forceps, antiseptic lotion (povidone iodine, spirit), band-aid, sterile gloves"],
         ["Medicine administration", "Medicine glass, spoon (5 mL), dropper, oral syringe, syringes and needles, nebuliser, inhaler with spacer"],
         ["Comfort appliances", "Backrest, air/rubber ring, bed cradle, hot water bag, ice bag, air cushion, footboard, sandbags, walker, wheelchair"],
         ["Hygiene", "Soap, basin, mug, mouth wash, nail cutter, comb, hand sanitiser, disinfectant (bleaching powder, phenol), waste bags"]],
        caption="Table 1.7  Standard home nursing articles")
    b.box("clinical", [
        "__Improvisation__ is the heart of home nursing — using ordinary household articles in place of hospital equipment:",
        "* Bed cradle ← wooden stool or cardboard box placed under the top sheet",
        "* Back rest ← inverted chair, wooden plank or firm pillows",
        "* Draw mackintosh ← thick polythene sheet or an old plastic table cover",
        "* Air ring ← a ring made of cloth/cotton or a rubber tube",
        "* Sand bag ← cloth bag filled with dry sand; Footboard ← wooden plank or a suitcase",
        "* Kidney tray ← steel bowl;  Sputum cup ← covered tin with newspaper lining",
        "* Ice bag ← polythene bag with crushed ice in a towel;  Hot water bag ← bottle wrapped in cloth",
        "* Steam inhaler ← kettle with a paper funnel;  Feeding cup ← spouted cup / straw",
    ])

    b.section_h("1.13", "Ethical and Legal Aspects; Rights of the Patient")
    b.bullets([
        "__Confidentiality__ — never disclose the patient's illness or secrets to outsiders.",
        "__Informed consent__ — necessary before any procedure, operation or investigation; a written consent is taken from the patient (adult, conscious, sound mind) or from the guardian for minors (<18 years) and the unconscious/mentally ill.",
        "__Negligence__ — failure to give the standard of care expected; __malpractice__ = professional negligence. ~Res ipsa loquitur~ = 'the thing speaks for itself'.",
        "__Assault and battery__ — threatening / touching or treating a patient without consent.",
        "__Patient's rights__ — right to information, right to privacy and dignity, right to a second opinion, right to refuse treatment, right to records, right to safe care without discrimination.",
        "__Documentation rule__ — 'If it is not recorded, it is not done'; records are legal documents. Never erase or use white ink; strike out with a single line, write 'error', and initial it.",
    ])

    b.box("recap", [
        "* Nursing = ~nutrix~ (to nourish). Home nursing = care of the sick in his own home.",
        "* Florence Nightingale (1820-1910): founder of modern nursing, Crimean War, St. Thomas' Hospital school 1860, ~Notes on Nursing~; Nurses' Day 12 May.",
        "* Red Cross — Henri Dunant, 1863; Indian Red Cross Society 1920; World Red Cross Day 8 May.",
        "* ICN 1899 (Geneva) • TNAI 1908 • INC Act 1947, constituted 1949 • WHO 7 April 1948.",
        "* Nursing process = ADPIE. Maslow: physiological needs first; oxygen is the most urgent.",
        "* Principles: safety, asepsis (hand washing = most important), comfort, privacy, economy, observation, health education.",
        "* Home nursing advantages: cheap, homely, less cross-infection; limitation: no trained staff or emergency equipment.",
    ])



def chapter_2(b):
    b.chapter(2, "The Nurse",
              "Categories, qualifications, qualities, duties, ethics, communication, records and self-care")

    b.section_h("2.1", "Who is a Nurse?")
    b.box("def", [
        "__Nurse__ — A person who is educated and trained in the art and science of nursing, is __registered with a State Nursing Council/Registration Council__, and is licensed to practise nursing.",
        "__Home nurse / attendant__ — a family member or semi-trained person who gives nursing care at home under guidance.",
    ])

    b.section_h("2.2", "Categories of Nursing Personnel in India")
    b.table(
        ["Category", "Course and duration", "Chief function"],
        [["ANM / MPW (Female) — ~Auxiliary Nurse Midwife~", "ANM: 2 years after 10+2",
          "Village-level worker at the sub-centre; MCH care, immunisation, home visits, deliveries"],
         ["GNM — ~General Nursing and Midwifery~", "3 years (+ 6 months internship) after 10+2",
          "Bedside nursing in hospitals and community; registered nurse and midwife (RN, RM)"],
         ["B.Sc. Nursing", "4 years after 10+2 (PCB)", "Staff nurse, ward in-charge, community health nurse, teacher"],
         ["Post Basic B.Sc. Nursing", "2 years for registered GNM nurses", "Supervisory and teaching posts"],
         ["M.Sc. Nursing / Ph.D.", "2 years after B.Sc. / research", "Nurse specialist, tutor, administrator, researcher"],
         ["Nurse Practitioner in Midwifery / NPCC", "Post-graduate residency", "Advanced independent practice"],
         ["Health Worker (Male) / MPW(M)", "1 year", "Communicable disease control, sanitation"],
         ["Nursing aide / Ward attendant / Home attendant", "Short certificate course",
          "Assists the nurse — moving patients, cleanliness, feeding (works under supervision)"],
         ["Dai (traditional birth attendant)", "Trained by the health department", "Assists home deliveries, refers complications"]],
        caption="Table 2.1  Nursing personnel and their preparation")

    b.sub("Regulatory and professional bodies")
    b.kv_bullets([
        ("Indian Nursing Council (INC)", "statutory body, Act of 1947 (constituted 1949), New Delhi — prescribes and maintains uniform standards of nursing education, recognises qualifications."),
        ("State Nursing Council / Registration Council", "registers nurses and midwives in the State; issues the licence to practise; renews registration."),
        ("TNAI (1908)", "professional welfare association of nurses in India; publishes ~The Nursing Journal of India~; member of ICN."),
        ("ICN (1899, Geneva)", "world federation of national nurses' associations; gives the ~ICN Code of Ethics for Nurses~."),
        ("Nurses' Registration and Tracking System / NCA (2023)", "the National Nursing and Midwifery Commission Act, 2023 replaces the INC Act to regulate nursing education and practice."),
    ])

    b.section_h("2.3", "Essential Qualities of a Good Nurse")
    b.table(
        ["Group", "Qualities expected"],
        [["Physical", "Good health, physical fitness and stamina, freedom from infection, clean and neat appearance, good posture, normal vision and hearing, pleasant voice, manual dexterity, immunised (Hepatitis B, tetanus, COVID, influenza)"],
         ["Mental / intellectual", "Intelligence, sound knowledge and skill, keen powers of observation, alertness, memory, resourcefulness, common sense, quick and correct decision-making, willingness to learn"],
         ["Moral / ethical", "Honesty, truthfulness, loyalty, integrity, sense of duty, discipline, punctuality, confidentiality, no discrimination, respect for life"],
         ["Emotional", "Emotional stability, patience, self-control, tolerance, cheerfulness, calmness in emergency, empathy (not mere sympathy), tactfulness"],
         ["Social", "Courtesy, good manners, co-operation, good communication, ability to work in a team, adaptability, sense of humour"],
         ["Professional", "Kindness and sympathy, gentleness, dependability, accuracy, neatness, initiative, accountability, keeping professional secrets, continuing education, leadership"]],
        caption="Table 2.2  The five/six groups of nursing qualities")
    b.box("mnemonic", ["The nurse's '__5 C's__': ~Care, Compassion, Competence, Communication, Conscience~ (some add Commitment and Courage).",
                       "Nightingale's triad: __the nurse must be a good observer, a good reporter and a good companion.__"])

    b.section_h("2.4", "Duties and Responsibilities of the Nurse")
    b.sub("Towards the patient")
    b.bullets([
        "Provide safe, clean, comfortable environment; give bed bath, mouth care, back care and change position.",
        "Observe and record __temperature, pulse, respiration, blood pressure, intake-output__ and general condition.",
        "Give medicines and treatments exactly as prescribed — right drug, dose, route, time and patient.",
        "Feed the helpless, attend to elimination needs, prevent bed sores and deformities.",
        "Give psychological support, listen to the patient, maintain privacy and dignity, explain procedures.",
        "Teach the patient and family about diet, drugs, hygiene, exercise and follow-up.",
        "Prepare the patient for investigations, operation and discharge; give after care.",
    ])
    b.sub("Towards the doctor, the institution and the profession")
    b.bullets([
        "Carry out instructions accurately and report changes and errors immediately; never alter a prescription on one's own.",
        "Keep equipment and drugs in order; check the emergency tray, oxygen and suction daily; avoid wastage.",
        "Maintain accurate records and hand over the ward at the change of shift.",
        "Maintain professional standards, take part in continuing education, guide juniors and students.",
    ])
    b.sub("Towards the family and community")
    b.bullets([
        "Keep the family informed, allay their anxiety and involve them in care.",
        "Give health education, promote immunisation, sanitation, family planning and nutrition.",
        "Report notifiable diseases; participate in national health programmes and disaster relief.",
    ])

    b.section_h("2.5", "Personal Hygiene, Grooming and Uniform of the Nurse")
    b.bullets([
        "__Daily bath__, deodorant, clean under-clothing; hair washed regularly and __tied up / covered__ so that it does not fall forward.",
        "__Nails short__, clean and unpolished; __no artificial nails__; hand jewellery removed (rings and wrist watch harbour organisms) — only a plain wedding band allowed.",
        "__Hand hygiene__ before and after every patient contact — the most important single habit.",
        "Uniform: clean, well fitting, changed daily, worn only on duty; comfortable __low-heeled, closed, non-slip shoes__ with soft soles (noiseless).",
        "Teeth brushed twice daily, no tobacco or strong-smelling food; no heavy perfume or make-up.",
        "__Cuts and abrasions covered__ with waterproof dressing; a nurse with a respiratory or skin infection or diarrhoea should not attend patients.",
        "Adequate rest, balanced diet, exercise, periodic medical check-up and immunisation.",
    ])

    b.section_h("2.6", "Nurse-Patient Relationship and Communication")
    b.sub("Phases of the therapeutic (helping) relationship")
    b.bullets([
        "__Pre-interaction__ — the nurse prepares herself and collects data.",
        "__Introductory / orientation__ phase — introduce oneself, build trust, identify problems, set goals.",
        "__Working phase__ — actual care, teaching, problem solving.",
        "__Termination phase__ — evaluate, prepare the patient for discharge or independence.",
    ])
    b.sub("Elements and types of communication")
    b.bullets([
        "Elements: __sender → message → channel → receiver → feedback__ (the loop is completed only by feedback).",
        "__Verbal__ — spoken and written words: clear, simple, in the patient's language, no medical jargon.",
        "__Non-verbal__ — facial expression, eye contact, touch, posture, gestures, tone, silence, appearance. About __70-90%__ of communication is non-verbal; ~non-verbal cues are more reliable~.",
        "__Therapeutic techniques__ — active listening, open-ended questions, silence, reflection, clarification, paraphrasing, summarising, giving information, offering self, touch.",
        "__Non-therapeutic (blocks)__ — giving false reassurance ('everything will be fine'), giving advice, judging or moralising, changing the subject, why-questions, arguing, belittling feelings, stereotyped comments, defensive response.",
    ])
    b.table(
        ["Barrier", "Example / remedy"],
        [["Physical", "Noise, distance, poor lighting → choose a quiet, private place"],
         ["Physiological", "Deafness, aphasia, unconsciousness, pain → use writing, signs, hearing aid, pictures"],
         ["Psychological", "Fear, anxiety, anger, depression, prejudice → build trust, be patient"],
         ["Social / cultural", "Language, dialect, customs, illiteracy → use interpreter, simple local words, pictures"],
         ["Semantic", "Medical jargon, abbreviations → use lay terms and repeat"]],
        caption="Table 2.3  Barriers to communication")
    b.box("clinical", [
        "__Talking to an unconscious patient:__ always speak to him by name and explain what you are doing — hearing may be intact. Never discuss the prognosis at the bedside.",
        "__Deaf patient:__ face the patient, speak slowly in good light so lips can be read, do not shout.",
        "__Blind patient:__ announce your arrival and departure, keep articles in fixed places, use touch.",
        "__Child:__ speak at eye level, use play, allow the parent to stay, never threaten with an injection.",
    ])

    b.section_h("2.7", "Professional Ethics and Legal Responsibility")
    b.sub("Basic ethical principles")
    b.table(
        ["Principle", "Meaning"],
        [["Autonomy", "Respecting the patient's right to decide (consent, refusal)"],
         ["Beneficence", "Doing good, acting in the patient's best interest"],
         ["Non-maleficence", "'Primum non nocere' — above all, do no harm"],
         ["Justice", "Fair and equal treatment of all, no discrimination"],
         ["Veracity", "Truthfulness"],
         ["Fidelity", "Keeping promises, loyalty, accountability"],
         ["Confidentiality", "Keeping the patient's information secret"]],
        caption="Table 2.4  Ethical principles")
    b.sub("Legal terms every nurse must know")
    b.kv_bullets([
        ("Negligence", "omission to do what a reasonable person would do; four elements — ~duty, breach of duty, damage, direct causation~."),
        ("Malpractice", "negligence by a professional in the course of professional duty."),
        ("Assault / Battery", "threat of bodily harm / actual unauthorised touching or treatment."),
        ("Invasion of privacy", "exposing the patient or revealing information without consent."),
        ("Defamation", "libel (written) or slander (spoken) damaging reputation."),
        ("False imprisonment", "restraining or detaining a patient without proper authority (illegal use of restraints)."),
        ("Informed consent", "explanation of procedure, risks, alternatives before signature; must be voluntary."),
        ("Vicarious liability", "the employer is responsible for the acts of the employee ('respondeat superior')."),
    ])
    b.box("caution", [
        "* Never give a medicine on a verbal order without written confirmation (except in a documented emergency).",
        "* Never leave a prepared injection unlabelled, or administer a drug prepared by someone else.",
        "* Never leave a helpless, confused or paediatric patient unattended with the side rails down.",
        "* Never disclose the patient's diagnosis (HIV, cancer, psychiatric illness) to anyone not authorised.",
    ])

    b.section_h("2.8", "Records and Reports")
    b.bullets([
        "__Purposes__ — communication between team members, continuity of care, legal evidence, research and teaching, statistics, audit, billing.",
        "__Principles of recording__ — ~accuracy, brevity, legibility, completeness, chronological order (with date and time), objectivity (record facts not opinion), authenticity (sign with name and designation), confidentiality, no blank lines~.",
        "__Types of records__ — admission sheet, case sheet/history, TPR-BP chart, intake-output chart, medication (treatment) chart, nurse's notes, nursing care plan, diet sheet, investigation reports, consent forms, referral and discharge summary, birth/death records, narcotic and stock registers.",
        "__Types of reports__ — change-of-shift (handover) report, telephonic report, transfer/referral report, incident/accident report, 24-hour census, notifiable disease report.",
        "Corrections: __single line through the error, write 'error', initial and date__ — never erase, overwrite or use correcting fluid; never use pencil.",
    ])

    b.section_h("2.9", "The Nurse's Own Safety — Occupational Hazards")
    b.table(
        ["Hazard", "Prevention"],
        [["Biological — HBV, HCV, HIV, tuberculosis, COVID-19", "Standard precautions, gloves, mask/N95, hepatitis-B vaccination, never recap needles, puncture-proof sharps box"],
         ["Needle-stick injury", "Do not squeeze; wash with soap and running water; do not scrub; report at once; test the source; start __post-exposure prophylaxis (PEP) within 2 hours, ideally not later than 72 hours__, for 28 days"],
         ["Back injury / musculoskeletal", "Correct body mechanics, bend knees not back, keep load close, use lifting aids and helpers, adjust bed height"],
         ["Chemical / cytotoxic", "Gloves, gown, mask, goggles, biosafety cabinet, spill kit"],
         ["Radiation", "Lead apron, distance, dosimeter badge, avoid in pregnancy"],
         ["Psychological — burnout, stress, violence", "Duty rotation, rest, recreation, counselling, de-escalation training"]],
        caption="Table 2.5  Occupational hazards of nursing personnel")

    b.box("recap", [
        "* INC — Act 1947, constituted 1949, New Delhi; State Council registers the nurse; TNAI 1908; ICN 1899 Geneva.",
        "* Qualities are grouped as physical, mental, moral, emotional, social, professional.",
        "* Hand washing before and after every patient contact = most important duty; nails short, hair tied, no rings.",
        "* Non-verbal communication makes up most of a message; false reassurance and advice-giving are blocks.",
        "* Ethics: autonomy, beneficence, non-maleficence, justice, veracity, fidelity, confidentiality.",
        "* Records: accurate, dated, signed, never erased; 'not recorded = not done'.",
        "* Needle-stick: wash, report, PEP within 2 h (up to 72 h) for 28 days.",
    ])



def chapter_3(b):
    b.chapter(3, "The Sick Room",
              "Selection, ventilation, lighting, temperature, furniture, cleanliness, disinfection and safety")

    b.section_h("3.1", "Meaning and Importance")
    b.box("def", ["__Sick room__ — the room in the house that is selected and prepared for the care of a sick person, so arranged that the patient gets maximum rest, comfort, fresh air and sunlight and the nurse can work with the least effort."])
    b.text("Nightingale's environmental theory states that a healthy environment — pure air, pure water, efficient drainage, cleanliness and light — is essential for recovery. The sick room must therefore be planned before the patient is shifted into it.")

    b.section_h("3.2", "Selection of the Sick Room — Ideal Requirements")
    b.table(
        ["Feature", "Ideal requirement", "Reason"],
        [["Situation", "Quiet part of the house, away from the kitchen, staircase, street and children's play area; preferably on the ground floor",
          "Rest and sleep; easy access for the doctor and stretcher"],
         ["Aspect / direction", "__South or south-east facing__ with windows on two opposite walls",
          "Gets morning sun and cross ventilation"],
         ["Size", "About __10-12 ft x 12-14 ft__; floor space __not less than 50 sq ft (1.5 m x 3 m)__ per patient and air space about __500-1000 cubic feet__",
          "Space to move around the bed on three sides"],
         ["Height of room", "At least __10-12 feet__", "Adequate air space"],
         ["Windows", "Window area = __1/5 of floor area__; sill about 3 ft from floor",
          "Light and ventilation"],
         ["Floor", "Smooth, hard, impervious, washable (mosaic/cement), no carpets or rugs",
          "Easy cleaning; prevents dust and slipping"],
         ["Walls and ceiling", "Light coloured, smooth, washable distemper/oil paint; no cracks or pictures collecting dust",
          "Reflects light; easily disinfected"],
         ["Attached facilities", "Bathroom and lavatory adjoining; water supply and electric points near the bed",
          "Convenience, less exertion"],
         ["Furniture", "Minimum — bed, bedside table, chair, screen, cupboard", "Less dust, more space"],
         ["Doors", "Wide enough to admit a stretcher/wheelchair; open outward if possible", "Emergency removal"]],
        caption="Table 3.1  Ideal features of a sick room")

    b.section_h("3.3", "Ventilation")
    b.box("def", ["__Ventilation__ — the process of replacing foul, used air of an occupied room by fresh outside air, so as to maintain the physical and chemical quality of air (temperature, humidity, movement and purity)."])
    b.sub("Standards")
    b.bullets([
        "Air space required: __1000-1200 cubic feet per person__ (minimum 500 cu ft); floor space __50-100 sq ft__.",
        "Air change required: __2-3 air changes per hour__ for a sick room (up to 6 in hospitals; __12 or more__ in operation theatres and isolation rooms).",
        "Rate of air movement should be about __5-10 ft/second (1-3 m/s)__ — enough to feel refreshing but not a draught.",
        "__Carbon dioxide__ of room air should not exceed __0.04-0.06%__ (600 ppm); it is used as an ~index of air pollution~ (Pettenkofer's standard 0.06%).",
    ])
    b.sub("Types of ventilation")
    b.table(
        ["Type", "Sub-types / methods", "Principle"],
        [["__Natural ventilation__", "Windows, doors, ventilators, skylight, roof ventilator, open verandah; ~cross ventilation~ = openings on opposite walls",
          "Wind (perflation), diffusion, and 'stack effect' (warm air rises and escapes through high openings, fresh air enters low openings) — aided by the ~inequality of temperature~"],
         ["__Artificial / mechanical__", "(a) Exhaust (extraction) — fan removes foul air, e.g. kitchens, mines\n(b) Plenum (propulsion) — fresh air blown in, e.g. theatres\n(c) Balanced — both exhaust and plenum\n(d) Air conditioning — control of temperature, humidity, purity and movement",
          "Fans, blowers, ducts, filters"]],
        caption="Table 3.2  Methods of ventilation")
    b.sub("Practical points")
    b.bullets([
        "Ventilate __without draught__ — never let cold air blow directly on the patient; protect with a screen, and place the bed so that the head is not in the line of the window.",
        "Air the room while giving the bed bath only after covering the patient properly; keep the room aired for a while every day.",
        "Windows are opened __from the top__ in cold weather (warm foul air escapes, cold air is deflected upward).",
        "Do not use a kerosene stove/charcoal ~sigri~ in a closed sick room — risk of __carbon monoxide poisoning__ and oxygen depletion.",
        "Foul air causes discomfort chiefly by __excess heat, humidity, body odour and lack of air movement__, not mainly by CO2 (Hill's theory).",
    ])
    b.box("hy", ["Effects of __inadequate ventilation__: stuffiness, headache, drowsiness, nausea, fainting, poor sleep, increased spread of droplet infection (TB, influenza, measles, COVID-19), and heat cramps/exhaustion."])

    b.section_h("3.4", "Lighting")
    b.bullets([
        "__Natural light (sunlight)__ is best — it is a natural disinfectant (ultraviolet rays), gives vitamin D, cheers the patient and helps detect abnormal colour (jaundice, cyanosis, pallor).",
        "Light should come from __behind or the side__ of the patient, never directly into his eyes; diffuse it with a curtain or blind.",
        "A __shaded bedside lamp / dim night lamp__ is required at night; a torch is kept ready for observation without disturbing sleep.",
        "Glare and flickering cause eye strain and headache; a patient with __measles, meningitis, migraine, eye injury or photophobia__ needs a darkened room.",
        "Illumination of about __100-200 lux__ is adequate for a sick room; more (300-500 lux) for reading and procedures.",
    ])

    b.section_h("3.5", "Temperature, Humidity and Comfort")
    b.table(
        ["Factor", "Desirable level", "Notes"],
        [["Room temperature (adult sick room)", "__20-22 °C (68-72 °F)__", "Measure at bed level with a room thermometer"],
         ["For infants, the aged, and after operation", "__24-27 °C (75-80 °F)__", "They lose heat rapidly"],
         ["Newborn / preterm nursery", "__28-32 °C__ (warmer)", "Prevent hypothermia"],
         ["Relative humidity", "__40-60%__ (ideal about 50%)", "Dry air irritates the throat; damp air prevents sweat evaporation"],
         ["Comfortable 'cooling power'", "Measured by __Kata thermometer__", "Effective temperature combines temperature, humidity and air movement"]],
        caption="Table 3.3  Thermal comfort in the sick room")
    b.bullets([
        "__Humidity is raised__ by keeping an open vessel of water, wet towel or steam kettle (useful in croup, bronchitis, dry cough, tracheostomy).",
        "__Humidity is lowered__ and heat relieved by fans, air-cooler, cross ventilation, and by sprinkling water on the floor (not near the bed).",
        "Instruments: __dry and wet bulb thermometers / hygrometer__ measure humidity; __sling psychrometer__, __globe thermometer__ (radiant heat), __Kata thermometer__ (air velocity and cooling power).",
    ])

    b.section_h("3.6", "Furniture and Equipment of the Sick Room")
    b.table(
        ["Article", "Requirement / use"],
        [["Bed", "Single, __narrow (about 3 ft/90 cm wide)__, __high (about 26-30 inch / 65-75 cm)__ to save the nurse's back, with a __firm level mattress__; accessible from both sides; head of the bed away from the window"],
         ["Bedside table / locker", "For drinking water, medicines, tissues, call bell, kidney tray; keep on the patient's convenient side"],
         ["Over-bed table", "For meals, reading, writing"],
         ["Chair / stool", "For the nurse, visitors, and for the patient to sit out of bed"],
         ["Screen (2-3 fold)", "Privacy during procedures; protection from draught and light"],
         ["Cupboard / shelf", "Linen, dressings and equipment — kept outside the room if the disease is infectious"],
         ["Waste bucket with lid and foot pedal", "Soiled dressings and rubbish, lined with a plastic bag"],
         ["Sink / wash basin, soap, towel, sanitiser", "Hand hygiene"],
         ["Bed pan, urinal, kidney tray, sputum cup", "Elimination and expectoration, each with a lid"],
         ["Clock, calendar, call bell / hand bell", "Orientation and summoning help"],
         ["Rubber goods", "Mackintosh, air ring, hot water bag, ice bag, rubber sheet"],
         ["Linen", "Two sets of bed sheets, draw sheet, pillow covers, blankets, towels, gowns"]],
        caption="Table 3.4  Sick room furniture and equipment")
    b.box("clinical", ["Keep the room __simple and uncluttered__: 'Everything that is not needed must be taken out of the sick room.' Excess furniture, curtains, carpets, flowers in stale water and soft toys collect dust and organisms."])

    b.section_h("3.7", "Cleanliness of the Sick Room")
    b.sub("Principles")
    b.bullets([
        "Cleaning must be done __without raising dust__ and with the least disturbance to the patient.",
        "__Damp dusting__ is the rule — a cloth wrung in warm water with a disinfectant/soap; dry dusting and sweeping with a broom raise dust and organisms.",
        "Clean __from cleaner to dirtier__ areas and __from above downwards__ (ceiling → walls → furniture → floor).",
        "Use a __vacuum cleaner or wet mop__ for the floor; wash the floor daily with soap and water and a disinfectant (phenol 1-2%, bleaching powder solution, sodium hypochlorite 1%).",
        "Cleaning should be finished before meals and before the doctor's visit; the patient is covered and the bed screened.",
    ])
    b.sub("Daily and weekly routine")
    b.table(
        ["Frequency", "Work to be done"],
        [["Several times a day", "Ventilate the room; tidy the bed; damp dust the bedside table, bed rails and equipment; empty and disinfect bedpan, urinal, sputum cup and waste bucket; clean the wash basin"],
         ["Daily", "Wet mop / wash the floor and bathroom; change soiled linen; clean the thermometer; wipe the door handles and switches with disinfectant; remove dead flowers and leftover food"],
         ["Weekly", "Wash windows, doors and window sills; clean under and behind the bed and cupboard; sun the mattress, pillows and blankets; scrub the bathroom; check and replenish stock"],
         ["On discharge / recovery", "__Terminal cleaning and disinfection__ — see 3.9"]],
        caption="Table 3.5  Cleaning routine")

    b.section_h("3.8", "Disposal of Waste, Excreta and Soiled Linen at Home")
    b.bullets([
        "__Excreta__ — normally flushed down the water closet. Infectious excreta (cholera, typhoid, dysentery, hepatitis A) must first be __disinfected for 1-2 hours__ with an equal volume of __bleaching powder (5%) or crude phenol (2-5%)__ or freshly prepared __1% sodium hypochlorite__, and then flushed. In villages with no latrine, bury deep away from the water source.",
        "__Sputum__ — collected in a covered sputum cup lined with paper/containing disinfectant; the paper and sputum are __burnt__; the cup is boiled.",
        "__Soiled dressings, cotton, paper tissues__ — collected in a paper/plastic bag and __burnt or buried__.",
        "__Soiled linen__ — handled with gloves, rolled with the soiled part inside, __never shaken__, soaked in disinfectant, then __boiled/washed separately__ and dried in the sun.",
        "__Left-over food and vomit__ of an infectious patient — disinfected and disposed; crockery boiled or washed with hot detergent water.",
        "__Sharps (needles, lancets, blades)__ — never thrown in household waste; put in a __puncture-proof container__ (tin/thick plastic bottle), needle destroyed/cut, then given to a health facility.",
        "Keep __waste covered__ at all times to keep out flies and animals; wash hands after handling waste.",
    ])

    b.section_h("3.9", "Disinfection of the Sick Room")
    b.table(
        ["Type", "When done", "How"],
        [["__Concurrent disinfection__", "__Throughout the illness__, immediately after the discharges (urine, faeces, sputum, vomit, pus, dressings) are produced",
          "Disinfect excreta and articles at once; damp dust with disinfectant daily"],
         ["__Terminal disinfection__", "__After recovery, death or removal__ of the patient",
          "Remove and wash/boil/sun all linen; wash the floor, walls and furniture with disinfectant; sun the mattress, pillows and blankets for 6-8 hours; expose the room to sunlight and air for 24 hours; whitewash/paint if necessary; boil or autoclave instruments"],
         ["__Fumigation / gaseous disinfection__", "Now considered of __little value__ for routine rooms; used rarely for special situations",
          "Formaldehyde vapour (500 mL formalin + 1000 mL water per 1000 cu ft, room sealed 12 h, neutralised with ammonia), sulphur dioxide by burning sulphur; ~today replaced by thorough cleaning with chemical disinfectants and UV lamps~"]],
        caption="Table 3.6  Concurrent, terminal and gaseous disinfection")
    b.box("num", [
        "* Bleaching powder should contain about __33% available chlorine__ (not less than 30%).",
        "* Household bleach for surface disinfection: __1% sodium hypochlorite__ (1 part of 5% bleach + 4 parts water).",
        "* Phenol (crude carbolic acid) __2-5%__ for floors and excreta;  __70% ethyl alcohol / 60-80% isopropyl__ for skin and small surfaces.",
        "* Boiling for __10 minutes (preferably 20-30 min)__ kills all ordinary pathogens (not spores).",
    ])

    b.section_h("3.10", "Control of Insects, Flies and Rodents")
    b.bullets([
        "__Flies__ (carry typhoid, cholera, dysentery, diarrhoea, food poisoning, trachoma, polio) — keep all food covered, use wire mesh on windows, fly swat/fly paper, bury or cover refuse, remove breeding places (garbage, manure, open drains), use insecticide spray.",
        "__Mosquitoes__ (malaria — ~Anopheles~; dengue/chikungunya — ~Aedes aegypti~, a day biter breeding in clean stored water; filariasis — ~Culex~; Japanese encephalitis — ~Culex tritaeniorhynchus~) — __bed nets (preferably insecticide-treated)__, screens, repellents, mosquito coil/mat, removal of stagnant water, weekly emptying of coolers and flower pots, larvicides (temephos), ~Gambusia~ fish, space spray.",
        "__Bed bugs, lice, fleas__ — boiling and sunning of bedding, scrubbing the cot, insecticide application; pediculosis treated with __permethrin 1% lotion__ or 5% dust in seams.",
        "__Cockroaches__ (mechanical carriers) — block cracks, keep the kitchen dry, bait/insecticide.",
        "__Rats__ (plague, leptospirosis, rat-bite fever, salmonellosis) — rat-proof storage, traps, rodenticides; handle with care.",
        "__Ants__ — keep sugar/food in closed containers; keep the patient's water covered.",
    ])

    b.section_h("3.11", "Safety in the Sick Room")
    b.table(
        ["Hazard", "Preventive measures"],
        [["Falls", "Bed at low height with brakes on, __side rails up__ for the unconscious, restless, elderly and children; call bell within reach; dry non-slippery floor; adequate light at night; support while walking; slippers with grip; no loose wires or mats"],
         ["Burns / scalds", "Test hot water bag temperature (__50-60 °C__) and cover it; never leave hot drinks or a heater within reach of a confused patient; no smoking, especially with oxygen"],
         ["Fire", "No naked flame, spark, oil or grease near __oxygen__; keep matches away; know the exit route; keep sand/water/extinguisher"],
         ["Poisoning / wrong medicine", "Keep all drugs __labelled and locked__ away from children; read the label three times; never keep kerosene or acid in a drink bottle; never keep an external application near oral medicines"],
         ["Electric shock", "Earthed appliances, no wet hands, no over-loaded socket, no wires under the carpet"],
         ["Suffocation / aspiration", "No pillow for infants, no polythene near a child; position the unconscious patient __on the side (recovery/lateral position)__; suction ready"],
         ["Infection", "Hand hygiene, isolation where needed, safe disposal, clean linen"],
         ["Injury to the nurse", "Correct body mechanics and lifting aids"]],
        caption="Table 3.7  Accident prevention in the sick room")

    b.section_h("3.12", "Comfort and the Psychological Environment")
    b.bullets([
        "__Noise control__ — soft shoes, oil hinges, low voices, no radio/TV noise, no whispering near the patient (it creates suspicion); noise should ideally be __below 35-45 dB__ in a sick room.",
        "__Odour control__ — ventilate, remove bedpans and soiled dressings at once, mouth care, clean linen; avoid strong deodorants.",
        "Allow the patient __personal belongings, photographs, a small radio, books__; permit __limited visitors__ at fixed times for a fixed time.",
        "Maintain a __routine__ for meals, medicines, sleep and toilet; group the nursing activities so that the patient gets an uninterrupted rest period.",
        "Avoid discussing the illness within the patient's hearing; answer questions honestly but with hope; respect religious practices.",
    ])

    b.section_h("3.13", "Care of Equipment and Rubber Goods")
    b.table(
        ["Article", "Care"],
        [["Mackintosh / rubber sheet", "Wash with soap and cold or lukewarm water, wipe dry, dust with talcum powder, __roll (never fold sharply)__; keep away from heat, sunlight, oil and spirit"],
         ["Hot water bag", "Fill only __two-thirds__, expel air, screw tightly, invert to test for leak, cover with a flannel bag; store __inflated with air__ and stopper closed"],
         ["Ice bag / air cushion", "Wash, dry, store slightly inflated"],
         ["Clinical thermometer", "Wipe from bulb upward, wash in cool soapy water (__never hot water — it bursts__), disinfect with spirit swab, store dry in individual container or in antiseptic solution"],
         ["Catheters and tubing", "Wash, flush, boil/autoclave or use disposable"],
         ["Instruments (metal)", "Clean off blood/pus, wash, dry, __autoclave or boil 20-30 min__"],
         ["Glassware", "Cold water first (blood is water soluble), then hot soapy water, rinse, dry"],
         ["Linen", "Soak stains (blood — cold water/hydrogen peroxide), wash, boil if infected, dry in the sun, iron"],
         ["Mattress and pillows", "Sun for 6-8 hours, protect with mackintosh, turn regularly"]],
        caption="Table 3.8  Care of sick room articles")

    b.box("recap", [
        "* Ideal sick room: quiet, south/south-east, ground floor, 2 windows opposite (window = 1/5 of floor area), 50-100 sq ft floor and 500-1200 cu ft air space per patient, washable floor, minimum furniture.",
        "* Ventilation: natural (perflation, diffusion, stack effect) and artificial (exhaust, plenum, balanced, air-conditioning); 2-3 air changes/hour; CO2 index of pollution 0.04-0.06%.",
        "* Temperature 20-22 °C (higher for infants, aged, post-op); humidity 40-60%; Kata thermometer measures cooling power.",
        "* Bed: narrow, firm, 26-30 inch high, accessible from both sides.",
        "* Damp dusting only; clean from above downwards and clean to dirty.",
        "* Concurrent disinfection = during illness; terminal = after recovery/death; fumigation is now of little value.",
        "* Bleaching powder 33% available chlorine; 1% hypochlorite for surfaces; boil 20-30 min.",
        "* Safety: side rails, call bell, locked medicines, no flame near oxygen, lateral position for the unconscious.",
    ])



def chapter_4(b):
    b.chapter(4, "Bed Making",
              "Types of beds, procedure, appliances, patient positions, moving and lifting, and prevention of bed sores")

    b.section_h("4.1", "Definition, Purposes and Principles")
    b.box("def", ["__Bed making__ — the technique of preparing a bed in such a way that the patient gets maximum comfort, rest and safety, while the bed remains clean, dry, wrinkle-free and attractive."])
    b.sub("Purposes")
    b.bullets([
        "To provide __comfort, rest and sleep__ — a wrinkle-free, dry bed prevents pressure sores.",
        "To keep the bed and the patient __clean and neat__ and to prevent infection and odour.",
        "To give the patient the __required position__ for treatment, examination or recovery.",
        "To economise the __nurse's time and energy__ and to keep the room tidy.",
    ])
    b.sub("General principles of bed making")
    b.numbered([
        "Collect __all articles__ before starting and arrange them in order of use (saves time and energy).",
        "__Wash hands__ before and after the procedure; wear gloves if the linen is soiled.",
        "Explain the procedure and ensure __privacy__ (screen the bed); maintain the patient's dignity.",
        "Work from __one side to the other__ (complete one side fully, then go to the other side) — this saves steps.",
        "__Never shake the linen__ (it scatters dust and organisms); fold or roll soiled linen with the __soiled surface inside__ and place it in the linen bag, ~never on the floor or on another bed~.",
        "Keep the bed __tight, smooth and wrinkle free__; the mackintosh must always be __completely covered__ by the draw sheet so it never touches the patient's skin.",
        "Use correct __body mechanics__ — raise the bed to a comfortable height, keep the feet apart, bend the knees, keep the back straight.",
        "Watch the patient's __condition, tubes, drains and IV line__ throughout; do not tire him.",
        "Finally: pillow comfortable, top sheet loose over the toes, __call bell, water and personal articles within reach__, side rails up if needed, and the bed lowered."
    ])

    b.section_h("4.2", "Articles Required and the Parts of a Bed")
    b.table(
        ["Article", "Size / purpose"],
        [["Cot / hospital bed", "Narrow (90 cm), firm, height 65-75 cm; may be plain, fowler (adjustable back), or electrically operated with side rails and wheels with brakes"],
         ["Mattress", "Firm, even, of uniform thickness; covered with a mattress cover/protector"],
         ["Bottom (under) sheet", "Large sheet spread over the mattress and tucked with __mitred corners__"],
         ["Mackintosh / rubber sheet", "Waterproof sheet placed across the middle of the bed to protect the mattress; must be covered by the draw sheet"],
         ["Draw sheet", "Half sheet placed over the mackintosh; can be 'drawn' through to give a fresh dry surface without complete bed making"],
         ["Top sheet", "Covers the patient; placed with the __wrong side up and the wide hem at the top__"],
         ["Blanket", "For warmth, covered by the top sheet or counterpane"],
         ["Counterpane / bed spread", "Outermost decorative cover"],
         ["Pillow and pillow cover", "Open end of the cover away from the door / entrance"],
         ["Linen bag / hamper", "For soiled linen"],
         ["Extras", "Bath towel, gown, screen, kidney tray, bedpan, disinfectant"]],
        caption="Table 4.1  Bed linen and equipment")

    b.section_h("4.3", "Types of Beds and their Purposes")
    b.table(
        ["Type of bed", "Description", "Used for"],
        [["__Closed bed__", "Top covers (counterpane) drawn right up to cover the whole bed including pillows", "Unoccupied bed, ready for a new patient; keeps the bed free of dust"],
         ["__Open bed__", "Top covers folded back (fan-folded) to the foot end", "A patient who is ambulant / who will return to bed shortly"],
         ["__Occupied bed__", "Bed made while the patient is in it, changing linen by turning the patient side to side", "Bedridden, helpless, unconscious patients"],
         ["__Admission bed__", "Clean, warm bed prepared with extra blankets and hot water bags, top covers fan-folded",
          "Receiving a new patient"],
         ["__Post-operative / anaesthetic / recovery bed__", "Bed stripped of pillows; mackintosh and draw sheet at the top and middle; top sheet fan-folded to one side lengthwise for easy transfer; warmed with hot water bags (removed before the patient arrives); kidney tray, mouth gag, tongue depressor, suction, oxygen and IV stand kept ready",
          "Patient returning from the operation theatre / unconscious patient"],
         ["__Cardiac bed__", "Patient supported in a sitting position with a backrest and 4-5 pillows; knees slightly flexed (__cardiac chair position__); over-bed table in front",
          "Heart failure, dyspnoea, severe asthma — reduces venous return and eases breathing (orthopnoea)"],
         ["__Fracture bed / orthopaedic bed__", "Firm mattress with __fracture board (bed board)__ under it; blocks to raise the foot of the bed; may have a Balkan frame, traction and bed cradle",
          "Fractures, traction, spinal injury"],
         ["__Divided bed__", "Bed made in two separate halves (top and bottom) leaving the affected part exposed",
          "Amputation of a limb, plaster cast, perineal or rectal operations"],
         ["__Amputation bed__", "A divided bed with sandbags and a bed cradle; a __tourniquet kept at the bedside__ for sudden bleeding",
          "After amputation"],
         ["__Blanket bed (bed for blanket bath/pack)__", "Bed with mackintosh and blanket next to the patient instead of a sheet",
          "Hot/cold packs, blanket bath, hyperpyrexia"],
         ["__Burn bed__", "Sterile bed with sterile linen, bed cradle, cradle to keep covers off the body; may be an air-fluidised bed",
          "Extensive burns — asepsis and prevention of friction"],
         ["__Plaster bed__", "Firm bed with a bed board and extra pillows to support the wet cast, cast left uncovered to dry",
          "Patient with a large plaster cast"],
         ["__Air / water bed, alternating pressure mattress, ripple bed__", "Mattress with air-filled cells that inflate and deflate alternately",
          "Prevention and treatment of __pressure sores__ in long-term bedridden patients"],
         ["__Fowler's bed__", "Head end raised 45-60 degrees (semi-Fowler 30-45 degrees, high Fowler 90 degrees)",
          "Dyspnoea, chest disease, after abdominal surgery, feeding, unconscious with head injury"],
         ["__Sponge / TPR bed__", "Mackintosh with towels spread over the bed", "Cold sponging in high fever"]],
        caption="Table 4.2  Types of beds (a favourite table for objective questions)")

    b.section_h("4.4", "Procedure — Making a Simple / Closed Bed")
    b.numbered([
        "Wash hands; collect linen in the order of use (bottom sheet, mackintosh, draw sheet, top sheet, blanket, counterpane, pillow cover) and carry it to the bedside on a chair/trolley.",
        "Strip the bed: loosen the linen all round, remove the pillow, and remove the covers one by one, __folding each into three (or four)__; place reusable linen on the chair and soiled linen in the bag.",
        "Turn the mattress if required; brush off crumbs; wipe the cot with a damp cloth from the head downwards.",
        "Spread the __bottom sheet__ with the centre fold in the middle of the bed and the wide hem at the head end; tuck in at the head end first, make a __mitred corner__, then tuck the side from head to foot.",
        "Place the __mackintosh__ across the middle of the bed (about 45 cm from the head end) and cover it completely with the __draw sheet__; tuck both in tightly.",
        "Go to the other side and repeat steps 4-5 (this is the 'one side at a time' rule).",
        "Spread the __top sheet__ wrong side up, wide hem at the head end, and the __blanket__ about 20-25 cm below the top; turn the top sheet over the blanket; tuck in at the foot end with mitred corners, leaving a __toe pleat (vertical or horizontal fold)__ to prevent foot drop and pressure on the toes.",
        "Spread the counterpane; put on a fresh pillow cover and place the pillow with its open end away from the door.",
        "Leave the bed neat; clear the articles; wash hands and record."
    ])
    b.box("clinical", ["__Mitred (envelope) corner__ — tuck the sheet end under the mattress, lift the side of the sheet at about 30-45 cm from the corner to form a triangle on the bed, tuck the hanging part under the mattress, then drop the triangle and tuck it in. It keeps the sheet tight and wrinkle-free."])

    b.section_h("4.5", "Making an Occupied Bed / Changing Linen with the Patient in Bed")
    b.numbered([
        "Explain, screen the bed, close windows/fan; wash hands, wear gloves if soiled.",
        "Remove the counterpane and blanket; keep the patient covered with the top sheet (never expose the patient).",
        "Loosen all the bottom linen on the near side; turn the patient __gently to the far side__ (with help, using the side rails for support).",
        "Roll the soiled bottom sheet, mackintosh and draw sheet lengthwise towards the patient's back; brush and wipe the exposed mattress.",
        "Spread the clean bottom sheet on the free half with the excess fan-folded/rolled close to the patient's back; place clean mackintosh and draw sheet; tuck in with mitred corners.",
        "Turn the patient to the clean side (over the rolls); remove the soiled linen, place it in the bag ~without shaking~; pull through and tuck the clean linen tightly.",
        "Change the top sheet by placing the clean one over the soiled one and withdrawing the soiled one from beneath; change the pillow cover and gown as required.",
        "Position the patient comfortably, tidy the bed, give a __back rub__ while the back is exposed, lower the bed, put up side rails, keep the call bell within reach, remove the screen, wash hands and record."
    ])
    b.box("hy", ["Always make the bed __from one side completely, then move to the other side__. Two nurses working on opposite sides make an occupied bed most safely; ~always turn the patient away from the side you are working on.~"])

    b.section_h("4.6", "Bedside Appliances and their Uses")
    b.table(
        ["Appliance", "Use"],
        [["__Bed cradle__ (hoop/frame over the bed)", "Keeps the weight of the bed clothes off a painful part, burn, wound, plaster or ulcer; allows air circulation and inspection; may carry a light for warmth"],
         ["__Backrest__", "Supports the patient in a sitting position (dyspnoea, cardiac, after abdominal surgery, for meals)"],
         ["__Air ring / rubber ring / cotton ring__", "Relieves pressure on the sacrum and buttocks (~use with caution — it may itself impair circulation; a ripple mattress is better~)"],
         ["__Air/water mattress, alternating pressure (ripple) mattress__", "Distributes body weight; prevents pressure sores"],
         ["__Bed blocks / shock blocks__", "Raise the head or foot end of the bed (foot end raised in shock; head end raised in head injury, dyspnoea)"],
         ["__Sandbags__", "Immobilise and support a limb or the head; prevent external rotation"],
         ["__Footboard / foot rest__", "Keeps the foot at a right angle to prevent __foot drop__ and toe pressure; gives something to push against"],
         ["__Bed board / fracture board__", "Placed under the mattress to give a firm surface (traction, spinal or orthopaedic cases)"],
         ["__Pillows, wedge and trochanter rolls__", "Support the head, back, limbs; maintain alignment; prevent external rotation of the hip"],
         ["__Bed rails / side rails__", "Prevent falls in the confused, restless, unconscious, aged and children"],
         ["__Over-bed (cardiac) table__", "For meals, reading, resting arms in dyspnoea"],
         ["__Mackintosh and draw sheet__", "Keep the bed dry; allow the sheet to be drawn through"],
         ["__Bedpan, urinal, commode__", "Elimination in bed or at the bedside"],
         ["__Balkan frame / Bohler-Braun frame, traction, pulleys__", "Continuous traction in fractures"],
         ["__Hand roll, splint__", "Prevent contracture in a paralysed hand"],
         ["__Trapeze bar (monkey bar)__", "Overhead bar the patient grasps to lift himself and change position"],
         ["__Cradle boot / heel protector__", "Prevents pressure on the heel and foot drop"]],
        caption="Table 4.3  Bedside appliances")

    b.section_h("4.7", "Positions of the Patient")
    b.table(
        ["Position", "How the patient lies", "Indications / uses"],
        [["__Supine (dorsal recumbent)__", "Flat on the back, face upward, arms at the sides, one pillow",
          "Rest, spinal injury, after spinal anaesthesia, examination of abdomen, CPR (on a hard surface)"],
         ["__Prone__", "On the abdomen, face turned to one side, arms at the sides or above the head",
          "Drainage of the mouth after tonsillectomy, unconscious patient, back/spine surgery, prevents hip flexion contracture; __prone ventilation__ improves oxygenation in ARDS/COVID-19"],
         ["__Lateral (side lying)__", "On one side, upper knee flexed and supported by a pillow",
          "Rest, relieving pressure on the back, giving an enema/injection (IM gluteal), unconscious patient"],
         ["__Recovery / semi-prone (Sims') position__", "On the left side, lower arm behind the back, upper knee and hip flexed",
          "__Unconscious patient__ (prevents aspiration, keeps the airway open), enema, rectal and vaginal examination, during labour"],
         ["__Fowler's__", "Head end raised __45-60°__, knees slightly flexed (Low/semi-Fowler 30-45°, High Fowler 90°)",
          "Dyspnoea, heart failure, chest disease, after abdominal surgery, feeding, nasogastric tube insertion, head injury (raised ICP)"],
         ["__Orthopnoeic__", "Sitting upright, leaning forward on an over-bed table with arms supported",
          "Severe dyspnoea — asthma, pulmonary oedema, COPD"],
         ["__Trendelenburg__", "Whole body tilted with the __head lower__ than the feet",
          "Pelvic surgery, insertion of a central line, ~formerly in shock — now only passive leg raising is advised~"],
         ["__Reverse Trendelenburg__", "Head higher than feet, body straight", "After head/neck surgery, gastro-oesophageal reflux"],
         ["__Lithotomy__", "On the back, legs raised and separated, hips and knees flexed, feet in stirrups",
          "Vaginal examination, delivery, perineal repair, catheterisation in the female, cystoscopy"],
         ["__Knee-chest (genupectoral)__", "Kneeling with the chest on the bed, head turned to one side, arms above the head",
          "Rectal and sigmoidoscopic examination, correction of a displaced uterus, prolapsed cord"],
         ["__Dorsal recumbent (with knees flexed)__", "On the back with knees drawn up and soles on the bed",
          "Abdominal examination, perineal care, catheterisation"],
         ["__Left lateral (enema) position__", "Left side with the right knee flexed", "Giving an enema/suppository (follows the direction of the colon)"],
         ["__Sitting (upright)__", "Sitting on the bed/chair with feet supported", "Meals, exercises, physiotherapy, examination of the chest"],
         ["__Elevated limb position__", "Affected limb raised on pillows above heart level", "Oedema, after limb surgery, venous ulcer, sprain"]],
        caption="Table 4.4  Patient positions — very frequently asked")
    b.box("mnemonic", ["__Fowler = sitting up__ (Fowl/bird sits up);  __Sims'/recovery = side__ (S for side, Safety of airway);  __Trendelenburg = head down__;  __Lithotomy = legs up for delivery__;  __Knee-chest = rectal examination__."])

    b.section_h("4.8", "Moving, Lifting and Transferring the Patient (Body Mechanics)")
    b.sub("Rules of good body mechanics")
    b.bullets([
        "Keep the __back straight__ and bend at the __hips and knees__, not at the waist; use the strong thigh and leg muscles.",
        "Keep the __feet apart (about 25-30 cm)__ with one foot slightly forward to widen the base of support; keep the __centre of gravity low__.",
        "Hold the load __close to the body__; face the direction of movement; __pivot with the feet, never twist the spine__.",
        "__Push, pull or roll__ rather than lift; use a draw sheet, sliding board, hoist or trolley.",
        "__Raise the bed__ to hip height and lower the side rails on the working side.",
        "Work with a __rhythm and a count__ ('on three') when two or more people lift; the tallest/strongest person takes the heaviest part (head and shoulders); one person gives the commands.",
        "Tell the patient what to do and encourage him to help.",
    ])
    b.sub("Common techniques")
    b.kv_bullets([
        ("Moving up in bed", "one or two nurses with a draw sheet; the patient flexes the knees and pushes with the feet while holding the trapeze bar or crossing the arms on the chest."),
        ("Turning to the side", "cross the far leg over the near, place the near arm across the chest, then roll the patient towards you with the hand on the shoulder and hip (log-rolling for spinal injury, keeping the head, spine and legs in a straight line)."),
        ("Bed to chair/wheelchair", "chair locked at a 45° angle to the bed; the patient sits, dangles the legs, then pivots on the stronger leg; the nurse blocks the patient's knees and feet and holds the transfer belt."),
        ("Bed to stretcher", "three-person carry or a sliding board; stretcher wheels locked, patient covered and strapped, head end first through doors, feet first down a slope."),
        ("Lifting an unconscious patient", "always two or more persons; support the head and neck; keep the airway clear."),
    ])
    b.box("caution", ["__Never lift a patient alone if he is heavy or helpless.__ Never drag the patient over the sheet — friction and shearing force cause __pressure sores__. Never pull on a paralysed arm (risk of shoulder dislocation)."])

    b.section_h("4.9", "Pressure Sores (Bed Sores / Decubitus Ulcer)")
    b.box("def", ["__Pressure sore__ — a localised area of __ischaemic necrosis__ of the skin and underlying tissue caused by __unrelieved pressure__ over a bony prominence (usually between a bone and a hard surface), often combined with friction, shearing force and moisture. Also called ~decubitus ulcer, bed sore or pressure injury~."])
    b.sub("Causes and contributing factors")
    b.table(
        ["Group", "Factors"],
        [["Mechanical (direct)", "Sustained __pressure__ (capillary closing pressure is about __32 mmHg__; tissue damage may begin within __1-2 hours__), __friction__ (dragging), __shearing force__ (sliding down in Fowler's position), wrinkled sheets, crumbs, hard objects, tight bandage or plaster, splints and tubes"],
         ["Moisture", "Incontinence of urine and faeces, sweating, wound discharge, wet linen (maceration of skin)"],
         ["Patient factors", "Immobility (unconscious, paralysed, sedated, in traction, very ill), __poor nutrition (low protein, vitamin C and zinc, anaemia, dehydration)__, emaciation or obesity, old age, thin dry skin, diabetes, peripheral vascular disease, oedema, fever, loss of sensation, faecal/urinary incontinence"],
         ["Nursing factors", "Failure to change position, careless lifting, poor hygiene, wrinkled or damp bed, use of hard bedpans"]],
        caption="Table 4.5  Causes of pressure sores")
    b.sub("Common sites")
    b.bullets([
        "__Supine position__ — __sacrum (most common site overall)__, heels, elbows, occiput, scapulae, spinous processes.",
        "__Lateral position__ — greater trochanter (hip), ear, shoulder (acromion), lateral knee and malleolus (ankle), inner knees.",
        "__Prone position__ — forehead, cheek/ear, chin, shoulder, breast, iliac crest (hip bones), knees, toes, genitalia in men.",
        "__Sitting__ — __ischial tuberosities__ (the commonest site in a wheelchair patient), coccyx, heels.",
    ])
    b.sub("Stages (grades) of pressure injury")
    b.table(
        ["Stage", "Features"],
        [["__Stage I__", "Intact skin with __non-blanchable redness__ (erythema); warmth, oedema, pain; discolouration in dark skin — ~reversible~"],
         ["__Stage II__", "Partial-thickness loss of the dermis — shallow open ulcer, abrasion or __intact/ruptured blister__"],
         ["__Stage III__", "Full-thickness skin loss; subcutaneous fat visible; slough may be present; __bone, tendon and muscle are not exposed__; may undermine"],
         ["__Stage IV__", "Full-thickness tissue loss with __exposed bone, tendon or muscle__; slough/eschar, undermining and tunnelling; risk of osteomyelitis"],
         ["__Unstageable__", "Base covered by slough or eschar so the depth cannot be determined"],
         ["__Deep tissue injury__", "Purple/maroon intact skin or a blood-filled blister from damage to underlying soft tissue"]],
        caption="Table 4.6  Staging of pressure sores")
    b.sub("Prevention — the nurse's most important responsibility")
    b.numbered([
        "__Change position at least every 2 hours__ (every 1 hour if sitting in a chair); keep a __turning chart/clock__ and follow a sequence (supine → right lateral → prone if permitted → left lateral).",
        "Use a __pressure-relieving mattress__ (alternating air/ripple mattress, water bed, foam or gel pads), pillows, heel protectors and a bed cradle; ~avoid the doughnut-type ring~.",
        "Keep the skin __clean and dry__; wash with mild soap and lukewarm water, pat dry (do not rub), apply a moisturiser; use barrier cream for incontinence; change wet linen at once.",
        "Keep the bed __smooth, dry and free of crumbs__; use a draw sheet to move the patient; __never drag__.",
        "Give __back care / pressure area care every 2-4 hours__ — gentle massage of the surrounding area with a moisturiser; ~do not massage directly over a reddened bony prominence~ and do not use spirit or hot water (they dry the skin).",
        "Provide a __high protein, high calorie, vitamin-C, zinc and iron rich diet__ with adequate fluids (2-3 L/day if permitted).",
        "Encourage __active and passive exercise, early ambulation and sitting out of bed__.",
        "Keep the head of the bed at __30° or less__ when possible to reduce shearing; raise the knee gatch slightly.",
        "__Inspect the skin at every turn__ and at every bath, especially over bony points; use a risk-assessment scale (__Braden scale, Norton scale, Waterlow scale__) on admission and at regular intervals.",
        "Avoid tight clothing, hard splints, and pressure from tubes, catheters and oxygen masks."
    ])
    b.sub("Treatment")
    b.bullets([
        "__Relieve the pressure completely__ over the sore — this is the first and most important step.",
        "Clean the ulcer with __normal saline__ (avoid hydrogen peroxide, povidone-iodine and antiseptics on granulating tissue); __debride__ slough (surgical, enzymatic, autolytic).",
        "Apply the appropriate dressing to keep the wound __moist and the surrounding skin dry__ — hydrocolloid, hydrogel, alginate or foam dressing; gauze soaked in saline for cavities.",
        "Treat infection with systemic antibiotics if there is cellulitis, osteomyelitis or sepsis; take a swab for culture; topical silver sulphadiazine/metronidazole for odour.",
        "Improve __nutrition__ (protein 1.2-1.5 g/kg/day, vitamin C, zinc), correct anaemia and control diabetes; relieve pain.",
        "Advanced measures: negative pressure wound therapy (vacuum dressing), skin graft or myocutaneous flap for Stage III-IV.",
    ])
    b.box("hy", [
        "* __Sacrum is the most common site__ of pressure sore; __ischial tuberosity__ in sitting patients; __heel__ is the second commonest.",
        "* Turn the patient __every 2 hours__; capillary closing pressure __32 mmHg__.",
        "* __Stage I__ = non-blanchable erythema with intact skin;  __Stage IV__ = bone/tendon/muscle exposed.",
        "* __Braden scale__ (score ≤ 18 = at risk; 6 sub-scales: sensory perception, moisture, activity, mobility, nutrition, friction/shear) and __Norton scale__ assess risk.",
        "* Clean pressure sores with __normal saline__, not antiseptics.",
    ])

    b.section_h("4.10", "Restraints (Protective Devices)")
    b.bullets([
        "__Types__ — physical (jacket, wrist/ankle cuff, mitten, belt, mummy restraint for infants, side rails) and chemical (sedatives).",
        "__Indications__ — to protect a confused, delirious, restless, psychotic or paediatric patient from pulling out tubes or falling; only when all other measures have failed.",
        "__Rules__ — written doctor's order (except in an emergency), __informed consent__, use the least restrictive type, apply with a __quick-release (clove hitch) knot to the bed frame, not the side rail__, pad the bony points, release and exercise the limb __every 2 hours__ (or at least every 30 min observation), check circulation and skin, record time, reason and response, remove as soon as possible.",
        "Improper use = __false imprisonment__ and can cause injury, strangulation, nerve damage and pressure sores.",
    ])

    b.box("recap", [
        "* Bed making: work one side at a time, never shake linen, mackintosh always covered by the draw sheet, mitred corners, toe pleat to prevent foot drop.",
        "* Post-operative bed: no pillow, top sheet fan-folded lengthwise, suction/oxygen/kidney tray ready; cardiac bed = sitting with backrest; divided bed = amputation/perineal surgery; fracture bed = bed board.",
        "* Positions: Fowler 45-60°, semi-Fowler 30-45°, high Fowler 90°; Sims'/lateral = unconscious; Trendelenburg = head low; lithotomy = delivery; knee-chest = rectal exam.",
        "* Body mechanics: bend knees, load close, pivot with feet, push rather than lift, count together.",
        "* Pressure sore: pressure > 32 mmHg; sacrum commonest; turn 2-hourly; Braden/Norton risk scales; clean with saline; high protein diet.",
        "* Restraints need a written order, quick-release knot to the bed frame, release every 2 hours.",
    ])



def chapter_5(b):
    b.chapter(5, "Patient's Toilet (Personal Hygiene of the Patient)",
              "Bed bath, mouth, hair, eye, ear, nail and back care, elimination needs and care of the incontinent patient")

    b.section_h("5.1", "Meaning, Importance and Principles")
    b.box("def", ["__Personal hygiene (patient's toilet)__ — the self-care measures by which a person maintains cleanliness of the body, mouth, hair, nails, skin and genitalia. When the patient cannot do it himself, the nurse performs it for him."])
    b.sub("Importance / purposes")
    b.bullets([
        "Removes __dirt, sweat, sebum, dead skin and micro-organisms__ — prevents skin infection and body odour.",
        "__Stimulates circulation__ and the nerve endings; relaxes the muscles; promotes sleep and a sense of well-being.",
        "Gives the nurse the chance for __complete observation__ of the skin, pressure areas, oedema, rashes, lumps, ranges of joint movement and the patient's mental state.",
        "Prevents __pressure sores, contractures, dental caries, gum disease, parasitic infestation and constipation__.",
        "Improves __self-esteem, appetite__ and the patient's relationship with the nurse.",
    ])
    b.sub("General principles")
    b.bullets([
        "__Privacy__ (screen the bed, close the door) and __dignity__ at all times — expose only the part being cleaned.",
        "Prevent __chilling__ — close windows and fans, use water at __40-46 °C (105-115 °F)__, cover the rest of the body with a bath blanket.",
        "__Hand hygiene__ and gloves for contact with secretions; clean __from the cleanest to the dirtiest area__ and from __above downwards__.",
        "Follow the patient's __habits, culture and wishes__ (time of bath, oil, soap); encourage self-care as much as possible.",
        "Work __quickly but gently__, with long firm strokes towards the heart; do not tire the patient; observe his condition throughout.",
        "Keep the used water, linen and articles away from the clean ones; clean and replace all equipment after use.",
    ])

    b.section_h("5.2", "Bathing the Patient")
    b.table(
        ["Type of bath", "Description / indication"],
        [["__Self / shower / tub bath__", "For the ambulant patient; the nurse keeps the articles ready, ensures a non-slip floor, a low-height stool and that the door is __not bolted from inside__; stays within call"],
         ["__Assisted bath__", "Patient bathes at the wash basin or in the bathroom with the nurse's help"],
         ["__Bed bath (complete/sponge bath)__", "Given in bed to a helpless, unconscious, very weak, paralysed or post-operative patient"],
         ["__Partial bath__", "Only the face, hands, axillae, back and perineum ('the parts that matter') are washed"],
         ["__Therapeutic / medicated bath__", "Medicated solution added — potassium permanganate (KMnO4 1:5000-1:10 000) for infected skin; sodium bicarbonate/oatmeal/starch for itching; ~sitz bath~ for perineal conditions; cold sponging for hyperpyrexia; emollient bath for dry skin; sulphur/benzyl benzoate applications for scabies"]],
        caption="Table 5.1  Types of baths")
    b.sub("Bed bath — articles required")
    b.text("Two basins/buckets of warm water, mug, soap in a dish, two wash cloths/sponges, two towels (face and body), bath blanket, clean gown/clothes, clean bed linen, comb, nail cutter, oil/moisturiser, talcum powder, mackintosh, screen, kidney tray, paper bag, gloves, linen bag; bedpan and urinal kept ready.")
    b.sub("Bed bath — procedure (sequence is important)")
    b.numbered([
        "Explain the procedure; offer the __bedpan/urinal first__; screen the bed; close windows and switch off the fan; wash hands; collect articles; raise the bed.",
        "Remove the top covers, keeping the patient covered with a __bath blanket__; remove the patient's clothes (remove from the __unaffected/uninjured limb first__ and put on to the affected limb first).",
        "__Face__ — wash the eyes with a soft wet cloth (~no soap~), from the __inner to the outer canthus__, using a separate corner of the cloth for each eye; then the face, ears and neck; dry.",
        "__Upper limbs__ — place a towel under the arm, wash the far arm first with long strokes __from the wrist towards the shoulder (distal to proximal)__, wash the axilla, then the near arm; soak the hands in the basin, clean the nails, dry well between the fingers.",
        "__Chest and abdomen__ — expose, wash, rinse and dry; special attention to __under the breasts and the umbilicus__; observe the skin.",
        "__Lower limbs__ — wash the far leg first from ankle to thigh; flex the knee and place the foot in the basin; clean between the toes; dry thoroughly (important in diabetes).",
        "__Back and buttocks__ — turn the patient to the lateral position; wash, rinse and dry the back and buttocks; give __back care with a gentle massage__ and inspect all pressure points; change the bottom linen at this stage.",
        "__Perineum (genitalia) — last of all__, with fresh water, a separate cloth and gloves; clean __from front to back__ in the female (to prevent faecal contamination of the urethra); in the male retract the foreskin, clean the glans in a circular motion and __replace the foreskin__.",
        "Change the water __whenever it becomes cool, soapy or dirty__ (at least 2-3 times).",
        "Apply oil/moisturiser and powder in the skin folds (~use powder sparingly — caking causes irritation~); comb the hair; cut the nails; dress the patient; make the bed.",
        "Position comfortably, keep the call bell and water within reach, clear and disinfect articles, wash hands, and __record the procedure, the condition of the skin and pressure areas__."
    ])
    b.box("caution", [
        "* __Do not give a bed bath__ immediately after a meal, during severe haemorrhage, in acute myocardial infarction/unstable condition, or when the patient is in severe pain or shock, without the doctor's permission.",
        "* Never leave a helpless patient alone in the bathroom, and never let a bathroom door be bolted from inside.",
        "* Avoid soap on the face and eyes, and on broken or inflamed skin.",
    ])

    b.section_h("5.3", "Care of the Mouth (Oral Hygiene)")
    b.bullets([
        "__Purposes__ — clean, moist, odour-free mouth; prevents __dental caries, gingivitis, stomatitis, halitosis, parotitis, glossitis, oral thrush and aspiration pneumonia__; improves appetite and taste.",
        "The conscious patient brushes __twice daily__ (morning and bedtime) with a soft brush, using the correct technique and flossing; a helpless patient is helped in the __Fowler's/sitting__ position with a kidney tray under the chin.",
        "__Special mouth care__ is required for the unconscious, seriously ill, dehydrated, high fever, NPO, oxygen therapy, post-operative, nasogastric tube, diabetic, cancer/chemotherapy and terminal patient — given __every 2-4 hours__ (2-hourly for the unconscious).",
    ])
    b.sub("Special (unconscious) mouth care — procedure")
    b.numbered([
        "Articles: sterile tray with artery/sponge-holding forceps, gauze swabs, tongue depressor, mouth gag, kidney tray, mouth wash solution, torch, lubricant (soft paraffin/glycerine), suction apparatus, gloves, towel.",
        "Position the patient in the __lateral/side-lying position with the head turned to one side__ and the head of the bed lowered (to prevent aspiration); place a towel and kidney tray.",
        "Keep the mouth open with a gag/tongue depressor; using swabs on forceps (one swab per stroke, discarded after use) clean in order: __teeth (outer then inner surfaces), gums, palate, inner cheeks, tongue and finally the lips__.",
        "__Never put a large amount of fluid__ in the mouth of an unconscious patient; use suction to remove secretions.",
        "Apply a lubricant to the lips; leave the mouth clean; inspect with a torch for ulcers, thrush, bleeding gums and loose teeth.",
        "Clean dentures separately with a brush over a basin of water, store in a labelled container of __plain cold water__ when out of the mouth, and never leave them loose in the bed."
    ])
    b.table(
        ["Mouth wash / agent", "Strength and use"],
        [["Normal saline (0.9%)", "Safest, general cleansing and after surgery"],
         ["Sodium bicarbonate solution", "1 teaspoon in 500 mL water; dissolves thick mucus and sordes"],
         ["Hydrogen peroxide", "Diluted 1:4 or 1:8 with water; loosens sordes and debris (~not for long use — it harms granulating tissue and enamel~)"],
         ["Chlorhexidine gluconate 0.2%", "Antiseptic; prevents plaque, gingivitis and ventilator-associated pneumonia"],
         ["Povidone-iodine gargle 2%", "Sore throat, before oral surgery"],
         ["Potassium permanganate 1:5000-1:8000", "Mild antiseptic gargle"],
         ["Nystatin suspension / clotrimazole", "__Oral thrush (candidiasis)__ — white curd-like patches"],
         ["Glycerine with lemon / soft paraffin / lip balm", "Moistens dry lips (~glycerine alone dries the mucosa, so it is now avoided~)"],
         ["Benzocaine / lignocaine viscous gel", "Painful stomatitis and mucositis"],
         ["Warm saline gargle", "Sore throat, tonsillitis, after tooth extraction"]],
        caption="Table 5.2  Common mouth washes and oral applications")
    b.box("def", ["__Sordes__ — dry, brown-black crusts of dried mucus, food, epithelial cells and bacteria on the teeth, lips and tongue of a dehydrated, febrile or unconscious patient with neglected mouth care. __Halitosis__ = foul breath.  __Stomatitis__ = inflammation of the oral mucosa.  __Parotitis__ (surgical mumps) = infection of the parotid gland from a dry, dirty mouth."])

    b.section_h("5.4", "Care of the Hair")
    b.bullets([
        "Comb and brush the hair __twice daily__; part it in small sections; for tangled hair apply oil, coconut oil or dilute vinegar/conditioner and comb from the ends upwards; plait long hair loosely at the side (not at the back of the head where it presses).",
        "__Bed shampoo__ — done weekly or when needed: articles are a mackintosh with a trough/kelly pad, bucket, jug of warm water (40 °C), shampoo, cotton balls for the ears, pad for the eyes, towels; the patient lies with the head at the edge of the bed, neck supported, the trough draining into the bucket; massage the scalp with the finger tips (not the nails), rinse thoroughly, dry and comb.",
        "__Shaving__ — soften the beard with warm water and soap/cream, shave __in the direction of hair growth__ with short strokes, holding the skin taut; ~take great care in patients on anticoagulants or with bleeding disorders — use an electric razor~.",
        "__Pediculosis (lice)__ — types: ~Pediculus capitis~ (head), ~P. corporis~ (body, vector of __epidemic typhus, relapsing fever and trench fever__) and ~Phthirus pubis~ (pubic, 'crab louse'). Treatment: __permethrin 1% lotion__ (leave 10 min), 5% permethrin cream, malathion 0.5%, or ivermectin; comb out nits (eggs) with a fine __nit comb__ soaked in vinegar; repeat after __7 days__; treat all contacts; boil/hot-iron clothes and bedding, or seal them in a bag for 2 weeks.",
        "__Dandruff__ — ketoconazole or selenium sulphide shampoo; keep the scalp clean.",
    ])

    b.section_h("5.5", "Care of the Eyes, Ears and Nose")
    b.table(
        ["Part", "Care"],
        [["__Eyes__", "Clean with sterile cotton/gauze moistened with normal saline or cool boiled water, wiping __from the inner canthus to the outer canthus__, a separate swab for each eye (~clean the less infected eye first~). For the unconscious patient with an absent blink reflex: instil __artificial tears/methylcellulose drops__, apply an antibiotic eye ointment and close the lids with a pad or tape to prevent __corneal ulcer and exposure keratitis__. Care of spectacles, contact lenses and an artificial eye (remove, clean with saline, store in saline)"],
         ["__Ears__", "Clean only the __outer ear (pinna) and the visible part of the canal__ with a soft cloth; __never insert a bud, pin, matchstick or hairpin__ into the canal. Soften hard wax with warm olive oil/ soda glycerine drops for 2-3 days and let the doctor syringe it with water at body temperature (__37 °C__). Care of a hearing aid — switch off when not in use, keep dry, check the battery"],
         ["__Nose__", "Clean with a moist cotton swab or a cotton applicator moistened with saline; __do not go deep__. Soften dried secretions with saline drops. For a patient with a nasogastric or oxygen tube, clean the nostril and change the tape daily and observe for pressure sores at the nostril. Teach the patient to blow the nose gently with __both nostrils open__"]],
        caption="Table 5.3  Care of the eyes, ears and nose")

    b.section_h("5.6", "Care of Hands, Feet and Nails")
    b.bullets([
        "Soak the hands in warm soapy water for 5-10 minutes (feet 10-20 min) to soften the nails; clean under the free edge; __cut the finger nails in a curve and the toe nails straight across__; file the edges; avoid injury to the cuticle.",
        "Dry well __between the toes__; apply moisturiser to the soles and heels but __not between the toes__; cotton socks; well-fitting footwear.",
        "__Diabetic foot care__ (very high yield) — inspect the feet daily (use a mirror), wash with lukewarm water and __test the temperature with the elbow__ (because of neuropathy), never walk barefoot, never use hot water bottles or corn-removing plasters, __never cut corns or nails too short__ (get a podiatrist/nurse to do it), report any blister, ulcer, colour change or numbness at once; control blood sugar.",
        "Look for __fungal infection (tinea pedis)__, ingrowing toe nail, callosities, corns, cracks and oedema.",
    ])

    b.section_h("5.7", "Back Care (Pressure Area Care)")
    b.numbered([
        "Given __after the bath and every 2-4 hours__, and after each episode of incontinence, to all bedridden patients.",
        "Articles: warm water, soap, towel, moisturising lotion/oil, talcum powder, gloves, clean linen.",
        "Turn the patient to the lateral or prone position; expose only the back; wash, rinse and pat dry.",
        "Pour a little lotion in the palm, warm it, and massage the back with __long, firm, upward strokes from the buttocks to the shoulders__ and circular strokes over the shoulders for __3-5 minutes__ — techniques: ~effleurage (long stroking), petrissage (kneading), tapotement (tapping)~.",
        "Inspect all pressure points for redness; __do not massage over a reddened or broken area__; do not use spirit (drying) or hot water.",
        "Change position, straighten the linen, and record the condition of the skin."
    ])

    b.section_h("5.8", "Meeting Elimination Needs")
    b.sub("Giving the bedpan and urinal")
    b.bullets([
        "Warm the bedpan (rinse with warm water), dry it, and __powder the rim__ (do not powder if a specimen is needed); cover it while carrying.",
        "Screen the bed, wear gloves; flex the patient's knees, ask him to raise the hips (or turn him to the side and roll the pan into place); place a mackintosh under the buttocks.",
        "Raise the head end slightly to give a __near-normal squatting position__; leave the toilet paper, call bell and water within reach and __give privacy__ — but never leave a weak patient alone for long.",
        "Afterwards: clean the perineum from __front to back__, remove the pan covered, give water to wash the hands, ventilate the room.",
        "__Observe and record__ the amount, colour, consistency, odour and abnormal contents (blood, mucus, pus, worms, undigested food) of stool and urine before disposal; measure the urine if an output chart is being kept; send a specimen if ordered.",
        "Clean and disinfect the bedpan/urinal after each use; each patient should have his own.",
        "A __fracture pan__ (with a shallow flat end) is used for patients in traction, after hip surgery or with a spinal injury; a __commode chair__ for those who can sit out of bed.",
    ])
    b.sub("Perineal care (vulval/genital toilet)")
    b.bullets([
        "Indicated after childbirth, after perineal surgery, with an indwelling catheter, in incontinence, vaginal discharge and for the unconscious patient — given __twice daily and after each soiling__.",
        "Position: dorsal recumbent with knees flexed (female) / supine (male); mackintosh and bedpan under the buttocks; sterile swabs and warm antiseptic solution (savlon/normal saline) poured from a jug.",
        "Clean __from above downwards and from the centre outwards, from the cleanest to the dirtiest area__: labia majora, labia minora, urethral meatus, vaginal orifice, then the perineum and anus __last__; use one swab for one stroke and discard it; __never wipe from the anus towards the vagina__.",
        "Dry, apply the prescribed ointment or a sterile pad, and record any discharge, swelling, redness or stitch line condition.",
    ])
    b.sub("Care of the incontinent patient")
    b.bullets([
        "__Types__ — stress, urge, overflow, functional, total incontinence; faecal incontinence.",
        "Keep the skin __clean, dry and protected__ with a barrier cream (zinc oxide, dimethicone); change pads/diapers frequently; never leave the patient on wet linen.",
        "Offer the bedpan/urinal __2-hourly (timed voiding)__; establish a __bladder and bowel training programme__ (fixed times, pelvic floor/__Kegel exercises__, fluid 1.5-2 L in the day but restricted 2 hours before bed, avoid caffeine).",
        "Use a condom (Uridom) drainage for men; an __indwelling catheter only as a last resort__ (infection risk).",
        "Prevent __pressure sores, urinary tract infection and dermatitis__; protect the patient's dignity — never scold or shame him.",
    ])
    b.sub("Constipation and its management")
    b.bullets([
        "__Causes in bed patients__ — immobility, low-fibre diet, inadequate fluid, ignoring the urge, lack of privacy, opioids/anticholinergics/iron/antacids (aluminium), painful piles, depression, hypothyroidism, dehydration.",
        "__Management__ — high-fibre diet (whole grains, fruit, vegetables), 2-3 L of fluid, warm drinks in the morning, exercise, privacy and a regular time, sitting position; then bulk laxative (isabgol/psyllium), osmotic (lactulose, milk of magnesia, PEG), stimulant (bisacodyl, senna), stool softener (liquid paraffin, docusate), glycerine suppository, and lastly an __enema__ or manual evacuation of __faecal impaction__.",
        "__Never give a laxative__ in undiagnosed abdominal pain, suspected appendicitis, or intestinal obstruction.",
    ])

    b.section_h("5.9", "Care of Vomiting, Expectoration and Dressing the Patient")
    b.bullets([
        "__Vomiting__ — turn the head to the __side__ (prevent aspiration), support the head, hold the kidney tray, loosen tight clothes, give mouth wash afterwards, ventilate the room, remove the vomitus at once; __observe and record__ the amount, colour (bile-stained, 'coffee ground' = old blood, faecal = intestinal obstruction), content, smell, force (projectile), relation to food and any accompanying pain; preserve a sample if poisoning is suspected.",
        "__Sputum__ — a __covered sputum cup__ with a disinfectant or paper lining is kept, emptied and disinfected 2-3 times a day; teach the patient to __cough covering the mouth__ and never to spit on the floor; record the amount, colour, consistency and odour (rusty in pneumonia, copious foul in bronchiectasis/abscess, blood-stained in TB/cancer, pink frothy in pulmonary oedema).",
        "__Changing the patient's clothes__ — remove the garment from the __unaffected arm first__ and put it on the __affected (or IV) arm first__; for a patient with an IV line, thread the bottle and tubing through the sleeve without disconnecting; keep the patient covered; use front-open gowns for the helpless.",
        "__Care of linen__ — remove soiled linen at once, do not shake, carry it away from the uniform, soak blood/faecal-stained linen in cold water first (hot water fixes protein stains), then wash with hot soapy water; boil/soak infected linen in disinfectant; dry in the sun.",
    ])

    b.box("recap", [
        "* Bed bath water 40-46 °C; sequence: face (eyes inner→outer canthus, no soap) → arms (distal to proximal) → chest/abdomen → legs → back (back care) → __perineum last__; change water 2-3 times.",
        "* Special mouth care 2-hourly for the unconscious, in the lateral position with the head turned; clean teeth→gums→palate→cheeks→tongue→lips; sordes = crusts of neglect.",
        "* Eyes of the unconscious: artificial tears + closure to prevent corneal ulcer; never insert anything in the ear canal.",
        "* Finger nails cut curved, toe nails straight; diabetic foot — never barefoot, never hot water, test with the elbow.",
        "* Back care 2-4 hourly with long upward strokes; never massage a reddened bony prominence.",
        "* Perineal care: front to back, centre outwards, one swab one stroke, anus last.",
        "* Pediculosis: permethrin 1%, repeat after 7 days; body louse transmits epidemic typhus.",
        "* Vomiting: head to one side; observe colour — coffee ground = bleeding, faecal = obstruction.",
    ])
