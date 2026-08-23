# -*- coding: utf-8 -*-
"""
Full content for:
Formulation Development of Pharmaceutical and Cosmetic Products (MPH204T)
M-Pharmacy (Pharmaceutics) - Semester II
"""


def build(n):
    syllabus(n)
    unit1(n)
    unit2(n)
    unit3(n)
    unit4(n)
    unit5(n)


# =====================================================================
#  SYLLABUS
# =====================================================================
def syllabus(n):
    n.h2("Syllabus : -")

    n.h3("Scope")
    n.para("This course is designed to impart knowledge and skills necessary to train the "
           "students on par with the routine of Industrial activities in R&D and F&D "
           "(Formulation & Development).")

    n.h3("Objectives")
    n.para("On completion of this course it is expected that students will be able to understand :")
    n.bullets([
        "The scheduled activities in a Pharmaceutical firm.",
        "The pre-formulation studies of pilot batches of pharmaceutical industry.",
        "The significance of dissolution and product stability.",
    ])

    n.h3("Unit I - Preformulation Studies")
    n.para("Molecular optimization of APIs (drug substances), crystal morphology and variations, "
           "powder flow, structure modification, drug-excipient compatibility studies, method "
           "of determination.")

    n.h3("Unit II - Formulation Additives")
    n.para("Study of different formulation additives, factors influencing their incorporation, "
           "formulation development and processing, new developments in excipient science. "
           "Design of experiments \u2013 factorial design for product and process development.")

    n.h3("Unit III - Solubility & Dissolution")
    n.para("Importance, experimental determination, phase-solubility analysis, pH-solubility "
           "profile, solubility techniques to improve solubility \u2013 cosolvency, salt formation, "
           "complexation, solid dispersion, micellar solubilization and hydrotropy. Theories and "
           "mechanisms of dissolution, in-vitro dissolution testing models \u2013 sink and non-sink, "
           "factors influencing dissolution, intrinsic dissolution studies, dissolution test "
           "apparatus \u2013 designs, dissolution testing for conventional and controlled release "
           "products, data handling and correction factor, biorelevant media, in-vitro and "
           "in-vivo correlations, levels of correlations.")

    n.h3("Unit IV - Product Stability")
    n.para("Degradation kinetics, mechanisms, stability testing of drugs and pharmaceuticals, "
           "factors influencing \u2013 media effects and pH effects, accelerated stability studies, "
           "interpretation of kinetic data (API & tablets), solid state stability and shelf life "
           "assignment, stability protocols, reports and ICH guidelines.")

    n.h3("Unit V - Cosmetics")
    n.para("Formulation, evaluation and packaging of the following cosmetic products : "
           "Dentifrices like tooth powders, pastes and gels; Manicure preparations like nail "
           "polish; Lipsticks; Eye lashes; Baby care products; Moisturizing cream, vanishing "
           "cream, cold cream; Shampoo; Soaps and syndet bars.")

    n.page_break()



# =====================================================================
#  UNIT I - PREFORMULATION STUDIES
# =====================================================================
def unit1(n):
    n.unit_title("Unit I - Preformulation Studies")

    n.para("Preformulation may be described as a stage of development during which the physical "
           "and chemical properties of a drug substance are characterised, alone and in "
           "combination with excipients, so that a stable, safe, effective and bioavailable "
           "dosage form can be designed. It is the first learning step in the rational "
           "development of a dosage form and is carried out before the actual formulation "
           "work begins.")

    n.h3("Goals / Objectives of Preformulation")
    n.bullets([
        "To establish the necessary physicochemical characteristics of a new drug substance.",
        "To determine its kinetic rate profile (stability).",
        "To establish its compatibility with common excipients.",
        "To generate data useful to the formulator in developing a stable and bioavailable dosage form that can be mass produced.",
        "To characterise the bulk drug so that manufacturing problems are anticipated and avoided.",
    ])

    n.h2("1. Molecular Optimization of APIs (Drug Substances)")
    n.para("Molecular optimization refers to the systematic modification and evaluation of a "
           "drug molecule (lead) to obtain the best balance of potency, selectivity, "
           "solubility, permeability, stability and manufacturability. During drug discovery "
           "and early development, a promising lead is optimized so that the final candidate "
           "(API) not only shows the desired pharmacological activity but also possesses "
           "acceptable biopharmaceutical and physicochemical properties for formulation.")

    n.h3("Key Molecular Properties Optimized")
    n.bullets([
        ("Aqueous solubility \u2013", "adequate solubility is essential for dissolution and oral absorption; poorly soluble candidates are optimized by salt selection, prodrug or structural changes."),
        ("Lipophilicity (log P / log D) \u2013", "governs membrane permeability and partitioning; an optimum (moderate) value is desired \u2013 too low limits permeation, too high limits solubility."),
        ("Ionization (pKa) \u2013", "influences solubility, dissolution, absorption and formulation pH; determined for optimum salt and pH selection."),
        ("Permeability \u2013", "ability to cross biological membranes, related to lipophilicity, molecular size and hydrogen bonding."),
        ("Chemical & metabolic stability \u2013", "resistance to hydrolysis, oxidation and first-pass metabolism."),
        ("Molecular weight and hydrogen-bond count \u2013", "governed by Lipinski's Rule of Five for good oral absorption."),
    ])

    n.h3("Lipinski's Rule of Five")
    n.para("Poor absorption or permeation is more likely when a molecule violates more than one "
           "of the following criteria :")
    n.bullets([
        "Molecular weight not more than 500 Da.",
        "Log P (calculated) not more than 5.",
        "Number of hydrogen-bond donors (OH + NH) not more than 5.",
        "Number of hydrogen-bond acceptors (N + O) not more than 10.",
    ], level=1)

    n.h3("Physicochemical Parameters Studied")
    n.h3("(a) Organoleptic Properties")
    n.para("Colour, odour and taste of the drug are recorded using descriptive terminology. "
           "These properties are important for patient acceptability; unpleasant taste or "
           "colour variation may require flavouring, colouring or coating. Colour is described "
           "as (e.g.) off-white, cream, tan; taste as tasteless, bitter, sweet; odour as "
           "pungent, aromatic, odourless.")

    n.h3("(b) Bulk Characterisation & Purity")
    n.para("The identity and purity of the bulk drug are confirmed by melting point, "
           "spectroscopic methods (UV, IR, NMR, Mass) and chromatography (HPLC, TLC, GC). "
           "Purity determination and detection of impurities/related substances is essential "
           "as impurities can affect stability and toxicity.")

    n.h3("(c) Solubility Analysis")
    n.para("Solubility is one of the most important preformulation parameters as a drug must be "
           "in solution to be absorbed. Key solubility studies include :")
    n.bullets([
        ("Intrinsic solubility (C0) \u2013", "the solubility of the unionized form of the drug, determined at a pH where it is completely unionized."),
        ("pKa determination \u2013", "the pH at which drug exists 50% ionized and 50% unionized; predicted from the Henderson-Hasselbalch equation and used to manipulate solubility."),
        ("pH-solubility profile \u2013", "solubility measured across a physiologically relevant pH range (1\u20138)."),
        ("Common-ion effect \u2013", "reduction of solubility of a slightly soluble salt by a common ion (e.g. hydrochloride salts in gastric HCl)."),
        ("Temperature effect \u2013", "solubility usually increases with temperature for endothermic dissolution."),
        ("Solubilization \u2013", "use of cosolvents, surfactants and complexation to improve solubility."),
    ])
    n.para(segments=[
        ("Henderson-Hasselbalch equations : ", True),
        ("For weak acids  pH = pKa + log ([ionized]/[unionized]);  "
         "for weak bases  pH = pKa + log ([unionized]/[ionized]). "
         "These relate the fraction ionized to pH and pKa and predict solubility and absorption "
         "at different sites of the GI tract.", ),
    ])

    n.h3("(d) Partition Coefficient (P) / log P")
    n.para("The partition coefficient is the ratio of the concentration of unionized drug "
           "distributed between an organic phase (usually n-octanol) and an aqueous phase at "
           "equilibrium :  P = C(octanol) / C(water). It is a measure of lipophilicity and "
           "correlates with membrane permeability and biological activity. Log P is commonly "
           "reported; log D refers to the distribution coefficient at a given pH accounting "
           "for ionization.")

    n.h3("(e) Dissociation Constant / Ionization")
    n.para("The dissociation constant (pKa) governs the degree of ionization at a given pH and "
           "therefore influences solubility, partitioning, absorption, salt formation and the "
           "choice of formulation pH. It is determined by potentiometric titration or "
           "spectrophotometry.")

    n.h2("2. Crystal Morphology and Variations")
    n.para("The solid state of a drug can exist in different physical forms which strongly "
           "influence solubility, dissolution rate, stability, flow and compressibility. The "
           "study of these forms is a critical part of preformulation.")

    n.h3("Crystal Habit")
    n.para("Crystal habit is the external shape (appearance) of a crystal, whereas the internal "
           "arrangement (lattice) may be the same. The same compound can crystallise into "
           "different habits depending on crystallisation conditions.")
    n.table(
        ["Crystal Habit", "Description / Example"],
        [
            ["Tabular", "Moderately expanded in two directions (flat plates)."],
            ["Platy / Flaky", "Flat, thin plate-like crystals."],
            ["Prismatic", "Column-like, elongated crystals."],
            ["Acicular", "Needle-like, slender crystals."],
            ["Bladed", "Flattened, blade-like elongated crystals."],
            ["Equant / Isometric", "Crystals with similar dimensions in all directions."],
        ],
        widths=[2.2, 4.3],
    )

    n.h3("Polymorphism")
    n.para("Polymorphism is the ability of a substance to exist in more than one crystalline "
           "form having the same chemical composition but different internal lattice "
           "arrangement. Different polymorphs differ in physical properties such as melting "
           "point, density, solubility, dissolution rate and stability, and hence can affect "
           "bioavailability and processing.")
    n.h3("Types of Polymorphs")
    n.bullets([
        ("Enantiotropic polymorph \u2013", "one form can be reversibly changed into another by varying temperature or pressure (a transition point exists below the melting point); the forms are interconvertible."),
        ("Monotropic polymorph \u2013", "one form is unstable at all temperatures and pressures below the melting point; the transformation is irreversible (only one form is stable)."),
    ])
    n.para(segments=[
        ("Metastable form : ", True),
        ("A polymorph that is not the most stable form has higher energy, higher solubility "
         "and faster dissolution, and is often preferred to improve bioavailability \u2013 but it "
         "may convert to the stable, less soluble form on storage, causing problems.", ),
    ])

    n.h3("Pseudopolymorphism (Solvates & Hydrates)")
    n.para("When solvent molecules are incorporated into the crystal lattice in a stoichiometric "
           "ratio, the crystals are called solvates (or hydrates when the solvent is water); "
           "this phenomenon is called pseudopolymorphism. Anhydrous forms generally show higher "
           "aqueous solubility and faster dissolution than their hydrated counterparts (e.g. "
           "anhydrous ampicillin dissolves faster than the trihydrate).")

    n.h3("Amorphous Form")
    n.para("In the amorphous state there is no long-range order (no defined lattice). Amorphous "
           "forms have higher internal energy, greater solubility and faster dissolution than "
           "crystalline forms, but they are thermodynamically unstable and tend to recrystallise "
           "on storage.")

    n.h3("Methods of Characterising Solid Forms")
    n.table(
        ["Method", "Property Determined"],
        [
            ["X-ray powder diffraction (XRPD)", "Definitive identification of crystalline forms and degree of crystallinity."],
            ["Differential Scanning Calorimetry (DSC)", "Melting point, polymorphic transitions, heats of fusion, purity."],
            ["Thermogravimetric Analysis (TGA)", "Loss of water/solvent (detects hydrates/solvates)."],
            ["Hot-stage microscopy", "Visual observation of melting and phase transitions."],
            ["IR / Raman spectroscopy", "Differences in bonding between polymorphs."],
            ["Solid-state NMR", "Molecular environment in different solid forms."],
            ["Scanning electron microscopy (SEM)", "Crystal habit, surface morphology, particle size."],
        ],
        widths=[2.9, 3.6],
    )

    n.h2("3. Powder Flow Properties")
    n.para("The flow of a powder is critical for accurate die filling in tableting and capsule "
           "filling, uniformity of dose and reproducible manufacturing. Poor flow leads to "
           "weight variation and content non-uniformity. Flow depends on particle size, shape, "
           "density, surface texture, moisture and cohesive forces.")

    n.h3("Parameters Governing Powder Flow")
    n.h3("(a) Bulk Density and Tapped Density")
    n.para("Bulk density is the mass of powder divided by the bulk (untapped) volume; tapped "
           "density is measured after mechanically tapping the container until no further "
           "volume change occurs. These are used to derive compressibility indices.")

    n.h3("(b) Carr's Compressibility Index and Hausner Ratio")
    n.para(segments=[
        ("Carr's Index (%) = [(Tapped density \u2212 Bulk density) / Tapped density] \u00d7 100.   ", ),
        ("Hausner Ratio = Tapped density / Bulk density.", ),
    ])
    n.para("Lower values indicate better flow. They are widely used indirect measures of "
           "flowability :")
    n.table(
        ["Carr's Index (%)", "Hausner Ratio", "Flow Character"],
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

    n.h3("(c) Angle of Repose (\u03b8)")
    n.para(segments=[
        ("The angle of repose is the maximum angle between the surface of a powder heap and the "
         "horizontal plane :  tan \u03b8 = h / r  (h = height, r = radius of the heap). "
         "Lower angles indicate better flow.", ),
    ])
    n.table(
        ["Angle of Repose (\u00b0)", "Flow Property"],
        [
            ["25 \u2013 30", "Excellent"],
            ["31 \u2013 35", "Good"],
            ["36 \u2013 40", "Fair (aid not needed)"],
            ["41 \u2013 45", "Passable (may hang up)"],
            ["46 \u2013 55", "Poor (agitation needed)"],
            ["56 \u2013 65", "Very poor"],
            ["> 66", "Very, very poor"],
        ],
        widths=[3.0, 3.5],
    )

    n.h3("(d) Particle Size and Shape")
    n.para("Very fine particles (< 100 \u00b5m) are cohesive and flow poorly, whereas coarse, "
           "spherical, free-flowing particles flow well. Particle size also affects dissolution, "
           "content uniformity and sedimentation. It is measured by sieving, microscopy, "
           "laser diffraction and Coulter counter methods.")

    n.h3("Methods to Improve Powder Flow")
    n.bullets([
        "Increasing particle size by granulation (wet or dry).",
        "Producing spherical particles by spray drying or spheronization.",
        "Adding glidants such as colloidal silicon dioxide or talc.",
        "Reducing moisture content (avoid liquid bridges).",
        "Adding lubricants such as magnesium stearate to reduce inter-particle friction.",
    ])

    n.h2("4. Structure Modification")
    n.para("When a drug candidate shows unfavourable physicochemical properties (poor solubility, "
           "instability, unpleasant taste or poor absorption), its molecular structure or solid "
           "form can be deliberately modified to improve these properties without altering the "
           "pharmacological action. Common approaches include :")

    n.h3("(a) Salt Formation")
    n.para("Converting an acidic or basic drug into a salt is the most common way to improve "
           "aqueous solubility and dissolution. Salt selection also improves stability, "
           "crystallinity, flow and hygroscopicity. Examples : sodium/potassium salts of acids, "
           "hydrochloride/sulphate salts of bases.")

    n.h3("(b) Prodrug Approach")
    n.para("A prodrug is a pharmacologically inactive derivative that is converted into the "
           "active drug in the body by enzymatic or chemical processes. Prodrugs are used to "
           "improve solubility, permeability, stability, taste and to achieve site-specific "
           "delivery (e.g. enalapril \u2192 enalaprilat; chloramphenicol palmitate for taste masking).")

    n.h3("(c) Complexation")
    n.para("Formation of inclusion complexes (e.g. with cyclodextrins) can increase apparent "
           "solubility, improve stability, mask taste and reduce irritation.")

    n.h3("(d) Change of Physical Form")
    n.para("Selecting a more soluble polymorph, an amorphous form, an anhydrate, or reducing "
           "particle size (micronization) modifies the effective properties of the same "
           "chemical entity.")

    n.h2("5. Drug\u2013Excipient Compatibility Studies")
    n.para("Excipients are added to a formulation for various functions, but they may interact "
           "physically or chemically with the drug, leading to loss of potency, change in "
           "appearance, or reduced bioavailability. Compatibility studies identify such "
           "interactions early so that incompatible excipients can be avoided and a stable "
           "formulation designed.")

    n.h3("Purpose")
    n.bullets([
        "To select excipients that are physically and chemically compatible with the drug.",
        "To detect potential interactions before large-scale formulation.",
        "To predict the stability of the final product and guide storage conditions.",
    ])

    n.h3("Methods of Determination")
    n.table(
        ["Method", "Principle / Use"],
        [
            ["Differential Scanning Calorimetry (DSC)",
             "Drug + excipient (1:1) mixture is scanned; appearance/disappearance/shift of endothermic or exothermic peaks indicates interaction. Rapid screening technique."],
            ["Thermogravimetric Analysis (TGA)",
             "Detects changes in weight loss pattern of mixtures indicating interaction."],
            ["Isothermal Stress Testing (IST)",
             "Drug-excipient blends stored at elevated temperature/humidity (e.g. 50\u201360\u00b0C, 75% RH) and analysed by HPLC/TLC for degradation."],
            ["Thin Layer Chromatography (TLC)",
             "Detects appearance of new spots (degradation products) indicating incompatibility."],
            ["HPLC",
             "Quantifies drug content and degradation products in stressed blends; most reliable."],
            ["FT-IR / Raman spectroscopy",
             "Shift or disappearance of characteristic functional-group bands indicates chemical interaction."],
            ["Vacuum / Fluorescence & visual",
             "Change in colour, caking, liquefaction, odour observed on storage."],
        ],
        widths=[2.6, 3.9],
    )

    n.h3("Common Types of Drug\u2013Excipient Interactions")
    n.bullets([
        ("Maillard reaction \u2013", "browning between amine drugs and reducing sugars such as lactose."),
        ("Acid\u2013base reactions \u2013", "between acidic and basic components."),
        ("Adsorption \u2013", "of drug onto excipients reducing availability."),
        ("Eutectic formation / liquefaction \u2013", "lowering of melting point causing sticking."),
        ("Oxidation, hydrolysis and complexation \u2013", "reducing potency."),
    ])

    n.h2("6. Method of Determination (Analytical Method Development)")
    n.para("A stability-indicating analytical method must be developed and validated during "
           "preformulation to accurately quantify the drug and its degradation products in the "
           "presence of excipients. Techniques commonly used include UV-Visible "
           "spectrophotometry (for assay and solubility studies) and HPLC (for assay, purity and "
           "stability studies). The method is validated for accuracy, precision, specificity, "
           "linearity, limit of detection, limit of quantitation and robustness before use.")

    n.h3("High-Yield Summary")
    n.bullets([
        "Preformulation characterises the drug before formulation to design a stable, bioavailable product.",
        "Solubility, pKa, partition coefficient and dissolution govern absorption.",
        "Polymorphism, pseudopolymorphism and amorphous forms affect solubility, stability and bioavailability.",
        "Powder flow is assessed by Carr's index, Hausner ratio and angle of repose.",
        "Drug-excipient compatibility is screened mainly by DSC, isothermal stress testing and HPLC/TLC.",
    ])

    n.page_break()



# =====================================================================
#  UNIT II - FORMULATION ADDITIVES
# =====================================================================
def unit2(n):
    n.unit_title("Unit II - Formulation Additives")

    n.para("Formulation additives (excipients) are substances other than the active "
           "pharmaceutical ingredient that are included in a dosage form. Although once "
           "considered inert, excipients are now known to influence the rate and extent of drug "
           "absorption, stability, manufacturability and patient acceptability. Their rational "
           "selection is therefore central to formulation development.")

    n.h3("Ideal Properties of an Excipient")
    n.bullets([
        "Physiologically inert and non-toxic.",
        "Physically and chemically stable and compatible with the drug and other excipients.",
        "Free from microbial load; acceptable to regulatory authorities.",
        "Should not interfere with bioavailability or with assay of the drug.",
        "Commercially available, economical and of consistent quality.",
        "Should not have an unacceptable taste, odour or colour.",
    ])

    n.h2("1. Study of Different Formulation Additives")
    n.para("Excipients are classified according to the function they perform in the dosage form. "
           "The major categories, their functions and examples are summarised below.")

    n.table(
        ["Additive (Function)", "Role", "Examples"],
        [
            ["Diluents / Fillers", "Add bulk to make a practical tablet/capsule size.",
             "Lactose, microcrystalline cellulose (MCC), dibasic calcium phosphate, mannitol, starch."],
            ["Binders / Adhesives", "Impart cohesiveness so granules/tablets hold together.",
             "PVP (povidone), starch paste, HPMC, gelatin, acacia."],
            ["Disintegrants", "Promote breakup of tablet/capsule into fragments in fluid.",
             "Starch, sodium starch glycolate, croscarmellose sodium, crospovidone."],
            ["Lubricants", "Reduce friction between granules and die wall; aid ejection.",
             "Magnesium stearate, stearic acid, sodium stearyl fumarate, talc."],
            ["Glidants", "Improve flow of powder/granules.",
             "Colloidal silicon dioxide (Aerosil), talc."],
            ["Anti-adherents", "Prevent sticking to punches/dies.",
             "Talc, magnesium stearate, cornstarch."],
            ["Coating agents", "Protect, mask taste, control release, improve appearance.",
             "HPMC, ethylcellulose, Eudragit polymers, sugar, shellac."],
            ["Colourants", "Improve appearance, aid identification.",
             "Approved dyes and lakes, iron oxides, titanium dioxide."],
            ["Sweeteners / Flavours", "Improve palatability of oral liquids/chewables.",
             "Sucrose, aspartame, saccharin, sorbitol; flavour oils."],
            ["Preservatives", "Prevent microbial growth in multi-dose liquids.",
             "Parabens, benzoic acid, benzalkonium chloride, sodium benzoate."],
            ["Antioxidants", "Prevent oxidative degradation of drug.",
             "BHA, BHT, ascorbic acid, sodium metabisulphite, tocopherol."],
            ["Surfactants / Wetting agents", "Reduce surface tension, aid wetting, solubilization.",
             "SLS, polysorbates (Tween), sorbitan esters (Span)."],
            ["Suspending / Viscosity agents", "Retard sedimentation; thicken.",
             "Sodium CMC, MC, xanthan gum, acacia, tragacanth, carbopol."],
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
    )

    n.h2("2. Factors Influencing Incorporation of Additives")
    n.para("The choice and quantity of an excipient are governed by several factors :")
    n.bullets([
        ("Nature of the drug \u2013", "solubility, dose, stability, particle size, hygroscopicity and compatibility with the additive."),
        ("Route of administration & dosage form \u2013", "oral, parenteral, topical requirements differ (e.g. sterility and tonicity for parenterals)."),
        ("Function required \u2013", "the specific role (binder, disintegrant, preservative, etc.) determines the class of additive."),
        ("Compatibility \u2013", "additive must not interact with drug or other excipients."),
        ("Regulatory acceptability \u2013", "must be listed/approved (GRAS, pharmacopoeial) with acceptable safety limits."),
        ("Physicochemical properties of additive \u2013", "flow, compressibility, particle size, moisture content."),
        ("Manufacturing process \u2013", "wet granulation, dry granulation or direct compression demand different excipient properties."),
        ("Cost and availability \u2013", "economical and consistently available material."),
        ("Organoleptic considerations \u2013", "taste, odour, colour affecting patient compliance."),
    ])

    n.h2("3. Formulation Development and Processing")
    n.para("Formulation development is the systematic process of converting a drug substance "
           "into a suitable dosage form. It integrates preformulation data, selection of "
           "excipients, choice of manufacturing process and optimization of the formula.")
    n.h3("General Stages")
    n.numbered([
        "Review of preformulation data (solubility, stability, flow, compatibility).",
        "Selection of the dosage form and target product profile.",
        "Selection of excipients and their concentrations.",
        "Selection of the manufacturing process (e.g. wet/dry granulation, direct compression).",
        "Preparation of trial (laboratory) batches and evaluation.",
        "Optimization of formula and process using Design of Experiments.",
        "Scale-up from laboratory to pilot to production scale.",
        "Stability studies and finalisation of the formulation.",
    ])
    n.h3("Common Processing Techniques for Solids")
    n.bullets([
        ("Wet granulation \u2013", "granulating powder with a binder solution; suits low-dose, poorly-flowing, moisture-stable drugs."),
        ("Dry granulation (slugging / roller compaction) \u2013", "for moisture- or heat-sensitive drugs."),
        ("Direct compression \u2013", "simple, economical; requires free-flowing, directly compressible excipients."),
    ])

    n.h2("4. New Developments in Excipient Science")
    n.para("To meet the demands of modern high-speed manufacturing (especially direct "
           "compression) and novel drug delivery, new and improved excipients have been "
           "developed :")
    n.bullets([
        ("Co-processed excipients \u2013", "two or more excipients combined at the sub-particle level to give a single multifunctional material with improved flow and compressibility (e.g. Ludipress, Cellactose, Prosolv, StarLac)."),
        ("Superdisintegrants \u2013", "highly efficient disintegrants used in low concentration for rapid disintegration, e.g. sodium starch glycolate, croscarmellose sodium, crospovidone \u2013 essential for orally disintegrating tablets."),
        ("Directly compressible excipients \u2013", "spray-dried lactose, MCC, dibasic calcium phosphate with good flow and binding."),
        ("Multifunctional excipients \u2013", "single material serving multiple roles (filler-binder-disintegrant)."),
        ("Novel excipients for modified release \u2013", "methacrylate copolymers (Eudragit), HPMC grades, polyethylene oxide."),
        ("Excipients for solubility enhancement \u2013", "cyclodextrins, poloxamers, novel surfactants."),
        ("Nanocarrier and lipid excipients \u2013", "for improving bioavailability of poorly soluble drugs."),
    ])

    n.h2("5. Design of Experiments (DoE) \u2013 Factorial Design")
    n.para("Design of Experiments is a structured, statistical approach to planning experiments "
           "so that the effect of several variables (factors) on a response can be studied "
           "simultaneously and efficiently. In formulation and process development, DoE is used "
           "to understand and optimize the relationship between formulation/process variables "
           "and product quality attributes with a minimum number of experiments.")

    n.h3("Limitation of the Traditional Approach (OFAT)")
    n.para("In the classical 'one-factor-at-a-time' (OFAT) method, only one variable is changed "
           "while the others are kept constant. This requires many experiments, cannot detect "
           "interactions between factors, and may miss the true optimum. DoE overcomes these "
           "drawbacks.")

    n.h3("Key Terminology")
    n.bullets([
        ("Factor \u2013", "an independent variable that is deliberately varied (e.g. binder concentration, compression force)."),
        ("Level \u2013", "the value/setting assigned to a factor (e.g. low and high), denoted \u2212 and +."),
        ("Response \u2013", "the measured outcome or dependent variable (e.g. hardness, disintegration time, drug release)."),
        ("Effect \u2013", "the change in response produced by changing the level of a factor."),
        ("Interaction \u2013", "when the effect of one factor depends on the level of another factor."),
        ("Runs / Trials \u2013", "the individual experiments performed."),
    ])

    n.h3("Factorial Design")
    n.para("A factorial design studies the effect of two or more factors, each at two or more "
           "levels, in all possible combinations. A design with 'k' factors each at 2 levels is "
           "called a 2^k factorial design and requires 2^k experimental runs.")

    n.para(segments=[("2\u00b2 Factorial Design (2 factors, 2 levels = 4 runs) : ", True)])
    n.table(
        ["Run", "Factor A", "Factor B", "Combination"],
        [
            ["1", "\u2013 (low)", "\u2013 (low)", "(1)"],
            ["2", "+ (high)", "\u2013 (low)", "a"],
            ["3", "\u2013 (low)", "+ (high)", "b"],
            ["4", "+ (high)", "+ (high)", "ab"],
        ],
        widths=[1.2, 1.9, 1.9, 1.5],
    )
    n.para("A 2\u00b3 factorial design (3 factors at 2 levels) requires 8 runs and allows the study "
           "of three main effects, three two-factor interactions and one three-factor "
           "interaction.")

    n.h3("Fractional Factorial Design")
    n.para("When the number of factors is large, a full factorial requires too many runs. A "
           "fractional factorial design studies only a carefully selected fraction "
           "(e.g. one half, 2^(k\u22121)) of the runs to screen the most important factors, at the "
           "cost of confounding some higher-order interactions.")

    n.h3("Response Surface Methodology & Optimization Designs")
    n.para("For optimization (finding the best combination), higher designs such as the central "
           "composite design and Box-Behnken design are used together with response surface "
           "methodology. These fit a mathematical (usually quadratic) model relating responses "
           "to factors and generate contour/response-surface plots to locate the optimum.")

    n.h3("Advantages of Factorial / DoE Approach")
    n.bullets([
        "Fewer experiments give more information than OFAT.",
        "Estimates the effect of each factor and, importantly, their interactions.",
        "Allows building of a predictive mathematical model.",
        "Enables true optimization and definition of a design space (Quality by Design).",
        "Economical in time, material and cost.",
    ])

    n.h3("Applications in Formulation")
    n.bullets([
        "Optimizing binder and disintegrant levels in tablets.",
        "Studying effect of process variables (compression force, granulation time) on tablet properties.",
        "Optimizing polymer levels in controlled-release formulations.",
        "Optimizing surfactant and oil ratios in emulsions/nanoemulsions.",
    ])

    n.page_break()



# =====================================================================
#  UNIT III - SOLUBILITY & DISSOLUTION
# =====================================================================
def unit3(n):
    n.unit_title("Unit III - Solubility & Dissolution")

    # -------------------------------------------------- Solubility
    n.h2("A. Solubility")
    n.para("Solubility is the maximum amount of a solute that dissolves in a given quantity of "
           "solvent at a specified temperature and pressure to form a saturated solution. It is "
           "commonly expressed quantitatively (mg/mL, molarity) or by descriptive pharmacopoeial "
           "terms.")

    n.h3("Importance of Solubility")
    n.bullets([
        "A drug must be dissolved (in solution) before it can be absorbed; solubility is a rate-limiting step for absorption of poorly soluble drugs.",
        "Governs the design of liquid dosage forms and the dose that can be delivered.",
        "Affects dissolution rate and hence bioavailability (BCS Class II and IV drugs).",
        "Influences formulation strategy (salt selection, solubilization techniques).",
    ])

    n.h3("Descriptive Solubility Terms (Pharmacopoeial)")
    n.table(
        ["Descriptive Term", "Parts of solvent per 1 part of solute"],
        [
            ["Very soluble", "Less than 1"],
            ["Freely soluble", "1 to 10"],
            ["Soluble", "10 to 30"],
            ["Sparingly soluble", "30 to 100"],
            ["Slightly soluble", "100 to 1000"],
            ["Very slightly soluble", "1000 to 10,000"],
            ["Practically insoluble", "More than 10,000"],
        ],
        widths=[2.8, 3.7],
    )

    n.h3("Experimental Determination of Solubility (Shake-Flask Method)")
    n.para("An excess of the drug is added to the solvent (of defined pH/temperature) in sealed "
           "vials which are shaken/rotated in a constant-temperature bath until equilibrium is "
           "reached (saturation). The supernatant is then filtered and the dissolved drug "
           "assayed (usually by UV or HPLC). Precautions include ensuring true equilibrium, "
           "maintaining constant temperature, preventing evaporation and confirming the solid "
           "form (no polymorphic conversion).")

    n.h3("Phase-Solubility Analysis")
    n.para("Phase-solubility analysis, introduced by Higuchi and Connors, studies the effect of "
           "an increasing concentration of a solubilizing/complexing agent (ligand) on the "
           "solubility of the drug. Increasing amounts of the ligand are added to a fixed excess "
           "of drug; after equilibrium the total dissolved drug is plotted against ligand "
           "concentration. It is used to determine the stoichiometry and stability constant of "
           "complexes and to assess purity.")
    n.para(segments=[("Types of phase-solubility diagrams : ", True)])
    n.bullets([
        ("Type A (soluble complexes) \u2013", "solubility increases with ligand; AL = linear, AP = positive deviation (higher-order complex), AN = negative deviation."),
        ("Type B (limited solubility complexes) \u2013", "BS = complex of limited solubility, BI = insoluble complex."),
    ])

    n.h3("pH-Solubility Profile")
    n.para("For ionizable drugs, solubility varies markedly with pH. A pH-solubility profile "
           "plots the total solubility of the drug against pH over the physiological range "
           "(usually 1\u20138). Weak acids show increasing solubility as pH rises above their pKa, "
           "while weak bases show increasing solubility as pH falls below their pKa. The profile "
           "guides salt selection, formulation pH and prediction of absorption along the GI tract.")

    n.h2("B. Techniques to Improve Solubility")
    n.para("Poorly water-soluble drugs (BCS Class II/IV) require solubility- and "
           "dissolution-enhancement techniques. The important approaches are :")

    n.h3("1. Cosolvency")
    n.para("A water-miscible cosolvent (e.g. ethanol, propylene glycol, glycerin, PEG 400) is "
           "added to water to reduce the polarity of the medium and increase the solubility of "
           "a poorly soluble non-polar drug. This is called cosolvency and the process is "
           "sometimes termed 'solvent blending'. It is simple and widely used for oral and "
           "parenteral liquids; care is needed to avoid precipitation on dilution and toxicity.")

    n.h3("2. Salt Formation")
    n.para("Converting a weak acid or base into an ionizable salt greatly increases aqueous "
           "solubility and dissolution rate (e.g. sodium salicylate, diclofenac sodium, "
           "hydrochloride salts of bases). Salt selection also improves stability and handling. "
           "The pH of the diffusion layer around the salt particle favours dissolution.")

    n.h3("3. Complexation")
    n.para("Formation of a soluble complex increases apparent solubility. Cyclodextrins "
           "(\u03b1-, \u03b2- and hydroxypropyl-\u03b2-cyclodextrin) form inclusion complexes in which the "
           "lipophilic drug molecule is entrapped within the hydrophobic cavity while the "
           "hydrophilic exterior confers water solubility. Complexation can also improve "
           "stability and mask taste.")

    n.h3("4. Solid Dispersion")
    n.para("A solid dispersion is a dispersion of one or more active ingredients in an inert "
           "hydrophilic carrier matrix in the solid state. The drug may be present as fine "
           "crystals, in the amorphous state, or molecularly dispersed, resulting in greatly "
           "increased surface area, improved wetting and faster dissolution.")
    n.para(segments=[("Types : ", True), ("simple eutectic mixtures, solid solutions, glass "
           "solutions/suspensions, and amorphous precipitations.", )])
    n.para(segments=[("Common carriers : ", True), ("PEG, PVP, HPMC, poloxamers, urea, mannitol.", )])
    n.para(segments=[("Methods of preparation : ", True), ("fusion (melting) method, solvent "
           "evaporation method, melting-solvent method, hot-melt extrusion and spray drying.", )])

    n.h3("5. Micellar Solubilization")
    n.para("Surfactants added above their critical micelle concentration (CMC) form micelles; "
           "poorly soluble drug molecules partition into the hydrophobic core of the micelles, "
           "increasing apparent solubility. This is called micellar solubilization "
           "(e.g. polysorbates, bile salts). It is used in liquid orals, parenterals and "
           "topical products.")

    n.h3("6. Hydrotropy")
    n.para("Hydrotropy is the increase in aqueous solubility of a poorly soluble solute brought "
           "about by the addition of a large amount of a second solute called a hydrotrope "
           "(e.g. sodium benzoate, sodium salicylate, urea, nicotinamide, sodium citrate). "
           "Hydrotropes are highly water-soluble compounds that enhance solubility by a "
           "self-aggregation/complexation mechanism; unlike surfactants they do not form true "
           "micelles.")

    n.h3("Other Approaches")
    n.bullets([
        ("Particle size reduction \u2013", "micronization and nanonization increase surface area and dissolution rate."),
        ("pH adjustment \u2013", "buffering the microenvironment to favour the ionized form."),
        ("Use of surfactants as wetting agents \u2013", "to improve wetting of hydrophobic powders."),
        ("Prodrug / structural modification.", ),
    ])

    # -------------------------------------------------- Dissolution
    n.h2("C. Dissolution")
    n.para("Dissolution is the process by which a solid substance goes into solution in a "
           "solvent. For solid oral dosage forms it is often the rate-determining step for drug "
           "absorption and is therefore a key quality-control and bioavailability parameter.")

    n.h3("Theories and Mechanisms of Dissolution")
    n.para(segments=[("(a) Diffusion-layer model (Noyes-Whitney / Nernst-Brunner) : ", True),
        ("the most widely accepted model. Dissolution occurs in two steps \u2013 rapid formation of "
         "a saturated stagnant layer (diffusion layer) at the solid surface, followed by "
         "diffusion of the dissolved drug across this layer into the bulk. The Noyes-Whitney "
         "equation describes the rate :", )])
    n.para(segments=[
        ("dC/dt = (D \u00b7 A / h \u00b7 V) (Cs \u2212 Ct)", True)], justify=False)
    n.para("where dC/dt = dissolution rate; D = diffusion coefficient; A = surface area of the "
           "dissolving solid; h = thickness of the diffusion layer; V = volume of dissolution "
           "medium; Cs = saturation solubility; Ct = concentration in the bulk at time t.")
    n.para(segments=[("(b) Danckwerts' (surface renewal) model : ", True),
        ("assumes that packets of fresh solvent continually reach and renew the solid surface, "
         "absorbing solute and carrying it into the bulk; there is no static diffusion layer.", )])
    n.para(segments=[("(c) Interfacial barrier (limited solvation) model : ", True),
        ("assumes the interfacial reaction (solvation) at the solid-liquid interface is the "
         "slow, rate-limiting step rather than diffusion.", )])

    n.h3("Factors Influencing Dissolution")
    n.para("Based on the Noyes-Whitney equation and practical experience, dissolution is "
           "affected by drug, formulation and apparatus factors :")
    n.bullets([
        ("Surface area (A) \u2013", "smaller particle size / larger surface area increases dissolution."),
        ("Solubility (Cs) \u2013", "polymorphic form, salt, amorphous state, pH and temperature increase Cs and rate."),
        ("Diffusion coefficient (D) & viscosity \u2013", "higher viscosity of medium lowers D and rate."),
        ("Diffusion-layer thickness (h) & agitation \u2013", "greater agitation reduces h and increases rate."),
        ("Volume of medium (V) & sink conditions \u2013", "maintaining sink conditions keeps (Cs \u2212 Ct) large."),
        ("Temperature \u2013", "increases solubility and diffusion, raising rate (test standardised at 37\u00b0C)."),
        ("Formulation factors \u2013", "binders, disintegrants, lubricants (hydrophobic lubricants retard), coating, hardness."),
        ("Wettability \u2013", "hydrophobic surfaces dissolve slowly; surfactants improve wetting."),
    ])

    n.h3("Intrinsic Dissolution Rate (IDR)")
    n.para("The intrinsic dissolution rate is the dissolution rate of a pure drug substance "
           "measured under conditions of constant surface area (usually a compressed disc of "
           "the pure drug in a die, e.g. Wood's apparatus). Because surface area is kept "
           "constant, IDR (expressed as mg/min/cm\u00b2) reflects the intrinsic properties of the "
           "drug (solubility, crystal form) independent of formulation. IDR values below "
           "~0.1 mg/min/cm\u00b2 usually indicate dissolution-rate-limited absorption.")

    n.h3("Sink and Non-Sink Conditions")
    n.bullets([
        ("Sink conditions \u2013", "the volume of dissolution medium is large enough (usually \u2265 3\u20135 times the volume required to saturate) that the dissolved drug concentration remains low (< 10\u201315% of saturation). This keeps the concentration gradient near maximum and mimics in-vivo dilution; it is the recommended condition for dissolution testing."),
        ("Non-sink conditions \u2013", "the drug concentration approaches saturation, the gradient falls and the dissolution rate slows; results may not reflect in-vivo behaviour."),
    ])

    n.h3("In-Vitro Dissolution Testing Models")
    n.para("In-vitro dissolution testing measures the amount of drug released from a dosage form "
           "into a defined medium over time. It is used for quality control, batch-to-batch "
           "consistency, formulation development, and as a surrogate for bioavailability. Models "
           "are broadly of two types : (i) closed-compartment (fixed volume, e.g. paddle and "
           "basket) and (ii) open/flow-through systems (continuous fresh medium, maintaining "
           "sink conditions).")

    n.h3("Dissolution Test Apparatus (USP) \u2013 Designs")
    n.table(
        ["Apparatus", "Name", "Typical Use"],
        [
            ["USP I", "Rotating basket", "Tablets, capsules (floating/disintegrating)."],
            ["USP II", "Paddle", "Tablets, capsules \u2013 most widely used."],
            ["USP III", "Reciprocating cylinder", "Modified/extended-release, pH change studies."],
            ["USP IV", "Flow-through cell", "Poorly soluble drugs, implants, sink conditions."],
            ["USP V", "Paddle over disc", "Transdermal patches."],
            ["USP VI", "Rotating cylinder", "Transdermal patches."],
            ["USP VII", "Reciprocating holder", "Extended-release, transdermals, small volumes."],
        ],
        widths=[1.2, 2.2, 3.1],
    )
    n.para("Standard conditions for apparatus I and II : medium volume 500\u2013900 mL (commonly "
           "900 mL), temperature 37 \u00b1 0.5 \u00b0C, basket usually 100 rpm and paddle usually "
           "50\u201375 rpm.")

    n.h3("Dissolution Testing : Conventional vs Controlled Release")
    n.bullets([
        ("Conventional (immediate-release) products \u2013", "a single-point specification is common (e.g. not less than a stated % dissolved in 30\u201345 minutes)."),
        ("Controlled/extended-release products \u2013", "multi-point (three or more) specifications are required to characterise the release profile (e.g. at 1, 4 and 8 h) to ensure neither dose dumping nor under-release, often using media of changing pH."),
    ])

    n.h3("Data Handling and Correction Factor")
    n.para("When samples are withdrawn during a dissolution test and replaced with fresh medium, "
           "the drug removed at each sampling point must be accounted for in the cumulative "
           "amount dissolved. A correction factor is applied to add back the quantity of drug "
           "removed in previous samples, so that the true cumulative percentage released is "
           "calculated. Data are then commonly analysed by model-dependent (zero-order, "
           "first-order, Higuchi, Korsmeyer-Peppas) and model-independent (f1 difference factor, "
           "f2 similarity factor) methods.")

    n.h3("Biorelevant Media")
    n.para("Biorelevant dissolution media simulate the composition of gastrointestinal fluids "
           "more closely than simple buffers, giving better in-vivo prediction, especially for "
           "poorly soluble drugs :")
    n.table(
        ["Medium", "Simulates"],
        [
            ["SGF (Simulated Gastric Fluid)", "Fasted stomach (pH ~1.2, with/without pepsin)."],
            ["SIF (Simulated Intestinal Fluid)", "Intestine (pH ~6.8, with/without pancreatin)."],
            ["FaSSIF", "Fasted-state simulated intestinal fluid (bile salts + lecithin, pH 6.5)."],
            ["FeSSIF", "Fed-state simulated intestinal fluid (higher bile salt, pH ~5.0)."],
        ],
        widths=[3.0, 3.5],
    )

    n.h2("D. In-Vitro / In-Vivo Correlation (IVIVC)")
    n.para("An in-vitro / in-vivo correlation is a predictive mathematical model describing the "
           "relationship between an in-vitro property of a dosage form (usually the extent or "
           "rate of drug dissolution) and a relevant in-vivo response (usually plasma drug "
           "concentration or amount absorbed). A good IVIVC allows dissolution testing to serve "
           "as a surrogate for bioequivalence studies, supporting formulation changes and "
           "reducing the need for human studies.")

    n.h3("Levels of Correlation")
    n.bullets([
        ("Level A \u2013", "point-to-point correlation between the entire in-vitro dissolution curve and the entire in-vivo absorption curve; the highest and most useful level."),
        ("Level B \u2013", "uses statistical moment analysis; the mean in-vitro dissolution time is compared with the mean in-vivo residence/dissolution time. It is not a point-to-point correlation."),
        ("Level C \u2013", "a single-point correlation relating one dissolution parameter (e.g. % dissolved at one time) to one pharmacokinetic parameter (e.g. Cmax or AUC); the weakest level."),
        ("Multiple Level C \u2013", "relates dissolution at several time points to one or more PK parameters."),
    ])

    n.h3("High-Yield Summary")
    n.bullets([
        "Solubility techniques: cosolvency, salt formation, complexation, solid dispersion, micellar solubilization, hydrotropy.",
        "Noyes-Whitney equation governs dissolution rate; sink conditions keep the gradient maximal.",
        "USP II (paddle) and USP I (basket) are the standard apparatus; 37\u00b0C, 900 mL.",
        "Level A IVIVC is the highest, point-to-point correlation.",
    ])

    n.page_break()



# =====================================================================
#  UNIT IV - PRODUCT STABILITY
# =====================================================================
def unit4(n):
    n.unit_title("Unit IV - Product Stability")

    n.para("Stability is defined as the capacity of a drug product to retain its physical, "
           "chemical, microbiological, therapeutic and toxicological properties within "
           "specified limits throughout its shelf life. Stability studies establish how the "
           "quality of a drug substance or product varies with time under the influence of "
           "environmental factors and are used to assign the shelf life (expiry date) and "
           "recommended storage conditions.")

    n.h3("Importance of Stability Studies")
    n.bullets([
        "To ensure safety and efficacy of the product up to the labelled expiry date.",
        "To establish the shelf life and recommended storage conditions.",
        "To select a stable formulation, packaging and container-closure system.",
        "To satisfy regulatory (ICH) requirements for product registration.",
    ])

    n.h2("1. Degradation (Reaction) Kinetics")
    n.para("Chemical stability is studied using reaction kinetics, which describes the rate at "
           "which a drug degrades and the order of that reaction. The order of a reaction is the "
           "way in which the reaction rate depends on the concentration of the reactant(s).")

    n.h3("Zero-Order Kinetics")
    n.para("The rate of degradation is independent of the concentration of the reactant "
           "(constant rate). Suspensions and many solid dosage forms often degrade by apparent "
           "zero order.")
    n.bullets([
        ("Rate equation :", "C = C0 \u2212 k0 t   (a plot of concentration vs time is linear)."),
        ("Units of k0 :", "concentration / time (e.g. mg/mL per hour)."),
        ("Half-life :", "t\u00bd = C0 / 2k0  (depends on initial concentration)."),
        ("Shelf life (t90) :", "t90 = 0.1 C0 / k0."),
    ], level=1)

    n.h3("First-Order Kinetics")
    n.para("The rate of degradation is directly proportional to the concentration of the "
           "reactant. Most solution-phase drug degradations follow first-order (or pseudo-first "
           "order) kinetics.")
    n.bullets([
        ("Rate equation :", "log C = log C0 \u2212 (k t / 2.303)  (log C vs time is linear)."),
        ("Units of k :", "reciprocal time (e.g. per hour)."),
        ("Half-life :", "t\u00bd = 0.693 / k  (independent of initial concentration)."),
        ("Shelf life (t90) :", "t90 = 0.105 / k."),
    ], level=1)

    n.h3("Pseudo-Zero and Pseudo-First Order")
    n.para("In suspensions, the drug in solution degrades by first order but is continuously "
           "replenished from the solid, so the concentration in solution stays constant and the "
           "loss appears as zero order (pseudo-zero order). When one reactant (e.g. water) is in "
           "large excess and effectively constant, a second-order reaction behaves as "
           "pseudo-first order.")

    n.h2("2. Mechanisms of Degradation")
    n.table(
        ["Mechanism", "Description / Example"],
        [
            ["Hydrolysis",
             "Reaction with water cleaving ester/amide bonds; the commonest route (e.g. aspirin, procaine, penicillins). Catalysed by H+/OH\u2212."],
            ["Oxidation",
             "Loss of electrons / reaction with oxygen forming free radicals; affects phenols, catecholamines, vitamins (e.g. adrenaline, ascorbic acid). Controlled by antioxidants, chelators, inert gas."],
            ["Photolysis",
             "Light (UV) induced degradation (e.g. nifedipine, riboflavin, sodium nitroprusside). Controlled by amber glass / opaque packaging."],
            ["Reduction",
             "Gain of electrons; less common."],
            ["Racemization",
             "Conversion of an active enantiomer into its inactive/less active isomer (e.g. adrenaline)."],
            ["Isomerization",
             "Conversion to an isomer of different activity (e.g. tetracycline to epi-tetracycline)."],
            ["Decarboxylation",
             "Loss of CO2 from carboxylic acids (e.g. p-aminosalicylic acid)."],
            ["Polymerization",
             "Combination of molecules to form larger units (e.g. ampicillin concentrated solutions)."],
        ],
        widths=[1.8, 4.7],
    )

    n.h2("3. Factors Influencing Stability")
    n.h3("(a) Temperature")
    n.para("An increase in temperature generally accelerates degradation. The relationship is "
           "described by the Arrhenius equation, which is the basis of accelerated stability "
           "testing :")
    n.para(segments=[("k = A \u00b7 e^(\u2212Ea/RT)     or     log k = log A \u2212 Ea / (2.303 RT)", True)],
           justify=False)
    n.para("where k = rate constant, A = frequency factor, Ea = energy of activation, "
           "R = gas constant, T = absolute temperature. A plot of log k against 1/T "
           "(Arrhenius plot) is linear and allows prediction of the rate constant at room "
           "temperature from data obtained at elevated temperatures.")

    n.h3("(b) pH Effect")
    n.para("Hydrolysis and many other reactions are catalysed by hydrogen and hydroxyl ions "
           "(specific acid-base catalysis) and by buffer species (general acid-base catalysis). "
           "A plot of the logarithm of the degradation rate constant against pH gives the "
           "pH-rate profile, from which the pH of maximum stability (the minimum of the curve) "
           "is identified and used to select the formulation pH / buffer.")

    n.h3("(c) Media / Solvent Effects")
    n.para("The nature of the solvent (dielectric constant, polarity), ionic strength and the "
           "presence of buffer salts influence the rate of degradation. Changing to a "
           "less polar solvent or a cosolvent system can slow ionic degradation reactions; "
           "increasing ionic strength can accelerate or retard reactions depending on the "
           "charges of the reacting species (primary salt effect).")

    n.h3("(d) Other Factors")
    n.bullets([
        ("Light \u2013", "photolabile drugs need amber/opaque packaging."),
        ("Oxygen \u2013", "oxidation controlled by antioxidants, chelating agents and nitrogen purging."),
        ("Moisture / humidity \u2013", "promotes hydrolysis and microbial growth; controlled by desiccants and moisture-proof packing."),
        ("Excipients & container \u2013", "incompatible excipients or leachables from the container may catalyse degradation."),
    ])

    n.h2("4. Accelerated Stability Studies")
    n.para("Because real-time shelf-life determination would take years, accelerated stability "
           "studies subject the product to elevated temperature (and humidity) to speed up "
           "degradation. Using the Arrhenius relationship, the rate constant at these stress "
           "conditions is extrapolated to normal storage temperature to predict the shelf life "
           "in a much shorter time.")
    n.h3("General Procedure")
    n.numbered([
        "Store the product at several elevated temperatures (e.g. 40, 50, 60\u00b0C).",
        "Withdraw samples at intervals and assay the intact drug.",
        "Determine the order of reaction and rate constant (k) at each temperature.",
        "Plot log k against 1/T (Arrhenius plot).",
        "Extrapolate to obtain k at room temperature (25\u00b0C).",
        "Calculate shelf life (t90) from the room-temperature rate constant.",
    ])

    n.h2("5. Interpretation of Kinetic Data (API & Tablets)")
    n.para("The assay data (concentration vs time) obtained at each temperature are plotted "
           "according to different orders; the plot giving the best straight line indicates the "
           "order and its slope gives the rate constant. For an API in solution first-order "
           "plots (log C vs t) are usually linear, whereas for tablets and suspensions the loss "
           "of potency frequently follows apparent zero-order kinetics. From the "
           "room-temperature rate constant the t90 (time for 10% degradation) is calculated and "
           "assigned as the shelf life. Care is required because solid-state reactions may not "
           "obey simple Arrhenius behaviour (moisture, phase changes and multiple mechanisms).")

    n.h2("6. Solid-State Stability")
    n.para("Degradation in the solid state (drug substance, tablets, powders) is generally "
           "slower and more complex than in solution. It is influenced by moisture, temperature, "
           "polymorphic transitions, particle size and the presence of excipients. Reactions "
           "often occur at the solid surface or in adsorbed moisture films and may follow "
           "topochemical or sigmoidal kinetics rather than simple order. Solid-state stability "
           "is studied by storing the solid under stress (temperature/humidity) and monitoring "
           "assay, appearance, dissolution and degradation products.")

    n.h2("7. Shelf-Life Assignment")
    n.para("The shelf life (expiration dating period) is the time during which the product "
           "remains within its approved specifications under recommended storage conditions. It "
           "is commonly taken as t90 \u2013 the time for the drug content to fall to 90% of its "
           "labelled amount (i.e. 10% degradation) \u2013 provided degradation products remain within "
           "safe limits. It is determined from real-time data (confirmed) and supported by "
           "accelerated data (predictive), and is stated with the appropriate storage statement.")

    n.h2("8. Stability Protocols and Reports")
    n.para("A stability protocol is a pre-approved written plan that defines how the study will "
           "be conducted. A stability report summarises and interprets the data obtained.")
    n.h3("A Stability Protocol Typically Specifies")
    n.bullets([
        "Product details, batch number, container-closure system and number of batches (usually at least 3).",
        "Storage conditions (long-term, intermediate, accelerated) and orientation.",
        "Testing time points (e.g. 0, 3, 6, 9, 12, 18, 24, 36 months).",
        "Tests to be performed (assay, related substances, dissolution, appearance, pH, moisture, microbial limits).",
        "Analytical methods (validated, stability-indicating) and acceptance criteria.",
    ])

    n.h2("9. ICH Guidelines for Stability Testing")
    n.para("The International Council for Harmonisation (ICH) Q1 series harmonises stability "
           "requirements worldwide :")
    n.table(
        ["Guideline", "Subject"],
        [
            ["Q1A(R2)", "Stability testing of new drug substances and products."],
            ["Q1B", "Photostability testing."],
            ["Q1C", "Stability testing of new dosage forms."],
            ["Q1D", "Bracketing and matrixing designs."],
            ["Q1E", "Evaluation of stability data (shelf-life extrapolation)."],
            ["Q1F", "Stability data for zones III and IV (hot/humid)."],
        ],
        widths=[1.6, 4.9],
    )
    n.h3("Climatic Zones and Storage Conditions")
    n.para("The world is divided into four climatic zones; India falls in Zone IVb (hot and very "
           "humid). ICH Q1A recommended storage conditions are :")
    n.table(
        ["Study", "Condition", "Minimum Period"],
        [
            ["Long-term", "25\u00b0C \u00b1 2\u00b0C / 60% RH \u00b1 5% (or 30\u00b0C/65% RH for Zone IV)", "12 months"],
            ["Intermediate", "30\u00b0C \u00b1 2\u00b0C / 65% RH \u00b1 5%", "6 months"],
            ["Accelerated", "40\u00b0C \u00b1 2\u00b0C / 75% RH \u00b1 5%", "6 months"],
        ],
        widths=[1.5, 3.6, 1.4],
    )
    n.para("A significant change at accelerated conditions (e.g. 5% loss of assay, exceeding "
           "specification for degradation products, or failure of dissolution/physical "
           "attributes) triggers testing at the intermediate condition. Q1B photostability uses "
           "defined visible and UV light exposures.")

    n.h3("High-Yield Summary")
    n.bullets([
        "First order: t\u00bd = 0.693/k, t90 = 0.105/k; zero order: t90 = 0.1C0/k0.",
        "Hydrolysis and oxidation are the two major degradation routes.",
        "Arrhenius equation underlies accelerated testing; pH-rate profile gives pH of maximum stability.",
        "Shelf life = t90 (time for 10% degradation).",
        "ICH Q1A(R2): long-term 25\u00b0C/60% RH, accelerated 40\u00b0C/75% RH for 6 months.",
    ])

    n.page_break()



# =====================================================================
#  UNIT V - COSMETICS
# =====================================================================
def unit5(n):
    n.unit_title("Unit V - Cosmetics")

    n.para("This unit deals with the formulation, evaluation and packaging of important cosmetic "
           "and cosmeceutical products. For each product the essential ingredients (with their "
           "role), the method of preparation, the quality-evaluation tests and suitable "
           "packaging are considered.")

    # -------------------------------------------------- Dentifrices
    n.h2("1. Dentifrices (Tooth Powders, Pastes and Gels)")
    n.para("Dentifrices are substances used with a toothbrush to clean the accessible surfaces "
           "of the teeth. They remove food debris, plaque and stains, polish the teeth, and may "
           "deliver therapeutic agents (fluoride, anti-sensitivity, anti-tartar).")

    n.h3("Ingredients of Dentifrices")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Abrasives / Polishing agents", "Remove plaque, debris and stains; polish teeth.",
             "Calcium carbonate, dicalcium phosphate, hydrated silica, calcium pyrophosphate."],
            ["Humectants", "Retain moisture, prevent drying of paste.",
             "Glycerin, sorbitol, propylene glycol."],
            ["Binders / Thickeners", "Give consistency, prevent separation.",
             "Sodium CMC, carrageenan, xanthan gum."],
            ["Surfactants (Detergents)", "Foaming and cleansing.",
             "Sodium lauryl sulphate."],
            ["Sweeteners", "Impart pleasant taste.",
             "Saccharin, sorbitol."],
            ["Flavours", "Freshness and acceptability.",
             "Peppermint, spearmint, menthol."],
            ["Therapeutic agents", "Anticaries / anti-sensitivity / antimicrobial.",
             "Sodium fluoride, stannous fluoride, strontium chloride, triclosan."],
            ["Preservatives", "Prevent microbial growth.",
             "Parabens, sodium benzoate."],
        ],
        widths=[1.9, 2.3, 2.3],
    )
    n.h3("Formulation & Preparation")
    n.bullets([
        ("Tooth powder \u2013", "abrasives, detergent, sweetener and flavour are finely powdered, thoroughly mixed and sieved."),
        ("Tooth paste \u2013", "humectant is dispersed in water, binder added to form a gel, the abrasive is mixed in, then surfactant, sweetener and flavour are added and the mass de-aerated and homogenised."),
        ("Tooth gel \u2013", "similar to paste but uses a higher proportion of thickening/gelling agent (e.g. silica) giving a clear/translucent gel."),
    ])
    n.h3("Evaluation")
    n.bullets([
        "Abrasiveness (should clean without damaging enamel).",
        "pH (should be near neutral, ~6.5\u20139).",
        "Foaming ability, spreadability and consistency.",
        "Moisture content, homogeneity and absence of hard/sharp particles.",
        "Fluoride/therapeutic content assay and stability.",
        "Microbial limits.",
    ])
    n.h3("Packaging")
    n.para("Tooth powders in wide-mouth plastic/metal containers with a sifter cap; pastes and "
           "gels in collapsible aluminium or laminated plastic tubes, or in laminate/plastic "
           "dispensers, packed in cartons.")

    # -------------------------------------------------- Nail polish
    n.h2("2. Manicure Preparations \u2013 Nail Polish (Nail Lacquer)")
    n.para("Nail polish (nail lacquer/enamel) is a coloured lacquer applied to the finger and "
           "toe nails for decoration and protection.")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Film former", "Forms the glossy, adherent film.", "Nitrocellulose."],
            ["Resins / Modifiers", "Improve gloss, adhesion and hardness.", "Toluene sulphonamide-formaldehyde resin."],
            ["Plasticizers", "Impart flexibility to the film.", "Dibutyl phthalate, camphor, castor oil."],
            ["Solvents & Diluents", "Dissolve film former; control drying.", "Ethyl acetate, butyl acetate, toluene."],
            ["Colourants", "Impart colour.", "Approved pigments, lakes, titanium dioxide."],
            ["Suspending agent", "Keep pigments dispersed (thixotropy).", "Modified bentonite (stearalkonium hectorite)."],
            ["Pearlising agent", "Pearly/lustrous effect.", "Guanine, bismuth oxychloride, mica."],
        ],
        widths=[1.9, 2.3, 2.3],
    )
    n.h3("Formulation")
    n.para("The film former, resin and plasticizer are dissolved in the solvent blend; pigments "
           "(pre-dispersed) and the suspending agent are added and the lacquer is milled to a "
           "smooth, uniform dispersion.")
    n.h3("Evaluation")
    n.bullets([
        "Drying time, gloss and smoothness of the film.",
        "Adhesion, hardness and flexibility of the dried film.",
        "Water and abrasion resistance.",
        "Colour uniformity and non-settling of pigment.",
        "Application/flow properties (viscosity).",
    ])
    n.h3("Packaging")
    n.para("Small glass bottles fitted with a cap that incorporates an applicator brush; the "
           "cap must be solvent-resistant and provide an airtight seal to prevent solvent "
           "evaporation. A related product, the nail-polish remover, contains solvents (acetone, "
           "ethyl acetate) with an emollient.")

    # -------------------------------------------------- Lipstick
    n.h2("3. Lipsticks")
    n.para("A lipstick is a moulded stick of a dispersion of colouring matter in a base of oils, "
           "fats and waxes, used to impart colour and protection to the lips.")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Waxes", "Give rigidity and the moulded shape; raise melting point.", "Carnauba wax, beeswax, candelilla wax, ozokerite."],
            ["Oils", "Dissolve/disperse dyes, provide gloss and emolliency.", "Castor oil, mineral oil, isopropyl myristate."],
            ["Fats", "Improve texture and application.", "Cocoa butter, lanolin, hydrogenated oils."],
            ["Colourants", "Staining dyes and covering pigments.", "Eosin (bromo acid), lakes, titanium dioxide."],
            ["Perfume", "Mask fatty odour, impart fragrance.", "Rose, fruit flavours."],
            ["Antioxidant / Preservative", "Prevent rancidity/microbial growth.", "BHA, BHT, tocopherol, parabens."],
        ],
        widths=[1.9, 2.3, 2.3],
    )
    n.h3("Formulation & Preparation")
    n.para("The staining dye is dissolved in castor oil; the waxes and fats are melted together; "
           "the two are combined with the dispersed pigments, milled, perfume and antioxidant "
           "added, and the molten mass is poured into moulds, cooled, removed and 'flamed' to "
           "give a glossy surface.")
    n.h3("Evaluation")
    n.bullets([
        "Melting point (should be > 55\u201360\u00b0C to resist deformation).",
        "Breaking point / mechanical strength.",
        "Force of application and spreadability.",
        "Colour uniformity, gloss and 'perspiration'/bleeding test.",
        "Surface anomalies, thixotropy and safety (skin irritation) tests.",
    ])
    n.h3("Packaging")
    n.para("Retractable metal or plastic swivel/propel-repel cases that protect the stick and "
           "allow easy application, packed in cartons.")

    # -------------------------------------------------- Eye lashes / mascara
    n.h2("4. Eye-Lash Preparations (Mascara)")
    n.para("Mascara is applied to the eyelashes to darken, thicken and lengthen them. It is "
           "available in cake, cream (emulsion) and liquid forms; being used near the eye it "
           "must be non-irritant, safe and free from harmful microbes.")
    n.h3("Ingredients")
    n.table(
        ["Ingredient", "Role", "Examples"],
        [
            ["Pigments", "Impart colour (usually black/brown).", "Iron oxides, carbon black (approved)."],
            ["Waxes", "Film formation, thickening of lashes.", "Beeswax, carnauba wax, paraffin wax."],
            ["Film formers / Resins", "Adhesion and water resistance.", "Acrylate polymers, PVP."],
            ["Emulsifiers / Surfactants", "Stabilise emulsion mascara.", "Triethanolamine stearate, soaps."],
            ["Preservatives", "Essential for eye-area safety.", "Parabens, phenoxyethanol."],
            ["Solvent / Water", "Vehicle.", "Water (emulsion) or volatile solvents."],
        ],
        widths=[1.9, 2.3, 2.3],
    )
    n.h3("Formulation")
    n.para("In emulsion (cream) mascara the waxes and emulsifier form the oil phase which is "
           "emulsified with the aqueous phase containing dispersed pigment, film former and "
           "preservative; the product is milled to a smooth paste.")
    n.h3("Evaluation")
    n.bullets([
        "Safety and non-irritancy to eye and skin (ocular safety is critical).",
        "Ease and evenness of application; smudge and water resistance.",
        "Drying time, adhesion and flaking.",
        "Microbial limits and preservative efficacy.",
        "Colour uniformity and stability.",
    ])
    n.h3("Packaging")
    n.para("Slim tube fitted with a screw cap carrying a spiral applicator brush/wand; the "
           "container must be airtight to prevent drying and contamination.")

    # -------------------------------------------------- Baby care
    n.h2("5. Baby-Care Products")
    n.para("Baby-care products are formulated for the delicate, thin and sensitive skin of "
           "infants. They must be extremely mild, non-irritant, tear-free (for shampoos/washes), "
           "and free from harsh chemicals. Common products include baby powder, baby oil, baby "
           "cream/lotion, baby soap and baby shampoo.")
    n.h3("Common Ingredients & Requirements")
    n.bullets([
        ("Baby powder \u2013", "talc or cornstarch with zinc oxide and a mild perfume; absorbs moisture and prevents nappy rash (talc must be asbestos-free)."),
        ("Baby oil \u2013", "light mineral oil / vegetable oils to protect and moisturise skin."),
        ("Baby cream/lotion \u2013", "emollients, humectants and protectants (zinc oxide) with mild preservatives."),
        ("Baby shampoo \u2013", "mild, non-ionic/amphoteric surfactants adjusted to eye-neutral pH ('no-tears')."),
    ])
    n.h3("Evaluation")
    n.bullets([
        "Mildness / non-irritancy (skin and eye) \u2013 patch and ocular tests.",
        "pH (skin-compatible, ~5.5\u20137; eye-neutral for shampoo).",
        "Absence of harmful substances and heavy metals.",
        "Fineness and flow (powder), spreadability (cream), foam (shampoo).",
        "Microbial limits and preservative efficacy.",
    ])
    n.h3("Packaging")
    n.para("Powders in sifter-top containers; oils, lotions and shampoos in squeeze/flip-top "
           "plastic bottles; child-safe, hygienic and easy-to-use packs.")

    # -------------------------------------------------- Creams
    n.h2("6. Moisturizing Cream")
    n.para("A moisturizing cream is an emulsion designed to add and retain moisture in the skin, "
           "keeping it soft and supple by reducing trans-epidermal water loss. It usually acts "
           "through occlusives, humectants and emollients.")
    n.h3("Ingredients")
    n.bullets([
        ("Occlusives \u2013", "form a film that reduces water loss (petrolatum, mineral oil, beeswax, dimethicone)."),
        ("Humectants \u2013", "attract and hold water in the stratum corneum (glycerin, sorbitol, propylene glycol, hyaluronic acid, urea)."),
        ("Emollients \u2013", "smooth and soften skin (fatty alcohols, esters, lanolin)."),
        ("Emulsifiers \u2013", "stabilise the o/w emulsion (stearic acid + TEA, cetostearyl alcohol/steareth)."),
        ("Preservatives, antioxidants, perfume and water.", ),
    ])
    n.h3("Preparation")
    n.para("Oil-phase ingredients and water-phase ingredients are heated separately to about "
           "70\u201375\u00b0C; the phases are combined with stirring, emulsified, and cooled with "
           "continuous mixing; perfume and heat-sensitive actives are added below 40\u00b0C.")

    n.h2("7. Vanishing Cream")
    n.para("A vanishing cream is a stearic-acid-based oil-in-water (o/w) emulsion that "
           "'vanishes' (leaves no visible greasy residue) when rubbed into the skin, leaving a "
           "thin protective film. It is a non-greasy day cream and a base for foundation.")
    n.h3("Typical Formula")
    n.table(
        ["Ingredient", "Role"],
        [
            ["Stearic acid", "Main base; part is saponified to form the emulsifier."],
            ["Potassium/Sodium hydroxide or borax", "Alkali to saponify stearic acid (in-situ soap)."],
            ["Glycerin / Propylene glycol", "Humectant."],
            ["Water", "Continuous (external) phase."],
            ["Preservative & Perfume", "Stability and fragrance."],
        ],
        widths=[2.7, 3.8],
    )
    n.h3("Preparation")
    n.para("Stearic acid is melted (oil phase); the alkali is dissolved in the heated aqueous "
           "phase with the humectant; the water phase is added to the oil phase with stirring \u2013 "
           "part of the stearic acid is saponified to form the soap emulsifier giving a smooth "
           "o/w cream; perfume is added on cooling.")

    n.h2("8. Cold Cream")
    n.para("Cold cream is a water-in-oil (w/o) emulsion (traditionally the 'galen's cerate') "
           "used as an emollient, cleansing and night cream. It gives a cooling sensation as "
           "the water evaporates. It leaves an oily emollient film on the skin.")
    n.h3("Typical Formula")
    n.table(
        ["Ingredient", "Role"],
        [
            ["Beeswax", "Emulsifier (with borax) and stiffening agent."],
            ["Borax", "Reacts with beeswax to form the w/o emulsifier (sodium soap)."],
            ["Liquid paraffin / Mineral oil", "Oil (external) phase / emollient."],
            ["Water", "Internal (dispersed) phase; gives cooling effect."],
            ["Perfume & Preservative", "Fragrance and stability."],
        ],
        widths=[2.7, 3.8],
    )
    n.h3("Preparation")
    n.para("Beeswax is melted in the oil (liquid paraffin) at ~70\u00b0C; borax is dissolved in "
           "water at the same temperature; the aqueous phase is added slowly to the oil phase "
           "with continuous stirring \u2013 borax and the free fatty acids of beeswax form the "
           "emulsifier giving a w/o cream; it is stirred until cool and perfume added.")

    n.h3("Evaluation of Creams (Common)")
    n.bullets([
        "Type of emulsion (dye/dilution test), pH and viscosity.",
        "Physical stability \u2013 phase separation, centrifugation and freeze-thaw cycling.",
        "Spreadability, texture and greasiness.",
        "Globule size and homogeneity (microscopy).",
        "Microbial limits and preservative efficacy; skin irritation test.",
    ])
    n.h3("Packaging of Creams")
    n.para("Wide-mouth glass or plastic jars, or collapsible aluminium / laminated tubes; "
           "the container must protect against contamination and water/perfume loss.")

    # -------------------------------------------------- Shampoo
    n.h2("9. Shampoo")
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
            ["Foam boosters / stabilisers", "Rich, stable foam.", "Lauryl/cocamide DEA."],
            ["Sequestering agent", "Prevent scum in hard water.", "EDTA."],
            ["Conditioning / anti-dandruff actives", "Therapeutic.", "Zinc pyrithione, ketoconazole, selenium sulphide."],
            ["Others", "Appearance, safety, fragrance.", "Opacifiers, colour, perfume, preservative, pH adjuster."],
        ],
        widths=[1.9, 2.1, 2.5],
    )
    n.h3("Types")
    n.para("Clear liquid, liquid cream (opaque/lotion), solid/cream, powder, anti-dandruff, "
           "conditioning ('2-in-1'), medicated and herbal shampoos.")
    n.h3("Evaluation")
    n.bullets([
        "Physical appearance, colour, odour and pH (mild, ~5\u20137).",
        "Foaming ability and foam stability.",
        "Percent solids content and viscosity/rheology.",
        "Detergency / cleaning action and wetting time.",
        "Surface tension, dirt-dispersion and eye-irritation (Draize) test.",
        "Conditioning performance (wet/dry combability) and microbial limits.",
    ])
    n.h3("Packaging")
    n.para("Squeeze plastic bottles with flip-top/disc-top closures, sachets, or pump "
           "dispensers; the container must be leak-proof and chemically compatible.")

    # -------------------------------------------------- Soaps & syndet
    n.h2("10. Soaps and Syndet Bars")
    n.para("Soaps are the sodium (hard soap) or potassium (soft soap) salts of long-chain fatty "
           "acids, produced by saponification of oils/fats with alkali. They are the classic "
           "cleansing agents but, being alkaline (pH ~9\u201310), can be harsh and form insoluble "
           "scum in hard water.")
    n.h3("Manufacture of Soap")
    n.bullets([
        ("Saponification \u2013", "fats/oils are boiled with sodium hydroxide (kettle/full-boiled process) to give soap and glycerin."),
        ("Neutralisation \u2013", "pre-formed fatty acids are neutralised with alkali (faster, more controlled)."),
        ("Finishing \u2013", "the soap is dried, milled with colour, perfume, superfatting agents and additives, then plodded, cut and stamped into bars."),
    ])
    n.h3("Syndet (Synthetic Detergent) Bars")
    n.para("Syndet bars are cleansing bars in which the cleansing agent is a synthetic surfactant "
           "(syndet = synthetic detergent) rather than, or in addition to, true soap. They "
           "contain less than about 10% true soap. Because their pH can be adjusted close to "
           "that of skin (~5.5\u20137), they are milder, do not form scum in hard water and are "
           "preferred for sensitive and dry skin.")
    n.table(
        ["Feature", "Soap", "Syndet Bar"],
        [
            ["Active cleanser", "Fatty-acid salt (true soap)", "Synthetic surfactants (e.g. sodium cocoyl isethionate)"],
            ["pH", "Alkaline (~9\u201310)", "Near skin pH (~5.5\u20137)"],
            ["Behaviour in hard water", "Forms scum", "No scum"],
            ["Mildness", "Can be harsh/drying", "Milder, better for sensitive skin"],
        ],
        widths=[1.9, 2.3, 2.3],
    )
    n.h3("Evaluation")
    n.bullets([
        "pH, moisture content and total fatty matter (TFM) \u2013 higher TFM = better quality soap.",
        "Free alkali / free fatty acid content.",
        "Foam volume and stability; hardness and wear rate.",
        "Cleansing ability, mildness and skin-irritation test.",
        "Microbial limits.",
    ])
    n.h3("Packaging")
    n.para("Bars are wrapped in paper, laminated film or cartons that protect against moisture "
           "loss, oxidation and perfume evaporation; liquid soaps in pump/flip-top bottles.")

    n.h3("High-Yield Summary")
    n.bullets([
        "Vanishing cream = stearic-acid-based o/w cream; Cold cream = beeswax-borax w/o cream.",
        "Lipstick base = waxes + oils + fats; eosin is the staining dye.",
        "Nail polish film former = nitrocellulose; solvent = ethyl/butyl acetate.",
        "Syndet bars are near skin pH (~5.5\u20137) and milder than alkaline soaps.",
        "TFM (total fatty matter) is a key quality parameter for soaps.",
    ])
