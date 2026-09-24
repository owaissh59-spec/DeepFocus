"""Chapters 14-17 : Immunity & Infectious Diseases, Care of the Aged and
Long-term Patient, Care of the Mentally Ill Patient, Special Drugs."""


def chapter_14(b):
    b.chapter(14, "Immunity and Infectious Diseases",
              "Types of immunity, vaccines and the cold chain, immunisation schedule, and disease-wise profiles")

    b.section_h("14.1", "Immunity — Definition and Types")
    b.box("def", ["__Immunity__ — the ability of the body to resist or overcome infection or the effects of a toxin. It is provided by the immune system through non-specific (innate) and specific (acquired) mechanisms."])
    b.table(
        ["Type", "Sub-type", "How acquired", "Examples", "Onset & duration"],
        [["__Innate (natural / non-specific) immunity__", "Present from birth; no memory",
          "Barriers — intact skin, mucus and cilia, tears (lysozyme), gastric acid, normal flora, cough reflex; cells — neutrophils, macrophages, NK cells; chemicals — complement, interferon, inflammation, fever",
          "Species, racial and individual resistance", "Immediate; lifelong but non-specific"],
         ["__Acquired — active — natural__", "Body makes its own antibodies", "After __suffering from the disease__ (clinical or subclinical infection)",
          "Measles, chickenpox, mumps, typhoid", "Slow onset (days-weeks); __long-lasting, often lifelong__; has memory"],
         ["__Acquired — active — artificial__", "Body makes its own antibodies after a vaccine",
          "__Vaccination__ — live attenuated, killed, toxoid, subunit, mRNA", "BCG, OPV, measles, DPT, hepatitis B",
          "Slow onset; long-lasting (may need boosters)"],
         ["__Acquired — passive — natural__", "Ready-made antibodies received",
          "__Mother to child__ — IgG across the placenta, IgA in colostrum and breast milk",
          "Protection of the newborn for the first 3-6 months", "__Immediate__; temporary (weeks-months)"],
         ["__Acquired — passive — artificial__", "Ready-made antibodies injected",
          "__Antiserum, immunoglobulin or antitoxin__ — ATS/TIG, anti-rabies immunoglobulin, anti-snake venom, anti-D, HBIG, convalescent plasma",
          "Used when immediate protection is needed or the person is already exposed",
          "__Immediate__; short lived (2-3 weeks); risk of serum sickness/anaphylaxis"],
         ["__Herd (community) immunity__", "Protection of the whole community",
          "When a large proportion (usually __80-95%__) is immune, transmission stops and even the unimmunised are protected",
          "Measles needs about 95%, polio about 80-85% coverage", "Depends on coverage being maintained"]],
        caption="Table 14.1  Types of immunity — a very frequently asked table")
    b.box("hy", [
        "__Active immunity__ = the body works (slow, long lasting, has memory, given ~before~ exposure).  __Passive immunity__ = ready-made antibodies (immediate, short lasting, no memory, given ~after~ exposure or when there is no time to wait).",
        "__Combined (simultaneous) active and passive immunisation__ is given in: __tetanus-prone wounds (TT/Td + TIG), rabies (vaccine + RIG), hepatitis B needle-stick (vaccine + HBIG), and diphtheria__.",
        "__Immunoglobulins__: __IgG__ — most abundant (about 75%), the only one crossing the placenta; __IgA__ — secretory, in milk/tears/saliva/mucosa; __IgM__ — largest ('millionaire'), the __first antibody produced__ in an infection and a marker of __recent/acute infection__; __IgE__ — allergy and helminth infection; __IgD__ — on B-cell surfaces.",
    ])

    b.section_h("14.2", "Vaccines")
    b.table(
        ["Class of vaccine", "Examples", "Points"],
        [["__Live attenuated__", "__BCG, OPV, measles, MMR, rotavirus, varicella, yellow fever, oral typhoid, JE (live), intranasal influenza__",
          "Give a strong, long-lasting immunity, often with a single dose; __contraindicated in pregnancy and immunodeficiency (HIV with low CD4, leukaemia, steroids, chemotherapy)__; heat and light sensitive; two live vaccines are given either on the same day or at least 4 weeks apart"],
         ["__Killed / inactivated (whole organism)__", "__IPV (injectable polio), whole-cell pertussis, rabies, hepatitis A, cholera (oral killed), JE (inactivated), influenza, typhoid (Vi killed)__",
          "Safer but weaker — need __multiple doses and boosters__ and usually an adjuvant"],
         ["__Toxoid__", "__Tetanus toxoid, diphtheria toxoid__ (in DPT/DT/Td)", "Modified, harmless toxin; needs boosters; adsorbed on alum → __never freeze__"],
         ["__Subunit / polysaccharide / conjugate / recombinant__", "__Hepatitis B (recombinant DNA), HPV, Hib, pneumococcal (PCV), meningococcal, acellular pertussis, typhoid Vi conjugate__",
          "Very safe and purified; conjugation to a protein makes them effective in infants under 2 years"],
         ["__Viral vector and mRNA (new generation)__", "Covishield/ChAdOx (vector), Covaxin (inactivated), Comirnaty and Spikevax (mRNA)",
          "mRNA vaccines need ultra-cold storage (−20 to −70 °C)"]],
        caption="Table 14.2  Classification of vaccines")

    b.section_h("14.3", "The Cold Chain")
    b.bullets([
        "__Cold chain__ — the system of storing and transporting vaccines at the recommended low temperature from the manufacturer to the point of use.",
        "__Storage temperatures__ — __walk-in cooler and ILR (Ice-Lined Refrigerator): +2 to +8 °C__; __deep freezer: −15 to −25 °C__ (for OPV and measles at the district and state level); __vaccine carrier and day carrier: with ice packs, for 1-2 days of field use__.",
        "In an ILR the __top shelf/basket holds the most heat-sensitive vaccines (OPV, measles, BCG)__ and the lower part holds __DPT, TT, Td, hepatitis B, PCV and diluents__ (which must ~never be frozen~).",
        "__Most heat-sensitive vaccine: OPV__ (then measles and BCG).  __Most sensitive to freezing: hepatitis B, DPT, TT/Td, PCV and IPV (adsorbed/ liquid vaccines)__.",
        "__Vaccine vial monitor (VVM)__ — a heat-sensitive square on the label: use while the __inner square is lighter than the outer circle (stages 1 and 2)__; __discard at stage 3 or 4__ (inner square the same colour as or darker than the circle).",
        "__Shake test__ — used on a suspected frozen adsorbed vaccine (DPT/TT/hepatitis B): if it shows rapid sedimentation with flakes compared with a control vial, it has been frozen and __must be discarded__.",
        "__Open vial policy__ — opened multi-dose vials of __OPV, DPT, TT/Td, hepatitis B and IPV may be used for up to 28 days__ if the VVM is usable, the expiry date has not passed, the septum is not submerged in water, and aseptic technique was used; but __BCG, measles/MR, JE and rotavirus (reconstituted or without preservative) must be discarded within 4 hours__ of opening/reconstitution.",
        "Reconstitute only with the __matching diluent of the same manufacturer, cooled to the same temperature__; never store a reconstituted vaccine overnight.",
        "Never keep vaccines in the __refrigerator door__; keep a thermometer inside and maintain a __twice-daily temperature record__; do not store food, drugs or specimens with vaccines.",
    ])

    b.section_h("14.4", "National Immunization Schedule (India, UIP)")
    b.table(
        ["Age", "Vaccine", "Dose, route and site"],
        [["__At birth__ (within 24 h for hep B; BCG and OPV-0 up to 1 year/15 days)",
          "__BCG, OPV-0 (zero dose), Hepatitis B birth dose__",
          "BCG __0.05 mL (under 1 month) / 0.1 mL, intradermal, left upper arm__; OPV 2 drops oral; Hep B 0.5 mL IM antero-lateral thigh"],
         ["__6 weeks__", "OPV-1, __Pentavalent-1 (DPT + hepatitis B + Hib)__, Rotavirus-1, __fIPV-1__, PCV-1",
          "OPV oral; Pentavalent 0.5 mL IM left thigh; Rotavirus 5 drops oral; fIPV 0.1 mL __intradermal right upper arm__; PCV 0.5 mL IM right thigh"],
         ["__10 weeks__", "OPV-2, Pentavalent-2, Rotavirus-2", "As above"],
         ["__14 weeks__", "OPV-3, Pentavalent-3, Rotavirus-3, __fIPV-2__, PCV-2", "As above"],
         ["__9-12 months__", "__Measles-Rubella (MR)-1__, JE-1 (in endemic districts), PCV-booster, __Vitamin A 1st dose (1 mL = 1 lakh IU)__",
          "MR 0.5 mL __subcutaneous, right upper arm__; JE SC left upper arm"],
         ["__16-24 months__", "__MR-2, DPT booster-1, OPV booster, JE-2__, Vitamin A 2nd dose (2 mL = 2 lakh IU)",
          "DPT 0.5 mL IM left upper arm; MR SC right upper arm"],
         ["__5-6 years__", "__DPT booster-2__", "0.5 mL IM left upper arm"],
         ["__10 years and 16 years__", "__Td (Tetanus-diphtheria)__", "0.5 mL IM upper arm"],
         ["__Pregnant woman__", "__Td-1 early in pregnancy, Td-2 four weeks later, Td booster__ if the last dose was within 3 years",
          "0.5 mL IM upper arm"],
         ["__Vitamin A__", "9 doses in all — 1st at 9 months, then every 6 months up to 5 years", "1 lakh IU at 9 months, then 2 lakh IU orally"]],
        caption="Table 14.3  National Immunization Schedule")
    b.box("num", [
        "__BCG__ — Bacillus Calmette-Guerin, ~Mycobacterium bovis~ (attenuated 'Danish 1331' strain); diluent __normal saline__; gives a __papule → ulcer → scar in 6-12 weeks__; no dressing or antiseptic on the site.",
        "__Measles and MR__ vaccine is reconstituted with __distilled/sterile water__ and given __subcutaneously__; discard within 4 hours.",
        "__Vitamin A__ — 1 lakh IU at 9 months; 2 lakh IU every 6 months up to 5 years (total 9 doses).",
        "__AEFI__ (adverse event following immunisation) must be reported — minor (fever, local pain, swelling), severe or serious (anaphylaxis, seizure, abscess, toxic shock); keep __adrenaline ready__ at every session and observe for 30 minutes.",
        "Immunisation programme milestones: __EPI 1974 (WHO) → EPI India 1978 → Universal Immunization Programme (UIP) 1985 → Mission Indradhanush 2014 → Intensified Mission Indradhanush__; India was declared __polio-free on 27 March 2014__; __smallpox eradicated globally in 1980__ (last natural case in India 1975); __maternal and neonatal tetanus eliminated in India in 2015__.",
    ])

    b.section_h("14.5", "Infectious Diseases — Comparative Profiles")
    b.table(
        ["Disease & agent", "Incubation period", "Mode of spread", "Main features", "Prevention / treatment"],
        [["__Measles__ (~Measles/rubeola virus~)", "10-14 days (rash on day 14)", "Droplet, airborne (highly infectious)",
          "Fever, cough, coryza, conjunctivitis (the 3 C's), __Koplik's spots__ (pathognomonic, on the buccal mucosa), then a maculopapular rash starting __behind the ears/hairline and spreading downwards__, with staining on fading",
          "__MR vaccine__; vitamin A; isolate 4 days before to 5 days after the rash; complications — pneumonia (commonest cause of death), otitis media, diarrhoea, blindness, SSPE, encephalitis"],
         ["__Chickenpox (varicella)__ (~Varicella-zoster virus~)", "14-16 days (10-21)", "Droplet, airborne, contact with vesicle fluid",
          "Mild fever then a __centripetal (trunk first) rash__, all stages present together (__pleomorphic__): macule → papule → vesicle → pustule → crust; ~dew-drop on a rose petal~ appearance; intense itching",
          "Varicella vaccine; infectious __1-2 days before the rash until all lesions crust (about 6 days)__; acyclovir for the severe/immunocompromised; ~herpes zoster (shingles) is a reactivation~"],
         ["__Mumps__ (~Mumps virus~)", "14-18 days", "Droplet, saliva", "Painful swelling of the __parotid gland(s)__, fever, pain on chewing; complications — orchitis (sterility), meningitis, pancreatitis, deafness",
          "MMR vaccine; isolate until the swelling subsides; symptomatic treatment, soft bland food, no sour food"],
         ["__Rubella (German measles)__", "14-21 days", "Droplet, transplacental", "Mild fever, fine pink rash, __posterior auricular and occipital lymphadenopathy__; __in the 1st trimester causes congenital rubella syndrome — cataract, deafness, heart defect__",
          "__MR/MMR vaccine; avoid pregnancy for 1 month after the vaccine__; keep away from pregnant women"],
         ["__Diphtheria__ (~Corynebacterium diphtheriae~)", "2-5 days", "Droplet, contact, fomites, infected milk",
          "Sore throat with a __grey-white adherent pseudo-membrane__ that bleeds on removal, bull neck, toxin causing __myocarditis and neuritis__, respiratory obstruction",
          "__DPT/Td; treatment: antitoxin (ADS) at once + penicillin/erythromycin__; strict isolation and bed rest; __Schick test__ (historical) for susceptibility"],
         ["__Whooping cough (pertussis)__ (~Bordetella pertussis~)", "7-14 days", "Droplet",
          "Catarrhal stage (most infectious) → __paroxysmal stage with bouts of coughing ending in an inspiratory 'whoop' and vomiting__ → convalescence; may last 6-10 weeks ('the 100-day cough'); lymphocytosis",
          "DPT/pentavalent; erythromycin/azithromycin; small frequent feeds after a bout; avoid dust and smoke"],
         ["__Tetanus (lockjaw)__ (~Clostridium tetani~ toxin)", "6-10 days (3-21; ~shorter = worse prognosis~)",
          "Spores from soil/dust/manure entering a wound; unclean delivery and cord cutting (neonatal tetanus)",
          "__Trismus (lockjaw), risus sardonicus, neck and back stiffness, opisthotonus, board-like abdomen, painful generalised spasms provoked by light, noise and touch__, with a fully conscious patient",
          "__Td/TT immunisation, 5 cleans at delivery, wound toilet, TIG/ATS__; treatment in a __dark, quiet room__ with diazepam/muscle relaxants, metronidazole, ventilation; ~one attack gives no immunity~"],
         ["__Poliomyelitis__ (~Poliovirus 1, 2, 3~)", "7-14 days (3-35)", "__Faeco-oral__ (and droplet)",
          "Fever, headache, then __asymmetrical flaccid paralysis with no sensory loss__, commonly of the leg; the vast majority of infections are subclinical",
          "__OPV and IPV; AFP surveillance of every case under 15 years__; no specific treatment — physiotherapy, splints, prevention of deformity"],
         ["__Tuberculosis__ (~Mycobacterium tuberculosis~)", "__4-12 weeks__ to develop a lesion (years to disease)", "__Airborne droplet nuclei__ (an untreated case infects 10-15 persons a year)",
          "__Cough over 2 weeks, evening rise of temperature, night sweats, loss of weight and appetite, haemoptysis__, chest pain; extra-pulmonary forms — lymph node, spine, meninges, abdomen",
          "__BCG; sputum microscopy/NAAT (CBNAAT); DOTS — 2 months intensive (HRZE) + 4 months continuation (HRE) under the NTEP__; isolate/ventilate, cough etiquette, contact tracing, nutrition support (Ni-kshay Poshan Yojana)"],
         ["__Typhoid (enteric fever)__ (~Salmonella typhi~)", "__10-14 days__ (7-21)", "Faeco-oral — contaminated water, food, milk, flies; carriers (gall bladder)",
          "__Step-ladder fever__ with a relative bradycardia, headache, coated tongue, __rose spots__ on the abdomen (2nd week), splenomegaly, constipation then pea-soup diarrhoea; complications in the __3rd week — intestinal perforation and haemorrhage__",
          "__Typhoid Vi/conjugate vaccine__, safe water and food, sanitation, handwashing; __blood culture (1st week), Widal test (2nd week), stool culture (3rd week)__; ceftriaxone/azithromycin; absolute bed rest and a soft low-fibre diet"],
         ["__Cholera__ (~Vibrio cholerae~ O1 El Tor/O139)", "__Hours to 5 days__ (usually 1-2)", "Faeco-oral — contaminated water and food",
          "__Sudden profuse painless 'rice-water' stools with fishy odour__ and effortless vomiting → rapid severe dehydration, muscle cramps, washerwoman's hands, sunken eyes, anuria, shock",
          "__ORS is the mainstay + IV Ringer lactate in severe cases__; doxycycline/azithromycin shortens shedding; safe water, chlorination, sanitation, oral cholera vaccine; __notifiable__"],
         ["__Bacillary dysentery / amoebiasis__", "1-7 days / 2-4 weeks", "Faeco-oral",
          "Frequent small stools with __blood and mucus, tenesmus and colic__; amoebic — gradual, with liver abscess possible",
          "ORS, ciprofloxacin (shigella), __metronidazole for amoebiasis__; hand washing, safe water and food"],
         ["__Hepatitis A and E__", "A: 15-45 days (about 4 weeks); E: 2-9 weeks", "__Faeco-oral__ (E often water-borne epidemics)",
          "Prodromal fever, anorexia, nausea, distaste for smoking, then __jaundice with dark urine and pale stools__, tender hepatomegaly; __hepatitis E is dangerous in pregnancy (up to 20% mortality)__",
          "Safe water and food, hand hygiene; __hepatitis A vaccine__; rest, no alcohol, no fatty food; ~no specific antiviral~"],
         ["__Hepatitis B and C__", "B: 45-180 days (2-6 months); C: 2 weeks-6 months", "__Blood, sharps, unsafe injections, transfusion, sexual contact, mother to child__",
          "May be asymptomatic; jaundice, and __chronic infection → cirrhosis and hepatocellular carcinoma__",
          "__Hepatitis B vaccine (0, 1, 6 months) and HBIG after exposure; screening of blood; safe injections and universal precautions__; antivirals (tenofovir; direct-acting antivirals cure hepatitis C)"],
         ["__HIV / AIDS__ (~Human immunodeficiency virus~)", "Weeks (seroconversion 3-12 weeks); AIDS after __7-10 years__",
          "__Sexual contact (the commonest, 80-85%), blood and blood products, contaminated needles, mother to child (in utero, at birth, breast milk)__; ~not by touch, air, food, water, insects, sharing utensils or swimming~",
          "Acute flu-like illness → long asymptomatic phase → weight loss, chronic fever and diarrhoea, oral thrush, herpes zoster, tuberculosis, ~Pneumocystis~ pneumonia, Kaposi's sarcoma; CD4 falls (__AIDS when CD4 under 200/mm3__)",
          "__ART for all (test and treat), universal precautions, safe blood, condoms, PPTCT/PMTCT with ART in pregnancy, PEP and PrEP__; counselling and confidentiality (~ICTC~); NACO programme"],
         ["__Malaria__ (~Plasmodium vivax, falciparum, malariae, ovale, knowlesi~)", "P. vivax 12-17 days; P. falciparum 9-14 days",
          "Bite of an infected __female Anopheles__ mosquito (night biter); also transfusion and transplacental",
          "__Paroxysms of cold stage (rigor) → hot stage → sweating stage__, splenomegaly, anaemia; __P. falciparum causes cerebral malaria, renal failure and black-water fever (the dangerous species)__",
          "__Blood smear/rapid diagnostic test__; treatment as per the National Drug Policy (chloroquine for vivax + primaquine 14 days; __ACT — artemisinin combination therapy for falciparum__ + single-dose primaquine); prevention — insecticide-treated bed nets, indoor residual spraying, source reduction, larvicides, ~Gambusia~ fish"],
         ["__Dengue__ (~Dengue virus 1-4~)", "4-10 days (3-14)", "__Aedes aegypti__ — a __day-biting__ mosquito breeding in clean stored water (coolers, tyres, flower pots)",
          "Sudden high fever, severe __retro-orbital headache, muscle and joint pain ('break-bone fever')__, rash, positive tourniquet test; __warning signs__ — severe abdominal pain, persistent vomiting, bleeding, restlessness, __falling platelet count with rising haematocrit__ (dengue haemorrhagic fever/shock syndrome)",
          "__No specific treatment — fluids and paracetamol only; AVOID aspirin, NSAIDs and IM injections__ (bleeding risk); source reduction, personal protection; monitor platelets and haematocrit"],
         ["__Chikungunya / Zika__", "3-7 days / 3-14 days", "~Aedes~ mosquito", "Chikungunya: fever with __severe prolonged joint pain__; Zika: mild illness but causes __microcephaly__ in the fetus",
          "Symptomatic; vector control; Zika — avoid pregnancy/travel advisory"],
         ["__Filariasis__ (~Wuchereria bancrofti~)", "8-16 months", "__Culex quinquefasciatus__ mosquito (breeds in dirty water)",
          "Recurrent fever with lymphangitis and lymphadenitis, __elephantiasis of the legs, scrotum and breast, hydrocele, chyluria__; ~night blood smear~ for microfilariae",
          "__Mass drug administration — DEC + albendazole (with ivermectin in triple therapy)__; limb hygiene and elevation, vector control"],
         ["__Kala-azar (visceral leishmaniasis)__", "2-6 months", "Bite of the __female Phlebotomus (sandfly)__ breeding in cracks of mud walls",
          "Prolonged fever with a double rise, gross __splenomegaly__ and hepatomegaly, darkening of the skin, wasting, pancytopenia",
          "__Liposomal amphotericin B (single dose) / miltefosine__; indoor residual spraying, plastering of cracks"],
         ["__Rabies__ (~Rabies virus~)", "__1-3 months__ (4 days to years; shorter with bites on the face and hands)",
          "__Bite, scratch or lick on broken skin by a rabid dog, cat, monkey, bat, mongoose, jackal__ (saliva)",
          "Prodrome with pain/tingling at the bite site, then __hydrophobia, aerophobia, hypersalivation, agitation, spasms of the throat__ (furious) or paralysis (dumb); __100% fatal once symptoms appear__",
          "__Immediate wound washing with soap and running water for 15 minutes__, then povidone-iodine; __anti-rabies vaccine (0, 3, 7, 14, 28 days IM, or intradermal schedule) + rabies immunoglobulin infiltrated around the wound for category III__; never suture tightly; pre-exposure vaccination for those at risk; ~animal is observed for 10 days~"],
         ["__Scabies / Pediculosis__", "2-6 weeks (scabies)", "Close personal contact, shared clothes and bedding",
          "Intense __night itching__ with burrows in the finger webs, wrists, axillae, groin and genitals; family members affected",
          "__Permethrin 5% cream__ (whole body below the neck, overnight, repeat after 7 days) or ivermectin; __treat all family members at the same time__ and wash/sun all clothes and bedding"],
         ["__Leprosy (Hansen's disease)__ (~M. leprae~)", "__2-5 years__ (up to 20)", "Prolonged close contact, droplets from the nose of untreated multibacillary cases",
          "__Hypopigmented or erythematous patch with loss of sensation__, thickened nerves, nodules, claw hand, foot drop, trophic ulcers, loss of eyebrows",
          "__Multidrug therapy (MDT) — rifampicin, dapsone (+ clofazimine for MB)__; free under the NLEP; disability care and no stigma — ~a patient becomes non-infectious within days of starting MDT~"],
         ["__Influenza / COVID-19__", "Influenza 1-4 days; COVID-19 2-14 days (median 5)", "Droplet, aerosol, contact",
          "Fever, cough, sore throat, myalgia; COVID-19 — loss of smell and taste, breathlessness, hypoxia, ARDS",
          "__Annual influenza vaccine, COVID-19 vaccine, mask, hand hygiene, distancing, ventilation__; oseltamivir for influenza; oxygen and steroids for severe COVID-19"],
         ["__Plague__ (~Yersinia pestis~)", "Bubonic 2-7 days; pneumonic 1-4 days", "__Rat flea (Xenopsylla cheopis)__ bite; pneumonic by droplet",
          "Bubonic — fever with a very painful __bubo__ (lymph node); pneumonic — fulminant pneumonia, highly fatal and highly contagious",
          "__Notifiable internationally__; streptomycin/doxycycline; rat and flea control, insecticide before rodenticide"],
         ["__Tetanus neonatorum / Ophthalmia neonatorum__", "3-14 days / 2-5 days", "Unclean cord care / infected birth canal (gonococcus, chlamydia)",
          "Refusal to suck, stiffness and spasms / purulent eye discharge in the newborn",
          "5 cleans, Td in pregnancy / eye toilet and antibiotic eye drops at birth"]],
        caption="Table 14.4  Infectious diseases at a glance (learn incubation periods and modes of spread)")

    b.section_h("14.6", "Isolation, Quarantine, Notification and Disinfection")
    b.bullets([
        "__Isolation__ — separation of an __infected__ person for the __period of communicability__; __quarantine__ — limitation of the movement of an apparently __healthy contact__ for the __longest incubation period__ of the disease.",
        "__Notifiable diseases (India, varies by State)__ — cholera, plague, yellow fever (internationally notifiable under the IHR), plus tuberculosis, HIV/AIDS, malaria, dengue, chikungunya, kala-azar, leprosy, measles, diphtheria, whooping cough, tetanus, polio/AFP, viral hepatitis, meningitis, rabies, typhoid, food poisoning, Japanese encephalitis, COVID-19; also maternal and infant deaths. Reporting is a __legal duty__ of the health worker (Form-P/IDSP reporting).",
        "__Disinfection__ — concurrent during illness and terminal after recovery (Chapter 3); the excreta of enteric fever, cholera, dysentery and hepatitis A must be disinfected before disposal.",
        "__Contacts__ — identify, examine, give chemoprophylaxis or vaccine where indicated (rifampicin for meningococcal and leprosy contacts, azithromycin for pertussis contacts, immunoglobulin for measles/hepatitis A contacts), and educate them about the early signs.",
        "__Surveillance__ — IDSP (Integrated Disease Surveillance Programme) weekly reporting of S, P and L forms; outbreak investigation; AFP and measles surveillance.",
    ])

    b.box("recap", [
        "* Active immunity = slow, long-lasting, has memory (disease/vaccine); passive = immediate, short-lived (maternal antibody, immunoglobulin, antitoxin).",
        "* IgG crosses the placenta and is the most abundant; IgM is the first formed and indicates recent infection; IgA is in breast milk.",
        "* Live vaccines: BCG, OPV, measles/MR, MMR, rotavirus, varicella, yellow fever — contraindicated in pregnancy and immunodeficiency.",
        "* Cold chain 2-8 °C (ILR); deep freezer −15 to −25 °C for OPV/measles; never freeze DPT, TT, hepatitis B, PCV, IPV; discard at VVM stage 3/4; shake test for a frozen vaccine.",
        "* Open vial policy: OPV, DPT, TT, hepatitis B, IPV = 28 days; BCG, measles/MR, JE, rotavirus = 4 hours.",
        "* BCG: 0.05/0.1 mL intradermal, left upper arm, saline diluent. Measles/MR: 0.5 mL subcutaneous, right upper arm.",
        "* Incubation: measles 10-14 d, chickenpox 14-16 d, mumps 14-18 d, rubella 14-21 d, diphtheria 2-5 d, pertussis 7-14 d, tetanus 6-10 d, polio 7-14 d, typhoid 10-14 d, cholera 1-2 d, hepatitis A 2-6 wk, hepatitis B 2-6 months, rabies 1-3 months, leprosy 2-5 years.",
        "* Koplik's spots = measles; pseudomembrane = diphtheria; rose spots and step-ladder fever = typhoid; rice-water stools = cholera; hydrophobia = rabies; night itching = scabies.",
        "* Dengue: no aspirin/NSAIDs/IM injections; Aedes bites by day; malaria — Anopheles bites at night.",
    ])



def chapter_15(b):
    b.chapter(15, "Care of the Aged and the Long-Term Patient",
              "Ageing changes, geriatric problems, prevention of complications, rehabilitation and palliative care")

    b.section_h("15.1", "Basic Concepts")
    b.table(
        ["Term", "Meaning"],
        [["__Geriatrics__", "The branch of medicine dealing with the diseases and care of old age"],
         ["__Gerontology__", "The scientific study of the process and problems of ageing (biological, psychological and social)"],
         ["__Elderly / Senior citizen (India)__", "A person aged __60 years and above__ (WHO also uses 60+; 'old old' 75-84, 'oldest old' 85+)"],
         ["__Senescence__", "The normal process of growing old"],
         ["__Long-term (chronic) patient__", "A patient needing care for more than 3 months — paralysis, arthritis, dementia, cancer, chronic kidney/lung disease"],
         ["__Rehabilitation__", "Restoring a disabled person to the fullest physical, mental, social and vocational usefulness of which he is capable"],
         ["__Palliative care__", "Active total care of a patient whose disease is not curable, aimed at the best possible quality of life for the patient and family"],
         ["__Activities of daily living (ADL)__", "Bathing, dressing, toileting, transferring, continence, feeding (assessed by the __Katz index/Barthel index__)"]],
        caption="Table 15.1  Terms in geriatric nursing")

    b.section_h("15.2", "Physiological Changes of Ageing (system-wise)")
    b.table(
        ["System", "Changes with age", "Nursing implication"],
        [["__Skin and hair__", "Thin, dry, inelastic, wrinkled skin; loss of subcutaneous fat; fragile capillaries (easy bruising); grey, thin hair; brittle nails; reduced sweating",
          "Gentle handling, moisturiser, avoid strong soap and hot water, protect from pressure and from injury, watch for pressure sores and hypothermia"],
         ["__Musculoskeletal__", "Loss of muscle mass and strength (sarcopenia), __osteoporosis__ (especially after menopause), thinning discs and loss of height, stiff joints, kyphosis, osteoarthritis",
          "__High risk of fracture (neck of femur, wrist, vertebra) from a minor fall__; calcium, vitamin D, protein, weight-bearing exercise, fall prevention"],
         ["__Nervous system__", "Fewer neurons, slower reflexes and reaction time, reduced short-term memory, altered sleep (less deep sleep, early waking), reduced thirst and temperature sensation, unsteady gait",
          "Speak slowly, give one instruction at a time, allow extra time, orient frequently, prevent falls and dehydration"],
         ["__Special senses__", "__Presbyopia, cataract, glaucoma, reduced night vision and glare tolerance; presbycusis (high-tone deafness)__, reduced taste and smell",
          "Good non-glare lighting, large print, face the patient and speak clearly in a low pitch, check spectacles and hearing aids, food may need more flavour (not more salt)"],
         ["__Cardiovascular__", "Stiff arteries and valves, reduced cardiac output and reserve, __postural hypotension__, varicose veins",
          "Change position slowly, watch for dizziness and syncope, avoid sudden exertion, monitor BP in both sitting and standing"],
         ["__Respiratory__", "Reduced elastic recoil and vital capacity, weak cough and ciliary action, rigid chest wall",
          "High risk of __pneumonia and atelectasis__ — deep breathing, early ambulation, position change, influenza and pneumococcal vaccine"],
         ["__Gastro-intestinal__", "Loss of teeth, dry mouth, reduced saliva and gastric acid, slow peristalsis, reduced liver mass and enzymes",
          "__Constipation__ (fibre, fluids, activity), indigestion, dysphagia and aspiration risk, altered drug metabolism, dental care"],
         ["__Urinary__", "Reduced renal blood flow and GFR, reduced bladder capacity, weak sphincter, prostatic enlargement in men",
          "__Nocturia, frequency, urgency, incontinence, retention__; drug doses must be reduced; watch for UTI (which may present as confusion)"],
         ["__Endocrine and metabolic__", "Reduced glucose tolerance, lower basal metabolic rate, menopause/andropause, reduced thyroid function",
          "Risk of diabetes and hypothyroidism; adjust calories; avoid weight gain"],
         ["__Immune system__", "Reduced immunity (immunosenescence)", "Infections are common, often __without fever__; vaccinate; watch for atypical presentation"],
         ["__Psychosocial__", "Retirement, loss of income and status, death of spouse and friends, loneliness, dependence, fear of death",
          "Respect, allow decision-making, encourage social contact, recreation and spiritual needs"]],
        caption="Table 15.2  Changes of ageing and their nursing implications")

    b.section_h("15.3", "Common Problems of the Aged — the 'Geriatric Giants'")
    b.table(
        ["Problem", "Causes", "Nursing management"],
        [["__Falls and instability__", "Poor vision, weakness, postural hypotension, dizziness, arthritis, neuropathy, sedatives and antihypertensives, poor footwear, wet or cluttered floors, poor lighting, unfamiliar surroundings",
          "__Fall risk assessment (Morse scale)__; clear pathways, non-slip dry floor, adequate night lighting, grab bars and raised toilet seat in the bathroom, bed at low height with brakes, call bell in reach, well-fitting non-slip footwear, walking aid at the correct height, review of medicines, vitamin D and balance exercises, no rushing, teach to sit at the edge of the bed for a minute before standing"],
         ["__Immobility__", "Paralysis, arthritis, fracture, fear of falling, deconditioning, depression",
          "Complications of immobility affect every system — __pressure sores, contractures and foot drop, muscle atrophy, osteoporosis, constipation and faecal impaction, urinary stasis and infection and stones, pneumonia and atelectasis, deep vein thrombosis and pulmonary embolism, postural hypotension, depression and confusion__; prevent with 2-hourly position change, passive and active exercises, deep breathing, early mobilisation, adequate fluid and fibre, and a footboard/splints"],
         ["__Incontinence__ (urinary and faecal)", "Weak sphincter, prostatic enlargement, UTI, constipation, immobility, dementia, diuretics",
          "Never scold; 2-hourly toileting and bladder training, pelvic floor (Kegel) exercises, easy-to-remove clothing, commode near the bed, barrier cream and pads, catheter only as a last resort, treat constipation and infection"],
         ["__Intellectual impairment — dementia and delirium__",
          "Dementia: Alzheimer's disease (commonest), vascular dementia — ~slow, progressive, irreversible~. Delirium: infection (especially UTI and pneumonia), dehydration, drugs, retention of urine, constipation, hypoxia, pain, electrolyte imbalance — ~sudden, fluctuating, reversible~",
          "__Any sudden confusion in an elderly person is delirium until proved otherwise — look for a treatable cause.__ Keep a calm, well-lit, familiar environment with a fixed routine; orient with a clock and calendar; use short simple sentences and the patient's name; avoid restraints and multiple sedatives; ensure safety (wandering, gas, stairs); involve the family; support the care-giver"],
         ["__Malnutrition and dehydration__", "Poor appetite, loss of teeth, dysphagia, poverty, loneliness, depression, reduced thirst sensation, drugs",
          "Small frequent energy- and protein-dense meals, soft food, dentures, company at meals, supplements, weigh monthly, __offer fluids every 1-2 hours (do not wait for thirst)__, watch for a dry tongue and concentrated urine"],
         ["__Insomnia__", "Pain, nocturia, anxiety, daytime napping, caffeine, dyspnoea, noise",
          "Sleep hygiene — fixed bedtime, no daytime naps, no tea/coffee in the evening, warm milk, back rub, quiet dark room, empty bladder, comfortable position; avoid routine hypnotics (they cause falls and confusion)"],
         ["__Depression and social isolation__", "Bereavement, loneliness, disability, chronic pain, dependence, financial worry",
          "Listen, allow the expression of grief, encourage hobbies and social/religious contact, involve in decisions, watch for __suicidal ideas (report at once)__, refer for treatment; depression in the elderly often presents as physical complaints or 'pseudodementia'"],
         ["__Polypharmacy and adverse drug reactions__", "Multiple diseases and prescribers, self-medication, altered kinetics (reduced renal and hepatic clearance, reduced albumin, altered body composition)",
          "__'Start low, go slow'__; review the whole drug list regularly (including over-the-counter and herbal products); simplify the regimen and use a pill box/calendar; watch specially for sedatives, anticholinergics, NSAIDs, digoxin, warfarin, oral hypoglycaemics and antihypertensives (the __Beers criteria__ list drugs to avoid in the elderly); teach the patient and family in writing with large print"],
         ["__Sensory deprivation and communication difficulty__", "Deafness, blindness, aphasia", "Hearing aid and spectacles kept clean and working, good light, face the patient, write, use gestures and pictures"],
         ["__Elder abuse and neglect__", "Care-giver stress, dependence, financial motives",
          "Look for unexplained bruises, fear, poor hygiene, malnutrition, unfilled prescriptions; report as per the __Maintenance and Welfare of Parents and Senior Citizens Act, 2007__"]],
        caption="Table 15.3  Common geriatric problems and their management")

    b.section_h("15.4", "Nursing Care of the Long-Term Bedridden Patient")
    b.numbered([
        "__Prevent pressure sores__ — 2-hourly turning with a turning chart, pressure-relieving mattress, skin inspection at every turn, keep dry and clean, high protein and vitamin C diet (see Chapter 4).",
        "__Prevent contractures and deformities__ — maintain __functional position__ (joints in mid-position, ankle at 90 degrees with a footboard, hand roll to prevent claw hand, trochanter roll to prevent external rotation of the hip); give __passive range-of-motion exercises to every joint 2-3 times a day, 5-10 repetitions each__; encourage active and isometric exercise; do not force a painful joint.",
        "__Prevent chest complications__ — semi-Fowler's position, __deep breathing and coughing exercises hourly while awake, incentive spirometry, blow a balloon/bubbles__, chest physiotherapy and postural drainage as ordered, adequate fluids, oral hygiene, and change of position.",
        "__Prevent deep vein thrombosis__ — leg and ankle exercises, early mobilisation, adequate hydration, elastic compression stockings, prescribed anticoagulant prophylaxis; __never massage the calf__ if DVT is suspected (unilateral calf pain, swelling, warmth) — report at once.",
        "__Prevent urinary problems__ — 2-3 L of fluid daily, regular voiding, upright position for voiding, perineal hygiene, avoid unnecessary catheterisation.",
        "__Prevent constipation and impaction__ — fibre, fluids, activity, regular time, privacy, prescribed laxative; check for impaction if there is spurious diarrhoea or no stool for 3 days.",
        "__Nutrition__ — high protein, high calorie, high fibre, vitamin- and mineral-rich diet with adequate fluid; assist or feed sitting up; weigh weekly.",
        "__Maintain hygiene, grooming and dignity__ — daily bed bath, mouth care 2-3 times a day, hair care, nail care, clean clothes; let the patient wear his own clothes and be well groomed — it improves morale.",
        "__Psychological and social care__ — talk to the patient, keep him informed and involved in decisions, provide radio/TV/books/phone, encourage visitors, maintain a day-night routine, respect religious practice, and __encourage maximum self-care (never do for the patient what he can do himself)__.",
        "__Support and teach the family care-giver__ — demonstrate lifting, bathing, feeding, drug administration and the signs to report; arrange respite; recognise care-giver burnout."
    ])
    b.box("clinical", [
        "__Rehabilitation aids and appliances__ — walking stick (held in the __hand opposite the affected leg__, elbow flexed 15-30°, height to the wrist crease), walker, crutches (2-3 finger breadths below the axilla with the weight taken on the __hands, not the axilla__), wheelchair, tripod, hand rails, raised toilet seat, commode chair, long-handled reacher, adapted cutlery, button hook, non-slip mat, hospital cot with side rails, air mattress, hoist.",
        "__Teaching a patient to walk with a stick after a stroke/hip surgery__: stick → affected leg → sound leg; __going up the stairs: good leg first; coming down: bad (affected) leg and the stick first__ ('up with the good, down with the bad').",
    ])

    b.section_h("15.5", "Palliative and Terminal Care; Care of the Dying")
    b.bullets([
        "__Aim__ — 'to add life to the days, not days to the life': relief of pain and distressing symptoms, psychological, social and spiritual support for the patient __and the family__, neither hastening nor postponing death.",
        "__Symptom control__ — pain (WHO ladder, __regular oral morphine 'by the clock' with a laxative and an antiemetic__; there is no maximum dose of morphine in terminal pain and __addiction is not a concern__), breathlessness (position, fan, oxygen, low-dose morphine), nausea, constipation, dry mouth (frequent sips, ice chips, mouth care), bed sores, anorexia (do not force food), 'death rattle' secretions (position and suction gently, anticholinergic), restlessness and fear.",
        "__Communication__ — answer questions honestly and simply, allow the patient to talk about dying and to express anger or fear, never take away hope, maintain privacy and never whisper at the bedside, let the family stay, allow the religious rites the family wishes.",
        "__Kubler-Ross stages of grief__ — __Denial → Anger → Bargaining → Depression → Acceptance__ (they may not occur in order, and some patients never reach acceptance).",
        "__Hospice care__ — specialised palliative care for the terminally ill, given in a hospice or at home by a team.",
        "__Advance directives, do-not-resuscitate orders and the patient's right to refuse treatment__ must be respected; euthanasia is illegal in India, but the Supreme Court has recognised __passive euthanasia and a living will (2018)__ in strictly defined circumstances.",
        "__Care of the body after death (last offices)__ and support of the bereaved family — see Chapter 6.",
    ])

    b.section_h("15.6", "Health Care Services and Schemes for the Elderly in India")
    b.bullets([
        "__National Programme for the Health Care of the Elderly (NPHCE), 2010__ — geriatric OPD and wards at district hospitals, regional geriatric centres, rehabilitation units at CHC/PHC and domiciliary visits by health workers.",
        "__Maintenance and Welfare of Parents and Senior Citizens Act, 2007__ — legally obliges children to maintain their parents; provides for old age homes and protection from abuse and abandonment.",
        "__National Policy on Older Persons (1999)__; __Integrated Programme for Senior Citizens__; __Rashtriya Vayoshri Yojana__ (free aids and appliances); __Vayoshreshtha Samman__; travel and income-tax concessions; Ayushman Bharat/PM-JAY coverage for those aged 70+.",
        "__International Day of Older Persons — 1 October__; __World Alzheimer's Day — 21 September__.",
    ])

    b.box("recap", [
        "* Elderly = 60 years and above in India; geriatrics = clinical care, gerontology = the study of ageing.",
        "* Ageing: presbyopia and presbycusis, osteoporosis, reduced GFR (so lower drug doses), postural hypotension, weak cough, constipation, reduced thirst and immunity.",
        "* Geriatric giants: falls/instability, immobility, incontinence, intellectual impairment (dementia/delirium), plus malnutrition, insomnia, depression and polypharmacy.",
        "* Sudden confusion in an elderly patient = delirium — look for UTI, pneumonia, dehydration, drugs, retention or constipation.",
        "* Prescribing: 'start low, go slow'; review the drug list; Beers criteria list drugs to avoid.",
        "* Complications of immobility: pressure sores, contractures, foot drop, pneumonia, DVT, constipation, UTI, osteoporosis, depression — turn 2-hourly, passive exercises, deep breathing, leg exercises.",
        "* Stick in the hand opposite the affected leg; crutch weight on the hands, not the axilla; stairs — 'up with the good, down with the bad'.",
        "* Palliative care: regular oral morphine by the clock with a laxative; Kubler-Ross — denial, anger, bargaining, depression, acceptance.",
        "* NPHCE 2010; Maintenance and Welfare of Parents and Senior Citizens Act 2007; Older Persons' Day 1 October.",
    ])


def chapter_16(b):
    b.chapter(16, "Care of the Mentally Ill and the Mentally Healthy Patient",
              "Mental health, classification of mental illness, therapeutic communication, safety, psychotropic drugs and ECT")

    b.section_h("16.1", "Mental Health and Mental Hygiene")
    b.box("def", [
        "__Mental health__ (WHO) — a state of well-being in which the individual realises his own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his community.",
        "__Mental hygiene__ — the science of promoting and preserving mental health and preventing mental illness.",
        "__Psychiatry__ — the branch of medicine dealing with the diagnosis, treatment and prevention of mental disorders. __Psychiatric nursing__ — nursing care of a person with a mental disorder, using the self as a therapeutic tool.",
    ])
    b.sub("Characteristics of a mentally healthy person")
    b.bullets([
        "Has a __realistic self-concept__ and accepts himself and others as they are; accepts his own limitations and strengths.",
        "Is in __touch with reality__, orientated in time, place and person; has insight.",
        "Can __form and maintain satisfying relationships__ and can give and receive affection.",
        "Can __handle stress, frustration and emotion__ appropriately and recovers from a setback (resilience).",
        "Is __independent, self-directing and responsible__; can take decisions and accept their consequences.",
        "Works __productively__, has a purpose in life, uses his abilities, and can enjoy leisure.",
        "Uses __mature coping mechanisms__ (sublimation, humour, altruism) rather than immature ones.",
    ])
    b.sub("Promotion of mental health")
    b.bullets([
        "A secure, loving childhood; consistent discipline; success experiences and encouragement.",
        "Balanced routine of work, rest, recreation, exercise, sleep and nutrition; avoidance of tobacco, alcohol and drugs.",
        "Healthy relationships and social support; the ability to express feelings and ask for help.",
        "Sex education, marriage and family counselling, guidance at times of transition (school, adolescence, marriage, retirement, bereavement).",
        "Early recognition and treatment of mental illness; removal of stigma; mental health education in schools and the community.",
    ])

    b.section_h("16.2", "Causes and Classification of Mental Illness")
    b.table(
        ["Group of causes", "Examples"],
        [["__Predisposing (biological)__", "Heredity and genes, neurotransmitter imbalance (__dopamine excess in schizophrenia; low serotonin and noradrenaline in depression; GABA in anxiety__), birth injury, brain damage, endocrine disorder, epilepsy, intellectual disability, ageing"],
         ["__Physical / organic__", "Head injury, infection (meningitis, encephalitis, neurosyphilis, HIV), tumour, stroke, dementia, hypothyroidism, vitamin B12 deficiency, uraemia, hepatic failure, hypoxia, drugs (steroids), alcohol and substance abuse, high fever (delirium)"],
         ["__Psychological__", "Faulty upbringing, maternal deprivation, childhood abuse, over-protection or rejection, unresolved conflict, poor self-esteem, faulty learning, personality type"],
         ["__Social / environmental (precipitating)__", "Bereavement, failure in examination or love, unemployment, poverty, debt, marital discord, migration, disaster, war, isolation, retirement, chronic physical illness, stigma"]],
        caption="Table 16.1  Causes of mental illness")
    b.table(
        ["Category", "Main features"],
        [["__Neurosis (minor psychiatric illness)__", "Insight and contact with reality are __retained__; no hallucination or delusion; the patient is distressed and seeks help; includes anxiety disorder, panic disorder, phobia, __obsessive-compulsive disorder__, hysteria/conversion and dissociative disorder, somatoform disorder, post-traumatic stress disorder, mild depression"],
         ["__Psychosis (major psychiatric illness)__", "__Loss of insight and of contact with reality__, __delusions and hallucinations__, disorganised thought and behaviour; includes __schizophrenia, bipolar (manic-depressive) disorder, severe depression with psychotic features, delusional disorder, organic psychosis/delirium__"],
         ["__Schizophrenia__", "Commonest psychosis; onset in adolescence/young adulthood; __delusions (especially of persecution and reference), auditory hallucinations, thought disorder and echo, disorganised speech and behaviour__ (positive symptoms) with __apathy, social withdrawal, poverty of speech, blunted affect and loss of volition__ (negative symptoms); subtypes: paranoid, catatonic, hebephrenic, simple, residual"],
         ["__Mood (affective) disorders__", "__Depression__ — persistent sadness, loss of interest (anhedonia), fatigue, guilt and worthlessness, poor concentration, __early morning waking, loss of appetite and weight, loss of libido, psychomotor retardation, suicidal ideas__. __Mania__ — elevated mood, over-activity, over-talkativeness (pressure of speech), grandiose ideas, flight of ideas, reduced need for sleep, over-spending, irritability, poor judgement. __Bipolar disorder__ — alternating episodes"],
         ["__Anxiety disorders__", "Excessive worry with palpitation, sweating, tremor, dry mouth, breathlessness, dizziness, chest discomfort, frequency of urine and a feeling of impending doom; __panic attack__ — sudden intense episode; __phobia__ — irrational fear of a specific object or situation"],
         ["__Organic brain syndromes__", "__Delirium__ (acute, fluctuating, with clouded consciousness, disorientation, visual hallucinations — a medical emergency) and __dementia__ (chronic, progressive loss of memory and intellect with clear consciousness)"],
         ["__Substance use disorders__", "__Alcohol__ (dependence, withdrawal: tremor, sweating, insomnia, seizures and __delirium tremens__ 48-72 h after stopping; Wernicke's encephalopathy needs __thiamine__), opioids (heroin, injectable — pin-point pupils, withdrawal cramps and yawning; treated with naloxone for overdose and buprenorphine/methadone substitution), cannabis, tobacco, sedatives, inhalants, stimulants"],
         ["__Child and adolescent disorders__", "Intellectual disability, autism spectrum disorder, ADHD, conduct disorder, enuresis, learning disability, school refusal, adolescent behaviour problems"],
         ["__Personality disorders and others__", "Antisocial, borderline, paranoid, dependent; eating disorders (anorexia nervosa, bulimia); sexual dysfunction; puerperal (post-partum) psychosis and post-natal depression; epilepsy-related behaviour problems; suicide"]],
        caption="Table 16.2  Classification of mental disorders")
    b.box("def", [
        "__Terms to know:__  __Delusion__ — a false, firm, unshakeable belief not in keeping with the person's culture (of persecution, grandeur, reference, guilt, nihilism, infidelity, hypochondriasis).  __Hallucination__ — a sense perception __without any external stimulus__ (auditory is the commonest in schizophrenia; visual in delirium and alcohol withdrawal; tactile, olfactory, gustatory).  __Illusion__ — a __misinterpretation__ of a real stimulus (a rope seen as a snake).  __Obsession__ — a recurrent, unwanted, intrusive thought; __compulsion__ — the repetitive act that relieves it (hand washing, checking).  __Insight__ — awareness of one's own illness.  __Affect/Mood__ — observed emotional expression / sustained inner feeling.  __Euphoria, elation, apathy, ambivalence, flight of ideas, echolalia, echopraxia, mutism, negativism, waxy flexibility, stupor, catatonia, confabulation, neologism, word salad, perseveration, tangentiality__.",
    ])

    b.section_h("16.3", "Principles of Psychiatric Nursing and Therapeutic Communication")
    b.numbered([
        "__Accept the patient as a person__ — separate the person from the behaviour; be non-judgemental; never ridicule, argue or laugh at him.",
        "Build __trust__ through consistency, honesty and keeping promises; be reliable and punctual; explain everything.",
        "Use the __self therapeutically__ — a calm, confident, unhurried manner; be aware of your own feelings and reactions.",
        "__Listen actively__ and allow the patient to express feelings; use open-ended questions, reflection, clarification and silence; sit at a safe, comfortable distance at eye level.",
        "__Do not agree with or reinforce a delusion or hallucination, and do not argue about it either__ — acknowledge the feeling, present reality gently and simply: ~'I do not hear the voices, but I understand they are frightening for you. I am here with you.'~",
        "Set __clear, consistent, firm limits__ on unacceptable behaviour, explaining the reason; the whole team must apply the same limits.",
        "Encourage __self-care, activity, occupational therapy, recreation and group participation__ — structure the day with a fixed routine.",
        "Give recognition for positive behaviour; involve the patient in planning his own care wherever possible.",
        "Maintain __confidentiality, dignity and rights__; obtain consent; avoid discussing the patient in his presence.",
        "Involve and __educate the family__; work for adherence to medication and for removal of stigma; arrange follow-up and rehabilitation."
    ])

    b.section_h("16.4", "Safety of the Psychiatric Patient")
    b.sub("Suicide risk and prevention")
    b.bullets([
        "__Warning signs__ — talk of death or hopelessness ('there is no point in living'), a previous attempt (the __single strongest predictor__), giving away belongings, writing a will or a note, sudden calmness after severe depression, collecting tablets or a rope, social withdrawal, severe insomnia, alcohol use, recent loss, chronic painful illness.",
        "__Never ignore or dismiss a threat, and never promise to keep suicidal thoughts secret__ — ask directly about plans, inform the doctor and the team at once and record it.",
        "__Nursing measures__ — __constant observation (one-to-one, within arm's length for a high-risk patient)__, especially at night, at change of shift, in the early morning and during the early recovery phase (when energy returns); remove __sharps, blades, glass, belts, ropes, ties, cords, plastic bags, matches, poisons and drugs__; check the room, bathroom (no bolt, no hook), windows (grill/shatter-proof) and locker; supervise medication and __check the mouth to ensure the tablet is swallowed__; count and account for sharps and cutlery; accompany to the bathroom; do not allow the patient to be alone with visitors who may bring harmful articles; encourage him to talk about his feelings and instil hope.",
    ])
    b.sub("The aggressive or violent patient")
    b.bullets([
        "__Early warning signs__ — restlessness and pacing, clenched fists and jaw, loud abusive speech, staring, invasion of others' space, refusal to co-operate, throwing objects, a history of violence.",
        "__De-escalation__ — remain calm and speak softly and slowly; keep a safe distance and __an exit behind you (never let the patient come between you and the door)__; do not turn your back; remove other patients from the area; never confront alone — __call for help and have adequate staff visible__; offer choices and food/medication; do not threaten, argue, shout or touch him suddenly; remove your own stethoscope, chains, dangling earrings and spectacles.",
        "__Restraint or seclusion is the last resort__ — used only when there is imminent danger and all else has failed: the doctor's order, adequate trained staff (usually 4-5, one for each limb and one for the head), correct technique, continuous observation, release and exercise of the limb and check of circulation __every 15-30 minutes with 2-hourly release__, attention to food, fluids and toileting, and full documentation with the reason, time and the patient's response. __Restraints must never be used for punishment or staff convenience__ (false imprisonment).",
        "__Rapid tranquillisation__ as prescribed (e.g. haloperidol with promethazine or lorazepam IM) with monitoring of vital signs, airway and the level of consciousness.",
    ])

    b.section_h("16.5", "Psychotropic Drugs")
    b.table(
        ["Group", "Examples", "Main side effects and nursing points"],
        [["__Typical antipsychotics (neuroleptics)__", "Chlorpromazine, haloperidol, trifluoperazine, fluphenazine decanoate (depot)",
          "__Extrapyramidal symptoms — acute dystonia, akathisia (restlessness), parkinsonism, tardive dyskinesia__ (treated/prevented with anticholinergics such as trihexyphenidyl or promethazine); postural hypotension (rise slowly), sedation, dry mouth, constipation, blurred vision, weight gain, photosensitivity (use sunscreen), galactorrhoea and amenorrhoea, jaundice, lowered seizure threshold; __neuroleptic malignant syndrome — high fever, muscle rigidity, altered consciousness, unstable BP, raised CPK: STOP the drug and treat as an emergency__"],
         ["__Atypical antipsychotics__", "Risperidone, olanzapine, quetiapine, aripiprazole, __clozapine__",
          "Fewer extrapyramidal effects but __weight gain, diabetes and dyslipidaemia__ — monitor weight, sugar and lipids. __Clozapine causes agranulocytosis__ — a mandatory regular white cell count; report any sore throat or fever at once"],
         ["__Antidepressants — SSRIs__", "Fluoxetine, sertraline, escitalopram, paroxetine",
          "Nausea, insomnia or drowsiness, sexual dysfunction, hyponatraemia; __take 2-4 weeks (up to 6) to act — the suicide risk may increase early in treatment when energy returns before mood improves__; never stop abruptly; __serotonin syndrome__ if combined with another serotonergic drug (agitation, tremor, hyperthermia, diarrhoea)"],
         ["__Tricyclic antidepressants__", "Amitriptyline, imipramine, nortriptyline",
          "Anticholinergic effects (dry mouth, constipation, retention of urine, blurred vision), postural hypotension, cardiac arrhythmia; __dangerous in overdose__; useful for nocturnal enuresis and neuropathic pain"],
         ["__MAO inhibitors__", "Phenelzine, tranylcypromine",
          "__Hypertensive crisis with tyramine-rich food — cheese, wine, beer, pickled and fermented food, yeast extract, broad beans__ — strict dietary teaching"],
         ["__Mood stabilisers__", "__Lithium carbonate__, valproate, carbamazepine, lamotrigine",
          "__Lithium has a narrow therapeutic range (0.6-1.2 mEq/L)__ — monitor levels, renal and thyroid function; __maintain a steady salt and fluid intake (2-3 L)__; toxicity (over 1.5 mEq/L): coarse tremor, vomiting, diarrhoea, ataxia, slurred speech, drowsiness, convulsions — __withhold the drug and report at once__; avoid dehydration, diuretics, NSAIDs and a low-salt diet; ~teratogenic~"],
         ["__Anxiolytics / hypnotics__", "Diazepam, lorazepam, alprazolam, clonazepam, zolpidem",
          "Sedation, falls in the elderly, __dependence and withdrawal (Schedule H1) — for short-term use only__; never combine with alcohol; taper gradually; antidote __flumazenil__"],
         ["__Anti-epileptics and others__", "Phenytoin, carbamazepine, sodium valproate, levetiracetam; donepezil and memantine for dementia; disulfiram, acamprosate and naltrexone for alcohol dependence; methadone and buprenorphine for opioid substitution",
          "Phenytoin — gum hypertrophy, hirsutism, ataxia; carbamazepine — rash, low sodium, blood dyscrasia; valproate — weight gain, hair loss, hepatotoxicity, teratogenic; __disulfiram + alcohol = a severe flushing reaction (the patient must be warned and consenting)__"]],
        caption="Table 16.3  Psychotropic drugs and nursing responsibilities")
    b.box("caution", [
        "__Nursing responsibilities with psychotropic drugs:__ give the drug under __direct observation and check the mouth__ (patients commonly hide tablets in the cheek or under the tongue); watch for early extrapyramidal reactions and report them; check BP before and after antipsychotics; warn about drowsiness (no driving or machinery); teach the patient and family that __the drug must be continued even after improvement__ and never stopped suddenly, as relapse is common; maintain the record of controlled drugs.",
    ])

    b.section_h("16.6", "Other Treatments and Nursing Care")
    b.table(
        ["Treatment", "Description", "Nursing care"],
        [["__Electroconvulsive therapy (ECT)__", "A brief controlled electrical current passed through the brain under general anaesthesia and a muscle relaxant, producing a modified seizure; a course of 6-12 treatments given 2-3 times a week. __Indications: severe depression with a high suicide risk or refusal to eat, catatonia, puerperal psychosis, and drug-resistant schizophrenia/mania__",
          "__Before:__ written informed consent, explain and reassure (dispel myths), __nil by mouth for 6-8 hours__, remove dentures, ornaments, hairpins, spectacles, contact lenses and nail polish, empty the bladder, loose clothing, record baseline vital signs, withhold the morning dose as ordered, keep the emergency tray, oxygen and suction ready.  __During:__ assist the anaesthetist, position the patient, support the joints and jaw (do not restrain the limbs forcibly).  __After:__ __lateral (recovery) position__, maintain the airway, oxygen and suction, observe respiration and vital signs until fully awake, side rails up, never leave alone, orientate repeatedly on waking (__transient confusion and short-term memory loss are expected__), offer food after the swallowing reflex returns, and record"],
         ["__Psychotherapy__", "Individual, group, family, cognitive behaviour therapy (CBT), behaviour therapy (systematic desensitisation, token economy, aversion therapy, relaxation), supportive therapy, play therapy for children",
          "Prepare the patient, keep appointments, maintain confidentiality, reinforce the learning between sessions"],
         ["__Occupational and recreational therapy__", "Purposeful graded activity — crafts, gardening, music, yoga, games, sports",
          "Raises self-esteem, gives structure and social contact, reduces preoccupation with symptoms"],
         ["__Milieu therapy / therapeutic community__", "The whole ward environment is used as the treatment", "Consistent rules, ward meetings, patient responsibility"],
         ["__Rehabilitation and community psychiatry__", "Day-care centre, half-way home, sheltered workshop, vocational training, family and community education, follow-up clinic, District Mental Health Programme",
          "Prevents relapse and institutionalisation; combats stigma; ensures drug adherence"]],
        caption="Table 16.4  Treatments in psychiatry")

    b.section_h("16.7", "Mental Health Legislation and Programmes (India)")
    b.bullets([
        "__Mental Healthcare Act, 2017__ (replaced the Mental Health Act, 1987) — gives __every person the right to access mental health care__, the right to live in the community, to protection from cruel and degrading treatment, to confidentiality, to legal aid and to make an __advance directive__ and appoint a __nominated representative__; provides for Central and State Mental Health Authorities and Mental Health Review Boards; regulates admission (independent, supported), the use of restraint and seclusion, and __prohibits unmodified ECT and ECT in minors without special sanction__; __decriminalises attempted suicide__.",
        "__Rights of Persons with Disabilities Act, 2016__ — includes mental illness and intellectual disability among the recognised disabilities; certification and benefits.",
        "__Narcotic Drugs and Psychotropic Substances (NDPS) Act, 1985__ — see Chapter 17.",
        "__National Mental Health Programme (1982)__ and the __District Mental Health Programme (1996, Bellary model)__ — integration of mental health into general health care, training of medical officers and health workers, and community care; __Tele-MANAS__ (national tele-mental-health helpline, 14416) launched in 2022.",
        "__World Mental Health Day — 10 October__; World Suicide Prevention Day — 10 September; National Institute of Mental Health and Neurosciences (__NIMHANS__), Bengaluru is the apex institute.",
    ])

    b.box("recap", [
        "* Neurosis: insight retained, no hallucination/delusion. Psychosis: insight lost, hallucinations and delusions present.",
        "* Delusion = false fixed belief; hallucination = perception without a stimulus (auditory in schizophrenia, visual in delirium); illusion = misinterpretation of a real stimulus.",
        "* Never argue with or reinforce a delusion — acknowledge the feeling and present reality.",
        "* Suicide: a previous attempt is the strongest predictor; constant observation, remove harmful articles, check the mouth after medication, never promise secrecy; risk rises early in recovery.",
        "* Violence: stay calm, keep an exit behind you, call for help, restraint only as a last resort with a doctor's order and 15-30 minute checks.",
        "* Antipsychotics → extrapyramidal symptoms and neuroleptic malignant syndrome; clozapine → agranulocytosis; lithium therapeutic 0.6-1.2 mEq/L (toxic over 1.5) — keep salt and fluid steady; SSRIs take 2-4 weeks; MAOI + tyramine = hypertensive crisis.",
        "* ECT: consent, NPO 6-8 h, remove dentures/ornaments, empty bladder; after — lateral position, airway, expect transient confusion and memory loss.",
        "* Mental Healthcare Act 2017: advance directive, nominated representative, decriminalises suicide attempt, bans unmodified ECT; NMHP 1982, DMHP 1996; World Mental Health Day 10 October.",
    ])



def chapter_17(b):
    b.chapter(17, "Special Drugs, Their Control and Administration",
              "Narcotics and psychotropics, schedules of the Drugs and Cosmetics Rules, storage, records, high-alert and cytotoxic drugs")

    b.section_h("17.1", "What Are 'Special' Drugs?")
    b.bullets([
        "__Special (controlled) drugs__ are those which, because of their __liability to abuse, their toxicity, their narrow therapeutic index or the need for special storage__, are subject to statutory control over their manufacture, sale, storage, prescription, administration, record keeping and disposal.",
        "They include: __narcotic (opioid) analgesics, psychotropic substances, barbiturates and other hypnotics, drugs of dependence, poisons, high-alert medicines, cytotoxic (anticancer) drugs, biologicals and vaccines, blood products, anaesthetic gases and medical oxygen, radiopharmaceuticals, and drugs with a narrow therapeutic index__.",
    ])

    b.section_h("17.2", "Laws Governing Drugs in India")
    b.table(
        ["Act / Rule", "Year", "What it controls"],
        [["__Drugs and Cosmetics Act and Rules__", "__Act 1940, Rules 1945__",
          "Import, manufacture, distribution and sale of drugs and cosmetics; standards of quality; licensing; the __Schedules (A to Y)__; defines misbranded, adulterated and spurious drugs"],
         ["__Pharmacy Act__", "__1948__", "Regulates the profession and practice of pharmacy; constitutes the __Pharmacy Council of India (PCI)__ and State Pharmacy Councils; registration of pharmacists; __a drug may be compounded/dispensed only by or under the supervision of a registered pharmacist__"],
         ["__Drugs and Magic Remedies (Objectionable Advertisements) Act__", "1954", "Prohibits advertisement of drugs claiming to cure specified diseases and of magic remedies"],
         ["__Narcotic Drugs and Psychotropic Substances (NDPS) Act__", "__1985__ (amended 1988, 2001, 2014, 2021)",
          "Prohibits and controls the cultivation, production, manufacture, possession, sale, purchase, transport, use, import and export of __narcotic drugs and psychotropic substances__; provides for very __stringent punishment__ (including up to 10-20 years' rigorous imprisonment and fine; death penalty possible for repeat offences in some cases) and for the treatment and rehabilitation of addicts; the __Narcotics Control Bureau (NCB)__ is the enforcing agency; 'Essential Narcotic Drugs' (including morphine) were made easier to access for medical use by the 2014 amendment"],
         ["__Poisons Act__", "1919", "Possession and sale of poisons"],
         ["__Drug Price Control Order (DPCO) / NPPA__", "DPCO 2013", "Price control of scheduled (essential) medicines by the National Pharmaceutical Pricing Authority"],
         ["__Medical Termination of Pregnancy Act__", "1971 (amended 2021)", "Conditions and places for the legal termination of pregnancy"],
         ["__Transplantation of Human Organs Act; Clinical Establishments Act; BMW Rules 2016; Food Safety and Standards Act 2006; Mental Healthcare Act 2017__",
          "-", "Related statutes affecting hospital and pharmacy practice"]],
        caption="Table 17.1  Principal drug laws in India")

    b.section_h("17.3", "Schedules of the Drugs and Cosmetics Rules (must know)")
    b.table(
        ["Schedule", "Subject matter"],
        [["__Schedule A__", "Specimen forms for applications and licences"],
         ["__Schedule B__", "Fees for the test or analysis of drugs by the Central Drugs Laboratory"],
         ["__Schedule C and C1__", "__Biological and special products__ — sera, vaccines, toxoids, antitoxins, insulin, hormones, blood products (C) and other special products such as digitalis, ergot and antibiotic preparations (C1); they require special licensing and cold storage"],
         ["__Schedule D__", "Drugs exempted from the import licence requirement"],
         ["__Schedule E1__", "List of __poisonous substances under the Ayurvedic, Siddha and Unani systems__"],
         ["__Schedule F, F1, FF__", "Requirements for blood banks and blood products (F), vaccines and sera (F1), ophthalmic solutions (FF)"],
         ["__Schedule G__", "Drugs to be used __only under medical supervision__; the label must carry the warning: ~'Caution: it is dangerous to take this preparation except under medical supervision'~ — most __anticancer (cytotoxic) drugs__, and some antidiabetics such as metformin and glibenclamide"],
         ["__Schedule H__", "__Prescription drugs__ — to be sold by retail __only on the prescription of a registered medical practitioner__; the label must bear the symbol __'Rx'__ and the warning ~'To be sold by retail on the prescription of a registered medical practitioner only'~ (most antibiotics, antihypertensives, hormones, sedatives)"],
         ["__Schedule H1__", "A sub-list of Schedule H (~about 46 drugs~) needing a __stricter record__: __third and higher generation antibiotics (cephalosporins, carbapenems), anti-tubercular drugs, and habit-forming benzodiazepines (alprazolam, diazepam, nitrazepam), tramadol__ etc. The label has a __red vertical band on the left with the Rx symbol__; the pharmacist must maintain a __separate register with the name and address of the prescriber and the patient, the name of the drug and the quantity supplied, to be retained for 3 years__"],
         ["__Schedule J__", "List of __diseases and conditions for which no drug may claim to be a remedy__ (e.g. baldness, cancer, cataract, deafness, AIDS, blindness, diabetes, obesity — in advertisements)"],
         ["__Schedule K__", "Drugs and classes of drugs __exempted__ from certain provisions (for example, household remedies sold in a village, drugs supplied by a registered practitioner to his own patient, and supply to a hospital)"],
         ["__Schedule M__", "__Good Manufacturing Practices (GMP)__ — requirements for premises, plant and equipment for the manufacture of drugs (M1 homoeopathic, M2 cosmetics, M3 medical devices)"],
         ["__Schedule N__", "__Minimum equipment required for the efficient running of a pharmacy__ (dispensing counter, balance, refrigerator, first-aid facilities, water supply etc.)"],
         ["__Schedule P__", "__Life period (shelf life) and storage conditions__ of drugs"],
         ["__Schedule P1__", "Pack sizes of drugs"],
         ["__Schedule Q__", "Permitted colouring agents and dyes in cosmetics and soaps"],
         ["__Schedule R and R1__", "Standards for mechanical contraceptives (condoms) and for medical devices"],
         ["__Schedule S__", "Standards for cosmetics (as per BIS specifications)"],
         ["__Schedule T__", "GMP for Ayurvedic, Siddha and Unani medicines"],
         ["__Schedule U and U1__", "Records of manufacture to be maintained (drugs / cosmetics)"],
         ["__Schedule V__", "Standards for patent and proprietary medicines"],
         ["__Schedule W__", "Drugs to be sold __only under generic names__ (largely superseded)"],
         ["__Schedule X__", "__The most strictly controlled schedule__ — __narcotic and psychotropic drugs, barbiturates and amphetamines__ (e.g. morphine, pethidine, fentanyl, methadone, barbiturates, amphetamine, methylphenidate, ketamine, pentazocine, buprenorphine, secobarbital). Requires a __special licence__, sale only against a __prescription in duplicate__ (one copy retained by the pharmacist for __2 years__), storage under __lock and key in a separate cupboard__, and maintenance of a register for 2 years; the label carries the symbol __'NRx' in red__"],
         ["__Schedule Y__", "Requirements and guidelines for __clinical trials__, import and manufacture of new drugs (now largely replaced by the __New Drugs and Clinical Trials Rules, 2019__)"]],
        caption="Table 17.2  Schedules of the Drugs and Cosmetics Rules, 1945 (learn H, H1, X, G, C, M, N, P, Y by heart)")
    b.box("mnemonic", [
        "__Quick recall:__  __G__ = 'Guard' (under medical supervision) • __H__ = prescription (Rx) • __H1__ = red band, separate register, 3 years • __X__ = NRx, duplicate prescription, double-locked, 2 years • __C/C1__ = biologicals/cold chain • __J__ = no cure claims • __M__ = manufacturing (GMP) • __N__ = pharmacy equipment • __P__ = shelf life • __Y__ = clinical trials.",
    ])

    b.section_h("17.4", "Narcotic and Psychotropic Drugs — Control in the Ward and Pharmacy")
    b.table(
        ["Requirement", "Details"],
        [["__Storage__", "In a __separate, substantially built cupboard/almirah with a double lock__, fixed to the wall, inside another locked cupboard or room; __the key is held personally by the nurse-in-charge/pharmacist on duty__ and handed over at each shift change; never left in a drawer or with a student"],
         ["__Stock (narcotic) register__", "A __bound register with serially numbered pages__ (no loose sheets, no pages torn out); a separate page for each drug and strength; columns for the date, time, patient's name, bed/hospital number, prescriber, dose given, balance in stock, the signature of the nurse who administered and of the witness"],
         ["__Checking__", "The __balance is physically counted and signed by two nurses at every shift change__ (three times a day); any discrepancy must be reported __immediately__ to the nursing superintendent and the pharmacist and investigated"],
         ["__Administration__", "Only against a __written, signed and dated prescription__; __two nurses check__ the drug, strength, dose, patient and time; the entry is made __immediately after__ giving; if only part of an ampoule is used, the __remainder is wasted in the presence of a witness and both sign__ the register; empty ampoules/used vials are usually retained for accounting"],
         ["__Indent and issue__", "Issued by the pharmacy only against a requisition signed by an authorised person, in exchange for the empty ampoules/a completed account; separate purchase records with the licence number are kept"],
         ["__Records retention__", "Prescriptions and registers for __2 years__ (Schedule X); NDPS records as prescribed; available for inspection by the Drugs Inspector"],
         ["__Disposal / destruction__", "Expired, damaged or unused narcotics are __never thrown away or flushed__; they are returned and destroyed only __in the presence of an authorised committee__, with a written record signed by all witnesses"],
         ["__Patient safety points__", "Check the __respiratory rate before every opioid dose (withhold if below 10-12/min)__, the level of sedation, the BP and the pain score; watch for constipation (give a laxative prophylactically), nausea, urinary retention and pruritus; keep __naloxone__ available as the antidote; do not give an opioid with alcohol or other CNS depressants without an order"]],
        caption="Table 17.3  Control of narcotic and psychotropic drugs")
    b.box("caution", [
        "Any loss, theft, breakage or discrepancy of a narcotic drug must be __reported at once in writing__; unexplained loss is a __criminal offence under the NDPS Act__ and also a serious professional misconduct. Never borrow, lend or 'adjust' narcotic stock between wards. Never leave a prepared narcotic injection unattended.",
    ])

    b.section_h("17.5", "High-Alert Medications")
    b.table(
        ["Group", "Examples", "Safety measures"],
        [["__Insulins__", "All insulins", "__Insulin syringe only; write 'unit' in full__; double-check the type (regular/NPH/mix) and dose with a second nurse; check the blood sugar before giving; keep the meal ready; store the in-use pen at room temperature and stock in the refrigerator (2-8 °C, never frozen); know the signs of hypoglycaemia"],
         ["__Anticoagulants__", "Heparin, low molecular weight heparin, warfarin",
          "Independent double check of the dose and the concentration (heparin comes in many strengths); monitor __aPTT/INR and platelets__; watch for bleeding (gums, urine, stool, bruises); keep __protamine sulphate (heparin) and vitamin K (warfarin)__ available; teach the patient about diet, interacting drugs, a soft toothbrush and an electric razor"],
         ["__Concentrated electrolytes__", "__Potassium chloride__, hypertonic saline, magnesium sulphate",
          "__Never give concentrated KCl as an IV bolus/push — it causes cardiac arrest__; always dilute (usually not more than 40 mEq/L peripherally) and infuse slowly with a pump, preferably with cardiac monitoring; store separately from other ampoules"],
         ["__Opioids and sedatives__", "Morphine, fentanyl, pethidine, midazolam", "As in 17.4; monitor respiration and sedation; antidotes naloxone and flumazenil"],
         ["__Chemotherapy / cytotoxics__", "Methotrexate, vincristine, cyclophosphamide, cisplatin, 5-FU",
          "Prescribed by a specialist; verified by two persons against the protocol and body surface area; __vincristine is fatal if given intrathecally — it must be labelled 'for intravenous use only'__; methotrexate for arthritis is __weekly, not daily__"],
         ["__Others__", "Digoxin, phenytoin, theophylline, lithium, aminoglycosides, thrombolytics, neuromuscular blockers, IV anaesthetics, oxytocin, adrenaline, magnesium sulphate",
          "__Check the pulse before digoxin (withhold if below 60/min in an adult or 90-100 in an infant)__; monitor drug levels for narrow-index drugs; __neuromuscular blockers must be stored separately with a warning label — they cause respiratory arrest if given by mistake__"]],
        caption="Table 17.4  High-alert medications and their safeguards")

    b.section_h("17.6", "Handling Cytotoxic (Anticancer) Drugs")
    b.bullets([
        "Prepare only in a __biological safety cabinet/laminar air flow (Class II B) in a designated area__, never on an open ward table; use a __closed-system transfer device__ and a luer-lock syringe.",
        "__PPE__ — double chemotherapy gloves (changed every 30-60 min), a long-sleeved impervious gown, mask/N95, cap, goggles and shoe covers.",
        "__Pregnant, breast-feeding and immunocompromised staff must not handle cytotoxic drugs__; staff should be rotated and have periodic health checks (blood count).",
        "Keep a __spill kit__ ready; in case of a spill, restrict the area, wear PPE, absorb with the pads provided (do not sweep or wipe widely), wash the area three times, and dispose of everything as __cytotoxic waste__; report and record the incident. For skin contact, wash with plenty of soap and water; for eye contact, irrigate with water/saline for 15 minutes and see the ophthalmologist.",
        "__Waste__ — all vials, syringes, needles, gowns, gloves and tubing go into a __labelled cytotoxic (yellow) container for incineration at high temperature__; the patient's excreta and linen are handled with gloves for __48 hours__ after administration.",
        "__Extravasation__ of a vesicant (doxorubicin, vincristine) — stop the infusion immediately, leave the cannula in place, aspirate the residual drug, mark the area, apply cold or warm compresses as per the drug protocol, give the specific antidote, elevate the limb, inform the doctor and document with a photograph.",
        "__Nursing care of the patient__ — antiemetics before and after, mouth care for mucositis (soft brush, saline rinses), monitor the blood count (__neutropenia — protective isolation and report any fever at once as it is an emergency__), hydration and output for nephrotoxic drugs, care of alopecia and body image, contraception advice and fertility counselling.",
    ])

    b.section_h("17.7", "Storage and Administration of Other Special Preparations")
    b.table(
        ["Preparation", "Storage", "Administration points"],
        [["__Vaccines and sera (Schedule C/C1)__", "__2-8 °C cold chain__; never freeze adsorbed vaccines; protect from light; VVM check",
          "Correct site, route and dose (Chapter 14); keep adrenaline ready; observe for 30 min; record the batch number and expiry"],
         ["__Insulin__", "Unopened: refrigerator __2-8 °C__; in-use vial/pen: __room temperature (below 30 °C) for 28 days__; __never freeze__; do not shake vigorously (roll cloudy insulin gently)",
          "Insulin syringe/pen only; rotate sites; give __regular insulin 30 min before a meal__, rapid analogues just before; when mixing, __draw clear (regular) before cloudy (NPH)__; keep glucose/glucagon ready for hypoglycaemia"],
         ["__Blood and blood products__", "__Whole blood/red cells 2-6 °C__ in a blood-bank refrigerator (never a ward refrigerator); platelets 20-24 °C with agitation; FFP frozen at −30 °C",
          "See Chapter 19 — start within 30 minutes of issue, complete within 4 hours, use a blood set with a filter, saline only"],
         ["__Medical oxygen and anaesthetic gases__", "Cylinders upright, chained, in a cool, well-ventilated room away from oil, grease and any flame; __colour codes: oxygen — black body with a white shoulder (white in ISO), nitrous oxide — blue, carbon dioxide — grey, medical air — grey/white-and-black, entonox — blue with blue-and-white quarters__",
          "__No smoking, no naked flame, no oil or grease__ on fittings or on the patient's face; check the contents and the flow meter; humidify for flows above 4 L/min; treat oxygen as a __prescribed drug__ (dose, flow, target saturation)"],
         ["__Eye preparations__", "Sterile; store as labelled", "One container per patient; __discard 4 weeks after opening__; never touch the dropper to the eye"],
         ["__Reconstituted antibiotics and suspensions__", "As labelled — many need refrigeration after reconstitution", "Write the __date and time of reconstitution and the discard date__ on the vial/bottle; shake before use"],
         ["__Sublingual nitroglycerine__", "Tight, amber glass container away from heat and light; potency lost in about 8 weeks after opening",
          "Patient sits or lies down (it causes a fall in BP and headache); one tablet under the tongue, repeat up to 3 doses 5 min apart, then seek emergency help"],
         ["__Radiopharmaceuticals__", "Lead-shielded container in a designated area with radiation warning signs", "Handled by trained personnel with dosimeters; the patient's urine and linen may need special precautions"]],
        caption="Table 17.5  Storage and administration of special preparations")

    b.section_h("17.8", "Rational Drug Use, Antibiotic Stewardship and DOTS")
    b.bullets([
        "__Rational use of drugs (WHO)__ — 'patients receive medications appropriate to their clinical needs, in doses that meet their own individual requirements, for an adequate period of time, and at the lowest cost to them and their community'.",
        "__Irrational practices__ — unnecessary antibiotics for viral fever and simple diarrhoea, injections where oral drugs would do, irrational fixed-dose combinations, polypharmacy, self-medication, incomplete courses, and prescribing by brand where cheaper generics exist.",
        "__Antimicrobial stewardship__ — prescribe an antibiotic only when indicated, ideally after culture; follow the hospital antibiotic policy and the __WHO AWaRe classification (Access, Watch, Reserve)__; give the right dose for the right duration; de-escalate on the basis of culture; review IV to oral switch; complete the course; and educate patients that __antibiotics do not cure viral illness__ — this is central to controlling __antimicrobial resistance (AMR)__.",
        "__DOTS / NTEP (tuberculosis)__ — __Directly Observed Treatment, Short-course__: every dose in the intensive phase is __swallowed in the presence of a treatment supporter__; __2 months of HRZE (intensive) followed by 4 months of HRE (continuation)__ in daily fixed-dose combinations by weight band; drug-resistant TB is treated under a separate regimen; the nurse/pharmacist explains the side effects (orange urine with rifampicin, neuritis with isoniazid — give pyridoxine, joint pain with pyrazinamide, visual change with ethambutol — report at once), ensures adherence, does contact tracing, and registers the patient on __Ni-kshay__ (with nutritional support of Rs 1000 per month under Ni-kshay Poshan Yojana).",
        "__Essential medicines__ — the __National List of Essential Medicines (NLEM)__ guides procurement; prescribe generically; report ADRs to __PvPI__; report a suspected __spurious or substandard drug__ to the Drugs Inspector.",
    ])

    b.section_h("17.9", "The Pharmacist's and Nurse's Statutory Responsibilities — Summary")
    b.numbered([
        "Dispense only against a valid prescription; verify the prescriber, the patient, the drug, the dose and the interactions; __refuse and refer back__ a prescription that is illegible, incomplete or unsafe.",
        "Maintain the statutory __registers — prescription register, Schedule H1 register (3 years), Schedule X register and prescriptions (2 years), narcotic register, purchase and sale records, and temperature records of the refrigerator__.",
        "Store drugs as per __Schedule P__ conditions, keep the pharmacy equipped as per __Schedule N__, and display the licence and the registered pharmacist's certificate.",
        "Keep the controlled-drug cupboard __double-locked__ and account for every dose; do the shift count with a witness.",
        "__Label__ every dispensed medicine with the patient's name, the drug and strength, the dose and directions, the date, the expiry, storage instructions and any warning ('shake well', 'for external use only', 'complete the course').",
        "__Counsel__ the patient in a language he understands and check his understanding by asking him to repeat the instructions.",
        "Never substitute, alter or add to a prescription without the prescriber's consent; never dispense a Schedule X or narcotic drug without the prescribed formalities.",
        "__Report__ adverse drug reactions, medication errors, near misses, suspected spurious drugs and any loss of controlled drugs.",
        "Dispose of expired, damaged and returned drugs by the approved route with documentation.",
        "Maintain __confidentiality__ of the prescription and the patient's condition, and practise within the limits of the Pharmacy Act and the Code of Pharmaceutical Ethics."
    ])

    b.box("recap", [
        "* Drugs and Cosmetics Act 1940/Rules 1945; Pharmacy Act 1948 (PCI); NDPS Act 1985 (NCB); Poisons Act 1919; DPCO 2013.",
        "* Schedule G = 'dangerous except under medical supervision'; H = Rx; H1 = red band + separate register kept 3 years; X = NRx, duplicate prescription, double lock, records 2 years.",
        "* Schedule C/C1 = biologicals (cold chain); J = no cure claims; M = GMP; N = pharmacy equipment; P = shelf life; Y = clinical trials.",
        "* Narcotics: double-locked cupboard, key with the nurse-in-charge, bound serially numbered register, count and sign at every shift by two nurses, waste witnessed, destruction only before a committee.",
        "* Check respiration before an opioid (hold if under 10-12/min); antidote naloxone. Check the pulse before digoxin (hold if under 60).",
        "* Never give concentrated potassium chloride as an IV push; never give vincristine intrathecally; methotrexate for arthritis is weekly.",
        "* Insulin: unopened 2-8 °C, in-use at room temperature for 28 days, never frozen; draw clear before cloudy.",
        "* Oxygen cylinder: black with a white shoulder, kept away from oil, grease and flame; oxygen is a prescribed drug.",
        "* Cytotoxics: laminar flow cabinet, double gloves, spill kit, cytotoxic yellow waste, no handling by pregnant staff.",
        "* DOTS: 2 months HRZE + 4 months HRE, every dose observed; rifampicin → orange urine; isoniazid → neuritis (give pyridoxine); ethambutol → optic neuritis.",
    ])
