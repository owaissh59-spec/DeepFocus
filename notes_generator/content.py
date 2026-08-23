# -*- coding: utf-8 -*-
"""
Full academic content for:
Formulation Development of Pharmaceutical and Cosmetic Products (MPH204T)
M-Pharmacy (Pharmaceutics) - Semester II

Expanded, exam-oriented notes with diagrams, worked examples, tables,
highlighted boxes and MCQs.
"""


def build(n):
    syllabus(n)
    unit1(n)
    unit2(n)
    unit3(n)
    unit4(n)
    unit5(n)
    extra(n)
    important_questions(n)
    mcq_bank(n)
    glossary(n)
    revision(n)


# =====================================================================
#  SYLLABUS
# =====================================================================
def syllabus(n):
    n.h2("Syllabus")

    n.h3("Scope")
    n.para("This course is designed to impart knowledge and skills necessary to train the "
           "students on par with the routine of industrial activities in R&D and F&D "
           "(Formulation & Development). It bridges the gap between theoretical pharmaceutics "
           "and the practical activities carried out in a pharmaceutical industry during the "
           "development of a new dosage form.")

    n.h3("Objectives")
    n.para("On completion of this course it is expected that students will be able to understand :")
    n.bullets([
        "The scheduled activities in a pharmaceutical firm.",
        "The pre-formulation studies of pilot batches of the pharmaceutical industry.",
        "The significance of dissolution and product stability.",
    ])

    n.h3("Course Contents (Theory \u2013 60 Hrs)")
    n.table(
        ["Unit", "Topic", "Hrs"],
        [
            ["I", "Preformulation Studies \u2013 molecular optimization of APIs, crystal morphology and variations, powder flow, structure modification, drug-excipient compatibility studies, method of determination.", "12"],
            ["II", "Formulation Additives \u2013 study of different formulation additives, factors influencing their incorporation, formulation development and processing, new developments in excipient science, Design of Experiments (factorial design).", "12"],
            ["III", "Solubility & Dissolution \u2013 importance, experimental determination, phase-solubility analysis, pH-solubility profile, techniques to improve solubility, theories & mechanisms of dissolution, apparatus, IVIVC and levels of correlation.", "12"],
            ["IV", "Product Stability \u2013 degradation kinetics, mechanisms, stability testing, factors influencing (media & pH effects), accelerated stability studies, shelf-life assignment, protocols, reports and ICH guidelines.", "12"],
            ["V", "Cosmetics \u2013 formulation, evaluation and packaging of dentifrices, nail polish, lipsticks, mascara, baby care products, moisturizing / vanishing / cold creams, shampoo, soaps and syndet bars.", "12"],
        ],
        widths=[0.6, 5.3, 0.6],
        fontsize=10.5,
    )
    n.box("How to use these notes", [
        "Each unit contains detailed theory, diagrams, worked examples, summary tables and MCQs.",
        "\u2605 boxes highlight high-yield points frequently asked in GPAT / NIPER / university exams.",
        "A consolidated Quick-Revision section is given at the end.",
    ], kind="NOTE")
    n.page_break()



# =====================================================================
#  UNIT I - PREFORMULATION STUDIES
# =====================================================================
def unit1(n):
    n.unit_title("Unit I \u2013 Preformulation Studies")

    n.h2("1.1 Introduction")
    n.para("Before a drug substance can be formulated into an acceptable dosage form, the "
           "formulator must know its fundamental physical and chemical properties. "
           "Preformulation is the branch of pharmaceutics that deals with the investigation of "
           "these properties of a drug substance, alone and when combined with excipients. It is "
           "the first step in the rational development of a dosage form.")
    n.para(segments=[
        ("Definition : ", True),
        ("Preformulation may be defined as a phase of development during which the physical and "
         "chemical properties of a drug substance are characterised, alone and in combination "
         "with excipients, in order to develop a stable, safe, effective, elegant and "
         "bioavailable dosage form that can be mass-produced.", )])
    n.para("Preformulation testing begins once a new compound shows sufficient pharmacological "
           "promise. The data generated guide the formulator in the selection of the salt/form "
           "of the drug, the choice of excipients, the manufacturing process and the packaging, "
           "and help anticipate problems that may occur during formulation, storage and use.")

    n.h3("Need / Importance of Preformulation")
    n.bullets([
        "Establishes the physicochemical characteristics of a new drug substance.",
        "Determines the kinetic rate profile (chemical stability).",
        "Establishes the compatibility of the drug with common excipients.",
        "Helps to select the most suitable salt/polymorphic form of the drug.",
        "Prevents costly re-formulation by anticipating problems early.",
        "Provides a scientific rationale for formulation and process design.",
    ])

    n.h3("Objectives / Goals of Preformulation")
    n.numbered([
        "To establish the physicochemical parameters of a new drug substance.",
        "To determine its kinetic rate profile and stability.",
        "To establish its compatibility with common excipients.",
        "To characterise the bulk drug so that manufacturing problems are anticipated.",
        "To generate data useful for the development of a stable and bioavailable dosage form.",
    ])
    n.figure("preform_flow.png", "General work-flow of preformulation studies", width=3.4)

    # ------------------------------------------------ molecular optimization
    n.h2("1.2 Molecular Optimization of APIs (Drug Substances)")
    n.para("Molecular optimization is the systematic modification and evaluation of a lead "
           "molecule so as to obtain the best possible balance of pharmacological potency, "
           "selectivity, solubility, permeability, chemical stability and manufacturability in "
           "the final active pharmaceutical ingredient (API). During drug discovery a promising "
           "'lead' is optimized so that the final candidate not only shows the desired activity "
           "but also possesses acceptable biopharmaceutical and physicochemical properties for "
           "formulation into a dosage form.")

    n.h3("Key Molecular Properties Optimized")
    n.bullets([
        ("Aqueous solubility \u2013", "adequate solubility is essential for dissolution and oral absorption; poorly soluble candidates are optimized by salt selection, prodrugs, particle-size reduction or structural changes."),
        ("Lipophilicity (log P / log D) \u2013", "governs membrane permeability and partitioning; an optimum (moderate) value is desired \u2013 too low limits permeation, too high limits solubility and may increase toxicity."),
        ("Ionization (pKa) \u2013", "influences solubility, dissolution, absorption and choice of formulation pH; used for salt selection."),
        ("Permeability \u2013", "the ability to cross biological membranes; related to lipophilicity, molecular size and hydrogen-bonding capacity."),
        ("Chemical & metabolic stability \u2013", "resistance to hydrolysis, oxidation and first-pass metabolism."),
        ("Molecular size & H-bonding \u2013", "governed by Lipinski's Rule of Five for good oral absorption."),
    ])

    n.h3("Lipinski's Rule of Five")
    n.para("Poor oral absorption or permeation is more likely when a molecule violates more than "
           "one of the following criteria (all cut-off values are multiples of five, hence the "
           "name) :")
    n.bullets([
        "Molecular weight not more than 500 Da.",
        "Calculated log P (cLogP) not more than 5.",
        "Number of hydrogen-bond donors (sum of OH and NH groups) not more than 5.",
        "Number of hydrogen-bond acceptors (sum of N and O atoms) not more than 10.",
    ], level=1)
    n.box("High-Yield", [
        "Lipinski's Rule of Five predicts oral bioavailability; MW \u2264 500, logP \u2264 5, HBD \u2264 5, HBA \u2264 10.",
        "It is a guideline for orally administered drugs; it does not apply to actively transported drugs, or to injectable / natural products.",
    ])

    n.h3("Approaches to Molecular Optimization")
    n.bullets([
        ("Structural modification \u2013", "changing functional groups to alter solubility, potency or stability."),
        ("Salt formation \u2013", "for ionizable drugs to modify solubility and stability."),
        ("Prodrug design \u2013", "temporary chemical modification reversed in-vivo."),
        ("Selection of physical form \u2013", "choosing a suitable polymorph, hydrate or amorphous form."),
    ])

    # ------------------------------------------------ physicochemical params
    n.h2("1.3 Physicochemical Parameters")

    n.h3("(a) Organoleptic Properties")
    n.para("The colour, odour and taste of the drug are recorded using descriptive terminology, "
           "since these properties influence patient acceptability. An unpleasant taste may "
           "require flavouring, sweetening, coating or the use of an insoluble salt/prodrug; an "
           "objectionable colour variation may need a colourant to standardise appearance.")
    n.table(
        ["Property", "Descriptive terms used"],
        [
            ["Colour", "Off-white, cream, yellow, tan, buff, etc."],
            ["Odour", "Odourless, pungent, aromatic, sulphurous."],
            ["Taste", "Tasteless, bitter, sweet, acidic, metallic."],
        ],
        widths=[1.7, 4.8],
    )

    n.h3("(b) Purity and Bulk Characterisation")
    n.para("The identity and purity of the bulk drug are confirmed using melting point, "
           "spectroscopic techniques (UV, IR, NMR, Mass) and chromatography (HPLC, TLC, GC). "
           "Determination of purity and detection of related substances / impurities is "
           "essential, as impurities may affect stability, safety and the assay of the drug. "
           "The moisture content is determined (usually by the Karl Fischer method) and the "
           "hygroscopicity of the powder is classified, since adsorbed moisture affects flow, "
           "stability and compaction.")

    n.h3("(c) Particle Size, Shape and Surface Area")
    n.para("Particle size affects solubility (of very fine particles), dissolution rate, "
           "content uniformity of low-dose drugs, flow, sedimentation of suspensions and "
           "absorption. It is measured by sieving, optical/electron microscopy, laser "
           "diffraction, the Coulter counter and sedimentation methods. A reduction in particle "
           "size increases the effective surface area and hence the dissolution rate "
           "(as predicted by the Noyes-Whitney equation).")

    # ------------------------------------------------ solubility
    n.h2("1.4 Solubility Analysis")
    n.para("Solubility is one of the most important preformulation parameters because a drug "
           "must be in solution before it can be absorbed. It is defined as the maximum amount "
           "of solute that dissolves in a given quantity of solvent at a specified temperature "
           "and pressure to form a saturated solution.")

    n.h3("Descriptive Solubility Terms (Pharmacopoeial)")
    n.table(
        ["Descriptive term", "Parts of solvent per 1 part of solute"],
        [
            ["Very soluble", "Less than 1"],
            ["Freely soluble", "1 to 10"],
            ["Soluble", "10 to 30"],
            ["Sparingly soluble", "30 to 100"],
            ["Slightly soluble", "100 to 1000"],
            ["Very slightly soluble", "1000 to 10,000"],
            ["Practically insoluble / insoluble", "More than 10,000"],
        ],
        widths=[2.9, 3.6],
    )

    n.h3("Important Solubility Concepts")
    n.bullets([
        ("Intrinsic solubility (C0) \u2013", "the solubility of the completely unionized form of the drug, determined at a pH where it is fully unionized."),
        ("Common-ion effect \u2013", "the solubility of a slightly soluble salt is reduced by the addition of a common ion (e.g. the hydrochloride salt of a base is less soluble in gastric HCl)."),
        ("Effect of temperature \u2013", "for most drugs (endothermic dissolution) solubility increases with temperature; for a few (exothermic) it decreases."),
        ("Effect of pH \u2013", "for ionizable drugs, solubility changes markedly with pH (see pH-solubility profile)."),
    ])

    n.h3("Dissociation Constant (pKa) and the Henderson-Hasselbalch Equation")
    n.para("The dissociation constant (pKa) is the pH at which a drug exists as 50% ionized and "
           "50% unionized species. The degree of ionization at any pH is given by the "
           "Henderson-Hasselbalch equations :")
    n.formula("For weak acids :  pH = pKa + log ( [ionized] / [unionized] )")
    n.formula("For weak bases :  pH = pKa + log ( [unionized] / [ionized] )")
    n.para("The ionized form is more water-soluble, while the unionized form is more lipophilic "
           "and better absorbed across membranes. Thus the pKa, together with the pH of the "
           "biological environment, governs both solubility and absorption. The pKa is "
           "determined by potentiometric titration or spectrophotometry.")

    n.h3("pH-Solubility Profile")
    n.para("For an ionizable drug, the total solubility is the sum of the intrinsic solubility "
           "of the unionized form and the (much higher) solubility of the ionized form. A "
           "pH-solubility profile plots total solubility against pH over the physiological range "
           "(1\u20138). Weak acids become more soluble as the pH rises above their pKa, while weak "
           "bases become more soluble as the pH falls below their pKa. The profile guides salt "
           "selection, formulation pH and prediction of absorption at different sites of the GI "
           "tract.")
    n.figure("ph_solubility.png", "pH-solubility profiles of a weak acid and a weak base", width=4.6)

    n.h3("Partition Coefficient (P) / log P")
    n.para("The partition coefficient is the ratio of the concentration of the unionized drug "
           "distributed between an organic phase (usually n-octanol) and an aqueous phase at "
           "equilibrium :")
    n.formula("P = C (octanol) / C (water)")
    n.para("It is a measure of lipophilicity and correlates with membrane permeability and "
           "biological activity. Log P is commonly reported. The distribution coefficient "
           "(log D) is the corresponding value at a defined pH that accounts for ionization and "
           "is more relevant for ionizable drugs at physiological pH. A moderate log P "
           "(approximately 1\u20133) usually gives the best balance of solubility and permeability.")

    n.h3("Biopharmaceutics Classification System (BCS)")
    n.para("The BCS classifies drug substances into four classes on the basis of their aqueous "
           "solubility and intestinal permeability. It is a powerful preformulation and "
           "regulatory tool that predicts whether dissolution or permeability will limit "
           "absorption, and is used to justify biowaivers.")
    n.figure("bcs.png", "The Biopharmaceutics Classification System (BCS)", width=4.6)
    n.table(
        ["Class", "Solubility", "Permeability", "Rate-limiting step / example"],
        [
            ["I", "High", "High", "Rapidly absorbed (e.g. paracetamol, metoprolol)."],
            ["II", "Low", "High", "Dissolution-limited (e.g. ibuprofen, ketoconazole)."],
            ["III", "High", "Low", "Permeability-limited (e.g. atenolol, ranitidine)."],
            ["IV", "Low", "Low", "Poorly absorbed (e.g. furosemide, hydrochlorothiazide)."],
        ],
        widths=[0.7, 1.2, 1.3, 3.3],
        fontsize=10.5,
    )
    n.box("High-Yield", [
        "BCS Class II drugs benefit most from solubility / dissolution enhancement techniques.",
        "Class I (and some Class III) drugs are candidates for biowaivers.",
    ])



    # ------------------------------------------------ crystal properties
    n.h2("1.5 Crystal Morphology and Variations")
    n.para("The solid state of a drug can exist in different physical forms which strongly "
           "influence solubility, dissolution rate, stability, flow and compressibility, and "
           "hence bioavailability and manufacturability. The study of these forms is a critical "
           "part of preformulation.")

    n.h3("Crystalline vs Amorphous Solids")
    n.para("In a crystalline solid the constituent molecules are arranged in a regular, "
           "repeating three-dimensional lattice with long-range order; such solids have a sharp "
           "melting point. In an amorphous solid there is no long-range order; such solids have "
           "higher internal energy, greater solubility and faster dissolution, but are "
           "thermodynamically unstable and tend to recrystallise on storage.")

    n.h3("Crystal Habit")
    n.para("Crystal habit is the external shape or appearance of a crystal, whereas the internal "
           "lattice may remain the same. The same compound can crystallise into different habits "
           "depending on the crystallisation conditions (solvent, temperature, rate of cooling, "
           "impurities). Habit affects flow, packing, compaction and even the tendency to cap or "
           "laminate during tableting.")
    n.figure("crystal_habit.png", "Common crystal habits", width=5.6)
    n.table(
        ["Crystal habit", "Description"],
        [
            ["Tabular", "Moderately expanded in two directions (flat plates)."],
            ["Platy / Flaky", "Flat, thin plate-like crystals."],
            ["Prismatic", "Column-like, elongated crystals."],
            ["Acicular", "Needle-like, slender crystals (poor flow, may cap)."],
            ["Bladed", "Flattened, blade-like elongated crystals."],
            ["Equant / Isometric", "Similar dimensions in all directions (good flow)."],
        ],
        widths=[2.1, 4.4],
    )

    n.h3("Polymorphism")
    n.para("Polymorphism is the ability of a substance to exist in more than one crystalline "
           "form having the same chemical composition but a different internal lattice "
           "arrangement. Different polymorphs differ in melting point, density, hardness, "
           "solubility, dissolution rate and stability. Polymorphism is important because a "
           "change in form on storage can alter dissolution and bioavailability, and can even "
           "cause product failure.")
    n.h3("Types of Polymorphs")
    n.bullets([
        ("Enantiotropic \u2013", "one form can be reversibly converted into another by changing temperature or pressure; a definite transition temperature exists below the melting point (e.g. sulphur, carbamazepine)."),
        ("Monotropic \u2013", "one form is unstable at all temperatures below the melting point and the transformation to the stable form is irreversible (e.g. glyceryl stearate)."),
    ])
    n.para(segments=[
        ("Stable vs metastable forms : ", True),
        ("The thermodynamically stable polymorph has the lowest energy, highest melting point "
         "and lowest solubility. A metastable polymorph has higher energy, higher solubility "
         "and faster dissolution, and is often preferred to improve bioavailability \u2013 but it "
         "may convert to the stable, less soluble form on storage, causing problems. "
         "Classic examples : chloramphenicol palmitate (form B is active, form A is poorly "
         "absorbed), and the withdrawal of ritonavir capsules when a new, less soluble "
         "polymorph appeared.", )])

    n.h3("Pseudopolymorphism (Solvates and Hydrates)")
    n.para("When solvent molecules are incorporated into the crystal lattice in a stoichiometric "
           "ratio, the crystals are called solvates (or hydrates when the solvent is water); "
           "this phenomenon is termed pseudopolymorphism. Anhydrous forms generally show higher "
           "aqueous solubility and faster dissolution than their hydrated counterparts. A "
           "classic example is ampicillin \u2013 the anhydrous form dissolves faster and gives higher "
           "blood levels than the trihydrate.")

    n.h3("Methods of Characterising Solid Forms")
    n.figure("dsc.png", "Schematic DSC thermogram showing melting endotherm", width=4.4)
    n.table(
        ["Method", "Property determined"],
        [
            ["X-ray powder diffraction (XRPD)", "Definitive identification of crystalline forms; degree of crystallinity. (Gold standard.)"],
            ["Differential Scanning Calorimetry (DSC)", "Melting point, polymorphic transitions, heat of fusion, purity."],
            ["Thermogravimetric Analysis (TGA)", "Weight loss due to water/solvent \u2013 detects hydrates/solvates."],
            ["Hot-stage microscopy", "Visual observation of melting and phase transitions."],
            ["IR / Raman spectroscopy", "Differences in bonding between polymorphs."],
            ["Solid-state NMR", "Molecular environment in different solid forms."],
            ["SEM / microscopy", "Crystal habit, surface morphology, particle size."],
        ],
        widths=[2.9, 3.6],
        fontsize=10.5,
    )
    n.box("High-Yield", [
        "XRPD is the definitive (gold-standard) technique for identifying polymorphs.",
        "Metastable / amorphous forms = higher solubility & dissolution but lower stability.",
        "Anhydrous forms usually dissolve faster than hydrates (e.g. ampicillin).",
    ])

    # ------------------------------------------------ powder flow
    n.h2("1.6 Powder Flow Properties")
    n.para("Good powder flow is essential for accurate die/capsule filling, uniformity of dose "
           "and reproducible manufacturing. Poor flow causes weight variation and content "
           "non-uniformity. Flow depends on particle size, shape, density, surface texture, "
           "moisture and interparticulate (cohesive/adhesive) forces.")

    n.h3("(a) Bulk Density and Tapped Density")
    n.para("Bulk density is the mass of powder divided by its bulk (untapped) volume; tapped "
           "density is measured after mechanically tapping a graduated cylinder until no further "
           "change in volume occurs. These are used to derive compressibility indices.")

    n.h3("(b) Carr's Compressibility Index and Hausner Ratio")
    n.formula("Carr's Index (%) = [(Tapped density \u2212 Bulk density) / Tapped density] \u00d7 100")
    n.formula("Hausner Ratio = Tapped density / Bulk density")
    n.para("Lower values indicate better flow. They are widely used indirect measures of "
           "flowability :")
    n.table(
        ["Carr's Index (%)", "Hausner Ratio", "Flow character"],
        [
            ["\u2264 10", "1.00 \u2013 1.11", "Excellent"],
            ["11 \u2013 15", "1.12 \u2013 1.18", "Good"],
            ["16 \u2013 20", "1.19 \u2013 1.25", "Fair"],
            ["21 \u2013 25", "1.26 \u2013 1.34", "Passable"],
            ["26 \u2013 31", "1.35 \u2013 1.45", "Poor"],
            ["32 \u2013 37", "1.46 \u2013 1.59", "Very poor"],
            ["> 38", "> 1.60", "Very, very poor"],
        ],
        widths=[2.0, 2.0, 2.5],
    )

    n.h3("(c) Angle of Repose")
    n.para("The angle of repose is the maximum angle between the surface of a powder heap and "
           "the horizontal plane. It is an indirect measure of interparticulate friction; lower "
           "angles indicate better flow.")
    n.figure("angle_repose.png", "Measurement of the angle of repose", width=3.6)
    n.table(
        ["Angle of repose (\u00b0)", "Flow property"],
        [
            ["25 \u2013 30", "Excellent"],
            ["31 \u2013 35", "Good"],
            ["36 \u2013 40", "Fair (aid not needed)"],
            ["41 \u2013 45", "Passable (may hang up)"],
            ["46 \u2013 55", "Poor (agitation needed)"],
            ["> 56", "Very poor"],
        ],
        widths=[2.6, 3.9],
    )

    n.h3("Methods to Improve Powder Flow")
    n.bullets([
        "Increasing particle size by granulation (wet or dry).",
        "Producing spherical particles by spray drying or spheronization.",
        "Adding glidants such as colloidal silicon dioxide or talc.",
        "Reducing moisture content to avoid liquid bridges.",
        "Adding lubricants such as magnesium stearate to reduce interparticulate friction.",
    ])

    # ------------------------------------------------ structure modification
    n.h2("1.7 Structure Modification")
    n.para("When a drug candidate shows unfavourable properties (poor solubility, instability, "
           "unpleasant taste or poor absorption), its molecular structure or physical form can "
           "be deliberately modified to improve these properties without altering the intended "
           "pharmacological action.")

    n.h3("(a) Salt Formation")
    n.para("Converting an acidic or basic drug into a salt is the most common way to improve "
           "aqueous solubility, dissolution and stability, and to improve crystallinity, flow "
           "and hygroscopicity. Salt selection considers solubility, stability, hygroscopicity, "
           "toxicity of the counter-ion and manufacturability.")
    n.table(
        ["Drug type", "Common salt-forming agents (counter-ions)"],
        [
            ["Acidic drugs", "Sodium, potassium, calcium, meglumine, ethanolamine."],
            ["Basic drugs", "Hydrochloride, sulphate, phosphate, maleate, tartrate, mesylate."],
        ],
        widths=[1.8, 4.7],
    )

    n.h3("(b) Prodrug Approach")
    n.para("A prodrug is a pharmacologically inactive derivative that is converted into the "
           "active drug in the body by enzymatic or chemical reaction. Prodrugs are used to "
           "improve solubility, permeability, stability and taste, and to achieve site-specific "
           "delivery. Examples : enalapril (\u2192 enalaprilat), chloramphenicol palmitate "
           "(taste masking), and dipivefrine (\u2192 adrenaline).")

    n.h3("(c) Complexation")
    n.para("Formation of inclusion complexes (e.g. with cyclodextrins) can increase apparent "
           "solubility, improve stability, mask taste and reduce local irritation.")

    n.h3("(d) Change of Physical Form")
    n.para("Selecting a more soluble polymorph, an amorphous form, an anhydrate, or reducing "
           "particle size (micronization / nanonization) modifies the effective properties of "
           "the same chemical entity.")

    # ------------------------------------------------ compatibility
    n.h2("1.8 Drug\u2013Excipient Compatibility Studies")
    n.para("Excipients are added to a formulation for various functions, but they may interact "
           "physically or chemically with the drug, leading to loss of potency, change in "
           "appearance or reduced bioavailability. Compatibility studies identify such "
           "interactions early so that incompatible excipients are avoided and a stable "
           "formulation is designed.")

    n.h3("Purpose")
    n.bullets([
        "To select excipients that are physically and chemically compatible with the drug.",
        "To detect potential interactions before large-scale formulation.",
        "To predict the stability of the final product and guide storage conditions.",
    ])

    n.h3("Methods of Determination")
    n.table(
        ["Method", "Principle / use"],
        [
            ["Differential Scanning Calorimetry (DSC)", "A 1:1 drug-excipient mixture is scanned; appearance, disappearance or shift of thermal peaks indicates interaction. Rapid screening tool."],
            ["Isothermal Stress Testing (IST)", "Drug-excipient blends stored under stress (e.g. 50\u201360\u00b0C, 75% RH) and analysed by HPLC / TLC for degradation."],
            ["Thin-Layer Chromatography (TLC)", "Appearance of new spots indicates formation of degradation products."],
            ["HPLC", "Quantifies drug and degradation products in stressed blends \u2013 most reliable and stability-indicating."],
            ["FT-IR / Raman", "Shift or disappearance of characteristic functional-group bands indicates chemical interaction."],
            ["Visual / microscopic", "Change in colour, caking, liquefaction, odour on storage."],
        ],
        widths=[2.4, 4.1],
        fontsize=10.5,
    )

    n.h3("Common Drug\u2013Excipient Interactions")
    n.bullets([
        ("Maillard reaction \u2013", "browning between amine drugs and reducing sugars such as lactose."),
        ("Acid\u2013base reactions \u2013", "between acidic and basic components."),
        ("Adsorption \u2013", "of the drug onto excipients, reducing availability."),
        ("Eutectic / liquefaction \u2013", "lowering of melting point causing sticking (e.g. with PEG)."),
        ("Oxidation, hydrolysis and complexation \u2013", "reducing potency."),
    ])

    n.h2("1.9 Method of Determination (Analytical Method Development)")
    n.para("A stability-indicating analytical method must be developed and validated during "
           "preformulation to accurately quantify the drug and its degradation products in the "
           "presence of excipients. UV-Visible spectrophotometry is used for assay and "
           "solubility studies, while HPLC is used for assay, purity and stability studies. The "
           "method is validated for accuracy, precision, specificity, linearity, limit of "
           "detection (LOD), limit of quantitation (LOQ), range and robustness before use.")

    deep1(n)

    n.box("Summary \u2013 Unit I", [
        "Preformulation characterises the drug before formulation to design a stable, bioavailable product.",
        "Solubility, pKa, log P and BCS class govern absorption.",
        "Polymorphism, pseudopolymorphism and amorphous forms affect solubility, stability & bioavailability; XRPD is definitive.",
        "Powder flow is judged by Carr's index, Hausner ratio and angle of repose.",
        "Drug-excipient compatibility is screened mainly by DSC, IST and HPLC / TLC.",
    ])

    # ------------------------------------------------ MCQs
    n.mcq_header("Unit I \u2013 Multiple Choice Questions")
    n.mcq("Preformulation study is carried out :",
          ["After formulation", "Before formulation of the dosage form",
           "During packaging", "After marketing"], 1,
          "Preformulation is the first learning step, done before actual formulation.")
    n.mcq("Which of the following is the definitive technique for identifying polymorphs ?",
          ["UV spectroscopy", "X-ray powder diffraction", "Titration", "Refractometry"], 1)
    n.mcq("According to Lipinski's Rule of Five, molecular weight should not exceed :",
          ["250 Da", "500 Da", "750 Da", "1000 Da"], 1)
    n.mcq("The partition coefficient (log P) is usually determined using which solvent system ?",
          ["Chloroform-water", "n-Octanol-water", "Ether-water", "Benzene-water"], 1,
          "n-Octanol mimics biological membranes.")
    n.mcq("A metastable polymorph, compared with the stable form, has :",
          ["Lower solubility", "Higher melting point",
           "Higher solubility and faster dissolution", "No difference"], 2)
    n.mcq("Carr's compressibility index of 12% indicates flow that is :",
          ["Excellent", "Good", "Poor", "Very poor"], 1)
    n.mcq("The Henderson-Hasselbalch equation relates :",
          ["Temperature and solubility", "pH, pKa and degree of ionization",
           "Pressure and volume", "Surface area and dissolution"], 1)
    n.mcq("Which BCS class is dissolution rate-limited and benefits most from solubility "
          "enhancement ?",
          ["Class I", "Class II", "Class III", "Class IV"], 1)
    n.mcq("Incorporation of solvent molecules into the crystal lattice in stoichiometric "
          "proportion is called :",
          ["Polymorphism", "Pseudopolymorphism (solvate/hydrate)", "Isomerism", "Eutexia"], 1)
    n.mcq("Angle of repose of 28\u00b0 indicates :",
          ["Excellent flow", "Poor flow", "No flow", "Very poor flow"], 0)
    n.mcq("Browning interaction between an amine drug and lactose is due to :",
          ["Oxidation", "Maillard reaction", "Photolysis", "Racemization"], 1)
    n.mcq("Which is NOT a goal of preformulation ?",
          ["Establishing physicochemical properties", "Determining stability profile",
           "Marketing the product", "Studying drug-excipient compatibility"], 2)
    n.page_break()



# =====================================================================
#  UNIT II - FORMULATION ADDITIVES
# =====================================================================
def unit2(n):
    n.unit_title("Unit II \u2013 Formulation Additives")

    n.h2("2.1 Introduction")
    n.para("Formulation additives (excipients) are substances other than the active "
           "pharmaceutical ingredient that are deliberately included in a dosage form. Although "
           "once regarded as inert 'fillers', excipients are now known to influence the rate and "
           "extent of drug absorption, the physical and chemical stability of the product, its "
           "manufacturability and patient acceptability. Their rational selection is therefore "
           "central to formulation development.")
    n.para(segments=[("Definition : ", True),
        ("An excipient is any component, other than the active substance, that has been "
         "appropriately evaluated for safety and is intentionally included in a drug delivery "
         "system to aid processing, to protect, support or enhance stability, bioavailability or "
         "patient acceptability, or to assist in product identification.", )])

    n.h3("Ideal Properties of an Excipient")
    n.bullets([
        "Physiologically inert, non-toxic and non-irritant.",
        "Physically and chemically stable and compatible with the drug and other excipients.",
        "Free from objectionable microbial load; acceptable to regulatory authorities.",
        "Should not interfere with the bioavailability or the assay of the drug.",
        "Commercially available, economical and of consistent quality.",
        "Should not have an unacceptable taste, odour or colour.",
        "Should have good functional (flow, compaction, solubility) properties.",
    ])

    n.h2("2.2 Study of Different Formulation Additives")
    n.para("Excipients are classified according to the function they perform in the dosage form. "
           "The major categories, their functions and representative examples are summarised "
           "below.")
    n.table(
        ["Additive (function)", "Role", "Examples"],
        [
            ["Diluents / Fillers", "Add bulk to make a practical tablet/capsule size.",
             "Lactose, microcrystalline cellulose (MCC), dibasic calcium phosphate, mannitol, starch."],
            ["Binders / Adhesives", "Impart cohesiveness so granules/tablets hold together.",
             "PVP (povidone), starch paste, HPMC, gelatin, acacia."],
            ["Disintegrants", "Promote break-up of the tablet in GI fluid.",
             "Starch, sodium starch glycolate, croscarmellose sodium, crospovidone."],
            ["Lubricants", "Reduce friction between granules and die wall; aid ejection.",
             "Magnesium stearate, stearic acid, sodium stearyl fumarate."],
            ["Glidants", "Improve flow of powder/granules.",
             "Colloidal silicon dioxide (Aerosil), talc."],
            ["Anti-adherents", "Prevent sticking to punches/dies.",
             "Talc, magnesium stearate, cornstarch."],
            ["Coating agents", "Protect, mask taste, control release, improve appearance.",
             "HPMC, ethylcellulose, Eudragit polymers, sugar, shellac."],
            ["Colourants", "Improve appearance, aid identification.",
             "Approved dyes and lakes, iron oxides, titanium dioxide."],
            ["Sweeteners / Flavours", "Improve palatability of oral products.",
             "Sucrose, aspartame, saccharin, sorbitol; flavour oils."],
            ["Preservatives", "Prevent microbial growth in multi-dose products.",
             "Parabens, benzoic acid, benzalkonium chloride, sodium benzoate."],
            ["Antioxidants", "Prevent oxidative degradation.",
             "BHA, BHT, ascorbic acid, sodium metabisulphite, tocopherol."],
            ["Surfactants / Wetting agents", "Reduce surface tension, aid wetting/solubilization.",
             "SLS, polysorbates (Tween), sorbitan esters (Span)."],
            ["Suspending / Viscosity agents", "Retard sedimentation; thicken.",
             "Sodium CMC, MC, xanthan gum, acacia, carbopol."],
            ["Emulsifying agents", "Stabilise emulsions.",
             "Acacia, tween/span blends, lecithin, cetyl alcohol."],
            ["Buffers", "Maintain and control pH.",
             "Citrate, phosphate, acetate buffers."],
            ["Chelating agents", "Complex trace metals that catalyse oxidation.",
             "EDTA and its salts, citric acid."],
            ["Tonicity agents", "Adjust osmotic pressure of parenterals/ophthalmics.",
             "Sodium chloride, dextrose, mannitol."],
            ["Solvents / Vehicles", "Dissolve or disperse the drug.",
             "Water, ethanol, glycerin, propylene glycol, PEG, fixed oils."],
        ],
        widths=[1.7, 2.2, 2.6],
        fontsize=10,
    )
    n.box("High-Yield", [
        "Superdisintegrants (croscarmellose, crospovidone, sodium starch glycolate) act in very low % (2\u20138%).",
        "Magnesium stearate is a hydrophobic lubricant \u2013 over-mixing retards dissolution.",
        "EDTA is a chelating agent used to prevent metal-catalysed oxidation.",
    ])

    n.h2("2.3 Factors Influencing Incorporation of Additives")
    n.para("The choice and quantity of an excipient are governed by several factors :")
    n.bullets([
        ("Nature of the drug \u2013", "solubility, dose, stability, particle size, hygroscopicity and compatibility."),
        ("Route & dosage form \u2013", "oral, parenteral and topical products have different requirements (e.g. sterility and tonicity for parenterals)."),
        ("Function required \u2013", "the specific role determines the class of additive selected."),
        ("Compatibility \u2013", "the additive must not interact with the drug or other excipients."),
        ("Regulatory acceptability \u2013", "must be approved / pharmacopoeial with acceptable safety limits."),
        ("Physicochemical properties of additive \u2013", "flow, compressibility, particle size, moisture content."),
        ("Manufacturing process \u2013", "wet granulation, dry granulation or direct compression demand different excipient properties."),
        ("Cost and availability \u2013", "economical and consistently available material."),
        ("Organoleptic considerations \u2013", "taste, odour and colour affecting compliance."),
    ])

    n.h2("2.4 Formulation Development and Processing")
    n.para("Formulation development is the systematic process of converting a drug substance "
           "into a suitable, stable and bioavailable dosage form. It integrates preformulation "
           "data, selection of excipients, choice of manufacturing process and optimization of "
           "the formula and process.")
    n.h3("General Stages of Formulation Development")
    n.numbered([
        "Review of preformulation data (solubility, stability, flow, compatibility).",
        "Definition of the target product profile and selection of the dosage form.",
        "Selection of excipients and their concentrations.",
        "Selection of the manufacturing process (wet/dry granulation, direct compression).",
        "Preparation and evaluation of laboratory (trial) batches.",
        "Optimization of formula and process using Design of Experiments.",
        "Scale-up from laboratory to pilot to production scale.",
        "Stability studies and finalisation of the formulation and packaging.",
    ])
    n.h3("Common Processing Techniques for Solid Dosage Forms")
    n.table(
        ["Technique", "Principle", "Suitable for"],
        [
            ["Wet granulation", "Granulate powder with a binder liquid, dry and size.", "Low-dose, poorly flowing, moisture/heat-stable drugs."],
            ["Dry granulation", "Slugging or roller compaction without liquid.", "Moisture- or heat-sensitive drugs."],
            ["Direct compression", "Blend and compress directly.", "Free-flowing, compressible drugs; economical."],
        ],
        widths=[1.6, 2.6, 2.3],
        fontsize=10.5,
    )

    n.h2("2.5 New Developments in Excipient Science")
    n.para("To meet the demands of modern high-speed manufacturing (especially direct "
           "compression) and novel drug-delivery systems, new and improved excipients have been "
           "developed :")
    n.bullets([
        ("Co-processed excipients \u2013", "two or more excipients combined at the sub-particle level to give a single multifunctional material with improved flow and compressibility (e.g. Ludipress, Cellactose, Prosolv (silicified MCC), StarLac, MicroceLac)."),
        ("Superdisintegrants \u2013", "highly efficient disintegrants used in low concentration for rapid disintegration \u2013 sodium starch glycolate, croscarmellose sodium, crospovidone; essential for orally disintegrating tablets."),
        ("Directly compressible excipients \u2013", "spray-dried lactose, MCC, dibasic calcium phosphate with good flow and binding."),
        ("Multifunctional excipients \u2013", "a single material serving several roles (filler-binder-disintegrant)."),
        ("Excipients for modified release \u2013", "methacrylate copolymers (Eudragit), HPMC grades, polyethylene oxide."),
        ("Excipients for solubility enhancement \u2013", "cyclodextrins, poloxamers, novel surfactants, solid-dispersion carriers."),
        ("Nanocarrier and lipid excipients \u2013", "for improving bioavailability of poorly soluble drugs."),
    ])

    n.h2("2.6 Design of Experiments (DoE) \u2013 Factorial Design")
    n.para("Design of Experiments is a structured, statistical approach to planning experiments "
           "so that the effect of several variables (factors) on one or more responses can be "
           "studied simultaneously and efficiently. In formulation and process development, DoE "
           "is used to understand and optimize the relationship between formulation/process "
           "variables and product quality attributes using a minimum number of experiments. It "
           "is a central tool of Quality by Design (QbD).")

    n.h3("Limitation of the Traditional (OFAT) Approach")
    n.para("In the classical 'one-factor-at-a-time' (OFAT) approach, only one variable is "
           "changed at a time while all others are held constant. This requires many "
           "experiments, cannot detect interactions between factors, and may miss the true "
           "optimum. DoE overcomes these drawbacks.")
    n.figure("ofat_vs_factorial.png", "OFAT vs factorial design \u2013 the factorial design covers the design space better", width=5.2)

    n.h3("Key Terminology")
    n.table(
        ["Term", "Meaning"],
        [
            ["Factor", "An independent variable that is deliberately varied (e.g. binder %, compression force)."],
            ["Level", "The value/setting assigned to a factor (e.g. low '\u2212' and high '+')."],
            ["Response", "The measured outcome / dependent variable (e.g. hardness, disintegration time)."],
            ["Effect", "The change in response produced by changing the level of a factor."],
            ["Interaction", "When the effect of one factor depends on the level of another factor."],
            ["Run / Trial", "An individual experiment performed at a defined combination of levels."],
        ],
        widths=[1.4, 5.1],
        fontsize=10.5,
    )

    n.h3("Factorial Design")
    n.para("A factorial design studies the effect of two or more factors, each at two or more "
           "levels, in all possible combinations. A design with 'k' factors each at 2 levels is "
           "called a 2^k factorial design and requires 2^k experimental runs.")
    n.para(segments=[("2\u00b2 Factorial Design (2 factors, 2 levels = 4 runs) : ", True)])
    n.table(
        ["Run", "Factor A", "Factor B", "Combination"],
        [
            ["1", "\u2212 (low)", "\u2212 (low)", "(1)"],
            ["2", "+ (high)", "\u2212 (low)", "a"],
            ["3", "\u2212 (low)", "+ (high)", "b"],
            ["4", "+ (high)", "+ (high)", "ab"],
        ],
        widths=[1.2, 1.9, 1.9, 1.5],
    )
    n.para("A 2\u00b3 factorial design (3 factors at 2 levels) requires 8 runs and allows the study "
           "of three main effects, three two-factor interactions and one three-factor "
           "interaction. The design is conveniently represented by the corners of a cube :")
    n.figure("factorial_cube.png", "2\u00b3 full factorial design represented as a cube (8 runs)", width=3.8)

    n.h3("Fractional Factorial Design")
    n.para("When the number of factors is large, a full factorial requires too many runs. A "
           "fractional factorial design studies only a carefully selected fraction "
           "(e.g. one-half, 2^(k\u22121)) of the runs to screen the most important factors, at the "
           "cost of confounding (aliasing) some higher-order interactions. It is mainly used "
           "for screening.")

    n.h3("Response Surface Methodology & Optimization Designs")
    n.para("For optimization (finding the best combination of factors), higher designs such as "
           "the central composite design and the Box-Behnken design are used together with "
           "response surface methodology (RSM). These fit a mathematical (usually quadratic) "
           "model relating the responses to the factors and generate contour and "
           "response-surface plots that locate the optimum and define the design space.")
    n.figure("response_surface.png", "Response-surface / contour plot used to locate the optimum", width=4.4)

    n.h3("Advantages of the Factorial / DoE Approach")
    n.bullets([
        "Fewer experiments give more information than OFAT.",
        "Estimates the effect of each factor and, importantly, their interactions.",
        "Allows building of a predictive mathematical model.",
        "Enables true optimization and definition of a design space (QbD).",
        "Economical in time, material and cost.",
    ])
    n.h3("Applications in Formulation")
    n.bullets([
        "Optimizing binder and disintegrant levels in tablets.",
        "Studying the effect of process variables (compression force, granulation time) on tablet properties.",
        "Optimizing polymer levels in controlled-release formulations.",
        "Optimizing surfactant and oil ratios in emulsions/nanoemulsions.",
    ])
    deep2(n)

    n.box("Summary \u2013 Unit II", [
        "Excipients are functional; superdisintegrants and co-processed excipients are key modern developments.",
        "2^k factorial design studies k factors at 2 levels in 2^k runs and reveals interactions.",
        "Fractional factorial = screening; Central composite / Box-Behnken = optimization (RSM).",
    ])

    n.mcq_header("Unit II \u2013 Multiple Choice Questions")
    n.mcq("A 2\u00b3 factorial design requires how many experimental runs ?",
          ["4", "6", "8", "9"], 2, "2^3 = 8 runs.")
    n.mcq("Which of the following is a superdisintegrant ?",
          ["Lactose", "Croscarmellose sodium", "Magnesium stearate", "Talc"], 1)
    n.mcq("Colloidal silicon dioxide is used in tablets mainly as a :",
          ["Binder", "Glidant", "Disintegrant", "Sweetener"], 1)
    n.mcq("The main limitation of the OFAT approach is that it :",
          ["Is too fast", "Cannot detect interactions between factors",
           "Uses too few chemicals", "Requires no experiments"], 1)
    n.mcq("Prosolv (silicified MCC) is an example of a :",
          ["Co-processed excipient", "Preservative", "Chelating agent", "Colourant"], 0)
    n.mcq("EDTA is added to formulations as a :",
          ["Lubricant", "Chelating (sequestering) agent", "Diluent", "Binder"], 1)
    n.mcq("Which design is most suitable for optimization using response surface methodology ?",
          ["Full factorial screening", "Box-Behnken / central composite design",
           "OFAT", "Random design"], 1)
    n.mcq("In a factorial design, the low and high levels of a factor are usually denoted by :",
          ["0 and 1 only", "\u2212 and +", "A and B", "x and y"], 1)
    n.mcq("Magnesium stearate over-blending typically :",
          ["Increases dissolution", "Retards dissolution (hydrophobic film)",
           "Has no effect", "Improves taste"], 1)
    n.mcq("Which excipient class prevents oxidative degradation of a drug ?",
          ["Antioxidants", "Diluents", "Glidants", "Sweeteners"], 0)
    n.page_break()



# =====================================================================
#  UNIT III - SOLUBILITY & DISSOLUTION
# =====================================================================
def unit3(n):
    n.unit_title("Unit III \u2013 Solubility & Dissolution")

    n.h2("3.1 Solubility \u2013 Importance")
    n.para("Solubility is the maximum amount of a solute that dissolves in a given quantity of "
           "solvent at a specified temperature and pressure to form a saturated solution. For a "
           "drug to be absorbed it must first be present in solution at the site of absorption; "
           "therefore solubility (and the rate at which the drug dissolves) is frequently the "
           "rate-limiting step for the absorption of orally administered drugs.")
    n.bullets([
        "A drug must be dissolved before it can be absorbed \u2013 solubility limits bioavailability of poorly soluble (BCS II & IV) drugs.",
        "Governs the design of liquid dosage forms and the dose that can be delivered.",
        "Affects the dissolution rate and hence the onset and extent of action.",
        "Determines the formulation strategy (salt selection, solubilization techniques).",
    ])

    n.h2("3.2 Experimental Determination of Solubility")
    n.para("The equilibrium (saturation) solubility is most commonly determined by the "
           "shake-flask method. An excess of the drug is added to the solvent of defined pH and "
           "temperature in sealed vials, which are shaken or rotated in a constant-temperature "
           "bath until equilibrium (saturation) is reached. The supernatant is then filtered and "
           "the dissolved drug is assayed, usually by UV spectrophotometry or HPLC.")
    n.h3("Precautions")
    n.bullets([
        "Ensure true equilibrium is reached (adequate shaking time).",
        "Maintain a constant temperature throughout.",
        "Prevent evaporation of solvent (sealed containers).",
        "Confirm that the solid form has not changed (no polymorphic conversion).",
        "Use a validated, specific assay for the dissolved drug.",
    ])

    n.h2("3.3 Phase-Solubility Analysis")
    n.para("Phase-solubility analysis, developed by Higuchi and Connors, studies the effect of "
           "an increasing concentration of a solubilizing / complexing agent (ligand) on the "
           "solubility of the drug. Increasing amounts of the ligand are added to a fixed excess "
           "of drug; after equilibrium the total dissolved drug is plotted against ligand "
           "concentration. It is used to determine the stoichiometry and stability constant of "
           "complexes and to assess drug purity.")
    n.figure("phase_solubility.png", "Types of phase-solubility diagrams (Higuchi & Connors)", width=4.8)
    n.bullets([
        ("Type A (soluble complexes) \u2013", "solubility increases with ligand concentration : A\u029f = linear, A\u1d18 = positive deviation (higher-order complex), A\u0274 = negative deviation."),
        ("Type B (limited-solubility complexes) \u2013", "B\ua731 = complex of limited solubility, B\u026a = insoluble complex."),
    ])
    n.para(segments=[("Stability constant (1:1 complex) : ", True),
        ("K = slope / [S0 (1 \u2212 slope)], where S0 is the intrinsic solubility of the drug and "
         "'slope' is that of the A\u029f phase-solubility line.", )])

    n.h2("3.4 pH-Solubility Profile")
    n.para("For an ionizable drug, solubility varies markedly with pH. A pH-solubility profile "
           "plots the total solubility of the drug against pH over the physiological range "
           "(usually 1\u20138). Weak acids show increasing solubility as the pH rises above their "
           "pKa, while weak bases show increasing solubility as the pH falls below their pKa. "
           "The profile guides salt selection, the formulation pH and prediction of absorption "
           "along the GI tract, and helps identify the risk of precipitation on transfer from "
           "the acidic stomach to the more alkaline intestine.")

    n.h2("3.5 Techniques to Improve Solubility")
    n.para("Poorly water-soluble drugs (BCS Class II / IV) require solubility- and "
           "dissolution-enhancement techniques. The important approaches specified in the "
           "syllabus are described below.")

    n.h3("1. Cosolvency")
    n.para("A water-miscible cosolvent (e.g. ethanol, propylene glycol, glycerin, PEG 400) is "
           "added to water to reduce the polarity (dielectric constant) of the medium and "
           "increase the solubility of a poorly soluble, relatively non-polar drug. This process "
           "is called cosolvency or solvent blending. It is simple and widely used in oral and "
           "parenteral liquids; care is needed to avoid precipitation of the drug on dilution "
           "and to keep the cosolvent within safe/tolerable limits.")

    n.h3("2. Salt Formation")
    n.para("Converting a weak acid or base into an ionizable salt greatly increases aqueous "
           "solubility and dissolution rate (e.g. sodium salicylate, diclofenac sodium, "
           "hydrochloride salts of basic drugs). The higher pH (for salts of acids) or lower pH "
           "(for salts of bases) in the diffusion layer around the dissolving particle favours "
           "dissolution. Salt formation also improves stability and handling.")

    n.h3("3. Complexation")
    n.para("Formation of a soluble complex increases apparent solubility. Cyclodextrins "
           "(\u03b1-, \u03b2- and hydroxypropyl-\u03b2-cyclodextrin) form inclusion complexes in which the "
           "lipophilic drug molecule is entrapped within the hydrophobic internal cavity while "
           "the hydrophilic exterior confers water solubility. Complexation can also improve "
           "stability, reduce irritation and mask taste.")

    n.h3("4. Solid Dispersion")
    n.para("A solid dispersion is a dispersion of one or more active ingredients in an inert "
           "hydrophilic carrier matrix in the solid state. The drug may be present as fine "
           "crystals, in the amorphous state, or molecularly dispersed, giving greatly increased "
           "effective surface area, improved wetting and much faster dissolution.")
    n.table(
        ["Aspect", "Details"],
        [
            ["Types", "Simple eutectic mixtures, solid solutions, glass solutions/suspensions, amorphous precipitations."],
            ["Carriers", "PEG, PVP, HPMC, poloxamers, urea, mannitol, Soluplus."],
            ["Methods", "Fusion (melting) method, solvent evaporation, melting-solvent method, hot-melt extrusion, spray drying."],
            ["Limitation", "Physical instability \u2013 the amorphous drug may recrystallise on storage."],
        ],
        widths=[1.3, 5.2],
        fontsize=10.5,
    )

    n.h3("5. Micellar Solubilization")
    n.para("Surfactants added above their critical micelle concentration (CMC) form micelles; "
           "poorly soluble drug molecules partition into the hydrophobic core of the micelles, "
           "thereby increasing the apparent solubility. This is called micellar solubilization "
           "(e.g. polysorbates, bile salts). It is used in liquid orals, parenterals and topical "
           "products. The amount solubilized increases with surfactant concentration above the "
           "CMC.")

    n.h3("6. Hydrotropy")
    n.para("Hydrotropy is the increase in the aqueous solubility of a poorly soluble solute "
           "brought about by the addition of a large amount of a second solute called a "
           "hydrotrope. Hydrotropes are highly water-soluble compounds (e.g. sodium benzoate, "
           "sodium salicylate, urea, nicotinamide, sodium citrate) that enhance solubility by a "
           "self-aggregation / weak complexation mechanism; unlike surfactants they do not form "
           "true micelles and there is a minimum hydrotrope concentration for the effect.")

    n.h3("Other Approaches")
    n.bullets([
        ("Particle-size reduction \u2013", "micronization and nanonization increase surface area and dissolution rate."),
        ("pH adjustment / buffering \u2013", "to favour the ionized, more soluble form in the microenvironment."),
        ("Use of surfactants as wetting agents \u2013", "to improve wetting of hydrophobic powders."),
        ("Prodrug / structural modification \u2013", "temporary chemical modification to improve solubility."),
    ])
    n.box("High-Yield", [
        "Six syllabus techniques : cosolvency, salt formation, complexation, solid dispersion, micellar solubilization, hydrotropy.",
        "Cyclodextrins \u2192 inclusion complexation; carriers like PEG/PVP \u2192 solid dispersion.",
        "Hydrotropy needs a LARGE amount of a highly soluble second solute; no micelle formation.",
    ])



    # ------------------------------------------------ dissolution
    n.h2("3.6 Dissolution \u2013 Theories and Mechanisms")
    n.para("Dissolution is the process by which a solid substance goes into solution in a "
           "solvent. For solid oral dosage forms it is frequently the rate-determining step for "
           "drug absorption and is therefore a key quality-control and bioavailability "
           "parameter.")

    n.h3("(a) Diffusion-Layer Model (Noyes-Whitney / Nernst-Brunner)")
    n.para("This is the most widely accepted model. Dissolution is considered to occur in two "
           "steps : (i) rapid formation of a thin, stagnant, saturated layer of solution "
           "(the diffusion layer) at the solid surface, followed by (ii) diffusion of the "
           "dissolved drug across this layer into the bulk solution, which is the slow, "
           "rate-limiting step. The rate is described by the Noyes-Whitney (Nernst-Brunner) "
           "equation :")
    n.figure("diffusion_layer.png", "Diffusion-layer model of dissolution", width=5.0)
    n.formula("dC/dt = (D \u00b7 A / h \u00b7 V) \u00d7 (Cs \u2212 Ct)")
    n.para("where dC/dt = dissolution rate; D = diffusion coefficient of the drug; A = effective "
           "surface area of the dissolving solid; h = thickness of the diffusion layer; "
           "V = volume of the dissolution medium; Cs = saturation solubility of the drug; and "
           "Ct = concentration of the drug in the bulk at time t.")

    n.h3("(b) Danckwerts' (Surface-Renewal) Model")
    n.para("This model assumes that macroscopic packets of fresh solvent continually reach and "
           "renew the solid surface, absorb solute and carry it away into the bulk by eddy "
           "diffusion; there is no static diffusion layer. Mass transfer occurs by continuous "
           "surface renewal.")

    n.h3("(c) Interfacial-Barrier (Limited-Solvation) Model")
    n.para("This model assumes that the interfacial reaction (solvation) at the solid-liquid "
           "interface is the slow, rate-limiting step rather than the diffusion of the dissolved "
           "drug. An intermediate concentration exists at the interface that is not necessarily "
           "the saturation solubility.")

    n.h3("Factors Influencing Dissolution")
    n.para("On the basis of the Noyes-Whitney equation and practical experience, dissolution is "
           "affected by drug, formulation and apparatus factors :")
    n.table(
        ["Factor", "Effect on dissolution rate"],
        [
            ["Surface area (A)", "Smaller particle size / larger surface area \u2192 faster dissolution."],
            ["Saturation solubility (Cs)", "Higher Cs (polymorph, salt, amorphous form, pH) \u2192 faster dissolution."],
            ["Diffusion coefficient (D)", "Higher medium viscosity lowers D and the rate."],
            ["Diffusion-layer thickness (h)", "Greater agitation reduces h \u2192 faster dissolution."],
            ["Volume of medium (V)", "Larger volume (sink conditions) keeps (Cs \u2212 Ct) large."],
            ["Temperature", "Higher temperature raises Cs and D (test standardised at 37\u00b0C)."],
            ["Formulation factors", "Binders, hydrophobic lubricants, coating and high hardness retard dissolution; disintegrants and wetting agents accelerate it."],
        ],
        widths=[2.2, 4.3],
        fontsize=10.5,
    )

    n.h3("Intrinsic Dissolution Rate (IDR)")
    n.para("The intrinsic dissolution rate is the dissolution rate of a pure drug substance "
           "measured under conditions of constant surface area (usually a compressed disc of the "
           "pure drug held in a die \u2013 the Wood's apparatus). Because the surface area is kept "
           "constant, IDR (expressed as mg min\u207b\u00b9 cm\u207b\u00b2) reflects the intrinsic properties of "
           "the drug (solubility, crystal form) independent of formulation. An IDR below "
           "approximately 0.1 mg min\u207b\u00b9 cm\u207b\u00b2 usually indicates dissolution-rate-limited "
           "absorption.")

    n.h3("Sink and Non-Sink Conditions")
    n.bullets([
        ("Sink conditions \u2013", "the volume of dissolution medium is large enough (usually at least 3\u20135 times the volume required to make a saturated solution) that the dissolved-drug concentration stays low (< 10\u201315% of saturation). The concentration gradient is thus kept near maximum, mimicking the continuous removal (dilution/absorption) that occurs in-vivo. Sink conditions are recommended for dissolution testing."),
        ("Non-sink conditions \u2013", "the drug concentration approaches saturation, the gradient falls and the dissolution rate slows; results may not reflect in-vivo behaviour."),
    ])

    n.h2("3.7 In-Vitro Dissolution Testing")
    n.para("In-vitro dissolution testing measures the amount of drug released from a dosage form "
           "into a defined medium over time. It is used for quality control, batch-to-batch "
           "consistency, formulation development, and as a surrogate for bioavailability. Models "
           "are broadly of two types : closed-compartment systems (fixed volume of medium, e.g. "
           "basket and paddle) and open / flow-through systems (continuous fresh medium, "
           "maintaining sink conditions).")

    n.h3("Dissolution Test Apparatus (USP) \u2013 Designs")
    n.figure("dissolution_apparatus.png", "USP Apparatus I (basket) and II (paddle)", width=4.8)
    n.table(
        ["Apparatus", "Name", "Typical use"],
        [
            ["USP I", "Rotating basket", "Tablets, capsules (floating/disintegrating)."],
            ["USP II", "Paddle", "Tablets, capsules \u2013 most widely used."],
            ["USP III", "Reciprocating cylinder", "Modified / extended-release, pH-change studies."],
            ["USP IV", "Flow-through cell", "Poorly soluble drugs, implants; maintains sink."],
            ["USP V", "Paddle over disc", "Transdermal patches."],
            ["USP VI", "Rotating cylinder", "Transdermal patches."],
            ["USP VII", "Reciprocating holder", "Extended-release, transdermals, small volumes."],
        ],
        widths=[1.2, 2.2, 3.1],
        fontsize=10.5,
    )
    n.para("Standard conditions for apparatus I and II : medium volume 500\u2013900 mL (commonly "
           "900 mL), temperature 37 \u00b1 0.5\u00b0C, basket usually rotated at 100 rpm and paddle "
           "usually at 50\u201375 rpm.")

    n.h3("Dissolution Testing : Conventional vs Controlled-Release Products")
    n.bullets([
        ("Conventional (immediate-release) \u2013", "a single-point specification is usually adequate (e.g. not less than a stated % dissolved in 30\u201345 minutes)."),
        ("Controlled / extended-release \u2013", "multi-point (three or more) specifications are required to characterise the whole release profile (e.g. at 1, 4 and 8 h) so as to guard against both dose-dumping and under-release; media of changing pH are often used."),
    ])
    n.figure("release_profiles.png", "Common drug-release kinetic profiles", width=4.6)

    n.h3("Data Handling and Correction Factor")
    n.para("When samples are withdrawn during a dissolution test and replaced with an equal "
           "volume of fresh medium, the amount of drug removed at each sampling point must be "
           "accounted for when calculating the cumulative amount dissolved. A correction factor "
           "is applied to add back the quantity of drug removed in the previous samples, so that "
           "the true cumulative percentage released is obtained. The corrected data are then "
           "analysed by model-dependent methods (zero-order, first-order, Higuchi, "
           "Korsmeyer-Peppas) and model-independent methods (f\u2081 difference factor and f\u2082 "
           "similarity factor).")
    n.box("Worked Example \u2013 f\u2082 similarity factor", [
        "The f\u2082 similarity factor compares a test and a reference dissolution profile.",
        "f\u2082 = 50 \u00d7 log { [1 + (1/n) \u03a3 (R\u209c \u2212 T\u209c)\u00b2]^(\u22120.5) \u00d7 100 }.",
        "f\u2082 between 50 and 100 indicates the two profiles are similar (difference \u2264 ~10%).",
        "f\u2081 (difference factor) should be between 0 and 15 for similarity.",
    ])

    n.h3("Biorelevant Media")
    n.para("Biorelevant dissolution media simulate the composition of gastrointestinal fluids "
           "more closely than simple buffers and therefore give better in-vivo prediction, "
           "especially for poorly soluble drugs :")
    n.table(
        ["Medium", "Simulates"],
        [
            ["SGF (Simulated Gastric Fluid)", "Fasted stomach (pH ~1.2, with or without pepsin)."],
            ["SIF (Simulated Intestinal Fluid)", "Intestine (pH ~6.8, with or without pancreatin)."],
            ["FaSSIF", "Fasted-state simulated intestinal fluid (bile salt + lecithin, pH ~6.5)."],
            ["FeSSIF", "Fed-state simulated intestinal fluid (higher bile salt, pH ~5.0)."],
        ],
        widths=[3.0, 3.5],
        fontsize=10.5,
    )

    n.h2("3.8 In-Vitro / In-Vivo Correlation (IVIVC)")
    n.para("An in-vitro / in-vivo correlation is a predictive mathematical model that describes "
           "the relationship between an in-vitro property of a dosage form (usually the extent "
           "or rate of drug dissolution) and a relevant in-vivo response (usually the plasma "
           "drug concentration or the amount of drug absorbed). A well-established IVIVC allows "
           "dissolution testing to serve as a surrogate for bioequivalence studies, thereby "
           "supporting formulation and manufacturing changes and reducing the need for human "
           "studies.")
    n.figure("ivivc.png", "Level A IVIVC \u2013 point-to-point correlation", width=4.2)
    n.h3("Levels of Correlation")
    n.bullets([
        ("Level A \u2013", "a point-to-point correlation between the entire in-vitro dissolution curve and the entire in-vivo absorption curve; the highest and most informative level."),
        ("Level B \u2013", "uses statistical-moment analysis; the mean in-vitro dissolution time is compared with the mean in-vivo residence / dissolution time. It is not a point-to-point correlation."),
        ("Level C \u2013", "a single-point correlation relating one dissolution parameter (e.g. % dissolved at one time) to one pharmacokinetic parameter (e.g. C\u2098\u2090\u2093 or AUC); the weakest level."),
        ("Multiple Level C \u2013", "relates dissolution at several time points to one or more pharmacokinetic parameters."),
    ])
    deep3(n)

    n.box("Summary \u2013 Unit III", [
        "Noyes-Whitney : dC/dt = DA(Cs \u2212 Ct)/hV; sink conditions keep the gradient maximal.",
        "USP II (paddle) and USP I (basket) are the standard apparatus; 37\u00b0C, 900 mL.",
        "IDR is measured at constant surface area (Wood's apparatus).",
        "Level A IVIVC is the highest, point-to-point correlation.",
    ])

    n.mcq_header("Unit III \u2013 Multiple Choice Questions")
    n.mcq("The Noyes-Whitney equation describes the rate of :",
          ["Absorption", "Dissolution", "Metabolism", "Excretion"], 1)
    n.mcq("In the Noyes-Whitney equation, 'h' represents :",
          ["Height of tablet", "Thickness of the diffusion layer",
           "Half-life", "Hydration number"], 1)
    n.mcq("Sink condition means the volume of medium is :",
          ["Equal to saturation volume", "At least 3\u20135 times the saturation volume",
           "Very small", "Zero"], 1)
    n.mcq("Cyclodextrins improve solubility mainly by :",
          ["Cosolvency", "Inclusion complexation", "Salt formation", "Micellization"], 1)
    n.mcq("Intrinsic dissolution rate is measured under conditions of constant :",
          ["Temperature only", "Surface area", "Volume only", "pH only"], 1,
          "Using a compressed disc (Wood's apparatus).")
    n.mcq("The most widely used dissolution apparatus for conventional tablets is :",
          ["USP I (basket)", "USP II (paddle)", "USP IV (flow-through)", "USP V"], 1)
    n.mcq("Hydrotropy differs from micellar solubilization in that hydrotropes :",
          ["Form true micelles", "Do NOT form micelles",
           "Are always surfactants", "Reduce solubility"], 1)
    n.mcq("The highest level of in-vitro/in-vivo correlation is :",
          ["Level A", "Level B", "Level C", "Multiple level C"], 0)
    n.mcq("FaSSIF and FeSSIF are examples of :",
          ["Buffers only", "Biorelevant dissolution media", "Surfactants", "Cosolvents"], 1)
    n.mcq("Phase-solubility analysis was introduced by :",
          ["Noyes and Whitney", "Higuchi and Connors", "Arrhenius", "Lipinski"], 1)
    n.mcq("An f\u2082 (similarity factor) value in which range indicates similar dissolution "
          "profiles ?",
          ["0\u201315", "15\u201350", "50\u2013100", "> 100"], 2)
    n.mcq("Solid dispersion improves dissolution mainly by :",
          ["Increasing particle size", "Converting drug to amorphous / molecular dispersion",
           "Forming a salt", "Raising the pH"], 1)
    n.page_break()



# =====================================================================
#  UNIT IV - PRODUCT STABILITY
# =====================================================================
def unit4(n):
    n.unit_title("Unit IV \u2013 Product Stability")

    n.h2("4.1 Introduction")
    n.para("Stability is defined as the capacity of a drug substance or drug product to retain "
           "its physical, chemical, microbiological, therapeutic and toxicological properties "
           "within specified limits throughout its shelf life under the influence of "
           "environmental factors such as temperature, humidity and light. Stability studies "
           "establish how the quality of a product varies with time and are used to assign the "
           "shelf life (expiry date) and the recommended storage conditions.")
    n.h3("Importance of Stability Studies")
    n.bullets([
        "To ensure the safety and efficacy of the product up to the labelled expiry date.",
        "To establish the shelf life and recommended storage conditions.",
        "To select a stable formulation, packaging and container-closure system.",
        "To satisfy regulatory (ICH) requirements for product registration.",
    ])

    n.h2("4.2 Degradation (Reaction) Kinetics")
    n.para("Chemical stability is studied using reaction kinetics, which describes the rate at "
           "which a drug degrades and the order of the reaction. The order of a reaction is the "
           "manner in which the reaction rate depends on the concentration of the reactant(s).")

    n.h3("Zero-Order Kinetics")
    n.para("The rate of degradation is independent of the concentration of the reactant "
           "(constant rate). Suspensions and many solid dosage forms show apparent zero-order "
           "loss of potency.")
    n.formula("C = C\u2080 \u2212 k\u2080 t")
    n.bullets([
        ("Plot :", "concentration (C) vs time is linear; slope = \u2212k\u2080."),
        ("Units of k\u2080 :", "concentration \u00d7 time\u207b\u00b9 (e.g. mg mL\u207b\u00b9 h\u207b\u00b9)."),
        ("Half-life :", "t\u00bd = C\u2080 / 2k\u2080 (depends on initial concentration)."),
        ("Shelf life :", "t\u2089\u2080 = 0.1 C\u2080 / k\u2080."),
    ], level=1)

    n.h3("First-Order Kinetics")
    n.para("The rate of degradation is directly proportional to the concentration of the "
           "reactant. Most solution-phase degradations follow first-order (or pseudo-first "
           "order) kinetics.")
    n.formula("log C = log C\u2080 \u2212 (k t / 2.303)")
    n.bullets([
        ("Plot :", "log C vs time is linear; slope = \u2212k/2.303."),
        ("Units of k :", "time\u207b\u00b9 (e.g. h\u207b\u00b9)."),
        ("Half-life :", "t\u00bd = 0.693 / k (independent of initial concentration)."),
        ("Shelf life :", "t\u2089\u2080 = 0.105 / k."),
    ], level=1)
    n.figure("order_kinetics.png", "Zero- vs first-order degradation profiles", width=5.2)

    n.h3("Pseudo-Zero and Pseudo-First Order")
    n.para("In a suspension, the drug in solution degrades by first order but is continuously "
           "replenished from the undissolved solid, so the concentration in solution remains "
           "constant and the loss appears as zero order (pseudo-zero order). When one reactant "
           "(e.g. water in hydrolysis) is present in large excess and effectively constant, a "
           "second-order reaction behaves as pseudo-first order.")

    n.box("Worked Example \u2013 first-order shelf life", [
        "A drug in solution degrades by first order with k = 2.1 \u00d7 10\u207b\u00b3 day\u207b\u00b9.",
        "t\u2089\u2080 = 0.105 / k = 0.105 / (2.1 \u00d7 10\u207b\u00b3) = 50 days.",
        "t\u00bd = 0.693 / k = 0.693 / (2.1 \u00d7 10\u207b\u00b3) = 330 days.",
        "Thus the product loses 10% potency in about 50 days.",
    ])

    n.h2("4.3 Mechanisms of Degradation")
    n.table(
        ["Mechanism", "Description / example"],
        [
            ["Hydrolysis", "Reaction with water cleaving ester / amide bonds \u2013 the commonest route (aspirin, procaine, penicillins). Catalysed by H\u207a / OH\u207b."],
            ["Oxidation", "Loss of electrons / reaction with oxygen, often free-radical (adrenaline, ascorbic acid, vitamins). Controlled by antioxidants, chelators, inert gas."],
            ["Photolysis", "Light (UV)-induced degradation (nifedipine, riboflavin, sodium nitroprusside). Controlled by amber / opaque packaging."],
            ["Reduction", "Gain of electrons; comparatively uncommon."],
            ["Racemization", "Conversion of an active enantiomer into a less/inactive isomer (adrenaline)."],
            ["Isomerization", "Conversion to an isomer of different activity (tetracycline \u2192 epi-tetracycline)."],
            ["Decarboxylation", "Loss of CO\u2082 from carboxylic acids (p-aminosalicylic acid)."],
            ["Polymerization", "Combination of molecules to larger units (concentrated ampicillin solutions)."],
        ],
        widths=[1.8, 4.7],
        fontsize=10.5,
    )

    n.h2("4.4 Factors Influencing Stability")
    n.h3("(a) Temperature \u2013 the Arrhenius Equation")
    n.para("An increase in temperature generally accelerates degradation. The relationship "
           "between the rate constant and temperature is given by the Arrhenius equation, which "
           "is the theoretical basis of accelerated stability testing :")
    n.formula("k = A \u00b7 e^(\u2212Ea/RT)     or     log k = log A \u2212 Ea / (2.303 RT)")
    n.para("where k = rate constant, A = frequency (Arrhenius) factor, Ea = energy of "
           "activation, R = gas constant and T = absolute temperature. A plot of log k against "
           "1/T (the Arrhenius plot) is a straight line of slope \u2212Ea/2.303R and allows the "
           "rate constant at room temperature to be predicted from data obtained at elevated "
           "temperatures.")
    n.figure("arrhenius.png", "Arrhenius plot of log k against 1/T", width=4.3)

    n.h3("(b) pH Effect \u2013 the pH-Rate Profile")
    n.para("Hydrolysis and many other reactions are catalysed by hydrogen and hydroxyl ions "
           "(specific acid-base catalysis) and by buffer species (general acid-base catalysis). "
           "A plot of the logarithm of the degradation-rate constant against pH gives the "
           "pH-rate profile, from which the pH of maximum stability (the minimum of the curve) "
           "is identified and used to select the formulation pH and buffer.")
    n.figure("ph_rate.png", "pH-rate profile showing the pH of maximum stability", width=4.6)

    n.h3("(c) Media / Solvent Effects")
    n.para("The nature of the solvent (dielectric constant, polarity), the ionic strength and "
           "the presence of buffer salts influence the rate of degradation. Changing to a less "
           "polar solvent or a cosolvent system can slow ionic degradation reactions; an "
           "increase in ionic strength can accelerate or retard a reaction depending on the "
           "charges of the reacting species (the primary salt effect).")

    n.h3("(d) Other Factors")
    n.bullets([
        ("Light \u2013", "photolabile drugs require amber / opaque packaging."),
        ("Oxygen \u2013", "oxidation is controlled by antioxidants, chelating agents and nitrogen purging."),
        ("Moisture / humidity \u2013", "promotes hydrolysis and microbial growth; controlled by desiccants and moisture-proof packaging."),
        ("Excipients & container \u2013", "incompatible excipients or leachables from the container may catalyse degradation."),
    ])

    n.h2("4.5 Accelerated Stability Studies")
    n.para("Because real-time shelf-life determination would take years, accelerated stability "
           "studies subject the product to elevated temperature (and humidity) to speed up "
           "degradation. Using the Arrhenius relationship, the rate constant at these stress "
           "conditions is extrapolated to normal storage temperature to predict the shelf life "
           "in a much shorter time.")
    n.h3("General Procedure")
    n.numbered([
        "Store the product at several elevated temperatures (e.g. 40, 50, 60\u00b0C).",
        "Withdraw samples at intervals and assay the intact drug.",
        "Determine the order of reaction and the rate constant (k) at each temperature.",
        "Plot log k against 1/T (Arrhenius plot).",
        "Extrapolate to obtain k at room temperature (25\u00b0C).",
        "Calculate the shelf life (t\u2089\u2080) from the room-temperature rate constant.",
    ])

    n.h2("4.6 Interpretation of Kinetic Data (API & Tablets)")
    n.para("The assay data (concentration vs time) obtained at each temperature are plotted "
           "according to different reaction orders; the plot that gives the best straight line "
           "indicates the order, and its slope gives the rate constant. For an API in solution, "
           "first-order plots (log C vs t) are usually linear, whereas for tablets and "
           "suspensions the loss of potency frequently follows apparent zero-order kinetics. "
           "From the room-temperature rate constant the t\u2089\u2080 (time for 10% degradation) is "
           "calculated and assigned as the shelf life. Solid-state reactions may not obey simple "
           "Arrhenius behaviour because of moisture, phase changes and multiple simultaneous "
           "mechanisms, so accelerated predictions must be confirmed by real-time data.")

    n.h2("4.7 Solid-State Stability")
    n.para("Degradation in the solid state (drug substance, tablets, powders) is generally "
           "slower and more complex than in solution. It is influenced by moisture, temperature, "
           "polymorphic transitions, particle size and the presence of excipients. Reactions "
           "often take place at the solid surface or in adsorbed moisture films and may follow "
           "topochemical or sigmoidal kinetics rather than a simple order. Solid-state stability "
           "is studied by storing the solid under stress (temperature / humidity) and monitoring "
           "assay, appearance, dissolution and degradation products.")

    n.h2("4.8 Shelf-Life Assignment")
    n.para("The shelf life (expiration dating period) is the time during which the product "
           "remains within its approved specifications under the recommended storage conditions. "
           "It is commonly taken as t\u2089\u2080 \u2013 the time for the drug content to fall to 90% of its "
           "labelled amount (i.e. 10% degradation) \u2013 provided the degradation products remain "
           "within safe limits. It is determined from real-time data (confirmatory) and "
           "supported by accelerated data (predictive), and is stated together with the "
           "appropriate storage statement.")

    n.h2("4.9 Stability Protocols and Reports")
    n.para("A stability protocol is a pre-approved written plan that defines how the study will "
           "be conducted; a stability report summarises and interprets the data obtained.")
    n.h3("A Stability Protocol Typically Specifies")
    n.bullets([
        "Product details, batch number, container-closure system and number of batches (usually at least 3 primary batches).",
        "Storage conditions (long-term, intermediate, accelerated) and container orientation.",
        "Testing time points (e.g. 0, 3, 6, 9, 12, 18, 24, 36 months).",
        "Tests to be performed (assay, related substances, dissolution, appearance, pH, moisture, microbial limits).",
        "Validated, stability-indicating analytical methods and acceptance criteria.",
    ])

    n.h2("4.10 ICH Guidelines for Stability Testing")
    n.para("The International Council for Harmonisation (ICH) Q1 series harmonises stability "
           "requirements across regions :")
    n.table(
        ["Guideline", "Subject"],
        [
            ["Q1A(R2)", "Stability testing of new drug substances and products."],
            ["Q1B", "Photostability testing."],
            ["Q1C", "Stability testing for new dosage forms."],
            ["Q1D", "Bracketing and matrixing designs."],
            ["Q1E", "Evaluation of stability data (shelf-life extrapolation)."],
            ["Q1F", "Stability data package for zones III and IV (hot / humid)."],
        ],
        widths=[1.6, 4.9],
        fontsize=10.5,
    )
    n.h3("Climatic Zones and Storage Conditions")
    n.para("The world is divided into four climatic zones; India falls in Zone IVb (hot and very "
           "humid). The ICH Q1A(R2) recommended storage conditions are :")
    n.table(
        ["Study", "Condition", "Minimum period"],
        [
            ["Long-term", "25\u00b0C \u00b1 2\u00b0C / 60% RH \u00b1 5% (or 30\u00b0C / 65% RH for Zone IV)", "12 months"],
            ["Intermediate", "30\u00b0C \u00b1 2\u00b0C / 65% RH \u00b1 5%", "6 months"],
            ["Accelerated", "40\u00b0C \u00b1 2\u00b0C / 75% RH \u00b1 5%", "6 months"],
        ],
        widths=[1.5, 3.6, 1.4],
        fontsize=10.5,
    )
    n.para("A significant change at the accelerated condition (e.g. a 5% loss of assay from the "
           "initial value, a degradation product exceeding its specification, or failure of "
           "dissolution / physical attributes) triggers testing at the intermediate condition. "
           "ICH Q1B photostability testing uses defined visible and UV light exposures.")

    deep4(n)

    n.box("Summary \u2013 Unit IV", [
        "First order : t\u00bd = 0.693/k, t\u2089\u2080 = 0.105/k;  zero order : t\u2089\u2080 = 0.1C\u2080/k\u2080.",
        "Hydrolysis and oxidation are the two major degradation routes.",
        "Arrhenius equation underlies accelerated testing; pH-rate profile gives the pH of maximum stability.",
        "Shelf life = t\u2089\u2080 (time for 10% degradation).",
        "ICH Q1A(R2) : long-term 25\u00b0C/60% RH, accelerated 40\u00b0C/75% RH for 6 months.",
    ])

    n.mcq_header("Unit IV \u2013 Multiple Choice Questions")
    n.mcq("For a first-order reaction, the shelf life (t\u2089\u2080) is given by :",
          ["0.693/k", "0.105/k", "0.1C\u2080/k\u2080", "C\u2080/2k\u2080"], 1)
    n.mcq("The half-life of a first-order reaction is :",
          ["Dependent on initial concentration", "0.693/k (independent of C\u2080)",
           "C\u2080/2k\u2080", "Always 100 days"], 1)
    n.mcq("The Arrhenius equation relates the rate constant to :",
          ["pH", "Temperature", "Surface area", "Viscosity"], 1)
    n.mcq("Aspirin most commonly degrades by :",
          ["Oxidation", "Hydrolysis", "Photolysis", "Racemization"], 1)
    n.mcq("The pH of maximum stability is obtained from the :",
          ["Arrhenius plot", "pH-rate profile", "Phase diagram", "BCS chart"], 1)
    n.mcq("Accelerated stability conditions per ICH Q1A(R2) are :",
          ["25\u00b0C/60% RH", "30\u00b0C/65% RH", "40\u00b0C/75% RH", "50\u00b0C/90% RH"], 2)
    n.mcq("Shelf life is usually defined as the time for the potency to fall to :",
          ["50%", "75%", "90% of labelled amount", "99%"], 2)
    n.mcq("Suspensions usually show which apparent order of degradation ?",
          ["Zero order", "First order", "Second order", "Third order"], 0)
    n.mcq("Which ICH guideline deals with photostability testing ?",
          ["Q1A", "Q1B", "Q1C", "Q1D"], 1)
    n.mcq("Oxidative degradation is best minimised by adding :",
          ["A binder", "An antioxidant + chelating agent", "A disintegrant", "A sweetener"], 1)
    n.mcq("India belongs to which ICH climatic zone ?",
          ["Zone I", "Zone II", "Zone III", "Zone IVb"], 3)
    n.page_break()



# =====================================================================
#  UNIT V - COSMETICS
# =====================================================================
def unit5(n):
    n.unit_title("Unit V \u2013 Cosmetics")

    n.h2("5.1 Introduction")
    n.para("Cosmetics are articles intended to be rubbed, poured, sprinkled or sprayed on, "
           "introduced into or otherwise applied to the human body for cleansing, beautifying, "
           "promoting attractiveness or altering the appearance, without affecting the body's "
           "structure or functions. A product that additionally exerts a therapeutic or "
           "'drug-like' benefit (e.g. anti-dandruff, anti-ageing, sunscreen) is termed a "
           "cosmeceutical. This unit deals with the formulation, evaluation and packaging of "
           "important cosmetic products.")

    n.h3("Emulsion Basis of Many Cosmetics")
    n.para("Many cosmetic creams and lotions are emulsions \u2013 dispersions of one liquid in "
           "another immiscible liquid stabilised by an emulsifier. The two common types are "
           "oil-in-water (o/w), which are non-greasy and washable, and water-in-oil (w/o), which "
           "are greasy and occlusive.")
    n.figure("emulsion_types.png", "Oil-in-water (o/w) and water-in-oil (w/o) emulsions", width=5.0)

    n.h3("HLB System")
    n.para("The Hydrophilic-Lipophilic Balance (HLB) is a numerical scale (0\u201320) that expresses "
           "the relative affinity of a surfactant for water and oil. It guides the selection of "
           "emulsifiers : low-HLB surfactants (3\u20136) favour w/o emulsions, while high-HLB "
           "surfactants (8\u201318) favour o/w emulsions.")
    n.figure("hlb_scale.png", "The HLB scale and surfactant applications", width=5.6)

    # ---------------------------------------------------- dentifrices
    n.h2("5.2 Dentifrices (Tooth Powders, Pastes and Gels)")
    n.para("Dentifrices are substances used with a toothbrush to clean the accessible surfaces "
           "of the teeth. They remove food debris, plaque and stains, polish the teeth and may "
           "deliver therapeutic agents (fluoride, anti-sensitivity, anti-tartar, antimicrobial).")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Abrasives / Polishing agents", "Remove plaque and stains; polish teeth.", "Calcium carbonate, dicalcium phosphate, hydrated silica, calcium pyrophosphate."],
            ["Humectants", "Retain moisture; prevent drying of the paste.", "Glycerin, sorbitol, propylene glycol."],
            ["Binders / Thickeners", "Give consistency; prevent separation.", "Sodium CMC, carrageenan, xanthan gum."],
            ["Surfactants (detergents)", "Foaming and cleansing.", "Sodium lauryl sulphate."],
            ["Sweeteners", "Pleasant taste.", "Saccharin, sorbitol."],
            ["Flavours", "Freshness and acceptability.", "Peppermint, spearmint, menthol."],
            ["Therapeutic agents", "Anticaries / anti-sensitivity / antimicrobial.", "Sodium fluoride, stannous fluoride, strontium chloride, triclosan."],
            ["Preservatives", "Prevent microbial growth.", "Parabens, sodium benzoate."],
        ],
        widths=[1.9, 2.2, 2.4],
        fontsize=10,
    )
    n.h3("Formulation & Preparation")
    n.bullets([
        ("Tooth powder \u2013", "abrasives, detergent, sweetener and flavour are finely powdered, thoroughly blended and sieved."),
        ("Tooth paste \u2013", "the humectant is dispersed in water, the binder is added to form a gel, the abrasive is mixed in, then surfactant, sweetener and flavour are added, and the mass is de-aerated and homogenised."),
        ("Tooth gel \u2013", "similar to the paste but uses a higher proportion of a gelling agent (e.g. silica) to give a clear or translucent gel."),
    ])
    n.h3("Evaluation")
    n.bullets([
        "Abrasiveness (should clean without damaging enamel \u2013 RDA value).",
        "pH (near neutral, ~6.5\u20139).",
        "Foaming ability, spreadability and consistency (extrudability from tube).",
        "Moisture content, homogeneity and absence of hard/sharp particles.",
        "Fluoride / therapeutic content assay and stability.",
        "Microbial limits.",
    ])
    n.h3("Packaging")
    n.para("Tooth powders are packed in wide-mouth plastic or metal containers with a sifter "
           "cap; pastes and gels are packed in collapsible aluminium or laminated plastic tubes "
           "or laminate dispensers, placed in cartons.")

    # ---------------------------------------------------- nail polish
    n.h2("5.3 Manicure Preparations \u2013 Nail Polish (Nail Lacquer)")
    n.para("Nail polish (nail lacquer / enamel) is a coloured lacquer applied to the finger and "
           "toe nails for decoration and protection.")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Film former", "Forms the glossy adherent film.", "Nitrocellulose."],
            ["Resins / Modifiers", "Improve gloss, adhesion, hardness.", "Toluene-sulphonamide-formaldehyde resin."],
            ["Plasticizers", "Impart flexibility to the film.", "Dibutyl phthalate, camphor, castor oil."],
            ["Solvents & Diluents", "Dissolve film former; control drying.", "Ethyl acetate, butyl acetate, toluene."],
            ["Colourants", "Impart colour.", "Approved pigments, lakes, titanium dioxide."],
            ["Suspending agent", "Keep pigments dispersed (thixotropy).", "Modified bentonite (stearalkonium hectorite)."],
            ["Pearlising agent", "Pearly / lustrous effect.", "Guanine, bismuth oxychloride, mica."],
        ],
        widths=[1.8, 2.3, 2.4],
        fontsize=10,
    )
    n.h3("Formulation")
    n.para("The film former, resin and plasticizer are dissolved in the solvent blend; the "
           "pre-dispersed pigments and the suspending agent are added, and the lacquer is milled "
           "to a smooth, uniform dispersion.")
    n.h3("Evaluation")
    n.bullets([
        "Drying time, gloss and smoothness of the film.",
        "Adhesion, hardness and flexibility of the dried film.",
        "Water and abrasion resistance.",
        "Colour uniformity and non-settling of pigment.",
        "Application / flow properties (viscosity).",
    ])
    n.h3("Packaging")
    n.para("Small glass bottles fitted with a cap incorporating an applicator brush; the cap "
           "must be solvent-resistant and give an airtight seal to prevent solvent evaporation. "
           "The related nail-polish remover contains solvents (acetone, ethyl acetate) with an "
           "added emollient.")

    # ---------------------------------------------------- lipstick
    n.h2("5.4 Lipsticks")
    n.para("A lipstick is a moulded stick consisting of a dispersion of colouring matter in a "
           "base of oils, fats and waxes, used to impart colour and protection to the lips.")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Waxes", "Give rigidity and the moulded shape; raise melting point.", "Carnauba wax, beeswax, candelilla wax, ozokerite."],
            ["Oils", "Dissolve / disperse dyes; provide gloss and emolliency.", "Castor oil, mineral oil, isopropyl myristate."],
            ["Fats", "Improve texture and application.", "Cocoa butter, lanolin, hydrogenated oils."],
            ["Colourants", "Staining dye and covering pigments.", "Eosin (bromo-acid dye), lakes, titanium dioxide."],
            ["Perfume", "Mask the fatty odour; impart fragrance.", "Rose, fruit flavours."],
            ["Antioxidant / Preservative", "Prevent rancidity / microbial growth.", "BHA, BHT, tocopherol, parabens."],
        ],
        widths=[1.8, 2.4, 2.3],
        fontsize=10,
    )
    n.h3("Formulation & Preparation")
    n.para("The staining dye is dissolved in castor oil; the waxes and fats are melted together; "
           "the two are combined with the dispersed pigments and milled; perfume and antioxidant "
           "are added; and the molten mass is poured into moulds, cooled, removed and 'flamed' "
           "to give a glossy surface.")
    n.h3("Evaluation")
    n.bullets([
        "Melting point (should be above ~55\u201360\u00b0C to resist deformation).",
        "Breaking point / mechanical strength.",
        "Force of application and spreadability.",
        "Colour uniformity, gloss and the 'perspiration' (bleeding) test.",
        "Surface anomalies, thixotropy and skin-irritation (safety) tests.",
    ])
    n.h3("Packaging")
    n.para("Retractable metal or plastic swivel (propel-repel) cases that protect the stick and "
           "allow easy application, packed in cartons.")

    # ---------------------------------------------------- mascara
    n.h2("5.5 Eye-Lash Preparations (Mascara)")
    n.para("Mascara is applied to the eyelashes to darken, thicken and lengthen them. It is "
           "available in cake, cream (emulsion) and liquid forms. Being used near the eye it "
           "must be non-irritant, safe and free from harmful micro-organisms.")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Pigments", "Impart colour (usually black / brown).", "Iron oxides, approved carbon black."],
            ["Waxes", "Film formation; thicken the lashes.", "Beeswax, carnauba wax, paraffin wax."],
            ["Film formers / Resins", "Adhesion and water resistance.", "Acrylate polymers, PVP."],
            ["Emulsifiers / Surfactants", "Stabilise emulsion mascara.", "Triethanolamine stearate, soaps."],
            ["Preservatives", "Essential for eye-area safety.", "Parabens, phenoxyethanol."],
            ["Solvent / Water", "Vehicle.", "Water (emulsion) or volatile solvents."],
        ],
        widths=[1.9, 2.3, 2.3],
        fontsize=10,
    )
    n.h3("Formulation & Evaluation")
    n.para("In emulsion (cream) mascara the waxes and emulsifier form the oil phase, which is "
           "emulsified with the aqueous phase containing dispersed pigment, film former and "
           "preservative, and the product is milled to a smooth paste. Evaluation focuses on "
           "ocular safety and non-irritancy, ease and evenness of application, smudge and water "
           "resistance, drying time, adhesion, flaking, microbial limits, preservative efficacy "
           "and colour stability.")
    n.h3("Packaging")
    n.para("A slim tube fitted with a screw cap carrying a spiral applicator brush (wand); the "
           "container must be airtight to prevent drying and contamination.")

    # ---------------------------------------------------- baby care
    n.h2("5.6 Baby-Care Products")
    n.para("Baby-care products are formulated for the delicate, thin and sensitive skin of "
           "infants. They must be extremely mild, non-irritant, 'tear-free' (for washes and "
           "shampoos) and free from harsh chemicals. Common products include baby powder, baby "
           "oil, baby cream / lotion, baby soap and baby shampoo.")
    n.h3("Common Products & Requirements")
    n.bullets([
        ("Baby powder \u2013", "talc or corn-starch with zinc oxide and a mild perfume; absorbs moisture and helps prevent nappy rash (talc must be asbestos-free)."),
        ("Baby oil \u2013", "light mineral oil / vegetable oils to protect and moisturise the skin."),
        ("Baby cream / lotion \u2013", "emollients, humectants and protectants (zinc oxide) with mild preservatives."),
        ("Baby shampoo \u2013", "mild non-ionic / amphoteric surfactants adjusted to an eye-neutral pH ('no-tears')."),
    ])
    n.h3("Evaluation & Packaging")
    n.bullets([
        "Mildness / non-irritancy to skin and eye (patch and ocular tests).",
        "pH (skin-compatible ~5.5\u20137; eye-neutral for shampoo).",
        "Absence of harmful substances and heavy metals; microbial limits and preservative efficacy.",
        "Fineness/flow (powder), spreadability (cream), foam (shampoo).",
    ])
    n.para("Powders are packed in sifter-top containers; oils, lotions and shampoos in squeeze / "
           "flip-top plastic bottles \u2013 child-safe, hygienic and easy to use.")



    # ---------------------------------------------------- creams
    n.h2("5.7 Moisturizing Cream")
    n.para("A moisturizing cream is an emulsion designed to add and retain moisture in the skin, "
           "keeping it soft and supple by reducing trans-epidermal water loss. It generally acts "
           "through a combination of occlusives, humectants and emollients.")
    n.h3("Ingredients")
    n.bullets([
        ("Occlusives \u2013", "form a film that reduces water loss (petrolatum, mineral oil, beeswax, dimethicone)."),
        ("Humectants \u2013", "attract and hold water in the stratum corneum (glycerin, sorbitol, propylene glycol, hyaluronic acid, urea)."),
        ("Emollients \u2013", "smooth and soften the skin (fatty alcohols, esters, lanolin)."),
        ("Emulsifiers \u2013", "stabilise the o/w emulsion (stearic acid + TEA, cetostearyl alcohol / steareth)."),
        ("Preservatives, antioxidants, perfume and purified water.", ),
    ])
    n.h3("Preparation")
    n.para("The oil-phase and water-phase ingredients are heated separately to about 70\u201375\u00b0C; "
           "the phases are combined with stirring, emulsified and cooled with continuous mixing; "
           "perfume and heat-sensitive actives are added below 40\u00b0C.")

    n.h2("5.8 Vanishing Cream")
    n.para("A vanishing cream is a stearic-acid-based oil-in-water (o/w) emulsion that "
           "'vanishes' (leaves no visible greasy residue) when rubbed into the skin, leaving a "
           "thin protective film. It is a non-greasy day cream and serves as a base for "
           "foundation make-up.")
    n.h3("Typical Formula")
    n.table(
        ["Ingredient", "Role"],
        [
            ["Stearic acid", "Main base; part is saponified to form the emulsifier."],
            ["Potassium hydroxide / borax", "Alkali to saponify part of the stearic acid (in-situ soap)."],
            ["Glycerin / Propylene glycol", "Humectant."],
            ["Purified water", "Continuous (external) phase."],
            ["Preservative & Perfume", "Stability and fragrance."],
        ],
        widths=[2.7, 3.8],
        fontsize=10.5,
    )
    n.h3("Preparation")
    n.para("Stearic acid is melted (oil phase); the alkali is dissolved in the heated aqueous "
           "phase with the humectant; the aqueous phase is added to the oil phase with stirring "
           "\u2013 part of the stearic acid is saponified to form the soap emulsifier, giving a "
           "smooth o/w cream; the perfume is added on cooling.")

    n.h2("5.9 Cold Cream")
    n.para("Cold cream is a water-in-oil (w/o) emulsion used as an emollient, cleansing and "
           "night cream. It gives a cooling sensation as the water slowly evaporates, and leaves "
           "an oily emollient film on the skin.")
    n.h3("Typical Formula")
    n.table(
        ["Ingredient", "Role"],
        [
            ["Beeswax", "Emulsifier (with borax) and stiffening agent."],
            ["Borax", "Reacts with the free fatty acids of beeswax to form the w/o emulsifier (soap)."],
            ["Liquid paraffin / Mineral oil", "Oil (external) phase and emollient."],
            ["Purified water", "Internal (dispersed) phase; gives the cooling effect."],
            ["Perfume & Preservative", "Fragrance and stability."],
        ],
        widths=[2.7, 3.8],
        fontsize=10.5,
    )
    n.h3("Preparation")
    n.para("Beeswax is melted in the liquid paraffin at ~70\u00b0C; borax is dissolved in water at "
           "the same temperature; the aqueous phase is added slowly to the oil phase with "
           "continuous stirring \u2013 borax and the free fatty acids of beeswax form the emulsifier, "
           "giving a w/o cream; it is stirred until cool and the perfume is added.")
    n.box("High-Yield", [
        "Vanishing cream = stearic-acid-based o/w cream (non-greasy).",
        "Cold cream = beeswax-borax w/o cream (greasy, cooling, emollient).",
        "Borax + beeswax free fatty acids form the emulsifying soap in cold cream.",
    ])

    n.h3("Evaluation of Creams (Common Tests)")
    n.bullets([
        "Type of emulsion (dye / dilution test), pH and viscosity.",
        "Physical stability \u2013 phase separation, centrifugation and freeze-thaw cycling.",
        "Spreadability, texture and greasiness.",
        "Globule size and homogeneity (microscopy).",
        "Microbial limits and preservative efficacy; skin-irritation test.",
    ])
    n.para("Creams are packed in wide-mouth glass or plastic jars, or in collapsible aluminium / "
           "laminated tubes; the container must protect against contamination and loss of water "
           "or perfume.")

    # ---------------------------------------------------- shampoo
    n.h2("5.10 Shampoo")
    n.para("A shampoo is a preparation of a surfactant (detergent) in a suitable form \u2013 liquid, "
           "gel or cream \u2013 used to remove sebum, dirt and styling residues from the hair and "
           "scalp while leaving the hair manageable and lustrous.")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Principal (primary) surfactant", "Detergency and foaming.", "Sodium lauryl sulphate, sodium laureth sulphate."],
            ["Secondary / auxiliary surfactant", "Improve foam, mildness, conditioning.", "Cocamidopropyl betaine, alkanolamides."],
            ["Conditioning agents", "Softness, manageability, anti-static.", "Cationic polymers (polyquaternium), silicones, lanolin."],
            ["Thickeners", "Adjust viscosity.", "Sodium chloride, CMC, carbomer."],
            ["Foam boosters / stabilisers", "Rich, stable foam.", "Lauryl / cocamide DEA."],
            ["Sequestering agent", "Prevent scum in hard water.", "EDTA."],
            ["Anti-dandruff actives", "Therapeutic.", "Zinc pyrithione, ketoconazole, selenium sulphide."],
            ["Others", "Appearance, safety, fragrance.", "Opacifiers, colour, perfume, preservative, pH adjuster."],
        ],
        widths=[1.9, 2.1, 2.5],
        fontsize=10,
    )
    n.h3("Types")
    n.para("Clear liquid, liquid cream (lotion / opaque), solid / cream, powder, anti-dandruff, "
           "conditioning ('2-in-1'), medicated and herbal shampoos.")
    n.h3("Evaluation")
    n.bullets([
        "Physical appearance, colour, odour and pH (mild, ~5\u20137).",
        "Foaming ability and foam stability.",
        "Percent solids content, viscosity and rheology.",
        "Detergency / cleaning action and wetting time.",
        "Surface tension, dirt-dispersion and eye-irritation (Draize) test.",
        "Conditioning performance (wet / dry combability) and microbial limits.",
    ])
    n.para("Shampoos are packed in squeeze plastic bottles with flip-top / disc-top closures, "
           "sachets, or pump dispensers; the container must be leak-proof and chemically "
           "compatible.")

    # ---------------------------------------------------- soaps & syndet
    n.h2("5.11 Soaps and Syndet Bars")
    n.para("Soaps are the sodium (hard soap) or potassium (soft soap) salts of long-chain fatty "
           "acids, produced by the saponification of oils / fats with an alkali. They are the "
           "classic cleansing agents but, being alkaline (pH ~9\u201310), can be harsh to the skin "
           "and form an insoluble scum in hard water.")
    n.h3("Manufacture of Soap")
    n.bullets([
        ("Saponification \u2013", "fats / oils are boiled with sodium hydroxide (the kettle / full-boiled process) to give soap and glycerin."),
        ("Neutralisation \u2013", "pre-formed fatty acids are neutralised with alkali (faster and more controlled)."),
        ("Finishing \u2013", "the soap is dried, milled with colour, perfume, superfatting agents and additives, then plodded, cut and stamped into bars."),
    ])
    n.h3("Syndet (Synthetic Detergent) Bars")
    n.para("Syndet bars are cleansing bars in which the cleansing agent is a synthetic "
           "surfactant (syndet = synthetic detergent) rather than, or in addition to, true soap "
           "(they contain less than about 10% true soap). Because their pH can be adjusted close "
           "to that of the skin (~5.5\u20137), they are milder, do not form a scum in hard water and "
           "are preferred for sensitive and dry skin.")
    n.table(
        ["Feature", "Soap", "Syndet bar"],
        [
            ["Active cleanser", "Fatty-acid salt (true soap)", "Synthetic surfactants (e.g. sodium cocoyl isethionate)"],
            ["pH", "Alkaline (~9\u201310)", "Near skin pH (~5.5\u20137)"],
            ["Behaviour in hard water", "Forms scum", "No scum"],
            ["Mildness", "Can be harsh / drying", "Milder; better for sensitive skin"],
        ],
        widths=[1.8, 2.3, 2.4],
        fontsize=10,
    )
    n.h3("Evaluation")
    n.bullets([
        "pH, moisture content and total fatty matter (TFM) \u2013 higher TFM = better quality soap.",
        "Free alkali / free fatty acid content.",
        "Foam volume and stability; hardness and wear (rate of consumption).",
        "Cleansing ability, mildness and skin-irritation test.",
        "Microbial limits.",
    ])
    n.para("Bars are wrapped in paper, laminated film or cartons to protect against loss of "
           "moisture, oxidation (rancidity) and perfume; liquid soaps are packed in pump / "
           "flip-top bottles.")

    deep5(n)

    n.box("Summary \u2013 Unit V", [
        "Lipstick base = waxes + oils + fats; eosin is the staining dye.",
        "Nail polish film former = nitrocellulose; solvent = ethyl / butyl acetate.",
        "Vanishing cream = stearic-acid o/w; cold cream = beeswax-borax w/o.",
        "Syndet bars are near skin pH (~5.5\u20137) and milder than alkaline soaps.",
        "TFM (total fatty matter) is a key quality parameter for soaps.",
    ])

    n.mcq_header("Unit V \u2013 Multiple Choice Questions")
    n.mcq("The film-forming agent in nail polish is :",
          ["Beeswax", "Nitrocellulose", "Titanium dioxide", "Castor oil"], 1)
    n.mcq("Cold cream is which type of emulsion ?",
          ["Oil-in-water (o/w)", "Water-in-oil (w/o)", "Multiple", "Micro-emulsion"], 1)
    n.mcq("Vanishing cream is based on :",
          ["Beeswax", "Stearic acid", "Liquid paraffin", "Cocoa butter"], 1)
    n.mcq("The staining dye commonly used in lipsticks is :",
          ["Eosin", "Amaranth", "Tartrazine", "Indigo"], 0)
    n.mcq("In cold cream, the emulsifier is formed by the reaction of borax with :",
          ["Stearic acid", "Free fatty acids of beeswax", "Glycerin", "Water"], 1)
    n.mcq("Total fatty matter (TFM) is an important quality parameter of :",
          ["Shampoo", "Soap", "Tooth powder", "Nail polish"], 1)
    n.mcq("Syndet bars have a pH close to :",
          ["2\u20133", "5.5\u20137 (skin pH)", "9\u201310", "12\u201313"], 1)
    n.mcq("A common abrasive in toothpaste is :",
          ["Calcium carbonate", "Sodium fluoride", "Glycerin", "Saccharin"], 0)
    n.mcq("The 'no-tears' quality of baby shampoo is achieved by using :",
          ["Strong anionic surfactants", "Mild non-ionic / amphoteric surfactants at eye-neutral pH",
           "High alkali", "Large amounts of perfume"], 1)
    n.mcq("Surfactants with high HLB values (8\u201318) are best suited to prepare :",
          ["w/o emulsions", "o/w emulsions", "Powders", "Suppositories"], 1)
    n.mcq("Which agent is added to shampoo to prevent scum formation in hard water ?",
          ["EDTA (sequestering agent)", "SLS", "Silicone", "Perfume"], 0)
    n.page_break()


# =====================================================================
#  QUICK REVISION
# =====================================================================
def revision(n):
    n.unit_title("Quick Revision \u2013 One-Liners")

    n.h2("Unit I \u2013 Preformulation")
    n.bullets([
        "Preformulation = characterisation of drug before formulation.",
        "Lipinski Rule of Five : MW \u2264 500, logP \u2264 5, HBD \u2264 5, HBA \u2264 10.",
        "Log P determined in n-octanol / water; measures lipophilicity.",
        "XRPD = definitive test for polymorphism; DSC gives melting point & transitions.",
        "Metastable / amorphous forms : higher solubility, lower stability.",
        "Anhydrous forms dissolve faster than hydrates (ampicillin).",
        "Flow : Carr's index & Hausner ratio (lower = better); angle of repose < 30\u00b0 = excellent.",
        "BCS II = low solubility / high permeability = dissolution-limited.",
    ])

    n.h2("Unit II \u2013 Additives & DoE")
    n.bullets([
        "Superdisintegrants : croscarmellose Na, crospovidone, sodium starch glycolate.",
        "Glidant = colloidal silica; lubricant = Mg stearate; chelator = EDTA.",
        "Co-processed excipients : Ludipress, Prosolv, Cellactose, StarLac.",
        "2^k factorial = k factors, 2 levels, 2^k runs; reveals interactions.",
        "Fractional factorial = screening; Box-Behnken / CCD = optimization (RSM).",
    ])

    n.h2("Unit III \u2013 Solubility & Dissolution")
    n.bullets([
        "Noyes-Whitney : dC/dt = DA(Cs \u2212 Ct)/hV.",
        "Solubility techniques : cosolvency, salt, complexation, solid dispersion, micellar solubilization, hydrotropy.",
        "Cyclodextrin = inclusion complex; PEG/PVP = solid-dispersion carriers.",
        "Sink condition = medium \u2265 3\u20135 \u00d7 saturation volume.",
        "USP I = basket, II = paddle, IV = flow-through; 37\u00b0C, 900 mL.",
        "IDR measured at constant surface area (Wood's apparatus).",
        "Level A IVIVC = point-to-point (highest).",
    ])

    n.h2("Unit IV \u2013 Product Stability")
    n.bullets([
        "First order : t\u00bd = 0.693/k, t\u2089\u2080 = 0.105/k.",
        "Zero order : t\u2089\u2080 = 0.1 C\u2080/k\u2080; suspensions = apparent zero order.",
        "Arrhenius : log k vs 1/T (slope = \u2212Ea/2.303R) \u2192 accelerated testing.",
        "pH-rate profile \u2192 pH of maximum stability.",
        "Hydrolysis & oxidation = major degradation routes.",
        "Shelf life = t\u2089\u2080 (10% degradation).",
        "ICH : long-term 25\u00b0C/60% RH, accelerated 40\u00b0C/75% RH \u00d7 6 months; Q1B = photostability.",
    ])

    n.h2("Unit V \u2013 Cosmetics")
    n.bullets([
        "Nail polish film former = nitrocellulose.",
        "Lipstick = waxes + oils + fats; dye = eosin.",
        "Vanishing cream = stearic acid o/w; cold cream = beeswax-borax w/o.",
        "TFM = quality parameter of soap; syndet pH ~5.5\u20137 (mild).",
        "HLB 3\u20136 = w/o emulsifier; 8\u201318 = o/w emulsifier.",
        "Toothpaste abrasive = CaCO\u2083 / dicalcium phosphate; fluoride = anticaries.",
    ])
    n.box("All the best !", [
        "Revise the highlighted \u2605 boxes and all formulae before the exam.",
        "Practise the numerical problems in Unit IV (kinetics / shelf life).",
    ], kind="NOTE")



# =====================================================================
#  DEEP-DIVE SECTIONS (expanded detail per unit)
# =====================================================================
def deep1(n):
    n.h2("1.10 Micromeritics and Bulk Characterisation (Detailed)")
    n.para("Micromeritics is the science and technology of small particles. Because the physical "
           "properties of a powdered drug depend heavily on particle size and packing, a "
           "detailed micromeritic characterisation is an essential part of preformulation.")

    n.h3("Particle-Size Analysis \u2013 Methods")
    n.table(
        ["Method", "Principle", "Approximate range"],
        [
            ["Sieving", "Mechanical separation through standard sieves.", "> 50 \u00b5m"],
            ["Optical microscopy", "Direct visual measurement of diameter (also gives shape).", "0.2 \u2013 100 \u00b5m"],
            ["Electron microscopy (SEM/TEM)", "Very fine particles and surface morphology.", "< 1 \u00b5m and below"],
            ["Sedimentation (Andreasen)", "Stokes' law \u2013 settling velocity vs size.", "1 \u2013 100 \u00b5m"],
            ["Coulter counter", "Change in electrical resistance as particles pass an orifice.", "0.5 \u2013 500 \u00b5m"],
            ["Laser diffraction", "Diffraction pattern of a laser beam by particles.", "0.1 \u2013 2000 \u00b5m"],
        ],
        widths=[1.9, 3.1, 1.5],
        fontsize=10.5,
    )
    n.para("The results are expressed as a particle-size distribution, and average diameters "
           "(number, surface, volume, and volume-surface / Sauter mean) are calculated. Particle "
           "size influences dissolution rate, content uniformity of low-dose drugs, flow, "
           "sedimentation of suspensions and, occasionally, the equilibrium solubility of very "
           "fine (< 1\u20132 \u00b5m) particles (Ostwald-Freundlich / Kelvin effect).")

    n.h3("Types of Density and Porosity")
    n.bullets([
        ("True density \u2013", "mass per unit volume of the solid material excluding all voids; measured by helium pycnometry."),
        ("Granule density \u2013", "includes intra-particulate pores but excludes inter-particulate voids; measured by mercury displacement."),
        ("Bulk density \u2013", "mass per unit bulk (untapped) volume including all voids."),
        ("Tapped density \u2013", "bulk density after tapping to the closest packing."),
    ])
    n.formula("Porosity (%) = [1 \u2212 (Bulk density / True density)] \u00d7 100")

    n.h3("Moisture Content and Hygroscopicity")
    n.para("Moisture affects flow, compaction, chemical stability (hydrolysis) and microbial "
           "growth. Moisture content is determined by loss on drying (LOD) or, more specifically "
           "for bound water, by the Karl Fischer titration. On the basis of moisture uptake at "
           "defined humidity, powders are classified as non-hygroscopic, slightly hygroscopic, "
           "moderately hygroscopic, very hygroscopic or deliquescent (dissolves in the water it "
           "absorbs).")

    n.h2("1.11 Solubility \u2013 Thermodynamics and Influencing Factors")
    n.para("Dissolution of a crystalline solid involves breaking the crystal lattice "
           "(endothermic) and solvation of the molecules by the solvent (exothermic). The net "
           "heat of solution and the entropy change determine the equilibrium solubility. For "
           "most drugs, dissolution is net endothermic, so solubility rises with temperature.")
    n.h3("Factors Affecting Solubility of a Drug")
    n.bullets([
        ("Molecular structure & polarity \u2013", "'like dissolves like'; polar drugs dissolve in polar solvents."),
        ("Crystal form \u2013", "amorphous > metastable polymorph > stable polymorph; anhydrate > hydrate."),
        ("Particle size \u2013", "very fine particles show slightly higher solubility (Ostwald-Freundlich)."),
        ("pH \u2013", "governs ionization and hence solubility of ionizable drugs."),
        ("Temperature \u2013", "usually increases solubility (endothermic dissolution)."),
        ("Nature of solvent & cosolvents \u2013", "dielectric constant / polarity."),
        ("Presence of other solutes \u2013", "common-ion effect, salting-in and salting-out."),
    ])

    n.h2("1.12 Preformulation Stability Screening")
    n.para("Early stability screening identifies the intrinsic degradation pathways of the drug "
           "and the conditions that must be controlled in the formulation. Small quantities of "
           "the drug are stressed and analysed by a stability-indicating method.")
    n.table(
        ["Stress condition", "Purpose"],
        [
            ["Solution stability across pH 1\u201312", "Identifies pH of maximum stability and hydrolytic susceptibility."],
            ["Thermal (50\u201380\u00b0C, dry)", "Detects thermal / solid-state degradation."],
            ["Humidity (75\u201390% RH)", "Detects hydrolysis and physical changes."],
            ["Oxidation (H\u2082O\u2082, O\u2082)", "Detects oxidative susceptibility \u2192 need for antioxidants."],
            ["Photolysis (UV / visible)", "Detects photolability \u2192 need for opaque packaging."],
        ],
        widths=[2.6, 3.9],
        fontsize=10.5,
    )

    n.h2("1.13 Salt Selection and Polymorph Implications (Detailed)")
    n.para("The choice of salt influences solubility, dissolution, hygroscopicity, stability, "
           "melting point and processability. An ideal salt has high solubility, good "
           "crystallinity, low hygroscopicity, adequate stability and a non-toxic counter-ion. "
           "The 'pKa rule' suggests that a stable salt normally requires a difference of at "
           "least about 3 units between the pKa of the acid and that of the base.")
    n.table(
        ["Property influenced by solid form", "Consequence for the product"],
        [
            ["Solubility & dissolution rate", "Bioavailability of poorly soluble drugs."],
            ["Melting point & hardness", "Milling, compaction and processing behaviour."],
            ["Hygroscopicity", "Physical/chemical stability and handling."],
            ["Chemical stability", "Shelf life and degradation."],
            ["Crystal habit", "Flow, packing and tableting (capping/lamination)."],
        ],
        widths=[3.0, 3.5],
        fontsize=10.5,
    )
    n.para("A change of polymorph on storage (e.g. conversion of a metastable form to the stable "
           "form) can reduce dissolution and cause a product to fail its specification; hence "
           "the intended form must be confirmed (XRPD/DSC) and controlled throughout the shelf "
           "life.")



def deep2(n):
    n.h2("2.7 Mechanisms of Action of Key Excipient Classes (Detailed)")

    n.h3("Diluents (Fillers)")
    n.para("Diluents provide the bulk needed to make a tablet or capsule of a practical size, "
           "especially for potent low-dose drugs. A good diluent is inert, compactible, "
           "free-flowing and non-hygroscopic. Soluble diluents (lactose, mannitol) aid "
           "dissolution and mouth-feel, while insoluble diluents (dibasic calcium phosphate) "
           "give hardness. Microcrystalline cellulose is a widely used diluent-binder for "
           "direct compression owing to its excellent compactibility and self-disintegrating "
           "property.")

    n.h3("Binders \u2013 Mechanism")
    n.para("Binders provide the cohesiveness that holds the powder particles together in a "
           "granule or tablet. They may be added as a dry powder (then activated by the "
           "granulating liquid) or as a solution (solution binders are more effective). During "
           "wet granulation, liquid bridges between particles are converted into solid bridges "
           "on drying. Over-addition of binder increases hardness but prolongs disintegration "
           "and can slow dissolution.")

    n.h3("Disintegrants \u2013 Mechanisms")
    n.para("Disintegrants promote the break-up of a tablet into smaller fragments in an aqueous "
           "environment, thereby increasing the surface area available for dissolution. They act "
           "by one or more of the following mechanisms :")
    n.bullets([
        ("Swelling \u2013", "the disintegrant absorbs water and swells, rupturing the tablet (e.g. starch, sodium starch glycolate)."),
        ("Wicking (capillary action) \u2013", "water is drawn into the tablet through capillary pores (e.g. microcrystalline cellulose)."),
        ("Deformation recovery \u2013", "particles deformed during compression return to their original shape on wetting."),
        ("Gas production \u2013", "effervescent mixtures release CO\u2082 (e.g. sodium bicarbonate + citric acid)."),
        ("Enzymatic action \u2013", "certain enzymes break binders (rarely used)."),
    ])
    n.para("Superdisintegrants (croscarmellose sodium, crospovidone, sodium starch glycolate) "
           "are highly efficient at low concentrations (2\u20138%) owing to rapid, high-capacity "
           "swelling and/or wicking.")

    n.h3("Lubricants, Glidants and Anti-adherents")
    n.para("Lubricants reduce friction between the tablet and the die wall during ejection and "
           "act at the boundary (boundary lubricants such as magnesium stearate) or as a fluid "
           "film. Being hydrophobic, boundary lubricants must be used in low concentration "
           "(0.25\u20131%) and blended for a limited time, otherwise they retard wetting, "
           "disintegration and dissolution. Glidants (colloidal silica) improve powder flow by "
           "reducing interparticulate friction, while anti-adherents (talc) prevent sticking to "
           "the punches.")

    n.h3("Functionality-Related Characteristics (FRCs)")
    n.para("Because the performance of an excipient depends not only on its chemical identity "
           "but also on its physical properties, pharmacopoeias now describe "
           "'functionality-related characteristics' \u2013 such as particle-size distribution, "
           "moisture, bulk/tapped density, specific surface area and degree of substitution \u2013 "
           "that must be controlled to ensure consistent performance from batch to batch.")

    n.h2("2.8 Design of Experiments \u2013 Effects, Model and ANOVA (Detailed)")
    n.para("The value of a factorial design lies in its ability to quantify the main effect of "
           "each factor and the interaction between factors. Consider a 2\u00b2 design with the "
           "measured responses shown below :")
    n.table(
        ["Run", "A", "B", "Response (Y)"],
        [
            ["(1)", "\u2212", "\u2212", "40"],
            ["a", "+", "\u2212", "60"],
            ["b", "\u2212", "+", "50"],
            ["ab", "+", "+", "80"],
        ],
        widths=[1.3, 1.4, 1.4, 2.0],
    )
    n.para(segments=[("Main effect of A ", True),
        ("= \u00bd [(a + ab) \u2212 ((1) + b)] = \u00bd [(60 + 80) \u2212 (40 + 50)] = \u00bd (140 \u2212 90) = +25.", )])
    n.para(segments=[("Main effect of B ", True),
        ("= \u00bd [(b + ab) \u2212 ((1) + a)] = \u00bd [(50 + 80) \u2212 (40 + 60)] = \u00bd (130 \u2212 100) = +15.", )])
    n.para(segments=[("Interaction AB ", True),
        ("= \u00bd [(ab + (1)) \u2212 (a + b)] = \u00bd [(80 + 40) \u2212 (60 + 50)] = \u00bd (120 \u2212 110) = +5.", )])
    n.para("A positive main effect means the response increases as the factor moves from its low "
           "to its high level. A non-zero interaction shows that the effect of one factor depends "
           "on the level of the other. These effects are used to build a predictive polynomial "
           "model :")
    n.formula("Y = b\u2080 + b\u2081X\u2081 + b\u2082X\u2082 + b\u2081\u2082X\u2081X\u2082 (+ quadratic terms for RSM)")
    n.para("The statistical significance of each term is judged by analysis of variance (ANOVA), "
           "using the F-test and p-values, and the adequacy of the model is judged by the "
           "coefficient of determination (R\u00b2). Contour and response-surface plots then guide the "
           "selection of the optimum and the design space.")

    n.h3("Other Experimental Designs")
    n.table(
        ["Design", "Use"],
        [
            ["Full factorial (2^k)", "Study of all main effects and interactions."],
            ["Fractional factorial", "Screening of many factors with fewer runs."],
            ["Plackett-Burman", "Screening of a large number of factors (main effects only)."],
            ["Central composite (CCD)", "Optimization / response surface (quadratic model)."],
            ["Box-Behnken", "Optimization with 3 levels, fewer runs than CCD."],
            ["Mixture (simplex) design", "When factors are proportions of a formulation summing to 100%."],
        ],
        widths=[2.0, 4.5],
        fontsize=10.5,
    )
    n.h3("Quality by Design (QbD) Terms")
    n.bullets([
        ("QTPP \u2013", "Quality Target Product Profile \u2013 the prospective summary of quality characteristics."),
        ("CQA \u2013", "Critical Quality Attribute \u2013 a property that must be within limits to ensure quality."),
        ("CPP \u2013", "Critical Process Parameter \u2013 a process variable affecting a CQA."),
        ("Design space \u2013", "the multidimensional combination of variables that assures quality."),
        ("Control strategy & continual improvement \u2013", "to keep the process within the design space."),
    ])



def deep3(n):
    n.h2("3.9 Solubilization Techniques \u2013 Comparison (Detailed)")
    n.para("Each solubility-enhancement technique has characteristic advantages and limitations "
           "that determine its suitability for a given drug and dosage form.")
    n.table(
        ["Technique", "Mechanism", "Advantages", "Limitations"],
        [
            ["Cosolvency", "Lowers medium polarity.", "Simple, cheap, effective.", "Precipitation on dilution; cosolvent toxicity."],
            ["Salt formation", "Ionized, more soluble species.", "Large increase in solubility & dissolution.", "Only for ionizable drugs; common-ion, pH shift."],
            ["Complexation", "Inclusion in cyclodextrin cavity.", "Improves solubility, stability, taste.", "Bulk, cost, limited cavity capacity."],
            ["Solid dispersion", "Amorphous / molecular dispersion.", "Large dissolution increase.", "Physical instability (recrystallisation)."],
            ["Micellar solubilization", "Partition into micelle core.", "Effective for very lipophilic drugs.", "Surfactant toxicity/taste; needs > CMC."],
            ["Hydrotropy", "Self-aggregation of hydrotrope.", "No organic solvent, water-based.", "Large amount of hydrotrope needed."],
        ],
        widths=[1.4, 1.7, 1.8, 1.6],
        fontsize=9.5,
    )

    n.h2("3.10 Hydrodynamics and Convective Diffusion")
    n.para("In a stirred dissolution vessel, drug transport across the diffusion layer is "
           "governed by both molecular diffusion and convection (bulk fluid movement). The "
           "thickness of the diffusion layer (h) decreases as the agitation (stirring) rate "
           "increases, thereby increasing the dissolution rate. For a rotating-disc system "
           "(constant surface area) the intrinsic dissolution rate is described by the Levich "
           "equation, which shows that the rate is proportional to the square root of the "
           "rotational speed. Hydrodynamics therefore strongly influence dissolution results and "
           "must be standardised (apparatus, rpm, vessel geometry, position).")

    n.h2("3.11 Dissolution Apparatus \u2013 Detailed Description")
    n.bullets([
        ("USP I (Rotating basket) \u2013", "the dosage form is placed in a cylindrical wire-mesh basket attached to a rotating shaft and immersed in the medium; useful for capsules and floating or disintegrating tablets."),
        ("USP II (Paddle) \u2013", "a paddle rotates in the medium and the dosage form rests at the bottom of the vessel; the most widely used apparatus for conventional tablets and capsules; a sinker may be used for floating forms."),
        ("USP III (Reciprocating cylinder) \u2013", "the sample is held in a glass cylinder that reciprocates vertically between rows of vessels containing different media; ideal for pH-change and extended-release studies."),
        ("USP IV (Flow-through cell) \u2013", "fresh medium is pumped continuously through a cell holding the sample; maintains true sink conditions and suits poorly soluble drugs, implants and suppositories."),
        ("USP V (Paddle over disc) \u2013", "for transdermal patches; the patch is held on a disc below the paddle."),
        ("USP VI (Rotating cylinder) \u2013", "for transdermal patches attached to a rotating cylinder."),
        ("USP VII (Reciprocating holder) \u2013", "sample holders reciprocate in small volumes; for extended-release and transdermal systems."),
    ])
    n.h3("Dissolution Medium and Test Conditions")
    n.para("The medium is chosen to reflect the physiological environment and to provide sink "
           "conditions \u2013 commonly 0.1 N HCl / simulated gastric fluid (pH 1.2), acetate buffer "
           "(pH 4.5) and phosphate buffer (pH 6.8), with surfactant added for poorly soluble "
           "drugs. The medium must be de-aerated (dissolved air bubbles cling to particles and "
           "affect results) and maintained at 37 \u00b1 0.5\u00b0C. The apparatus is periodically "
           "calibrated using USP calibrator tablets (e.g. prednisone \u2013 disintegrating, and "
           "salicylic acid \u2013 non-disintegrating).")

    n.h2("3.12 Kinetic Models of Drug Release")
    n.para("The corrected dissolution data are fitted to mathematical models; the model giving "
           "the best fit (highest R\u00b2) describes the release mechanism.")
    n.table(
        ["Model", "Equation (simplified)", "Interpretation"],
        [
            ["Zero order", "Q = k\u2080 t", "Constant release, independent of concentration (ideal CR)."],
            ["First order", "log Q = log Q\u2080 \u2212 kt/2.303", "Release proportional to amount remaining."],
            ["Higuchi", "Q = k\u2095 \u221at", "Diffusion-controlled release from a matrix."],
            ["Hixson-Crowell", "Q\u2080^\u2153 \u2212 Q\u209c^\u2153 = kt", "Release governed by change in surface area / erosion."],
            ["Korsmeyer-Peppas", "Mt/M\u221e = k t\u207f", "n indicates mechanism (Fickian vs anomalous transport)."],
        ],
        widths=[1.7, 2.4, 2.4],
        fontsize=9.5,
    )
    n.para("For the Korsmeyer-Peppas model applied to a cylindrical matrix, n \u2264 0.45 indicates "
           "Fickian (diffusion-controlled) release, 0.45 < n < 0.89 indicates anomalous "
           "(non-Fickian) transport, and n \u2265 0.89 indicates case-II (erosion / swelling) "
           "release.")

    n.h2("3.13 IVIVC \u2013 Methods and Applications (Detailed)")
    n.para("Establishing a Level A correlation usually requires the fraction of drug absorbed "
           "in-vivo to be estimated from plasma data by a deconvolution method and then plotted "
           "against the fraction dissolved in-vitro.")
    n.bullets([
        ("Wagner-Nelson method \u2013", "estimates the fraction absorbed for a one-compartment model (no need for i.v. data)."),
        ("Loo-Riegelman method \u2013", "estimates the fraction absorbed for a two-compartment model (requires i.v. data)."),
        ("Convolution \u2013", "predicts the plasma profile from the dissolution data using the model."),
    ])
    n.h3("Applications of IVIVC")
    n.bullets([
        "As a surrogate for bioequivalence studies (biowaivers), reducing human studies.",
        "To set clinically meaningful dissolution specifications.",
        "To support scale-up and post-approval changes (SUPAC).",
        "To aid formulation optimization during development.",
    ])
    n.para("The BCS-based biowaiver allows in-vivo bioequivalence studies to be waived for "
           "certain immediate-release products of BCS Class I (and, under conditions, Class III) "
           "drugs, provided they are rapidly and similarly dissolving \u2013 a direct application of "
           "solubility, permeability and dissolution science.")



def deep4(n):
    n.h2("4.11 Types of Stability")
    n.table(
        ["Type", "Meaning"],
        [
            ["Chemical", "Each active ingredient retains its chemical integrity and labelled potency."],
            ["Physical", "Appearance, palatability, uniformity, dissolution and suspendability are retained."],
            ["Microbiological", "Sterility or resistance to microbial growth is retained; preservatives remain effective."],
            ["Therapeutic", "The therapeutic effect remains unchanged."],
            ["Toxicological", "No significant increase in toxicity occurs."],
        ],
        widths=[1.7, 4.8],
        fontsize=10.5,
    )

    n.h2("4.12 Higher-Order and Complex Reactions")
    n.para("Although most drug degradations are zero or first order, more complex kinetics are "
           "sometimes encountered :")
    n.bullets([
        ("Second-order \u2013", "rate depends on the product of two reactant concentrations; 1/C vs t is linear."),
        ("Reversible reactions \u2013", "the drug degrades to a product that can revert (e.g. some epimerisations)."),
        ("Parallel reactions \u2013", "the drug degrades simultaneously by two or more pathways."),
        ("Consecutive reactions \u2013", "the degradation product itself degrades further."),
        ("Pseudo-order \u2013", "a higher-order reaction behaves as a lower order because one reactant is constant."),
    ])

    n.h2("4.13 Accelerated Stability \u2013 the Q10 Method")
    n.para("The Q10 value is the factor by which the reaction rate increases for every 10\u00b0C rise "
           "in temperature (typically 2\u20135, often assumed \u2248 3). It provides a quick estimate of "
           "the effect of temperature on shelf life without a full Arrhenius study :")
    n.formula("t\u2089\u2080 (T\u2082) = t\u2089\u2080 (T\u2081) / Q10^[(T\u2082 \u2212 T\u2081)/10]")
    n.box("Worked Example \u2013 Q10 estimate", [
        "A product has a shelf life of 6 months at 40\u00b0C. Estimate the shelf life at 25\u00b0C (Q10 = 3).",
        "Temperature difference = 40 \u2212 25 = 15\u00b0C.",
        "Factor = Q10^(15/10) = 3^1.5 \u2248 5.2.",
        "Shelf life at 25\u00b0C \u2248 6 months \u00d7 5.2 \u2248 31 months (~2.6 years).",
    ])
    n.box("Worked Example \u2013 zero-order shelf life", [
        "A suspension (100 mg/mL) degrades by zero order with k\u2080 = 0.5 mg mL\u207b\u00b9 month\u207b\u00b9.",
        "t\u2089\u2080 = 0.1 C\u2080 / k\u2080 = (0.1 \u00d7 100) / 0.5 = 20 months.",
        "So 10% is lost in 20 months.",
    ])

    n.h2("4.14 Strategies to Improve Stability")
    n.h3("Controlling Hydrolysis")
    n.bullets([
        "Formulate at the pH of maximum stability using a suitable buffer.",
        "Reduce water content (dry powders, non-aqueous or anhydrous vehicles).",
        "Use a less polar solvent / cosolvent to slow ionic hydrolysis.",
        "Complexation or a suspension of a poorly soluble salt to reduce dissolved (reactive) drug.",
        "Store at low temperature; supply as a powder for reconstitution.",
    ])
    n.h3("Controlling Oxidation")
    n.bullets([
        "Add antioxidants (BHA, BHT, tocopherol, ascorbic acid, sodium metabisulphite).",
        "Add chelating agents (EDTA, citric acid) to bind catalytic trace metals.",
        "Replace headspace air with nitrogen; use oxygen-impermeable packaging.",
        "Protect from light; control pH; avoid heavy-metal contamination.",
    ])

    n.h2("4.15 Photostability Testing (ICH Q1B)")
    n.para("Photostability testing confirms that light exposure does not cause unacceptable "
           "change. The sample is exposed to a total illumination of not less than 1.2 million "
           "lux-hours (visible) and an integrated near-UV energy of not less than 200 watt-hours "
           "per square metre. Two options are permitted for the light source \u2013 Option 1 uses a "
           "combined visible + UV source (e.g. an artificial daylight lamp) and Option 2 uses "
           "separate cool-white fluorescent and near-UV lamps. Chemical actinometry (e.g. the "
           "quinine actinometer) may be used to monitor the exposure.")

    n.h2("4.16 Physical Stability of Dosage Forms")
    n.bullets([
        ("Suspensions \u2013", "caking, crystal growth, change in particle size and re-dispersibility."),
        ("Emulsions \u2013", "creaming, coalescence, cracking and phase inversion."),
        ("Tablets \u2013", "changes in hardness, disintegration, dissolution, and moisture-related changes."),
        ("Semisolids \u2013", "bleeding, phase separation, change in consistency and drug crystallisation."),
    ])

    n.h2("4.17 Bracketing, Matrixing and the Container-Closure System")
    n.para("To reduce the number of samples tested, ICH Q1D permits reduced designs. In "
           "bracketing, only the extremes of a design factor (e.g. the smallest and largest "
           "container sizes or strengths) are tested. In matrixing, a selected subset of samples "
           "is tested at each time point, with different subsets at different points. The "
           "container-closure system is an essential part of stability, since it protects the "
           "product from moisture, oxygen and light; the possible migration of leachables from "
           "the container into the product must also be evaluated.")



def deep5(n):
    n.h2("5.12 Structure of Skin and Hair (Relevance to Cosmetics)")
    n.para("The skin consists of the outer epidermis (whose outermost layer, the stratum "
           "corneum, is the main barrier to water loss and penetration), the dermis (connective "
           "tissue, blood vessels, glands) and the subcutaneous fat. Moisturisers act on the "
           "stratum corneum by occlusion, humectancy and emolliency to reduce trans-epidermal "
           "water loss. A hair fibre consists of the outer cuticle (overlapping scales), the "
           "cortex (bulk, pigment) and sometimes a central medulla. Shampoos clean the hair and "
           "scalp, while conditioners smooth the cuticle and reduce static and tangling.")

    n.h2("5.13 Quantitative Example Formulae")
    n.h3("Cold Cream (representative %)")
    n.table(
        ["Ingredient", "% w/w", "Function"],
        [
            ["White beeswax", "15.0", "Emulsifier / stiffener"],
            ["Borax", "0.7", "Forms soap emulsifier with beeswax"],
            ["Liquid paraffin", "50.0", "Oil phase / emollient"],
            ["Purified water", "34.0", "Aqueous (internal) phase"],
            ["Perfume & preservative", "q.s.", "Fragrance / stability"],
        ],
        widths=[2.4, 1.2, 2.9],
        fontsize=10.5,
    )
    n.h3("Vanishing Cream (representative %)")
    n.table(
        ["Ingredient", "% w/w", "Function"],
        [
            ["Stearic acid", "15.0", "Base; partly saponified"],
            ["Potassium hydroxide", "0.7", "Saponifying alkali"],
            ["Glycerin", "8.0", "Humectant"],
            ["Purified water", "76.0", "Continuous phase"],
            ["Perfume & preservative", "q.s.", "Fragrance / stability"],
        ],
        widths=[2.4, 1.2, 2.9],
        fontsize=10.5,
    )
    n.h3("Clear Liquid Shampoo (representative %)")
    n.table(
        ["Ingredient", "% w/w", "Function"],
        [
            ["Sodium laureth sulphate", "40.0 (as supplied)", "Primary surfactant"],
            ["Cocamidopropyl betaine", "8.0", "Secondary / mild surfactant"],
            ["Cocamide DEA", "3.0", "Foam booster / thickener"],
            ["Sodium chloride", "q.s.", "Viscosity adjuster"],
            ["EDTA, preservative, perfume, colour", "q.s.", "Sequestrant / stability / aesthetics"],
            ["Purified water", "to 100", "Vehicle"],
        ],
        widths=[2.7, 1.4, 2.4],
        fontsize=10.5,
    )

    n.h2("5.14 Evaluation Methods \u2013 Described")
    n.bullets([
        ("Emulsion-type (dye) test \u2013", "a water-soluble dye colours the continuous phase uniformly only in an o/w emulsion; an oil-soluble dye does so for w/o."),
        ("Dilution test \u2013", "an emulsion is miscible with its external phase (o/w dilutes with water)."),
        ("Globule-size / microscopy \u2013", "smaller, uniform globules indicate a more stable emulsion."),
        ("Accelerated stability \u2013", "centrifugation and freeze-thaw cycling reveal creaming or cracking tendencies."),
        ("Spreadability \u2013", "measured by the area a fixed mass spreads under a fixed load, or by a slip-and-drag apparatus."),
        ("Rheology / viscosity \u2013", "assesses consistency, pourability and extrudability."),
        ("Foam test (Ross-Miles) \u2013", "measures foam volume and stability of shampoos and soaps."),
        ("Microbial challenge (preservative-efficacy) test \u2013", "confirms that the preservative system controls a deliberately added microbial load."),
    ])

    n.h2("5.15 Preservatives, Antioxidants and Packaging in Cosmetics")
    n.para("Because many cosmetics contain water and are used repeatedly, an effective "
           "preservative system (parabens, phenoxyethanol, benzyl alcohol, DMDM hydantoin) is "
           "essential to prevent microbial spoilage, while antioxidants (BHA, BHT, tocopherol) "
           "prevent rancidity of oils and fats. Packaging protects the product from "
           "contamination, moisture and light and provides convenient, tamper-evident, "
           "aesthetically pleasing delivery. Common packs include collapsible tubes, wide-mouth "
           "jars, squeeze and pump bottles, and lipstick/mascara containers with integral "
           "applicators; the material (glass, plastic, aluminium, laminate) is chosen for "
           "compatibility and barrier properties.")

    n.h2("5.16 Regulatory Note")
    n.para("In India, cosmetics are regulated under the Drugs and Cosmetics Act, 1940 and its "
           "Rules, which define a cosmetic, prohibit the use of certain colours and ingredients, "
           "and lay down labelling and manufacturing requirements. Products that make a "
           "therapeutic claim are treated as drugs and require the corresponding approvals.")



# =====================================================================
#  IMPORTANT QUESTIONS (for exams)
# =====================================================================
def important_questions(n):
    n.unit_title("Important Questions (University / Competitive Exams)")
    n.para("The following questions cover the frequently examined areas of this subject. "
           "Long-answer questions carry about 10 marks and short-answer / short-notes about "
           "5 marks.")

    n.h2("Unit I \u2013 Preformulation Studies")
    n.h3("Long-Answer Questions")
    n.numbered([
        "Define preformulation. Discuss its goals and describe the physicochemical parameters studied during preformulation.",
        "What is polymorphism ? Classify polymorphs and explain their pharmaceutical significance with examples.",
        "Explain the various methods used to evaluate powder flow properties.",
        "Discuss drug-excipient compatibility studies and the methods used to detect incompatibilities.",
    ])
    n.h3("Short Notes")
    n.numbered([
        "Lipinski's Rule of Five.", "Biopharmaceutics Classification System (BCS).",
        "Partition coefficient and its significance.", "Pseudopolymorphism.",
        "Carr's index and Hausner ratio.", "Structure modification (salt formation & prodrugs).",
    ])

    n.h2("Unit II \u2013 Formulation Additives")
    n.h3("Long-Answer Questions")
    n.numbered([
        "Classify formulation additives (excipients) with their functions and suitable examples.",
        "What is Design of Experiments ? Explain factorial design with the calculation of main effects and interaction for a 2\u00b2 design.",
        "Discuss the factors influencing the incorporation of additives and the new developments in excipient science.",
    ])
    n.h3("Short Notes")
    n.numbered([
        "Superdisintegrants.", "Co-processed excipients.", "Mechanisms of disintegrant action.",
        "Fractional factorial design.", "Quality by Design (QbD) terminology.",
    ])

    n.h2("Unit III \u2013 Solubility & Dissolution")
    n.h3("Long-Answer Questions")
    n.numbered([
        "Describe the various techniques used to improve the solubility of poorly soluble drugs.",
        "State the Noyes-Whitney equation and explain the factors influencing the dissolution rate.",
        "Describe the different USP dissolution test apparatus and their applications.",
        "Explain IVIVC and its levels of correlation.",
    ])
    n.h3("Short Notes")
    n.numbered([
        "Phase-solubility analysis.", "Solid dispersion.", "Hydrotropy.",
        "Sink vs non-sink conditions.", "Intrinsic dissolution rate.",
        "Biorelevant dissolution media.",
    ])

    n.h2("Unit IV \u2013 Product Stability")
    n.h3("Long-Answer Questions")
    n.numbered([
        "Explain zero-order and first-order degradation kinetics with their equations for half-life and shelf life.",
        "Describe the mechanisms of drug degradation with examples and methods to prevent them.",
        "Explain accelerated stability studies based on the Arrhenius equation.",
        "Discuss the ICH guidelines and storage conditions for stability testing.",
    ])
    n.h3("Short Notes")
    n.numbered([
        "Arrhenius equation.", "pH-rate profile.", "Q10 method.",
        "Shelf-life (t90) assignment.", "Photostability testing (ICH Q1B).",
        "Bracketing and matrixing.",
    ])

    n.h2("Unit V \u2013 Cosmetics")
    n.h3("Long-Answer Questions")
    n.numbered([
        "Describe the formulation, evaluation and packaging of a toothpaste (dentifrice).",
        "Explain the formulation and evaluation of cold cream and vanishing cream, and differentiate between them.",
        "Discuss the formulation, evaluation and packaging of a shampoo.",
        "Differentiate between soaps and syndet bars and describe the manufacture of soap.",
    ])
    n.h3("Short Notes")
    n.numbered([
        "Lipstick formulation.", "Nail polish (lacquer).", "Mascara.",
        "Baby-care products.", "HLB system.", "Total fatty matter (TFM).",
    ])
    n.page_break()


# =====================================================================
#  PRACTICE MCQ BANK
# =====================================================================
def mcq_bank(n):
    n.unit_title("Practice MCQ Bank (GPAT / NIPER Style)")
    n.para("Additional multiple-choice questions for rapid revision and competitive-exam "
           "practice. Answers are given with brief explanations.")

    n.mcq_header("Set A \u2013 Preformulation")
    n.mcq("The solubility of the completely unionized form of a drug is called :",
          ["Molar solubility", "Intrinsic solubility", "Apparent solubility", "Kinetic solubility"], 1)
    n.mcq("Which technique measures the heat of fusion and melting point of a solid ?",
          ["XRPD", "DSC", "HPLC", "Karl Fischer"], 1)
    n.mcq("Karl Fischer titration determines :",
          ["Assay", "Water (moisture) content", "pH", "Particle size"], 1)
    n.mcq("Helium pycnometry is used to measure :",
          ["Bulk density", "Tapped density", "True density", "Porosity only"], 2)
    n.mcq("Sauter mean diameter is a :",
          ["Number mean", "Volume-surface mean", "Length mean", "Weight mean"], 1)
    n.mcq("A deliquescent powder is one that :",
          ["Loses water", "Absorbs enough water to dissolve", "Never absorbs water", "Sublimes"], 1)
    n.mcq("The 'pKa rule' for stable salt formation suggests a minimum pKa difference of about :",
          ["1 unit", "2 units", "3 units", "6 units"], 2)
    n.mcq("Ostwald-Freundlich equation relates solubility to :",
          ["Temperature", "Particle size", "pH", "Viscosity"], 1)

    n.mcq_header("Set B \u2013 Additives & DoE")
    n.mcq("Microcrystalline cellulose primarily acts as a :",
          ["Lubricant", "Diluent-binder (direct compression)", "Glidant", "Colourant"], 1)
    n.mcq("Effervescent disintegration is based on the release of :",
          ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], 1)
    n.mcq("Plackett-Burman designs are mainly used for :",
          ["Optimization", "Screening many factors", "Stability", "Dissolution"], 1)
    n.mcq("A negative main effect of a factor indicates the response :",
          ["Increases with the factor", "Decreases as the factor goes low\u2192high",
           "Is unaffected", "Is always zero"], 1)
    n.mcq("CQA in QbD stands for :",
          ["Critical Quality Attribute", "Continuous Quality Assurance",
           "Chemical Quantitative Assay", "Controlled Quality Analysis"], 0)
    n.mcq("Boundary lubricants such as magnesium stearate are used in a concentration of about :",
          ["5\u201310%", "0.25\u20131%", "15\u201320%", "25\u201330%"], 1)

    n.mcq_header("Set C \u2013 Solubility & Dissolution")
    n.mcq("Above the CMC, a surfactant increases drug solubility by :",
          ["Salt formation", "Micellar solubilization", "Cosolvency", "Hydrotropy"], 1)
    n.mcq("The Levich equation shows intrinsic dissolution rate is proportional to :",
          ["Rotation speed", "Square root of rotation speed", "Temperature squared", "Viscosity"], 1)
    n.mcq("The Higuchi model describes drug release that is :",
          ["Zero order", "Diffusion-controlled (\u221at)", "First order", "Erosion only"], 1)
    n.mcq("In the Korsmeyer-Peppas model (cylinder), n \u2264 0.45 indicates :",
          ["Case-II transport", "Fickian diffusion", "Super case-II", "Zero order"], 1)
    n.mcq("USP apparatus IV is the :",
          ["Paddle", "Basket", "Flow-through cell", "Paddle over disc"], 2)
    n.mcq("The Wagner-Nelson method is used to estimate :",
          ["Fraction dissolved", "Fraction absorbed (one-compartment)",
           "Rate constant of degradation", "Partition coefficient"], 1)
    n.mcq("BCS-based biowaivers are most applicable to which class ?",
          ["Class I", "Class II", "Class IV", "None"], 0)
    n.mcq("Dissolution medium is de-aerated because dissolved air :",
          ["Increases solubility", "Forms bubbles that alter results",
           "Changes pH", "Adds nutrients"], 1)

    n.mcq_header("Set D \u2013 Product Stability")
    n.mcq("For a zero-order reaction, a plot of concentration vs time is :",
          ["Curved", "A straight line", "Exponential", "Sigmoidal"], 1)
    n.mcq("The slope of an Arrhenius plot equals :",
          ["\u2212Ea/R", "\u2212Ea/2.303R", "Ea/RT", "log A"], 1)
    n.mcq("A Q10 value of 3 means the rate increases how many fold per 10\u00b0C rise ?",
          ["2", "3", "10", "0.3"], 1)
    n.mcq("Tetracycline undergoes which type of degradation to epi-tetracycline ?",
          ["Hydrolysis", "Isomerization (epimerization)", "Oxidation", "Photolysis"], 1)
    n.mcq("Which is added to prevent metal-catalysed oxidation ?",
          ["EDTA", "Lactose", "Starch", "Talc"], 0)
    n.mcq("Long-term stability storage condition (ICH, temperate zone) is :",
          ["5\u00b0C", "25\u00b0C/60% RH", "40\u00b0C/75% RH", "60\u00b0C"], 1)
    n.mcq("Second-order reactions give a straight line when plotting :",
          ["C vs t", "log C vs t", "1/C vs t", "\u221aC vs t"], 2)

    n.mcq_header("Set E \u2013 Cosmetics")
    n.mcq("The cooling sensation of cold cream is due to :",
          ["Menthol", "Slow evaporation of water", "Alcohol", "Camphor"], 1)
    n.mcq("Which wax is combined with borax to emulsify cold cream ?",
          ["Carnauba wax", "Beeswax", "Paraffin wax", "Candelilla wax"], 1)
    n.mcq("An HLB value of 4 is typical of a :",
          ["o/w emulsifier", "w/o emulsifier", "Solubiliser", "Detergent"], 1)
    n.mcq("The main detergent in most shampoos is :",
          ["Cetyl alcohol", "Sodium lauryl/laureth sulphate", "Glycerin", "Lanolin"], 1)
    n.mcq("Anti-dandruff activity is provided by :",
          ["Zinc pyrithione", "Sodium chloride", "EDTA", "Perfume"], 0)
    n.mcq("Fluoride is added to toothpaste as a(n) :",
          ["Abrasive", "Anticaries agent", "Humectant", "Binder"], 1)
    n.mcq("The Ross-Miles test evaluates :",
          ["Viscosity", "Foam volume and stability", "pH", "Colour"], 1)
    n.mcq("Titanium dioxide in lipstick / nail polish acts as a :",
          ["Preservative", "Opacifier / white pigment", "Plasticizer", "Solvent"], 1)
    n.page_break()



# =====================================================================
#  ADDITIONAL TOPICS & NUMERICALS
# =====================================================================
def extra(n):
    n.unit_title("Additional Topics & Solved Numericals")

    # ---------------- Unit I extra
    n.h2("A. Preformulation \u2013 Additional Notes")
    n.h3("Applications of Preformulation Data")
    n.bullets([
        "Selection of the most appropriate salt and polymorphic form of the drug.",
        "Choice of the manufacturing process (wet/dry granulation vs direct compression).",
        "Selection of compatible excipients and a suitable packaging system.",
        "Prediction of shelf life and recommended storage conditions.",
        "Identification of the need for solubility-enhancement or stabilisation strategies.",
    ])
    n.h3("Solved Numerical \u2013 Degree of Ionization")
    n.box("Numerical 1 \u2013 Henderson-Hasselbalch (weak acid)", [
        "A weak acid drug (pKa = 4.4) is present in the intestinal fluid at pH 6.4. Find the ratio of ionized to unionized drug.",
        "pH = pKa + log ([ionized]/[unionized]).",
        "6.4 = 4.4 + log (ratio)  \u21d2  log (ratio) = 2  \u21d2  ratio = 100 : 1.",
        "So 100 parts ionized to 1 part unionized \u2013 highly ionized, favouring solubility.",
    ])
    n.box("Numerical 2 \u2013 Weak base", [
        "A weak base (pKa = 8.0) is in gastric fluid at pH 2.0. Find the ionized : unionized ratio.",
        "For bases : pH = pKa + log ([unionized]/[ionized]).",
        "2.0 = 8.0 + log ([unionized]/[ionized]) \u21d2 log = \u22126 \u21d2 unionized:ionized = 1:10\u2076.",
        "The base is almost completely ionized (and hence soluble) in the stomach.",
    ])

    # ---------------- Unit II extra
    n.h2("B. Formulation Additives \u2013 Specific Excipients")
    n.h3("Important Diluents and Binders")
    n.table(
        ["Excipient", "Notable features"],
        [
            ["Lactose (\u03b1-monohydrate, spray-dried, anhydrous)", "Common diluent; spray-dried grade is directly compressible; reducing sugar (Maillard risk with amines)."],
            ["Microcrystalline cellulose (MCC)", "Excellent dry binder / diluent; self-disintegrant; direct compression."],
            ["Dibasic calcium phosphate", "Insoluble diluent; good flow; abrasive to punches."],
            ["Mannitol", "Non-hygroscopic, negative heat of solution (cooling) \u2013 ideal for chewables/ODTs."],
            ["Povidone (PVP)", "Widely used solution binder; also solubiliser/solid-dispersion carrier."],
            ["HPMC", "Binder, film former and matrix former for sustained release."],
        ],
        widths=[2.4, 4.1],
        fontsize=10.5,
    )
    n.h3("Coating and Film-Formers")
    n.para("Coating protects the drug, masks taste/odour, improves appearance and controls "
           "release. Film coating uses polymers such as HPMC and ethylcellulose with a "
           "plasticizer (e.g. PEG, triethyl citrate), an opacifier (titanium dioxide), colour "
           "and a solvent/aqueous dispersion. Enteric coating (cellulose acetate phthalate, "
           "Eudragit L/S) resists gastric acid and dissolves in the intestine, protecting "
           "acid-labile drugs and the stomach.")

    # ---------------- Unit III extra
    n.h2("C. Solubility & Dissolution \u2013 Additional Notes")
    n.h3("Dissolution-Profile Comparison")
    n.para("Two dissolution profiles are compared by model-independent factors. The difference "
           "factor f\u2081 measures the percentage difference between the two curves at each point, "
           "and the similarity factor f\u2082 measures their closeness. For similarity, f\u2081 should be "
           "between 0 and 15 and f\u2082 between 50 and 100. These are widely used to justify "
           "formulation and manufacturing changes.")
    n.box("Numerical 3 \u2013 Noyes-Whitney interpretation", [
        "If the particle size of a drug is reduced so that its surface area (A) doubles, and all",
        "other terms in the Noyes-Whitney equation stay constant, the dissolution rate will :",
        "dC/dt \u221d A, so doubling A doubles the initial dissolution rate.",
        "This is the basis of micronization for BCS Class II drugs.",
    ])
    n.h3("Factors Governing Sink Conditions")
    n.para("Sink conditions are ensured by using a large volume of medium, adding a surfactant "
           "to raise the saturation solubility of poorly soluble drugs, using a flow-through "
           "(open) system, or periodically replacing the medium. Maintaining sink conditions is "
           "essential for meaningful, discriminating and in-vivo-relevant dissolution data.")

    # ---------------- Unit IV extra
    n.h2("D. Product Stability \u2013 Full Arrhenius Numerical")
    n.box("Numerical 4 \u2013 Arrhenius extrapolation", [
        "For a drug in solution the first-order rate constants are :",
        "k = 8.0 \u00d7 10\u207b\u00b3 h\u207b\u00b9 at 60\u00b0C (333 K) and k = 1.0 \u00d7 10\u207b\u00b3 h\u207b\u00b9 at 40\u00b0C (313 K).",
        "Step 1 : log(k\u2082/k\u2081) = (Ea/2.303R)(1/T\u2081 \u2212 1/T\u2082).",
        "log(8.0/1.0) = 0.903;  (1/313 \u2212 1/333) = 1.92 \u00d7 10\u207b\u2074 K\u207b\u00b9.",
        "Ea = (0.903 \u00d7 2.303 \u00d7 8.314) / (1.92 \u00d7 10\u207b\u2074) \u2248 90.1 kJ/mol.",
        "Step 2 : extrapolate to 25\u00b0C (298 K) using the Arrhenius equation \u2192 k\u2082\u2085 \u2248 1.5 \u00d7 10\u207b\u2074 h\u207b\u00b9.",
        "Step 3 : t\u2089\u2080 = 0.105 / k\u2082\u2085 \u2248 0.105 / (1.5 \u00d7 10\u207b\u2074) \u2248 700 h \u2248 29 days.",
    ])
    n.h3("Definitions \u2013 Dating Terms")
    n.bullets([
        ("Expiry / expiration date \u2013", "the date up to which the product meets specification if stored correctly."),
        ("Re-test date \u2013", "the date after which a drug substance must be re-examined before use."),
        ("Shelf life (t\u2089\u2080) \u2013", "the established time during which the product remains within specification."),
    ])

    # ---------------- Unit V extra
    n.h2("E. Cosmetics \u2013 Additional Notes")
    n.h3("Ideal Properties of Cosmetic Products")
    n.bullets([
        "Safe, non-toxic and non-irritant to skin, eyes and mucous membranes.",
        "Physically and chemically stable throughout the shelf life.",
        "Free from harmful microbial contamination (adequately preserved).",
        "Elegant in appearance, colour, odour and feel; easy and pleasant to apply.",
        "Compatible packaging that protects and dispenses the product conveniently.",
    ])
    n.h3("Dentifrice \u2013 Additional Points")
    n.para("The abrasive is the principal component of a dentifrice and its abrasivity is "
           "controlled (measured as Relative Dentin Abrasivity, RDA) so that plaque and stains "
           "are removed without eroding enamel or dentine. Fluoride (sodium fluoride, sodium "
           "monofluorophosphate, stannous fluoride) is the key anticaries agent, while "
           "potassium/strontium salts reduce dentinal sensitivity and pyrophosphates / triclosan "
           "give anti-tartar and antibacterial action.")
    n.h3("Tests for Emulsion Stability of Creams")
    n.bullets([
        ("Centrifugation \u2013", "accelerates creaming/separation; a stable cream shows no separation."),
        ("Freeze-thaw cycling \u2013", "stresses the emulsion through temperature extremes."),
        ("Accelerated storage \u2013", "at 40\u201345\u00b0C to predict long-term physical stability."),
        ("Globule-size analysis \u2013", "an increase in globule size over time indicates instability (coalescence)."),
    ])

    n.h2("F. Reference Textbooks")
    n.bullets([
        "The Theory and Practice of Industrial Pharmacy \u2013 Lachman, Lieberman & Kanig.",
        "Physical Pharmacy / Martin's Physical Pharmacy and Pharmaceutical Sciences.",
        "Remington : The Science and Practice of Pharmacy.",
        "Pharmaceutical Preformulation and Formulation \u2013 Mark Gibson.",
        "Harry's Cosmeticology; Poucher's Perfumes, Cosmetics and Soaps.",
        "ICH Q1A(R2) and Q1B stability guidelines.",
    ])
    n.page_break()



# =====================================================================
#  GLOSSARY
# =====================================================================
def glossary(n):
    n.unit_title("Glossary of Key Terms")
    n.para("A quick reference to the important terms used throughout this subject.")
    n.table(
        ["Term", "Meaning"],
        [
            ["Preformulation", "Characterisation of the physicochemical properties of a drug before formulation."],
            ["Intrinsic solubility (C\u2080)", "Solubility of the completely unionized form of a drug."],
            ["pKa", "The pH at which a drug is 50% ionized and 50% unionized."],
            ["Partition coefficient (log P)", "Ratio of drug concentration in octanol to that in water; a measure of lipophilicity."],
            ["Polymorphism", "Existence of a substance in more than one crystalline form."],
            ["Pseudopolymorphism", "Incorporation of solvent into the crystal lattice (solvates/hydrates)."],
            ["Enantiotropic polymorph", "Reversibly interconvertible forms with a transition point below the melting point."],
            ["Monotropic polymorph", "One form is metastable at all temperatures; conversion is irreversible."],
            ["Crystal habit", "External shape of a crystal."],
            ["Carr's index", "(Tapped\u2212Bulk)/Tapped \u00d7100; a measure of compressibility/flow."],
            ["Hausner ratio", "Tapped density / Bulk density; a measure of flow."],
            ["Angle of repose", "Maximum angle of a powder heap with the horizontal; indicates flow."],
            ["BCS", "Biopharmaceutics Classification System (solubility \u00d7 permeability)."],
            ["Excipient", "Any non-active component included in a dosage form."],
            ["Superdisintegrant", "Highly efficient disintegrant used in low concentration."],
            ["Co-processed excipient", "Two or more excipients combined at sub-particle level for multifunctionality."],
            ["Glidant", "Improves powder flow (e.g. colloidal silica)."],
            ["Lubricant", "Reduces die-wall friction (e.g. magnesium stearate)."],
            ["Factor / Level / Response", "Independent variable / its setting / the measured outcome in DoE."],
            ["Interaction", "When the effect of one factor depends on the level of another."],
            ["Design space", "Combination of variables that assures product quality (QbD)."],
            ["Cosolvency", "Increasing solubility by adding a water-miscible cosolvent."],
            ["Complexation", "Increasing solubility by forming a soluble complex (e.g. cyclodextrin)."],
            ["Solid dispersion", "Drug dispersed in an inert hydrophilic carrier in the solid state."],
            ["Micellar solubilization", "Solubilization of drug within surfactant micelles above the CMC."],
            ["Hydrotropy", "Solubility increase by a large amount of a highly soluble second solute."],
            ["Dissolution", "Process by which a solid goes into solution."],
            ["Noyes-Whitney equation", "dC/dt = DA(Cs\u2212Ct)/hV; describes dissolution rate."],
            ["Sink condition", "Medium volume \u2265 3\u20135 \u00d7 that needed to saturate; keeps gradient maximal."],
            ["Intrinsic dissolution rate", "Dissolution rate per unit constant surface area."],
            ["IVIVC", "In-vitro / in-vivo correlation."],
            ["Level A correlation", "Point-to-point in-vitro/in-vivo correlation (highest level)."],
            ["Biorelevant media", "Media simulating GI fluids (SGF, SIF, FaSSIF, FeSSIF)."],
            ["Zero-order kinetics", "Rate independent of concentration; C = C\u2080 \u2212 k\u2080t."],
            ["First-order kinetics", "Rate proportional to concentration; log C linear with time."],
            ["Half-life (t\u00bd)", "Time for concentration to fall by half."],
            ["Shelf life (t\u2089\u2080)", "Time for potency to fall to 90% (10% degradation)."],
            ["Arrhenius equation", "k = A\u00b7e^(\u2212Ea/RT); relates rate to temperature."],
            ["pH-rate profile", "Plot of log k vs pH; its minimum is the pH of maximum stability."],
            ["Q10", "Factor by which rate increases per 10\u00b0C rise in temperature."],
            ["ICH Q1A / Q1B", "Guidelines for stability testing / photostability testing."],
            ["HLB", "Hydrophilic-Lipophilic Balance of a surfactant (0\u201320)."],
            ["o/w and w/o emulsion", "Oil-in-water and water-in-oil emulsions."],
            ["Syndet", "Synthetic-detergent cleansing bar (skin-pH, mild)."],
            ["TFM", "Total Fatty Matter \u2013 quality parameter of soap."],
            ["Dentifrice", "A tooth-cleaning preparation (powder, paste or gel)."],
        ],
        widths=[2.1, 4.4],
        fontsize=10.5,
    )
    n.page_break()
