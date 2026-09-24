# -*- coding: utf-8 -*-
"""Chapter 2 - Structure and Functions of the Body."""


def render(b):
    b.chapter(
        "Structure and Functions of the Body",
        "Cells, tissues and systems \u2014 skeletal, muscular, circulatory, "
        "respiratory, nervous, digestive, urinary, endocrine, skin, sense organs "
        "and reproductive systems, with all the normal values a first aider must "
        "know.",
        syllabus=[
            "Structure and functions of the body \u2014 organisation of the body, "
            "all major systems with their parts, functions and normal values.",
            "Anatomical terms, body cavities and regions used while describing "
            "injuries; landmarks used in first aid (pressure points, CPR site).",
        ])

    # ------------------------------------------------------------------
    b.h2("Levels of Organisation of the Human Body")
    b.p("The body is built up in a definite order. Anatomy is the study of the "
        "*structure* of the body; physiology is the study of its *functions*.")
    b.table(
        ["Level", "Description", "Example"],
        [["1. Cell", "Smallest living, structural and functional unit of the body "
                     "(discovered by Robert Hooke, 1665).",
          "Red blood cell, nerve cell"],
         ["2. Tissue", "A group of similar cells performing the same function.",
          "Muscle tissue, nervous tissue"],
         ["3. Organ", "Two or more tissues combining to perform a specific "
                      "function.", "Heart, lung, stomach"],
         ["4. System", "A group of organs working together for one major "
                       "function.", "Circulatory system, digestive system"],
         ["5. Organism", "All systems working together \u2014 the complete human "
                         "being.", "Human body"]],
        weights=[1.9, 7.4, 3.3])
    b.box("NUMBERS TO REMEMBER", [
        "The adult body has about **75\u2013100 trillion cells**, **4 basic "
        "tissue types**, and roughly **11 organ systems**.",
        "Body water = **about 60 %** of body weight in an adult male (55 % female, "
        "75 % in a newborn). Two-thirds of it is **intracellular**.",
        "Average adult blood volume = **5\u20136 litres (about 8 % of body "
        "weight; 70 ml/kg)**.",
        "**Homeostasis** = maintenance of a constant internal environment "
        "(temperature, pH 7.35\u20137.45, glucose, fluids). Failure of "
        "homeostasis = disease.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("The Cell and the Four Basic Tissues")
    b.h3("Chief parts of a cell")
    b.table(
        ["Part", "Function"],
        [["Cell (plasma) membrane", "Selectively permeable outer covering; "
                                    "controls entry and exit of substances."],
         ["Cytoplasm", "Jelly-like fluid holding the organelles; site of "
                       "metabolic reactions."],
         ["Nucleus", "Control centre; contains DNA/chromosomes (**46 in 23 "
                     "pairs**); directs cell activity and division."],
         ["Mitochondria", "**Powerhouse** of the cell \u2014 produces energy as "
                          "ATP by aerobic respiration."],
         ["Ribosomes", "Protein synthesis (\u2018protein factory\u2019)."],
         ["Endoplasmic reticulum", "Transport channel; rough ER = protein, "
                                   "smooth ER = fat/lipid synthesis."],
         ["Golgi apparatus", "Packaging and secretion of proteins "
                             "(\u2018post office\u2019)."],
         ["Lysosome", "Contains digestive enzymes \u2014 \u2018suicidal bag\u2019 "
                      "of the cell; destroys worn-out parts and bacteria."],
         ["Centrosome", "Takes part in cell division."]],
        weights=[3.0, 9.6])
    b.h3("The four primary tissues")
    b.table(
        ["Tissue", "Where found", "Function"],
        [["Epithelial", "Skin surface, lining of mouth, gut, air passages, "
                        "glands, blood vessels",
          "Protection, absorption, secretion, filtration"],
         ["Connective", "Bone, cartilage, tendon, ligament, blood, fat "
                        "(adipose), lymph",
          "Support, binding, transport, storage, defence \u2014 the **most "
          "abundant** tissue type"],
         ["Muscular", "Skeletal muscle, heart, walls of gut and vessels",
          "Movement, maintenance of posture, propulsion, heat production"],
         ["Nervous", "Brain, spinal cord, nerves",
          "Reception of stimuli, conduction of impulses, control and "
          "co-ordination"]],
        weights=[2.0, 5.2, 5.4])

    # ------------------------------------------------------------------
    b.h2("Anatomical Terms, Planes, Cavities and Regions")
    b.p("These words are used in every description of injury \u2014 learn them "
        "once and they save confusion for ever.")
    b.table(
        ["Term", "Meaning", "Term", "Meaning"],
        [["Anatomical position", "Standing erect, eyes forward, arms at sides, "
                                 "palms facing forward", "Superior / Inferior",
          "Above / below"],
         ["Anterior (ventral)", "Front of the body", "Posterior (dorsal)",
          "Back of the body"],
         ["Medial / Lateral", "Nearer to / away from the midline",
          "Proximal / Distal", "Nearer to / farther from the trunk (root of a "
                               "limb)"],
         ["Superficial / Deep", "Near the surface / away from the surface",
          "Supine / Prone", "Lying face up / lying face down"],
         ["Flexion / Extension", "Bending / straightening a joint",
          "Abduction / Adduction", "Moving away from / towards the midline"],
         ["Palmar / Plantar", "Palm of hand / sole of foot",
          "Unilateral / Bilateral", "One side / both sides"]],
        weights=[2.6, 4.0, 2.4, 3.6], size=8.6)
    b.h3("Planes of the body")
    b.bullets([
        "**Sagittal (median) plane** \u2014 vertical, divides the body into "
        "right and left halves.",
        "**Coronal (frontal) plane** \u2014 vertical, divides into front and back.",
        "**Transverse (horizontal/axial) plane** \u2014 divides into upper and "
        "lower parts.",
    ])
    b.h3("Body cavities and their contents")
    b.table(
        ["Cavity", "Contents"],
        [["Cranial cavity", "Brain (protected by the skull and meninges)"],
         ["Vertebral (spinal) canal", "Spinal cord"],
         ["Thoracic cavity", "Heart in the pericardium, lungs in the pleurae, "
                             "oesophagus, trachea, great vessels, thymus "
                             "(mediastinum = the space between the lungs)"],
         ["Abdominal cavity", "Stomach, small and large intestine, liver, "
                              "gall bladder, pancreas, spleen, kidneys, "
                              "suprarenal glands"],
         ["Pelvic cavity", "Urinary bladder, rectum, reproductive organs, "
                           "sigmoid colon"]],
        weights=[2.8, 9.8])
    b.p("The **diaphragm** separates the thoracic from the abdominal cavity. "
        "The abdomen is divided for description into **nine regions** (right "
        "hypochondrium, epigastrium, left hypochondrium; right lumbar, umbilical, "
        "left lumbar; right iliac/inguinal, hypogastrium/suprapubic, left "
        "iliac/inguinal) or more simply into **four quadrants** by lines crossing "
        "at the umbilicus.")
    b.box("WHY THIS MATTERS IN FIRST AID", [
        "Pain in the **right hypochondrium** \u2192 liver/gall bladder; "
        "**right iliac fossa** \u2192 appendix; **epigastrium** \u2192 "
        "stomach/heart (a heart attack is often mistaken for \u2018gas\u2019).",
        "Injury below the **5th rib on the left** can tear the **spleen**; "
        "on the right, the **liver** \u2014 both cause severe internal bleeding.",
        "Always describe an injury using the casualty's **own right and left**, "
        "not yours.",
    ], kind="note")

    # ------------------------------------------------------------------
    b.h2("The Skeletal System")
    b.p("The adult human skeleton has ==206 bones== (a newborn has about "
        "**270\u2013300**, which fuse with growth). The skeleton is divided into "
        "the **axial skeleton (80 bones)** and the **appendicular skeleton "
        "(126 bones)**.")
    b.h3("Functions of the skeleton (mnemonic: S-P-M-M-S)")
    b.bullets([
        "**S**hape, support and framework of the body.",
        "**P**rotection of vital organs (skull \u2192 brain, ribs \u2192 heart "
        "and lungs, vertebrae \u2192 spinal cord, pelvis \u2192 bladder and "
        "reproductive organs).",
        "**M**ovement \u2014 bones act as levers for muscles; joints allow "
        "motion.",
        "**M**ineral storage \u2014 99 % of body **calcium** and much phosphorus "
        "is stored in bone.",
        "**S**ite of blood-cell formation (**haematopoiesis**) in **red bone "
        "marrow**; yellow marrow stores fat.",
    ])
    b.h3("Count of bones \u2014 the most examined table in anatomy")
    b.table(
        ["Region", "Bones", "Number"],
        [["**AXIAL SKELETON**", "", "**80**"],
         ["Skull \u2013 cranium", "Frontal 1, Parietal 2, Temporal 2, "
                                  "Occipital 1, Sphenoid 1, Ethmoid 1", "8"],
         ["Skull \u2013 face", "Maxilla 2, Zygomatic 2, Nasal 2, Lacrimal 2, "
                               "Palatine 2, Inferior nasal concha 2, Vomer 1, "
                               "Mandible 1", "14"],
         ["Ear ossicles", "Malleus, incus, stapes \u2014 3 in each ear", "6"],
         ["Hyoid", "The only bone that has no joint with another bone", "1"],
         ["Vertebral column", "Cervical 7, Thoracic 12, Lumbar 5, Sacrum 1 "
                              "(5 fused), Coccyx 1 (4 fused)", "26"],
         ["Thoracic cage", "Ribs 24 (12 pairs) + Sternum 1", "25"],
         ["**APPENDICULAR SKELETON**", "", "**126**"],
         ["Shoulder girdle", "Clavicle 2 + Scapula 2", "4"],
         ["Upper limbs", "Humerus 2, Radius 2, Ulna 2, Carpals 16, "
                         "Metacarpals 10, Phalanges 28", "60"],
         ["Pelvic girdle", "Hip bone (ilium + ischium + pubis fused) \u2014 2",
          "2"],
         ["Lower limbs", "Femur 2, Patella 2, Tibia 2, Fibula 2, Tarsals 14, "
                         "Metatarsals 10, Phalanges 28", "60"],
         ["**TOTAL**", "", "**206**"]],
        weights=[3.0, 8.0, 1.3], align=["l", "l", "c"])
    b.bullets([
        "Bones in one **hand = 27**; in one **foot = 26**; one upper limb "
        "(including girdle) = 32; one lower limb (including hip bone) = 31.",
        "Vertebral column in a child = **33 vertebrae**; in an adult = **26** "
        "(because 5 sacral fuse into 1 and 4 coccygeal fuse into 1). "
        "It has **4 curves** and about **100 joints**.",
        "Ribs: **12 pairs** \u2014 **true ribs 1\u20137** (joined directly to "
        "the sternum by their own cartilage), **false ribs 8\u201310** (joined "
        "indirectly) and **floating ribs 11\u201312** (not joined in front).",
        "The **sternum** has 3 parts \u2014 manubrium, body and xiphoid process; "
        "chest compressions are given on the **lower half of the sternum**.",
    ])
    b.h3("Types of bones")
    b.table(
        ["Type", "Example"],
        [["Long", "Femur, humerus, tibia, radius, ulna, metacarpals"],
         ["Short", "Carpals (wrist) and tarsals (ankle)"],
         ["Flat", "Skull bones, sternum, ribs, scapula"],
         ["Irregular", "Vertebrae, facial bones, hip bone"],
         ["Sesamoid", "**Patella** (kneecap) \u2014 the largest sesamoid bone"],
         ["Pneumatic (air-filled)", "Maxilla, frontal, sphenoid, ethmoid "
                                    "(contain sinuses)"]],
        weights=[3.2, 9.4])
    b.h3("Record facts about bones")
    b.table(
        ["Superlative", "Bone"],
        [["Longest, heaviest and strongest bone", "**Femur** (thigh bone) "
                                                  "\u2014 about \u00bc of the "
                                                  "body height"],
         ["Smallest bone", "**Stapes** (stirrup) in the middle ear"],
         ["Largest / broadest flat bone", "Hip bone; the largest flat bone of "
                                          "the skull is the parietal"],
         ["Strongest, hardest substance in the body", "**Enamel** of the tooth "
                                                      "(bone is the hardest "
                                                      "*tissue*)"],
         ["Only bone with no articulation", "**Hyoid** bone in the neck"],
         ["Most commonly fractured bone", "**Clavicle** (collar bone)"],
         ["Longest bone of the upper limb", "Humerus"],
         ["Bone that protects the brain", "Skull (cranium); the **soft spot** in "
                                          "a baby's skull is the "
                                          "**fontanelle**"],
         ["Movable bone of the skull", "**Mandible** (lower jaw) \u2014 also the "
                                       "strongest facial bone"]],
        weights=[4.6, 8.0])
    b.h3("Structure of a long bone")
    b.bullets([
        "**Periosteum** \u2014 tough outer membrane carrying blood vessels; "
        "**compact bone** \u2014 dense outer layer; **spongy (cancellous) "
        "bone** \u2014 inner honeycomb; **medullary cavity** \u2014 contains "
        "marrow.",
        "**Epiphysis** (end), **diaphysis** (shaft), **epiphyseal plate** "
        "(growth plate \u2014 injury to it in children can stunt growth).",
        "Bone cells: **osteoblasts** (bone-forming), **osteocytes** (mature) and "
        "**osteoclasts** (bone-resorbing). Vitamin **D** and calcium are needed "
        "for bone formation; deficiency causes **rickets** in children and "
        "**osteomalacia/osteoporosis** in adults.",
    ])
    b.h3("Joints (articulations)")
    b.table(
        ["Class", "Movement", "Examples"],
        [["Fibrous (synarthrosis)", "Immovable / fixed",
          "Sutures of the skull, teeth in sockets"],
         ["Cartilaginous (amphiarthrosis)", "Slightly movable",
          "Between vertebral bodies, symphysis pubis, first rib\u2013sternum"],
         ["Synovial (diarthrosis)", "Freely movable \u2014 have a capsule, "
                                    "synovial membrane and fluid",
          "Shoulder, hip, knee, elbow, wrist"]],
        weights=[3.4, 4.4, 4.8])
    b.table(
        ["Type of synovial joint", "Movement", "Example"],
        [["Ball and socket", "All directions (most mobile)",
          "**Shoulder** (most mobile and most commonly dislocated), **hip**"],
         ["Hinge", "Flexion and extension only", "Elbow, knee, ankle, "
                                                 "interphalangeal joints"],
         ["Pivot (trochoid)", "Rotation", "Atlanto-axial joint (turning the "
                                          "head \u2018no\u2019), radio-ulnar"],
         ["Gliding (plane)", "Sliding", "Between carpals, tarsals, "
                                        "acromio-clavicular"],
         ["Saddle", "Two directions + limited rotation", "Carpo-metacarpal "
                                                         "joint of the "
                                                         "**thumb**"],
         ["Condyloid (ellipsoid)", "Flexion, extension, abduction, adduction",
          "Wrist, metacarpo-phalangeal (knuckle)"]],
        weights=[3.2, 4.4, 5.0])
    b.bullets([
        "**Ligament** = tough fibrous band joining **bone to bone** (stabilises "
        "a joint). **Tendon** = cord joining **muscle to bone**. "
        "**Cartilage** = smooth elastic tissue covering joint surfaces.",
        "**Synovial fluid** lubricates and nourishes the joint cartilage.",
        "The **atlas** (1st cervical vertebra) supports the skull; the **axis** "
        "(2nd) allows rotation. **C7** is the vertebra prominens felt at the "
        "base of the neck.",
    ])

    # ------------------------------------------------------------------
    b.h2("The Muscular System")
    b.p("There are about **600\u2013650 skeletal muscles**, forming "
        "**40\u201345 % of body weight**. Muscles work by contraction, always "
        "in **antagonistic pairs** (one flexes, the other extends).")
    b.table(
        ["Feature", "Skeletal (striated, voluntary)",
         "Smooth (non-striated, involuntary)", "Cardiac"],
        [["Where", "Attached to bones of limbs, trunk, face",
          "Walls of stomach, intestine, blood vessels, bladder, uterus, iris",
          "Only in the wall (myocardium) of the heart"],
         ["Control", "**Voluntary** \u2014 under conscious control",
          "**Involuntary** \u2014 autonomic nerves and hormones",
          "**Involuntary**, but striated; has its own pacemaker"],
         ["Appearance", "Striated, long cylindrical, multinucleate",
          "Spindle-shaped, single central nucleus, no striations",
          "Striated, branched, intercalated discs"],
         ["Fatigue", "Fatigues quickly", "Slow, sustained, does not fatigue "
                                         "easily", "**Never fatigues** "
                                                   "(works lifelong)"],
         ["Function", "Movement, posture, heat production (shivering)",
          "Peristalsis, vasoconstriction, emptying of bladder",
          "Pumping of blood \u2014 about 70 beats/min for life"]],
        weights=[1.7, 4.0, 4.4, 3.5], size=8.6)
    b.h3("Important muscle facts and major muscles")
    b.table(
        ["Muscle / fact", "Detail"],
        [["Largest / strongest muscle", "**Gluteus maximus** (buttock) \u2014 "
                                        "largest; **masseter** (jaw) \u2014 "
                                        "strongest by force; the **heart** is "
                                        "the hardest-working muscle"],
         ["Smallest muscle", "**Stapedius** (in the middle ear)"],
         ["Longest muscle", "**Sartorius** (front of thigh)"],
         ["Chief muscle of respiration", "**Diaphragm** (dome-shaped; supplied "
                                         "by the **phrenic nerve**, C3\u2013C5) "
                                         "assisted by the intercostals"],
         ["Muscles of the shoulder/arm", "Deltoid (abducts arm), biceps brachii "
                                         "(flexes elbow), triceps (extends "
                                         "elbow), pectoralis major (chest), "
                                         "trapezius and latissimus dorsi (back)"],
         ["Muscles of the leg", "Quadriceps femoris (extends knee), hamstrings "
                                "(flex knee), gastrocnemius and soleus (calf "
                                "\u2192 Achilles tendon), tibialis anterior"],
         ["Abdominal muscles", "Rectus abdominis, external and internal oblique, "
                               "transversus abdominis \u2014 protect viscera and "
                               "help in expiration, coughing, defaecation"],
         ["Strongest tendon", "**Achilles (calcaneal) tendon** \u2014 attaches "
                              "calf muscles to the heel bone"],
         ["Energy for contraction", "**ATP**; fuel is glucose and oxygen. "
                                    "Anaerobic work produces **lactic acid** "
                                    "\u2192 muscle cramp and fatigue"],
         ["Muscle tone", "Continuous partial contraction that maintains posture; "
                         "lost in unconsciousness \u2014 this is why the tongue "
                         "falls back and blocks the airway"]],
        weights=[3.4, 9.2])

    # ------------------------------------------------------------------
    b.h2("The Circulatory (Cardio-Vascular) System")
    b.p("Consists of the **heart** (pump), the **blood vessels** (pipes) and the "
        "**blood** (transport medium). Discovery of circulation \u2014 "
        "**William Harvey**.")
    b.h3("The heart")
    b.bullets([
        "Cone-shaped muscular organ the size of a closed fist; weight "
        "**250\u2013350 g**; lies in the **mediastinum**, behind the sternum, "
        "**two-thirds to the left** of the midline; apex points down and to the "
        "left at the level of the 5th intercostal space.",
        "Covered by a double membrane, the **pericardium**; its wall has three "
        "layers \u2014 **endocardium** (inner), **myocardium** (thick muscle) and "
        "**epicardium/pericardium** (outer).",
        "**Four chambers** \u2014 right atrium, right ventricle, left atrium, "
        "left ventricle. The **left ventricle has the thickest wall** because it "
        "pumps blood to the whole body.",
        "**Valves** prevent backflow: **tricuspid** (right atrium \u2192 right "
        "ventricle), **bicuspid/mitral** (left atrium \u2192 left ventricle), "
        "**pulmonary** (right ventricle \u2192 pulmonary artery) and **aortic** "
        "(left ventricle \u2192 aorta). Heart sounds **\u2018lub\u2019 (S1)** = "
        "closure of tricuspid and mitral, **\u2018dub\u2019 (S2)** = closure of "
        "aortic and pulmonary valves.",
        "**Pacemaker = SA (sino-atrial) node** in the right atrium \u2192 AV node "
        "\u2192 bundle of His \u2192 Purkinje fibres. The heart's own blood supply "
        "comes from the **coronary arteries** (first branches of the aorta); "
        "their blockage causes **heart attack (myocardial infarction)**.",
        "**Cardiac output** = stroke volume (\u2248 70 ml) \u00d7 heart rate "
        "(\u2248 72/min) = about **5 litres/minute**. The heart beats about "
        "**100,000 times a day**.",
    ])
    b.h3("Circulation \u2014 the two circuits")
    b.table(
        ["Circuit", "Path", "Note"],
        [["**Pulmonary circulation** (heart \u2192 lungs \u2192 heart)",
          "Right atrium \u2192 right ventricle \u2192 pulmonary artery \u2192 "
          "lungs \u2192 pulmonary veins \u2192 left atrium",
          "The **pulmonary artery is the only artery carrying deoxygenated "
          "blood**; the **pulmonary vein is the only vein carrying oxygenated "
          "blood**"],
         ["**Systemic circulation** (heart \u2192 body \u2192 heart)",
          "Left atrium \u2192 left ventricle \u2192 aorta \u2192 arteries "
          "\u2192 capillaries of the body \u2192 veins \u2192 superior and "
          "inferior vena cava \u2192 right atrium",
          "Carries oxygen and nutrients to every cell and removes CO\u2082 and "
          "wastes"],
         ["**Portal circulation**",
          "Veins of the stomach, intestine, spleen and pancreas \u2192 hepatic "
          "portal vein \u2192 liver \u2192 hepatic vein \u2192 inferior vena "
          "cava",
          "Allows the liver to process absorbed food and detoxify"],
         ["**Coronary circulation**",
          "Aorta \u2192 right and left coronary arteries \u2192 heart muscle",
          "Supplies the myocardium itself"]],
        weights=[3.0, 5.4, 4.8], first_bold=False, size=8.8)
    b.h3("Blood vessels")
    b.table(
        ["Feature", "Artery", "Vein", "Capillary"],
        [["Direction", "Carries blood **away from** the heart",
          "Carries blood **towards** the heart",
          "Connects arterioles to venules"],
         ["Blood", "Oxygenated (except pulmonary artery)",
          "Deoxygenated (except pulmonary vein)", "Exchange of gases, nutrients "
                                                  "and wastes with tissues"],
         ["Wall", "Thick, muscular, elastic", "Thin, less elastic",
          "One cell thick (endothelium only)"],
         ["Valves", "Absent", "**Present** (prevent backflow against gravity)",
          "Absent"],
         ["Pressure / flow", "High pressure, pulsating, rapid",
          "Low pressure, steady, slow", "Very slow \u2014 allows exchange"],
         ["Bleeding pattern", "**Bright red, spurts in jets with each beat**",
          "**Dark red, steady flow / oozes**", "**Oozes slowly from the whole "
                                               "surface**"],
         ["Position", "Deep (protected)", "Mostly superficial",
          "In every tissue"]],
        weights=[2.1, 3.7, 3.5, 3.3], size=8.6)
    b.bullets([
        "**Largest artery** = **aorta**; **largest veins** = superior and "
        "inferior **vena cava**; **largest lymphatic vessel** = thoracic duct.",
        "Total length of all blood vessels \u2248 **96,000 km**; capillaries are "
        "the most numerous (~5\u201310 \u00b5m wide).",
        "**Blood pressure** = the pressure of blood on arterial walls. Normal "
        "adult = **120/80 mm Hg** (systolic/diastolic); measured with a "
        "**sphygmomanometer** over the **brachial artery**. Hypertension "
        "\u2265 140/90; hypotension < 90/60.",
    ])
    b.h3("Blood \u2014 composition and functions")
    b.table(
        ["Component", "Normal value", "Function"],
        [["Plasma (55 %)", "91 % water + proteins (albumin, globulin, "
                           "fibrinogen), salts, glucose, hormones, wastes",
          "Transport medium; maintains blood volume, pressure and osmotic "
          "balance"],
         ["RBC (erythrocytes)", "Male 4.5\u20135.5 million/mm\u00b3; "
                                "female 4.0\u20135.0 million/mm\u00b3; "
                                "lifespan **120 days**",
          "Carry **oxygen** as oxyhaemoglobin; no nucleus; made in red bone "
          "marrow, destroyed in the spleen (\u2018graveyard of RBCs\u2019)"],
         ["Haemoglobin", "Male **13\u201318 g/dl**, female **12\u201316 g/dl**",
          "Iron-containing red pigment that binds oxygen; low level = "
          "**anaemia**"],
         ["WBC (leucocytes)", "**4,000\u201311,000/mm\u00b3**",
          "**Defence** against infection; neutrophils (most numerous, 60\u201370 "
          "%) phagocytose bacteria; lymphocytes make antibodies; eosinophils in "
          "allergy"],
         ["Platelets (thrombocytes)", "**1.5\u20134.5 lakh/mm\u00b3** "
                                      "(150,000\u2013450,000)",
          "**Clotting** of blood; lifespan 8\u201310 days"],
         ["Clotting time / bleeding time", "Clotting 3\u20138 min; "
                                           "bleeding 1\u20134 min",
          "Clotting needs **vitamin K**, calcium, prothrombin and fibrinogen: "
          "fibrinogen \u2192 **fibrin** mesh \u2192 clot"]],
        weights=[2.5, 4.4, 5.7], size=8.8)
    b.bullets([
        "**Functions of blood (mnemonic: T-R-P-D)** \u2014 **T**ransport "
        "(O\u2082, CO\u2082, food, hormones, wastes), **R**egulation "
        "(temperature, pH, water balance), **P**rotection (WBC, antibodies, "
        "clotting) and **D**efence against infection.",
        "**pH of blood = 7.35\u20137.45** (slightly alkaline). Colour is due to "
        "haemoglobin; blood is **8 % of body weight**.",
        "**Blood groups (Landsteiner)** \u2014 A, B, AB, O. **O negative = "
        "universal donor**; **AB positive = universal recipient**. Rh factor "
        "present = Rh positive. Group **O** is commonest in India, **AB** the "
        "rarest.",
        "**Anticoagulants:** heparin (natural, from liver/mast cells), citrate "
        "and EDTA (in blood bags); stored blood keeps for **35\u201342 days** at "
        "2\u20136 \u00b0C.",
    ])
    b.h3("Pulse \u2014 where to feel it")
    b.table(
        ["Pulse point", "Artery / site", "Use in first aid"],
        [["Radial", "Thumb-side of the front of the wrist",
          "Routine pulse counting in a conscious casualty"],
         ["Carotid", "Side of the neck, beside the windpipe",
          "Pulse check in a collapsed casualty (trained rescuers only, "
          "\u2264 10 s)"],
         ["Brachial", "Inner side of the arm above the elbow",
          "Blood pressure; pulse check in **infants**; pressure point for arm "
          "bleeding"],
         ["Femoral", "Groin, midway along the fold",
          "Pressure point for severe leg bleeding"],
         ["Temporal", "In front of the ear", "Bleeding from the scalp"],
         ["Facial", "Lower border of the jaw",
          "Bleeding from the face"],
         ["Popliteal / Posterior tibial / Dorsalis pedis",
          "Behind the knee / behind the inner ankle / top of the foot",
          "To confirm circulation beyond a splint or bandage"]],
        weights=[3.0, 4.4, 5.2])
    b.p("Normal pulse = **60\u2013100 beats/min** (average 72). **Tachycardia** "
        "> 100/min; **bradycardia** < 60/min. Note rate, **rhythm** (regular or "
        "irregular) and **volume** (strong, weak, thready). A **rapid, weak, "
        "thready pulse is the classical sign of shock**.")
    b.h3("The lymphatic system (part of circulation and defence)")
    b.bullets([
        "Consists of **lymph**, lymph capillaries and vessels, **lymph nodes**, "
        "**spleen**, **thymus**, tonsils and Peyer's patches.",
        "Functions \u2014 drains excess tissue fluid back to the blood, absorbs "
        "**fats** from the intestine (through lacteals), filters out bacteria in "
        "the nodes, and produces **lymphocytes** and antibodies.",
        "**Spleen** \u2014 largest lymphatic organ, in the left hypochondrium; "
        "stores blood, destroys old RBCs; easily ruptured in left-sided abdominal "
        "injury \u2192 severe internal bleeding.",
        "Lymph flows in **one direction only** (towards the heart) and is moved "
        "by muscle contraction and breathing; the **thoracic duct** empties into "
        "the left subclavian vein.",
    ])

    # ------------------------------------------------------------------
    b.h2("The Respiratory System")
    b.p("Respiration supplies **oxygen** to the cells and removes **carbon "
        "dioxide**. Breathing (ventilation) is only its mechanical part.")
    b.table(
        ["Part", "Points to remember"],
        [["Nose", "Air is **warmed, moistened and filtered**; lined by ciliated "
                  "mucous membrane. The nose is the correct route of breathing."],
         ["Pharynx (throat)", "Common passage for air and food; divided into "
                              "naso-, oro- and laryngo-pharynx."],
         ["Larynx (voice box)", "Contains the vocal cords; the **epiglottis** "
                                "closes it during swallowing so that food goes "
                                "into the oesophagus, not the windpipe."],
         ["Trachea (windpipe)", "About **10\u201312 cm** long, held open by "
                                "**16\u201320 C-shaped cartilage rings**; "
                                "divides at the level of T4\u2013T5 into two "
                                "bronchi."],
         ["Bronchi and bronchioles", "**Right bronchus is shorter, wider and "
                                     "more vertical** \u2014 therefore inhaled "
                                     "foreign bodies usually enter the right "
                                     "lung."],
         ["Alveoli", "About **300 million** thin-walled air sacs; total surface "
                     "area **70\u201380 m\u00b2**; site of **gas exchange by "
                     "diffusion** across a membrane one cell thick."],
         ["Lungs", "Cone-shaped, spongy; **right lung has 3 lobes**, "
                   "**left has 2** (to make room for the heart \u2014 cardiac "
                   "notch). Covered by the **pleura** with pleural fluid "
                   "between its two layers."],
         ["Diaphragm", "Main muscle of breathing; contracts and flattens during "
                       "inspiration."]],
        weights=[2.6, 10.0])
    b.h3("Mechanism of breathing")
    b.table(
        ["", "Inspiration (active)", "Expiration (passive at rest)"],
        [["Muscles", "Diaphragm contracts and descends; external intercostals "
                     "contract and raise the ribs",
          "Diaphragm and intercostals relax; elastic recoil of the lungs"],
         ["Chest cavity", "Increases in all three diameters",
          "Decreases"],
         ["Pressure inside", "Falls below atmospheric \u2192 air rushes **in**",
          "Rises above atmospheric \u2192 air is pushed **out**"],
         ["Duration", "About 2 seconds", "About 3 seconds"]],
        weights=[2.2, 5.4, 5.0])
    b.h3("Respiratory values and air composition")
    b.table(
        ["Value", "Normal figure"],
        [["Respiratory rate \u2014 adult", "**12\u201320/min** (average "
                                           "16\u201318); child 20\u201330; "
                                           "infant 30\u201360; newborn "
                                           "40\u201360"],
         ["Tidal volume", "**500 ml** (about 6\u20138 ml/kg) per quiet breath"],
         ["Vital capacity", "**4,000\u20135,000 ml** (about 4.8 litres in men)"],
         ["Total lung capacity", "About **6,000 ml**"],
         ["Residual volume", "1,200 ml \u2014 air that can never be breathed out"],
         ["Dead space", "About **150 ml** of air that does not take part in "
                        "exchange"],
         ["Ratio of respiration to pulse", "About **1 : 4**"],
         ["Control centre", "**Medulla oblongata** (respiratory centre), "
                            "stimulated chiefly by a rise in **CO\u2082** in "
                            "the blood"]],
        weights=[3.4, 9.2])
    b.table(
        ["Gas", "Inspired (atmospheric) air", "Expired air", "Alveolar air"],
        [["Oxygen", "**21 %**", "**16 %**", "14 %"],
         ["Carbon dioxide", "**0.04 %**", "**4 %**", "5.5 %"],
         ["Nitrogen", "79 %", "79 %", "80 %"],
         ["Water vapour", "Variable", "Saturated", "Saturated"],
         ["Temperature", "Atmospheric", "Body temperature", "Body temperature"]],
        weights=[2.6, 4.0, 3.0, 3.0], align=["l", "c", "c", "c"])
    b.box("FIRST-AID SIGNIFICANCE", [
        "Expired air still contains **16 % oxygen** \u2014 that is why "
        "**mouth-to-mouth respiration works**.",
        "The brain uses **20 % of the body's oxygen**; it cannot store oxygen, "
        "hence damage begins within 3\u20134 minutes of stopped breathing.",
        "**Difficulty in breathing = dyspnoea**; absent breathing = "
        "**apnoea**; blue discoloration from lack of oxygen = "
        "**cyanosis** (seen first in lips, tongue, nail beds and ear lobes); "
        "rapid breathing = tachypnoea.",
        "In an unconscious casualty the commonest cause of airway obstruction is "
        "the **tongue falling back** \u2014 hence head tilt and chin lift.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("The Nervous System")
    b.p("The control and communication system of the body. Structural unit = "
        "the **neuron** (nerve cell), which cannot regenerate once destroyed.")
    b.table(
        ["Division", "Parts", "Function"],
        [["**Central nervous system (CNS)**", "**Brain** + **spinal cord**",
          "Receives, interprets and stores information; initiates responses"],
         ["**Peripheral nervous system (PNS)**", "**12 pairs of cranial "
                                                 "nerves** + **31 pairs of "
                                                 "spinal nerves**",
          "Carries sensory impulses to and motor impulses from the CNS"],
         ["**Autonomic nervous system (ANS)**", "**Sympathetic** and "
                                                "**parasympathetic** divisions",
          "Involuntary control of heart, glands, gut, vessels and pupils"]],
        weights=[3.4, 4.2, 5.0], first_bold=False)
    b.h3("Parts of the brain and their functions")
    b.table(
        ["Part", "Function"],
        [["Cerebrum (largest part; 2 hemispheres, grey outer cortex)",
          "**Higher functions** \u2014 intelligence, memory, reasoning, speech, "
          "emotion, will, and the centres for voluntary movement and sensation. "
          "The **left** hemisphere controls the **right** side of the body "
          "(crossed control)."],
         ["Cerebellum (\u2018little brain\u2019, behind and below)",
          "**Balance, posture, co-ordination** of voluntary movement and muscle "
          "tone. Damage \u2192 staggering gait, tremors."],
         ["Mid-brain", "Relay for visual and auditory reflexes; pupil reflex."],
         ["Pons", "Bridge between the parts of the brain; helps control "
                  "breathing rhythm."],
         ["Medulla oblongata (lowest part, continues as the spinal cord)",
          "==Vital centres== \u2014 **respiratory, cardiac (heart rate) and "
          "vasomotor (blood pressure)** centres, plus reflexes of swallowing, "
          "coughing, sneezing and vomiting. Injury here is rapidly fatal."],
         ["Hypothalamus", "**Temperature regulation**, hunger, thirst, sleep, "
                          "emotion; controls the pituitary gland."],
         ["Thalamus", "Relay station for sensations, especially pain."],
         ["Brain stem", "Mid-brain + pons + medulla; controls consciousness and "
                        "vital functions."]],
        weights=[3.6, 9.0])
    b.bullets([
        "Brain weight \u2248 **1,300\u20131,400 g**; it contains about "
        "**86\u2013100 billion neurons** and receives **15\u201320 % of the "
        "cardiac output**.",
        "**Meninges** = three protective membranes \u2014 **dura mater** "
        "(outer, tough), **arachnoid mater** (middle) and **pia mater** (inner, "
        "delicate). Inflammation = **meningitis**.",
        "**Cerebrospinal fluid (CSF)** \u2014 about **130\u2013150 ml**, "
        "circulates in the ventricles and around the cord, acting as a "
        "**shock absorber** and nutrient medium. Clear watery fluid leaking from "
        "the ear or nose after a head injury is CSF and indicates a **fractured "
        "base of the skull**.",
        "**Spinal cord** \u2014 about **45 cm** long, extends from the medulla "
        "to the level of **L1\u2013L2**; gives off **31 pairs** of spinal nerves "
        "(**cervical 8, thoracic 12, lumbar 5, sacral 5, coccygeal 1**).",
        "**Reflex action** \u2014 an involuntary, rapid, protective response "
        "(knee jerk, blinking, withdrawal from heat). Reflex arc = receptor "
        "\u2192 sensory neuron \u2192 **spinal cord** \u2192 motor neuron \u2192 "
        "effector muscle. It does **not** involve the brain, which is why it is "
        "fast.",
    ])
    b.h3("The twelve cranial nerves (mnemonic and functions)")
    b.box("MNEMONIC FOR ORDER", [
        "**O**n **O**ld **O**lympus' **T**owering **T**op, **A** **F**inn "
        "**A**nd **G**erman **V**iewed **S**ome **H**ops \u2014 Olfactory, "
        "Optic, Oculomotor, Trochlear, Trigeminal, Abducent, Facial, "
        "Auditory (vestibulocochlear), Glossopharyngeal, Vagus, Spinal "
        "accessory, Hypoglossal.",
        "For type: **S**ome **S**ay **M**arry **M**oney, **B**ut **M**y "
        "**B**rother **S**ays **B**ig **B**rains **M**atter **M**ore "
        "(S = sensory, M = motor, B = both).",
    ], kind="mnemonic")
    b.table(
        ["No.", "Nerve", "Type", "Main function"],
        [["I", "Olfactory", "Sensory", "Smell"],
         ["II", "Optic", "Sensory", "Vision"],
         ["III", "Oculomotor", "Motor", "Movement of the eyeball; constriction "
                                        "of the pupil; raising the eyelid"],
         ["IV", "Trochlear", "Motor", "Downward and outward eye movement "
                                      "(superior oblique)"],
         ["V", "Trigeminal", "Both", "Sensation of the face; muscles of "
                                     "chewing \u2014 the **largest** cranial "
                                     "nerve"],
         ["VI", "Abducent", "Motor", "Outward movement of the eye "
                                     "(lateral rectus)"],
         ["VII", "Facial", "Both", "Muscles of facial expression; taste from the "
                                   "front of the tongue; tears and saliva"],
         ["VIII", "Vestibulocochlear (auditory)", "Sensory",
          "**Hearing and balance**"],
         ["IX", "Glossopharyngeal", "Both", "Taste from the back of the tongue; "
                                            "swallowing; gag reflex"],
         ["X", "Vagus", "Both", "**Longest** cranial nerve \u2014 supplies "
                                "heart, lungs and gut; slows the heart; "
                                "parasympathetic"],
         ["XI", "Spinal accessory", "Motor", "Movement of the neck and shoulder "
                                             "muscles"],
         ["XII", "Hypoglossal", "Motor", "Movement of the tongue"]],
        weights=[0.9, 3.2, 1.4, 7.1], align=["c", "l", "c", "l"])
    b.h3("Sympathetic versus parasympathetic (autonomic) actions")
    b.table(
        ["Organ", "Sympathetic (\u2018fight or flight\u2019)",
         "Parasympathetic (\u2018rest and digest\u2019)"],
        [["Heart", "Rate and force **increase**", "Rate **decreases**"],
         ["Bronchi", "Dilate (more air)", "Constrict"],
         ["Pupils", "**Dilate**", "**Constrict**"],
         ["Skin vessels", "Constrict \u2192 pallor, cold clammy skin",
          "Dilate"],
         ["Sweat glands", "**Increased sweating**", "Little effect"],
         ["Gut / digestion", "Slowed, mouth becomes dry",
          "Peristalsis and secretion increase"],
         ["Adrenal gland", "Secretes **adrenaline**", "\u2014"],
         ["Chief transmitter", "Noradrenaline / adrenaline", "Acetylcholine"]],
        weights=[2.2, 5.4, 5.0])
    b.p("All the classical signs of **shock and fear** \u2014 pale cold clammy "
        "skin, rapid pulse, dilated pupils, dry mouth, rapid breathing \u2014 "
        "are sympathetic (adrenaline) effects. This is why they appear together.")

    # ------------------------------------------------------------------
    b.h2("The Digestive System")
    b.p("The alimentary canal is a muscular tube about **9 metres (30 feet)** "
        "long from mouth to anus, with accessory organs opening into it.")
    b.table(
        ["Part", "Length / size", "Function and points to remember"],
        [["Mouth", "\u2014", "**Mastication** (chewing) and mixing with saliva; "
                             "**salivary amylase (ptyalin)** begins starch "
                             "digestion. Three pairs of salivary glands \u2014 "
                             "parotid (largest), submandibular, sublingual; "
                             "1\u20131.5 litres of saliva daily."],
         ["Teeth", "**32 permanent**, **20 milk (deciduous)** teeth",
          "Incisors (cut), canines (tear), premolars and molars (grind); "
          "hardest substance = **enamel**."],
         ["Pharynx & oesophagus", "Oesophagus **25 cm**",
          "Swallowing (deglutition); food is pushed by **peristalsis**. The "
          "epiglottis guards the airway."],
         ["Stomach", "Capacity **1\u20131.5 litres**",
          "Stores and churns food; secretes **HCl** (kills bacteria, pH "
          "1.5\u20133.5), **pepsin** (protein), rennin and mucus; forms "
          "**chyme**. Intrinsic factor for vitamin B\u2081\u2082 absorption."],
         ["Small intestine", "**6\u20137 m** \u2014 duodenum 25 cm, jejunum, "
                             "ileum",
          "**Main site of digestion and absorption**; villi enormously increase "
          "surface area; receives bile and pancreatic juice in the duodenum."],
         ["Large intestine", "**1.5 m** \u2014 caecum, appendix, colon, rectum, "
                             "anal canal",
          "**Absorption of water**, salts and some vitamins; formation and "
          "storage of faeces; bacterial flora make vitamin K and B."],
         ["Liver", "**Largest gland/internal organ, 1.2\u20131.5 kg**, right "
                   "hypochondrium",
          "Secretes **bile** (emulsifies fat), stores glycogen, iron and "
          "vitamins, **detoxifies** poisons and alcohol, forms urea and plasma "
          "proteins, produces heat, destroys old RBCs. Only organ that can "
          "**regenerate**."],
         ["Gall bladder", "Stores 30\u201350 ml", "Stores and concentrates bile."],
         ["Pancreas", "12\u201315 cm, behind the stomach",
          "**Dual gland** \u2014 exocrine: pancreatic juice (amylase, lipase, "
          "trypsin); endocrine: **insulin and glucagon** from the islets of "
          "Langerhans."]],
        weights=[2.1, 2.9, 8.2], size=8.8)
    b.h3("Digestive enzymes at a glance")
    b.table(
        ["Enzyme", "Source", "Acts on", "Converts to"],
        [["Salivary amylase (ptyalin)", "Saliva", "Starch", "Maltose"],
         ["Pepsin", "Stomach (with HCl)", "Proteins", "Peptones"],
         ["Rennin", "Stomach (infants)", "Milk casein", "Curd"],
         ["Trypsin", "Pancreas", "Proteins/peptones", "Amino acids"],
         ["Pancreatic amylase", "Pancreas", "Starch", "Maltose/glucose"],
         ["Lipase (+ bile salts)", "Pancreas", "Fats", "Fatty acids + glycerol"],
         ["Maltase, sucrase, lactase", "Small intestine", "Disaccharides",
          "Glucose (monosaccharides)"],
         ["Bile (not an enzyme)", "Liver", "Fat", "Emulsified fat droplets"]],
        weights=[3.4, 2.6, 2.6, 3.4])
    b.p("**End products absorbed:** carbohydrates as **glucose**, proteins as "
        "**amino acids**, fats as **fatty acids and glycerol** (through "
        "lacteals into the lymph). Balanced diet = carbohydrate, protein, fat, "
        "vitamins, minerals, water and fibre. **1 g carbohydrate/protein = 4 "
        "kcal; 1 g fat = 9 kcal.**")

    # ------------------------------------------------------------------
    b.h2("The Urinary (Excretory) System")
    b.table(
        ["Organ", "Facts"],
        [["Kidneys (2)", "Bean-shaped, **11 \u00d7 6 \u00d7 3 cm**, ~150 g "
                         "each, at the back of the abdomen at T12\u2013L3; the "
                         "**right kidney is slightly lower** (liver above it). "
                         "Functional unit = **nephron** (about **1 million per "
                         "kidney**)."],
         ["Ureters (2)", "**25\u201330 cm** muscular tubes carrying urine from "
                         "kidney to bladder by peristalsis."],
         ["Urinary bladder", "Muscular reservoir in the pelvis; capacity "
                             "**400\u2013600 ml**; desire to pass urine at "
                             "about 200\u2013300 ml."],
         ["Urethra", "Male **18\u201320 cm**, female **4 cm** (hence urinary "
                     "infection is commoner in women)."]],
        weights=[2.6, 10.0])
    b.bullets([
        "**Functions of the kidney:** excretion of urea, uric acid, creatinine "
        "and drugs; regulation of **water and electrolyte balance**, **blood "
        "pressure** (renin) and **acid-base balance**; secretion of "
        "**erythropoietin** (stimulates RBC formation) and activation of "
        "**vitamin D**.",
        "Urine formation = **glomerular filtration \u2192 selective "
        "reabsorption \u2192 tubular secretion**. About **180 litres** are "
        "filtered daily, of which **1\u20131.5 litres** are excreted as urine.",
        "Normal urine \u2014 pale amber, aromatic, pH ~6, specific gravity "
        "1.010\u20131.030, 96 % water + urea (main solid waste), uric acid, "
        "creatinine, salts. **Sugar, protein, blood, ketones and pus are "
        "abnormal.**",
        "Normal output **\u2265 30 ml/hour (0.5 ml/kg/h)**. Reduced output "
        "(**oliguria**) or none (**anuria**) is an important sign of **shock, "
        "dehydration or severe burns**. Excessive urine = polyuria; painful = "
        "dysuria; blood in urine = haematuria.",
        "Other excretory organs: **skin** (water, salt, urea in sweat), **lungs** "
        "(CO\u2082 and water vapour), **liver** (bile pigments) and **large "
        "intestine** (faeces).",
    ])

    # ------------------------------------------------------------------
    b.h2("The Endocrine System")
    b.p("Ductless glands that pour **hormones** ('chemical messengers') directly "
        "into the blood. Action is slower but longer-lasting than nervous "
        "control.")
    b.table(
        ["Gland", "Chief hormone(s)", "Action / deficiency-excess"],
        [["**Pituitary** (\u2018master gland\u2019, pea-sized, base of brain)",
          "Growth hormone, TSH, ACTH, FSH/LH, prolactin, **ADH (vasopressin)** "
          "and oxytocin from the posterior lobe",
          "Controls other glands and growth. Excess GH \u2192 gigantism/"
          "acromegaly; deficiency \u2192 dwarfism; lack of ADH \u2192 "
          "**diabetes insipidus**"],
         ["**Thyroid** (largest endocrine gland, in the neck)",
          "**Thyroxine (T4), T3** and calcitonin",
          "Controls **metabolic rate**. Deficiency \u2192 cretinism (child), "
          "myxoedema (adult), **goitre** with iodine lack; excess \u2192 "
          "thyrotoxicosis with bulging eyes"],
         ["Parathyroid (4, behind the thyroid)", "Parathormone",
          "Regulates **calcium**; deficiency \u2192 tetany (muscle spasm, "
          "cramps)"],
         ["**Adrenal (suprarenal)**, above each kidney",
          "Medulla: **adrenaline (epinephrine)** and noradrenaline. "
          "Cortex: cortisol, aldosterone, sex hormones",
          "Adrenaline = the **emergency hormone** (fight or flight): raises "
          "heart rate, BP and blood sugar, dilates pupils and bronchi \u2014 "
          "used as the **drug of choice in anaphylaxis**. Cortisol deficiency "
          "\u2192 Addison's disease"],
         ["**Pancreas** \u2014 islets of Langerhans",
          "**Insulin** (beta cells) and **glucagon** (alpha cells)",
          "Insulin **lowers** blood glucose; glucagon raises it. Lack of insulin "
          "\u2192 **diabetes mellitus**; excess insulin or missed meal \u2192 "
          "**hypoglycaemia**"],
         ["Ovaries / Testes", "Oestrogen and progesterone / testosterone",
          "Secondary sexual characters, reproduction, menstrual cycle"],
         ["Thymus", "Thymosin", "Maturation of T-lymphocytes (immunity); "
                                "largest in childhood"],
         ["Pineal", "Melatonin", "Sleep-wake (circadian) rhythm"]],
        weights=[3.0, 4.0, 5.6], first_bold=False, size=8.8)
    b.p("Normal **fasting blood glucose = 70\u2013110 mg/dl**; post-prandial "
        "< 140 mg/dl. Below **70 mg/dl = hypoglycaemia** (a first-aid "
        "emergency \u2014 give sugar); above 200 mg/dl random suggests diabetes.")

    # ------------------------------------------------------------------
    b.h2("The Skin (Integumentary System) and Temperature Regulation")
    b.p("The skin is the ==largest organ of the body== \u2014 area about "
        "**1.5\u20132 m\u00b2**, weight about 4 kg (16 % of body weight).")
    b.table(
        ["Layer", "Details"],
        [["Epidermis (outer)", "No blood vessels; several layers of epithelium; "
                               "outermost dead **keratin** layer; contains "
                               "**melanin** (colour, protects from UV). Renews "
                               "every 4 weeks."],
         ["Dermis (true skin)", "Contains **blood vessels, nerve endings, sweat "
                                "glands, sebaceous (oil) glands, hair follicles** "
                                "and collagen/elastic fibres. Pain of a burn "
                                "comes from these nerve endings."],
         ["Subcutaneous layer", "**Adipose (fatty) tissue** \u2014 insulation, "
                                "energy store, shock absorption."]],
        weights=[2.6, 10.0])
    b.h3("Functions of the skin (mnemonic: S-H-A-P-E-S)")
    b.bullets([
        "**S**ensation \u2014 touch, pain, pressure, heat and cold receptors.",
        "**H**eat regulation \u2014 sweating and dilatation of vessels lose heat; "
        "constriction and shivering conserve it.",
        "**A**bsorption of some drugs and ointments, and **excretion** of water, "
        "salt and urea as sweat (500\u2013700 ml daily).",
        "**P**rotection \u2014 barrier against injury, micro-organisms, "
        "chemicals and ultraviolet light (the body's **first line of defence**).",
        "**E**laboration of **vitamin D** from sunlight.",
        "**S**torage of fat and water; **cosmetic/identity** (fingerprints).",
    ])
    b.box("TEMPERATURE FACTS", [
        "Normal body temperature **98.4 \u00b0F (37 \u00b0C)**; oral, axillary "
        "(0.5\u00b0 lower) and rectal (0.5\u00b0 higher) sites. "
        "\u00b0C = (\u00b0F \u2212 32) \u00d7 5/9.",
        "**Fever (pyrexia)** > 99 \u00b0F; **hyperpyrexia** > 105 \u00b0F; "
        "**hypothermia** < 95 \u00b0F (35 \u00b0C).",
        "Heat is produced by metabolism, muscle activity and shivering; lost by "
        "**radiation, conduction, convection and evaporation** (sweating) \u2014 "
        "and also through breathing, urine and faeces.",
        "The **hypothalamus** is the body's thermostat.",
        "Loss of skin (as in burns) causes loss of fluid, heat and the barrier "
        "against infection \u2014 the three dangers of a major burn.",
    ], kind="key")

    # ------------------------------------------------------------------
    b.h2("The Sense Organs")
    b.table(
        ["Organ", "Structure", "Function / first-aid relevance"],
        [["**Eye**", "Sclera (white), cornea (transparent front), iris with "
                     "**pupil**, lens, aqueous and vitreous humour, "
                     "**retina** with rods (dim light) and cones (colour), "
                     "optic nerve, conjunctiva, lacrimal (tear) gland",
          "Vision. **Pupil signs** are vital: equal and reacting = normal; "
          "**unequal** = head injury/stroke; **pinpoint** = morphine/opium "
          "poisoning or organophosphate; **widely dilated and fixed** = cardiac "
          "arrest, deep unconsciousness, atropine/dhatura poisoning"],
         ["**Ear**", "**Outer** \u2014 pinna and canal up to the eardrum "
                     "(tympanic membrane); **middle** \u2014 3 ossicles "
                     "(malleus, incus, stapes) and the **Eustachian tube** to "
                     "the throat; **inner** \u2014 cochlea (hearing) and "
                     "**semicircular canals** (balance)",
          "Hearing and **equilibrium**. Bleeding or clear fluid from the ear "
          "after a head injury suggests a **fractured base of skull** \u2014 "
          "never plug the ear"],
         ["**Nose**", "Nasal cavity with ciliated mucosa, turbinates, olfactory "
                      "nerve endings; rich blood supply in the septum",
          "Smell; filters, warms and moistens air. The rich vessels explain "
          "**epistaxis** (nose bleed)"],
         ["**Tongue**", "Papillae with taste buds; muscular organ",
          "Taste (sweet, salt, sour, bitter, umami), speech, chewing and "
          "swallowing. Falls back and blocks the airway in unconsciousness"],
         ["**Skin**", "Nerve endings in the dermis",
          "Touch, pressure, pain, heat and cold"]],
        weights=[1.7, 5.3, 5.6], first_bold=False, size=8.8)

    # ------------------------------------------------------------------
    b.h2("The Reproductive System (in brief)")
    b.bullets([
        "**Male:** two testes (in the scrotum) producing **sperm** and "
        "**testosterone**; epididymis, vas deferens, seminal vesicles, prostate "
        "gland, urethra and penis.",
        "**Female:** two **ovaries** producing **ova** and the hormones "
        "oestrogen and progesterone; fallopian tubes (site of fertilisation), "
        "**uterus** (for pregnancy), cervix, vagina and external genitalia; "
        "**breasts** for lactation.",
        "**Menstrual cycle** \u2014 about **28 days**; ovulation on about day "
        "14. **Pregnancy (gestation)** = **280 days / 40 weeks / 9 calendar "
        "months**, divided into three trimesters.",
        "First-aid relevance: pregnancy alters first aid \u2014 a pregnant "
        "casualty is turned onto her **left side** (to prevent the uterus "
        "pressing on the inferior vena cava), CPR compressions are given "
        "slightly higher on the sternum, and bleeding in pregnancy is always an "
        "emergency.",
    ])

    # ------------------------------------------------------------------
    b.h2("Master Table of Normal Values (learn by heart)")
    b.table(
        ["Parameter", "Normal value"],
        [["Body temperature", "98.4 \u00b0F / 37 \u00b0C"],
         ["Pulse (adult)", "60\u2013100 beats/min (avg 72)"],
         ["Respiration (adult)", "12\u201320 breaths/min (avg 16\u201318)"],
         ["Blood pressure (adult)", "120/80 mm Hg"],
         ["Blood volume", "5\u20136 litres (8 % of body weight)"],
         ["Haemoglobin", "M 13\u201318 g/dl, F 12\u201316 g/dl"],
         ["RBC count", "4.5\u20135.5 million/mm\u00b3"],
         ["WBC count", "4,000\u201311,000/mm\u00b3"],
         ["Platelet count", "1.5\u20134.5 lakh/mm\u00b3"],
         ["Blood pH", "7.35\u20137.45"],
         ["Fasting blood sugar", "70\u2013110 mg/dl"],
         ["Urine output", "1\u20131.5 litre/day (\u2265 30 ml/hour)"],
         ["Tidal volume", "500 ml"],
         ["Cardiac output", "5 litres/min"],
         ["SpO\u2082", "95\u2013100 %"],
         ["CSF volume", "130\u2013150 ml"],
         ["Number of bones (adult)", "206"],
         ["Number of muscles", "About 600\u2013650"],
         ["Chromosomes", "46 (23 pairs)"],
         ["Normal sleep (adult)", "7\u20138 hours"]],
        weights=[4.0, 4.6])

    # ------------------------------------------------------------------
    b.h2("Chapter Recap \u2014 One-Line Revision")
    b.bullets([
        "Cell \u2192 tissue \u2192 organ \u2192 system \u2192 organism; "
        "4 tissue types; connective tissue is the most abundant.",
        "**206 bones** = axial 80 + appendicular 126; 27 in a hand, 26 in a "
        "foot; **femur** largest, **stapes** smallest, **clavicle** most often "
        "fractured.",
        "Vertebrae **7-12-5-5-4**; ribs **12 pairs** (7 true, 3 false, 2 "
        "floating).",
        "Heart has 4 chambers and 4 valves; **left ventricle** is thickest; "
        "pacemaker = **SA node**; pulmonary artery carries deoxygenated blood.",
        "Blood = plasma 55 % + cells 45 %; RBC lifespan **120 days**; "
        "**O\u2212 universal donor**, **AB+ universal recipient**.",
        "Right lung **3 lobes**, left **2**; inhaled foreign bodies go to the "
        "**right** lung; expired air has **16 % O\u2082** and **4 % CO\u2082**.",
        "Vital centres (breathing, heart, BP) are in the **medulla oblongata**; "
        "balance in the **cerebellum**; thermostat in the **hypothalamus**.",
        "**12 cranial nerves, 31 pairs of spinal nerves**; vagus is the longest, "
        "trigeminal the largest.",
        "**Liver** is the largest gland; **thyroid** the largest endocrine "
        "gland; **pituitary** the master gland; **skin** the largest organ.",
        "Adrenaline explains every sign of shock \u2014 pale, cold, clammy skin "
        "with a rapid weak pulse and dilated pupils.",
    ])
