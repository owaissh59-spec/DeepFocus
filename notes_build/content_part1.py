"""
content_part1.py  -  PART I : HEALTH EDUCATION
Chapters 1-9 of the JKSSB Junior Pharmacist notes.
"""

from docx_style import (
    BLUE, GREEN, MAROON, NAVY, ORANGE, PURPLE, TEAL,
    SH_BAND, SH_BAND_GREEN, SH_HEADER_BLUE, SH_HEADER_GREEN,
    SH_HEADER_PURPLE, SH_HEADER_TEAL,
    box, bullet, bullets, chapter_end, chapter_title, defn, h2, h3, h4,
    numbered, para, part_title, rule, table,
)
from docx.shared import Pt


# ===========================================================================
# CHAPTER 1
# ===========================================================================
def chapter_01(doc):
    chapter_title(doc, 1, "Health, Disease and the Foundations of Health Education")

    para(doc, "Health education is an applied science. Before its principles, ethics and "
              "methods can make sense, the vocabulary it works with \u2014 health, disease, "
              "prevention, health promotion \u2014 must be precise. This chapter builds that "
              "base, and almost every definition in it is independently examinable.")

    # ---------------- 1.1 Health
    h2(doc, "1.1  The Concept of Health")

    box(doc, "definition",
        ["**WHO definition (1948, from the Preamble to the WHO Constitution):** Health is a "
         "state of ^^complete physical, mental and social well-being^^ and not merely the "
         "absence of disease or infirmity.",
         "**1978 (Alma-Ata) addition:** \u2026 and the ability to lead a __socially and "
         "economically productive life__.",
         "**Operational definition (WHO):** health is a condition in which there is "
         "(a) no obvious evidence of disease and the person is functioning normally, and "
         "(b) no minimal or hidden impairment of the several organs."],
        title="DEFINITIONS OF HEALTH")

    bullets(doc, [
        "The WHO definition has been criticised as an **idealistic goal rather than a "
        "realistic proposition** \u2014 the word \u201ccomplete\u201d makes it unattainable "
        "and unmeasurable; hence the operational definition was framed for practical use.",
        "Health is **relative**, **multidimensional**, a **positive concept** (not merely "
        "absence of disease), a **fundamental human right**, and an **essential component of "
        "development**.",
        "WHO's slogan **\u201cHealth for All by the Year 2000 AD\u201d** was adopted at the "
        "~~30th World Health Assembly, 1977~~ and the means to achieve it \u2014 ^^Primary "
        "Health Care^^ \u2014 was declared at ~~Alma-Ata (Almaty, USSR), 6\u201312 September "
        "1978~~.",
    ])

    h3(doc, "1.1.1  Dimensions of Health")
    table(doc,
          ["Dimension", "What it covers", "Key markers / exam points"],
          [["Physical", "Perfect functioning of the body; all organs in harmony; the "
            "\u201cbiological\u201d dimension.",
            "Good complexion, clean skin, bright eyes, firm flesh, sweet breath, good "
            "appetite, sound sleep, regular bowel/bladder, coordinated movements, normal "
            "pulse, BP and weight for height."],
           ["Mental", "Ability to respond to the many varied experiences of life with "
            "flexibility and a cheerful temper; absence of mental illness.",
            "Free from internal conflict, self-respecting, knows self, adjusts to "
            "environment, accepts criticism, controls anger/fear. **Mental health is not "
            "merely absence of mental illness.**"],
           ["Social", "Quantity and quality of interpersonal ties; harmony and integration "
            "within and between the individual and the community.",
            "Social skills, social functioning, ability to see oneself as a member of a "
            "society. Measured through social adjustment and social support."],
           ["Spiritual", "That part of the individual which reaches out for meaning and "
            "purpose in life; integrity, principles and ethics.",
            "Included as a dimension by WHO; covers purpose in life, transcendent values, "
            "faith, commitment."],
           ["Emotional", "Recognising and appropriately expressing feelings; earlier merged "
            "with mental health, now treated separately.",
            "Mental = \u201ccognition / knowing\u201d; Emotional = \u201caffective / "
            "feeling\u201d."],
           ["Vocational", "Work, occupation and economic self-sufficiency as a source of "
            "self-esteem and health.",
            "Becomes especially significant when a person suddenly loses a job or retires."],
           ["Others", "Philosophical, cultural, socio-economic, environmental, educational, "
            "nutritional, curative and preventive dimensions.",
            "Often listed together as \u201cother dimensions\u201d in textbooks."]],
          header_fill=SH_HEADER_BLUE, caption="Table 1.1  Dimensions of health")

    box(doc, "mnemonic",
        "The four **core WHO dimensions** = ``P M S S`` \u2192 **P**hysical, **M**ental, "
        "**S**ocial, **S**piritual. Add ``E V`` (**E**motional, **V**ocational) for the "
        "six commonly asked dimensions.")

    h3(doc, "1.1.2  Concepts of Health (Evolution of Thought)")
    table(doc,
          ["Concept", "Core idea", "Limitation"],
          [["Biomedical (germ theory)", "Health = absence of disease; the body is a machine "
            "and disease is its breakdown; doctor's task is repair.",
            "Ignored environmental, social, psychological and cultural determinants."],
           ["Ecological", "Health is a dynamic ^^equilibrium between man and his "
            "environment^^; disease is maladjustment. Introduced the ideas of ecology and "
            "human ecology.",
            "Focuses on adaptation, less on social organisation."],
           ["Psychosocial", "Health is determined not only by biological factors but also by "
            "social, psychological, cultural, economic and political factors.",
            "Needed integration with biological understanding."],
           ["Holistic", "A ^^synthesis of all the above^^ \u2014 health is a unified, "
            "multidimensional process involving the well-being of the whole person in the "
            "context of the environment. Recognises the influence of agriculture, education, "
            "housing, industry and public health.",
            "The currently accepted concept; emphasises **health promotion** and "
            "**intersectoral coordination**."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 1.2  Changing concepts of health")

    h3(doc, "1.1.3  Spectrum and Determinants of Health")
    para(doc, "**Spectrum of health:** health and disease lie along a continuum "
              "(\u201chealth\u2013disease spectrum\u201d) \u2014 ``positive health \u2192 "
              "better health \u2192 freedom from sickness \u2192 unrecognised sickness \u2192 "
              "mild sickness \u2192 severe sickness \u2192 death``. There is no single "
              "cut-off point; the lowest point is death and the highest point is optimum "
              "or positive health.")

    table(doc,
          ["Group of determinants", "Examples"],
          [["Biological / genetic", "Genetic constitution, sex, age, race; inborn errors of "
            "metabolism, haemoglobinopathies, chromosomal anomalies."],
           ["Behavioural & socio-cultural", "Lifestyle: diet, smoking, alcohol, physical "
            "activity, sexual behaviour, customs, beliefs, religion, cultural practices."],
           ["Environment", "\u201cInternal\u201d (tissues, organs) and \u201cexternal\u201d "
            "\u2014 physical, biological and psychosocial; water, air, housing, waste, "
            "noise, radiation."],
           ["Socio-economic", "Economic status, education (especially ^^female "
            "literacy^^), occupation, political system. **Education is regarded as a key "
            "determinant \u2014 the infant mortality rate is closely linked to female "
            "literacy.**"],
           ["Health services", "Availability, accessibility, affordability, acceptability "
            "and quality of care; immunisation, antenatal care, safe delivery."],
           ["Ageing of population, gender, other factors",
            "Growing elderly population, gender discrimination, information technology, "
            "globalisation and trade."]],
          header_fill=SH_HEADER_TEAL, caption="Table 1.3  Determinants of health")

    # ---------------- 1.2 Disease
    h2(doc, "1.2  Disease, Illness and Sickness")
    defn(doc, "Disease", "A physiological or psychological dysfunction \u2014 the "
                         "**objective, pathological** state, as diagnosed by the physician. "
                         "Literally __dis-ease__, the opposite of ease.")
    defn(doc, "Illness", "The **subjective** state of the person who feels aware of not "
                         "being well.")
    defn(doc, "Sickness", "A **state of social dysfunction** \u2014 the role the individual "
                          "assumes when ill (\u201csickness role\u201d).")

    h3(doc, "1.2.1  Epidemiological Triad and the Iceberg of Disease")
    bullets(doc, [
        "**Epidemiological triad** = ^^Agent + Host + Environment^^. Disease results from "
        "an interaction of the three; this is the basis of the multifactorial causation "
        "concept.",
        "**Iceberg phenomenon of disease:** what is visible above the waterline is clinical "
        "disease; hidden below are pre-symptomatic, sub-clinical, latent, carrier and "
        "undiagnosed states. The submerged portion constitutes the **hidden mass of "
        "disease** and is of great epidemiological importance \u2014 it is the target of "
        "screening and of health education.",
    ])

    h3(doc, "1.2.2  Natural History of Disease and Levels of Prevention")
    table(doc,
          ["Level of prevention", "Phase of disease", "Mode of intervention", "Examples"],
          [["Primordial", "Before risk factors appear (in childhood)",
            "Discouraging the emergence of risk-factor lifestyles",
            "Health education to prevent children from starting smoking; promoting healthy "
            "eating habits in schools; national policy on tobacco and salt."],
           ["Primary", "Pre-pathogenesis (susceptibility)",
            "**Health promotion** and **specific protection**",
            "Health education, nutrition, safe water, housing; immunisation, "
            "chemoprophylaxis, iodisation of salt, use of helmets, fluoridation."],
           ["Secondary", "Early pathogenesis / pre-symptomatic",
            "**Early diagnosis and prompt treatment**",
            "Screening (cancer cervix, diabetes), case finding, DOTS for tuberculosis, "
            "treating hypertension early."],
           ["Tertiary", "Late pathogenesis / disability",
            "**Disability limitation** and **rehabilitation**",
            "Preventing complications of diabetes; physiotherapy, prosthesis, "
            "reconstructive surgery, vocational and social rehabilitation."]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 1.4  Levels of prevention and modes of intervention")

    box(doc, "highyield",
        ["**Health education is used at EVERY level of prevention**, but it is the "
         "dominant tool of ^^primordial^^ and ^^primary^^ prevention (health promotion).",
         "The **five modes of intervention** (Leavell & Clark) are: health promotion, "
         "specific protection, early diagnosis & treatment, disability limitation, "
         "rehabilitation.",
         "Rehabilitation has ~~four components~~: **medical, vocational, social and "
         "psychological** rehabilitation."])

    # ---------------- 1.3 Health promotion
    h2(doc, "1.3  Health Promotion and the Ottawa Charter")
    defn(doc, "Health promotion (WHO, Ottawa 1986)",
         "The **process of enabling people to increase control over, and to improve, their "
         "health**. It is not confined to health care; health is a resource for everyday "
         "life, not the objective of living.")

    table(doc,
          ["Ottawa Charter, 1986", "Content"],
          [["Five action areas",
            "1. Build healthy **public policy**  2. Create **supportive environments**  "
            "3. Strengthen **community action**  4. Develop **personal skills** (this is "
            "where health education sits)  5. **Reorient health services** towards "
            "prevention and promotion."],
           ["Three basic strategies",
            "^^Advocate^^ (for health), ^^Enable^^ (empower people, reduce inequity), "
            "^^Mediate^^ (between differing interests in society)."],
           ["Prerequisites for health",
            "Peace, shelter, education, food, income, a stable ecosystem, sustainable "
            "resources, social justice and equity."]],
          header_fill=SH_HEADER_PURPLE)

    bullets(doc, [
        "The **First International Conference on Health Promotion** was held at ~~Ottawa, "
        "Canada in 1986~~ and produced the **Ottawa Charter**.",
        "The **Bangkok Charter for Health Promotion in a Globalized World** was adopted in "
        "~~2005~~ (6th Global Conference); it added advocacy, investment, capacity building, "
        "regulation/legislation and partnership as key actions.",
        "**Health promotion approaches** (Park): (1) medical/preventive, (2) behaviour "
        "change, (3) educational, (4) empowerment, (5) social change.",
    ])

    # ---------------- 1.4 Related terms
    h2(doc, "1.4  Health Education and its Cousins \u2014 Distinguishing the Terms")
    table(doc,
          ["Term", "Meaning", "Relationship"],
          [["Health education", "Planned learning experiences that help people **voluntarily** "
            "change behaviour to improve health.",
            "The educational **core** of health promotion."],
           ["Health promotion", "The broad process of enabling control over health; includes "
            "policy, environment and services besides education.",
            "**Wider than health education.** Health education \u2282 health promotion."],
           ["IEC \u2014 Information, Education & Communication",
            "A strategy combining information giving, education and communication to "
            "increase awareness and promote behaviour change; the term used in almost all "
            "Indian national health programmes.",
            "The operational form of health education in Indian public health."],
           ["BCC \u2014 Behaviour Change Communication",
            "An interactive, evidence-based, audience-segmented process aimed specifically "
            "at changing and sustaining behaviour.",
            "The **newer, more focused successor to IEC**; emphasises two-way dialogue."],
           ["Health propaganda / publicity",
            "One-way dissemination of slogans and messages to persuade, without concern "
            "for understanding or voluntary choice.",
            "**Not** health education \u2014 education respects free, informed choice."],
           ["Social marketing",
            "Applying commercial marketing techniques (product, price, place, promotion) to "
            "promote socially beneficial behaviour \u2014 e.g. subsidised condoms, ORS.",
            "A **tool used within** health promotion."],
           ["Health literacy",
            "The cognitive and social skills that determine the motivation and ability of "
            "individuals to gain access to, understand and use information to promote "
            "health.",
            "The **outcome** of effective health education."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 1.5  Health education versus related concepts")

    box(doc, "exam",
        ["Health education relies on ^^voluntary, informed decision-making^^; propaganda "
         "relies on persuasion and repetition. This distinction is a classic MCQ.",
         "**Education informs and enables; propaganda persuades; indoctrination "
         "compels.**"])

    h2(doc, "1.5  Health Education in Primary Health Care")
    para(doc, "The Alma-Ata Declaration (1978) listed **eight essential components of "
              "primary health care**. The very first is education:")
    numbered(doc, [
        "**Education concerning prevailing health problems and the methods of preventing "
        "and controlling them** \u2014 i.e. health education.",
        "Promotion of food supply and proper nutrition.",
        "An adequate supply of safe water and basic sanitation.",
        "Maternal and child health care, including family planning.",
        "Immunisation against the major infectious diseases.",
        "Prevention and control of locally endemic diseases.",
        "Appropriate treatment of common diseases and injuries.",
        "Provision of essential drugs.",
    ])
    box(doc, "highyield",
        "^^Health education is the FIRST of the eight elements of primary health care^^ and "
        "is described as the **most cost-effective single intervention in public health**. "
        "The four principles (pillars) of PHC are ~~equitable distribution, community "
        "participation, intersectoral coordination and appropriate technology~~.")

    chapter_end(doc)



# ===========================================================================
# CHAPTER 2
# ===========================================================================
def chapter_02(doc):
    chapter_title(doc, 2, "Health Education \u2014 Definition, Aims, Objectives and Scope")

    h2(doc, "2.1  Definitions of Health Education")
    para(doc, "Several definitions are quoted in examinations. Learn the author with the "
              "definition.")

    table(doc,
          ["Source", "Definition"],
          [["**WHO Expert Committee, 1969**",
            "Health education, like general education, is concerned with **change in "
            "knowledge, feelings and behaviour of people**. In its most usual form it "
            "concentrates on developing such health practices as are believed to bring about "
            "the best possible state of well-being."],
           ["**Alma-Ata / WHO (1978)**",
            "A process aimed at encouraging people to want to be healthy, to know how to "
            "stay healthy, to do what they can individually and collectively to maintain "
            "health, and to seek help when needed."],
           ["**Grout**",
            "Health education is the **translation of what is known about health into "
            "desirable individual and community behaviour patterns** by means of the "
            "educational process."],
           ["**Dorothy Nyswander**",
            "Health education is the process of providing learning experiences which "
            "favourably influence understanding, attitudes and conduct in regard to "
            "individual and community health."],
           ["**Lawrence W. Green (1980)**",
            "Any **combination of learning experiences** designed to facilitate "
            "**voluntary** actions conducive to health."],
           ["**Joint Committee on Health Education Terminology (2001)**",
            "Any combination of planned learning experiences based on sound theories that "
            "provide individuals, groups and communities the opportunity to acquire "
            "information and the skills needed to make quality health decisions."],
           ["**National Conference on Preventive Medicine (USA)**",
            "A process that informs, motivates and helps people to adopt and maintain "
            "healthful practices and lifestyles, advocates environmental changes as needed "
            "and conducts professional training and research to the same end."]],
          header_fill=SH_HEADER_BLUE, caption="Table 2.1  Standard definitions")

    box(doc, "highyield",
        ["Two words recur in almost every definition and are the key to MCQs: "
         "^^voluntary^^ and ^^behaviour change^^.",
         "Health education aims at change in the **three domains of learning** \u2014 "
         "**K**nowledge (cognitive), **A**ttitude/feelings (affective) and **P**ractice/"
         "behaviour (psychomotor): the basis of the famous ~~KAP~~ studies "
         "(Knowledge\u2013Attitude\u2013Practice)."])

    h2(doc, "2.2  Aim and Objectives of Health Education")
    h3(doc, "2.2.1  Aim")
    para(doc, "The ultimate aim of health education is **not merely to give information but "
              "to bring about a change in behaviour**, so that people attain and maintain "
              "positive health through their own effort and action. It seeks to make health "
              "an asset valued by the community.")

    h3(doc, "2.2.2  The Three Classical Objectives (WHO)")
    table(doc,
          ["Objective", "What it involves", "Level of learning"],
          [["1.  **Informing people**",
            "Disseminating scientific knowledge about health, diseases and their "
            "prevention; the dissemination of information is the first and most basic "
            "objective.", "Cognitive \u2014 knowledge"],
           ["2.  **Motivating people**",
            "Persuading people to change and adopt healthy practices; motivation involves "
            "arousing interest, creating a felt need and sustaining desire.",
            "Affective \u2014 attitude"],
           ["3.  **Guiding into action**",
            "Helping people to take action, to use health services wisely and to sustain "
            "the new behaviour \u2014 by working with them, not for them.",
            "Psychomotor \u2014 practice"]],
          header_fill=SH_HEADER_TEAL)

    h3(doc, "2.2.3  Specific Objectives")
    bullets(doc, [
        "To make people **aware** of their own health problems and the resources available.",
        "To help people **understand** that health is a valuable community asset.",
        "To promote the **correct use of health services** \u2014 to seek care early and "
        "avoid quackery and self-medication.",
        "To develop a **sense of responsibility** for one's own health and that of others.",
        "To bring about a **change in attitudes and values**, not just knowledge.",
        "To develop and maintain **healthful behaviour and skills** (hand-washing, oral "
        "rehydration, breast-feeding, exercise).",
        "To encourage **community participation** and self-reliance in solving local health "
        "problems.",
        "To secure the **adoption and maintenance of healthy lifestyles**.",
        "To create demand for and support healthy **public policy** and environmental change.",
    ])

    box(doc, "note",
        "Objectives should be written in ^^SMART^^ form \u2014 **S**pecific, "
        "**M**easurable, **A**chievable/Attainable, **R**elevant/Realistic, "
        "**T**ime-bound.")

    h2(doc, "2.3  Scope and Content of Health Education")
    para(doc, "The scope of health education is as wide as health itself. The WHO Expert "
              "Committee grouped the content under the following heads:")
    table(doc,
          ["Area", "Content taught"],
          [["Human biology", "Structure and functioning of the body; how to keep it fit; "
            "personal responsibility for one's body."],
           ["Nutrition", "Balanced diet, locally available low-cost foods, nutritional "
            "deficiency disorders, infant and young child feeding, breast-feeding, "
            "supplementary feeding, food hygiene and adulteration."],
           ["Hygiene", "**Personal hygiene** \u2014 bathing, care of skin, hair, teeth, "
            "eyes, ears, nose, hands and feet, clothing, rest, sleep, exercise, posture. "
            "**Environmental hygiene** \u2014 safe water, excreta and refuse disposal, "
            "housing, ventilation, lighting, vector control."],
           ["Family health care", "Antenatal, natal and postnatal care, family planning, "
            "spacing of children, care of the newborn, growth monitoring, immunisation, "
            "adolescent health, care of the elderly."],
           ["Control of communicable diseases", "Modes of spread and prevention of "
            "tuberculosis, malaria, dengue, diarrhoeal disease, hepatitis, HIV/AIDS, COVID-19, "
            "vaccine-preventable diseases; notification and isolation."],
           ["Control of non-communicable diseases", "Hypertension, diabetes, cancer, "
            "cardiovascular disease, obesity, COPD; risk-factor reduction \u2014 tobacco, "
            "alcohol, salt, sugar, fat, physical inactivity, stress."],
           ["Mental health", "Coping with stress, sleep hygiene, substance abuse "
            "prevention, suicide prevention, reduction of stigma."],
           ["Prevention of accidents", "Road, home, occupational, agricultural and "
            "industrial accidents; first aid; poisoning; drowning; burns."],
           ["Use of health services", "What services exist, where, when and how to use "
            "them; referral; health insurance; entitlements; rights of the patient."]],
          header_fill=SH_HEADER_GREEN, caption="Table 2.2  Content of health education")

    h2(doc, "2.4  Approaches and Models in Health Education")
    table(doc,
          ["Approach (Park)", "Description"],
          [["**Regulatory / managed prevention approach**",
            "Legislation and enforcement \u2014 compulsory immunisation, seat-belt and "
            "helmet laws, food standards, ban on smoking in public places. Effective but "
            "may be resented as compulsion."],
           ["**Service approach**",
            "Providing health services at the doorstep on the assumption that people will "
            "use them. Often fails because it is based on the planners' assumptions and not "
            "on the **felt needs** of the people."],
           ["**Health education approach**",
            "Providing information and education so that people act on their own; slow but "
            "produces permanent, self-sustaining change. **The approach of choice.**"],
           ["**Primary health care approach**",
            "Community participation and involvement of people in planning and "
            "implementation, with health education as its backbone."]],
          header_fill=SH_HEADER_PURPLE)

    h3(doc, "2.4.1  Models of Health Education")
    table(doc,
          ["Model", "Assumption", "Comment"],
          [["Medical model", "Ill-health is due to disease; information from an expert will "
            "make people comply.", "Expert-centred, paternalistic, one-way; limited success."],
           ["Motivation model", "Behaviour changes when the individual is motivated and "
            "internalises the value of health.",
            "Change is gradual but lasting; needs interpersonal work."],
           ["Social intervention / social change model",
            "Behaviour is determined by the social environment; change society and "
            "behaviour follows.",
            "Requires policy, legislation and environmental modification."]],
          header_fill=SH_HEADER_BLUE)

    h2(doc, "2.5  Health Education and the Pharmacist")
    para(doc, "For a **Junior Pharmacist** health education is a daily duty, not a "
              "theoretical subject. The pharmacist is frequently the most accessible health "
              "professional a patient meets, and the last one before the medicine is used.")
    bullets(doc, [
        "**Patient counselling** on the dose, frequency, duration, route, timing in relation "
        "to food, expected effects and common adverse effects of each medicine.",
        "Ensuring **adherence/compliance** \u2014 explaining why a full course of "
        "antibiotics or anti-tubercular therapy must be completed; demonstrating inhaler, "
        "insulin pen, ORS and eye-drop technique.",
        "Promoting **rational drug use** and discouraging self-medication, irrational "
        "antibiotic use and **antimicrobial resistance**.",
        "Advising on **storage** of medicines (cool, dry, dark, out of reach of children; "
        "cold chain for vaccines and insulin) and safe **disposal of expired medicines**.",
        "Explaining **look-alike / sound-alike** hazards, expiry dates, generic equivalence "
        "and cost-effective generic substitution (Jan Aushadhi).",
        "Counselling on **lifestyle** \u2014 tobacco cessation, diet, exercise, salt "
        "restriction \u2014 and on **ORS, immunisation, family planning and iron-folic acid**.",
        "Reporting and educating about **adverse drug reactions** (pharmacovigilance, "
        "PvPI) and drug\u2013food/drug\u2013drug interactions.",
        "Health education in the pharmacy through **posters, leaflets, display boards** and "
        "participation in health days and camps.",
    ])

    h2(doc, "2.6  Benefits and Limitations")
    table(doc,
          ["Benefits", "Limitations / difficulties"],
          [["Cheapest and most cost-effective public-health intervention; needs no costly "
            "technology.",
            "Results are **slow** and not immediately visible or measurable."],
           ["Produces **permanent, self-sustaining** change because it is voluntary.",
            "Behaviour is deeply rooted in culture, custom and religion \u2014 difficult "
            "to change."],
           ["Empowers people; builds self-reliance and community participation.",
            "Illiteracy, poverty, superstition and lack of felt need obstruct it."],
           ["Improves utilisation of existing health services and reduces the load of "
            "preventable disease.",
            "Knowledge alone does not guarantee practice \u2014 the **KAP gap**."],
           ["Applicable at all levels of prevention and in all settings.",
            "Shortage of trained health educators and of evaluation of programmes."]],
          header_fill=SH_HEADER_TEAL)

    chapter_end(doc)


# ===========================================================================
# CHAPTER 3
# ===========================================================================
def chapter_03(doc):
    chapter_title(doc, 3, "Principles of Health Education")

    para(doc, "These principles are the single most frequently examined part of the health "
              "education syllabus. Learn the **name** of each principle together with one "
              "concrete example.")

    table(doc,
          ["Principle", "Meaning", "Illustration"],
          [["1.  **Credibility**",
            "The message must be **scientifically accurate**, consistent with facts and "
            "compatible with the beliefs of the community. It must come from a **trusted, "
            "respected source**. Once credibility is lost it is almost impossible to regain.",
            "A pharmacist who gives correct, unbiased drug information is believed; "
            "exaggerated claims destroy trust."],
           ["2.  **Interest**",
            "People will listen only to what interests them. Health teaching must be "
            "related to the **felt needs** of the people \u2014 a need actually perceived "
            "by them, not merely assumed by the educator.",
            "Talking about malaria during an outbreak; teaching a diabetic about foot care "
            "after an ulcer has frightened him."],
           ["3.  **Participation**",
            "Active involvement of the learner produces far better results than passive "
            "listening. The **highest degree of participation** is the hallmark of good "
            "health education \u2014 it is based on the psychological principle of active "
            "learning.",
            "Group discussion, panel discussion, workshops, demonstrations by the learner, "
            "involving village leaders in planning."],
           ["4.  **Motivation**",
            "Every person has a fundamental desire to learn; awakening this desire is "
            "motivation. **Primary motives** are inborn (sex, hunger, survival); "
            "**secondary motives** are created by outside forces (praise, rivalry, rewards, "
            "punishment, recognition).",
            "Incentives and rewards in family-planning and immunisation programmes; "
            "appreciation of a mother who completes her child's immunisation."],
           ["5.  **Comprehension**",
            "Teach at the **level of understanding** of the audience. Never use words or "
            "concepts the audience cannot follow; assess the audience's literacy and "
            "existing knowledge first.",
            "Saying \u201craised blood sugar\u201d instead of \u201chyperglycaemia\u201d; "
            "using the local dialect."],
           ["6.  **Reinforcement**",
            "Few people learn everything in a single exposure. **Repetition at intervals**, "
            "through different channels, fixes the message.",
            "Repeating the pulse-polio message by radio, poster, school children and "
            "house visits."],
           ["7.  **Learning by doing**",
            "Learning is far more effective when the learner performs the act. "
            "\u201cIf I do it, I know it.\u201d",
            "Making the mother actually prepare and taste the ORS solution rather than only "
            "hearing about it."],
           ["8.  **Known to unknown**",
            "Proceed from what the people already know to what they do not \u2014 from the "
            "simple to the complex, and from the concrete to the abstract. Use the existing "
            "knowledge as a peg on which to hang new knowledge.",
            "Explaining germs by starting from the familiar idea of \u201cdirt causes "
            "disease\u201d."],
           ["9.  **Setting an example**",
            "The educator must **practise what he preaches**. Example is more powerful than "
            "precept.",
            "A health worker who smokes cannot run a tobacco-cessation clinic credibly."],
           ["10.  **Good human relations**",
            "Sharing information, warmth, sympathy, kindness and a non-judgemental manner "
            "build the rapport on which all education rests. Approachability of the health "
            "worker is vital.",
            "Listening patiently to an anxious mother before advising her."],
           ["11.  **Feedback**",
            "The educator must obtain the reaction of the audience and modify the message, "
            "channel and method accordingly. Feedback converts one-way communication into "
            "**two-way communication**.",
            "Asking the patient to repeat back the dosage instructions \u2014 the "
            "\u201cteach-back\u201d method."],
           ["12.  **Leaders / community leaders**",
            "Work **through** the local leaders \u2014 opinion leaders, teachers, "
            "panchayat members, religious heads, ASHA \u2014 because people imitate those "
            "they respect. Leaders are the channel to the community.",
            "Training village opinion leaders as change agents for sanitation."],
           ["13.  **Soil, seed and sower**",
            "The **soil** = the community/learner, the **seed** = the message/facts, and "
            "the **sower** = the health educator. Good seed must be sown by a good sower in "
            "well-prepared soil.",
            "Community must be prepared (rapport, felt need) before the message is "
            "delivered."],
           ["14.  **Total personality / whole person**",
            "Health education must be directed to the **whole person** and to all "
            "dimensions of health, not to one disease or one organ in isolation.",
            "Counselling a hypertensive about diet, exercise, stress and tobacco, not only "
            "about tablets."],
           ["15.  **Use of multiple channels / media**",
            "No single method is adequate; combining individual, group and mass approaches "
            "reinforces the message through several senses.",
            "A camp using a film show, a demonstration and personal counselling together."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 3.1  Principles of health education")

    box(doc, "mnemonic",
        ["A convenient string for the core principles: "
         "``C I P M C R L K S G F L`` \u2192 **C**redibility, **I**nterest, "
         "**P**articipation, **M**otivation, **C**omprehension, **R**einforcement, "
         "**L**earning by doing, **K**nown to unknown, **S**etting an example, "
         "**G**ood human relations, **F**eedback, **L**eaders.",
         "Remember the trio ^^soil \u2013 seed \u2013 sower^^ = community \u2013 message "
         "\u2013 educator."])

    h2(doc, "3.1  Motivation in Detail")
    table(doc,
          ["Type", "Definition", "Examples"],
          [["Primary (biological) motives", "Inborn, unlearned drives common to all human "
            "beings.", "Hunger, thirst, sex, sleep, self-preservation, maternal drive."],
           ["Secondary (social) motives", "Acquired through learning and social "
            "interaction; created by external forces.",
            "Praise, recognition, rivalry, competition, love of children, fear of disease, "
            "desire for prestige, money, punishment."],
           ["Incentives", "Objects or conditions that arouse or sustain motivated "
            "behaviour; may be positive (reward) or negative (punishment).",
            "Cash incentive under Janani Suraksha Yojana; free supply of spectacles; "
            "certificates to \u201copen-defecation-free\u201d villages."]],
          header_fill=SH_HEADER_TEAL)

    h3(doc, "3.1.1  Maslow's Hierarchy of Needs (Basis of Motivation)")
    para(doc, "A need lower in the hierarchy must be reasonably satisfied before a higher "
              "need motivates behaviour \u2014 which is why health advice fails in a "
              "starving family.")
    table(doc,
          ["Level", "Need", "Health-education implication"],
          [["5 (highest)", "**Self-actualisation** \u2014 realising one's potential",
            "Appeals to personal excellence, fitness goals, being a role model."],
           ["4", "**Esteem** \u2014 self-respect, recognition, status",
            "Awards to model villages/mothers; praise for compliance."],
           ["3", "**Love and belonging** \u2014 affection, acceptance by the group",
            "Group activities, peer educators, mothers' meetings, self-help groups."],
           ["2", "**Safety and security** \u2014 protection, freedom from fear",
            "Immunisation, accident prevention, insurance, safe workplaces."],
           ["1 (lowest)", "**Physiological** \u2014 air, water, food, shelter, sleep, sex",
            "Nutrition and safe water must come first; teaching hygiene to a hungry "
            "community will not work."]],
          header_fill=SH_HEADER_GREEN)

    h2(doc, "3.2  Principles of Learning Applied to Health Education")
    bullets(doc, [
        "**Learning is an active process** \u2014 the learner must participate.",
        "**Learning proceeds from the known to the unknown**, simple to complex, concrete "
        "to abstract, whole to part.",
        "**Readiness** \u2014 physical, mental and emotional readiness of the learner "
        "(maturation) is essential.",
        "**Reinforcement and practice** strengthen learning; **recency** and **primacy** "
        "effects make the first and the last points best remembered.",
        "**Satisfaction and success** promote learning; repeated failure discourages it.",
        "**Multi-sensory learning** is superior \u2014 the more senses involved, the better "
        "the retention.",
        "**Transfer of learning** \u2014 what is learnt should be applicable to real life.",
        "**Individual differences** \u2014 people learn at different rates; the learning "
        "curve is not uniform (plateaus occur).",
    ])

    box(doc, "highyield",
        ["Approximate contribution of the senses to learning: ^^sight \u2248 83%^^, "
         "hearing \u2248 11%, smell \u2248 3.5%, touch \u2248 1.5%, taste \u2248 1%. "
         "Hence **visual aids are the most effective single class of aid**.",
         "Approximate retention: we remember about **10% of what we read, 20% of what we "
         "hear, 30% of what we see, 50% of what we see and hear, 70% of what we say, and "
         "~~90% of what we say and do~~** \u2014 the rationale for \u201clearning by "
         "doing\u201d (Edgar Dale's Cone of Experience)."])

    h2(doc, "3.3  Barriers to Effective Health Education")
    table(doc,
          ["Barrier", "Examples"],
          [["Physiological", "Deafness, poor vision, defective speech, fatigue, illness, "
            "pain, hunger."],
           ["Psychological", "Low intelligence, poor memory, emotional disturbance, "
            "anxiety, fear, prejudice, neurosis, hostility to the educator."],
           ["Environmental", "Noise, poor lighting, overcrowding, invisibility of the "
            "speaker, uncomfortable seating, distance, bad weather."],
           ["Cultural", "Illiteracy, language and dialect differences, customs, taboos, "
            "religious beliefs, food fads, superstition, blind faith, caste and gender norms."],
           ["Social", "Poverty, social class distance between educator and learner, "
            "unemployment, migration, lack of leadership."],
           ["Programme-related", "Poorly trained educators, unsuitable methods and media, "
            "inadequate funds, no follow-up, no evaluation, message not in local language."]],
          header_fill=SH_HEADER_PURPLE)

    chapter_end(doc)


# ===========================================================================
# CHAPTER 4
# ===========================================================================
def chapter_04(doc):
    chapter_title(doc, 4, "Ethics in Health Education")

    para(doc, "Health education deals with people's beliefs, bodies and private lives. "
              "Ethics defines the limits within which the educator may work. Ethical "
              "practice is what separates ^^health education^^ from ^^manipulation^^.")

    h2(doc, "4.1  The Core Ethical Principles")
    table(doc,
          ["Principle", "Meaning", "Application in health education"],
          [["**Autonomy** (respect for persons)",
            "The right of a competent individual to make his or her own decisions, free "
            "from coercion.",
            "Present balanced facts and let the person decide; never coerce a woman into "
            "sterilisation or a patient into a trial. **Voluntariness is the essence of "
            "health education.**"],
           ["**Beneficence**", "The duty to do good and to act in the best interest of the "
            "individual and community.",
            "Choose messages that genuinely benefit the audience; promote proven "
            "interventions."],
           ["**Non-maleficence** (__primum non nocere__)",
            "The duty to do no harm, including psychological and social harm.",
            "Avoid messages that frighten unnecessarily, stigmatise, or create guilt; avoid "
            "exaggerated fear appeals."],
           ["**Justice / equity**",
            "Fair distribution of benefits and burdens; the most needy must not be the "
            "least served.",
            "Reach the illiterate, the poor, the disabled, tribal and remote populations; "
            "materials in local languages and accessible formats."],
           ["**Veracity** (truthfulness)",
            "Obligation to tell the truth and not to deceive.",
            "Never overstate benefits or conceal risks of a drug, vaccine or procedure; "
            "correct one's own errors."],
           ["**Fidelity**", "Faithfulness to promises and to the trust reposed in the "
            "professional.", "Keep appointments and commitments made to the community."],
           ["**Confidentiality / privacy**",
            "Information obtained in a professional relationship must not be disclosed "
            "without consent.",
            "Never name an HIV-positive or TB patient in a community meeting; secure "
            "records and digital data."]],
          header_fill=SH_HEADER_BLUE, caption="Table 4.1  Core ethical principles")

    box(doc, "mnemonic",
        "The **four classical principles of bioethics** (Beauchamp & Childress) = "
        "^^A B N J^^ \u2192 **A**utonomy, **B**eneficence, **N**on-maleficence, "
        "**J**ustice.")

    h2(doc, "4.2  Informed Consent in Health Education and Research")
    bullets(doc, [
        "Consent must be **informed** (full disclosure in understandable language), "
        "**voluntary** (free of coercion or undue inducement) and given by a person "
        "**competent** to consent.",
        "The participant must be told the purpose, procedure, risks, benefits, "
        "alternatives, confidentiality safeguards and the **right to withdraw at any time "
        "without penalty**.",
        "Consent for photography, filming or the use of a patient's story or image in "
        "teaching material must be **separate and explicit**.",
        "For minors and persons unable to consent, **assent** of the individual plus "
        "consent of the parent/legal guardian is required.",
        "Research involving human participants requires clearance by an **Institutional "
        "Ethics Committee**; in India the governing document is the **ICMR National "
        "Ethical Guidelines for Biomedical and Health Research Involving Human "
        "Participants (2017)**.",
    ])

    h2(doc, "4.3  Code of Ethics for the Health Education Profession")
    para(doc, "The **Coalition of National Health Education Organizations (CNHEO)** code is "
              "the internationally quoted standard. It is arranged in six articles, each "
              "describing a set of responsibilities.")
    table(doc,
          ["Article", "Responsibility to \u2026", "Key obligations"],
          [["I", "**The public**",
            "Support the right of individuals to make informed decisions; respect diversity, "
            "values and dignity; act on issues that can adversely affect health."],
           ["II", "**The profession**",
            "Maintain and improve competence; promote the profession's integrity; give "
            "credit to others' work; avoid conflicts of interest."],
           ["III", "**Employers**",
            "Accept only responsibilities for which one is qualified; be accountable and "
            "honest about capabilities and outcomes; use resources properly."],
           ["IV", "**The delivery of health education**",
            "Use appropriate, evidence-based strategies; be truthful about the "
            "effectiveness of programmes; respect the rights of participants."],
           ["V", "**Research and evaluation**",
            "Conduct research ethically and honestly; protect privacy and dignity; report "
            "results accurately, including negative findings; avoid plagiarism and "
            "fabrication."],
           ["VI", "**Professional preparation**",
            "Select students fairly; provide quality training and supervision; act as a "
            "role model for trainees."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 4.2  CNHEO Code of Ethics for the Health Education Profession")

    h2(doc, "4.4  Common Ethical Dilemmas and Pitfalls")
    table(doc,
          ["Issue", "The ethical problem", "Correct practice"],
          [["**Victim blaming**",
            "Blaming the individual for a disease caused largely by poverty, environment or "
            "genetics \u2014 e.g. blaming a malnourished mother for her child's stunting.",
            "Address structural determinants too; use supportive, non-accusatory language."],
           ["**Fear appeals / scare tactics**",
            "Graphic images and threats may cause anxiety, denial or avoidance rather than "
            "behaviour change, especially if no realistic solution is offered.",
            "Use moderate fear **only when an effective, feasible action is simultaneously "
            "offered** (efficacy message)."],
           ["**Stigmatisation and labelling**",
            "Messages about HIV, tuberculosis, leprosy, mental illness or obesity may "
            "reinforce discrimination.",
            "Use person-first language (\u201ca person with leprosy\u201d, not \u201ca "
            "leper\u201d); involve affected people in designing messages."],
           ["**Paternalism**",
            "Deciding for people \u201cfor their own good\u201d, withholding information.",
            "Inform fully and respect the decision even if the educator disagrees."],
           ["**Conflict of interest / commercial sponsorship**",
            "Accepting support from tobacco, alcohol, infant-formula or pharmaceutical "
            "companies may bias messages.",
            "Disclose all funding; refuse sponsorship that compromises the message. Note "
            "the **IMS Act, 1992** (Infant Milk Substitutes Act) which restricts promotion "
            "of infant formula."],
           ["**Cultural insensitivity**",
            "Imposing outside norms; ignoring religion, caste, gender or local custom.",
            "Adapt messages to local culture; use local idiom, folk media and local "
            "leaders."],
           ["**Data privacy in digital health education**",
            "Mobile apps, teleconsultation and social media generate identifiable health "
            "data.", "Obtain consent for data use; anonymise; store securely; comply with "
            "applicable data-protection law."],
           ["**Misinformation and unverified claims**",
            "Forwarding unverified remedies, especially on social media, can cause direct "
            "harm.", "Verify from authoritative sources before communicating; correct "
            "misinformation promptly and respectfully."]],
          header_fill=SH_HEADER_PURPLE)

    h2(doc, "4.5  Ethics for the Pharmacist as Health Educator")
    para(doc, "In India the conduct of a registered pharmacist is governed by the "
              "**Pharmacy Act, 1948** and the **Pharmacy Practice Regulations, 2015** "
              "framed by the Pharmacy Council of India, besides the Drugs and Cosmetics "
              "Act, 1940.")
    bullets(doc, [
        "Dispense only against a **valid prescription** for prescription-only "
        "(Schedule H, H1, X) medicines; never encourage self-medication with antibiotics.",
        "Maintain **patient confidentiality**; prescription records must not be disclosed "
        "except as required by law.",
        "Give **unbiased drug information**; do not let trade incentives influence advice "
        "or substitution.",
        "Do not **claim to diagnose or to be a physician**; refer when the condition is "
        "beyond the pharmacist's scope.",
        "Keep **professional competence** current through continuing education.",
        "Display the **registration certificate**, observe conditions of the drug licence, "
        "and maintain prescribed registers (including Schedule H1 register).",
        "Never advertise medicines in a manner prohibited by the **Drugs and Magic "
        "Remedies (Objectionable Advertisements) Act, 1954**.",
    ])

    box(doc, "highyield",
        ["The single most quoted ethical requirement of health education is that behaviour "
         "change must be ^^voluntary and informed^^ \u2014 any element of force converts "
         "education into coercion.",
         "Confidentiality may be **legally overridden** in narrow situations such as "
         "notification of a notifiable disease or a court order \u2014 recognised as "
         "\u201cprivileged communication\u201d."])

    chapter_end(doc)



# ===========================================================================
# CHAPTER 5
# ===========================================================================
def chapter_05(doc):
    chapter_title(doc, 5, "The Health Educator \u2014 Attributes, Roles and Responsibilities")

    defn(doc, "Health educator",
         "A person who, by training and function, helps individuals, families and "
         "communities to acquire the knowledge, attitudes and skills needed to protect and "
         "promote their health. **Every health worker is a health educator**, but some "
         "\u2014 health education officers, extension educators, counsellors \u2014 are "
         "specialists in it.")

    h2(doc, "5.1  Attributes / Qualities of a Good Health Educator")
    para(doc, "Attributes are conventionally grouped as **personal, professional and "
              "social**. This grouping makes the long list easy to reproduce in an "
              "examination.")

    h3(doc, "5.1.1  Personal Attributes")
    table(doc,
          ["Attribute", "Why it matters"],
          [["**Good personality and pleasant appearance**",
            "Creates the first favourable impression; neat, clean, appropriately dressed."],
           ["**Sound physical and mental health**",
            "The educator is a **living example** of what he teaches; personal hygiene and "
            "healthy habits carry more weight than words."],
           ["**Sincerity, honesty and integrity**",
            "The basis of credibility; never misleads, never exaggerates."],
           ["**Patience, tolerance and perseverance**",
            "Behaviour change is slow; resistance, ridicule and failure must be absorbed "
            "without irritation."],
           ["**Empathy and sympathy**",
            "The ability to feel with the people and to see the problem from their point of "
            "view; **empathy, not pity**."],
           ["**Emotional stability, self-control and cheerfulness**",
            "Anger, sarcasm or discouragement destroys rapport."],
           ["**Humility and a non-judgemental attitude**",
            "Never talks down to people, never ridicules beliefs however irrational."],
           ["**Enthusiasm, initiative and resourcefulness**",
            "Improvises aids from locally available material; works with limited resources."],
           ["**Sense of humour**",
            "Holds attention, relieves tension and makes the message memorable."],
           ["**Punctuality, reliability and self-discipline**",
            "Keeping appointments with the community builds trust."]],
          header_fill=SH_HEADER_BLUE)

    h3(doc, "5.1.2  Professional Attributes")
    table(doc,
          ["Attribute", "Content"],
          [["**Sound and up-to-date knowledge**",
            "Of health sciences, the local disease pattern, national health programmes and "
            "the services available; must keep learning continuously."],
           ["**Mastery of the subject to be taught**",
            "Able to answer questions accurately and to admit frankly when he does not know."],
           ["**Skill in communication**",
            "Clear speech, correct use of the **local language and idiom**, good listening, "
            "effective use of non-verbal cues."],
           ["**Skill in teaching methods and media**",
            "Able to select and use individual, group and mass methods and to prepare and "
            "handle audio-visual aids."],
           ["**Ability to plan, organise and evaluate**",
            "Needs assessment, objective setting, budgeting, record-keeping, monitoring and "
            "evaluation."],
           ["**Leadership and organising ability**",
            "Can mobilise the community, form committees, coordinate with other sectors."],
           ["**Research and analytical ability**",
            "Can carry out a KAP survey, interpret data and use evidence."],
           ["**Professional ethics**",
            "Confidentiality, respect for autonomy, truthfulness (Chapter 4)."],
           ["**Willingness to work as a team member**",
            "Health education is a team activity involving doctors, nurses, pharmacists, "
            "ASHA, teachers and voluntary agencies."]],
          header_fill=SH_HEADER_TEAL)

    h3(doc, "5.1.3  Social Attributes")
    bullets(doc, [
        "**Knowledge of the community** \u2014 its culture, customs, beliefs, taboos, "
        "social structure, caste and religious composition, festivals and economy.",
        "**Acceptance by the community** \u2014 preferably drawn from or resident in the "
        "community; ability to identify and work through **local leaders**.",
        "**Good human relations and social skills** \u2014 friendliness, approachability, "
        "the ability to mix freely with all sections without discrimination.",
        "**Respect for local culture** \u2014 modifies the message to fit the culture "
        "rather than attacking the culture.",
        "**Democratic outlook** \u2014 encourages participation and shared decision-making "
        "rather than issuing orders.",
    ])

    box(doc, "mnemonic",
        "Qualities of a health educator in one line \u2014 ^^\u201cK\u2013A\u2013S\u201d^^: "
        "**K**nowledge (sound and current), **A**ttitude (empathy, patience, honesty, "
        "non-judgemental), **S**kills (communication, teaching, planning, evaluation, "
        "leadership).")

    h2(doc, "5.2  Areas of Responsibility of a Health Educator")
    para(doc, "The **National Commission for Health Education Credentialing (NCHEC)** "
              "framework is the standard statement of what a health educator is responsible "
              "for. The classical form lists **seven areas**; the current (2020) model "
              "lists **eight**.")
    table(doc,
          ["Area", "Responsibility", "Typical tasks"],
          [["I", "**Assessment of needs and capacity**",
            "Collect and analyse data on health status, behaviours, determinants, existing "
            "resources; identify priority needs (KAP surveys, community diagnosis)."],
           ["II", "**Planning**",
            "Involve stakeholders, set SMART objectives, select theory-based strategies, "
            "prepare a work plan, budget and timeline."],
           ["III", "**Implementation**",
            "Deliver the programme, train staff and volunteers, monitor progress, adapt to "
            "field realities."],
           ["IV", "**Evaluation and research**",
            "Design evaluation, collect and interpret data, measure process, impact and "
            "outcome; disseminate findings."],
           ["V", "**Advocacy**",
            "Influence policy, legislation and resource allocation for health; build "
            "coalitions (this is a separate area in the 2020 model)."],
           ["VI", "**Communication**",
            "Determine the message and audience, select channels, develop and pre-test "
            "materials, deliver and evaluate the communication."],
           ["VII", "**Leadership and management**",
            "Administer programmes, manage people, budgets, materials and partnerships; "
            "ensure accountability."],
           ["VIII", "**Ethics and professionalism**",
            "Practise within the code of ethics, maintain competence, serve as a resource "
            "person and mentor, contribute to the profession."]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 5.1  NCHEC areas of responsibility")

    box(doc, "highyield",
        "The classical **seven areas of responsibility** are often asked as: assess needs; "
        "plan; implement; conduct evaluation/research; **administer and manage**; **serve "
        "as a health education resource person**; **communicate and advocate**. "
        "The credential awarded in the USA is ^^CHES^^ (Certified Health Education "
        "Specialist), instituted in **1988** by NCHEC.")

    h2(doc, "5.3  Functions of the Health Educator in the Field")
    bullets(doc, [
        "Carrying out **community diagnosis** and identifying felt needs.",
        "Planning, conducting and evaluating **health education programmes and campaigns**.",
        "Preparing, pre-testing and distributing **IEC material** in the local language.",
        "**Training** health workers, ASHA, anganwadi workers, teachers, dais and "
        "volunteers in health education skills.",
        "Acting as a **resource person and consultant** to other departments and voluntary "
        "agencies.",
        "Organising **school health education**, health exhibitions, health melas, camps "
        "and observance of health days.",
        "**Intersectoral coordination** with education, agriculture, rural development, "
        "water supply, ICDS and panchayati raj institutions.",
        "**Advocacy** with administrators and elected representatives for health-supportive "
        "policies.",
        "**Research and record-keeping**: KAP studies, operational research, reports and "
        "documentation.",
        "Providing **feedback** to programme managers about community response and "
        "misconceptions.",
    ])

    h2(doc, "5.4  The Health Education Workforce in India")
    table(doc,
          ["Functionary", "Level", "Health education role"],
          [["**ASHA** (Accredited Social Health Activist)",
            "Village \u2014 one per 1000 population (relaxed in tribal/hilly areas)",
            "The **first port of call** and the principal **change agent** for health "
            "education at village level; created under NRHM in **2005**; an honorary "
            "volunteer paid by performance-based incentives; holds the drug kit and "
            "promotes institutional delivery, immunisation, ORS and family planning."],
           ["**ANM / MPW (Female)** \u2014 Auxiliary Nurse Midwife",
            "Sub-centre \u2014 one per 5000 (3000 in hilly/tribal)",
            "Antenatal, natal and postnatal education, immunisation, family planning "
            "counselling, nutrition and hygiene education."],
           ["**MPW (Male) / MHW**", "Sub-centre",
            "Education on communicable disease control, environmental sanitation, "
            "vector control, safe water."],
           ["**Anganwadi Worker (AWW)**", "Anganwadi \u2014 one per 400\u2013800 population "
            "(ICDS, launched **1975**)",
            "Nutrition and health education (NHED) to women 15\u201345 years, "
            "supplementary nutrition, pre-school education, growth monitoring."],
           ["**Health Worker / Health Assistant (LHV)**", "Sub-centre / PHC",
            "Supervision and on-the-job training of field workers in health education."],
           ["**Block Extension Educator (BEE)**", "Block / PHC",
            "The designated **health education specialist at block level**; plans and "
            "conducts IEC activities, trains workers, maintains aids and equipment."],
           ["**District Extension and Media Officer (DEMO) / District Health Education "
            "Officer**", "District",
            "Coordinates all district IEC activity, media liaison, exhibitions, supply of "
            "material, supervision of BEEs."],
           ["**State Health Education Bureau / State IEC Bureau**", "State",
            "Plans state-level IEC strategy, produces material, trains district staff."],
           ["**Central Health Education Bureau (CHEB)**", "National",
            "Apex national body for health education (see Chapter 9)."],
           ["**Pharmacist**", "PHC / CHC / hospital / community pharmacy",
            "Patient counselling, drug adherence, rational drug use, ADR reporting, "
            "storage and disposal advice, display of IEC material."]],
          header_fill=SH_HEADER_PURPLE,
          caption="Table 5.2  Health education functionaries in India")

    h2(doc, "5.5  Difficulties Faced by the Health Educator")
    bullets(doc, [
        "**Illiteracy, poverty and superstition** in the community; blind faith in "
        "quacks and magico-religious remedies.",
        "**Absence of a felt need** \u2014 people do not perceive the problem as important.",
        "**Cultural and language barriers**; resistance to change deep-rooted customs.",
        "**Too few trained health educators**; health education added as an extra duty to "
        "already overburdened staff.",
        "**Inadequate funds, transport and audio-visual equipment**; material not adapted "
        "to the local language or culture.",
        "**Lack of coordination** between health and other departments.",
        "**Absence of evaluation** \u2014 programmes continue without knowing whether they "
        "work.",
        "**Misinformation on social media** competing with scientific messages.",
    ])

    chapter_end(doc)


# ===========================================================================
# CHAPTER 6
# ===========================================================================
def chapter_06(doc):
    chapter_title(doc, 6, "Communication \u2014 The Vehicle of Health Education")

    para(doc, "Health education is delivered through communication; therefore the theory of "
              "communication is an examinable part of this unit.")

    defn(doc, "Communication",
         "The **two-way process of exchanging or sharing of ideas, facts, feelings and "
         "impressions** between a source and a receiver in such a way that there is common "
         "understanding. Derived from the Latin __communis__ = \u201ccommon\u201d.")

    h2(doc, "6.1  Aims and Functions of Communication")
    bullets(doc, [
        "To **inform** \u2014 transfer of knowledge and skills.",
        "To **educate** \u2014 produce understanding and change in attitude.",
        "To **motivate and persuade** \u2014 create the desire to act.",
        "To **change behaviour** and to sustain it.",
        "To **change social norms** and to advocate policy.",
        "To provide **entertainment with education** (\u201cedutainment\u201d, folk media).",
    ])

    h2(doc, "6.2  Elements of the Communication Process")
    table(doc,
          ["Element", "Description", "Requirement for effectiveness"],
          [["**Sender / Source / Communicator**",
            "The originator of the message \u2014 the health educator.",
            "Credibility, knowledge of the subject and of the audience, communication skill, "
            "positive attitude."],
           ["**Message**", "The information, idea or attitude to be transmitted; its "
            "content, treatment and code.",
            "Must be **meaningful, clear, simple, specific, timely, accurate, culturally "
            "acceptable and interesting**; fitted to the felt need."],
           ["**Channel / Medium**", "The physical route by which the message travels.",
            "Interpersonal (face to face), mass media (radio, TV, press), traditional/folk "
            "media, digital media. Use **more than one channel**."],
           ["**Receiver / Audience**", "The individual, group or community for whom the "
            "message is meant.",
            "Message must be matched to age, education, culture, felt needs and readiness of "
            "the audience (**audience segmentation**)."],
           ["**Feedback**", "The flow of information from the receiver back to the sender.",
            "Converts one-way into **two-way communication**; permits correction of the "
            "message. Its absence is the biggest weakness of mass media."],
           ["**Noise**", "Any distortion or interference that reduces fidelity.",
            "Physical (traffic sound), physiological (deafness), psychological (prejudice), "
            "semantic (wrong words). Must be minimised."],
           ["**Effect / Outcome**", "The observable change produced in the receiver.",
            "Change in knowledge, attitude or practice; the real measure of success."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 6.1  Elements of communication")

    box(doc, "mnemonic",
        ["**SMCRF** \u2192 ^^S^^ender \u2192 ^^M^^essage \u2192 ^^C^^hannel \u2192 "
         "^^R^^eceiver \u2192 ^^F^^eedback (plus **noise** acting throughout).",
         "**Berlo's model (1960)** is the classic ``S-M-C-R`` model. "
         "**Lasswell's formula (1948)** asks: ~~Who says What in Which channel to Whom with "
         "What effect?~~  **Shannon\u2013Weaver (1949)** added the concept of **noise**."])

    h2(doc, "6.3  Types of Communication")
    table(doc,
          ["Basis", "Types", "Notes"],
          [["Direction", "**One-way** (didactic) vs **two-way** (Socratic)",
            "One-way = lecture, radio, poster: speedy, reaches many, but no feedback, "
            "little learning, listener passive. Two-way = discussion, counselling: slower "
            "but produces real learning. **Two-way is superior for health education.**"],
           ["Mode", "**Verbal** vs **Non-verbal**",
            "Non-verbal (gestures, posture, facial expression, eye contact, touch, "
            "silence, dress, distance) may carry **more weight than words** and can "
            "contradict them."],
           ["Number of persons", "**Intrapersonal, interpersonal, group, mass**",
            "Interpersonal is the most effective for behaviour change; mass is the most "
            "efficient for awareness."],
           ["Formality", "**Formal** (through official channels) vs **informal** "
            "(grapevine)",
            "Informal channels spread fast and are often more believed \u2014 useful but "
            "also the route of rumours."],
           ["Sensory channel", "**Visual, auditory, audio-visual, tactile, olfactory**",
            "Audio-visual is most effective because it engages two senses."],
           ["Purpose", "**Didactic, Socratic, therapeutic, mass, group**",
            "Therapeutic communication is used in counselling and patient care."]],
          header_fill=SH_HEADER_TEAL)

    h2(doc, "6.4  Barriers to Communication")
    table(doc,
          ["Barrier", "Examples", "Remedy"],
          [["**Physiological**", "Deafness, poor vision, defective speech, fatigue, pain, "
            "hunger, difficulty in understanding due to low intelligence.",
            "Speak clearly and loudly, use visual aids, keep sessions short, treat the "
            "underlying problem."],
           ["**Psychological**", "Emotional disturbance, anxiety, fear, prejudice, "
            "hostility, low motivation, neurosis, poor memory, **levels of "
            "perception**.",
            "Build rapport first, reduce anxiety, be non-judgemental, repeat and reinforce."],
           ["**Environmental**", "Noise, poor lighting, overcrowding, distance, invisibility "
            "of the speaker, congested room, bad weather.",
            "Choose a quiet, well-lit, adequately sized venue; use a microphone; seat the "
            "audience so all can see."],
           ["**Cultural**", "Illiteracy, language and dialect, customs, taboos, religious "
            "beliefs, food fads, blind faith, caste and gender norms, economic and social "
            "class differences.",
            "Use local language and idiom, folk media and local leaders; adapt the message "
            "to culture."],
           ["**Semantic / linguistic**", "Technical jargon, medical terminology, "
            "abbreviations, words with different local meanings.",
            "Use simple everyday words; test the material on a sample audience "
            "(**pre-testing**)."],
           ["**Social**", "Poverty, unemployment, social distance between educator and "
            "community, lack of leadership.",
            "Work through community structures; address underlying social needs."]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 6.2  Barriers to communication and their remedies")

    h2(doc, "6.5  The Seven C's of Effective Communication")
    table(doc,
          ["C", "Requirement"],
          [["**Clear**", "The message must be unambiguous and easily understood."],
           ["**Concise**", "Short, to the point, free of unnecessary detail."],
           ["**Concrete**", "Specific and vivid, with facts and figures rather than vague "
            "generalities."],
           ["**Correct**", "Scientifically accurate, free of error in fact and language."],
           ["**Coherent**", "Logically organised and consistent; one idea leads to the next."],
           ["**Complete**", "Contains everything the receiver needs in order to act."],
           ["**Courteous**", "Respectful, considerate of the receiver's feelings and "
            "culture."]],
          header_fill=SH_HEADER_PURPLE, fractions=[0.16, 0.84])

    h2(doc, "6.6  Health Communication and BCC")
    bullets(doc, [
        "**Health communication** is the study and use of communication strategies to "
        "inform and influence individual and community decisions that enhance health.",
        "**BCC (Behaviour Change Communication)** is an interactive, research-based process "
        "that develops tailored messages through a mix of channels to encourage and sustain "
        "positive behaviour. Its steps: ``situation analysis \u2192 audience segmentation "
        "\u2192 message design \u2192 channel selection \u2192 pre-testing \u2192 "
        "implementation \u2192 monitoring \u2192 evaluation``.",
        "**Counselling** is a two-way, non-directive, confidential process that helps a "
        "person to understand a problem and arrive at his own decision. Widely used in "
        "HIV (pre-test and post-test counselling), family planning, tobacco cessation and "
        "medication adherence.",
        "**Pre-testing** of every message and material on a sample of the target audience "
        "is mandatory good practice \u2014 it checks comprehension, attraction, "
        "acceptability, involvement and persuasion.",
    ])

    box(doc, "note",
        "In counselling the pharmacist should use the ^^teach-back (show-back) method^^: "
        "after explaining, ask the patient to repeat the instructions or demonstrate the "
        "technique. This is the practical application of the principle of **feedback**.")

    chapter_end(doc)


# ===========================================================================
# CHAPTER 7
# ===========================================================================
def chapter_07(doc):
    chapter_title(doc, 7, "Essential Steps in Health Education")

    para(doc, "The syllabus phrase \u201cessential steps\u201d is used in two senses, and "
              "both are examined. **(A)** the psychological steps through which an "
              "individual passes on the way from ignorance to sustained action, and "
              "**(B)** the managerial steps in planning and running a health education "
              "programme. Learn both.")

    # ---------------- A
    h2(doc, "7.1  Part A \u2014 The Psychological / Behavioural Steps")
    table(doc,
          ["Step", "What happens", "What the educator does"],
          [["1.  **Gaining entry and building rapport**",
            "The educator becomes known and accepted; confidence is established.",
            "Meet community leaders, be introduced by a trusted person, be courteous, "
            "listen first."],
           ["2.  **Capturing attention / creating awareness**",
            "The individual becomes **aware** that the problem and a solution exist. "
            "Awareness is created mainly through **mass media**.",
            "Use posters, radio, TV, exhibitions, folk media, health days."],
           ["3.  **Arousing interest and creating a felt need**",
            "The person begins to feel that the problem concerns **him personally** and "
            "seeks more information.",
            "Relate the message to his own life and family; supply details; group "
            "discussion."],
           ["4.  **Motivation and desire (evaluation stage)**",
            "The person weighs the advantages and disadvantages and develops the **desire** "
            "to act. This is the crucial and most difficult step.",
            "Interpersonal counselling, testimonials of adopters, demonstration of benefit, "
            "incentives."],
           ["5.  **Decision-making**",
            "The individual makes up his mind to try the new practice.",
            "Remove doubts, answer objections, make the action easy and available."],
           ["6.  **Action / trial and adoption**",
            "He actually performs the behaviour \u2014 first on trial, then permanently.",
            "Provide the means (ORS packets, latrine, contraceptive, vaccine), teach the "
            "skill by **learning by doing**."],
           ["7.  **Reinforcement, follow-up and maintenance**",
            "The new behaviour is repeated until it becomes a habit; relapse is prevented.",
            "Repeat visits, praise, support groups, continuing reminders, family support."],
           ["8.  **Evaluation**",
            "The educator measures whether knowledge, attitude and practice actually "
            "changed.", "KAP survey, records, coverage data, feedback for redesign."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 7.1  Essential steps in health education (behavioural sequence)")

    box(doc, "mnemonic",
        "Core sequence to recite: ^^Awareness \u2192 Interest \u2192 Motivation/Desire "
        "\u2192 Decision \u2192 Action \u2192 Maintenance^^. Several textbooks compress it "
        "into **four essential steps: awareness, motivation, decision-making and action**.")

    h3(doc, "7.1.1  Rogers' Stages of Adoption of an Innovation")
    table(doc,
          ["Stage", "Description"],
          [["**Awareness**", "The person learns for the first time that the new idea or "
            "practice exists."],
           ["**Interest**", "He wants to know more and actively seeks information."],
           ["**Evaluation**", "He mentally weighs the pros and cons and applies it to his "
            "own situation."],
           ["**Trial**", "He tries the practice on a small scale."],
           ["**Adoption**", "Satisfied with the trial, he accepts it permanently and "
            "becomes an advocate for it."]],
          header_fill=SH_HEADER_TEAL, fractions=[0.20, 0.80])

    table(doc,
          ["Adopter category", "Share of population", "Character"],
          [["**Innovators**", "\u2248 2.5%", "Venturesome, cosmopolite, first to try; often "
            "not respected locally."],
           ["**Early adopters**", "\u2248 13.5%", "**Local opinion leaders** \u2014 the most "
            "important group to target because others imitate them."],
           ["**Early majority**", "\u2248 34%", "Deliberate, adopt just before the average "
            "person."],
           ["**Late majority**", "\u2248 34%", "Sceptical, adopt under peer pressure or "
            "economic necessity."],
           ["**Laggards**", "\u2248 16%", "Traditional, suspicious of change, last to "
            "adopt."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 7.2  Rogers' adopter categories")

    # ---------------- B
    h2(doc, "7.2  Part B \u2014 Steps in Planning a Health Education Programme")
    numbered(doc, [
        "**Community diagnosis / needs assessment.** Collect data on demography, disease "
        "pattern, existing KAP, felt needs, resources, culture and leadership. Methods: "
        "survey, records, interviews, focus-group discussion, observation.",
        "**Setting priorities.** Rank problems by magnitude, severity, feasibility of "
        "control, community concern and cost. One cannot do everything at once.",
        "**Formulating objectives.** Write **SMART** objectives in the three domains "
        "(knowledge, attitude, practice), stating who will do what, how much and by when.",
        "**Identifying and segmenting the target audience.** Primary audience (those whose "
        "behaviour must change), secondary audience (those who influence them \u2014 "
        "husbands, mothers-in-law, teachers) and tertiary audience (policy makers).",
        "**Selecting the content.** Accurate, relevant, need-based, culturally acceptable, "
        "limited to a few key messages.",
        "**Selecting methods and media.** Match the method to the objective, audience size, "
        "literacy, resources and time (Chapter 8). Combine individual, group and mass "
        "approaches.",
        "**Preparing and pre-testing the material.** Develop aids, then pre-test on a "
        "sample of the audience for comprehension, attractiveness, acceptability and "
        "persuasiveness; revise accordingly.",
        "**Planning the resources.** Manpower, money, material, transport, time; prepare a "
        "budget and a time schedule (Gantt chart).",
        "**Training the personnel.** Orient and train the workers, volunteers and leaders "
        "who will deliver the programme.",
        "**Implementation.** Carry out the plan, supervise, maintain records, and "
        "co-ordinate with other sectors.",
        "**Monitoring.** Continuous checking during implementation that activities are "
        "going as planned; make mid-course corrections.",
        "**Evaluation.** Measure achievement against the objectives \u2014 see \u00a77.4.",
        "**Feedback and replanning.** Use the evaluation findings to modify the programme; "
        "the cycle then repeats.",
    ])

    box(doc, "highyield",
        "The **first and most essential step** in planning any health education programme "
        "is ^^assessment of the needs of the community (community diagnosis)^^, and the "
        "needs must be the **felt needs** of the people. The **last** step is "
        "**evaluation with feedback**, which makes the process a continuous cycle.")

    h2(doc, "7.3  Theories and Models Used to Plan Health Education")
    table(doc,
          ["Model / theory", "Key constructs", "Use"],
          [["**Health Belief Model** (Hochbaum, Rosenstock, Kegels \u2014 1950s)",
            "Perceived **susceptibility**, perceived **severity**, perceived **benefits**, "
            "perceived **barriers**, **cues to action**, **self-efficacy**.",
            "Explains why people do or do not take a preventive action such as screening or "
            "immunisation. The **oldest and most widely used** model in health education."],
           ["**PRECEDE\u2013PROCEED model** (Lawrence Green)",
            "PRECEDE = **P**redisposing, **R**einforcing and **E**nabling **C**onstructs in "
            "**E**ducational **D**iagnosis and **E**valuation; PROCEED = **P**olicy, "
            "**R**egulatory and **O**rganizational **C**onstructs in **E**ducational and "
            "**E**nvironmental **D**evelopment.",
            "The standard **framework for planning and evaluating** a health education "
            "programme; works **backwards** from the desired outcome."],
           ["**Transtheoretical / Stages of Change model** (Prochaska & DiClemente)",
            "**Pre-contemplation \u2192 Contemplation \u2192 Preparation \u2192 Action "
            "\u2192 Maintenance** (\u00b1 relapse and termination).",
            "Matching the intervention to the person's stage of readiness; widely used in "
            "tobacco, alcohol and obesity work."],
           ["**Theory of Reasoned Action / Planned Behaviour** (Ajzen & Fishbein)",
            "Attitude towards the behaviour + subjective norm (+ perceived behavioural "
            "control) \u2192 **intention** \u2192 behaviour.",
            "Shows that **intention** is the immediate determinant of behaviour and that "
            "social norms matter."],
           ["**Social Cognitive / Social Learning Theory** (Bandura)",
            "Observational learning (modelling), **self-efficacy**, reciprocal determinism, "
            "reinforcement, outcome expectations.",
            "Basis of peer education, demonstrations and role models; the source of the "
            "important concept of **self-efficacy**."],
           ["**Diffusion of Innovations** (Everett Rogers)",
            "Innovation, communication channels, time, social system; adopter categories.",
            "Explains how new practices spread through a community and identifies opinion "
            "leaders."],
           ["**Social ecological model**",
            "Individual \u2192 interpersonal \u2192 organisational \u2192 community "
            "\u2192 public policy levels.",
            "Reminds the educator that behaviour is nested in an environment; intervene at "
            "several levels."]],
          header_fill=SH_HEADER_PURPLE,
          caption="Table 7.3  Behaviour change models")

    h2(doc, "7.4  Evaluation of Health Education")
    table(doc,
          ["Type of evaluation", "Question answered", "Indicators"],
          [["**Formative**", "Is the material suitable __before__ full-scale launch?",
            "Pre-testing results, comprehension and acceptability of messages."],
           ["**Process (monitoring)**",
            "Was the programme delivered as planned?",
            "Number of sessions held, people reached, materials distributed, quality of "
            "sessions, cost incurred, coverage."],
           ["**Impact**", "Did knowledge, attitude and behaviour change?",
            "KAP scores before and after, proportion practising the behaviour, service "
            "utilisation rates."],
           ["**Outcome**", "Did health status improve?",
            "Incidence and prevalence of disease, morbidity, mortality, nutritional status, "
            "immunisation coverage."],
           ["**Summative**", "Was the whole programme worth it?",
            "Overall achievement of objectives, cost-effectiveness, sustainability."]],
          header_fill=SH_HEADER_GREEN)

    bullets(doc, [
        "Evaluation must be **built into the programme from the planning stage**, not added "
        "at the end.",
        "**Baseline data** collected before the intervention are essential for measuring "
        "change.",
        "Common designs: before\u2013after (pre-test/post-test) in one group; comparison "
        "with a control group; and time-trend analysis.",
        "Evaluation should be **participatory** \u2014 involving the community itself.",
    ])

    chapter_end(doc)



# ===========================================================================
# CHAPTER 8
# ===========================================================================
def chapter_08(doc):
    chapter_title(doc, 8, "Methods of Health Education")

    para(doc, "This is the largest and most heavily examined chapter of the unit. The "
              "methods of health education are classified by the **size of the audience "
              "reached** into three main approaches.")

    box(doc, "highyield",
        ["The ^^three main methods (approaches) of health education^^ are: "
         "**(1) Individual approach, (2) Group approach, (3) Mass approach.**",
         "**Individual** methods are the **most effective for behaviour change** but reach "
         "the fewest people. **Mass** methods reach the largest numbers but are least "
         "effective in changing behaviour. **Group** methods lie in between and are the "
         "most widely used in practice."])

    table(doc,
          ["Approach", "Methods included", "Reach", "Effectiveness for behaviour change"],
          [["**Individual**", "Personal contact, health counselling, patient interview, "
            "home visit, personal letter", "Very few", "**Highest** \u2014 permits full "
            "two-way communication and tailoring"],
           ["**Group**", "Lecture, demonstration, group discussion, panel discussion, "
            "symposium, workshop, seminar, conference, role play, buzz session, "
            "brainstorming, case study, field trip", "Moderate", "High \u2014 peer "
            "interaction reinforces learning"],
           ["**Mass**", "Television, radio, newspapers, printed matter, films, posters, "
            "exhibitions, health museums, folk media, internet and social media, mHealth",
            "Very large", "**Lowest** \u2014 good for awareness, poor for behaviour change; "
            "no feedback"]],
          header_fill=SH_HEADER_BLUE, align_center_cols=[2],
          caption="Table 8.1  The three approaches compared")

    # ------------------------------------------------ individual
    h2(doc, "8.1  Individual Approach")
    h3(doc, "8.1.1  Personal Contact / Individual Health Teaching")
    bullets(doc, [
        "Takes place whenever a health worker meets a person \u2014 in the clinic, the "
        "pharmacy, the home or the field. **Every contact is an opportunity for health "
        "education.**",
        "**Advantages:** full two-way communication; the message can be tailored to the "
        "individual's problem, language and level; doubts can be cleared on the spot; "
        "confidence and rapport develop; questions can be asked freely; privacy is "
        "possible; immediate feedback.",
        "**Limitations:** reaches only one person at a time; time-consuming and expensive "
        "per head; depends entirely on the skill and attitude of the worker; the number of "
        "workers available is limited.",
    ])

    h3(doc, "8.1.2  Health Counselling")
    bullets(doc, [
        "A **face-to-face, two-way, confidential and non-directive** process in which the "
        "counsellor helps the client to understand his problem, examine the alternatives "
        "and **arrive at his own decision**.",
        "Essentials: privacy, adequate time, active listening, empathy, an accepting and "
        "non-judgemental attitude, confidentiality, and **no imposition of the "
        "counsellor's own values**.",
        "Steps: establishing rapport \u2192 identifying the problem \u2192 exploring "
        "feelings and alternatives \u2192 helping the client decide \u2192 supporting "
        "action \u2192 follow-up.",
        "**Uses:** genetic counselling, marital and pre-marital counselling, family "
        "planning, HIV pre-test and post-test counselling, tobacco and alcohol cessation, "
        "nutrition, adolescent health, and **medication counselling by the pharmacist**.",
        "**GATHER** approach in counselling: **G**reet, **A**sk, **T**ell, **H**elp, "
        "**E**xplain, **R**eturn/refer.",
    ])

    h3(doc, "8.1.3  Home Visit")
    bullets(doc, [
        "Education in the family's own surroundings, where the real problems (water "
        "storage, kitchen, latrine, ventilation, vector breeding) can be seen and "
        "discussed.",
        "**Advantages:** builds excellent rapport; allows the whole family to be involved; "
        "practical problems become visible; ideal for the housebound, the elderly and "
        "postnatal mothers.",
        "**Limitations:** very time-consuming, costly, requires transport; reaches few "
        "families; may be resented as intrusion if not properly announced.",
    ])

    # ------------------------------------------------ group
    h2(doc, "8.2  Group Approach")
    para(doc, "A group is an audience assembled for a common purpose. Group methods use the "
              "**dynamics of the group** \u2014 peer influence, discussion and shared "
              "decision-making \u2014 to reinforce learning. The composition of the group "
              "(mothers, school children, industrial workers, patients) decides the method "
              "and the message.")

    h3(doc, "8.2.1  Lecture")
    bullets(doc, [
        "A talk given by one person to an audience; the oldest and most widely misused "
        "method.",
        "The audience should **not exceed about 30 people**, and the lecture should not "
        "exceed **15\u201320 minutes** of effective attention span.",
        "**Essentially one-way communication** \u2014 hence its greatest defect: the "
        "audience is passive and there is little feedback and little learning.",
        "**Advantages:** economical of time; covers much information; suitable for "
        "presenting new knowledge to a literate audience; good for introducing a topic.",
        "**Limitations:** no participation; retention poor; unsuitable for illiterate or "
        "uninterested audiences; attention falls rapidly.",
        "**Improved by:** using audio-visual aids, examples and humour, asking questions, "
        "allowing discussion at the end, and good voice modulation and eye contact.",
    ])

    h3(doc, "8.2.2  Demonstration")
    bullets(doc, [
        "A **carefully prepared presentation showing how to perform a skill or procedure**, "
        "with an explanation of the underlying principle \u2014 \u201cseeing is "
        "believing\u201d.",
        "It should be followed by a **return demonstration (re-demonstration) by the "
        "learner** \u2014 this converts it into learning by doing and is the single most "
        "effective group method for teaching skills.",
        "**Examples:** preparation of ORS, hand-washing steps, use of a metered-dose "
        "inhaler or insulin pen, breast-feeding position, preparation of weaning food, "
        "cooking demonstration, use of a condom, bandaging and first aid.",
        "**Requirements:** all must be able to see; keep the group small; use real "
        "articles; perform slowly, step by step; explain while doing; repeat; check "
        "understanding.",
        "**Advantages:** holds attention, uses several senses, teaches skills, highly "
        "convincing. **Limitations:** needs preparation, equipment and a small group; "
        "time-consuming.",
    ])

    h3(doc, "8.2.3  Discussion Methods")
    table(doc,
          ["Method", "Group size / structure", "How it is conducted", "Value and limits"],
          [["**Group discussion**",
            "**6\u201312 participants** (ideal); seated in a **circle or semicircle** so "
            "all can see one another; has a **group leader (chairman)** and a **recorder** "
            "or secretary.",
            "The leader introduces the topic, keeps the discussion on track, encourages "
            "the silent and restrains the talkative, and sums up. The recorder notes the "
            "points and prepares the report.",
            "Considered **one of the most effective methods** \u2014 maximum "
            "participation, free exchange of ideas, group decision. Fails if the group is "
            "too large, if a few dominate, or if the leader is autocratic."],
           ["**Panel discussion**",
            "**4\u20138 panellists** (experts) with a **chairman/moderator**, before an "
            "audience.",
            "The chairman introduces the subject and the panellists, who discuss the topic "
            "among themselves for about 30\u201345 minutes; the audience then puts "
            "questions. There are **no set speeches**.",
            "Presents several viewpoints on a controversial topic; stimulating. Depends "
            "heavily on the chairman and on informed panellists; the audience is largely "
            "passive."],
           ["**Symposium**",
            "A series of **2\u20135 speakers**, each an expert, with a chairman.",
            "Each speaker delivers a **prepared speech** on one aspect of the subject; "
            "there is **no discussion among the speakers**. The chairman sums up at the "
            "end and the audience may ask questions.",
            "Thorough, authoritative coverage of a subject. More formal and less "
            "interactive than a panel discussion."],
           ["**Workshop**",
            "A large group divided into **small working groups** of 4\u201310, each with a "
            "leader and recorder; has a chairman and resource persons.",
            "Consists of **individual and group work**: the participants learn by doing, "
            "produce material, solve problems, then report back to the plenary session. "
            "Lasts from a day to several weeks.",
            "Excellent for developing **skills** and for producing a concrete output "
            "(e.g. a training module). Needs careful organisation and resources."],
           ["**Seminar**",
            "A group of students or workers with an expert leader.",
            "One member presents a paper on a topic which is then discussed by all.",
            "Good for in-depth academic study; needs a literate, prepared group."],
           ["**Conference**",
            "A large formal assembly of professionals.",
            "Papers are read, sessions and workshops are held, resolutions are passed.",
            "Good for exchange of knowledge and for advocacy; expensive; reaches "
            "professionals rather than the community."],
           ["**Role play (socio-drama)**",
            "Audience **not more than about 25**; a few volunteers act.",
            "Participants **act out a real-life situation** (e.g. a mother refusing "
            "immunisation, a quack, a pharmacist counselling) without a script; the "
            "audience then discusses what happened and why.",
            "Creates deep insight into attitudes and feelings, exposes prejudices, highly "
            "interesting; especially useful for illiterate groups and school children. "
            "Needs a skilled facilitator; may embarrass shy participants."],
           ["**Buzz session / buzz group**",
            "A large group split into **small buzz groups of 4\u20136** for a few minutes.",
            "Each small group discusses the question simultaneously ('buzzing'), then a "
            "spokesman reports its conclusion to the whole gathering.",
            "Converts a passive audience into an active one in a few minutes; useful when "
            "time is short and the group is large."],
           ["**Brainstorming**",
            "Usually **6\u201312 members**, for 10\u201315 minutes.",
            "Members generate **as many ideas as possible without any criticism or "
            "evaluation**; quantity is encouraged; only afterwards are the ideas judged.",
            "Excellent for generating fresh solutions and for planning; must strictly "
            "postpone criticism."],
           ["**Case study / problem-solving**",
            "Small group.",
            "A real or simulated case is presented and analysed by the group.",
            "Develops analytical and decision-making ability."],
           ["**Field trip / study visit / exhibit tour**",
            "A small organised group.",
            "The group visits a site \u2014 a water works, a model village, a hospital, an "
            "ICDS centre \u2014 with a clear objective, preparation and follow-up "
            "discussion.",
            "Very convincing \u2014 'seeing for oneself'; costly and needs organisation."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 8.2  Group methods of health education")

    box(doc, "mnemonic",
        ["Numbers worth memorising: **Lecture \u2264 30** listeners \u00b7 "
         "**Group discussion 6\u201312** \u00b7 **Panel 4\u20138** panellists \u00b7 "
         "**Symposium 2\u20135** speakers \u00b7 **Role play audience \u2264 25** \u00b7 "
         "**Buzz group 4\u20136** \u00b7 **Brainstorming 6\u201312**.",
         "Difference to remember: in a ^^panel discussion^^ the experts **talk to one "
         "another** with no prepared speeches; in a ^^symposium^^ each expert delivers a "
         "**prepared speech** and they do **not** discuss among themselves."])

    # ------------------------------------------------ mass
    h2(doc, "8.3  Mass Approach")
    para(doc, "Mass media are used when the object is to reach very large numbers quickly, "
              "chiefly to **create awareness** and to support interpersonal work. They are "
              "**one-way** and provide no feedback, so they seldom change behaviour by "
              "themselves.")

    table(doc,
          ["Medium", "Features", "Advantages", "Limitations"],
          [["**Television**", "Audio-visual; the most powerful mass medium; reaches the "
            "illiterate.", "Sight plus sound; high credibility and impact; wide reach; can "
            "demonstrate.",
            "Expensive; one-way; viewing is often for entertainment; message quickly "
            "forgotten; electricity and set required."],
           ["**Radio**", "Auditory; very wide reach including remote and illiterate "
            "populations; local-language broadcasts and community radio.",
            "Cheap, portable, no literacy needed, works without electricity (battery), "
            "large coverage.",
            "Only one sense; no visual demonstration; no feedback; listener may not be "
            "attentive."],
           ["**Newspapers, magazines, press**", "Printed word; reach the literate, urban, "
            "opinion-forming public.",
            "Can be re-read and preserved; carry detail; cheap per copy; good for advocacy.",
            "Useless for illiterates; low readership in rural areas; news value may distort "
            "the health message."],
           ["**Printed material** \u2014 posters, leaflets, pamphlets, folders, booklets, "
            "handbills, flip books, banners, hoardings",
            "Cheap, portable, can be taken home and re-read; can be produced locally in the "
            "local language.",
            "Inexpensive, widely distributable, reinforces spoken messages, good take-home "
            "reminder.",
            "Needs literacy (except pictorial matter); discarded easily; no feedback."],
           ["**Films, documentaries, video and mobile film vans**",
            "Audio-visual, dramatic, emotionally powerful; useful in villages without "
            "electricity using mobile vans.",
            "Holds attention, teaches skills, reaches illiterates, entertaining.",
            "Costly to make; needs equipment, power and a darkened space; passive audience."],
           ["**Health museum and health exhibition**",
            "Static and moving displays, models, specimens, charts, working models; "
            "**health melas** and fairs.",
            "Several senses involved, self-paced, attractive, suitable for all ages and "
            "literacy levels; can be combined with services and check-ups.",
            "Costly; static in one place; requires space, staff and maintenance."],
           ["**Folk media / traditional media**",
            "Puppet shows, street plays (nukkad natak), folk songs, ballads, dances, "
            "__kathputli__, __tamasha__, __jatra__, __bhavai__, drum-beating.",
            "**Culturally rooted, entertaining and highly acceptable**; excellent for "
            "illiterate rural audiences; cheap; permits some interaction.",
            "Message may be diluted by entertainment; needs local artists; limited "
            "audience per show."],
           ["**Internet, social media and mHealth**",
            "Websites, WhatsApp, YouTube, mobile SMS/IVR services, apps, teleconsultation, "
            "e-learning.",
            "Very rapid, cheap, interactive, personalised, scalable; permits two-way "
            "communication and reminders; useful for adherence reminders.",
            "Digital divide (age, income, language); **serious risk of misinformation**; "
            "privacy concerns; needs literacy and a device."],
           ["**Health days and campaigns**",
            "Observance of days such as World Health Day (7 April), World TB Day (24 March), "
            "World No-Tobacco Day (31 May), World AIDS Day (1 December), National "
            "Immunisation Day (Pulse Polio).",
            "Focuses attention intensely for a short period; mobilises many agencies and "
            "the press.",
            "Short-lived effect unless followed by sustained work \u2014 the classic "
            "weakness of the **campaign approach**."]],
          header_fill=SH_HEADER_GREEN,
          caption="Table 8.3  Mass media in health education")

    # ------------------------------------------------ AV aids
    h2(doc, "8.4  Audio-Visual (AV) Aids")
    defn(doc, "Audio-visual aids",
         "Instructional devices that are **used to supplement and reinforce the spoken or "
         "written word** by appealing to the senses, thereby making learning clearer, more "
         "interesting and better retained. They are **aids to teaching, never a substitute "
         "for the teacher**.")

    h3(doc, "8.4.1  Classification of AV Aids")
    table(doc,
          ["Basis of classification", "Categories", "Examples"],
          [["**By sense organ used**",
            "Auditory (hearing) \u00b7 Visual (sight) \u00b7 Combined audio-visual",
            "**Auditory:** radio, tape recorder, microphone, public address system, "
            "megaphone, telephone. **Visual:** posters, charts, graphs, maps, models, "
            "specimens, flannelgraph, flash cards, bulletin board, blackboard, slides, "
            "OHP transparencies, photographs, printed matter. **Combined:** television, "
            "cinema/film, video, sound filmstrip, drama, puppet show, computer "
            "presentation, LCD projection."],
           ["**By complexity**", "Simple \u00b7 Sophisticated",
            "**Simple:** chalkboard, chart, poster, flannelgraph, flash card, model, "
            "specimen \u2014 cheap, locally made, need no power. **Sophisticated:** "
            "television, cinema, LCD projector, computer \u2014 costly, need power and "
            "maintenance."],
           ["**By projection**", "Projected \u00b7 Non-projected",
            "**Projected:** slides, filmstrips, films, overhead projector, LCD/DLP "
            "projector, epidiascope. **Non-projected:** blackboard, charts, posters, "
            "models, flannelgraph, flip chart, bulletin board."],
           ["**By dimension**", "Two-dimensional \u00b7 Three-dimensional",
            "**2-D:** poster, chart, graph, map, photograph, cartoon. "
            "**3-D:** models, specimens, objects, dioramas, puppets."]],
          header_fill=SH_HEADER_PURPLE,
          caption="Table 8.4  Classification of audio-visual aids")

    h3(doc, "8.4.2  The Common Aids in Detail")
    table(doc,
          ["Aid", "Description and correct use"],
          [["**Chalkboard / blackboard / whiteboard**",
            "The most common, cheapest and most flexible aid. Write large and legibly; use "
            "few words; stand aside while writing; erase before starting a new idea; use "
            "coloured chalk for emphasis."],
           ["**Chart**", "A sheet presenting an idea in a summarised, logical, visual form "
            "(flow chart, tree chart, tabular chart, pull chart, flip chart). **One chart "
            "= one idea.** Letters must be readable from the back of the room."],
           ["**Poster**",
            "A pictorial display with a **brief, arresting message**; usually about "
            "**50 \u00d7 75 cm (20 \u00d7 30 inches)**. Requirements: **one idea only**, "
            "few words (ideally under about seven), bold lettering readable from "
            "3\u20134 metres, bright contrasting colours, an eye-catching illustration, and "
            "a slogan. Must be displayed at eye level where people wait, and **changed "
            "frequently**."],
           ["**Leaflet, pamphlet, folder, booklet, handbill**",
            "Printed take-home matter. A **leaflet/handbill** is a single sheet with one "
            "message; a **folder** is folded, giving a few panels; a **pamphlet/booklet** "
            "has several pages and more detail. Use simple language, pictures and plenty "
            "of white space."],
           ["**Flannelgraph (khadigraph / flannel board)**",
            "A board covered with flannel, khadi or velvet on which cut-outs backed with "
            "sandpaper or rough cloth are made to stick. The story is **built up step by "
            "step** as the talk proceeds, which holds attention. Cheap, reusable, needs no "
            "electricity."],
           ["**Flash cards**",
            "A set of about **10\u201312 stiff cards (roughly 25 \u00d7 30 cm)** carrying a "
            "picture on the front and the text of the message on the back for the speaker. "
            "They are 'flashed' one by one in sequence at about **1 metre** from a small "
            "audience (up to 25\u201330). Excellent for illiterate groups."],
           ["**Bulletin board / notice board**",
            "A board on which notices, cuttings, photographs and posters are pinned. Must "
            "be placed where people gather and **kept up to date**, neat and uncluttered."],
           ["**Models**",
            "Three-dimensional representations: **scale models** (life-size, enlarged or "
            "reduced), **cut-away (sectional) models**, **working models**. Useful when the "
            "real object cannot be shown \u2014 e.g. a sanitary latrine, the human heart, "
            "a smokeless chulha, a model of the eye."],
           ["**Specimens and objects**",
            "Real materials \u2014 foodstuffs, drug samples, an adulterated sample, a "
            "mosquito larva in a bottle, an intra-uterine device, a diseased organ. The "
            "**most concrete and convincing** of all visual aids."],
           ["**Graphs and diagrams**",
            "Line, bar, pie and pictogram forms used to present numerical data. Keep to one "
            "comparison per graph; label clearly; use pictograms for illiterates."],
           ["**Maps**", "Show the geographical distribution of disease, services and "
            "resources; spot maps of cases are used in outbreak investigation."],
           ["**Puppets**",
            "Glove, string (marionette), rod and shadow puppets present a story humorously; "
            "very popular with children and rural audiences; can tackle sensitive subjects "
            "indirectly."],
           ["**Overhead projector (OHP) / slides / LCD projector**",
            "For larger audiences. Rules: **not more than 6\u20137 lines per slide** and a "
            "few words per line; large font; high contrast; do not read out the slide; "
            "allow enough time for the audience to read."],
           ["**Cinema, video, television**",
            "Best for showing motion, process and emotion; should be preceded by an "
            "introduction and **followed by a discussion**."]],
          header_fill=SH_HEADER_BLUE)

    h3(doc, "8.4.3  Criteria of a Good AV Aid and Rules for Use")
    bullets(doc, [
        "**Simple** \u2014 conveys one idea at a time, free from unnecessary detail.",
        "**Accurate** and scientifically correct; **up to date**.",
        "**Appropriate** to the age, education, culture and language of the audience.",
        "**Visible / audible** to the whole audience; adequate size and contrast.",
        "**Interesting and attractive**, arousing curiosity.",
        "**Cheap, locally available and easily transportable**; preferably made from local "
        "material.",
        "**Durable and easy to maintain**, and safe to use.",
        "Rules of use: be **familiar with the aid and test the equipment beforehand**; keep "
        "the aid **covered until needed and remove it afterwards**; talk to the audience, "
        "not to the aid; use **several aids** in one session; never let the aid replace the "
        "educator.",
    ])

    box(doc, "highyield",
        ["An AV aid is only an **aid**; the ^^health educator remains the key factor^^.",
         "**Edgar Dale's Cone of Experience** arranges learning experiences from the most "
         "concrete at the base (**direct purposeful experience**) to the most abstract at "
         "the apex (**verbal symbols**). The nearer the base, the more effective the "
         "learning.",
         "The most effective single visual aid for an **illiterate** rural audience is a "
         "**demonstration with real objects / flash cards / flannelgraph**; the cheapest "
         "and most versatile aid in a classroom is the **chalkboard**."])

    h2(doc, "8.5  Choosing the Right Method")
    table(doc,
          ["Situation / objective", "Method of choice"],
          [["Creating awareness among a very large population quickly",
            "**Mass media** \u2014 radio, television, press, hoardings, social media."],
           ["Changing a deep-rooted personal behaviour",
            "**Individual counselling** with follow-up."],
           ["Teaching a skill (ORS, inhaler, hand-washing)",
            "**Demonstration** followed by return demonstration by the learner."],
           ["Reaching an illiterate rural audience",
            "**Folk media, flash cards, flannelgraph, puppets, film, demonstration**."],
           ["Getting a community to take a collective decision",
            "**Group discussion** with local leaders."],
           ["Exploring a controversial subject with several viewpoints",
            "**Panel discussion**."],
           ["Giving authoritative, comprehensive information on a subject",
            "**Symposium** or lecture."],
           ["Developing practical skills in workers",
            "**Workshop** with small working groups."],
           ["Activating a large, passive audience in a few minutes",
            "**Buzz session**."],
           ["Generating new solutions to a problem", "**Brainstorming**."],
           ["Exposing attitudes and prejudices, e.g. about immunisation refusal",
            "**Role play / socio-drama**."],
           ["Educating a patient at the point of dispensing",
            "**Personal contact plus a printed leaflet** (medication counselling)."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 8.5  Matching the method to the objective")

    h2(doc, "8.6  Health Education in Specific Settings")
    table(doc,
          ["Setting", "Key points"],
          [["**School health education**",
            "The school is the **most cost-effective and important setting**, because habits "
            "are formed in childhood and children carry messages home ('each child a health "
            "messenger'). Content: personal hygiene, nutrition, oral health, exercise, "
            "first aid, prevention of tobacco/alcohol/substance use, adolescent and "
            "reproductive health, road safety, mental health. Methods: integration with the "
            "curriculum, health clubs, school health committees, eco-clubs, rallies, "
            "essay/painting competitions, midday meal as a teaching opportunity. Programmes: "
            "**School Health Programme**, now under **Ayushman Bharat \u2014 School Health "
            "and Wellness Ambassadors** (two teachers per school)."],
           ["**Community / village**",
            "Work through the **Gram Panchayat, Village Health Sanitation and Nutrition "
            "Committee (VHSNC), Mahila Mandal, self-help groups and ASHA**; use "
            "Village Health and Nutrition Days (VHND); folk media; Swachh Bharat and "
            "Poshan Abhiyaan platforms."],
           ["**Hospital and clinic**",
            "Waiting-area posters, display boards, television, group talks for patients and "
            "attendants, bedside teaching, discharge counselling and pre-operative "
            "explanation. **Pharmacy counselling counter** is a major opportunity."],
           ["**Workplace / industry**",
            "Occupational hazards, use of personal protective equipment, safety drills, "
            "first aid, ergonomics, tobacco and alcohol, periodic medical examination, "
            "employees' health committees."],
           ["**Antenatal and postnatal clinic**",
            "Diet in pregnancy, iron-folic acid and calcium, immunisation (Td), danger "
            "signs, institutional delivery, exclusive breast-feeding, newborn care, "
            "contraception, care of the umbilical cord."]],
          header_fill=SH_HEADER_GREEN)

    chapter_end(doc)


# ===========================================================================
# CHAPTER 9
# ===========================================================================
def chapter_09(doc):
    chapter_title(doc, 9,
                  "History, Development and Growth of Health Education in India")

    h2(doc, "9.1  The Ancient and Medieval Foundations")
    bullets(doc, [
        "**Indus Valley Civilisation (c. 3000 BC)** \u2014 Mohenjo-daro and Harappa had "
        "planned drainage, covered sewers, public baths and wells: evidence of an "
        "organised, community-wide idea of hygiene.",
        "**Vedic period** \u2014 the Vedas, especially the **Atharva Veda**, prescribed "
        "rules of personal cleanliness, diet, daily routine (__dinacharya__), seasonal "
        "regimen (__ritucharya__) and conduct. Health teaching was embedded in **religion "
        "and custom**, which made it powerfully effective.",
        "**Ayurveda \u2014 Charaka Samhita and Sushruta Samhita** \u2014 laid down "
        "__swasthavritta__ (the code of healthy living): the concept that **prevention "
        "precedes cure**. Sushruta is called the 'Father of Surgery'; Charaka emphasised "
        "diet, conduct and mental hygiene.",
        "**Emperor Ashoka (3rd century BC)** \u2014 rock edicts publicised health rules, "
        "hospitals (for people and animals), wells, rest-houses and the planting of "
        "medicinal herbs along roads: possibly the world's earliest **state-sponsored "
        "health communication**.",
        "**Medieval period** \u2014 the Unani system flourished; epidemics of plague, "
        "cholera and smallpox were common; organised public health declined and health "
        "practices were transmitted through religion, folklore, proverbs and folk songs.",
    ])

    h2(doc, "9.2  The Colonial Period \u2014 The Beginnings of Organised Health Education")
    table(doc,
          ["Year", "Landmark", "Significance"],
          [["**1859\u201363**", "**Royal Commission** on the health of the Army in India "
            "(appointed after the 1857 revolt).",
            "Its report led to the creation of public health machinery in India."],
           ["**1864**", "**Commissions of Public Health** / Sanitary Commissioners appointed "
            "in Bombay, Madras and Bengal.",
            "First official sanitary organisation; sanitary reports and public health "
            "propaganda began."],
           ["**1873**", "**Births, Deaths and Marriages Registration Act**.",
            "Beginning of vital statistics, the factual basis of health education."],
           ["**1880**", "**Vaccination Act**.",
            "Made smallpox vaccination compulsory in certain areas; required public "
            "persuasion and education."],
           ["**1897**", "**Epidemic Diseases Act** (after the Bombay plague of 1896).",
            "Provided for notification, inspection and segregation; heavy use of "
            "publicity."],
           ["**1904**", "**Plague Commission** report.",
            "Recommended public education about rats, fleas and personal hygiene."],
           ["**1919**", "**Montague\u2013Chelmsford reforms (Government of India Act, "
            "1919)**.",
            "**Public health, sanitation and vital statistics were transferred to the "
            "provinces** \u2014 health education became a provincial responsibility."],
           ["**1920**", "**Indian Red Cross Society** established.",
            "Became a major agency of voluntary health education, first aid and "
            "maternal-child welfare."],
           ["**1923**", "The **Rockefeller Foundation** assisted health and hygiene work; "
            "rural health units set up.",
            "Introduced modern public health education methods to India."],
           ["**1932**", "**All India Institute of Hygiene and Public Health (AIIHPH), "
            "Calcutta** established.",
            "The **first institution in India** to give formal training in public health "
            "including health education; created a Department of Health Education."],
           ["**1935**", "**Government of India Act, 1935**.",
            "Further provincial autonomy in health matters."],
           ["**1939**", "**Health Publicity Bureau** (also called the Central Health "
            "Publicity Bureau) organised at the centre under the Public Health "
            "Commissioner.",
            "The **direct forerunner of the Central Health Education Bureau**; produced "
            "posters, pamphlets and films."],
           ["**1939**", "First **Maternity and Child Welfare Bureau** / Lady Reading Health "
            "School, Delhi.",
            "Trained health visitors who carried out home-based health education."],
           ["**1943\u201346**", "**Bhore Committee** (Health Survey and Development "
            "Committee), chaired by Sir Joseph Bhore; report submitted in **1946** in four "
            "volumes.",
            "The **most important landmark**. It recognised health education as an "
            "essential function of the health services, recommended **a Central Health "
            "Education Bureau, state bureaux and the appointment of trained health "
            "educators**, the three-month and long-term plans, the 'social physician' "
            "concept, and integration of preventive with curative services."]],
          header_fill=SH_HEADER_BLUE,
          caption="Table 9.1  Pre-independence landmarks")

    h2(doc, "9.3  Post-Independence Growth")
    table(doc,
          ["Year", "Development", "Significance for health education"],
          [["**1951**", "**First Five Year Plan** began.",
            "Health education included in planned development; the community development "
            "programme used the extension-education approach."],
           ["**1952**", "**National Family Planning Programme** launched \u2014 India was "
            "the **first country in the world** to have a state family planning programme.",
            "Created an enormous and continuing demand for mass health education, motivation "
            "and IEC."],
           ["~~1956~~", "^^CENTRAL HEALTH EDUCATION BUREAU (CHEB) established at New "
            "Delhi^^ under the Directorate General of Health Services, Ministry of Health "
            "(on the recommendation of the Bhore Committee), by reorganising the Health "
            "Publicity Bureau.",
            "**The single most important landmark in Indian health education** \u2014 the "
            "apex national body. **This year is very frequently asked.**"],
           ["**1956**", "**Indian Public Health Association (IPHA)** and other professional "
            "bodies took shape; publication of professional journals.",
            "Professionalisation of public health and health education."],
           ["**1959\u201361**", "**Mudaliar Committee** (Health Survey and Planning "
            "Committee), report 1961.",
            "Found health education weak; recommended strengthening of health education "
            "bureaux and training."],
           ["**1961**", "**School Health Committee** (chaired by Renuka Ray) reported.",
            "Recommended a systematic **school health service and school health "
            "education**."],
           ["**1963**", "**Chadah Committee**.",
            "Monthly home visits by basic health workers for malaria surveillance "
            "\u2014 combined with health education."],
           ["**1966**", "**Mukherjee Committee**.",
            "Separated malaria work from family planning so that each could be pursued "
            "properly."],
           ["**1967**", "**Jungalwalla Committee** ('Integration of Health Services').",
            "Recommended an integrated health service and uniform referral system; state "
            "health education bureaux strengthened in most states around this period."],
           ["**1973**", "**Kartar Singh Committee** ('Multipurpose Workers').",
            "Created the **Multipurpose Health Worker (MPW)** scheme \u2014 one male and "
            "one female worker per 5000 population \u2014 who carry health education to "
            "every household."],
           ["**1975**", "**Srivastava Committee** (Group on Medical Education and Support "
            "Manpower).",
            "Recommended **community health volunteers/workers** and the **ROME** "
            "(Reorientation of Medical Education) scheme \u2014 health education by "
            "community-based volunteers."],
           ["**1975**", "**Integrated Child Development Services (ICDS)** launched (2 "
            "October 1975).",
            "**Nutrition and Health Education (NHED)** became one of its six services, "
            "delivered by the anganwadi worker to women aged 15\u201345."],
           ["**1977**", "**Rural Health Scheme** and the **Community Health Worker / "
            "Volunteer** scheme; **NIHFW** established (9 March 1977) by merging NIHAE "
            "(1964) and NIFP (1970).",
            "NIHFW became the apex institute for **training, research and evaluation** in "
            "health and family welfare, including health education and IEC."],
           ["~~1978~~", "**Alma-Ata Declaration** \u2014 'Health for All by 2000 AD' "
            "through **Primary Health Care**; India was a signatory.",
            "Health education declared the **first of the eight essential elements of "
            "PHC** \u2014 the greatest single boost that health education has received."],
           ["**1983**", "**First National Health Policy** of India.",
            "Gave a central place to health education, community participation and the "
            "training of health volunteers."],
           ["**1986**", "**Ottawa Charter** (international) and the **Bajaj Committee** "
            "(health manpower planning) in India; **National Policy on Education, 1986**.",
            "Shift from health education to the wider concept of **health promotion**; "
            "health education strengthened in schools."],
           ["**1992**", "**Child Survival and Safe Motherhood (CSSM)** programme.",
            "Large-scale IEC for immunisation, ORS and safe delivery."],
           ["**1997**", "**Reproductive and Child Health (RCH) Programme**, Phase I "
            "(RCH-II from 2005).",
            "Adopted the **target-free, client-centred** approach; IEC replaced by "
            "**BCC** with emphasis on counselling and informed choice."],
           ["**2002**", "**National Health Policy 2002**.",
            "Emphasised IEC, decentralisation and increased public health spending."],
           ["~~2005~~", "**National Rural Health Mission (NRHM)** launched (12 April 2005); "
            "creation of the ^^ASHA^^ \u2014 Accredited Social Health Activist.",
            "The **most significant recent development**: one trained female community "
            "health volunteer per 1000 population acting as a **health educator and change "
            "agent**; also the VHSNC, Village Health and Nutrition Days, Rogi Kalyan "
            "Samitis and a dedicated **IEC/BCC** budget in every state PIP."],
           ["**2013**", "**National Urban Health Mission (NUHM)**; NRHM + NUHM = **National "
            "Health Mission (NHM)**.",
            "Extended organised health education to urban slums through **ASHA and Mahila "
            "Arogya Samitis**."],
           ["**2014 onwards**", "**Swachh Bharat Mission** (2 October 2014), **Mission "
            "Indradhanush** (2014), **Poshan Abhiyaan** (2018), **Eat Right India**, "
            "**Fit India Movement** (2019).",
            "Mass behaviour-change campaigns on sanitation, immunisation, nutrition, safe "
            "food and physical activity \u2014 health education at national campaign "
            "scale."],
           ["**2017**", "**National Health Policy 2017**.",
            "Explicit goal of **health promotion and prevention**, school health "
            "programmes, 'Health in All Policies', and a target of 2.5% of GDP for health."],
           ["**2018**", "**Ayushman Bharat** \u2014 **Health and Wellness Centres (HWC)** "
            "plus PM-JAY (23 September 2018).",
            "HWCs deliver **comprehensive primary health care with health promotion and "
            "wellness activities** (yoga, exercise, screening); **School Health and Wellness "
            "Ambassadors** appointed; **Community Health Officer (CHO)** added as a health "
            "educator at HWC level."],
           ["**2020\u201322**", "**COVID-19 pandemic** response.",
            "The largest risk-communication and community-engagement exercise in Indian "
            "history \u2014 mass media, mobile caller tunes, Aarogya Setu, CoWIN, and the "
            "fight against the accompanying **'infodemic'** of misinformation."]],
          header_fill=SH_HEADER_TEAL,
          caption="Table 9.2  Post-independence growth of health education in India")

    h2(doc, "9.4  The Central Health Education Bureau (CHEB)")
    box(doc, "definition",
        "The **Central Health Education Bureau** was set up in ~~1956~~ at **New Delhi** "
        "under the **Directorate General of Health Services, Ministry of Health and Family "
        "Welfare**, on the recommendation of the **Bhore Committee (1946)**. It is the "
        "^^apex national body for health education in India^^.")

    h3(doc, "9.4.1  Objectives")
    bullets(doc, [
        "To promote health education as an integral part of all health, medical and family "
        "welfare programmes.",
        "To develop and strengthen health education services at the national, state and "
        "district levels.",
        "To **train** health and allied personnel in health education methods.",
        "To produce, pre-test and distribute health education **material and media** in "
        "several languages.",
        "To conduct **research and evaluation** in health education and health behaviour.",
        "To coordinate the health education work of government, voluntary and international "
        "agencies.",
    ])

    h3(doc, "9.4.2  Functions and Divisions")
    table(doc,
          ["Function / division", "Work done"],
          [["**Training**", "Courses and workshops for health education officers, medical "
            "and paramedical staff, teachers and field workers; the **Diploma/certificate "
            "courses in health education**."],
           ["**Production of media and material**",
            "Posters, folders, flip books, flash cards, charts, exhibits, films, radio and "
            "television spots, slide sets and exhibition panels; a **media production "
            "unit**."],
           ["**Research and evaluation**",
            "KAP studies, pre-testing of material, operational research, evaluation of IEC "
            "campaigns and studies of health behaviour."],
           ["**Publication and documentation**",
            "Health education literature, technical reports, a library and documentation "
            "centre; the journal **'Swasth Hind'**."],
           ["**School health education**",
            "Development of school health education curricula, teachers' guides and "
            "training of teachers."],
           ["**Technical advice and coordination**",
            "Advises the Ministry, states, national programmes and voluntary agencies; "
            "coordinates the observance of health days and national campaigns."],
           ["**Community health education / field practice**",
            "Demonstration and field-practice projects; support to state and district "
            "bureaux."]],
          header_fill=SH_HEADER_GREEN)

    h2(doc, "9.5  Organisation of Health Education Services in India")
    table(doc,
          ["Level", "Agency / officer"],
          [["**National / Centre**",
            "**Central Health Education Bureau (CHEB)**, New Delhi; the **IEC Division** of "
            "the Ministry of Health and Family Welfare; **NIHFW**; the media divisions of "
            "the national programmes (NACO, NTEP, NVBDCP); **Directorate of Advertising and "
            "Visual Publicity (DAVP/CBC)**; All India Radio, Doordarshan, Song and Drama "
            "Division and Field Publicity Directorate."],
           ["**State**", "**State Health Education Bureau / State IEC Bureau** headed by a "
            "State Health Education Officer / Mass Media Officer, under the Directorate of "
            "Health Services."],
           ["**District**",
            "**District Health Education Officer** / **District Extension and Media Officer "
            "(DEMO)** with a district mass education and information unit."],
           ["**Block / PHC**",
            "**Block Extension Educator (BEE)** \u2014 the designated health educator at "
            "block level; Health Assistants (male and female)."],
           ["**Sub-centre**", "**ANM / MPW (Female)** and **MPW (Male)**."],
           ["**Village / community**",
            "**ASHA**, anganwadi worker, VHSNC, Gram Panchayat, Mahila Mandal, self-help "
            "groups, school teachers, trained dais and local opinion leaders."]],
          header_fill=SH_HEADER_PURPLE,
          caption="Table 9.3  The health education machinery, centre to village")

    h2(doc, "9.6  Institutions and Professional Bodies")
    table(doc,
          ["Body", "Note"],
          [["**CHEB**, New Delhi (1956)", "Apex national health education body."],
           ["**NIHFW**, New Delhi (1977)",
            "National Institute of Health and Family Welfare \u2014 apex technical "
            "institute for training, research, evaluation, consultancy and specialised "
            "services in health and family welfare."],
           ["**AIIHPH**, Kolkata (1932)",
            "All India Institute of Hygiene and Public Health \u2014 oldest public health "
            "training institute in India."],
           ["**NCDC**, Delhi (formerly NICD, 1963; originally Malaria Institute of India, "
            "1909)",
            "National Centre for Disease Control \u2014 training and IEC on communicable "
            "disease."],
           ["**ICMR**, New Delhi (1911 as IRFA, renamed 1949)",
            "Apex body for biomedical research; issues the national ethical guidelines."],
           ["**IIHFW / SIHFW**",
            "Indian/State Institutes of Health and Family Welfare \u2014 state-level "
            "training in IEC and management."],
           ["**IPHA**", "Indian Public Health Association \u2014 professional body; "
            "publishes the __Indian Journal of Public Health__."],
           ["**IAPSM**", "Indian Association of Preventive and Social Medicine."],
           ["**Indian Red Cross Society (1920)**, **TB Association of India (1939)**, "
            "**Hind Kusht Nivaran Sangh**, **Family Planning Association of India (1949)**, "
            "**Indian Council for Child Welfare**, **Kasturba Health Society**",
            "Major **voluntary agencies** in health education."],
           ["**IUHPE (1951)** and **SOPHE (1950)**",
            "International Union for Health Promotion and Education; Society for Public "
            "Health Education \u2014 the leading international professional bodies."],
           ["**WHO (7 April 1948)**, **UNICEF (1946)**, **UNESCO**, **UNFPA**, "
            "**World Bank**, **USAID**, **Rockefeller** and **Ford Foundations**",
            "International agencies supporting health education in India. "
            "**World Health Day is observed on 7 April.**"]],
          header_fill=SH_HEADER_BLUE)

    h2(doc, "9.7  Achievements and Continuing Constraints")
    table(doc,
          ["Achievements", "Constraints"],
          [["Eradication of **smallpox (last case 1975, India declared free 1977; world "
            "1980)** and of **polio (last case 13 January 2011; India certified polio-free "
            "27 March 2014)** \u2014 both achieved largely through mass communication and "
            "community mobilisation.",
            "Health education is still treated as a **subsidiary activity** with a small "
            "budget and few dedicated trained posts."],
           ["Elimination of **guinea-worm (2000)**, **yaws (2016)** and **maternal and "
            "neonatal tetanus (2015)**; leprosy elimination as a public health problem "
            "(2005).",
            "**Shortage of trained health educators**; BEE and DEMO posts often vacant or "
            "diverted to other work."],
           ["A very large trained community-level cadre \u2014 about a million **ASHAs** "
            "and anganwadi workers acting as health educators.",
            "Material is often produced centrally and is **not adapted to local language "
            "and culture**; little pre-testing."],
           ["Rise in institutional deliveries, immunisation coverage, ORS and "
            "contraceptive use, sanitation coverage and iodised-salt consumption.",
            "Persistence of the **KAP gap** \u2014 knowledge has risen faster than "
            "practice."],
           ["Wide penetration of radio, television and mobile telephony giving "
            "unprecedented reach.",
            "**Misinformation on social media**, commercial advertising of unhealthy "
            "products, and inadequate **evaluation** of IEC activity."]],
          header_fill=SH_HEADER_TEAL)

    box(doc, "highyield",
        ["Dates that are asked most often: ^^CHEB \u2013 1956, New Delhi^^; "
         "**Bhore Committee report \u2013 1946**; **AIIHPH Kolkata \u2013 1932**; "
         "**NIHFW \u2013 1977**; **Alma-Ata \u2013 1978**; **Ottawa Charter \u2013 1986**; "
         "**NRHM and ASHA \u2013 2005**; **ICDS \u2013 1975**; **India's family planning "
         "programme \u2013 1952 (world's first)**.",
         "The committee that recommended the establishment of CHEB was the "
         "~~Bhore Committee (Health Survey and Development Committee, 1946)~~."])

    chapter_end(doc)
