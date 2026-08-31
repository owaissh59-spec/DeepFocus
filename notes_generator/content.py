# -*- coding: utf-8 -*-
"""
Full academic content for:
Advances in Drug Delivery System (MPT102T)
M. Pharmacy (Pharmaceutical Technology) - Semester I

Comprehensive, theory-oriented exam notes with diagrams, worked examples,
tables and highlighted boxes. (No MCQs - the examination is theoretical.)

Syllabus (Parul University / PCI pattern):
  1. Sustained Release (SR) & Controlled Release (CR) Formulations
  2. Oral Sustained Release Drug Delivery Systems (mechanisms)
  3. Microencapsulation
  4. Implants and Inserts
  5. Transdermal Drug Delivery Systems (incl. sonophoresis / iontophoresis)
  6. Personalized Medicine
"""


def build(n):
    syllabus(n)
    intro_ndds(n)
    unit1(n)
    unit1_extra(n)
    unit1_more(n)
    unit2(n)
    unit2_extra(n)
    unit2_more(n)
    unit3(n)
    unit3_extra(n)
    unit3_more(n)
    unit4(n)
    unit4_extra(n)
    unit4_more(n)
    unit5(n)
    unit5_extra(n)
    unit5_more(n)
    unit6(n)
    unit6_extra(n)
    unit6_more(n)
    polymers(n)
    polymer_monographs(n)
    optimization(n)
    evaluation_methods(n)
    regulatory_stability(n)
    numericals(n)
    applications_ndds(n)
    comparison_tables(n)
    case_studies(n)
    future_trends(n)
    important_questions(n)
    model_notes(n)
    model_notes2(n)
    glossary(n)
    abbreviations(n)
    revision(n)


# =====================================================================
#  SYLLABUS
# =====================================================================
def syllabus(n):
    n.h2("Syllabus & Course Overview")

    n.h3("Scope")
    n.para("This course is designed to impart knowledge on the area of advances in novel drug "
           "delivery systems. It builds on the fundamentals of physical pharmacy, "
           "biopharmaceutics and pharmaceutics and introduces the modern approaches by which the "
           "rate, time and site of drug release can be modulated to obtain a superior "
           "therapeutic outcome. The student is trained to appreciate why a conventional dosage "
           "form is often sub-optimal and how rational design of the delivery system can improve "
           "efficacy, safety and patient compliance.")

    n.h3("Objectives")
    n.para("Upon completion of this course it is expected that the students will be able to "
           "understand :")
    n.bullets([
        "Recent innovations in conventional dosage forms \u2013 including site-specific delivery "
        "and time-release (temporal) modulation.",
        "Preparation, evaluation and application of new drug delivery systems.",
        "The criteria for selection of drugs and polymers for the development of a delivery "
        "system.",
    ])

    n.h3("Course Contents (Theory \u2013 60 Hrs)")
    n.table(
        ["Unit", "Topic", "Hrs"],
        [
            ["1", "Sustained Release (SR) & Controlled Release (CR) Formulations \u2013 basic "
                  "concepts, terminology, advantages/disadvantages, drug candidate selection, "
                  "dosage calculations, physicochemical & biological factors and approaches, "
                  "mechanism of release, classification, design, fabrication, evaluation & "
                  "applications of oral CDDS.", "10"],
            ["2", "Oral Sustained Release DDS \u2013 physicochemical & biological factors; "
                  "dissolution-controlled, diffusion-controlled, bio-erodible, osmotically "
                  "controlled, ion-exchange and mucoadhesive drug delivery systems.", "5"],
            ["3", "Microencapsulation \u2013 definition, objectives, release & stability kinetics, "
                  "coating materials, methods of preparation, evaluation & applications.", "5"],
            ["4", "Implants and Inserts \u2013 host\u2013implant and implant\u2013host reactions; "
                  "subcutaneous, intramuscular, intra-ocular, intra-vaginal and intra-uterine "
                  "systems.", "15"],
            ["5", "Transdermal Drug Delivery Systems \u2013 skin permeation fundamentals, "
                  "development approaches, kinetic evaluation, formulation design & optimization; "
                  "sonophoresis, iontophoresis and latest skin-delivery developments.", "10"],
            ["6", "Personalized Medicine \u2013 introduction, definition, pharmacogenetics, "
                  "categories of patients; customized DDS, bioelectronic medicines, 3D printing "
                  "of pharmaceuticals and telepharmacy.", "15"],
        ],
        widths=[0.5, 5.4, 0.6],
        fontsize=10,
    )

    n.h3("Recommended Books")
    n.bullets([
        "Encyclopedia of Pharmaceutical Technology \u2013 J. Swarbrick & J. C. Boylan.",
        "Theory and Practice of Industrial Pharmacy \u2013 L. Lachman, H. Lieberman.",
        "Modern Pharmaceutics \u2013 G. S. Banker & C. T. Rhodes.",
        "Controlled Drug Delivery : Fundamentals & Applications \u2013 J. R. Robinson & V. H. Lee.",
        "Novel Drug Delivery Systems \u2013 Y. W. Chien.",
        "Targeted & Controlled Drug Delivery \u2013 S. P. Vyas & R. K. Khar.",
        "Advances in Controlled and Novel Drug Delivery \u2013 (Ed.) N. K. Jain.",
    ])

    n.box("How to use these notes", [
        "Each unit contains detailed theory, labelled diagrams, worked examples, summary tables "
        "and highlighted boxes.",
        [("\u2605 boxes ", True), ("highlight high-yield points frequently asked in university "
         "theory papers and viva.")],
        "A list of important questions, a glossary and a consolidated Quick-Revision section are "
        "given at the end.",
        "As the paper is theoretical, focus on definitions, classifications, mechanisms, "
        "labelled diagrams, merits/demerits and applications.",
    ], kind="NOTE")
    n.page_break()



# =====================================================================
#  UNIT I  -  SR / CR FORMULATIONS
# =====================================================================
def unit1(n):
    n.unit_title("Unit I \u2013 Sustained & Controlled Release Formulations")

    # ---------------------------------------------------------------- 1.1
    n.h2("1.1 Introduction & Basic Concepts")
    n.para("The conventional (immediate-release) dosage form is designed to release the whole of "
           "its drug content promptly after administration so as to produce a rapid and complete "
           "systemic absorption. Although simple and inexpensive, such systems suffer from a "
           "characteristic 'peak-and-valley' plasma profile when the drug is given repeatedly. "
           "The plasma concentration rises above the minimum effective concentration (MEC), often "
           "overshooting the minimum toxic concentration (MTC), and then falls below the MEC "
           "before the next dose, so that the patient oscillates between periods of over-"
           "medication (toxicity) and under-medication (no effect). Frequent dosing also lowers "
           "patient compliance.")
    n.para("A rate-controlled delivery system is designed to overcome these limitations by "
           "delivering the drug at a pre-determined rate, for a pre-determined period, and (in "
           "advanced systems) at a pre-determined site, so that the plasma concentration is "
           "maintained within the therapeutic window for a prolonged time from a single "
           "administration.")
    n.figure("plasma_profiles.png",
             "Plasma drug concentration vs time for conventional, sustained and controlled "
             "release systems (MEC = minimum effective conc., MSC = maximum safe conc.)",
             width=5.4)

    n.h3("Therapeutic Window")
    n.para(segments=[
        ("The therapeutic window (therapeutic range) ", True),
        ("is the range of plasma drug concentration that lies between the ", ),
        ("minimum effective concentration (MEC) ", False, True),
        ("and the ", ),
        ("maximum safe / toxic concentration (MSC / MTC). ", False, True),
        ("An ideal delivery system keeps the plasma level within this band for the entire "
         "duration of therapy. The narrower the window, the greater the need for rate control.", )])

    n.h3("Rationale for Rate-Controlled Delivery")
    n.bullets([
        "To maintain a constant, therapeutically effective plasma level with minimum "
        "fluctuation.",
        "To reduce the frequency of administration (e.g., once or twice daily instead of every "
        "few hours).",
        "To reduce the total dose and dose-related side effects.",
        "To improve patient compliance and convenience.",
        "To deliver the drug to a specific site when required (spatial control).",
        "To make the therapy more economical over the course of treatment.",
    ])

    # ---------------------------------------------------------------- 1.2 terminology
    n.h2("1.2 Terminology of Modified-Release Systems")
    n.para("The term 'modified-release' is an umbrella term covering all dosage forms whose drug-"
           "release characteristics of time-course and/or location are chosen to accomplish "
           "therapeutic or convenience objectives not offered by conventional forms. The "
           "important sub-categories are defined below.")
    n.figure("release_terminology.png",
             "Release profiles illustrating immediate, sustained, delayed and repeat-action "
             "systems", width=5.2)

    n.h3("Sustained-Release System")
    n.para("A system that provides an initial dose sufficient to produce the therapeutic response "
           "promptly, followed by a gradual (slower) release of drug at a rate that will maintain "
           "the therapeutic level over an extended period. The release rate is slowed but is not "
           "necessarily constant \u2013 i.e., sustained release prolongs the duration of action "
           "but does not strictly control the plasma level. (Synonyms : sustained-action, "
           "prolonged-action, extended-release, retard.)")

    n.h3("Controlled-Release System")
    n.para("A system that releases the drug at a pre-determined, usually constant (zero-order) "
           "rate and, ideally, maintains a constant plasma or tissue concentration for a defined "
           "period. Controlled release implies a higher degree of control over the temporal and "
           "sometimes spatial delivery than sustained release; it seeks to reduce the plasma-"
           "level fluctuation to near zero.")

    n.box("SR vs CR \u2013 the key distinction", [
        [("Sustained release ", True), ("\u2013 only prolongs the duration of action; release "
         "rate declines with time (usually first-order / Higuchi); some fluctuation persists.")],
        [("Controlled release ", True), ("\u2013 maintains a constant drug level by releasing at "
         "a constant (zero-order) rate; predictable and reproducible; little or no fluctuation.")],
        "Thus every CR system is sustained, but not every SR system is truly controlled.",
    ], kind="HIGH-YIELD")

    n.h3("Other Terms")
    n.term("Delayed-release system :",
           "releases the drug at a time other than promptly after administration, e.g., "
           "enteric-coated tablets that release drug only after they leave the stomach. The "
           "total amount is released but at a later time; the rate is not necessarily slowed.")
    n.term("Repeat-action system :",
           "releases one dose immediately and a second (or subsequent) equal dose after a lag "
           "period, mimicking repeated administration; typically a coated inner core within an "
           "immediate-release outer layer.")
    n.term("Site-specific / targeted system :",
           "delivers the drug to a particular organ, tissue or cell (spatial placement of "
           "control) \u2013 e.g., colon-targeted, hepatic or tumour-targeted systems.")
    n.term("Receptor targeting :",
           "delivery directed to a particular receptor for a drug within an organ or tissue \u2013 "
           "the ultimate refinement of site-specific delivery.")
    n.term("Extended-release :",
           "an FDA/USP term encompassing both sustained- and controlled-release products that "
           "allow at least a two-fold reduction in dosing frequency compared with the "
           "conventional form.")

    n.table(
        ["Term", "Temporal control", "Spatial (site) control", "Example"],
        [
            ["Immediate release", "None (prompt)", "None", "Conventional tablet"],
            ["Sustained release", "Prolonged, rate declines", "None", "Matrix retard tablet"],
            ["Controlled release", "Constant (zero-order)", "Sometimes", "Osmotic pump (OROS)"],
            ["Delayed release", "Time-shifted", "GI region", "Enteric-coated tablet"],
            ["Repeat action", "Pulsatile (2 doses)", "None", "Two-layer coated tablet"],
            ["Site specific", "Optional", "Organ / tissue", "Colon-targeted capsule"],
        ],
        widths=[1.4, 1.7, 1.7, 1.5],
        fontsize=9.5,
    )

    # ---------------------------------------------------------------- 1.3 adv/disadv
    n.h2("1.3 Advantages & Disadvantages of SR / CR Systems")
    n.h3("Advantages")
    n.numbered([
        [("Improved patient compliance ", True), ("due to reduced frequency of dosing.")],
        [("Reduced plasma-level fluctuation ", True), ("\u2013 a more uniform effect and fewer "
         "concentration-dependent adverse effects.")],
        [("Reduction in total dose ", True), ("of drug used over the course of therapy in many "
         "cases.")],
        [("Reduced night-time dosing ", True), ("and uninterrupted sleep for the patient.")],
        [("Reduction of drug accumulation ", True), ("with chronic therapy.")],
        [("Improved efficiency of treatment ", True), ("\u2013 better control of the condition "
         "with a smoother response.")],
        [("Economy ", True), ("\u2013 although unit cost is higher, the overall cost of therapy "
         "may be lower.")],
    ])
    n.h3("Disadvantages")
    n.numbered([
        [("Dose dumping ", True), ("\u2013 accidental, rapid release of the entire dose can cause "
         "toxicity if the system fails.")],
        [("Poor in-vivo / in-vitro correlation ", True), ("in some cases.")],
        [("Reduced ability to adjust the dose ", True), ("or to promptly terminate therapy "
         "(e.g., in adverse reactions the dose cannot be quickly withdrawn).")],
        [("Higher cost ", True), ("of manufacture and sophisticated technology required.")],
        [("First-pass metabolism ", True), ("may reduce bioavailability of some drugs delivered "
         "slowly.")],
        [("Increased potential for variability ", True), ("due to GI transit, food and disease.")],
        [("Not suitable for all drugs ", True), ("\u2013 the drug and dose must satisfy specific "
         "criteria (see below).")],
    ])

    # ---------------------------------------------------------------- 1.4 candidate selection
    n.h2("1.4 Drug Candidate Selection for SR / CR Dosage Forms")
    n.para("Not every drug is a suitable candidate for a rate-controlled system. The selection is "
           "governed by the physicochemical, pharmacokinetic and pharmacodynamic properties of "
           "the drug. The following are the desirable and the disqualifying characteristics.")

    n.h3("Physicochemical Factors influencing the design")
    n.bullets([
        [("Aqueous solubility & pH-dependent solubility : ", True), ("very poorly soluble drugs "
         "(< 0.01 mg/mL) are difficult to sustain because dissolution itself is rate-limiting; "
         "highly soluble drugs are hard to retard. An intermediate solubility is ideal.")],
        [("Partition coefficient (log P) : ", True), ("governs the ability to cross biological "
         "membranes; extremely high or low log P values are unfavourable. A balanced lipophilicity "
         "is required for both membrane transport and release control.")],
        [("Drug stability : ", True), ("drugs unstable in the environment of a particular GI "
         "segment are poor candidates for that region; e.g., drugs degraded in the small "
         "intestine benefit from rapid-release forms.")],
        [("Molecular size & diffusivity : ", True), ("large molecules (> 500 Da onwards) diffuse "
         "slowly through polymeric membranes / matrices; the diffusion coefficient falls with "
         "increasing molecular size.")],
        [("Protein binding : ", True), ("highly protein-bound drugs already have a prolonged "
         "biological half-life and may not need sustaining.")],
        [("pKa & degree of ionisation : ", True), ("since only the unionised form permeates, the "
         "pKa relative to the pH of the absorption site is important.")],
    ])

    n.h3("Biological (Pharmacokinetic / Pharmacodynamic) Factors")
    n.bullets([
        [("Biological half-life (t\u00bd) : ", True), ("the ideal candidate has t\u00bd of "
         "about 2\u20138 h. Drugs with very short t\u00bd (< 1 h) need an impractically large "
         "dose; drugs with long t\u00bd (> 8 h, e.g., digoxin, warfarin) are inherently "
         "sustained and need no formulation aid.")],
        [("Absorption rate & window : ", True), ("the drug should be well and uniformly absorbed "
         "throughout the GI tract. Drugs with a narrow 'absorption window' (absorbed only from "
         "the upper GI, e.g., riboflavin, iron) are poor candidates unless gastro-retentive.")],
        [("Rate of metabolism : ", True), ("drugs extensively metabolised or that induce/inhibit "
         "enzymes may show non-linear kinetics and are difficult to formulate.")],
        [("Dosing size (dose) : ", True), ("a single dose > 0.5\u20131.0 g leads to an "
         "unacceptably large SR unit.")],
        [("Therapeutic index : ", True), ("drugs with a narrow therapeutic index require precise "
         "rate control; dose dumping would be dangerous.")],
        [("Margin of safety & MEC/MTC : ", True), ("a well-defined and reasonably wide "
         "therapeutic window is desirable.")],
    ])

    n.box("Ideal characteristics of a drug for SR/CR", [
        "Molecular weight < 500 Da; moderate aqueous solubility (not < 0.1 mg/mL).",
        "Biological half-life between 2 and 8 h.",
        "Uniform absorption from the whole GI tract; good stability in GI fluids.",
        "Dose < 0.5 g; wide therapeutic index; first-order (linear) pharmacokinetics.",
        "Neither very high nor very low apparent partition coefficient.",
    ], kind="HIGH-YIELD")

    n.h3("Drugs unsuitable for SR / CR")
    n.bullets([
        "Drugs with very short or very long half-life.",
        "Drugs requiring large doses (> 1 g).",
        "Drugs with narrow absorption window / poor absorption in the lower GI.",
        "Drugs whose action is intended to be prompt and short (e.g., analgesics for acute "
        "pain in some cases).",
        "Drugs with low therapeutic index (unless very precise control is guaranteed).",
    ])

    # ---------------------------------------------------------------- 1.5 dosage calculations
    n.h2("1.5 Dosage Calculations for SR / CR Systems")
    n.para("A sustained-release product usually contains two portions of drug : an immediate-"
           "release (loading / initial) dose D\u2080 that promptly raises the plasma level to the "
           "therapeutic value, and a maintenance (sustaining) dose D\u2098 that is released "
           "slowly to compensate for elimination. The total dose is the sum of the two.")

    n.h3("Maintenance dose and release rate")
    n.para("For a system that is to deliver drug at a zero-order rate equal to the rate of "
           "elimination, the desired release rate (K\u1d63\u2080) is :")
    n.formula("K\u1d63\u2080 = Rate of elimination = C\u209a \u00d7 CL = C\u209a \u00d7 k\u2091 \u00d7 Vd")
    n.para("where C\u209a is the desired steady-state plasma concentration, CL is the total body "
           "clearance, k\u2091 is the first-order elimination rate constant and Vd is the volume "
           "of distribution.")
    n.para("The total maintenance dose to sustain the level for a time T\u1d48 is :")
    n.formula("D\u2098 = K\u1d63\u2080 \u00d7 T\u1d48 = C\u209a \u00d7 k\u2091 \u00d7 Vd \u00d7 T\u1d48")

    n.h3("Loading (initial) dose")
    n.para("The loading dose that immediately establishes the therapeutic level is :")
    n.formula("D\u2080 = C\u209a \u00d7 Vd   (for i.v.) ;   D\u2080 = C\u209a \u00d7 Vd / F   (for oral, F = bioavailability)")
    n.para("When the maintenance system begins releasing drug immediately, a correction is "
           "applied because some maintenance drug is released during the time the loading dose is "
           "still effective :")
    n.formula("D\u2080 (corrected) = D\u2080 \u2013 (K\u1d63\u2080 \u00d7 T\u209a)")
    n.para("where T\u209a is the time to reach peak concentration from the immediate-release "
           "portion.")
    n.para("Total dose  W = D\u2080 + D\u2098 = D\u2080 + K\u1d63\u2080 \u00d7 T\u1d48.")

    n.h3("Worked Example")
    n.box("Numerical", [
        "A drug has t\u00bd = 4 h, Vd = 20 L and desired C\u209a = 10 mg/L. Design a 12-h SR dose "
        "(assume F = 1).",
        [("Step 1 \u2013 k\u2091 : ", True), ("k\u2091 = 0.693 / 4 = 0.173 h\u207b\u00b9.")],
        [("Step 2 \u2013 Loading dose : ", True), ("D\u2080 = C\u209a \u00d7 Vd = 10 \u00d7 20 = "
         "200 mg.")],
        [("Step 3 \u2013 Release rate : ", True), ("K\u1d63\u2080 = C\u209a \u00d7 k\u2091 \u00d7 "
         "Vd = 10 \u00d7 0.173 \u00d7 20 = 34.6 mg/h.")],
        [("Step 4 \u2013 Maintenance dose (for 12 h) : ", True), ("D\u2098 = 34.6 \u00d7 12 = "
         "415 mg.")],
        [("Total dose : ", True), ("W = 200 + 415 = 615 mg.")],
    ], kind="EXAMPLE")

    # ---------------------------------------------------------------- 1.6 approaches / mechanism
    n.h2("1.6 Physicochemical & Biological Approaches to SR / CR")
    n.para("Rate control can be achieved by chemical modification of the drug molecule, by "
           "physical / formulation approaches, or by exploiting biological handling of the drug. "
           "The main strategies are summarised below.")

    n.h3("Physicochemical Approaches")
    n.bullets([
        [("Prodrugs : ", True), ("a bio-reversible derivative that regenerates the active drug "
         "slowly, prolonging action (e.g., depot esters).")],
        [("Salt / complex formation : ", True), ("poorly soluble salts, resonates or complexes "
         "release the drug slowly (e.g., penicillin G procaine, drug\u2013tannate complexes).")],
        [("Adjustment of particle size / polymorph : ", True), ("larger particles or a less "
         "soluble polymorph dissolve more slowly.")],
        [("Coating : ", True), ("film or micro-encapsulation with polymers of controlled "
         "permeability.")],
        [("Embedding in a matrix : ", True), ("wax, hydrophilic or plastic matrices retard "
         "diffusion / dissolution.")],
        [("Osmotic control : ", True), ("water influx through a semipermeable membrane pumps out "
         "drug solution at a constant rate.")],
    ])
    n.h3("Biological Approaches")
    n.bullets([
        [("Modifying the molecule for slower metabolism ", True), ("or slower renal clearance.")],
        [("Co-administration of an adjuvant ", True), ("that slows absorption or metabolism "
         "(e.g., a vasoconstrictor with a local anaesthetic; a metabolism inhibitor).")],
        [("Altering the route ", True), ("to a depot site (i.m., s.c.) to obtain slow "
         "absorption.")],
    ])

    n.h3("Mechanisms of Drug Delivery / Release from SR-CR Systems")
    n.para("The rate-limiting step in a SR/CR system may be diffusion, dissolution, osmosis, "
           "ion-exchange or erosion. These are treated in detail in Unit II. In brief :")
    n.bullets([
        [("Diffusion-controlled : ", True), ("drug diffuses through a polymer membrane "
         "(reservoir) or matrix (monolithic).")],
        [("Dissolution-controlled : ", True), ("a slowly dissolving coat or matrix controls the "
         "rate at which drug becomes available.")],
        [("Osmotically controlled : ", True), ("osmotic pressure drives constant delivery.")],
        [("Ion-exchange controlled : ", True), ("drug bound to a resin is released by exchange "
         "with GI ions.")],
        [("Erosion / bioerosion-controlled : ", True), ("release accompanies gradual erosion of "
         "a biodegradable matrix.")],
    ])

    # ---------------------------------------------------------------- 1.7 classification & design
    n.h2("1.7 Classification of Oral Controlled Drug Delivery Systems")
    n.figure("cdds_classification.png",
             "Classification of oral controlled drug delivery systems", width=5.6)
    n.para("Oral CDDS may be broadly classified according to the rate-controlling mechanism into "
           "the following groups :")
    n.numbered([
        [("Diffusion-controlled systems ", True), ("\u2013 reservoir (membrane) and matrix "
         "(monolithic) devices.")],
        [("Dissolution-controlled systems ", True), ("\u2013 encapsulation (coated) and matrix "
         "(embedded) devices.")],
        [("Diffusion + dissolution (dual) systems ", True), ("\u2013 combining both mechanisms.")],
        [("Osmotically controlled systems ", True), ("\u2013 elementary and push-pull osmotic "
         "pumps.")],
        [("Ion-exchange resin systems.", True), ("")],
        [("Gastro-retentive & bioerodible systems.", True), ("")],
    ])

    n.h2("1.8 Design, Fabrication, Evaluation & Applications of Oral CDDS")
    n.h3("Design considerations")
    n.bullets([
        "Selection of drug candidate satisfying the criteria of section 1.4.",
        "Choice of rate-controlling mechanism and polymer / excipient.",
        "Fixing the target release rate (zero-order desirable) and duration.",
        "Deciding the loading and maintenance dose fractions.",
        "Ensuring stability, manufacturability and reproducibility of release.",
    ])
    n.h3("Fabrication techniques")
    n.bullets([
        [("Matrix tablets : ", True), ("drug + rate-controlling polymer (HPMC, ethylcellulose, "
         "waxes) compressed directly or after granulation.")],
        [("Coated multiparticulates (pellets / beads) : ", True), ("drug layered on non-pareils "
         "then film-coated; filled into capsules.")],
        [("Osmotic tablets : ", True), ("core compressed and coated with a semipermeable "
         "membrane, then laser-drilled.")],
        [("Micro-encapsulation : ", True), ("coacervation, spray drying, etc. (Unit III).")],
    ])
    n.h3("Evaluation of oral CDDS")
    n.bullets([
        [("Physical tests : ", True), ("weight variation, hardness, friability, thickness.")],
        [("Drug content & content uniformity.", True), ("")],
        [("In-vitro dissolution / release ", True), ("using USP apparatus; data fitted to "
         "kinetic models (zero-order, first-order, Higuchi, Korsmeyer\u2013Peppas).")],
        [("Release-mechanism analysis ", True), ("via the diffusional exponent n of the "
         "Korsmeyer\u2013Peppas model.")],
        [("Stability & accelerated studies ", True), ("as per ICH.")],
        [("In-vivo / bioavailability & IVIVC ", True), ("studies.")],
    ])
    n.figure("release_kinetics.png",
             "Common drug-release kinetic models used to characterise CDDS", width=5.0)
    n.h3("Applications")
    n.bullets([
        "Once-daily antihypertensives (nifedipine GITS, diltiazem CD).",
        "Sustained-release analgesics and anti-inflammatory agents.",
        "Extended-release antidiabetics (metformin XR).",
        "Prolonged-release theophylline and antihistamines.",
        "Chronotherapeutic (time-controlled) delivery of cardiovascular drugs.",
    ])
    n.page_break()



# =====================================================================
#  UNIT II  -  ORAL SR DDS (MECHANISMS)
# =====================================================================
def unit2(n):
    n.unit_title("Unit II \u2013 Oral Sustained-Release Drug Delivery Systems")

    n.h2("2.1 Introduction")
    n.para("The oral route remains the most preferred route of administration because of its "
           "convenience, safety and economy. Oral sustained-release systems achieve rate control "
           "through one (or a combination) of the following mechanisms : dissolution control, "
           "diffusion control, osmotic control, ion-exchange and erosion. This unit examines the "
           "physicochemical and biological factors that influence their design and then treats "
           "each mechanism in detail.")

    n.h2("2.2 Physicochemical & Biological Factors influencing Design")
    n.para("The factors discussed in Unit I (solubility, partition coefficient, pKa, stability, "
           "molecular size, half-life, absorption window, dose, therapeutic index and "
           "metabolism) all apply directly to oral SR design. In addition, the following "
           "GI-specific factors are important.")
    n.h3("GI-tract related factors")
    n.bullets([
        [("GI transit time : ", True), ("a conventional non-disintegrating unit resides "
         "8\u201312 h in the GI tract (stomach 0.5\u20132 h, small intestine ~3 h, colon variable). "
         "Release must be completed within the absorptive transit time.")],
        [("Absorption window : ", True), ("drugs absorbed only from the upper GI (e.g., iron, "
         "riboflavin, L-dopa) need gastro-retentive design.")],
        [("Gastric emptying & motility : ", True), ("affected by food, posture and disease; "
         "influences the residence and hence the absorbed fraction.")],
        [("Luminal pH & enzymes : ", True), ("pH rises from ~1.5 (stomach) to ~7.5 (ileum); "
         "affects ionisation, solubility and stability.")],
        [("First-pass metabolism : ", True), ("slow presentation of drug to the liver can "
         "increase first-pass loss for high-extraction drugs.")],
    ])

    # ---------------------------------------------------------------- dissolution
    n.h2("2.3 Dissolution-Controlled Systems")
    n.para("Here the rate-limiting step is the slow dissolution of a coat or matrix, so that the "
           "drug becomes available for absorption only as fast as the barrier dissolves. A drug "
           "with inherently slow dissolution is itself sustained; otherwise a slowly-soluble salt, "
           "derivative or coat is used. The release approximately follows the Noyes\u2013Whitney "
           "relationship.")
    n.formula("dC/dt = (D \u00d7 A / h) \u00d7 (Cs \u2013 Ct)")
    n.para("where D = diffusion coefficient, A = surface area, h = diffusion-layer thickness, "
           "Cs = saturation solubility and Ct = concentration in the bulk.")
    n.figure("dissolution_controlled.png",
             "Encapsulation (coated beads) and matrix dissolution-controlled systems", width=5.0)
    n.h3("(a) Encapsulation / Coating (Reservoir) dissolution systems")
    n.para("Drug particles or granules are coated with slowly dissolving polymers or waxes of "
           "varying thickness. Beads with thin coats dissolve early, those with thicker coats "
           "later, producing a sustained overall release (the principle of Spansule\u00ae "
           "capsules). Coating materials include cellulose derivatives, PEG, waxes and shellac.")
    n.h3("(b) Matrix (monolithic) dissolution systems")
    n.para("Drug is dispersed uniformly in a slowly dissolving or erodible matrix (e.g., wax such "
           "as carnauba or castor wax, or a hydrophilic gum). As the matrix dissolves/erodes, "
           "drug is released. Prepared by fusion (congealing the drug in molten wax) or by "
           "aqueous/organic granulation.")

    # ---------------------------------------------------------------- diffusion
    n.h2("2.4 Diffusion-Controlled Systems")
    n.para("Diffusion of the drug (rather than dissolution) is the rate-limiting step. Two "
           "sub-types exist : reservoir (membrane) and matrix (monolithic).")
    n.figure("reservoir_matrix.png",
             "Reservoir (membrane) and matrix (monolithic) diffusion-controlled devices",
             width=5.2)
    n.h3("(a) Reservoir (membrane) devices")
    n.para("A core of drug is enclosed within a rate-controlling polymer membrane. Drug dissolves "
           "at the inner surface and diffuses across the membrane. For a slab (film) the flux "
           "follows Fick's first law and yields a near constant (zero-order) release as long as "
           "the core remains saturated :")
    n.formula("dQ/dt = (A \u00d7 D \u00d7 K \u00d7 \u0394C) / L")
    n.para("where A = area, D = diffusion coefficient in the membrane, K = partition coefficient "
           "of drug between membrane and core, \u0394C = concentration difference and L = membrane "
           "thickness. Advantage : zero-order release possible. Disadvantage : risk of dose "
           "dumping if the membrane ruptures; membrane thickness must be reproducible.")
    n.h3("(b) Matrix (monolithic) devices")
    n.para("Drug is dispersed uniformly throughout an insoluble polymer (e.g., ethylcellulose, "
           "PVC, polyethylene) or a hydrophilic matrix. Release from a homogeneous matrix follows "
           "the Higuchi equation and is proportional to the square-root of time :")
    n.formula("Q = \u221a[ D \u00d7 Cs \u00d7 (2A \u2013 Cs) \u00d7 t ]   (dispersed-drug, "
              "planar matrix)")
    n.para("where Q = amount released per unit area at time t, A = total drug content per unit "
           "volume and Cs = drug solubility in the matrix. Because release declines with "
           "\u221at, matrix systems are 'first-order-like' and do not give true zero-order "
           "release, but they are simple, cheap and free of dose-dumping risk.")

    n.table(
        ["Feature", "Reservoir (membrane)", "Matrix (monolithic)"],
        [
            ["Drug location", "Core, surrounded by membrane", "Dispersed throughout"],
            ["Release order", "Near zero-order", "\u221at (Higuchi), declining"],
            ["Dose dumping", "Possible (membrane failure)", "Unlikely"],
            ["Fabrication", "Coating / microencapsulation", "Direct compression / granulation"],
            ["Cost / complexity", "Higher", "Lower"],
        ],
        widths=[1.5, 2.5, 2.5],
        fontsize=9.5,
    )

    # ---------------------------------------------------------------- bioerodible
    n.h2("2.5 Bio-erodible & Combination (Diffusion\u2013Dissolution) Systems")
    n.para("In bio-erodible / biodegradable systems the polymer matrix gradually erodes in the "
           "biological environment and the drug is released by a combination of diffusion and "
           "erosion. An advantage is that no device residue remains to be removed. Erosion may be "
           "of two types :")
    n.figure("bioerosion.png", "Bulk erosion vs surface erosion of a biodegradable matrix",
             width=5.0)
    n.bullets([
        [("Bulk (homogeneous) erosion : ", True), ("water penetrates the whole matrix and "
         "degradation occurs throughout the bulk (e.g., poly-lactide/glycolide, PLGA). Size "
         "changes little until late.")],
        [("Surface (heterogeneous) erosion : ", True), ("degradation is confined to the surface "
         "and the device shrinks progressively while keeping its shape (e.g., polyanhydrides, "
         "poly-ortho-esters). Gives more nearly zero-order release.")],
    ])
    n.para("Common biodegradable polymers : poly(lactic acid) (PLA), poly(lactic-co-glycolic "
           "acid) (PLGA), poly-\u03b5-caprolactone, polyanhydrides, poly-ortho-esters and natural "
           "polymers (albumin, gelatin, chitosan). Erosion-controlled release is widely used for "
           "injectable microspheres and implants.")

    # ---------------------------------------------------------------- osmotic
    n.h2("2.6 Osmotically Controlled Systems")
    n.para("Osmotic systems use the osmotic pressure developed by the imbibition of water across "
           "a semipermeable membrane as the driving force for delivery. They give a constant "
           "(zero-order) release that is essentially independent of the pH and hydrodynamics of "
           "the GI environment \u2013 their outstanding advantage.")
    n.figure("osmotic_pump.png", "Elementary osmotic pump (EOP / OROS)", width=3.4)
    n.h3("Elementary Osmotic Pump (EOP)")
    n.para("The EOP consists of an osmotic core (drug plus an osmotic agent such as NaCl, KCl, "
           "mannitol or lactose) surrounded by a rigid semipermeable membrane (usually cellulose "
           "acetate) that has a single small delivery orifice made by a laser. Water is imbibed "
           "osmotically, dissolving the core and generating hydrostatic pressure that pumps the "
           "saturated drug solution out through the orifice at a constant volume rate.")
    n.formula("dM/dt = (A \u00d7 Lp \u00d7 \u03c3 \u00d7 \u0394\u03c0 / h) \u00d7 Cs")
    n.para("where A = membrane area, Lp = mechanical permeability, \u03c3 = reflection "
           "coefficient, \u0394\u03c0 = osmotic-pressure difference, h = membrane thickness and "
           "Cs = solubility of drug in the pumped solution. Delivery is constant while the core "
           "remains saturated.")
    n.h3("Push-Pull Osmotic Pump (Bilayer, OROS Push-Pull)")
    n.para("For poorly soluble drugs a bilayer core is used : a drug layer and an osmotic 'push' "
           "layer (a swellable polymer such as polyethylene oxide). Imbibed water swells the push "
           "layer, which forces the drug layer (as a suspension) out of the orifice. This extends "
           "osmotic delivery to insoluble drugs. (Example : nifedipine GITS.)")
    n.box("Advantages of osmotic systems", [
        "Zero-order release, independent of GI pH, motility and food.",
        "Good in-vitro / in-vivo correlation.",
        "Delivery rate can be programmed by membrane thickness, orifice size and osmogen.",
    ], kind="HIGH-YIELD")

    # ---------------------------------------------------------------- ion exchange
    n.h2("2.7 Ion-Exchange Resin Systems")
    n.para("An ion-exchange resin is a water-insoluble cross-linked polymer bearing ionisable "
           "functional groups. An ionised drug is bound to the resin by exchanging with the "
           "resin's counter-ions, forming a drug\u2013resin complex (resinate). In the GI tract, "
           "the abundant Na\u207a, K\u207a, H\u207a (for cationic drugs) or Cl\u207b (for anionic "
           "drugs) displace the drug, releasing it slowly.")
    n.figure("ion_exchange.png", "Release of a cationic drug from a drug\u2013resin complex",
             width=5.0)
    n.para("Cationic (basic) drugs are bound to cation-exchange resins bearing \u2013SO\u2083\u207b "
           "or \u2013COO\u207b groups; anionic (acidic) drugs are bound to anion-exchange resins "
           "bearing quaternary ammonium groups. Release depends on the ionic environment (rather "
           "than pH alone), giving a fairly reproducible rate. Coating the resinate and further "
           "treatment (the 'Pennkinetic' system) improves control. Examples : "
           "nicotine\u2013polacrilex, hydrocodone\u2013 and dextromethorphan\u2013resin "
           "suspensions.")
    n.bullets([
        [("Advantages : ", True), ("good for liquid SR suspensions; taste masking; protects "
         "drug; release relatively insensitive to enzymes.")],
        [("Limitations : ", True), ("release depends on variable GI ionic strength & diet; only "
         "ionisable drugs; drug\u2013resin ratio limits loading.")],
    ])

    # ---------------------------------------------------------------- mucoadhesive
    n.h2("2.8 Mucoadhesive (Bioadhesive) Drug Delivery Systems")
    n.para("Mucoadhesion is the ability of a material (usually a hydrophilic polymer) to adhere to "
           "the mucus layer of a biological surface, thereby prolonging the residence time of the "
           "dosage form at the site of absorption and intensifying contact. This is especially "
           "valuable for drugs with a narrow absorption window and for local action.")
    n.figure("mucoadhesion.png", "Stages / mechanism of mucoadhesion", width=5.4)
    n.h3("Theories / mechanism of mucoadhesion")
    n.bullets([
        [("Wetting theory : ", True), ("adhesive spreads and wets the mucosa (governed by "
         "spreading coefficient).")],
        [("Diffusion (interpenetration) theory : ", True), ("polymer chains and mucin chains "
         "inter-diffuse and entangle across the interface.")],
        [("Electronic theory : ", True), ("electron transfer forms an electrical double layer at "
         "the interface.")],
        [("Adsorption theory : ", True), ("adhesion by secondary forces \u2013 hydrogen bonds, "
         "van der Waals and hydrophobic interactions.")],
        [("Fracture theory : ", True), ("relates adhesive strength to the force required to "
         "separate the surfaces.")],
    ])
    n.h3("Ideal mucoadhesive polymer & examples")
    n.para("An ideal mucoadhesive polymer should have numerous hydrogen-bonding groups, high "
           "molecular weight, chain flexibility, appropriate charge and be biocompatible and "
           "non-toxic. Examples : carbopol (polyacrylic acid), sodium carboxymethylcellulose, "
           "HPMC, chitosan, sodium alginate, and thiolated polymers (thiomers).")
    n.h3("Applications")
    n.bullets([
        "Buccal and sublingual tablets / films (bypass first-pass metabolism).",
        "Gastro-retentive mucoadhesive tablets for narrow-window drugs.",
        "Nasal, ocular and vaginal mucoadhesive systems.",
        "Colon-targeted and intestinal absorption enhancement.",
    ])
    n.page_break()



# =====================================================================
#  UNIT III  -  MICROENCAPSULATION
# =====================================================================
def unit3(n):
    n.unit_title("Unit III \u2013 Microencapsulation")

    n.h2("3.1 Definition")
    n.para(segments=[
        ("Microencapsulation ", True),
        ("is the process by which small solid particles, liquid droplets or gases are enveloped "
         "within a thin coating of a wall-forming (shell) material to form small capsules "
         "(microcapsules) of size ranging from about 1 to 1000 \u00b5m. The material inside the "
         "capsule is the ", ),
        ("core (internal phase / fill) ", False, True),
        ("and the coating is the ", ),
        ("wall / shell (membrane).", False, True)])
    n.para("Particles below 1 \u00b5m are called nanocapsules and those above 1000 \u00b5m are "
           "macrocapsules. When the drug is distributed uniformly throughout a polymer particle "
           "(no distinct core-shell), the product is a microsphere / micromatrix rather than a "
           "true microcapsule.")

    n.h2("3.2 Objectives / Reasons for Microencapsulation")
    n.numbered([
        "To achieve sustained or controlled release of the drug.",
        "To mask the bitter taste or unpleasant odour of the drug.",
        "To protect the core from environmental factors (light, moisture, oxygen) and improve "
        "stability.",
        "To convert liquids into free-flowing powders (e.g., oils, vitamins).",
        "To separate incompatible ingredients in a formulation.",
        "To reduce gastric irritation (e.g., aspirin, KCl, ferrous salts).",
        "To reduce volatility and hygroscopicity.",
        "To achieve targeted or site-specific delivery.",
        "To improve handling and flow properties of powders.",
    ])

    n.h2("3.3 Types of Microcapsules / Microspheres")
    n.figure("microcapsule_types.png",
             "Mononuclear, polynuclear and matrix (microsphere) types", width=5.4)
    n.bullets([
        [("Mononuclear (core-shell) : ", True), ("a single core enclosed by the shell.")],
        [("Polynuclear (multi-core) : ", True), ("several cores enclosed within a single "
         "shell.")],
        [("Matrix / microsphere : ", True), ("core material dispersed uniformly throughout the "
         "wall material.")],
    ])

    n.h2("3.4 Coating (Wall) Materials")
    n.para("The choice of coating material governs the release rate, protection and stability of "
           "the microcapsule. An ideal coating material should be capable of forming a coherent "
           "film, be chemically compatible and non-reactive with the core, provide the desired "
           "release characteristics, and be economical.")
    n.table(
        ["Category", "Examples"],
        [
            ["Water-soluble polymers", "Gelatin, gum acacia, starch, PVP, carboxymethylcellulose"],
            ["Water-insoluble polymers", "Ethylcellulose, polyethylene, polymethacrylate, "
             "cellulose nitrate"],
            ["Enteric (pH-dependent) polymers", "Cellulose acetate phthalate, shellac, "
             "zein, Eudragit L/S"],
            ["Waxes & lipids", "Beeswax, carnauba wax, stearic acid, glyceryl stearate"],
            ["Proteins", "Albumin, gelatin"],
            ["Biodegradable polymers", "PLA, PLGA, poly-\u03b5-caprolactone, chitosan, alginate"],
        ],
        widths=[2.3, 4.2],
        fontsize=9.5,
    )

    n.h2("3.5 Methods of Microencapsulation")
    n.para("The methods are broadly classified into physical, physico-chemical and chemical "
           "methods.")

    n.h3("(a) Coacervation \u2013 Phase Separation")
    n.para("This is the classical and most widely used method. It involves three steps : (i) "
           "formation of three immiscible phases \u2013 the liquid vehicle, the core material and "
           "the coating material; (ii) deposition of the liquid polymer coating on the core; and "
           "(iii) rigidisation of the coating by thermal, cross-linking or desolvation "
           "techniques. Coacervation may be simple (one polymer, phase separation induced by a "
           "non-solvent, salt or temperature change) or complex (two oppositely charged polymers, "
           "e.g., gelatin\u2013acacia, whose interaction produces the coacervate).")
    n.figure("coacervation.png", "Steps of coacervation / phase-separation microencapsulation",
             width=5.6)

    n.h3("(b) Spray Drying")
    n.para("The core is dispersed / dissolved in a solution of the coating polymer; the mixture "
           "is atomised into a stream of hot air. The solvent evaporates instantly and dry "
           "microcapsules are collected in a cyclone. It is rapid, single-step and economical, "
           "and suitable for heat-sensitive materials because exposure to heat is very brief.")
    n.figure("spray_drying.png", "Spray-drying microencapsulation", width=3.2)

    n.h3("(c) Air-Suspension Coating (Wurster process) & Pan Coating")
    n.para("In pan coating, the solid cores (larger particles / tablets) are tumbled in a coating "
           "pan while the coating solution is sprayed and warm air dries the film. In the Wurster "
           "air-suspension technique, particles are suspended in an upward stream of air and the "
           "coating is sprayed and dried repeatedly as the particles circulate \u2013 giving very "
           "uniform films, ideal for controlled release.")
    n.figure("pan_coating.png", "Pan coating and air-suspension (Wurster) coating", width=5.2)

    n.h3("(d) Other methods")
    n.bullets([
        [("Solvent evaporation : ", True), ("polymer and drug are dissolved in a volatile organic "
         "solvent, emulsified in an aqueous phase and the solvent evaporated to harden the "
         "microspheres (common for PLGA microspheres).")],
        [("Emulsification\u2013cross-linking / ionotropic gelation : ", True), ("e.g., alginate "
         "droplets gelled with calcium chloride; chitosan cross-linked with "
         "tripolyphosphate.")],
        [("Interfacial & in-situ polymerisation : ", True), ("the shell is formed by "
         "polymerisation of monomers at the core surface.")],
        [("Spray congealing : ", True), ("a molten wax\u2013drug dispersion is sprayed into cool "
         "air where it congeals.")],
        [("Multiorifice-centrifugal & pan-drying techniques.", True), ("")],
    ])

    n.h2("3.6 Release & Stability Kinetics")
    n.para("Drug release from microcapsules occurs by diffusion through the wall, by dissolution "
           "/ erosion of the wall, or by osmotic rupture. The release data are commonly fitted to "
           "kinetic models :")
    n.bullets([
        [("Zero-order : ", True), ("constant amount released per unit time (ideal CR).")],
        [("First-order : ", True), ("release proportional to the amount remaining.")],
        [("Higuchi model : ", True), ("release proportional to \u221at (matrix diffusion).")],
        [("Korsmeyer\u2013Peppas : ", True), ("Mt/M\u221e = k\u00b7t\u207f; the exponent n "
         "indicates the mechanism (Fickian diffusion when n \u2264 0.43 for spheres; "
         "anomalous / non-Fickian for intermediate n; case-II / erosion when n \u2192 0.85).")],
    ])
    n.para("Stability kinetics assess how the encapsulated drug degrades on storage. Because the "
           "coat protects the core from moisture, oxygen and light, microencapsulation usually "
           "increases the shelf-life; the degradation still follows the appropriate reaction "
           "order and can be predicted from accelerated data using the Arrhenius relationship.")

    n.h2("3.7 Evaluation of Microcapsules")
    n.bullets([
        [("Particle size & shape : ", True), ("microscopy, sieving, laser diffraction, SEM.")],
        [("Surface morphology : ", True), ("scanning electron microscopy (SEM).")],
        [("Wall thickness & core-shell structure.", True), ("")],
        [("Drug content / loading & encapsulation efficiency.", True), ("")],
        [("Flow properties : ", True), ("angle of repose, Carr's index, Hausner ratio.")],
        [("In-vitro drug release / dissolution and kinetic modelling.", True), ("")],
        [("Isolation & envelope characteristics; residual solvent.", True), ("")],
    ])
    n.formula("% Encapsulation efficiency = (Actual drug content / Theoretical drug content) \u00d7 100")

    n.h2("3.8 Applications of Microencapsulation")
    n.bullets([
        "Sustained / controlled release of drugs (e.g., aspirin, KCl, theophylline).",
        "Taste and odour masking (e.g., paracetamol, chloramphenicol).",
        "Protection of unstable drugs (vitamins, prostaglandins).",
        "Conversion of liquids to solids (cod-liver oil, vitamin A/E).",
        "Separation of incompatible substances.",
        "Reduction of gastric irritation and toxicity.",
        "Preparation of injectable depot microspheres (leuprolide PLGA).",
        "Use in carbonless copy paper, cosmetics and food industries.",
    ])
    n.page_break()



# =====================================================================
#  UNIT IV  -  IMPLANTS AND INSERTS
# =====================================================================
def unit4(n):
    n.unit_title("Unit IV \u2013 Implants and Inserts")

    n.h2("4.1 Introduction & Definition")
    n.para(segments=[
        ("An implant ", True),
        ("is a sterile, solid dosage form (device) of a suitable size and shape that is placed "
         "into the body \u2013 usually subcutaneously or intramuscularly \u2013 by injection or "
         "surgical insertion, where it releases the drug over a prolonged period (weeks to "
         "years). An ", ),
        ("insert ", True),
        ("is a similar rate-controlled device placed into a body cavity or orifice such as the "
         "eye (ocular insert), vagina (vaginal ring) or uterus (intra-uterine device).", )])
    n.para("Implants and inserts are the ultimate long-acting controlled-release systems. Because "
           "they bypass the GI tract, they avoid first-pass metabolism and GI degradation, deliver "
           "at a constant (often zero-order) rate, and dramatically improve patient compliance "
           "(a single insertion may last months). Their chief limitations are the need for a "
           "minor surgical / invasive procedure for insertion (and sometimes removal), the risk "
           "of local tissue reaction, and the difficulty of terminating therapy abruptly.")
    n.figure("implant_sites.png", "Common sites for implants and inserts in the body", width=3.4)

    n.h3("Classification of implantable systems")
    n.bullets([
        [("Non-biodegradable implants : ", True), ("made of inert polymers (silicone / PDMS, "
         "ethylene-vinyl acetate, polyurethane); must be surgically removed after use "
         "(e.g., Norplant\u00ae).")],
        [("Biodegradable implants : ", True), ("made of erodible polymers (PLA, PLGA, "
         "polyanhydrides); do not require removal (e.g., Zoladex\u00ae, Gliadel\u00ae wafer).")],
        [("Pump / osmotic implants : ", True), ("e.g., the DUROS\u00ae osmotic implant and "
         "implantable infusion pumps that deliver at a programmable rate.")],
    ])

    # ---------------------------------------------------------------- biocompatibility
    n.h2("4.2 Biocompatibility : Reaction of Host to Implant & Implant to Host")
    n.para("Biocompatibility is the ability of a material to perform with an appropriate host "
           "response in a specific application. Because an implant is a foreign body, the tissue "
           "and the implant interact in two directions.")

    n.h3("Reaction of the Host to the Implant (tissue response)")
    n.para("When a device is implanted it causes injury and initiates the classical foreign-body "
           "reaction, which proceeds through the following overlapping stages :")
    n.figure("host_reaction.png", "Sequence of host response (foreign-body reaction) to an implant",
             width=5.6)
    n.numbered([
        [("Injury & protein adsorption : ", True), ("implantation injures tissue; blood proteins "
         "immediately adsorb onto the surface forming a provisional matrix.")],
        [("Acute inflammation : ", True), ("neutrophils and exudate arrive (minutes to days).")],
        [("Chronic inflammation : ", True), ("monocytes / macrophages and lymphocytes "
         "predominate (days to weeks).")],
        [("Granulation tissue : ", True), ("fibroblasts and new capillaries proliferate.")],
        [("Foreign-body giant cells : ", True), ("macrophages fuse on the surface in an attempt "
         "to engulf the implant.")],
        [("Fibrous encapsulation : ", True), ("a collagenous fibrous capsule walls off the "
         "implant. A thick capsule can act as an additional diffusion barrier and slow release.")],
    ])
    n.para("The intensity of this response depends on the size, shape, surface chemistry, "
           "roughness, degradation products and the movement of the implant. A biocompatible "
           "material provokes only a thin, quiescent capsule.")

    n.h3("Reaction of the Implant to the Host (material response)")
    n.para("Conversely, the biological environment acts on the implant : body fluids, enzymes, "
           "pH, ions and mechanical stress can cause the material to degrade, swell, corrode, "
           "leach additives, absorb lipids or lose mechanical strength. For biodegradable "
           "implants this degradation is intentional and controlled; for non-biodegradable "
           "implants any degradation is undesirable and may release toxic products. The "
           "degradation products must be non-toxic, non-carcinogenic and readily eliminated.")
    n.box("Requirements of an ideal implant material", [
        "Biocompatible, non-toxic, non-carcinogenic and non-allergenic.",
        "Chemically & physically stable (or predictably biodegradable) in the body.",
        "Adequate mechanical strength; easy to sterilise; able to give the desired release rate.",
        "Degradation products (if any) must be safe and eliminable.",
    ], kind="HIGH-YIELD")

    # ---------------------------------------------------------------- subcutaneous
    n.h2("4.3 Subcutaneous Implants")
    n.para("Subcutaneous implants are small rods, pellets, capsules or discs inserted under the "
           "skin (usually of the upper arm) using a trocar or a minor incision. Because the "
           "subcutaneous tissue is relatively avascular and easily accessible, it is the "
           "preferred site for long-acting implants; insertion and removal are simple.")
    n.figure("implant_release.png", "Zero-order release characteristic of a well-designed implant",
             width=4.8)
    n.h3("Design types")
    n.bullets([
        [("Reservoir (membrane) implants : ", True), ("a drug core within a rate-controlling "
         "silicone or EVA membrane \u2013 gives near zero-order release (e.g., Norplant\u00ae "
         "levonorgestrel rods; Implanon\u00ae / Nexplanon\u00ae etonogestrel).")],
        [("Matrix (monolithic) implants : ", True), ("drug dispersed in a polymer rod; release "
         "declines with \u221at.")],
        [("Biodegradable implants : ", True), ("e.g., Zoladex\u00ae (goserelin in PLGA depot) "
         "for prostate cancer; no removal needed.")],
    ])
    n.h3("Applications")
    n.bullets([
        "Long-acting contraception (levonorgestrel, etonogestrel implants \u2013 up to 3\u20135 yr).",
        "Hormone therapy (testosterone, estradiol pellets).",
        "Cancer therapy (goserelin, leuprolide depots).",
        "Narcotic antagonist / de-addiction (naltrexone implants).",
    ])

    # ---------------------------------------------------------------- intramuscular
    n.h2("4.4 Intramuscular Implants & Depot Injections")
    n.para("The intramuscular site is highly vascular, so absorption is faster than from the "
           "subcutaneous site; it is therefore used for injectable depot systems (oily "
           "solutions, aqueous suspensions, microspheres and in-situ forming implants) rather "
           "than for solid rods that would be difficult to remove. Drug is released slowly by "
           "dissolution / partitioning from the depot.")
    n.bullets([
        [("Oily / esterified depots : ", True), ("lipophilic esters in an oily vehicle (e.g., "
         "testosterone enanthate, fluphenazine decanoate) release drug over weeks.")],
        [("Aqueous microcrystalline suspensions : ", True), ("e.g., procaine penicillin, "
         "medroxyprogesterone acetate (Depo-Provera\u00ae).")],
        [("Biodegradable microspheres : ", True), ("PLGA microspheres of leuprolide "
         "(Lupron Depot\u00ae).")],
        [("In-situ forming implants : ", True), ("a polymer solution that solidifies into a depot "
         "on injection (e.g., Atrigel\u00ae, Eligard\u00ae leuprolide).")],
    ])

    # ---------------------------------------------------------------- intraocular
    n.h2("4.5 Intra-ocular Inserts")
    n.para("Conventional eye drops have very poor ocular bioavailability (< 5 %) because of rapid "
           "drainage, tear turnover and naso-lacrimal loss, and give large pulses in "
           "concentration. Ocular inserts are solid or semisolid rate-controlled devices placed "
           "in the cul-de-sac (conjunctival sac) that release drug at a constant rate for "
           "prolonged periods, greatly improving bioavailability and patient compliance.")
    n.figure("ocular_insert.png", "Ocusert\u00ae reservoir-type ocular insert (cross-section)",
             width=4.2)
    n.h3("Classification of ocular inserts")
    n.bullets([
        [("Insoluble inserts : ", True), ("reservoir (Ocusert\u00ae Pilo \u2013 pilocarpine "
         "between two EVA membranes for glaucoma; zero-order for 7 days) and diffusional / "
         "osmotic types; must be removed.")],
        [("Soluble inserts : ", True), ("made of soluble natural or synthetic polymers (e.g., "
         "SODI\u00ae, Lacrisert\u00ae hydroxypropylcellulose) that dissolve and need no "
         "removal.")],
        [("Bio-erodible inserts : ", True), ("made of erodible polymers.")],
    ])
    n.para("Advantages : prolonged contact and increased bioavailability, accurate dosing, "
           "reduced systemic side effects and better compliance. Disadvantages : foreign-body "
           "sensation, occasional movement / loss of the insert and difficulty of "
           "self-insertion.")

    # ---------------------------------------------------------------- intravaginal
    n.h2("4.6 Intra-vaginal Inserts (Vaginal Rings)")
    n.para("The vaginal mucosa is richly vascularised and permeable, allowing systemic delivery "
           "that avoids the GI tract and first-pass metabolism, as well as local therapy. Vaginal "
           "rings are flexible, doughnut-shaped elastomeric (silicone / EVA) devices that a woman "
           "can insert and remove herself and that release steroids at a controlled rate for weeks "
           "to months.")
    n.bullets([
        [("Reservoir / core rings : ", True), ("drug core surrounded by a rate-controlling "
         "sheath.")],
        [("Matrix rings : ", True), ("drug dispersed throughout the elastomer.")],
        [("Examples : ", True), ("NuvaRing\u00ae (etonogestrel + ethinyl-estradiol, monthly "
         "contraception); Estring\u00ae / Femring\u00ae (estradiol for menopausal therapy).")],
    ])

    # ---------------------------------------------------------------- intrauterine
    n.h2("4.7 Intra-uterine Systems (IUDs / IUS)")
    n.para("Intra-uterine devices deliver drug directly to the uterine cavity, giving high local "
           "concentration with minimal systemic exposure, for very long durations (up to 5\u201310 "
           "years). Modern medicated intra-uterine systems combine the mechanical contraceptive "
           "action of the device with the pharmacological action of a released agent.")
    n.figure("iud_device.png", "T-shaped medicated intra-uterine system (Progestasert\u00ae type)",
             width=2.6)
    n.bullets([
        [("Progesterone-releasing IUS : ", True), ("Progestasert\u00ae released progesterone "
         "from a T-shaped reservoir for ~1 year.")],
        [("Levonorgestrel IUS : ", True), ("Mirena\u00ae releases levonorgestrel for up to 5 "
         "years; used for contraception and menorrhagia.")],
        [("Copper IUDs : ", True), ("release cupric ions that are spermicidal (e.g., "
         "CuT-380A).")],
    ])
    n.para("Advantages : very long action, high compliance, reversible, local action with low "
           "systemic levels. Disadvantages : insertion by a trained professional, risk of "
           "expulsion, uterine irritation, cramping or bleeding.")

    n.h2("4.8 Comparative Summary of Implant / Insert Sites")
    n.table(
        ["Site", "Typical system", "Duration", "Example"],
        [
            ["Subcutaneous", "Reservoir / matrix rod", "Months\u2013years", "Norplant, Implanon"],
            ["Intramuscular", "Depot injection / microspheres", "Weeks\u2013months", "Lupron Depot"],
            ["Intra-ocular", "Reservoir insert", "Up to 1 week+", "Ocusert Pilo"],
            ["Intra-vaginal", "Elastomeric ring", "Weeks\u2013months", "NuvaRing, Estring"],
            ["Intra-uterine", "Medicated T-device", "1\u201310 years", "Mirena, Progestasert"],
        ],
        widths=[1.4, 2.2, 1.4, 1.5],
        fontsize=9.5,
    )
    n.page_break()



# =====================================================================
#  UNIT V  -  TRANSDERMAL DRUG DELIVERY SYSTEMS
# =====================================================================
def unit5(n):
    n.unit_title("Unit V \u2013 Transdermal Drug Delivery Systems")

    n.h2("5.1 Introduction & Definition")
    n.para(segments=[
        ("A transdermal drug delivery system (TDDS) ", True),
        ("is a self-contained, discrete dosage form (a 'patch') which, when applied to the intact "
         "skin, delivers the drug through the skin at a controlled rate into the systemic "
         "circulation. It provides a non-invasive, painless and continuous route that bypasses "
         "the gastrointestinal tract and hepatic first-pass metabolism.", )])
    n.h3("Advantages")
    n.bullets([
        "Avoids first-pass metabolism and GI degradation / irritation.",
        "Provides controlled, constant (often zero-order) plasma levels for a prolonged time.",
        "Reduces dosing frequency and improves compliance.",
        "Therapy can be terminated simply by removing the patch.",
        "Useful for drugs with a short half-life and narrow therapeutic index.",
        "Suitable for unconscious or nauseated patients.",
    ])
    n.h3("Disadvantages / Limitations")
    n.bullets([
        "Only potent drugs (dose usually < 10\u201320 mg/day) can be delivered because skin "
        "permeability is limited.",
        "The stratum corneum is a formidable barrier \u2013 large or hydrophilic molecules "
        "permeate poorly.",
        "Possibility of local skin irritation, erythema or sensitisation.",
        "Not suitable for drugs that irritate the skin or are extensively metabolised in skin.",
        "Comparatively expensive; adhesion problems with sweat / movement.",
    ])

    n.h2("5.2 Fundamentals of Skin Permeation")
    n.para("The skin comprises three principal layers : the epidermis (whose outermost, dead, "
           "keratinised layer, the stratum corneum, is the main permeation barrier), the dermis "
           "(vascularised connective tissue containing the capillaries that carry absorbed drug "
           "away), and the subcutaneous fat. The stratum corneum behaves as a 'brick-and-mortar' "
           "structure \u2013 keratin-filled corneocytes (bricks) embedded in intercellular lipid "
           "lamellae (mortar).")
    n.figure("skin_structure.png", "Structure of skin and the path of transdermal permeation",
             width=5.4)
    n.h3("Routes of permeation across the skin")
    n.figure("permeation_routes.png",
             "Transcellular, intercellular and appendageal routes of skin permeation", width=5.2)
    n.bullets([
        [("Transcellular (intracellular) route : ", True), ("directly through the corneocytes "
         "and lipid \u2013 requires repeated partitioning; shorter path but many barriers.")],
        [("Intercellular route : ", True), ("through the tortuous lipid matrix between "
         "corneocytes \u2013 the predominant pathway for most drugs.")],
        [("Appendageal (trans-follicular) route : ", True), ("through hair follicles, sebaceous "
         "and sweat glands \u2013 a minor pathway (~0.1 % of surface area) but important early "
         "and for ions / large molecules.")],
    ])
    n.h3("Permeation kinetics \u2013 Fick's law, flux and lag time")
    n.para("Steady-state permeation across the skin obeys Fick's first law of diffusion :")
    n.formula("J\u209b\u209b = (D \u00d7 K \u00d7 \u0394C) / h = P \u00d7 \u0394C")
    n.para("where J\u209b\u209b = steady-state flux, D = diffusion coefficient in the stratum "
           "corneum, K = partition coefficient (skin/vehicle), \u0394C = concentration gradient, "
           "h = thickness of the barrier and P = permeability coefficient (P = D\u00b7K/h). The "
           "cumulative amount permeated plotted against time is linear at steady state; "
           "extrapolation of this line to the time-axis gives the lag time :")
    n.formula("Lag time  t\u2097 = h\u00b2 / (6 \u00d7 D)")
    n.figure("permeation_kinetics.png",
             "Permeation profile showing steady-state flux (slope) and lag time", width=4.6)

    n.h2("5.3 Approaches / Penetration Enhancement")
    n.para("Because the stratum corneum limits delivery, several chemical, physical and "
           "formulation approaches are used to enhance permeation.")
    n.h3("(a) Chemical penetration enhancers")
    n.para("These reversibly reduce the barrier resistance of the stratum corneum by disrupting "
           "the ordered lipid, increasing drug partitioning or fluidising the membrane. Examples "
           ": water, alcohols (ethanol), sulphoxides (DMSO), fatty acids (oleic acid), Azone "
           "(laurocapram), surfactants, terpenes, propylene glycol and urea.")
    n.h3("(b) Physical / active enhancement techniques")
    n.bullets([
        [("Iontophoresis : ", True), ("application of a small electric current to drive ionised "
         "/ charged drug molecules across the skin (electro-repulsion) and to induce "
         "electro-osmotic flow. Delivery is proportional to the current and can be switched on/off "
         "\u2013 giving programmable delivery (e.g., lidocaine, pilocarpine).")],
        [("Sonophoresis (phonophoresis) : ", True), ("use of ultrasound to enhance permeation. "
         "Low-frequency ultrasound produces cavitation that transiently disrupts the stratum "
         "corneum lipids, greatly increasing permeability, even of macromolecules such as "
         "insulin.")],
        [("Electroporation : ", True), ("short high-voltage pulses create transient aqueous pores "
         "in the lipid bilayers.")],
        [("Microneedles : ", True), ("micron-sized needles painlessly create micro-channels "
         "through the stratum corneum.")],
        [("Others : ", True), ("magnetophoresis, thermal / laser ablation, needle-free jet "
         "injection.")],
    ])
    n.figure("iontophoresis.png", "Iontophoresis \u2013 electrically assisted transdermal delivery",
             width=4.6)
    n.figure("sonophoresis.png", "Sonophoresis \u2013 ultrasound-assisted transdermal delivery",
             width=4.4)

    n.h2("5.4 Formulation Design & Types of Transdermal Patches")
    n.para("A transdermal patch consists of the following components : the backing membrane "
           "(occlusive, protects from the environment), the drug reservoir or matrix, the "
           "rate-controlling membrane (in reservoir types), the pressure-sensitive adhesive that "
           "attaches the patch to the skin, and the release liner (removed before use).")
    n.figure("tdds_types.png", "Reservoir, drug-in-adhesive and matrix-dispersion transdermal "
             "patches", width=5.6)
    n.h3("Types")
    n.bullets([
        [("Reservoir (membrane-controlled) system : ", True), ("drug solution / gel held between "
         "the backing and a rate-controlling polymeric membrane; gives zero-order release but "
         "risk of dose dumping on membrane rupture.")],
        [("Matrix / monolithic system : ", True), ("drug dispersed in a polymer matrix; the "
         "matrix itself controls release (Higuchi kinetics).")],
        [("Drug-in-adhesive system : ", True), ("drug incorporated directly in the adhesive layer "
         "\u2013 thin, comfortable, single-layer; the commonest modern design.")],
        [("Micro-reservoir system : ", True), ("hybrid combining reservoir and matrix "
         "principles \u2013 tiny drug reservoirs dispersed in a polymer matrix.")],
    ])

    n.h2("5.5 Formulation Considerations & Optimization")
    n.h3("Drug selection criteria for TDDS")
    n.bullets([
        "Molecular weight preferably < 500 Da.",
        "Adequate lipophilicity : log P about 1\u20133 (balanced partitioning).",
        "Low melting point (< 200 \u00b0C) and moderate solubility in both oil and water.",
        "Potent drug \u2013 effective daily dose low (ideally < 10\u201320 mg).",
        "Short biological half-life and non-irritant, non-sensitising to skin.",
    ])
    n.h3("Optimization of the formulation")
    n.para("The formulation is optimised (often using factorial / response-surface design of "
           "experiments) with respect to the type and amount of polymer, plasticiser, penetration "
           "enhancer and adhesive, so as to obtain the target flux, adequate adhesion and skin "
           "compatibility. In-vitro permeation studies through excised skin or synthetic "
           "membranes in Franz diffusion cells are used to measure flux, permeability coefficient "
           "and lag time, and to establish an in-vitro / in-vivo correlation.")

    n.h2("5.6 Evaluation of Transdermal Systems")
    n.bullets([
        [("Physical : ", True), ("thickness, weight uniformity, folding endurance, moisture "
         "content / uptake, tensile strength.")],
        [("Adhesion tests : ", True), ("peel adhesion, tack and shear strength.")],
        [("Drug content & content uniformity.", True), ("")],
        [("In-vitro release & permeation : ", True), ("Franz diffusion cell across skin / "
         "membrane; flux, permeability, lag time.")],
        [("Skin irritation / sensitisation studies.", True), ("")],
        [("Stability studies as per ICH.", True), ("")],
    ])

    n.h2("5.7 Latest Developments & Applications")
    n.para("Recent advances include microneedle patches (solid, coated, dissolving and hollow), "
           "'smart' feedback-controlled iontophoretic patches, needle-free delivery of vaccines "
           "and biologics, and transdermal delivery of peptides / proteins using low-frequency "
           "sonophoresis. Marketed TDDS include nitroglycerin, nicotine, fentanyl, clonidine, "
           "scopolamine, estradiol, testosterone and rivastigmine patches.")
    n.page_break()



# =====================================================================
#  UNIT VI  -  PERSONALIZED MEDICINE
# =====================================================================
def unit6(n):
    n.unit_title("Unit VI \u2013 Personalized Medicine")

    n.h2("6.1 Introduction & Definition")
    n.para("The traditional 'one-size-fits-all' approach to drug therapy assumes that a given "
           "dose of a given drug will produce a similar response in all patients. In reality, "
           "patients differ widely in their response owing to genetic, physiological, "
           "environmental and lifestyle differences, so that the same drug may be ineffective in "
           "some and toxic in others. Personalized (individualised / precision) medicine seeks to "
           "tailor the choice of drug, the dose and the delivery to the characteristics of the "
           "individual patient.")
    n.para(segments=[
        ("Definition : ", True),
        ("Personalized medicine is a medical model that uses an individual's genetic, "
         "molecular, biomarker and clinical information to tailor prevention, diagnosis and "
         "treatment \u2013 delivering the right drug, at the right dose, to the right patient, at "
         "the right time.", )])
    n.figure("personalized_workflow.png", "Work-flow of personalized medicine", width=5.4)
    n.h3("Aims / advantages")
    n.bullets([
        "Maximise efficacy while minimising adverse drug reactions.",
        "Select responders and avoid treating non-responders (companion diagnostics).",
        "Individualise the dose to the patient's metabolic capacity.",
        "Enable early / predictive and preventive intervention.",
        "Reduce trial-and-error prescribing and overall cost of therapy.",
    ])

    n.h2("6.2 Pharmacogenetics & Pharmacogenomics")
    n.para(segments=[
        ("Pharmacogenetics ", True),
        ("is the study of how variations in a single gene influence an individual's response to a "
         "drug, whereas ", ),
        ("pharmacogenomics ", True),
        ("is the broader study of how the entire genome (many genes) affects drug response. Both "
         "form the scientific basis of personalized medicine.", )])
    n.para("Genetic polymorphisms may affect pharmacokinetics (drug-metabolising enzymes, "
           "transporters) or pharmacodynamics (receptors, targets). The most important examples "
           "involve the cytochrome-P450 enzymes.")
    n.figure("metabolizer_types.png",
             "Pharmacogenetic metabolizer phenotypes (illustrated for CYP2D6)", width=4.8)
    n.h3("Metabolizer phenotypes")
    n.bullets([
        [("Poor metabolizers (PM) : ", True), ("deficient enzyme activity \u2013 drug accumulates; "
         "risk of toxicity at standard doses (or failure to activate a prodrug).")],
        [("Intermediate metabolizers (IM) : ", True), ("reduced activity.")],
        [("Extensive metabolizers (EM) : ", True), ("normal 'wild-type' activity.")],
        [("Ultra-rapid metabolizers (UM) : ", True), ("increased activity \u2013 drug cleared too "
         "fast; therapeutic failure, or excessive activation of a prodrug.")],
    ])
    n.h3("Clinical pharmacogenetic examples")
    n.table(
        ["Gene / marker", "Drug", "Clinical relevance"],
        [
            ["CYP2C9 / VKORC1", "Warfarin", "Dose individualisation to avoid bleeding"],
            ["CYP2D6", "Codeine, tamoxifen", "PM \u2013 no analgesia; UM \u2013 toxicity"],
            ["TPMT", "Azathioprine / 6-MP", "Low activity \u2192 severe myelosuppression"],
            ["HLA-B*57:01", "Abacavir", "Hypersensitivity reaction \u2013 test before use"],
            ["HER2 (Neu)", "Trastuzumab", "Only HER2-positive breast cancers respond"],
            ["EGFR mutation", "Gefitinib / erlotinib", "Predicts response in NSCLC"],
            ["UGT1A1", "Irinotecan", "Reduced activity \u2192 toxicity"],
        ],
        widths=[1.7, 1.9, 2.9],
        fontsize=9.0,
    )

    n.h2("6.3 Categories of Patients for Personalized Medicine")
    n.para("Personalized approaches are especially valuable for the following categories of "
           "patients, in whom variability or special needs make standard therapy risky or "
           "sub-optimal :")
    n.bullets([
        "Patients on drugs with a narrow therapeutic index (e.g., warfarin, digoxin, "
        "immunosuppressants).",
        "Patients with known genetic polymorphisms in metabolising enzymes / targets.",
        "Cancer patients (tumour molecular profiling guides targeted therapy).",
        "Paediatric and geriatric patients (special dose and formulation needs).",
        "Patients with organ (hepatic / renal) impairment altering pharmacokinetics.",
        "Patients showing unusual response \u2013 non-responders or those with adverse reactions.",
        "Patients requiring complex multi-drug regimens (polypharmacy).",
    ])

    n.h2("6.4 Customized Drug Delivery Systems")
    n.para("Once the individual requirement is known, the delivery system itself can be "
           "customised \u2013 in dose, combination, release profile, size and shape \u2013 to suit "
           "the patient. Approaches include :")
    n.bullets([
        [("Individualised dosing : ", True), ("compounding or printing the exact dose required "
         "for a specific patient rather than commercial fixed strengths.")],
        [("Polypills / fixed-dose combinations : ", True), ("multiple drugs a patient needs "
         "combined in one unit to improve adherence.")],
        [("Tailored release profiles : ", True), ("chronotherapeutic or multi-phasic release "
         "matched to the patient's disease rhythm.")],
        [("Patient-friendly forms : ", True), ("orodispersible, chewable or flavoured forms for "
         "children and the elderly.")],
        [("Point-of-care / on-demand manufacture : ", True), ("small-scale production (e.g., 3D "
         "printing) at the pharmacy or hospital.")],
    ])

    n.h2("6.5 Bioelectronic Medicines")
    n.para("Bioelectronic medicine (electroceuticals) is an emerging field that uses electrical "
           "impulses delivered by miniature implanted devices to modulate the activity of nerves "
           "and organs, instead of (or in addition to) chemical drugs. By reading and correcting "
           "the electrical signalling of the body's neural circuits, these devices aim to treat "
           "disease with high precision and few systemic side effects.")
    n.figure("bioelectronic.png", "Principle of a bioelectronic (neuromodulation) device", width=5.0)
    n.h3("Examples & applications")
    n.bullets([
        "Cardiac pacemakers and implantable cardioverter-defibrillators.",
        "Deep-brain stimulation for Parkinson's disease and essential tremor.",
        "Vagus-nerve stimulation for epilepsy, depression and inflammatory disease.",
        "Spinal-cord stimulators for chronic pain.",
        "Cochlear implants; sacral-nerve stimulation for bladder control.",
    ])
    n.para("Advantages : highly targeted, drug-free, reversible and adjustable. Limitations : "
           "invasive implantation, device / battery maintenance and high cost.")

    n.h2("6.6 3D Printing of Pharmaceuticals")
    n.para("Three-dimensional (3D) printing is an additive manufacturing technique that builds a "
           "solid object layer-by-layer from a digital design. Applied to pharmaceuticals, it "
           "allows on-demand fabrication of dosage forms with a precisely controlled dose, "
           "geometry, internal structure and release profile \u2013 a powerful enabler of "
           "personalized medicine.")
    n.figure("printing_3d.png", "Fused-deposition-modelling 3D printing of a tablet", width=4.0)
    n.h3("Common 3D-printing techniques for medicines")
    n.bullets([
        [("Fused deposition modelling (FDM) : ", True), ("a drug-loaded polymer filament is "
         "melted and extruded layer-by-layer.")],
        [("Powder-based binder-jet printing : ", True), ("a liquid binder is jetted onto powder "
         "layers (used for Spritam\u00ae, the first FDA-approved 3D-printed tablet, a "
         "rapidly-disintegrating levetiracetam form).")],
        [("Stereolithography (SLA) : ", True), ("a photopolymer resin is cured by light "
         "layer-by-layer \u2013 high resolution.")],
        [("Semi-solid extrusion (SSE) : ", True), ("a paste / gel is extruded \u2013 suitable at "
         "room temperature for heat-labile drugs.")],
    ])
    n.h3("Advantages of 3D-printed medicines")
    n.bullets([
        "Precise, flexible and individualised dosing (any strength).",
        "Complex geometries and multi-drug 'polyprintlets' with tailored release.",
        "Rapid prototyping and on-demand, decentralised manufacture.",
        "Reduction of excipients and possibility of highly porous, fast-dissolving tablets.",
    ])
    n.para("Challenges include regulatory approval, quality control of small batches, limited "
           "range of pharmaceutical-grade printable materials and stability during processing.")

    n.h2("6.7 Telepharmacy")
    n.para("Telepharmacy is the delivery of pharmaceutical care and services by a registered "
           "pharmacist to patients at a distance through the use of telecommunications and "
           "information technology, when direct, in-person contact is not possible. It extends "
           "pharmacy services to remote, rural and under-served areas.")
    n.figure("telepharmacy.png", "Telepharmacy \u2013 remote delivery of pharmaceutical care",
             width=5.2)
    n.h3("Services & applications")
    n.bullets([
        "Remote order entry, prescription review and verification by a pharmacist.",
        "Tele-counselling and patient education via video link.",
        "Remote supervision of dispensing at a satellite / automated site.",
        "Medication-therapy management and monitoring of chronic patients.",
        "Support for rural hospitals lacking an on-site pharmacist.",
    ])
    n.para("Advantages : improved access, cost savings, expanded reach and continuity of care. "
           "Limitations : dependence on technology / connectivity, data-privacy and security "
           "concerns, licensing / regulatory issues and the absence of physical examination.")
    n.page_break()



# =====================================================================
#  ADDITIONAL SECTION - POLYMERS & MATERIALS IN DDS
# =====================================================================
def polymers(n):
    n.unit_title("Selection of Drugs & Polymers for Delivery Systems")

    n.h2("A.1 Why Polymers are Central to Advanced DDS")
    n.para("Polymers are the workhorses of novel drug delivery. They form the membranes, "
           "matrices, coats and scaffolds that control the rate, time and place of drug release. "
           "The choice of polymer determines whether the release is diffusion-, dissolution-, "
           "osmotic- or erosion-controlled, and whether the device is biodegradable or must be "
           "removed. This section consolidates the polymer knowledge required across all units.")

    n.h2("A.2 Criteria for Selection of a Drug for a Novel DDS")
    n.para("The general criteria (detailed in Units I and V) are summarised : appropriate "
           "molecular size and solubility, suitable partition coefficient, an intermediate "
           "biological half-life, low effective dose, good stability, adequate therapeutic index "
           "and uniform absorption. The specific requirement varies with the system (e.g., high "
           "potency for TDDS and implants; ionisable for ion-exchange systems and iontophoresis).")

    n.h2("A.3 Criteria for Selection of a Polymer")
    n.bullets([
        "Biocompatible, non-toxic, non-immunogenic and non-carcinogenic.",
        "Chemically compatible and non-reactive with the drug.",
        "Able to provide the desired release rate and mechanical properties.",
        "Easily processed and sterilisable; stable on storage.",
        "For biodegradable systems : predictable, controllable degradation to safe products.",
        "Economical and readily available in pharmaceutical grade.",
    ])

    n.h2("A.4 Classification of Polymers used in DDS")
    n.h3("(a) Natural polymers")
    n.para("Gelatin, gum acacia, sodium alginate, chitosan, starch, albumin, zein, guar gum, "
           "xanthan gum, cellulose. Generally biocompatible and biodegradable, but batch "
           "variability and microbial contamination are concerns.")
    n.h3("(b) Synthetic non-biodegradable polymers")
    n.para("Silicone (polydimethylsiloxane, PDMS), ethylene-vinyl acetate (EVA), polyurethane, "
           "poly(methyl methacrylate), ethylcellulose, polyethylene. Used for reservoir "
           "membranes and non-degradable implants that must be removed.")
    n.h3("(c) Synthetic biodegradable polymers")
    n.para("Poly(lactic acid) (PLA), poly(glycolic acid) (PGA), poly(lactic-co-glycolic acid) "
           "(PLGA), poly-\u03b5-caprolactone (PCL), polyanhydrides and poly-ortho-esters. Erode "
           "in the body to safe metabolites and need no removal \u2013 the mainstay of injectable "
           "depots and implants.")
    n.h3("(d) pH-dependent (enteric) & other functional polymers")
    n.para("Cellulose acetate phthalate, hydroxypropylmethylcellulose phthalate, shellac and the "
           "methacrylic-acid copolymers (Eudragit\u00ae L, S, RS, RL) provide site-specific "
           "(enteric / colonic) release and film coating.")

    n.table(
        ["Rate-control mechanism", "Representative polymers"],
        [
            ["Diffusion (reservoir membrane)", "Silicone, EVA, ethylcellulose"],
            ["Diffusion / swelling matrix", "HPMC, carbopol, sodium alginate"],
            ["Dissolution / erosion", "Waxes, PLGA, polyanhydrides"],
            ["Osmotic", "Cellulose acetate (semipermeable membrane)"],
            ["Ion-exchange", "Polacrilin (cross-linked polymethacrylate resins)"],
            ["Mucoadhesion", "Carbopol, chitosan, Na-CMC, thiomers"],
            ["Enteric / site specific", "CAP, HPMCP, Eudragit L/S, shellac"],
        ],
        widths=[2.4, 4.1],
        fontsize=9.5,
    )
    n.page_break()


# =====================================================================
#  IMPORTANT QUESTIONS
# =====================================================================
def important_questions(n):
    n.unit_title("Important Theory Questions")

    n.h2("Long-Answer (10-mark) Questions")
    n.numbered([
        "Define sustained and controlled release. Differentiate between them and discuss the "
        "advantages and disadvantages of SR/CR systems.",
        "Discuss in detail the physicochemical and biological factors influencing the design of "
        "an oral controlled-release dosage form.",
        "Explain the criteria for selection of a drug candidate for a sustained-release dosage "
        "form. Add a note on dosage calculations.",
        "Classify oral controlled drug delivery systems. Describe the design, fabrication and "
        "evaluation of oral CDDS.",
        "Explain diffusion-controlled drug delivery systems (reservoir and matrix) with suitable "
        "equations and diagrams.",
        "Describe osmotically controlled drug delivery systems (EOP and push-pull). Give their "
        "advantages.",
        "Write in detail on microencapsulation : definition, objectives, coating materials and "
        "methods of preparation.",
        "Discuss coacervation-phase separation and spray-drying methods of microencapsulation "
        "with diagrams.",
        "Describe the reaction of the host to an implant and of the implant to the host "
        "(biocompatibility).",
        "Write in detail on ocular inserts \u2013 classification, the Ocusert system, advantages "
        "and limitations.",
        "Discuss the fundamentals of skin permeation and describe the types of transdermal "
        "patches with diagrams.",
        "Explain iontophoresis and sonophoresis as approaches to enhance transdermal delivery.",
        "Define personalized medicine. Explain pharmacogenetics and its role with suitable "
        "examples.",
        "Write in detail on 3D printing of pharmaceuticals and its role in personalized "
        "medicine.",
    ])

    n.h2("Short-Answer (5-mark) Questions")
    n.numbered([
        "Terminology : delayed release, repeat action and site-specific systems.",
        "Therapeutic window and its significance in rate-controlled delivery.",
        "Higuchi equation and its application to matrix systems.",
        "Ion-exchange resin drug delivery systems.",
        "Mucoadhesion \u2013 theories and applications.",
        "Bioerodible drug delivery systems (bulk vs surface erosion).",
        "Release and stability kinetics of microcapsules.",
        "Types of microcapsules / microspheres.",
        "Subcutaneous implants with examples.",
        "Intra-uterine and intra-vaginal drug delivery systems.",
        "Routes of drug permeation across the skin.",
        "Penetration enhancers in TDDS.",
        "Metabolizer phenotypes (PM, IM, EM, UM) with examples.",
        "Bioelectronic medicines.",
        "Telepharmacy \u2013 services, advantages and limitations.",
        "Criteria for selection of polymers for drug delivery systems.",
    ])
    n.page_break()


# =====================================================================
#  GLOSSARY
# =====================================================================
def glossary(n):
    n.unit_title("Glossary of Key Terms")
    n.h2("Glossary")
    terms = [
        ("Sustained release", "System that prolongs the duration of action by releasing drug "
         "slowly; release rate declines with time."),
        ("Controlled release", "System that releases drug at a constant (zero-order) rate to "
         "maintain a constant plasma level."),
        ("Delayed release", "Release of drug at a time other than immediately after "
         "administration (e.g., enteric-coated)."),
        ("Repeat action", "System releasing one dose promptly and another after a lag period."),
        ("Therapeutic window", "Plasma-concentration range between the MEC and the maximum safe "
         "concentration."),
        ("MEC / MTC", "Minimum effective and minimum toxic concentration, respectively."),
        ("Zero-order release", "Constant amount of drug released per unit time, independent of "
         "concentration."),
        ("Higuchi model", "Release proportional to the square-root of time; describes matrix "
         "diffusion."),
        ("Korsmeyer\u2013Peppas", "Empirical model (Mt/M\u221e = k\u00b7t\u207f) used to identify "
         "the release mechanism from the exponent n."),
        ("Reservoir system", "Drug core enclosed in a rate-controlling membrane."),
        ("Matrix system", "Drug dispersed uniformly throughout a polymer."),
        ("Osmotic pump", "Device that delivers drug at a constant rate driven by osmotic "
         "pressure."),
        ("Osmogen", "Osmotically active agent (e.g., NaCl, mannitol) in an osmotic core."),
        ("Ion-exchange resin", "Insoluble polymer that binds an ionised drug and releases it by "
         "exchange with GI ions."),
        ("Mucoadhesion", "Adhesion of a material to the mucus layer to prolong residence time."),
        ("Bioerodible polymer", "Polymer that degrades in the body, releasing drug and leaving "
         "no residue."),
        ("Microencapsulation", "Enclosure of small particles / droplets within a thin coating to "
         "form microcapsules (1\u20131000 \u00b5m)."),
        ("Coacervation", "Phase-separation method of microencapsulation."),
        ("Implant", "Solid device placed in the body (s.c. / i.m.) for prolonged drug release."),
        ("Insert", "Rate-controlled device placed in a body cavity (eye, vagina, uterus)."),
        ("Biocompatibility", "Ability of a material to perform with an appropriate host response."),
        ("Foreign-body reaction", "Host tissue response culminating in fibrous encapsulation of "
         "an implant."),
        ("TDDS", "Transdermal drug delivery system \u2013 a patch delivering drug through intact "
         "skin."),
        ("Stratum corneum", "Outermost dead keratinised layer of skin; the main permeation "
         "barrier."),
        ("Flux (Jss)", "Steady-state amount of drug permeating per unit area per unit time."),
        ("Lag time", "Time before steady-state permeation is established (t\u2097 = h\u00b2/6D)."),
        ("Iontophoresis", "Use of an electric current to drive charged drug across skin."),
        ("Sonophoresis", "Use of ultrasound to enhance transdermal permeation."),
        ("Personalized medicine", "Tailoring therapy to an individual's genetic and molecular "
         "profile."),
        ("Pharmacogenetics", "Study of how single-gene variation affects drug response."),
        ("Pharmacogenomics", "Study of how the whole genome affects drug response."),
        ("Bioelectronic medicine", "Use of electrical impulses from implanted devices to treat "
         "disease."),
        ("3D printing", "Additive, layer-by-layer manufacture of dosage forms with tailored "
         "dose and structure."),
        ("Telepharmacy", "Provision of pharmaceutical care at a distance using telecommunication "
         "technology."),
    ]
    for term, definition in terms:
        n.term(term + " \u2013", definition)
    n.page_break()


# =====================================================================
#  QUICK REVISION
# =====================================================================
def revision(n):
    n.unit_title("Quick Revision")

    n.h2("Unit I \u2013 SR / CR Formulations")
    n.bullets([
        "SR prolongs action (rate declines); CR maintains a constant level (zero-order).",
        "Ideal drug : MW < 500, t\u00bd 2\u20138 h, dose < 0.5 g, moderate solubility, wide "
        "therapeutic index, uniform GI absorption.",
        "Total dose W = D\u2080 (loading) + D\u2098 (maintenance); K\u1d63\u2080 = C\u209a "
        "\u00d7 k\u2091 \u00d7 Vd.",
        "Advantages : compliance, less fluctuation, lower dose; disadvantage : dose dumping, "
        "cost, hard to reverse.",
    ])
    n.h2("Unit II \u2013 Oral SR Mechanisms")
    n.bullets([
        "Diffusion : reservoir (zero-order, Fick) & matrix (Higuchi, \u221at).",
        "Dissolution : coated beads / slowly-dissolving matrix (Noyes\u2013Whitney).",
        "Osmotic : EOP / push-pull \u2013 zero-order, pH & motility independent.",
        "Ion-exchange : drug\u2013resinate released by GI counter-ions.",
        "Bioerodible : bulk vs surface erosion; mucoadhesive : prolongs residence via "
        "interpenetration.",
    ])
    n.h2("Unit III \u2013 Microencapsulation")
    n.bullets([
        "Size 1\u20131000 \u00b5m; core + wall; types \u2013 mononuclear, polynuclear, matrix.",
        "Objectives : SR, taste masking, stability, liquid\u2192solid, separate incompatibles.",
        "Methods : coacervation (simple / complex), spray drying, Wurster / pan coating, "
        "solvent evaporation.",
        "% Encapsulation efficiency = actual/theoretical \u00d7 100; release fitted to kinetic "
        "models.",
    ])
    n.h2("Unit IV \u2013 Implants & Inserts")
    n.bullets([
        "Implant \u2013 s.c./i.m.; insert \u2013 eye/vagina/uterus.",
        "Host\u2192implant : injury \u2192 inflammation \u2192 giant cells \u2192 fibrous "
        "capsule. Implant\u2192host : degradation / corrosion.",
        "Subcutaneous : Norplant, Implanon; i.m. depot : Lupron, Zoladex.",
        "Ocular : Ocusert (pilocarpine, EVA, 7 days); vaginal : NuvaRing; uterine : Mirena, "
        "Progestasert.",
    ])
    n.h2("Unit V \u2013 Transdermal DDS")
    n.bullets([
        "Barrier = stratum corneum ('brick & mortar'); routes \u2013 transcellular, "
        "intercellular (main), appendageal.",
        "Jss = D\u00b7K\u00b7\u0394C/h = P\u00b7\u0394C; lag time t\u2097 = h\u00b2/6D.",
        "Patch types : reservoir, matrix, drug-in-adhesive, micro-reservoir.",
        "Enhancement : chemical enhancers, iontophoresis (charged drugs), sonophoresis "
        "(ultrasound), microneedles.",
        "Ideal drug : MW < 500, log P 1\u20133, potent (< ~20 mg/day), non-irritant.",
    ])
    n.h2("Unit VI \u2013 Personalized Medicine")
    n.bullets([
        "Right drug, right dose, right patient, right time \u2013 based on genetic / molecular "
        "profile.",
        "Pharmacogenetics (one gene) vs pharmacogenomics (whole genome); phenotypes PM/IM/EM/UM.",
        "Examples : warfarin (CYP2C9/VKORC1), codeine (CYP2D6), abacavir (HLA-B*57:01), "
        "trastuzumab (HER2).",
        "Customized DDS, bioelectronic medicine (electroceuticals), 3D printing (Spritam\u00ae), "
        "telepharmacy.",
    ])
    n.box("Final tip", [
        "For the theory paper, always support answers with a labelled diagram, a definition, a "
        "classification and named examples \u2013 these earn the most marks.",
    ], kind="NOTE")



# =====================================================================
#  UNIT I  -  DEEP DIVE / EXPANSION
# =====================================================================
def unit1_extra(n):
    n.h2("1.9 Pharmacokinetic Basis of Sustained Release")
    n.para("A rational SR design begins with the pharmacokinetics of the drug. For a drug obeying "
           "one-compartment first-order kinetics, the amount of drug in the body at steady state "
           "and the required input rate can be calculated so that the release rate matches the "
           "elimination rate. The important relationships are given below.")
    n.h3("Rate of elimination and desired input rate")
    n.para("At steady state the rate of drug input equals the rate of elimination. For a zero-"
           "order input from the delivery system :")
    n.formula("Input rate (K\u1d63\u2080) = Elimination rate = k\u2091 \u00d7 Ab,ss = k\u2091 \u00d7 Cp,ss \u00d7 Vd")
    n.para("where Ab,ss is the amount in the body at steady state and Cp,ss the steady-state "
           "plasma concentration. Because k\u2091 = 0.693/t\u00bd, drugs with a short half-life "
           "require a proportionally larger maintenance dose, which is why very short-t\u00bd "
           "drugs are impractical for SR.")
    n.h3("The maintenance-to-loading dose ratio")
    n.para("The relative sizes of the loading dose (D\u2080) and the maintenance dose (D\u2098) "
           "depend on the half-life and the intended duration. As the intended duration of "
           "sustaining (T\u1d48) increases or the half-life decreases, the maintenance fraction "
           "grows relative to the loading dose.")
    n.box("Worked Example \u2013 short vs long half-life", [
        "Two drugs A and B both need Cp = 5 mg/L with Vd = 15 L, sustained for 10 h.",
        [("Drug A (t\u00bd = 2 h) : ", True), ("k\u2091 = 0.347 h\u207b\u00b9; K\u1d63\u2080 = 5 "
         "\u00d7 0.347 \u00d7 15 = 26 mg/h; D\u2098 = 260 mg.")],
        [("Drug B (t\u00bd = 6 h) : ", True), ("k\u2091 = 0.116 h\u207b\u00b9; K\u1d63\u2080 = 5 "
         "\u00d7 0.116 \u00d7 15 = 8.7 mg/h; D\u2098 = 87 mg.")],
        [("Conclusion : ", True), ("the short-t\u00bd drug A needs ~3\u00d7 the maintenance dose "
         "\u2013 illustrating why moderate half-lives are preferred.")],
    ], kind="EXAMPLE")

    n.h2("1.10 Release Kinetics & Mathematical Models (in detail)")
    n.para("The in-vitro release data of a CDDS are fitted to mathematical models to characterise "
           "the mechanism and to compare formulations. The principal models are :")
    n.h3("Zero-order model")
    n.formula("Q\u209c = Q\u2080 + k\u2080 t")
    n.para("A plot of cumulative % released versus time is linear; ideal for controlled release. "
           "Osmotic pumps and well-designed reservoir systems approach this behaviour.")
    n.h3("First-order model")
    n.formula("log Q = log Q\u2080 \u2013 (k\u2081 t / 2.303)")
    n.para("A plot of log(% remaining) versus time is linear; typical of matrix systems releasing "
           "water-soluble drugs and of many conventional formulations.")
    n.h3("Higuchi model")
    n.formula("Q = k\u2095 \u221at")
    n.para("Cumulative release is proportional to the square-root of time; describes diffusion-"
           "controlled release from a homogeneous or granular matrix. Assumptions include : "
           "initial drug concentration in the matrix is much higher than solubility; drug "
           "diffusion is one-dimensional; sink conditions are maintained; the matrix does not "
           "dissolve.")
    n.h3("Korsmeyer\u2013Peppas (power-law) model")
    n.formula("Mt / M\u221e = k t\u207f")
    n.para("Used when the mechanism is unknown or more than one type of release is involved. The "
           "release exponent n identifies the mechanism.")
    n.table(
        ["Exponent n (cylinder)", "Release mechanism"],
        [
            ["n \u2264 0.45", "Fickian diffusion (Higuchi)"],
            ["0.45 < n < 0.89", "Anomalous (non-Fickian) transport"],
            ["n = 0.89", "Case-II transport (zero-order, erosion)"],
            ["n > 0.89", "Super case-II transport"],
        ],
        widths=[2.4, 4.1],
        fontsize=9.5,
    )
    n.h3("Hixson\u2013Crowell model")
    n.formula("Q\u2080^(1/3) \u2013 Q\u209c^(1/3) = k t")
    n.para("Describes release from systems where the surface area and diameter change (erosion / "
           "dissolution of particles) \u2013 the 'cube-root' law.")

    n.h2("1.11 In-Vitro / In-Vivo Correlation (IVIVC) for CDDS")
    n.para("IVIVC is a predictive mathematical model describing the relationship between an "
           "in-vitro property of a dosage form (usually the extent or rate of dissolution) and a "
           "relevant in-vivo response (plasma concentration or amount absorbed). A good IVIVC "
           "allows dissolution testing to serve as a surrogate for bioequivalence studies, which "
           "is particularly valuable for CDDS whose performance depends heavily on release.")
    n.table(
        ["Level", "Correlation", "Usefulness"],
        [
            ["Level A", "Point-to-point (dissolution vs absorption)", "Highest; can waive "
             "bioequivalence"],
            ["Level B", "Mean dissolution time vs mean residence time", "Uses statistical moments"],
            ["Level C", "Single point (e.g., % at 1 h vs Cmax)", "Weakest; limited use"],
            ["Multiple C", "Several time points vs a PK parameter", "Better than single C"],
        ],
        widths=[1.2, 3.3, 2.0],
        fontsize=9.5,
    )

    n.h2("1.12 Gastro-retentive Drug Delivery Systems (GRDDS)")
    n.para("Drugs with a narrow absorption window in the upper GI tract, drugs that act locally "
           "in the stomach, or drugs unstable in the intestine benefit from being retained in the "
           "stomach. Gastro-retentive systems prolong gastric residence and thereby improve "
           "absorption and the utility of CDDS.")
    n.h3("Approaches to gastric retention")
    n.bullets([
        [("Floating (low-density) systems : ", True), ("density less than gastric fluid "
         "(< 1.004 g/mL) so the unit floats; effervescent (gas-generating) or non-effervescent "
         "(hydrocolloid gel) types.")],
        [("High-density (sinking) systems : ", True), ("density > 2.5 g/mL so the unit settles "
         "in the antrum and resists emptying.")],
        [("Bioadhesive / mucoadhesive systems : ", True), ("adhere to the gastric mucosa.")],
        [("Swelling / expanding systems : ", True), ("swell to a size too large to pass the "
         "pylorus (plug-type / unfoldable systems).")],
        [("Magnetic systems : ", True), ("retained by an external magnet.")],
        [("Raft-forming systems : ", True), ("form a floating gel raft on gastric contents "
         "(antacid / anti-reflux).")],
    ])
    n.box("High-yield \u2013 GRDDS", [
        "Ideal for narrow-absorption-window drugs (furosemide, riboflavin, L-dopa, captopril).",
        "Floating systems are the most widely used; effervescent types use NaHCO\u2083 + citric "
        "acid to generate CO\u2082.",
        "Not suitable for drugs irritant to the gastric mucosa or unstable in acid.",
    ], kind="HIGH-YIELD")
    n.page_break()



# =====================================================================
#  UNIT II  -  DEEP DIVE / EXPANSION
# =====================================================================
def unit2_extra(n):
    n.h2("2.9 Hydrophilic Matrix Systems & the Gel-Layer Concept")
    n.para("Hydrophilic matrix tablets (e.g., those based on HPMC) are the most popular oral SR "
           "platform because of their simplicity, low cost and safety. On contact with GI fluid "
           "the surface polymer hydrates and forms a viscous gel layer around the tablet. This "
           "gel layer controls both the diffusion of dissolved drug out of the matrix and the "
           "penetration of water in. Release therefore involves three simultaneous fronts :")
    n.bullets([
        [("Swelling front : ", True), ("boundary between the dry glassy core and the rubbery "
         "gel.")],
        [("Diffusion front : ", True), ("boundary between undissolved and dissolved drug within "
         "the gel.")],
        [("Erosion front : ", True), ("outer boundary where the gel erodes into the medium.")],
    ])
    n.para("Water-soluble drugs are released predominantly by diffusion through the gel (Higuchi "
           "kinetics), whereas poorly soluble drugs are released mainly by erosion of the gel "
           "(closer to zero-order). The release rate is governed by polymer type, viscosity "
           "grade, polymer : drug ratio, particle size and tablet geometry.")

    n.h2("2.10 Factors Controlling Osmotic Delivery Rate")
    n.para("The delivery rate of an osmotic system can be programmed by adjusting the following "
           "variables, which makes osmotic pumps very versatile :")
    n.bullets([
        [("Membrane permeability & thickness : ", True), ("thicker or less permeable membrane "
         "slows water influx and hence delivery.")],
        [("Membrane area : ", True), ("larger area increases the rate.")],
        [("Osmotic pressure of the core (osmogen) : ", True), ("higher osmotic pressure "
         "increases the driving force.")],
        [("Solubility of the drug in the pumped fluid : ", True), ("directly proportional to the "
         "amount delivered per unit volume.")],
        [("Size of the delivery orifice : ", True), ("must be within an optimum range \u2013 too "
         "small causes hydrostatic build-up, too large permits diffusion / burst.")],
    ])
    n.table(
        ["Osmotic system", "Feature", "Suitable drug"],
        [
            ["Elementary (EOP)", "Single core + orifice", "Water-soluble"],
            ["Push-pull (bilayer)", "Drug layer + push layer", "Poorly soluble"],
            ["Controlled-porosity", "Pore-formers in membrane", "Various"],
            ["Sandwiched (SOTS)", "Two orifices, central drug", "Various"],
            ["Liquid OROS", "Soft-gelatin liquid core", "Liquid / lipophilic"],
        ],
        widths=[1.8, 2.3, 2.0],
        fontsize=9.5,
    )

    n.h2("2.11 Colon-Targeted Drug Delivery")
    n.para("Delivery to the colon is desirable for the local treatment of colonic diseases "
           "(ulcerative colitis, Crohn's disease, colon cancer) and for the systemic delivery of "
           "proteins / peptides that would be degraded in the upper GI. Because the colon is "
           "distal, several triggers are exploited to release drug specifically there :")
    n.bullets([
        [("pH-dependent systems : ", True), ("coats (Eudragit S/L) that dissolve only at the "
         "higher pH of the terminal ileum / colon.")],
        [("Time-dependent (time-lagged) systems : ", True), ("release after a lag matching the "
         "small-intestinal transit time (~3\u20134 h after gastric emptying).")],
        [("Microbially triggered systems : ", True), ("use polysaccharides (pectin, guar gum, "
         "chitosan, amylose) or azo-polymers degraded specifically by colonic bacteria.")],
        [("Pressure-controlled systems : ", True), ("rupture under the higher luminal pressure of "
         "the colon.")],
    ])

    n.h2("2.12 Pulsatile (Time-Controlled) Delivery")
    n.para("Some diseases follow a circadian rhythm (e.g., early-morning asthma, angina, "
           "arthritis, hypertension) and are best treated by chronotherapy \u2013 delivering the "
           "drug in a pulse at the time of greatest need. Pulsatile systems release the drug "
           "rapidly after a programmed lag time. They may be rupturable (a swelling or "
           "effervescent core that bursts a coat), erodible-coat, or capsule-based (e.g., "
           "Pulsincap\u00ae).")

    n.h2("2.13 Comparative Overview of Oral SR Mechanisms")
    n.table(
        ["Mechanism", "Rate-limiting step", "Typical kinetics", "Advantage / limitation"],
        [
            ["Dissolution", "Coat / matrix dissolution", "First order", "Simple / pH-sensitive"],
            ["Diffusion (reservoir)", "Membrane diffusion", "Zero order", "Constant / dose-dump risk"],
            ["Diffusion (matrix)", "Matrix diffusion", "Higuchi (\u221at)", "Cheap / declining rate"],
            ["Osmotic", "Water influx", "Zero order", "pH-independent / costly"],
            ["Ion-exchange", "Ionic exchange", "Variable", "Liquid SR / diet-dependent"],
            ["Erosion", "Polymer erosion", "Near zero order", "No residue / variable"],
        ],
        widths=[1.5, 1.6, 1.4, 2.0],
        fontsize=8.8,
    )
    n.box("High-yield \u2013 which mechanism gives zero-order?", [
        "Osmotic pumps and (ideally) reservoir-membrane systems give true zero-order release.",
        "Matrix (monolithic) systems give \u221at (Higuchi) release \u2013 rate declines with "
        "time.",
        "Surface-erosion systems approach zero-order; bulk-erosion systems do not.",
    ], kind="HIGH-YIELD")
    n.page_break()



# =====================================================================
#  UNIT III  -  DEEP DIVE / EXPANSION
# =====================================================================
def unit3_extra(n):
    n.h2("3.9 Classification of Microencapsulation Methods")
    n.para("The many techniques are conveniently grouped as physical, physico-chemical and "
           "chemical methods according to the principle by which the wall is formed around the "
           "core.")
    n.table(
        ["Class", "Methods"],
        [
            ["Physical / mechanical", "Spray drying, spray congealing, air-suspension (Wurster) "
             "coating, pan coating, multiorifice-centrifugal, fluid-bed coating"],
            ["Physico-chemical", "Simple & complex coacervation, solvent evaporation, ionotropic "
             "gelation, supercritical-fluid, layer-by-layer"],
            ["Chemical", "Interfacial polymerisation, in-situ polymerisation, "
             "polycondensation"],
        ],
        widths=[1.8, 4.7],
        fontsize=9.5,
    )

    n.h3("Simple vs Complex Coacervation")
    n.table(
        ["Feature", "Simple coacervation", "Complex coacervation"],
        [
            ["Number of polymers", "One", "Two (oppositely charged)"],
            ["Driving force", "Desolvation (salt, alcohol, heat)", "Electrostatic attraction"],
            ["Typical system", "Gelatin + sodium sulphate", "Gelatin (+) + acacia (\u2212)"],
            ["pH dependence", "Low", "Strongly pH-dependent"],
        ],
        widths=[1.6, 2.4, 2.5],
        fontsize=9.3,
    )
    n.para("In complex coacervation, the pH is adjusted below the isoelectric point of gelatin so "
           "that gelatin becomes positively charged and interacts with negatively charged acacia; "
           "the neutralised complex separates as a coacervate that deposits around the core. The "
           "coating is then hardened (cross-linked) with formaldehyde or glutaraldehyde and "
           "cooling.")

    n.h2("3.10 Factors affecting Microencapsulation & Release")
    n.bullets([
        [("Core : coat ratio : ", True), ("influences wall thickness and hence release rate.")],
        [("Wall material & its molecular weight : ", True), ("determine permeability and "
         "mechanical strength.")],
        [("Particle size of the core : ", True), ("smaller cores give larger surface area and "
         "faster release.")],
        [("Method & process variables : ", True), ("temperature, stirring speed, rate of "
         "addition of non-solvent, pH.")],
        [("Solvent & hardening conditions.", True), ("")],
        [("Cross-linking density : ", True), ("higher cross-linking slows release.")],
    ])

    n.h2("3.11 Microspheres in Advanced Delivery")
    n.para("Polymeric microspheres (matrix type) are extensively used as injectable depot systems "
           "and as carriers for targeted delivery. Biodegradable PLGA microspheres of peptides "
           "(leuprolide, octreotide, triptorelin) provide once-monthly to once-3-monthly therapy. "
           "Albumin and starch microspheres, magnetic microspheres and mucoadhesive microspheres "
           "extend the concept to targeting. Bio-adhesive microspheres prolong residence at "
           "mucosal sites; magnetic microspheres can be localised by an external magnetic field.")

    n.h2("3.12 Marketed / Representative Products")
    n.table(
        ["Product principle", "Example"],
        [
            ["Taste-masked micro-capsules", "Micro-encapsulated paracetamol / aspirin"],
            ["Sustained-release beads", "Theo-Dur\u00ae, Spansule\u00ae capsules"],
            ["Depot PLGA microspheres", "Lupron Depot\u00ae (leuprolide)"],
            ["Enteric micro-capsules", "Enteric-coated omeprazole pellets"],
        ],
        widths=[3.0, 3.5],
        fontsize=9.5,
    )
    n.box("High-yield \u2013 Microencapsulation", [
        "Size range 1\u20131000 \u00b5m; below 1 \u00b5m = nanocapsule.",
        "Complex coacervation classic pair = gelatin + acacia (gum arabic); hardened with "
        "glutaraldehyde.",
        "Spray drying = fastest, single-step, good for heat-labile drugs (brief heat exposure).",
        "Encapsulation efficiency = actual / theoretical drug content \u00d7 100.",
    ], kind="HIGH-YIELD")
    n.page_break()


# =====================================================================
#  UNIT IV  -  DEEP DIVE / EXPANSION
# =====================================================================
def unit4_extra(n):
    n.h2("4.9 Advantages & Disadvantages of Implantable Systems")
    n.h3("Advantages")
    n.bullets([
        "Very long duration of action (weeks to years) from a single administration.",
        "Constant, often zero-order release and predictable plasma levels.",
        "Bypass first-pass metabolism and GI degradation.",
        "Excellent patient compliance; useful when oral therapy is unreliable.",
        "Localised delivery with high local and low systemic concentration (inserts).",
        "Lower total dose and fewer systemic side effects.",
    ])
    n.h3("Disadvantages")
    n.bullets([
        "Require a minor surgical / invasive procedure for insertion (and removal of "
        "non-degradable types).",
        "Risk of local tissue reaction, infection or fibrous encapsulation.",
        "Difficult to terminate therapy quickly (device must be removed).",
        "Possibility of dose dumping if a reservoir membrane ruptures.",
        "Patient acceptability and cost.",
    ])

    n.h2("4.10 Biodegradable Polymers for Implants")
    n.para("Biodegradable implants avoid the need for surgical removal. The most important "
           "polymers are the aliphatic polyesters PLA, PGA and their copolymer PLGA, which "
           "hydrolyse to lactic and glycolic acids that enter normal metabolic pathways.")
    n.bullets([
        [("PLA / PGA / PLGA : ", True), ("degrade by bulk hydrolysis of ester bonds; the "
         "lactide : glycolide ratio and molecular weight control the degradation time (weeks to "
         "months). Higher glycolide content degrades faster.")],
        [("Polyanhydrides & poly-ortho-esters : ", True), ("degrade by surface erosion, giving "
         "more nearly zero-order release (e.g., Gliadel\u00ae carmustine wafer for brain "
         "tumours).")],
        [("Poly-\u03b5-caprolactone : ", True), ("very slow degradation \u2013 suited to long-term "
         "(> 1 yr) systems (e.g., Capronor\u00ae contraceptive).")],
        [("Natural polymers : ", True), ("collagen, gelatin, albumin and chitosan.")],
    ])

    n.h2("4.11 In-Situ Forming Implants")
    n.para("These are injectable liquid systems that transform into a solid or semisolid depot "
           "after administration, avoiding surgery. Formation can be triggered by :")
    n.bullets([
        [("Solvent removal / phase inversion : ", True), ("a polymer (PLGA) dissolved in a "
         "biocompatible solvent (NMP) precipitates as the solvent diffuses away "
         "(Atrigel\u00ae / Eligard\u00ae).")],
        [("Thermal gelation : ", True), ("a polymer solution (e.g., poloxamer) that is liquid at "
         "room temperature and gels at body temperature.")],
        [("In-situ cross-linking : ", True), ("chemical or photo cross-linking after "
         "injection.")],
        [("Ionic gelation : ", True), ("alginate gelling with body calcium.")],
    ])

    n.h2("4.12 Implantable Pumps")
    n.para("Implantable pumps deliver drug at a programmable or constant rate for very long "
           "periods :")
    n.bullets([
        [("Osmotic implantable pumps : ", True), ("the DUROS\u00ae system and the ALZET\u00ae "
         "research pump use osmosis to deliver at a constant rate for months (e.g., "
         "Viadur\u00ae leuprolide for 12 months).")],
        [("Infusion / peristaltic pumps : ", True), ("electromechanical pumps for insulin, "
         "chemotherapy or intrathecal analgesia (baclofen, morphine).")],
        [("Programmable pumps : ", True), ("allow the rate to be changed non-invasively by "
         "telemetry.")],
    ])

    n.h2("4.13 Sterilisation & Evaluation of Implants")
    n.para("Because implants are placed in sterile tissue, they must themselves be sterile and "
           "free of pyrogens. Terminal sterilisation is preferred; heat-labile biodegradable "
           "polymers are often sterilised by gamma-irradiation or aseptically processed. "
           "Gamma-irradiation, however, can accelerate degradation of PLGA and must be validated.")
    n.h3("Evaluation")
    n.bullets([
        [("Physical : ", True), ("dimensions, weight, surface morphology (SEM), mechanical "
         "strength.")],
        [("Drug content & uniformity.", True), ("")],
        [("In-vitro release : ", True), ("in a suitable medium, fitted to kinetic models; "
         "accelerated release testing at elevated temperature.")],
        [("Degradation studies : ", True), ("molecular-weight loss, mass loss, morphology over "
         "time (for biodegradable types).")],
        [("Sterility & pyrogen (endotoxin) tests.", True), ("")],
        [("Biocompatibility / tissue-irritation studies in animals.", True), ("")],
        [("In-vivo release & pharmacokinetics.", True), ("")],
    ])

    n.h2("4.14 Representative Marketed Implants & Inserts")
    n.table(
        ["Product", "Drug / use", "Type"],
        [
            ["Norplant\u00ae", "Levonorgestrel (contraception)", "Non-degradable s.c. rods"],
            ["Implanon / Nexplanon\u00ae", "Etonogestrel (contraception)", "s.c. rod"],
            ["Zoladex\u00ae", "Goserelin (prostate cancer)", "Biodegradable s.c. depot"],
            ["Gliadel\u00ae wafer", "Carmustine (brain tumour)", "Biodegradable (polyanhydride)"],
            ["Ocusert\u00ae Pilo", "Pilocarpine (glaucoma)", "Ocular reservoir insert"],
            ["Vitrasert\u00ae", "Ganciclovir (CMV retinitis)", "Intra-ocular implant"],
            ["Mirena\u00ae", "Levonorgestrel (5 yr)", "Intra-uterine system"],
            ["NuvaRing\u00ae", "Etonogestrel + estrogen", "Vaginal ring"],
        ],
        widths=[1.9, 2.5, 2.1],
        fontsize=9.0,
    )
    n.box("High-yield \u2013 Implants & Inserts", [
        "Foreign-body reaction ends in fibrous encapsulation \u2013 a thick capsule slows "
        "release.",
        "PLGA = bulk erosion; polyanhydrides / poly-ortho-esters = surface erosion (nearer "
        "zero-order).",
        "Ocusert delivers pilocarpine at zero-order for 7 days using EVA membranes.",
        "Mirena (levonorgestrel IUS) acts up to 5 years; Progestasert released progesterone for "
        "~1 year.",
    ], kind="HIGH-YIELD")
    n.page_break()



# =====================================================================
#  UNIT V  -  DEEP DIVE / EXPANSION
# =====================================================================
def unit5_extra(n):
    n.h2("5.8 Detailed Skin Anatomy relevant to Permeation")
    n.para("A sound knowledge of skin structure explains why transdermal delivery is so "
           "restricted. The skin is the largest organ (~1.8 m\u00b2, ~10 % of body weight) and "
           "comprises three regions.")
    n.h3("Epidermis")
    n.para("The avascular epidermis (50\u2013100 \u00b5m) is a stratified epithelium. Its "
           "innermost basal layer continuously produces keratinocytes that migrate outward, "
           "differentiate and die, forming the stratum corneum. The stratum corneum "
           "(10\u201320 \u00b5m, ~15\u201320 layers of flattened corneocytes) is the principal "
           "rate-limiting barrier \u2013 a 'brick-and-mortar' arrangement of keratin-rich cells "
           "in a matrix of ordered intercellular lipids (ceramides, cholesterol, free fatty "
           "acids).")
    n.h3("Dermis")
    n.para("The dermis (3\u20135 mm) is vascular connective tissue containing collagen, elastin, "
           "blood and lymph vessels, nerves and the skin appendages (hair follicles, sebaceous "
           "and sweat glands). The rich capillary network here carries the permeated drug into "
           "the systemic circulation, so the dermis usually offers little resistance to lipophilic "
           "drugs but can be a barrier to very lipophilic molecules.")
    n.h3("Subcutaneous tissue (hypodermis)")
    n.para("A layer of fat and connective tissue that anchors the skin and acts as a depot for "
           "highly lipophilic drugs.")

    n.h2("5.9 Factors influencing Transdermal Permeation")
    n.h3("Biological factors")
    n.bullets([
        [("Skin condition : ", True), ("damaged / diseased skin (eczema, burns) is far more "
         "permeable; solvents and vesicants damage the barrier.")],
        [("Skin age : ", True), ("infant and elderly skin differ in permeability.")],
        [("Regional variation : ", True), ("permeability varies with body site (postauricular, "
         "scrotal and forehead skin are more permeable than the forearm).")],
        [("Skin hydration : ", True), ("hydration (occlusion) swells the corneocytes and "
         "increases permeation.")],
        [("Skin temperature & blood flow : ", True), ("higher temperature and blood flow enhance "
         "flux.")],
        [("Skin metabolism : ", True), ("cutaneous enzymes can metabolise the drug (relevant to "
         "prodrugs).")],
    ])
    n.h3("Physicochemical factors")
    n.bullets([
        [("Partition coefficient : ", True), ("a balanced log P (~1\u20133) is optimum; too "
         "hydrophilic cannot cross lipid, too lipophilic cannot leave the stratum corneum into "
         "the aqueous dermis.")],
        [("Molecular size : ", True), ("flux falls sharply above ~500 Da.")],
        [("Solubility & melting point : ", True), ("low melting point correlates with higher "
         "solubility and flux.")],
        [("Degree of ionisation : ", True), ("the unionised form permeates far better; hence pH "
         "of the vehicle matters.")],
        [("Drug concentration & thermodynamic activity : ", True), ("flux is proportional to the "
         "thermodynamic activity; supersaturated systems enhance delivery.")],
    ])

    n.h2("5.10 Permeation Mathematics (Michaels / steady state)")
    n.para("For a drug permeating a membrane of thickness h under sink conditions, the amount "
           "permeated per unit area (Q) versus time is initially curved and becomes linear at "
           "steady state :")
    n.formula("Q = (D\u00b7Cs / h) \u00d7 [ t \u2013 (h\u00b2 / 6D) ]")
    n.para("The slope of the linear portion gives the steady-state flux Jss = D\u00b7Cs/h and the "
           "intercept on the time-axis gives the lag time t\u2097 = h\u00b2/6D, from which the "
           "diffusion coefficient D can be estimated. The permeability coefficient is P = "
           "Jss / Cv (Cv = donor concentration).")

    n.h2("5.11 Microneedle Technology")
    n.para("Microneedles are arrays of micron-scale projections that pierce only the stratum "
           "corneum, creating micro-conduits for drug (including macromolecules and vaccines) "
           "without reaching the pain nerves or blood vessels of the deeper dermis \u2013 hence "
           "painless. Four types are recognised :")
    n.bullets([
        [("Solid microneedles : ", True), ("'poke-and-patch' \u2013 pierce the skin, then apply "
         "a drug patch/formulation.")],
        [("Coated microneedles : ", True), ("drug coated on the needle dissolves after "
         "insertion.")],
        [("Dissolving microneedles : ", True), ("made of soluble polymer / sugar containing the "
         "drug; dissolve completely, leaving no sharps waste.")],
        [("Hollow microneedles : ", True), ("permit active infusion of liquid formulation.")],
    ])

    n.h2("5.12 Methods of Preparation of Transdermal Patches")
    n.bullets([
        [("Solvent-casting (film-casting) : ", True), ("polymer, drug, plasticiser and enhancer "
         "dissolved in a volatile solvent, cast on a backing and dried \u2013 the commonest "
         "matrix method.")],
        [("Hot-melt extrusion : ", True), ("drug and thermoplastic polymer melted and extruded "
         "into a film (solvent-free).")],
        [("Asymmetric-membrane / phase-inversion methods.", True), ("")],
    ])

    n.h2("5.13 Representative Marketed Transdermal Products")
    n.table(
        ["Drug", "Indication"],
        [
            ["Nitroglycerin", "Angina prophylaxis"],
            ["Nicotine", "Smoking cessation"],
            ["Fentanyl", "Chronic pain"],
            ["Scopolamine (hyoscine)", "Motion sickness"],
            ["Clonidine", "Hypertension"],
            ["Estradiol / testosterone", "Hormone replacement"],
            ["Rivastigmine", "Alzheimer's dementia"],
            ["Rotigotine", "Parkinson's disease"],
        ],
        widths=[2.6, 3.9],
        fontsize=9.3,
    )
    n.box("High-yield \u2013 TDDS", [
        "Stratum corneum = rate-limiting barrier; intercellular lipid route predominates.",
        "Ideal drug : MW < 500, log P 1\u20133, potent (< ~20 mg/day), low melting point, "
        "non-irritant.",
        "Iontophoresis drives charged drugs by current; sonophoresis uses ultrasound "
        "cavitation.",
        "Scopolamine (postauricular) was the first marketed transdermal patch (1979).",
    ], kind="HIGH-YIELD")
    n.page_break()


# =====================================================================
#  UNIT VI  -  DEEP DIVE / EXPANSION
# =====================================================================
def unit6_extra(n):
    n.h2("6.8 The Human Genome, SNPs & the Basis of Variability")
    n.para("The completion of the Human Genome Project (2003) provided the reference against "
           "which individual variation is measured. The most common form of genetic variation is "
           "the single-nucleotide polymorphism (SNP) \u2013 a single base difference occurring in "
           "at least 1 % of the population. SNPs (and copy-number variations) in genes coding for "
           "drug-metabolising enzymes, transporters, receptors and targets account for much of "
           "the inter-individual difference in drug response, and are the molecular foundation of "
           "pharmacogenomics.")

    n.h2("6.9 Biomarkers & Companion Diagnostics")
    n.para("A biomarker is a measurable indicator of a biological state (a gene, protein, "
           "metabolite or imaging feature) used to predict disease, prognosis or drug response. A "
           "companion diagnostic is an in-vitro test that is co-developed with a drug and is "
           "essential for its safe and effective use \u2013 it identifies the patients most "
           "likely to benefit (or to be harmed). Examples : HER2 testing before trastuzumab; EGFR "
           "mutation testing before gefitinib; BRAF V600E testing before vemurafenib; KRAS "
           "testing before cetuximab.")

    n.h2("6.10 Pharmacogenomics in Oncology (Targeted Therapy)")
    n.para("Cancer is the flagship application of personalized medicine because tumours can be "
           "molecularly profiled and matched to targeted drugs. Genotyping the tumour identifies "
           "'driver' mutations that can be blocked selectively, sparing normal cells and reducing "
           "toxicity compared with conventional cytotoxic chemotherapy.")
    n.table(
        ["Tumour marker", "Targeted drug", "Cancer"],
        [
            ["HER2 amplification", "Trastuzumab", "Breast"],
            ["BCR-ABL fusion", "Imatinib", "Chronic myeloid leukaemia"],
            ["EGFR mutation", "Gefitinib / erlotinib", "Non-small-cell lung"],
            ["BRAF V600E", "Vemurafenib", "Melanoma"],
            ["KRAS wild-type", "Cetuximab", "Colorectal"],
            ["PD-L1 expression", "Pembrolizumab", "Various (immunotherapy)"],
        ],
        widths=[1.9, 2.2, 2.4],
        fontsize=9.0,
    )

    n.h2("6.11 Nanotechnology in Personalized Medicine")
    n.para("Nanocarriers (liposomes, polymeric nanoparticles, dendrimers, micelles) can be "
           "engineered with targeting ligands (antibodies, peptides, folate) that recognise "
           "markers over-expressed on a particular patient's diseased cells, giving 'theranostic' "
           "systems that combine therapy and diagnosis. This allows the delivery to be "
           "personalised to the molecular signature of the individual's disease.")

    n.h2("6.12 Advances in Customized Manufacturing")
    n.para("Beyond 3D printing, personalized dosage forms are enabled by : automated compounding, "
           "printed orodispersible films of individualised dose, and digital 'formulation-on-"
           "demand'. 3D printing in particular allows dose flexibility, complex multi-drug "
           "'polyprintlets', tailored release geometry and rapid decentralised production at the "
           "point of care.")
    n.h3("Comparison of 3D-printing techniques")
    n.table(
        ["Technique", "Principle", "Note"],
        [
            ["FDM", "Melt-extrude drug-loaded filament", "Needs thermostable drug"],
            ["Binder-jet", "Liquid binder on powder bed", "Spritam\u00ae (levetiracetam)"],
            ["SLA", "Light-cures liquid resin", "High resolution"],
            ["SSE", "Extrudes paste at room temp", "Good for heat-labile drugs"],
        ],
        widths=[1.3, 2.7, 2.5],
        fontsize=9.2,
    )

    n.h2("6.13 Challenges, Ethics & Future Perspective")
    n.bullets([
        [("Scientific : ", True), ("many diseases are polygenic and multifactorial; a single "
         "marker rarely explains response fully.")],
        [("Economic : ", True), ("cost of genotyping and companion diagnostics; reimbursement "
         "issues.")],
        [("Ethical & legal : ", True), ("genetic privacy, informed consent, risk of "
         "discrimination, data security.")],
        [("Regulatory : ", True), ("approval frameworks for small / individualised batches "
         "(e.g., 3D-printed medicines) and companion diagnostics.")],
        [("Educational : ", True), ("need to train clinicians and pharmacists in genomics.")],
    ])
    n.box("High-yield \u2013 Personalized Medicine", [
        "Right drug \u2013 right dose \u2013 right patient \u2013 right time.",
        "Pharmacogenetics = one gene; pharmacogenomics = whole genome; SNP = commonest "
        "variation.",
        "Companion diagnostics : HER2\u2013trastuzumab, EGFR\u2013gefitinib, HLA-B*57:01"
        "\u2013abacavir, TPMT\u2013azathioprine.",
        "Spritam\u00ae = first FDA-approved 3D-printed tablet (binder-jet).",
        "Electroceuticals = bioelectronic medicine; telepharmacy extends care to remote areas.",
    ], kind="HIGH-YIELD")
    n.page_break()



# =====================================================================
#  UNIT I  -  FURTHER EXPANSION
# =====================================================================
def unit1_more(n):
    n.h2("1.13 Physicochemical Factors \u2013 Detailed Treatment")
    n.h3("Aqueous solubility & dissolution")
    n.para("Because a drug must be in solution to be absorbed, its aqueous solubility sets a "
           "lower limit on the delivery rate. Very poorly soluble drugs (< 0.01 mg/mL) are "
           "intrinsically sustained by their slow dissolution, so building further retardation "
           "into the formulation may make the plasma level sub-therapeutic. Conversely, freely "
           "soluble drugs release too quickly from simple matrices and need a strong "
           "rate-controlling barrier. A solubility in the range 0.1\u201310 mg/mL is generally "
           "considered workable. The pH-dependence of solubility is also important because the "
           "unit travels through regions of very different pH.")
    n.h3("Partition coefficient (log P)")
    n.para("The partition coefficient reflects the drug's lipophilicity and hence its ability to "
           "cross the lipid membranes of the GI epithelium and of polymeric rate-controlling "
           "membranes. Drugs with very low log P are too hydrophilic to permeate; those with very "
           "high log P are so lipophilic that they localise in the membrane and are not released. "
           "An intermediate, balanced log P is optimal, both for absorption and for controlled "
           "release through a polymer.")
    n.h3("Drug pKa & ionisation")
    n.para("Only the unionised species readily crosses lipid membranes (pH-partition hypothesis). "
           "The fraction unionised at a given site is governed by the drug's pKa and the local "
           "pH (Henderson\u2013Hasselbalch). A weak acid is largely unionised (and better "
           "absorbed) in the acidic stomach, whereas a weak base is better absorbed in the more "
           "alkaline intestine. This influences where in the GI tract the drug should be "
           "released.")
    n.h3("Drug stability")
    n.para("A drug that is unstable in gastric acid should be protected (enteric release), while "
           "one unstable in the small intestine may be better released rapidly in the stomach. "
           "For a sustained system that keeps the drug in the GI tract for many hours, chemical "
           "and enzymatic stability throughout the transit is essential.")
    n.h3("Molecular size & diffusivity")
    n.para("The diffusion coefficient of a drug through a polymer decreases as molecular size "
           "increases; molecules above ~500 Da diffuse slowly and above ~1000 Da may not diffuse "
           "usefully through common membranes. This limits the range of drugs deliverable by "
           "diffusion-controlled systems.")
    n.h3("Protein binding")
    n.para("Extensive plasma-protein binding acts as a depot that prolongs the apparent "
           "half-life; such drugs may not require a sustaining formulation. Binding also "
           "influences the free (active) concentration and the volume of distribution used in "
           "dose calculations.")

    n.h2("1.14 Biological Factors \u2013 Detailed Treatment")
    n.h3("Absorption")
    n.para("The rate and site of absorption must be compatible with slow release. If the "
           "absorption rate constant is much smaller than the intended release rate, absorption "
           "(not release) becomes rate-limiting and the design fails. Drugs absorbed by active "
           "transport from a specific 'window' in the upper GI (e.g., riboflavin, some B-"
           "vitamins, L-dopa, iron) are unsuitable unless the system is gastro-retentive.")
    n.h3("Distribution & metabolism")
    n.para("A large or variable volume of distribution and extensive or saturable (non-linear) "
           "metabolism complicate the prediction of plasma levels. High hepatic-extraction drugs "
           "presented slowly to the liver may show greater first-pass loss, lowering "
           "bioavailability.")
    n.h3("Biological half-life \u2013 the central criterion")
    n.para("The half-life summarises elimination and is the single most important selection "
           "criterion. Drugs with t\u00bd < 1 h need very large maintenance doses (impractical); "
           "drugs with t\u00bd > 8\u201312 h are already long-acting. The window t\u00bd = "
           "2\u20138 h is therefore ideal.")
    n.table(
        ["Half-life", "Suitability for SR", "Example"],
        [
            ["< 1 h", "Unsuitable (dose too large)", "Furosemide, levodopa"],
            ["2\u20138 h", "Ideal", "Theophylline, metoprolol, diltiazem"],
            ["> 8 h", "Not needed (already long)", "Digoxin, warfarin, phenytoin"],
        ],
        widths=[1.3, 2.7, 2.5],
        fontsize=9.3,
    )

    n.h2("1.15 Design of Specific Oral CR Dosage Forms")
    n.h3("Coated (film / press) systems")
    n.para("A rate-controlling film of ethylcellulose or a methacrylate copolymer is applied to "
           "drug pellets, granules or tablets. Blending fast- and slow-releasing coated fractions "
           "gives the desired overall profile (as in Spansule capsules).")
    n.h3("Matrix (embedded) tablets")
    n.para("The drug is embedded in a hydrophilic (HPMC), hydrophobic (wax) or plastic "
           "(ethylcellulose) matrix and compressed. Simple, robust and free of dose-dumping "
           "risk; release usually follows Higuchi kinetics.")
    n.h3("Multi-layer & inlay tablets")
    n.para("Two- or three-layer tablets provide an immediate-release layer over a sustaining "
           "layer, combining prompt onset with prolonged action (a designed loading + "
           "maintenance dose).")

    n.h2("1.16 Representative Marketed SR / CR Products")
    n.table(
        ["Technology", "Marketed product / drug"],
        [
            ["Osmotic (push-pull)", "Procardia XL / Adalat GITS (nifedipine)"],
            ["Osmotic (EOP)", "Acutrim, Volmax"],
            ["Coated multiparticulate", "Spansule capsules; Theo-Dur"],
            ["Hydrophilic matrix", "Metformin XR, diltiazem SR"],
            ["Ion-exchange resin", "Codeine / dextromethorphan Pennkinetic suspensions"],
            ["Gastro-retentive", "Ciprofloxacin floating tablet (Cifran OD)"],
        ],
        widths=[2.3, 4.2],
        fontsize=9.3,
    )
    n.page_break()


# =====================================================================
#  UNIT II  -  FURTHER EXPANSION
# =====================================================================
def unit2_more(n):
    n.h2("2.14 Diffusion Mathematics \u2013 Reservoir Geometries")
    n.para("The steady-state release rate from a reservoir device depends on its geometry. For "
           "the three common shapes, with a saturated core (constant activity), the rate is :")
    n.h3("Slab (planar film)")
    n.formula("dM/dt = A\u00b7D\u00b7K\u00b7\u0394C / L   (constant \u2013 zero order)")
    n.h3("Cylinder")
    n.formula("dM/dt = 2\u03c0\u00b7D\u00b7K\u00b7\u0394C\u00b7L / ln(r\u2092/r\u1d62)")
    n.h3("Sphere")
    n.formula("dM/dt = 4\u03c0\u00b7D\u00b7K\u00b7\u0394C\u00b7r\u2092\u00b7r\u1d62 / (r\u2092 \u2013 r\u1d62)")
    n.para("In every case, as long as the core remains saturated the concentration gradient is "
           "constant and release is zero-order; once the core is depleted below saturation, the "
           "gradient (and rate) falls.")

    n.h2("2.15 Advantages & Limitations of each Mechanism")
    n.h3("Diffusion systems")
    n.para("Advantages : reservoir types give zero-order release; well understood and "
           "predictable. Limitations : risk of dose dumping on membrane failure; potential for "
           "residual drug; reproducible membrane thickness required.")
    n.h3("Dissolution systems")
    n.para("Advantages : simple and inexpensive; no membrane to rupture. Limitations : first-"
           "order (declining) release; sensitive to GI pH and to the dissolution environment.")
    n.h3("Osmotic systems")
    n.para("Advantages : zero-order release independent of pH, food and motility; excellent "
           "IVIVC. Limitations : costly and technically demanding; require a laser-drilled "
           "orifice; the membrane and osmogen must be carefully engineered.")
    n.h3("Ion-exchange systems")
    n.para("Advantages : useful for liquid SR suspensions and taste masking; protect the drug. "
           "Limitations : release depends on the variable ionic content of the diet; only "
           "ionisable drugs; loading limited by resin capacity.")

    n.h2("2.16 Selection of System according to Drug Properties")
    n.table(
        ["Drug property", "Preferred SR mechanism"],
        [
            ["Water-soluble, ionisable", "Ion-exchange / osmotic"],
            ["Poorly soluble", "Push-pull osmotic / matrix"],
            ["Narrow absorption window", "Gastro-retentive / mucoadhesive"],
            ["Needs constant level (zero order)", "Osmotic / reservoir membrane"],
            ["Low cost required", "Hydrophilic matrix"],
            ["Local colonic action", "Colon-targeted (pH / microflora)"],
        ],
        widths=[2.7, 3.8],
        fontsize=9.3,
    )
    n.page_break()


# =====================================================================
#  UNIT III  -  FURTHER EXPANSION
# =====================================================================
def unit3_more(n):
    n.h2("3.13 Interfacial & In-situ Polymerisation")
    n.para("In interfacial polymerisation, two reactive monomers (one water-soluble, one oil-"
           "soluble) react at the interface of an emulsion droplet to form a polymeric membrane "
           "around the core (e.g., polyamide / nylon shells by the reaction of a diamine with a "
           "diacid chloride). In in-situ polymerisation the monomer is supplied from one phase "
           "only and polymerises on the core surface. Both give thin, uniform walls but may leave "
           "traces of reactive monomer, which must be controlled.")

    n.h2("3.14 Solvent Evaporation & Ionotropic Gelation \u2013 Detail")
    n.para("In the solvent-evaporation (emulsion) method, the polymer (e.g., PLGA, "
           "ethylcellulose) and drug are dissolved in a volatile, water-immiscible solvent "
           "(dichloromethane); this organic phase is emulsified into an aqueous phase containing "
           "a stabiliser (PVA). Continuous stirring and gentle heat evaporate the solvent, "
           "hardening the droplets into microspheres, which are washed and dried. It is the "
           "standard route to biodegradable PLGA microspheres.")
    n.para("In ionotropic gelation, a solution of a polyelectrolyte (sodium alginate or chitosan) "
           "containing the drug is dropped into a solution of a counter-ion (calcium chloride or "
           "tripolyphosphate); instantaneous cross-linking forms gelled beads. It is mild, "
           "aqueous and free of organic solvents \u2013 ideal for proteins and cells.")

    n.h2("3.15 Multiorifice-Centrifugal & Fluidised-Bed Methods")
    n.para("In the multiorifice-centrifugal process (developed by the Southwest Research "
           "Institute), core and coating are passed through a rotating cylinder with orifices; "
           "centrifugal force ejects coated droplets that solidify in flight. Fluidised-bed / "
           "Wurster coating suspends the cores in an air stream and sprays the coating "
           "repeatedly, giving very uniform films, and is widely used industrially for "
           "controlled-release pellets.")

    n.h2("3.16 Nanoparticles & Nanocapsules (brief)")
    n.para("When the particle size is reduced below 1 \u00b5m, the product is a nanoparticle "
           "(matrix) or nanocapsule (reservoir). The very large surface area, the ability to "
           "cross biological barriers and the possibility of surface functionalisation make "
           "nanoparticles important for targeted and intracellular delivery, although the general "
           "principles of wall material and release kinetics remain those of "
           "microencapsulation.")
    n.page_break()



# =====================================================================
#  UNIT IV  -  FURTHER EXPANSION
# =====================================================================
def unit4_more(n):
    n.h2("4.15 Ocular Anatomy & Barriers to Ocular Delivery")
    n.para("The design of ocular inserts is dictated by the anatomy and protective mechanisms of "
           "the eye, which make conventional topical delivery very inefficient.")
    n.h3("Pre-corneal factors limiting bioavailability")
    n.bullets([
        [("Rapid solution drainage : ", True), ("the eye holds only ~7\u201310 \u00b5L; an "
         "instilled drop (~50 \u00b5L) is largely lost by drainage within minutes.")],
        [("Tear turnover & dilution : ", True), ("tears are replaced at ~16 % per minute, "
         "diluting and washing away the drug.")],
        [("Naso-lacrimal drainage : ", True), ("drug drains into the nasolacrimal duct and can be "
         "absorbed systemically, causing side effects.")],
        [("Non-productive absorption : ", True), ("loss to the conjunctiva and sclera.")],
        [("Corneal barrier : ", True), ("the cornea (lipophilic epithelium \u2013 hydrophilic "
         "stroma \u2013 lipophilic endothelium) requires the drug to be both lipophilic and "
         "hydrophilic (amphiphilic) to penetrate.")],
    ])
    n.para("Consequently, ocular bioavailability from drops is typically < 5 %. Ocular inserts "
           "overcome this by providing prolonged, controlled contact, thereby increasing "
           "bioavailability, reducing dosing frequency and lowering systemic side effects.")
    n.h3("The Ocusert system in detail")
    n.para("The Ocusert\u00ae Pilo-20 / Pilo-40 is a flat, flexible, elliptical reservoir insert. "
           "A core of pilocarpine gelled with alginic acid is sandwiched between two "
           "rate-controlling ethylene-vinyl acetate (EVA) membranes and bordered by a "
           "titanium-dioxide-filled white retaining ring for visibility. It is placed in the "
           "conjunctival cul-de-sac and delivers pilocarpine at a constant rate (20 or "
           "40 \u00b5g/h) for 7 days for the control of glaucoma, replacing four-times-daily "
           "drops.")

    n.h2("4.16 Vaginal Route \u2013 Anatomy & Advantages")
    n.para("The vaginal epithelium is a stratified squamous mucosa richly supplied with blood; "
           "drug absorbed here enters the systemic circulation directly, avoiding hepatic first-"
           "pass metabolism. Permeability varies with the menstrual cycle (thickness and "
           "hydration change with oestrogen). The route is used both for local action "
           "(antifungals, spermicides) and for systemic hormone delivery. Advantages : self-"
           "insertion and removal, avoidance of first-pass, prolonged controlled release from "
           "rings, and reversibility. Limitations : cultural acceptability, local irritation, "
           "influence of cycle and discharge, and gender specificity.")

    n.h2("4.17 Intra-uterine Route \u2013 Mechanism & History")
    n.para("Intra-uterine devices exploit the uterus as a site for very long-term local delivery. "
           "The earliest inert IUDs (Lippes loop) acted purely mechanically. Medicated systems "
           "greatly improved efficacy and reduced side effects :")
    n.bullets([
        [("Copper IUDs (CuT-380A) : ", True), ("release cupric ions that are toxic to sperm and "
         "impair implantation; effective for up to 10 years.")],
        [("Progesterone IUS (Progestasert\u00ae) : ", True), ("a T-shaped device releasing "
         "65 \u00b5g/day progesterone from an ethylene-vinyl acetate reservoir for ~1 year; "
         "thickens cervical mucus and thins the endometrium.")],
        [("Levonorgestrel IUS (Mirena\u00ae) : ", True), ("releases ~20 \u00b5g/day levonorgestrel "
         "for up to 5 years; also used to treat menorrhagia.")],
    ])
    n.para("Advantages : extremely long action, high compliance, reversible, high local with low "
           "systemic exposure. Disadvantages : professional insertion, risk of expulsion, "
           "perforation, cramping, irregular bleeding and pelvic infection.")

    n.h2("4.18 Subcutaneous vs Intramuscular \u2013 Comparison")
    n.table(
        ["Feature", "Subcutaneous", "Intramuscular"],
        [
            ["Vascularity", "Lower (slower absorption)", "Higher (faster absorption)"],
            ["Preferred form", "Solid rods / implants", "Depot injections / microspheres"],
            ["Removal", "Possible (non-degradable)", "Not practical"],
            ["Volume tolerated", "Small", "Larger"],
            ["Example", "Norplant, Implanon", "Depo-Provera, Lupron Depot"],
        ],
        widths=[1.5, 2.5, 2.5],
        fontsize=9.2,
    )

    n.h2("4.19 Ideal Requirements of Implants & Inserts")
    n.bullets([
        "Deliver the drug at the required (often zero-order) rate for the intended duration.",
        "Be biocompatible and cause minimal tissue reaction.",
        "Be sterile, pyrogen-free and of reproducible quality.",
        "Be small and comfortable enough for the site; easy to insert (and remove if "
        "non-degradable).",
        "For biodegradable types, degrade completely into safe, eliminable products.",
        "Be physically and chemically stable during manufacture, sterilisation and storage.",
    ])
    n.page_break()


# =====================================================================
#  UNIT V  -  FURTHER EXPANSION
# =====================================================================
def unit5_more(n):
    n.h2("5.14 Vesicular Carriers for Skin Delivery (latest developments)")
    n.para("Vesicular systems are among the most important recent developments in skin delivery. "
           "They can entrap both hydrophilic and lipophilic drugs, act as a local depot in the "
           "skin, and (for the deformable types) enhance penetration through the stratum "
           "corneum.")
    n.bullets([
        [("Liposomes : ", True), ("concentric phospholipid bilayer vesicles; localise drug in "
         "the upper skin layers and reduce systemic side effects, but classical liposomes "
         "penetrate the stratum corneum poorly.")],
        [("Transfersomes : ", True), ("ultra-deformable ('elastic') liposomes containing an edge "
         "activator (surfactant) that lets them squeeze through the intercellular lipid channels "
         "along the trans-epidermal hydration gradient \u2013 capable of delivering even "
         "macromolecules.")],
        [("Ethosomes : ", True), ("vesicles with a high ethanol content; the ethanol fluidises "
         "both the vesicle and the stratum-corneum lipids, giving deep penetration.")],
        [("Niosomes : ", True), ("non-ionic surfactant vesicles \u2013 cheaper and more stable "
         "than liposomes.")],
        [("Pharmacosomes / aquasomes : ", True), ("other colloidal carriers explored for skin "
         "delivery.")],
    ])

    n.h2("5.15 Mechanisms of Chemical Penetration Enhancement")
    n.para("Chemical enhancers act by one or more of the following mechanisms (the 'lipid-"
           "protein-partitioning' or LPP theory) :")
    n.bullets([
        [("Disruption / fluidisation of the intercellular lipid : ", True), ("e.g., oleic acid, "
         "terpenes, Azone insert into and disorder the lipid bilayers.")],
        [("Interaction with keratin (protein) : ", True), ("e.g., DMSO, surfactants alter the "
         "keratin conformation, opening the corneocytes.")],
        [("Increasing drug partitioning / solubility : ", True), ("co-solvents such as propylene "
         "glycol and ethanol increase the drug's partitioning into the stratum corneum.")],
        [("Increasing hydration : ", True), ("water and occlusion swell the tissue and open the "
         "structure.")],
    ])

    n.h2("5.16 Iontophoresis \u2013 Mechanisms & Factors")
    n.para("Iontophoresis moves drug by two mechanisms : electro-repulsion (like charges repel, "
           "so a cationic drug is driven from the anode and an anionic drug from the cathode) and "
           "electro-osmosis (bulk solvent flow from anode to cathode carries neutral and large "
           "molecules). Delivery is governed by the current density, duration, drug charge and "
           "concentration, pH and the electrode system. Because it can be switched on and off and "
           "the rate set by the current, iontophoresis allows programmable, feedback-controlled "
           "delivery (e.g., the GlucoWatch\u00ae reverse-iontophoresis glucose monitor, and "
           "fentanyl iontophoretic patches).")

    n.h2("5.17 Sonophoresis & Other Physical Methods")
    n.para("Sonophoresis uses ultrasound (low frequency 20\u2013100 kHz is most effective) to "
           "enhance permeation, chiefly through cavitation \u2013 the formation and violent "
           "collapse of gas bubbles that transiently disorganise the stratum-corneum lipids. It "
           "can deliver macromolecules such as insulin and heparin. Related physical methods "
           "include electroporation (high-voltage pulses forming transient pores), thermal "
           "ablation, laser microporation and needle-free jet injection.")

    n.h2("5.18 Ideal Properties & Components \u2013 Consolidated")
    n.table(
        ["Component", "Function", "Example"],
        [
            ["Backing membrane", "Occlusive protective outer layer", "Polyester, aluminised film"],
            ["Drug reservoir / matrix", "Holds the drug", "Silicone, acrylate, HPMC"],
            ["Rate-controlling membrane", "Controls release (reservoir type)", "EVA"],
            ["Pressure-sensitive adhesive", "Attaches patch to skin", "Polyacrylate, silicone"],
            ["Release liner", "Protects adhesive; removed before use", "Siliconised polyester"],
        ],
        widths=[1.9, 2.6, 2.0],
        fontsize=9.0,
    )
    n.page_break()


# =====================================================================
#  UNIT VI  -  FURTHER EXPANSION
# =====================================================================
def unit6_more(n):
    n.h2("6.14 Evolution & Levels of Personalized Medicine")
    n.para("The idea that treatment should suit the individual is ancient, but modern "
           "personalized medicine became feasible only with the molecular-biology revolution and "
           "the sequencing of the human genome. It can be applied at several levels : selecting "
           "the drug (responder identification), individualising the dose (to metabolic "
           "capacity), timing the therapy (chronotherapy), and tailoring the delivery system "
           "(customised dosage form). The greater the genetic and physiological contribution to "
           "variability, the greater the benefit of a personalized approach.")

    n.h2("6.15 Pharmacokinetic vs Pharmacodynamic Pharmacogenetics")
    n.para("Genetic variation influences drug response through two routes :")
    n.bullets([
        [("Pharmacokinetic (PK) polymorphisms : ", True), ("affect drug-metabolising enzymes "
         "(CYP2D6, CYP2C9, CYP2C19, TPMT, UGT1A1, NAT2) and transporters (P-glycoprotein), "
         "changing the drug's concentration.")],
        [("Pharmacodynamic (PD) polymorphisms : ", True), ("affect the drug target or pathway "
         "(receptors, VKORC1 for warfarin, \u03b2-adrenoceptors, ion channels), changing the "
         "response at a given concentration.")],
    ])

    n.h2("6.16 Applications across Specialties")
    n.table(
        ["Specialty", "Personalized example"],
        [
            ["Cardiology", "Warfarin & clopidogrel (CYP2C19) dosing"],
            ["Oncology", "HER2, EGFR, BRAF-guided targeted therapy"],
            ["Psychiatry", "CYP2D6 / CYP2C19 dosing of antidepressants"],
            ["Infectious disease", "HLA-B*57:01 before abacavir; HCV genotype-guided therapy"],
            ["Transplant / immunology", "TPMT before thiopurines"],
            ["Pain", "CYP2D6 status and codeine efficacy / toxicity"],
        ],
        widths=[2.0, 4.5],
        fontsize=9.2,
    )

    n.h2("6.17 Digital Health, Wearables & Artificial Intelligence")
    n.para("Personalized medicine is increasingly supported by digital tools. Wearable sensors "
           "and 'digital pills' (ingestible sensors) provide continuous, individual physiological "
           "and adherence data. Electronic health records combined with machine-learning / "
           "artificial-intelligence algorithms can integrate genomic, clinical and lifestyle data "
           "to predict the best therapy for a given patient and to support clinical decisions. "
           "These technologies also underpin telepharmacy and remote monitoring.")

    n.h2("6.18 Gene & Cell Therapy \u2013 the Ultimate Personalization")
    n.para("Gene therapy (introducing, correcting or silencing a gene) and cell therapies such as "
           "CAR-T (a patient's own T-cells engineered to attack their cancer) represent the most "
           "individualised treatments of all, being manufactured for a single patient. Although "
           "outside the scope of routine formulation, they illustrate the direction in which "
           "personalized medicine is moving, and depend heavily on advanced, targeted delivery "
           "systems (viral and non-viral vectors, lipid nanoparticles).")

    n.h2("6.19 Bioelectronic Medicine \u2013 Further Detail")
    n.para("Bioelectronic devices work by recording and/or stimulating the electrical activity of "
           "specific neural circuits. By closing the loop \u2013 sensing a physiological signal "
           "and delivering a corrective electrical stimulus \u2013 they can regulate organ "
           "function with a precision and reversibility that chemical drugs cannot match. Current "
           "research targets include the vagus nerve (inflammation, rheumatoid arthritis, "
           "diabetes) and peripheral nerves controlling metabolism and immunity. Advantages are "
           "high specificity and freedom from systemic drug side effects; challenges are the "
           "invasiveness of implantation, power supply, biocompatibility of electrodes and long-"
           "term stability.")

    n.h2("6.20 Telepharmacy \u2013 Models & Regulation")
    n.para("Telepharmacy is implemented through several models : remote dispensing sites "
           "supervised by a central pharmacist; tele-consultation and counselling; remote order "
           "verification for hospitals; and automated dispensing units with video oversight. Its "
           "practice requires appropriate licensing, standard operating procedures, secure "
           "data-transfer that protects patient confidentiality, and validated technology. When "
           "well governed, it extends the reach of the pharmacist and improves access to "
           "medicines and pharmaceutical care in remote and under-served communities.")
    n.page_break()



# =====================================================================
#  INTRODUCTION TO NOVEL DRUG DELIVERY SYSTEMS
# =====================================================================
def intro_ndds(n):
    n.unit_title("Introduction to Novel Drug Delivery Systems")

    n.h2("I.1 The Need for Novel Drug Delivery")
    n.para("A drug is of little value unless it is delivered to its site of action at the right "
           "concentration, for the right duration, with minimal exposure of other tissues. "
           "Conventional dosage forms release the whole dose promptly and rely on the body to "
           "distribute and eliminate it; this produces fluctuating plasma levels, frequent "
           "dosing, systemic exposure of non-target tissues and, for many modern drugs (poorly "
           "soluble, unstable or macromolecular), inadequate or unreliable delivery. Novel drug "
           "delivery systems (NDDS) were developed to overcome these limitations by controlling "
           "the rate (temporal control) and/or the place (spatial control) of drug release.")

    n.h2("I.2 Temporal and Spatial Control")
    n.bullets([
        [("Temporal (rate) control : ", True), ("delivering the drug at a defined rate over a "
         "defined time \u2013 sustained, controlled, delayed, pulsatile and chronotherapeutic "
         "systems.")],
        [("Spatial (site) control : ", True), ("delivering the drug to a specific organ, tissue, "
         "cell or receptor \u2013 targeted and site-specific systems.")],
        [("Combined control : ", True), ("the most advanced systems control both rate and place "
         "simultaneously.")],
    ])

    n.h2("I.3 Ideal Characteristics of a Drug Delivery System")
    n.numbered([
        "Deliver the drug at a controlled, predictable and reproducible rate.",
        "Maintain the therapeutic concentration for the desired duration with minimal "
        "fluctuation.",
        "Direct the drug to the target site and spare non-target tissues (where required).",
        "Be safe, biocompatible and free of toxic degradation products.",
        "Protect the drug from premature degradation.",
        "Improve patient compliance and convenience.",
        "Be simple to manufacture, stable on storage and economical.",
    ])

    n.h2("I.4 Evolution / Generations of Drug Delivery")
    n.para("The development of drug delivery is often described in generations :")
    n.bullets([
        [("First generation (1950s\u20131980s) : ", True), ("basic sustained- and controlled-"
         "release oral and transdermal systems; establishing the physicochemical principles of "
         "release.")],
        [("Second generation (1980s\u20132010) : ", True), ("smart / self-regulated systems, "
         "targeting, nanocarriers and delivery of peptides / proteins \u2013 many scientific "
         "successes but fewer clinical products because of biological barriers.")],
        [("Third generation (2010\u2013present) : ", True), ("modulation of the biological "
         "environment, overcoming physiological barriers, personalized and 'smart' responsive "
         "delivery, and manufacturing advances such as 3D printing.")],
    ])

    n.h2("I.5 Classification of Novel Delivery Systems")
    n.table(
        ["Basis", "Types"],
        [
            ["Rate of release", "Immediate, sustained, controlled, delayed, pulsatile"],
            ["Route / site", "Oral, transdermal, ocular, nasal, pulmonary, implantable, vaginal, "
             "uterine"],
            ["Mechanism", "Diffusion, dissolution, osmotic, ion-exchange, erosion, swelling"],
            ["Carrier", "Matrix / reservoir devices, microspheres, implants, patches, vesicles"],
        ],
        widths=[1.6, 4.9],
        fontsize=9.3,
    )

    n.h2("I.6 Scope of this Course")
    n.para("This course focuses on the systems specified in the syllabus : sustained and "
           "controlled release formulations and their oral mechanisms; microencapsulation; "
           "implants and inserts; transdermal systems; and the emerging field of personalized "
           "medicine. Throughout, emphasis is placed on the criteria for selecting suitable drugs "
           "and polymers, the mechanism of release, and the preparation, evaluation and "
           "application of each system.")
    n.page_break()


# =====================================================================
#  NUMERICALS WORKBOOK
# =====================================================================
def numericals(n):
    n.unit_title("Numericals & Worked Examples")

    n.h2("N.1 Elimination Rate Constant & Half-life")
    n.box("Example 1", [
        "A drug has a half-life of 3 h. Calculate its elimination rate constant.",
        [("Solution : ", True), ("k\u2091 = 0.693 / t\u00bd = 0.693 / 3 = 0.231 h\u207b\u00b9.")],
    ], kind="EXAMPLE")

    n.h2("N.2 Zero-order Release / Maintenance Dose")
    n.box("Example 2", [
        "Desired steady-state plasma level Cp = 8 mg/L; Vd = 25 L; t\u00bd = 5 h. Find the "
        "zero-order release rate and the maintenance dose for 8 h.",
        [("k\u2091 : ", True), ("0.693/5 = 0.1386 h\u207b\u00b9.")],
        [("Release rate K\u1d63\u2080 : ", True), ("Cp \u00d7 k\u2091 \u00d7 Vd = 8 \u00d7 0.1386 "
         "\u00d7 25 = 27.7 mg/h.")],
        [("Maintenance dose (8 h) : ", True), ("27.7 \u00d7 8 = 221.7 mg.")],
    ], kind="EXAMPLE")

    n.h2("N.3 Loading Dose & Total Dose")
    n.box("Example 3", [
        "For the drug in Example 2 (F = 1), find the loading dose and total dose.",
        [("Loading dose D\u2080 : ", True), ("Cp \u00d7 Vd = 8 \u00d7 25 = 200 mg.")],
        [("Total dose W : ", True), ("D\u2080 + D\u2098 = 200 + 221.7 = 421.7 mg.")],
    ], kind="EXAMPLE")

    n.h2("N.4 Corrected Loading Dose")
    n.box("Example 4", [
        "If the immediate-release portion peaks at T\u209a = 1.5 h and K\u1d63\u2080 = 27.7 mg/h, "
        "find the corrected loading dose.",
        [("D\u2080(corrected) : ", True), ("D\u2080 \u2013 (K\u1d63\u2080 \u00d7 T\u209a) = 200 "
         "\u2013 (27.7 \u00d7 1.5) = 200 \u2013 41.6 = 158.4 mg.")],
    ], kind="EXAMPLE")

    n.h2("N.5 Bioavailability Correction (oral)")
    n.box("Example 5", [
        "A drug with F = 0.8 requires Cp = 10 mg/L and Vd = 20 L. Find the oral loading dose.",
        [("D\u2080 : ", True), ("(Cp \u00d7 Vd)/F = (10 \u00d7 20)/0.8 = 250 mg.")],
    ], kind="EXAMPLE")

    n.h2("N.6 Higuchi Release")
    n.box("Example 6", [
        "A matrix releases 20 % of its drug in 1 h and follows Higuchi kinetics (Q = k\u2095"
        "\u221at). How much is released in 4 h?",
        [("k\u2095 : ", True), ("Q/\u221at = 20/\u221a1 = 20 %\u00b7h\u207b\u2070\u00b7\u2075.")],
        [("At 4 h : ", True), ("Q = 20 \u00d7 \u221a4 = 20 \u00d7 2 = 40 %.")],
        [("Note : ", True), ("release doubles when time quadruples \u2013 characteristic of "
         "\u221at kinetics.")],
    ], kind="EXAMPLE")

    n.h2("N.7 Permeation \u2013 Flux & Lag Time")
    n.box("Example 7", [
        "A transdermal patch shows a steady-state flux of 25 \u00b5g/cm\u00b2/h and a lag time of "
        "2 h across skin 40 \u00b5m thick. Estimate the diffusion coefficient.",
        [("From t\u2097 = h\u00b2/6D : ", True), ("D = h\u00b2/(6\u00b7t\u2097).")],
        [("Convert h : ", True), ("40 \u00b5m = 40 \u00d7 10\u207b\u2074 cm = 4 \u00d7 10\u207b"
         "\u00b3 cm.")],
        [("D : ", True), ("(4\u00d710\u207b\u00b3)\u00b2 / (6\u00d72) = 1.6\u00d710\u207b\u2075 / "
         "12 = 1.33 \u00d7 10\u207b\u2076 cm\u00b2/h.")],
    ], kind="EXAMPLE")

    n.h2("N.8 Osmotic Delivery Rate (concept)")
    n.box("Example 8", [
        "State how the delivery rate of an elementary osmotic pump changes if the membrane area "
        "is doubled (other factors constant).",
        [("Answer : ", True), ("since dM/dt \u221d A, doubling the membrane area doubles the "
         "delivery rate.")],
    ], kind="EXAMPLE")
    n.page_break()



# =====================================================================
#  APPLICATIONS OF NDDS
# =====================================================================
def applications_ndds(n):
    n.unit_title("Therapeutic Applications of Advanced DDS")

    n.h2("T.1 Cardiovascular System")
    n.para("Once-daily controlled-release nifedipine (GITS/osmotic), diltiazem and verapamil "
           "provide smooth 24-h blood-pressure control and avoid the reflex tachycardia caused "
           "by peaks. Transdermal nitroglycerin gives sustained anti-anginal prophylaxis and "
           "transdermal clonidine controls hypertension while avoiding first-pass metabolism. "
           "Chronotherapeutic (pulsatile) systems time the release of antihypertensives and "
           "anti-anginals to the early-morning surge in cardiovascular events.")

    n.h2("T.2 Central Nervous System")
    n.para("Extended-release formulations of anti-epileptics and antidepressants reduce dosing "
           "frequency and smooth plasma levels. Transdermal rivastigmine improves tolerability in "
           "Alzheimer's disease, transdermal rotigotine gives continuous dopaminergic "
           "stimulation in Parkinson's disease, and deep-brain stimulation (bioelectronic) treats "
           "movement disorders. Personalized dosing guided by CYP2D6 / CYP2C19 genotype improves "
           "antidepressant therapy.")

    n.h2("T.3 Endocrine & Reproductive System")
    n.para("Long-acting contraceptive implants (Norplant, Implanon), depot injections "
           "(Depo-Provera), vaginal rings (NuvaRing) and intra-uterine systems (Mirena) provide "
           "months-to-years of reliable, reversible contraception. Insulin delivery is being "
           "advanced by pumps, closed-loop 'artificial pancreas' systems and needle-free / "
           "sonophoretic approaches.")

    n.h2("T.4 Oncology")
    n.para("Biodegradable implants (Gliadel wafer, Zoladex), depot microspheres (Lupron Depot) "
           "and targeted nanocarriers deliver chemotherapy with improved local concentration and "
           "reduced systemic toxicity. Personalized, biomarker-guided targeted therapy "
           "(trastuzumab, imatinib, gefitinib) exemplifies precision oncology.")

    n.h2("T.5 Ophthalmology")
    n.para("Ocular inserts (Ocusert), intra-ocular implants (Vitrasert, Retisert) and "
           "punctal/mucoadhesive systems overcome the very poor bioavailability of eye drops and "
           "provide prolonged, controlled delivery for glaucoma and posterior-segment "
           "diseases.")

    n.h2("T.6 Infectious & Local Diseases")
    n.para("Colon-targeted systems deliver aminosalicylates and steroids for inflammatory bowel "
           "disease; long-acting injectable antipsychotics and antiretrovirals improve adherence; "
           "vaginal and buccal mucoadhesive systems treat local infections. Pharmacogenomic "
           "testing (HLA-B*57:01) prevents abacavir hypersensitivity.")
    n.page_break()


# =====================================================================
#  CONSOLIDATED COMPARISON TABLES
# =====================================================================
def comparison_tables(n):
    n.unit_title("Consolidated Comparison Tables")

    n.h2("C.1 Sustained vs Controlled Release")
    n.table(
        ["Point", "Sustained release", "Controlled release"],
        [
            ["Rate", "Declines with time", "Constant (zero-order)"],
            ["Plasma level", "Some fluctuation", "Nearly constant"],
            ["Kinetics", "First-order / Higuchi", "Zero-order"],
            ["Predictability", "Moderate", "High"],
            ["Example", "Retard matrix tablet", "Osmotic pump (OROS)"],
        ],
        widths=[1.5, 2.5, 2.5],
        fontsize=9.3,
    )

    n.h2("C.2 Reservoir vs Matrix Devices")
    n.table(
        ["Point", "Reservoir", "Matrix"],
        [
            ["Structure", "Core + membrane", "Drug dispersed in polymer"],
            ["Release order", "Zero-order", "\u221at (Higuchi)"],
            ["Dose dumping", "Possible", "Unlikely"],
            ["Cost / complexity", "Higher", "Lower"],
        ],
        widths=[1.6, 2.4, 2.5],
        fontsize=9.3,
    )

    n.h2("C.3 Simple vs Complex Coacervation")
    n.table(
        ["Point", "Simple", "Complex"],
        [
            ["Polymers", "One", "Two, oppositely charged"],
            ["Trigger", "Desolvation", "Electrostatic interaction"],
            ["Classic system", "Gelatin + Na\u2082SO\u2084", "Gelatin + acacia"],
        ],
        widths=[1.6, 2.4, 2.5],
        fontsize=9.3,
    )

    n.h2("C.4 Routes of Skin Permeation")
    n.table(
        ["Route", "Path", "Contribution"],
        [
            ["Transcellular", "Through corneocytes + lipid", "Repeated partitioning"],
            ["Intercellular", "Through lipid between cells", "Major pathway"],
            ["Appendageal", "Follicles / glands", "Minor; early & for ions"],
        ],
        widths=[1.6, 2.9, 2.0],
        fontsize=9.3,
    )

    n.h2("C.5 Pharmacogenetics vs Pharmacogenomics")
    n.table(
        ["Point", "Pharmacogenetics", "Pharmacogenomics"],
        [
            ["Scope", "Single gene", "Whole genome / many genes"],
            ["Focus", "Individual drug response", "Broad drug\u2013genome interactions"],
            ["Example", "CYP2D6 & codeine", "Genome-wide association of response"],
        ],
        widths=[1.4, 2.6, 2.5],
        fontsize=9.3,
    )
    n.page_break()


# =====================================================================
#  ABBREVIATIONS
# =====================================================================
def abbreviations(n):
    n.unit_title("Abbreviations")
    n.h2("Common Abbreviations used in this Subject")
    items = [
        ("SR / CR", "Sustained release / Controlled release"),
        ("NDDS", "Novel drug delivery system"),
        ("CDDS", "Controlled drug delivery system"),
        ("MEC / MTC", "Minimum effective / minimum toxic concentration"),
        ("MSC", "Maximum safe concentration"),
        ("Cp,ss", "Steady-state plasma concentration"),
        ("Vd", "Volume of distribution"),
        ("k\u2091", "Elimination rate constant"),
        ("t\u00bd", "Biological half-life"),
        ("CL", "Total body clearance"),
        ("F", "Bioavailability"),
        ("IVIVC", "In-vitro / in-vivo correlation"),
        ("EOP / OROS", "Elementary osmotic pump / oral osmotic system"),
        ("GRDDS", "Gastro-retentive drug delivery system"),
        ("TDDS", "Transdermal drug delivery system"),
        ("PSA", "Pressure-sensitive adhesive"),
        ("EVA", "Ethylene-vinyl acetate"),
        ("PLA / PGA / PLGA", "Poly(lactic), poly(glycolic), poly(lactic-co-glycolic) acid"),
        ("PDMS", "Polydimethylsiloxane (silicone)"),
        ("CAP / HPMCP", "Cellulose acetate phthalate / HPMC phthalate"),
        ("IUD / IUS", "Intra-uterine device / system"),
        ("Jss", "Steady-state flux"),
        ("SNP", "Single-nucleotide polymorphism"),
        ("PM / IM / EM / UM", "Poor / intermediate / extensive / ultra-rapid metabolizer"),
        ("CYP", "Cytochrome P450"),
        ("TPMT", "Thiopurine methyltransferase"),
        ("FDM / SLA / SSE", "Fused deposition modelling / stereolithography / semi-solid "
         "extrusion"),
        ("ICH", "International Council for Harmonisation"),
        ("SEM", "Scanning electron microscopy"),
    ]
    for ab, full in items:
        n.term(ab + " \u2013", full)
    n.page_break()



# =====================================================================
#  EVALUATION METHODS (CONSOLIDATED)
# =====================================================================
def evaluation_methods(n):
    n.unit_title("Evaluation Methods for Advanced DDS")

    n.h2("E.1 In-Vitro Dissolution / Release Testing")
    n.para("Dissolution testing is the single most important in-vitro tool for characterising "
           "modified-release products and for quality control. It measures the rate and extent of "
           "drug release under standardised conditions and, when correlated with in-vivo data "
           "(IVIVC), can serve as a surrogate for bioequivalence.")
    n.figure("dissolution_apparatus.png", "USP dissolution apparatus I (basket) and II (paddle)",
             width=5.0)
    n.h3("USP dissolution apparatus")
    n.table(
        ["Apparatus", "Type", "Typical use"],
        [
            ["I", "Rotating basket", "Capsules, floating / disintegrating forms"],
            ["II", "Paddle", "Tablets (most common)"],
            ["III", "Reciprocating cylinder", "Modified-release, pH change studies"],
            ["IV", "Flow-through cell", "Poorly soluble drugs, implants, suppositories"],
            ["V", "Paddle over disc", "Transdermal patches"],
            ["VI", "Rotating cylinder", "Transdermal patches"],
            ["VII", "Reciprocating holder", "Small-volume, transdermal, stents"],
        ],
        widths=[1.1, 2.2, 3.2],
        fontsize=9.2,
    )
    n.para("Key variables to be controlled and reported are the medium (volume, pH, "
           "surfactant), temperature (37 \u00b1 0.5 \u00b0C), rotation speed and sampling times. "
           "The medium is chosen to provide sink conditions and to reflect the physiological "
           "environment; a pH change (e.g., 1.2 \u2192 6.8) may be programmed for enteric and "
           "colonic systems.")

    n.h3("Comparison of dissolution profiles")
    n.para("Two release profiles are compared using model-independent factors :")
    n.bullets([
        [("Difference factor f\u2081 : ", True), ("measures the percentage difference between two "
         "curves; f\u2081 should be 0\u201315 for similarity.")],
        [("Similarity factor f\u2082 : ", True), ("a logarithmic transformation of the mean "
         "squared difference; f\u2082 between 50 and 100 indicates similar profiles.")],
    ])
    n.formula("f\u2082 = 50 \u00d7 log { [1 + (1/n)\u03a3(R\u209c \u2013 T\u209c)\u00b2]^(\u20130.5) \u00d7 100 }")

    n.h2("E.2 In-Vitro Permeation Testing (TDDS)")
    n.para("Skin permeation is studied in a Franz diffusion cell : the skin (or a synthetic "
           "membrane) is mounted between a donor compartment (holding the patch / formulation) "
           "and a receptor compartment (holding the receptor medium, stirred and thermostatted "
           "at 32\u201337 \u00b0C). Samples are withdrawn from the receptor at intervals and "
           "assayed; the cumulative amount permeated per unit area is plotted against time to "
           "obtain the steady-state flux (Jss), permeability coefficient and lag time.")
    n.figure("franz_cell.png", "Franz diffusion cell for in-vitro skin permeation studies",
             width=3.6)

    n.h2("E.3 Solid-State & Physical Characterisation")
    n.bullets([
        [("Particle size & morphology : ", True), ("optical / electron microscopy (SEM), laser "
         "diffraction, sieving.")],
        [("Thermal analysis : ", True), ("DSC and TGA detect polymorphism, drug\u2013polymer "
         "interaction and thermal events.")],
        [("X-ray powder diffraction (XRPD) : ", True), ("distinguishes crystalline and amorphous "
         "states.")],
        [("FTIR / spectroscopy : ", True), ("confirms drug\u2013excipient compatibility.")],
        [("Mechanical tests : ", True), ("hardness, friability, tensile strength, folding "
         "endurance (films).")],
    ])

    n.h2("E.4 Biopharmaceutics Classification System (BCS)")
    n.para("The BCS classifies drugs by aqueous solubility and intestinal permeability into four "
           "classes; it guides formulation strategy and underpins the biowaiver of in-vivo "
           "bioequivalence studies for certain immediate-release products.")
    n.figure("bcs.png", "Biopharmaceutics Classification System (BCS)", width=4.4)
    n.bullets([
        [("Class I (high solubility, high permeability) : ", True), ("well absorbed; dissolution "
         "usually not limiting.")],
        [("Class II (low solubility, high permeability) : ", True), ("dissolution-limited; "
         "solubility-enhancement strategies help.")],
        [("Class III (high solubility, low permeability) : ", True), ("permeation-limited; "
         "absorption enhancers / mucoadhesion help.")],
        [("Class IV (low solubility, low permeability) : ", True), ("poorly absorbed; the most "
         "challenging.")],
    ])

    n.h2("E.5 In-Vivo & Bioavailability Studies")
    n.para("Ultimately, the performance of an advanced DDS is confirmed in vivo by measuring the "
           "plasma-concentration\u2013time profile and deriving Cmax, Tmax and AUC, and by "
           "comparing these with a reference to establish relative bioavailability or "
           "bioequivalence. A validated IVIVC then links these to the in-vitro release, allowing "
           "release testing to be used for routine control.")
    n.page_break()


# =====================================================================
#  REGULATORY & STABILITY
# =====================================================================
def regulatory_stability(n):
    n.unit_title("Stability & Regulatory Considerations")

    n.h2("R.1 Importance of Stability in Advanced DDS")
    n.para("Modified-release and novel delivery systems often contain polymers, plasticisers and "
           "functional coats whose properties can change on storage, altering the release profile "
           "(for example, film curing / ageing of a coated pellet can slow release over time). "
           "Stability studies must therefore verify not only the chemical stability of the drug "
           "but also the constancy of the release characteristics throughout the shelf-life.")

    n.h2("R.2 Degradation Kinetics & Shelf-life")
    n.para("The rate of chemical degradation follows an order of reaction (zero, first or "
           "second). For most drugs, degradation is first-order, and the time for 10 % loss "
           "(t\u2089\u2080, the shelf-life or expiry period) is calculated from the rate "
           "constant. Accelerated studies at elevated temperature, analysed by the Arrhenius "
           "equation, allow the room-temperature shelf-life to be predicted.")
    n.formula("log k = log A \u2013 (Ea / 2.303 R) \u00d7 (1/T)   (Arrhenius)")
    n.formula("t\u2089\u2080 = 0.105 / k   (first-order)")

    n.h2("R.3 ICH Stability Testing")
    n.para("The International Council for Harmonisation (ICH) guideline Q1A(R2) prescribes the "
           "conditions for stability testing of new drug substances and products :")
    n.table(
        ["Study", "Condition", "Minimum period"],
        [
            ["Long-term", "25 \u00b0C / 60 % RH", "12 months"],
            ["Intermediate", "30 \u00b0C / 65 % RH", "6 months"],
            ["Accelerated", "40 \u00b0C / 75 % RH", "6 months"],
        ],
        widths=[1.7, 2.5, 2.3],
        fontsize=9.3,
    )
    n.para("Related guidelines : Q1B (photostability), Q1C (new dosage forms), Q1D "
           "(bracketing and matrixing designs), Q1E (evaluation of stability data). Climatic "
           "zones (I\u2013IV) define the storage conditions appropriate to the intended market.")
    n.h3("Bracketing & matrixing")
    n.bullets([
        [("Bracketing : ", True), ("only the extremes of certain design factors (e.g., strength, "
         "container size) are tested, assuming the intermediates are represented by the "
         "extremes.")],
        [("Matrixing : ", True), ("a selected subset of samples is tested at each time point, "
         "reducing the total number of tests.")],
    ])

    n.h2("R.4 Regulatory Aspects of Modified-Release Products")
    n.para("Modified-release products require additional documentation : justification of the "
           "release mechanism, in-vitro release specifications with a validated method, IVIVC "
           "where possible, food-effect studies, dose-dumping (alcohol-interaction) studies, and "
           "demonstration that the release is reproducible across batches. Novel systems such as "
           "3D-printed and individualised medicines pose new regulatory challenges regarding "
           "batch definition, quality control of small quantities and point-of-care manufacture, "
           "which regulators are actively addressing.")
    n.box("High-yield \u2013 Stability & Regulatory", [
        "First-order shelf-life t\u2089\u2080 = 0.105 / k; Arrhenius predicts long-term from "
        "accelerated data.",
        "ICH long-term = 25 \u00b0C/60 % RH; accelerated = 40 \u00b0C/75 % RH for 6 months.",
        "Modified-release products need dose-dumping (alcohol) and food-effect studies.",
    ], kind="HIGH-YIELD")
    n.page_break()



# =====================================================================
#  POLYMER MONOGRAPHS
# =====================================================================
def polymer_monographs(n):
    n.unit_title("Monographs of Important DDS Polymers")
    n.para("A working knowledge of the individual polymers used in advanced delivery is essential "
           "for the rational selection required by this course. The following short monographs "
           "summarise the nature, mechanism and typical use of the most important polymers.")

    n.h2("P.1 Hydroxypropyl Methylcellulose (HPMC / Hypromellose)")
    n.para("A non-ionic, water-soluble cellulose ether available in many viscosity grades. On "
           "hydration it forms a viscous gel layer that controls release, making it the workhorse "
           "of hydrophilic matrix tablets. It is also used as a film-coating agent and binder. "
           "Release rate is tuned by viscosity grade and polymer level. Non-toxic, widely "
           "accepted and inexpensive.")

    n.h2("P.2 Ethylcellulose")
    n.para("A water-insoluble, non-ionic cellulose ether used as a rate-controlling membrane "
           "coat and as an insoluble matrix former for diffusion-controlled release. Combined "
           "with a pore-former (HPMC, PEG) its permeability can be adjusted. Also used for "
           "microencapsulation and taste masking.")

    n.h2("P.3 Methacrylic-acid Copolymers (Eudragit\u00ae)")
    n.para("A family of acrylic / methacrylic copolymers with different functional groups :")
    n.bullets([
        [("Eudragit L / S : ", True), ("anionic, dissolve above pH 6 / 7 \u2013 enteric and "
         "colonic (site-specific) release.")],
        [("Eudragit RL / RS : ", True), ("contain quaternary ammonium groups; insoluble but "
         "permeable \u2013 sustained release (RL more permeable than RS).")],
        [("Eudragit E : ", True), ("cationic, soluble in gastric fluid \u2013 taste masking / "
         "protective coats.")],
    ])

    n.h2("P.4 Poly(lactic-co-glycolic acid) (PLGA)")
    n.para("The most widely used synthetic biodegradable polymer for microspheres, implants and "
           "in-situ depots. It undergoes bulk hydrolysis to lactic and glycolic acids, which are "
           "eliminated through normal metabolism. Degradation time (weeks to months) is tuned by "
           "the lactide : glycolide ratio and molecular weight; a higher glycolide fraction "
           "degrades faster. Requires no removal.")

    n.h2("P.5 Silicone (Polydimethylsiloxane, PDMS)")
    n.para("A biocompatible, non-biodegradable elastomer used as a rate-controlling membrane and "
           "matrix in reservoir implants and inserts (Norplant, vaginal rings, Ocusert). "
           "Lipophilic drugs partition and diffuse through it, giving near zero-order release. "
           "Chemically inert and stable, but must be surgically removed.")

    n.h2("P.6 Ethylene-Vinyl Acetate (EVA)")
    n.para("A flexible, biocompatible, non-degradable copolymer whose permeability increases with "
           "vinyl-acetate content. Used as the rate-controlling membrane of the Ocusert insert, "
           "of implants and of vaginal rings.")

    n.h2("P.7 Chitosan")
    n.para("A natural cationic polysaccharide obtained by deacetylation of chitin. "
           "Biodegradable, biocompatible, mucoadhesive and permeation-enhancing. Used in "
           "mucoadhesive systems, nasal / colon delivery, nanoparticles and ionotropic-gelation "
           "microspheres (cross-linked with tripolyphosphate).")

    n.h2("P.8 Carbopol (Polyacrylic acid)")
    n.para("A high-molecular-weight, cross-linked polyacrylic-acid polymer that swells to a gel "
           "in water. An excellent mucoadhesive and a rate-controlling agent in matrices and "
           "gels; widely used in buccal, ocular and gastro-retentive systems.")

    n.h2("P.9 Sodium Alginate")
    n.para("A natural anionic polysaccharide from seaweed that forms gel beads instantly on "
           "contact with divalent calcium ions (ionotropic gelation) \u2013 a mild, aqueous route "
           "to microspheres suitable for proteins. Also used in raft-forming and mucoadhesive "
           "systems.")

    n.h2("P.10 Cellulose Acetate")
    n.para("A water-insoluble polymer used chiefly as the semipermeable membrane of osmotic "
           "pumps, permitting water influx while remaining impermeable to solutes. Its "
           "permeability is adjusted with plasticisers and pore-formers.")

    n.h3("Summary table")
    n.table(
        ["Polymer", "Nature", "Principal DDS use"],
        [
            ["HPMC", "Soluble, non-ionic", "Hydrophilic matrix / coating"],
            ["Ethylcellulose", "Insoluble, non-ionic", "Membrane / insoluble matrix"],
            ["Eudragit L/S", "Anionic, pH-sensitive", "Enteric / colonic release"],
            ["Eudragit RL/RS", "Insoluble, permeable", "Sustained release"],
            ["PLGA", "Biodegradable polyester", "Microspheres / implants"],
            ["Silicone (PDMS)", "Inert elastomer", "Reservoir implants / rings"],
            ["EVA", "Non-degradable", "Rate-controlling membrane"],
            ["Chitosan", "Cationic natural", "Mucoadhesive / nanoparticles"],
            ["Carbopol", "Cross-linked acrylic", "Mucoadhesion / gel matrix"],
            ["Cellulose acetate", "Semipermeable", "Osmotic-pump membrane"],
        ],
        widths=[1.7, 2.0, 2.8],
        fontsize=9.0,
    )
    n.page_break()


# =====================================================================
#  FORMULATION OPTIMIZATION / DoE
# =====================================================================
def optimization(n):
    n.unit_title("Formulation Design & Optimization")

    n.h2("O.1 The Need for Systematic Optimization")
    n.para("The performance of an advanced delivery system depends on several interacting "
           "formulation and process variables (polymer type and level, plasticiser, enhancer, "
           "coating thickness, process parameters). Changing one factor at a time (OFAT) is slow, "
           "misses interactions and rarely finds the true optimum. A statistical Design of "
           "Experiments (DoE) approach studies all factors simultaneously, reveals interactions "
           "and locates the optimum with the fewest experiments \u2013 the basis of the modern "
           "Quality-by-Design (QbD) philosophy.")

    n.h2("O.2 Terminology")
    n.bullets([
        [("Factor : ", True), ("an independent variable that is changed (e.g., polymer amount).")],
        [("Level : ", True), ("the value assigned to a factor (low / high, coded \u2212 / +).")],
        [("Response : ", True), ("the measured output (e.g., % released at a given time, flux).")],
        [("Interaction : ", True), ("when the effect of one factor depends on the level of "
         "another.")],
        [("Design space : ", True), ("the multidimensional combination of factors shown to "
         "assure quality.")],
    ])

    n.h2("O.3 Factorial Designs")
    n.para("In a full factorial design, every combination of factor levels is studied. A "
           "two-level, three-factor design (2\u00b3) needs 8 experiments and estimates all main "
           "effects and interactions. When the number of factors is large, fractional factorial "
           "and Plackett\u2013Burman designs are used for screening the important factors with "
           "fewer runs.")

    n.h2("O.4 Response-Surface Methodology (RSM)")
    n.para("Once the important factors are identified, RSM designs (central-composite, "
           "Box\u2013Behnken) fit a second-order (quadratic) model that describes curvature and "
           "locates the optimum. The results are visualised as contour and 3-D response-surface "
           "plots, from which the factor settings giving the target release profile are chosen "
           "and validated.")

    n.h2("O.5 Quality by Design (QbD) & Process Analytical Technology")
    n.para("QbD (ICH Q8) builds quality into the product by design rather than testing it in at "
           "the end. It begins with the Quality Target Product Profile (QTPP), identifies the "
           "Critical Quality Attributes (CQAs) such as the release profile, links them to "
           "Critical Material Attributes and Critical Process Parameters through risk assessment "
           "and DoE, and defines a design space and a control strategy. Process Analytical "
           "Technology (PAT) provides real-time monitoring to keep the process within that "
           "space.")
    n.box("High-yield \u2013 Optimization", [
        "OFAT ignores interactions; factorial designs study all factors together.",
        "2\u00b3 full factorial = 8 runs; RSM (CCD / Box\u2013Behnken) locates the optimum.",
        "QbD (ICH Q8) : QTPP \u2192 CQA \u2192 design space \u2192 control strategy.",
    ], kind="HIGH-YIELD")
    n.page_break()



# =====================================================================
#  CASE STUDIES OF LANDMARK PRODUCTS
# =====================================================================
def case_studies(n):
    n.unit_title("Case Studies of Landmark Delivery Systems")
    n.para("The following marketed products illustrate how the principles of this course are "
           "applied in practice; they are frequently cited examples in theory papers.")

    n.h2("CS.1 Procardia XL / Adalat GITS (Nifedipine)")
    n.para("A push-pull osmotic tablet (OROS) delivering the poorly soluble calcium-channel "
           "blocker nifedipine at a constant zero-order rate for 24 h. The bilayer core (a drug "
           "layer and a swelling push layer) is coated with a cellulose-acetate semipermeable "
           "membrane bearing a laser-drilled orifice. Imbibed water swells the push layer, which "
           "expels a fine suspension of nifedipine through the orifice. It demonstrates "
           "pH-independent, food-independent delivery and excellent IVIVC \u2013 the benchmark of "
           "controlled release.")

    n.h2("CS.2 Ocusert\u00ae Pilo (Pilocarpine)")
    n.para("A reservoir ocular insert delivering pilocarpine at a constant rate (20 or "
           "40 \u00b5g/h) for 7 days for glaucoma. The alginate-gelled drug core lies between two "
           "ethylene-vinyl acetate rate-controlling membranes. It replaces four-times-daily drops, "
           "improves compliance, avoids concentration peaks and greatly increases ocular "
           "bioavailability. A classic reservoir zero-order insert.")

    n.h2("CS.3 Norplant\u00ae (Levonorgestrel)")
    n.para("A subcutaneous contraceptive implant of six silicone (PDMS) capsules containing "
           "levonorgestrel, providing up to five years of contraception by slow diffusion through "
           "the silicone membrane. It illustrates a non-biodegradable reservoir implant that must "
           "be surgically removed. Later single-rod EVA systems (Implanon / Nexplanon) simplified "
           "insertion and removal.")

    n.h2("CS.4 Duragesic\u00ae (Fentanyl Transdermal Patch)")
    n.para("A transdermal system delivering the potent opioid fentanyl for 72 h for chronic pain. "
           "Fentanyl's low molecular weight, high potency and suitable lipophilicity make it an "
           "ideal transdermal candidate. Early versions were reservoir patches with a "
           "rate-controlling membrane; later drug-in-adhesive matrices reduced the dose-dumping "
           "risk. It exemplifies drug-selection criteria for TDDS.")

    n.h2("CS.5 Lupron Depot\u00ae (Leuprolide)")
    n.para("Injectable PLGA microspheres delivering the peptide leuprolide (an LHRH analogue) for "
           "1\u20136 months for prostate cancer and endometriosis. It shows how biodegradable "
           "microspheres protect a peptide from degradation and provide long-acting depot "
           "delivery without an implant that must be removed.")

    n.h2("CS.6 Mirena\u00ae (Levonorgestrel IUS)")
    n.para("A T-shaped intra-uterine system releasing ~20 \u00b5g/day levonorgestrel for up to "
           "five years, giving high local endometrial concentration with low systemic exposure. "
           "Used for contraception and for menorrhagia. Illustrates very long-term, site-specific "
           "local delivery.")

    n.h2("CS.7 Spritam\u00ae (Levetiracetam)")
    n.para("The first FDA-approved 3D-printed medicine (2015), made by powder binder-jet "
           "printing. Its highly porous structure disintegrates in the mouth within seconds even "
           "at a high (1000 mg) dose, aiding epileptic patients who have difficulty swallowing. It "
           "demonstrates the potential of additive manufacturing for individualised, "
           "patient-friendly dosage forms.")
    n.page_break()


# =====================================================================
#  FUTURE TRENDS
# =====================================================================
def future_trends(n):
    n.unit_title("Recent Advances & Future Perspectives")

    n.h2("F.1 Stimuli-Responsive ('Smart') Systems")
    n.para("Smart delivery systems release drug in response to a physiological or external "
           "stimulus, so that delivery matches the need in real time. Triggers include pH (tumour "
           "/ endosome / colon), temperature, glucose concentration (self-regulated insulin "
           "systems), enzymes, light, ultrasound and magnetic fields. Closed-loop or "
           "self-regulated systems sense the signal and adjust the release automatically \u2013 "
           "for example, glucose-responsive insulin delivery aiming at an 'artificial "
           "pancreas'.")

    n.h2("F.2 Delivery of Biologics & Nucleic Acids")
    n.para("Peptides, proteins, monoclonal antibodies and nucleic acids (siRNA, mRNA) are "
           "increasingly important therapeutics but are large, fragile and poorly permeable. "
           "Advanced carriers \u2013 PLGA depots, lipid nanoparticles (as used for mRNA "
           "vaccines), long-acting injectables and microneedles \u2013 protect these molecules "
           "and control their delivery, an area of intense current development.")

    n.h2("F.3 Nanomedicine & Targeting")
    n.para("Nanocarriers functionalised with targeting ligands, and 'theranostic' systems that "
           "combine therapy with imaging, aim to concentrate the drug at the diseased site and "
           "spare healthy tissue \u2013 the ideal of spatial control. Passive (EPR effect) and "
           "active (ligand-receptor) targeting are being combined with stimuli-responsive release "
           "for greater selectivity.")

    n.h2("F.4 Digitally Enabled & Personalized Delivery")
    n.para("The convergence of delivery technology with digital health \u2013 ingestible sensors "
           "('digital pills'), wearable delivery devices, closed-loop pumps and 3D printing "
           "guided by a patient's genomic and clinical data \u2013 is moving therapy towards "
           "truly individualised, on-demand medicine. Artificial-intelligence tools support "
           "formulation design, dose individualisation and adherence monitoring.")

    n.h2("F.5 Sustainable & Point-of-Care Manufacturing")
    n.para("Additive manufacturing and continuous processing promise decentralised, on-demand and "
           "more sustainable production of individualised medicines at the hospital or pharmacy, "
           "reducing waste and inventory. Realising this vision depends on advances in "
           "pharmaceutical-grade materials, in-line quality control and appropriate regulatory "
           "frameworks.")
    n.box("Perspective", [
        "The trajectory of drug delivery is from controlling when (temporal) and where (spatial) "
        "toward controlling how much and how often in real time (responsive), individualised to "
        "the patient (personalized).",
    ], kind="NOTE")
    n.page_break()



# =====================================================================
#  MODEL SHORT NOTES
# =====================================================================
def model_notes(n):
    n.unit_title("Model Short Notes")
    n.para("Concise, ready model answers to frequently asked short-note questions, useful for "
           "quick pre-exam revision.")

    n.h2("M.1 Therapeutic Window")
    n.para("The therapeutic window is the range of plasma drug concentration lying between the "
           "minimum effective concentration (MEC) and the maximum safe / toxic concentration "
           "(MSC / MTC). An ideal delivery system maintains the plasma level within this band for "
           "the whole duration of therapy. A narrow window (e.g., digoxin, theophylline) demands "
           "precise rate control and makes dose dumping dangerous.")

    n.h2("M.2 Dose Dumping")
    n.para("Dose dumping is the unintended, rapid release of a large fraction (or all) of the "
           "drug from a modified-release system, producing a sudden high plasma level and "
           "possible toxicity. It may follow membrane rupture (reservoir systems), formulation "
           "failure or co-ingestion of alcohol (which can dissolve certain matrices). Regulatory "
           "guidelines therefore require alcohol-interaction studies for oral modified-release "
           "products.")

    n.h2("M.3 Higuchi Equation")
    n.para("The Higuchi model describes diffusion-controlled release from a matrix : Q = "
           "k\u2095\u221at, i.e., the amount released is proportional to the square-root of time. "
           "It assumes drug content far exceeds solubility, one-dimensional diffusion, constant "
           "diffusivity, sink conditions and a non-dissolving matrix. A plot of Q versus "
           "\u221at is linear for a matrix system.")

    n.h2("M.4 Osmotic Pump")
    n.para("An osmotic pump delivers drug at a constant zero-order rate driven by osmotic "
           "pressure. Water is imbibed across a semipermeable cellulose-acetate membrane into an "
           "osmotic core; the resulting hydrostatic pressure pumps saturated drug solution out "
           "through a laser-drilled orifice. Delivery is independent of GI pH, food and motility. "
           "The elementary osmotic pump suits soluble drugs; the push-pull (bilayer) type suits "
           "poorly soluble drugs.")

    n.h2("M.5 Complex Coacervation")
    n.para("Complex coacervation is a phase-separation method of microencapsulation using two "
           "oppositely charged polymers (classically gelatin and acacia). Below gelatin's "
           "isoelectric point the positively charged gelatin and negatively charged acacia "
           "attract, forming a coacervate that deposits around the core; the wall is then "
           "hardened by cross-linking (glutaraldehyde) and cooling.")

    n.h2("M.6 Foreign-Body Reaction to an Implant")
    n.para("The host response to an implant proceeds through protein adsorption, acute and "
           "chronic inflammation, granulation-tissue formation, foreign-body giant-cell formation "
           "and finally fibrous encapsulation. The fibrous capsule walls off the implant and can "
           "act as an additional diffusion barrier that slows drug release. A biocompatible "
           "material produces only a thin, quiescent capsule.")

    n.h2("M.7 Stratum Corneum & Permeation Routes")
    n.para("The stratum corneum, the outermost dead keratinised layer of the epidermis, is the "
           "principal barrier to transdermal permeation \u2013 a 'brick-and-mortar' of corneocytes "
           "in a lipid matrix. Drugs cross by the transcellular, intercellular (major) or "
           "appendageal (minor) route. Its resistance is the reason only potent, low-molecular-"
           "weight, suitably lipophilic drugs are deliverable transdermally.")

    n.h2("M.8 Iontophoresis vs Sonophoresis")
    n.para("Iontophoresis uses a small electric current to drive charged drug molecules across "
           "the skin by electro-repulsion and electro-osmosis; delivery is proportional to the "
           "current and can be switched on/off. Sonophoresis uses ultrasound, mainly low "
           "frequency, whose cavitation transiently disrupts the stratum-corneum lipids; it can "
           "deliver even macromolecules such as insulin.")

    n.h2("M.9 Pharmacogenetics")
    n.para("Pharmacogenetics is the study of how variation in a single gene affects an "
           "individual's response to a drug. Polymorphisms in metabolising enzymes (e.g., CYP2D6, "
           "TPMT) create poor, intermediate, extensive and ultra-rapid metabolizers, explaining "
           "why standard doses may be toxic in some and ineffective in others. It is the basis of "
           "dose individualisation in personalized medicine.")

    n.h2("M.10 3D Printing of Medicines")
    n.para("3D printing builds a dosage form layer-by-layer from a digital design, allowing "
           "precise, individualised doses, complex geometries, multi-drug 'polyprintlets' and "
           "tailored release. Techniques include FDM, powder binder-jet (used for Spritam\u00ae, "
           "the first approved 3D-printed tablet), stereolithography and semi-solid extrusion. It "
           "is a key enabler of point-of-care personalized medicine.")
    n.page_break()



# =====================================================================
#  MODEL SHORT NOTES - PART 2
# =====================================================================
def model_notes2(n):
    n.h2("M.11 Mucoadhesion")
    n.para("Mucoadhesion is the adhesion of a (usually hydrophilic) polymer to the mucus layer of "
           "a biological surface, prolonging the residence time of the dosage form and "
           "intensifying contact for absorption or local action. It proceeds through wetting / "
           "contact, swelling, interpenetration of polymer and mucin chains and finally "
           "entanglement and secondary bonding. Common mucoadhesives are carbopol, chitosan, "
           "sodium CMC and thiomers; applications include buccal, nasal, ocular, vaginal and "
           "gastro-retentive systems.")

    n.h2("M.12 Ion-Exchange Resin Systems")
    n.para("An ionised drug is bound to an oppositely charged, insoluble cross-linked resin to "
           "form a resinate. In the GI tract the abundant counter-ions (Na\u207a, K\u207a, "
           "H\u207a, Cl\u207b) displace the drug, releasing it slowly at a rate governed by the "
           "ionic environment rather than pH alone. Useful for liquid sustained-release "
           "suspensions and taste masking; limited to ionisable drugs and dependent on diet.")

    n.h2("M.13 Bioerodible Systems")
    n.para("In bioerodible systems the polymer matrix gradually degrades in the body and the drug "
           "is released by combined diffusion and erosion, leaving no residue to be removed. "
           "Bulk erosion (PLGA) degrades throughout the matrix, whereas surface erosion "
           "(polyanhydrides, poly-ortho-esters) proceeds layer-by-layer and gives release nearer "
           "to zero-order.")

    n.h2("M.14 Gastro-retentive Systems")
    n.para("Gastro-retentive systems prolong gastric residence to improve absorption of drugs "
           "with a narrow upper-GI absorption window or for local gastric action. Approaches "
           "include floating (low-density) systems, high-density (sinking) systems, mucoadhesive, "
           "swelling / expanding, raft-forming and magnetic systems. Floating effervescent "
           "systems generate CO\u2082 from bicarbonate to lower the density below that of gastric "
           "fluid.")

    n.h2("M.15 Microspheres vs Microcapsules")
    n.para("A microcapsule is a reservoir (core-shell) structure in which a distinct core is "
           "surrounded by a wall, whereas a microsphere is a matrix particle in which the drug is "
           "dispersed uniformly throughout the polymer. Both lie in the 1\u20131000 \u00b5m range; "
           "below 1 \u00b5m the equivalents are nanocapsules and nanospheres.")

    n.h2("M.16 Companion Diagnostics")
    n.para("A companion diagnostic is an in-vitro test co-developed with a drug and essential to "
           "its safe, effective use, identifying the patients most likely to benefit or to be "
           "harmed. Examples include HER2 testing before trastuzumab, EGFR-mutation testing "
           "before gefitinib and HLA-B*57:01 testing before abacavir. They are central to "
           "biomarker-guided personalized therapy.")

    n.h2("M.17 In-Situ Forming Implants")
    n.para("These are injectable liquids that solidify into a drug depot in the body, avoiding "
           "surgery. Formation is triggered by solvent removal / phase inversion (PLGA in NMP, "
           "as in Atrigel / Eligard), thermal gelation (poloxamers), in-situ cross-linking or "
           "ionic gelation. They combine the convenience of an injection with the prolonged "
           "action of an implant.")
    n.page_break()
