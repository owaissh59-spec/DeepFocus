"""Chapters 10-13 : Medicines, Special Conditions & Treatments, Bandaging,
Further Observations."""


def chapter_10(b):
    b.chapter(10, "Medicines",
              "Routes, dosage forms, the rights of administration, prescription reading, dose calculation, injections and storage")

    b.section_h("10.1", "Basic Terms")
    b.table(
        ["Term", "Meaning"],
        [["__Drug / Medicine__", "Any substance used in the diagnosis, prevention, treatment or cure of disease (a 'medicine' is the drug in its final dosage form)"],
         ["__Pharmacology / Pharmacy__", "Science of drugs and their action on the body / art and science of preparing and dispensing medicines"],
         ["__Pharmacokinetics__", "What the body does to the drug — __Absorption, Distribution, Metabolism, Excretion (ADME)__"],
         ["__Pharmacodynamics__", "What the drug does to the body — mechanism of action, receptors, dose-response"],
         ["__Bioavailability__", "Fraction of an administered dose reaching the systemic circulation unchanged; __100% for the intravenous route__"],
         ["__Generic / Brand (proprietary) name__", "Official non-proprietary name (paracetamol) / manufacturer's trade name (Crocin)"],
         ["__Therapeutic dose / Maximum dose / Minimum dose__", "Usual effective dose / largest safe dose / smallest effective dose"],
         ["__Loading dose / Maintenance dose__", "Large initial dose to reach the effective level quickly / dose to maintain that level"],
         ["__Therapeutic index__", "Ratio of toxic dose to therapeutic dose — a __narrow therapeutic index__ (digoxin, phenytoin, lithium, warfarin, theophylline, aminoglycosides) needs monitoring"],
         ["__Side effect / Adverse drug reaction (ADR) / Toxic effect__", "Unwanted but predictable effect at normal dose / any noxious unintended response / effect of over-dosage"],
         ["__Idiosyncrasy / Allergy / Anaphylaxis__", "Genetically determined abnormal reaction / immune-mediated reaction / severe, life-threatening allergic reaction"],
         ["__Tolerance / Dependence / Addiction / Withdrawal__", "Need for a larger dose for the same effect / physical or psychological need / compulsive drug-seeking / symptoms on stopping"],
         ["__Cumulation__", "Accumulation of the drug when excretion is slower than administration (digoxin, heavy metals)"],
         ["__Synergism / Antagonism / Potentiation__", "Combined effect greater than the sum / one drug opposing another / one drug increasing the effect of another"],
         ["__Contraindication__", "A condition in which the drug must not be given"],
         ["__Placebo__", "An inert substance given as a medicine"],
         ["__Prophylactic / Palliative / Curative drug__", "Prevents disease / relieves symptoms / cures the disease"],
         ["__Antidote__", "A substance that counteracts a poison"],
         ["__First-pass effect__", "Metabolism of an oral drug in the liver/gut wall before it reaches the circulation (avoided by the sublingual, rectal and parenteral routes)"]],
        caption="Table 10.1  Pharmacological terms")

    b.section_h("10.2", "Routes of Administration")
    b.table(
        ["Route", "Examples / method", "Advantages", "Disadvantages"],
        [["__Oral (per os, PO)__", "Tablets, capsules, syrups, suspensions, powders",
          "Safest, cheapest, most convenient, self-administered, no asepsis needed",
          "Slow onset, unsuitable if vomiting/unconscious/NPO, gastric irritation, first-pass metabolism, unpleasant taste, cannot be used in emergency"],
         ["__Sublingual / Buccal__", "Tablet under the tongue or in the cheek — __nitroglycerine__, isosorbide dinitrate, buprenorphine, ondansetron",
          "Very rapid absorption, __avoids first-pass metabolism__, can be spat out", "Only a few drugs, irritation, must not be swallowed or chewed"],
         ["__Rectal__", "Suppositories, enema, ointment — diazepam, paracetamol, bisacodyl, indomethacin",
          "Useful in vomiting, unconscious and uncooperative patients and children; partly avoids first pass",
          "Embarrassing, erratic absorption, local irritation"],
         ["__Intramuscular (IM)__", "Deltoid, vastus lateralis, ventrogluteal, dorsogluteal; 1-5 mL",
          "Rapid absorption, suitable for depot/oily preparations, can give irritant drugs",
          "Painful, risk of nerve/vessel injury, abscess, contraindicated in bleeding disorders and shock"],
         ["__Subcutaneous (SC)__", "Outer upper arm, abdomen, anterior thigh — __insulin, heparin, adrenaline, vaccines__; up to 1-2 mL",
          "Slow, uniform absorption; can be self-administered; depot implants possible",
          "Small volume only, irritant drugs cause necrosis, slower than IM"],
         ["__Intradermal (ID)__", "Inner forearm, deltoid — __Mantoux test, BCG, allergy testing__; 0.1 mL",
          "Very small dose, for diagnostic and immunisation purposes", "Tiny volume, painful, needs skill"],
         ["__Intravenous (IV)__", "Bolus, infusion, via cannula or central line",
          "__Fastest action (bioavailability 100%)__, exact dose, large volumes, drugs for emergency, irritant solutions can be given diluted",
          "Most dangerous — no recall once given; risk of embolism, thrombophlebitis, infiltration, extravasation, infection, anaphylaxis; needs skill and asepsis"],
         ["__Inhalation__", "Metered dose inhaler with spacer, dry powder inhaler, nebuliser, oxygen, anaesthetic gases — salbutamol, budesonide, ipratropium",
          "Direct action on the airway with a small dose and few systemic effects, rapid onset", "Needs correct technique and coordination, local irritation, oral thrush with steroids (rinse the mouth)"],
         ["__Topical / transdermal__", "Ointment, cream, lotion, gel, paste, dusting powder, patch (nitroglycerine, fentanyl, hormones, nicotine)",
          "Local action, steady blood level with patches, avoids first pass", "Slow, may stain, systemic absorption if applied over a large or broken area"],
         ["__Instillation / local__", "Eye, ear and nose drops, ointment, gargle, throat paint, vaginal pessary, urethral, intrathecal, intra-articular, intracardiac, intraosseous",
          "Direct local effect where needed", "Needs asepsis; risk if the wrong strength or wrong site is used"],
         ["__Others__", "Intraperitoneal (dialysis), intrapleural, epidural/spinal, intra-arterial, intra-ocular, implant",
          "Specialised indications", "Performed by the doctor only"]],
        caption="Table 10.2  Routes of drug administration")
    b.box("hy", ["__Order of speed of onset__ (fastest first): __IV → inhalation/intraosseous → IM → SC → sublingual → rectal → oral → topical.__  The __IV route is the fastest and the most dangerous__; the __oral route is the safest__ and the commonest."])

    b.section_h("10.3", "Dosage Forms")
    b.table(
        ["Group", "Dosage forms"],
        [["__Solid oral__", "Tablet (plain, coated, __enteric-coated, sustained/controlled release__, chewable, dispersible, effervescent, sublingual), capsule (hard and soft gelatin, spansule), powder, granules, pill, lozenge/troche, sachet"],
         ["__Liquid oral__", "Syrup, elixir (hydro-alcoholic), linctus (for cough), suspension (__shake well__), emulsion, mixture, drops, tincture, spirit, solution, oral rehydration solution"],
         ["__Parenteral__", "Injection in ampoule, vial, pre-filled syringe, large-volume infusion; lyophilised powder for reconstitution; depot injection"],
         ["__Topical__", "Ointment (oily), cream (water-washable), gel/jelly, paste (thick), lotion, liniment (rubbed in), paint, dusting powder, spray, aerosol, medicated patch, medicated shampoo"],
         ["__Rectal and vaginal__", "Suppository, enema, rectal ointment, pessary, vaginal cream/tablet"],
         ["__Ophthalmic / otic / nasal__", "Eye drops and ointment (__sterile, single patient, discard 4 weeks after opening__), ear drops, nasal drops and spray, inhaler"],
         ["__Inhalational__", "MDI, dry powder inhaler, respirator (nebuliser) solution, oxygen, volatile anaesthetics"]],
        caption="Table 10.3  Dosage forms")
    b.box("caution", [
        "* __Never crush, break or chew an enteric-coated or sustained-release tablet or open a spansule capsule__ (dose dumping / gastric irritation / loss of action).",
        "* __Shake suspensions and emulsions well__ before pouring; do not refrigerate a suspension unless directed.",
        "* Keep a __separate marked measure/spoon__ for external applications, and never store external preparations with oral medicines.",
        "* Reconstituted syrups (many antibiotics) are usually stable only __7-14 days__, often needing refrigeration — write the date of reconstitution on the label.",
    ])

    b.section_h("10.4", "The 'Rights' of Drug Administration")
    b.numbered([
        "__Right patient__ — check the identity by name band, asking the name and date of birth, and the bed number (never by bed number alone).",
        "__Right drug__ — read the label three times (when taking it out, while preparing, and before returning/discarding); check the generic name, not just the appearance.",
        "__Right dose__ — check the strength and calculate carefully; get high-risk calculations double-checked by a second person.",
        "__Right route__ — as written; never change the route on your own.",
        "__Right time__ — as prescribed (within 30 minutes of the scheduled time), noting before/after food.",
        "__Right documentation__ — record __immediately after__ giving (never before); record refusal, omission and the reason.",
        "__Right to refuse__ — the informed patient may refuse; record and report it.",
        "__Right assessment and right evaluation__ — check the pulse before digoxin, BP before an antihypertensive, blood sugar before insulin, respiration before an opioid, and the response afterwards.",
        "__Right education__ — tell the patient what the drug is, why it is given, and what to expect."
    ])
    b.box("clinical", [
        "__General rules while giving medicines:__",
        "* __Never give a drug prepared by someone else__, and never leave a prepared dose unlabelled or unattended.",
        "* __Never give a drug from an unlabelled, illegible or damaged container__ — return it to the pharmacy.",
        "* Check the __expiry date__ and look for discolouration, precipitate, cloudiness, cracks and leakage.",
        "* Check for __allergies__ before every new drug; question any order that appears unusual, illegible or a wrong dose; do not accept a verbal/telephone order except in an emergency, and then write it down and get it signed.",
        "* Stay with the patient until the drug is __actually swallowed__ (especially in psychiatry and tuberculosis DOTS).",
        "* Report and record any __medication error immediately__ — the patient's safety comes before self-protection.",
        "* Remember __LASA (look-alike, sound-alike)__ drugs: ~dopamine/dobutamine, hydralazine/hydroxyzine, chlorpromazine/chlorpropamide, cefotaxime/ceftazidime, metoprolol/misoprostol, insulin types~ — read the full name and store them apart.",
    ])

    b.section_h("10.5", "Reading a Prescription — Abbreviations and Latin Terms")
    b.table(
        ["Abbreviation", "Meaning", "Abbreviation", "Meaning"],
        [["__Rx__", "Recipe — 'take thou'", "__ac / pc__", "Before food / after food"],
         ["__OD / BD (BID) / TDS (TID) / QID__", "Once / twice / three times / four times a day", "__hs / nocte / mane__", "At bedtime / at night / in the morning"],
         ["__q4h, q6h, q8h__", "Every 4, 6 or 8 hours", "__SOS / PRN__", "If necessary / as and when required"],
         ["__STAT__", "Immediately, at once", "__NPO / NBM__", "Nothing by mouth"],
         ["__PO / PR / PV__", "By mouth / per rectum / per vagina", "__SL__", "Sublingual"],
         ["__IM / IV / SC / ID / IVI__", "Intramuscular / intravenous / subcutaneous / intradermal / IV infusion", "__OU / OD (eye) / OS__", "Both eyes / right eye / left eye"],
         ["__gtt / gtts__", "Drop / drops", "__AD / AS / AU__", "Right ear / left ear / both ears"],
         ["__mg / mcg (ug) / g / mL / L__", "Milligram / microgram / gram / millilitre / litre", "__IU / U__", "International unit / unit (~always write 'unit' in full — 'U' is misread as 0~)"],
         ["__tab / cap / syp / inj / oint__", "Tablet / capsule / syrup / injection / ointment", "__q / qs / ad lib__", "Each / a sufficient quantity / as desired"],
         ["__1/2, 1/4 tab, ss__", "Half, quarter tablet, one half", "__c / s (c̄ / s̄)__", "With / without"],
         ["__DNS / NS / RL / D5__", "Dextrose-normal saline / normal saline / Ringer lactate / 5% dextrose", "__O2, NG, RT__", "Oxygen, nasogastric, Ryle's tube"]],
        caption="Table 10.4  Prescription abbreviations")
    b.sub("Parts of a prescription")
    b.bullets([
        "__Date; name, age, sex, weight and address of the patient__; __superscription__ (Rx); __inscription__ (name, strength and quantity of each drug); __subscription__ (directions to the pharmacist); __signatura / transcription (Sig.)__ — directions for the patient; __renewal/refill instructions__; and the __prescriber's signature, registration number and address__.",
        "A prescription for a __Schedule H, H1 or X__ drug must be a written, signed prescription of a registered medical practitioner; __Schedule X__ needs a prescription in duplicate, one copy retained by the pharmacist for __2 years__.",
    ])
    b.box("caution", [
        "__Error-prone abbreviations to be avoided (as per the 'Do Not Use' list):__",
        "* 'U' for unit (misread as 0 or 4) → write __'unit'__; 'IU' → write __'international unit'__.",
        "* __A trailing zero__ (1.0 mg read as 10 mg) — write '1 mg'; always use a __leading zero__ ('0.5 mg', never '.5 mg').",
        "* 'OD' for 'once daily' can be read as 'right eye'; 'µg' can be read as 'mg' → write __'microgram'__.",
        "* 'MS/MSO4/MgSO4' — write __morphine sulphate__ and __magnesium sulphate__ in full.",
    ])

    b.section_h("10.6", "Dose Calculation")
    b.box("num", [
        "__Basic formula:__  Dose to be given = (Dose ordered ÷ Dose on hand) × Quantity on hand (volume or number of tablets).",
        "__Example 1:__ Order 250 mg; stock is a 500 mg tablet → 250/500 = __half a tablet__.",
        "__Example 2:__ Order amikacin 375 mg; stock 500 mg in 2 mL → (375/500) × 2 = __1.5 mL__.",
        "__Example 3 (syrup):__ Order paracetamol 180 mg; syrup is 125 mg in 5 mL → (180/125) × 5 = __7.2 mL__.",
        "__IV drip rate (drops/minute) = (Total volume in mL × drop factor) ÷ (Time in minutes).__  Drop factor: __macro-drip 15 or 20 drops/mL (adult sets), micro-drip/paediatric 60 drops/mL__.",
        "__Example 4:__ 1000 mL over 8 hours with a 20 drops/mL set → (1000 × 20) ÷ (8 × 60) = __41-42 drops/min__.",
        "__Infusion time (hours) = Total volume ÷ mL per hour.__",
        "__Body surface area (BSA, m2) = square root of [height (cm) × weight (kg) ÷ 3600]__ (Mosteller formula).",
    ])
    b.sub("Paediatric dose calculation")
    b.table(
        ["Rule", "Formula"],
        [["__Body weight (the preferred method)__", "Dose = mg/kg × weight in kg (e.g. paracetamol 15 mg/kg/dose)"],
         ["__Body surface area (most accurate, used for cytotoxics)__", "Child dose = (BSA of child in m2 ÷ 1.73) × adult dose"],
         ["__Young's rule (1-12 years)__", "Child dose = adult dose × age in years ÷ (age + 12)"],
         ["__Clark's rule__", "Child dose = adult dose × weight in lb ÷ 150"],
         ["__Fried's rule (infants under 1 year)__", "Dose = adult dose × age in months ÷ 150"],
         ["__Dilling's rule__", "Child dose = adult dose × age in years ÷ 20"]],
        caption="Table 10.5  Paediatric dose rules")
    b.sub("Household and metric measures")
    b.bullets([
        "__1 teaspoon = 5 mL • 1 dessertspoon = 10 mL • 1 tablespoon = 15 mL • 1 cup = 240 mL • 1 glass/tumbler = 200-250 mL • 15-16 drops = 1 mL (standard dropper, 20 drops for water)__.",
        "__1 g = 1000 mg; 1 mg = 1000 micrograms; 1 L = 1000 mL; 1 kg = 2.2 lb; 1 inch = 2.54 cm; 1 grain = 60-65 mg; 1 minim = 0.06 mL; 1 ounce = about 30 mL__.",
        "__1 unit of insulin = 0.01 mL of U-100 insulin__ — always use an __insulin syringe marked in units__, never a tuberculin or ordinary syringe.",
    ])

    b.section_h("10.7", "Administering Oral Medicines")
    b.numbered([
        "Check the order, the patient's name, the drug, dose, route, time and allergies; wash hands.",
        "Pour tablets into the cap/medicine cup __without touching them with the hand__; pour liquids with the __label uppermost__ (so drips do not spoil the label), hold the measure at __eye level on a flat surface and read the lower meniscus__, and wipe the neck of the bottle.",
        "Give with a __full glass of water__ (unless restricted) in the __sitting or Fowler's position__; never give oral medicines to a lying-flat or drowsy patient.",
        "Stay until the medicine is swallowed; check the mouth of a psychiatric or non-compliant patient.",
        "Special points — give irritant drugs (iron, NSAIDs, steroids, metformin) __after food__; give sucralfate, ampicillin, levothyroxine, rifampicin and iron __on an empty stomach__; do not give tetracycline or iron with milk, antacids or calcium; do not crush enteric-coated/SR tablets; dilute and give liquid iron and potassium with a straw; give cough linctus __undiluted and without water afterwards__; sublingual tablets are __not swallowed__.",
        "Record immediately and observe for the effect and for side effects."
    ])

    b.section_h("10.8", "Injections — Sites, Angles and Technique")
    b.table(
        ["Injection", "Site", "Needle & angle", "Volume"],
        [["__Intradermal (ID)__", "Inner (flexor) surface of the forearm, upper chest, scapular area; __BCG: left upper arm over the deltoid insertion__",
          "26-27 G, 10-15 mm, __10-15 degrees__, bevel up — a __bleb/wheal must form__", "0.1 mL (BCG 0.05 mL in newborns, 0.1 mL after 1 month)"],
         ["__Subcutaneous (SC)__", "Outer aspect of the upper arm, anterior thigh, __abdomen (insulin — rotate sites, avoid 5 cm around the umbilicus)__, upper back",
          "25-26 G, __45 degrees (90 degrees with a short insulin needle or if the skin is pinched)__; ~do not massage after heparin or insulin~", "0.5-1 mL (max 2 mL)"],
         ["__Intramuscular (IM)__", "__Deltoid__ (2-3 finger breadths below the acromion — vaccines, max 1-2 mL); __Vastus lateralis__ (middle third of the outer thigh — __the site of choice in infants__); __Ventrogluteal__ (safest in adults — palm on the greater trochanter, index finger on the anterior superior iliac spine, middle finger along the iliac crest, inject in the V); __Dorsogluteal__ (upper outer quadrant of the buttock — risk of __sciatic nerve__ injury, avoid in children under 3 years)",
          "21-23 G, 1-1.5 inch, __90 degrees__; __Z-track technique__ for irritant drugs (iron dextran, hydroxyzine, promethazine)", "Adult 1-3 mL (up to 5 mL in the gluteal); deltoid 1 mL; infant 0.5-1 mL"],
         ["__Intravenous (IV)__", "Dorsum of the hand, forearm (cephalic, basilic), median cubital (for sampling), great saphenous, scalp veins in infants; central: subclavian, internal jugular, femoral",
          "18-24 G cannula; __15-30 degrees__, bevel up, tourniquet 10-15 cm above the site, released before injecting", "Any volume, at the prescribed rate"]],
        caption="Table 10.6  Injection sites and technique")
    b.sub("General rules for injections")
    b.bullets([
        "Strict asepsis: wash hands, clean the top of the vial and the skin with a __spirit/alcohol swab in a circular motion from the centre outwards, and let it dry__; use a new sterile syringe and needle for each injection.",
        "Expel air completely; __aspirate before an IM injection__ to make sure the needle is not in a vessel (~aspiration is no longer recommended for vaccines and for the ventrogluteal site~); if blood appears, withdraw and start again with a fresh syringe.",
        "Inject __slowly__, withdraw quickly, and apply gentle pressure with a dry swab (__do not rub after insulin, heparin or a vaccine__).",
        "Never inject into an inflamed, infected, scarred, oedematous, paralysed or hardened area; __rotate sites__ in patients on repeated injections (insulin, heparin) to prevent lipodystrophy.",
        "Dispose of the needle and syringe __immediately into a puncture-proof container without recapping__.",
        "Keep __adrenaline (1:1000), hydrocortisone, an antihistamine, oxygen and an airway__ ready whenever giving an injection or a vaccine — and observe the patient for __15-30 minutes__ afterwards.",
    ])
    b.sub("Complications of injections")
    b.bullets([
        "__Local__ — pain, bleeding, bruising, abscess, cellulitis, sterile abscess, tissue necrosis, nodule/fibrosis, lipodystrophy, nerve injury (sciatic, radial), accidental intra-arterial injection (severe pain, blanching — an emergency), needle breakage.",
        "__IV therapy__ — __infiltration__ (fluid into the tissue: swelling, coolness, pallor — stop, remove, elevate, warm/cold compress), __extravasation__ (leakage of a vesicant drug — stop at once, aspirate, inform the doctor, consider an antidote), __phlebitis/thrombophlebitis__ (redness, warmth, a palpable cord along the vein — remove the cannula, apply a warm compress), air embolism, catheter embolism, speed shock, circulatory overload (dyspnoea, raised JVP, crepitations — stop or slow the drip, sit the patient up, give oxygen, inform the doctor), sepsis.",
        "__Systemic__ — anaphylaxis, fainting, drug reaction, transmission of hepatitis B/C or HIV through unsafe practice.",
    ])
    b.box("caution", [
        "__Anaphylaxis — recognise and act in seconds:__ itching, urticaria, flushing, swelling of the lips/tongue/throat, hoarseness, stridor, wheeze, severe dyspnoea, abdominal cramps, fall of BP, tachycardia, collapse.",
        "__Treatment:__ stop the drug → call for help → __adrenaline (epinephrine) 1:1000, 0.5 mL (0.5 mg) IM into the mid-outer thigh__ (child 0.01 mg/kg), repeat every 5-15 min if needed → lay the patient flat with the legs raised (sit up if breathless) → high-flow __oxygen__ → secure the airway → __IV fluids__ → antihistamine (chlorpheniramine/pheniramine) and __hydrocortisone 100-200 mg IV__ → nebulised salbutamol for wheeze → observe for __6-24 hours__ (biphasic reaction).",
    ])

    b.section_h("10.9", "Intravenous Infusion — Nursing Points")
    b.bullets([
        "Check the fluid: name, strength, expiry, clarity (no particles, no turbidity), intact seal; label the bottle with the patient's name, the added drug, the date, time and rate, and the nurse's initials.",
        "Prime the set to remove all air; maintain a closed system; change the giving set every __72-96 hours__ (__24 h for blood, lipid and TPN__), and the peripheral cannula as per policy/when indicated.",
        "Keep the site __visible and dressed with a transparent film__; check hourly for pain, swelling, redness, leakage, the backflow of blood and the drip rate.",
        "Never 'catch up' a slow infusion by opening the roller clamp fully (risk of overload, especially in the elderly, infants, cardiac and renal patients); __use an infusion pump for children, potent drugs and precise rates__.",
        "Common IV fluids: __normal saline 0.9% (isotonic, for dehydration, shock, with blood), Ringer lactate (balanced — the fluid of choice in burns and surgical loss), 5% dextrose (free water and calories, ~not for resuscitation~), DNS, isolyte-P/M (paediatric), mannitol (osmotic diuretic), colloids (dextran, gelatin, albumin, hydroxyethyl starch)__.",
        "__Never give a hypotonic or dextrose solution with blood__ — it causes haemolysis; flush the line with normal saline only.",
    ])

    b.section_h("10.10", "Storage, Stock and Disposal of Medicines")
    b.bullets([
        "Store in a __cool, dry, dark place away from direct sunlight__; 'store below 25-30 °C' means room temperature, __'cold chain' 2-8 °C__ (refrigerator, never the freezer for vaccines/insulin, never the refrigerator door), deep freeze for polio vaccine (−20 °C).",
        "__Vaccines and insulin must never be frozen__ (adsorbed vaccines — DPT, TT, hepatitis B — are destroyed by freezing); the __shake test__ detects a frozen adsorbed vaccine; use the __vaccine vial monitor (VVM)__ — discard at __stage 3 or 4__.",
        "Keep medicines in the __original labelled container__, tightly closed; light-sensitive drugs in amber bottles; store __external preparations separately from oral ones__; store liquids below powders/tablets to prevent damage from leakage.",
        "__Narcotics and Schedule X drugs__ in a __double-locked cupboard__ with a register and daily count (see Chapter 17); keep the keys with the nurse-in-charge.",
        "Follow __FEFO (first expiry, first out)__ and FIFO for stock rotation; check expiry dates monthly; maintain a stock/bin card, indent and issue register, and an emergency (crash) tray checked and sealed daily.",
        "Keep all medicines __out of the reach of children__; never store medicines with food; never transfer a drug to an unlabelled or food container.",
        "__Disposal__ — return expired and unused drugs to the pharmacy for documented destruction; ~never flush drugs down the toilet or throw them in household waste~ (antibiotics and cytotoxics are environmental hazards); expired drugs go in the __yellow bag for incineration__, cytotoxics in a labelled cytotoxic (yellow) container; narcotics are destroyed only before a witnessing committee with a record.",
    ])

    b.section_h("10.11", "Adverse Drug Reactions, Interactions and Pharmacovigilance")
    b.table(
        ["Type / topic", "Details"],
        [["__ADR types__", "Type A — augmented, dose-related and predictable (bleeding with warfarin, hypoglycaemia with insulin); Type B — bizarre, unpredictable, not dose-related (penicillin anaphylaxis); Type C — chronic/cumulative; Type D — delayed (carcinogenesis, teratogenesis); Type E — end-of-treatment (withdrawal); Type F — failure of therapy"],
         ["__Common ADRs to watch__", "Aspirin/NSAIDs — gastric bleeding; steroids — hyperglycaemia, Cushingoid features, infection, osteoporosis; aminoglycosides — nephrotoxicity and ototoxicity; chloroquine — retinopathy; isoniazid — hepatitis and neuritis; rifampicin — orange urine and hepatitis; ethambutol — optic neuritis; phenytoin — gum hypertrophy; metoclopramide/haloperidol — dystonia and extrapyramidal effects; ACE inhibitors — dry cough and hyperkalaemia; opioids — respiratory depression and constipation"],
         ["__Important interactions__", "Warfarin + aspirin/NSAID (bleeding); warfarin + vitamin-K rich food (reduced effect); digoxin + diuretic (hypokalaemia → toxicity); tetracycline/iron/fluoroquinolone + antacid, milk or calcium (chelation); MAO inhibitor + tyramine-rich food (hypertensive crisis); sildenafil + nitrate (severe hypotension); oral contraceptive + rifampicin/antiepileptics (failure); alcohol + metronidazole (disulfiram reaction); statin + grapefruit juice; methotrexate + NSAID"],
         ["__Antidotes__", "__Paracetamol → N-acetylcysteine__; opioids → __naloxone__; benzodiazepines → __flumazenil__; organophosphate → __atropine + pralidoxime__; warfarin → __vitamin K (+ FFP)__; heparin → __protamine sulphate__; iron → __desferrioxamine__; methanol/ethylene glycol → ethanol/fomepizole; digoxin → digoxin-specific antibody; cyanide → sodium thiosulphate/hydroxocobalamin; methotrexate → folinic acid (leucovorin); lead → EDTA/DMSA; snake bite → polyvalent anti-snake venom"],
         ["__Pharmacovigilance__", "__PvPI — Pharmacovigilance Programme of India__ (National Coordination Centre: __IPC, Ghaziabad__); report any suspected ADR on the __Suspected ADR reporting form (Form for reporting to PvPI)__, or by the ADR mobile app / toll-free number 1800-180-3024; WHO centre: __Uppsala Monitoring Centre, Sweden__"]],
        caption="Table 10.7  Adverse reactions, interactions and antidotes")

    b.box("recap", [
        "* Rights of administration: patient, drug, dose, route, time, documentation, refusal, assessment, education.",
        "* IV is fastest (100% bioavailability); oral is safest; sublingual and rectal avoid first-pass metabolism.",
        "* Angles: ID 10-15°, SC 45° (or 90° with short needle), IM 90°, IV 15-30°.",
        "* IM sites: deltoid (vaccines), vastus lateralis (infants), ventrogluteal (safest adult), dorsogluteal (sciatic nerve risk).",
        "* Dose = (ordered / on hand) × quantity; drip rate = (volume × drop factor) / minutes; micro-drip = 60 drops/mL.",
        "* 1 tsp = 5 mL; 1 tbsp = 15 mL; 1 g = 1000 mg; insulin only in an insulin syringe.",
        "* Never crush enteric-coated or sustained-release tablets; shake suspensions; record after giving, never before.",
        "* Anaphylaxis: adrenaline 1:1000, 0.5 mL IM in the mid-outer thigh, then oxygen, fluids, hydrocortisone, antihistamine.",
        "* Cold chain 2-8 °C; never freeze DPT/TT/hepatitis B; discard a vaccine at VVM stage 3/4; FEFO for stock.",
        "* Antidotes: paracetamol → N-acetylcysteine; opioid → naloxone; organophosphate → atropine + pralidoxime; heparin → protamine.",
    ])



def chapter_11(b):
    b.chapter(11, "Special Conditions and Treatments",
              "Local applications of heat and cold, inhalations, gargles, irrigations, enema, catheterisation and other nursing treatments")

    b.section_h("11.1", "Application of Heat")
    b.box("def", ["__Local application of heat__ causes __vasodilatation__ → increased blood supply, increased leucocyte and nutrient delivery, muscle relaxation and softening of exudate. It __relieves pain and spasm, hastens suppuration ('ripening' of an abscess), and promotes absorption and healing__."])
    b.table(
        ["Method", "Technique and temperature", "Uses", "Precautions"],
        [["__Hot water bag/bottle__ (dry heat)", "Fill __two-thirds__, expel air, screw the cap, invert to test for leaks, wrap in a flannel cover; water at __50-60 °C (adults)__, __40.5-46 °C for children, the elderly and the unconscious__; apply 20-30 min",
          "Abdominal colic, backache, muscle spasm, warming a cold patient, dysmenorrhoea",
          "__Never place directly on the skin__; never use for the unconscious, paralysed, anaesthetised, diabetic or confused patient, on a baby, or on an area with poor sensation; inspect the skin every 5-10 min for redness (risk of burns)"],
         ["__Electric heating pad / infrared lamp__", "Low setting; lamp __45-60 cm away__ for 15-20 min", "Muscular pain, stiff joints, bed sores (to dry the area)",
          "No pins, no wet dressing (electrocution), never lie on the pad"],
         ["__Hot moist compress / fomentation__ (moist heat — penetrates better)", "Gauze or flannel wrung out in hot water (40-46 °C), applied and covered with a mackintosh and towel; changed every 5 min for 15-20 min; may be sterile for a wound",
          "Boil, abscess, whitlow, stye, infected wound, breast engorgement, injection site induration, thrombophlebitis",
          "Aseptic technique for open wounds; protect the surrounding skin with petroleum jelly"],
         ["__Poultice (cataplasm)__", "Thick paste of kaolin/linseed/magnesium sulphate spread on gauze, heated and applied warm, covered to retain heat for 2-4 h",
          "Boils, abscesses, carbuncle — to localise infection and relieve pain", "Test the temperature on the back of your hand; do not apply too hot"],
         ["__Hot soaks / arm and foot bath__", "Immerse the part in water at 40-43 °C for 15-20 min", "Infected hand/foot, sprain, ingrowing nail, diabetic foot (with great care)",
          "Maintain the temperature by adding hot water at the side, away from the limb"],
         ["__Sitz (hip) bath__", "Patient sits in a tub with hot water (40-43 °C) covering the hips and buttocks for 15-20 min, feet outside; may add potassium permanganate or salt",
          "__After childbirth/episiotomy, haemorrhoids, fissure, perineal or rectal surgery, prostatitis__ — relieves pain, cleans and promotes healing",
          "Watch for faintness and giddiness; keep the shoulders covered; never leave the patient alone; check the temperature"],
         ["__Steam and hot air bath, wax bath, short-wave diathermy, ultrasound__", "Physiotherapy modalities", "Arthritis, chronic joint and muscle pain",
          "Given by a physiotherapist; diathermy is contraindicated with a metal implant or pacemaker"]],
        caption="Table 11.1  Methods of applying heat")

    b.section_h("11.2", "Application of Cold")
    b.box("def", ["__Local cold__ causes __vasoconstriction__ → reduced blood flow, reduced metabolism, reduced nerve conduction and reduced inflammation. It __checks bleeding and oedema, relieves pain and itching, limits inflammation and reduces temperature__."])
    b.table(
        ["Method", "Technique", "Uses", "Precautions"],
        [["__Ice bag / cold pack__", "Fill __one-third to two-thirds__ with crushed ice (small pieces), expel air, cover with a towel; apply __20-30 min, then rest__",
          "Sprain, contusion, fracture, headache, toothache, after tonsillectomy (ice collar), insect sting, sports injury, after an injection, to reduce swelling and bleeding",
          "Never apply ice directly on the skin (frost bite); remove if the skin becomes pale, blue, mottled or numb; avoid over an open wound, in Raynaud's disease and peripheral vascular disease"],
         ["__Cold compress__", "Gauze wrung out in cold water or iced water, changed every 2-3 min for 15-20 min",
          "Black eye, eye injury, epistaxis, headache, sprain, bleeding", "Do not let it become warm"],
         ["__Cold (tepid) sponging__", "Water at 27-32 °C, long strokes to the limbs, compresses in the axillae, groins and forehead, for about 20-30 min",
          "__Hyperpyrexia (over 39.5-40 °C)__, heat stroke", "Stop if __shivering__, cyanosis or collapse occurs; take the temperature after 30 min; never use ice water or alcohol"],
         ["__Ice cradle / ice collar / cold blanket__", "Ice bags suspended over the part / collar round the neck", "After tonsillectomy and thyroid surgery, hyperthermia",
          "Watch the skin; change the position"],
         ["__Evaporating lotion / cooling lotion__", "Lotion (spirit, calamine, lead lotion) applied on gauze and left uncovered to evaporate", "Sprains, inflamed joints, itching", "Do not cover with mackintosh (prevents evaporation)"]],
        caption="Table 11.2  Methods of applying cold")
    b.box("hy", [
        "__RICE__ for a fresh soft-tissue injury (first 24-48 hours) — __R~est~, I~ce~, C~ompression~, E~levation~__; heat is applied only ~after~ 48 hours, when bleeding has stopped.",
        "Never apply heat to: an acute injury within 48 h, an undiagnosed abdominal pain (~possible appendicitis — heat can cause rupture~), active bleeding, or a malignant swelling.",
    ])

    b.section_h("11.3", "Inhalations")
    b.table(
        ["Type", "Method", "Indication"],
        [["__Simple steam inhalation__", "Boiling water in a jug/inhaler with a paper funnel or a steam inhaler; the patient inhales steam through the mouth/nose for __10-15 minutes__, with a towel over the head; done 2-4 times daily",
          "Common cold, sinusitis, laryngitis, dry cough, croup, loosening thick secretions"],
         ["__Medicated steam inhalation__", "Add __tincture benzoin (5 mL to 500 mL water) or menthol, eucalyptus or camphor__ ('Nelson's inhaler')", "Sinusitis, bronchitis, nasal congestion"],
         ["__Dry/medicated inhalation__", "A few drops of a volatile oil on a handkerchief or in a bowl", "Nasal blockage"],
         ["__Nebulisation__", "Drug in solution converted to a fine mist by a jet/ultrasonic nebuliser and breathed through a mask or mouth-piece over __10-15 minutes__: __salbutamol, ipratropium, budesonide, adrenaline, hypertonic saline, antibiotics__",
          "__Acute asthma, bronchiolitis, croup, COPD, cystic fibrosis__, and any patient too breathless to use an inhaler"],
         ["__Metered dose inhaler (MDI) with spacer / dry powder inhaler__", "Shake, exhale, seal the lips, press and inhale slowly and deeply, hold the breath for __10 seconds__, wait 30-60 s before the next puff; use a __spacer__ for children and the elderly; __rinse the mouth after a steroid inhaler__",
          "Maintenance treatment of asthma and COPD"]],
        caption="Table 11.3  Inhalation therapy")
    b.box("caution", ["Steam inhalation carries a real risk of __scalding__ — keep the jug on a low, stable surface, never on the patient's lap or bed, and never leave a child or a confused patient alone with it. Watch for giddiness and stop if the patient feels faint."])

    b.section_h("11.4", "Mouth, Throat, Eye, Ear and Nose Treatments")
    b.table(
        ["Treatment", "Procedure and points"],
        [["__Gargle__", "Warm solution (normal saline, salt water, povidone-iodine 2%, chlorhexidine, potassium permanganate 1:8000) held at the back of the throat and agitated by exhaling, then __spat out, not swallowed__; 2-4 times daily. For sore throat, tonsillitis, after oral surgery"],
         ["__Throat paint / swab__", "Mandl's paint (compound iodine glycerine) applied to the tonsils and pharynx with a swab on a holder, using a tongue depressor and good light; __the patient must not eat or drink for 30 minutes__ afterwards; watch for gagging and vomiting"],
         ["__Eye drops (instillation)__", "Wash hands, check the drug, strength, eye (right/left) and expiry; clean the lids from inner to outer canthus; the patient looks up; pull down the lower lid to form a pouch and drop the medicine into the __lower conjunctival sac (never on the cornea)__ holding the dropper __1-2 cm above__ without touching the eye or lashes; ask the patient to close the eye gently (not to squeeze) and press the inner canthus (~punctal occlusion~) for 1 min to reduce systemic absorption; wait __5 minutes between two different drops__; apply ointment in a thin line from the inner to the outer canthus __after__ the drops; one dropper per patient per eye; use for a maximum of 4 weeks after opening"],
         ["__Eye irrigation (eye wash)__", "Normal saline or the prescribed lotion at body temperature, poured __from the inner canthus to the outer canthus__ with the head turned to the side, kidney tray below; used for chemical burns (irrigate copiously for at least 15-20 min), discharge and foreign bodies"],
         ["__Eye pad and bandage__", "Sterile pad over the closed lid, secured obliquely (never press on the eyeball); after surgery or injury"],
         ["__Ear drops__", "Warm the bottle to room/body temperature (__cold drops cause giddiness and vertigo__); position the patient with the affected ear __uppermost__; pull the pinna __up and back in adults, down and back in children under 3 years__; instil the drops on the wall of the canal; keep the position for __5-10 minutes__ and press the tragus gently; plug loosely with cotton only if ordered"],
         ["__Ear irrigation (syringing)__", "Done by a doctor/trained nurse for wax (softened first with olive oil or soda-glycerine for 2-3 days); fluid at __37 °C__ directed at the upper posterior wall; __contraindicated if the drum is perforated or there is discharge/infection__; watch for pain, giddiness and vomiting"],
         ["__Nasal drops / spray__", "Blow the nose first; for the sinuses use the __'Proetz' head-low position__ (head extended back over the edge of the bed) or lateral head-low position; instil the drops and keep the position for 1-2 minutes; breathe through the mouth; do not share the dropper; limit decongestant drops to __under 5-7 days__ (rebound congestion — rhinitis medicamentosa)"]],
        caption="Table 11.4  Local treatments of the head and neck")

    b.section_h("11.5", "Enema, Suppository and Flatus Tube")
    b.box("def", ["__Enema__ — the introduction of a solution into the rectum and lower colon through a rectal tube, for cleansing, evacuation, retention or diagnostic purposes."])
    b.table(
        ["Type of enema", "Solution and amount", "Purpose / indication"],
        [["__Cleansing (evacuant) enema__ — soap and water, normal saline, tap water",
          "Adult __500-1000 mL at 40.5-43 °C (105-110 °F)__; child 250-500 mL; infant 50-150 mL; soap solution: 5 mL of soft soap per 1000 mL",
          "Constipation and faecal impaction; before surgery, delivery, sigmoidoscopy/colonoscopy or an X-ray of the abdomen"],
         ["__Retention enema__ (oil retention)", "Olive/arachis oil or glycerine __100-200 mL__, retained for __1-3 hours__ (or as long as possible)",
          "Softening hard impacted faeces; often followed later by a cleansing enema"],
         ["__Medicated / therapeutic enema__", "Prescribed drug — __steroid (ulcerative colitis), neomycin, lactulose, sodium polystyrene sulphonate (for high potassium), paraldehyde/diazepam (for convulsions)__",
          "To give a drug when the oral route is impossible or for local action"],
         ["__Carminative (flatus) enema__", "Milk and molasses, or magnesium sulphate + glycerine + water (MGW) 30:60:90 mL", "To expel flatus and relieve abdominal distension"],
         ["__Astringent enema__", "Cold normal saline, alum or tannic acid solution", "To check bleeding and reduce inflammation"],
         ["__Emollient / sedative / stimulant / nutrient enema__", "Starch, thin gruel / paraldehyde / coffee / glucose saline (~obsolete~)", "Soothing, sedation, stimulation, nutrition (historical)"],
         ["__Barium enema__", "Barium sulphate suspension given under X-ray control", "__Diagnostic__ — X-ray of the large bowel"],
         ["__Disposable phosphate (Enema Fleet) / glycerine suppository__", "Small volume (about 118 mL) ready-to-use", "Quick bowel evacuation; commonly used today"]],
        caption="Table 11.5  Types of enema")
    b.sub("Procedure of giving a cleansing enema")
    b.numbered([
        "Check the order; explain; screen the bed; keep a bedpan/commode and toilet paper ready close by; wash hands, wear gloves.",
        "Position: __left lateral (Sims') position with the right knee flexed__ — this follows the anatomical direction of the sigmoid colon (the knee-chest position is an alternative; infants are placed supine with the legs raised).",
        "Place a mackintosh and towel under the buttocks; hang the enema can __45-50 cm (18 inches) above the anus__ (a lower height and slower flow for a child); expel the air from the tubing.",
        "Lubricate the rectal tube (12-16 Fr for an adult) and insert it gently __7.5-10 cm (3-4 inches) in an adult__ (5 cm in a child, 2.5-3.75 cm in an infant), directing it towards the umbilicus; ~never force against resistance~.",
        "Allow the fluid to run in __slowly over 5-10 minutes__; ask the patient to breathe deeply through the mouth; stop temporarily if there is cramping; clamp the tube before it empties completely (to avoid air entry) and withdraw it gently, holding a pad against the anus.",
        "Ask the patient to __retain the fluid for 5-15 minutes__ (oil retention 1-3 h); then give the bedpan or assist to the toilet; do not leave a weak patient alone.",
        "Observe and record the __amount, colour, consistency and content of the returned flow__, the patient's tolerance, and the result (whether the bowel was cleared). Clean and disinfect the equipment; wash hands."
    ])
    b.box("caution", [
        "__Contraindications to an enema:__ undiagnosed abdominal pain, suspected appendicitis or peritonitis, intestinal obstruction, recent rectal/colonic surgery, rectal bleeding, severe piles/fissure, pregnancy near term (unless ordered), raised intracranial pressure, and a patient with a very low platelet count or neutropenia.",
        "__Dangers:__ perforation of the rectum, vagal stimulation (bradycardia, fainting), water intoxication and electrolyte imbalance (repeated tap-water enemas, especially in children and renal patients), dependence with repeated use, and mucosal damage.",
    ])
    b.bullets([
        "__Suppository__ — a bullet-shaped solid inserted into the rectum: __glycerine/bisacodyl (constipation), paracetamol or diclofenac (fever and pain), diazepam (convulsions), antihaemorrhoidal__. Position: left lateral; wear a glove, lubricate the tip, insert __past the internal sphincter (about 5-7.5 cm in an adult, 2.5 cm in a child) against the rectal wall__; ask the patient to retain it for __20-30 minutes__. Store suppositories in a __cool place/refrigerator__.",
        "__Flatus tube__ — a wide, soft rectal tube (24-32 Fr) inserted 10-15 cm with the outer end under water in a bowl, kept for __not more than 20-30 minutes__, to relieve __abdominal distension (flatulence) after operation__; bubbling shows the escape of gas. Alternatives: hot fomentation, early ambulation, and a prescribed prokinetic.",
    ])

    b.section_h("11.6", "Urinary Catheterisation and Bladder Irrigation")
    b.bullets([
        "__Indications__ — acute or chronic __retention of urine__, accurate output measurement in a critical patient, before and after certain surgeries and during labour, bladder irrigation, instillation of a drug, urinary incontinence with pressure sores, collection of a sterile specimen, and to keep the bladder empty in pelvic surgery.",
        "__Types__ — intermittent (Nelaton/simple, plain catheter), __indwelling (Foley — 2-way with a balloon, 3-way for irrigation)__, suprapubic, condom (Uridom) drainage in men. Sizes: __adult female 14-16 Fr, adult male 16-18 Fr, children 6-10 Fr__; 1 Fr = 1/3 mm.",
        "__Strict aseptic technique__ — sterile gloves, sterile catheter and lubricant (2% lignocaine jelly), antiseptic cleaning of the meatus, sterile drape. Position: female — dorsal recumbent with knees flexed and separated; male — supine with the legs slightly apart.",
        "Clean the __female__ perineum from front to back and identify the __urethral meatus above the vaginal opening__ (insert 5-7.5 cm until urine flows, then 2.5 cm more); in the __male__, retract the foreskin, hold the penis at __60-90 degrees__, insert __17-22.5 cm__ until urine flows, then advance further before inflating; __replace the foreskin afterwards__.",
        "__Inflate the balloon only after urine flows__ (5-10 mL of sterile water, ~not saline~ — it can crystallise); if the patient complains of pain while inflating, stop at once (the balloon may be in the urethra).",
        "In __chronic retention__, drain gradually (some authorities advise clamping after 300-500 mL and releasing after 15-30 min) to prevent __haematuria, hypotension and post-obstructive diuresis__.",
        "__Care of an indwelling catheter__ — keep the __drainage bag below the level of the bladder but off the floor__, never disconnect the closed system, prevent kinking and loops, secure the catheter to the thigh/abdomen, do a __meatal toilet with soap and water daily__, encourage __fluid intake of 2-3 L__, empty the bag when two-thirds full using a separate container for each patient, measure and record output, take specimens from the sampling port with aseptic technique, and __remove the catheter as early as possible__ (the risk of infection rises by about 5% per day).",
        "__Bladder irrigation/washout__ — continuous with a 3-way catheter (after prostate/bladder surgery to prevent clot retention) or intermittent with sterile normal saline at room temperature; record the volume in and out separately and __subtract the irrigation fluid from the total output__; report bright-red drainage, clots or no outflow at once.",
        "__Complications__ — catheter-associated UTI (the commonest hospital-acquired infection), urethral trauma and stricture, bleeding, false passage, paraphimosis (foreskin not replaced), bladder spasm, blockage, and encrustation.",
    ])

    b.section_h("11.7", "Other Special Treatments")
    b.table(
        ["Treatment", "Description and nursing points"],
        [["__Vaginal douche / irrigation__", "Warm antiseptic solution (40-43 °C) run into the vagina in the dorsal recumbent position with a bedpan; for pre-operative preparation and discharge; ~avoid in pregnancy and menstruation~"],
         ["__Vaginal pessary/cream__", "Inserted at bedtime in the lying position with an applicator; the patient is told it may stain and to use a pad"],
         ["__Medicated (therapeutic) bath__", "KMnO4 1:5000-1:10 000 for infected skin; sodium bicarbonate/oatmeal/starch for itching; emollient bath for eczema; 15-30 min, water at 37-40 °C"],
         ["__Wet packs and cold/hot wet sheet packs__", "Whole-body application for hyperpyrexia or skin disease; watch the pulse and for shivering"],
         ["__Counter-irritants__", "__Mustard plaster/poultice__ (1 part mustard to 4-6 parts flour, applied for __15-20 minutes only__, protecting the skin with gauze and oil — remove at once if there is burning), turpentine stupe, liniment rubs, capsaicin ointment; used for chest congestion and muscular pain; __never apply to broken skin or to children/the unconscious__"],
         ["__Cupping, blistering, leeching, venesection__", "Old (largely historical) methods of counter-irritation and blood letting; __leech therapy__ is still occasionally used in plastic surgery and traditional medicine; __venesection__ is used today for polycythaemia and haemochromatosis"],
         ["__Local applications__", "Lotion (cooling), liniment (rubbed in for pain), paint, ointment/cream (applied thinly in the direction of hair growth with a spatula or gloved hand), paste (thick protective layer), dusting powder (dry, on intact skin), plaster; wear gloves for hormone, steroid and cytotoxic preparations"],
         ["__Ryle's tube aspiration (gastric lavage/decompression)__", "For poisoning (only within 1 hour, with a protected airway; ~contraindicated in corrosive and hydrocarbon poisoning~), pyloric obstruction, paralytic ileus, before emergency surgery; use warm normal saline/tap water 200-300 mL at a time, save the first aspirate for analysis, measure and record the aspirate"],
         ["__Cold and hot applications to the eye, ear and joints__", "As described above; never apply heat to an inflamed eye without an order"]],
        caption="Table 11.6  Miscellaneous nursing treatments")

    b.box("recap", [
        "* Heat = vasodilatation (relieves spasm, hastens suppuration); cold = vasoconstriction (checks bleeding, oedema, pain). RICE for fresh injury; heat only after 48 h.",
        "* Hot water bag: fill two-thirds, 50-60 °C for adults, 40.5-46 °C for children/elderly/unconscious, always covered.",
        "* Sitz bath 40-43 °C for 15-20 min — episiotomy, piles, fissure, perineal surgery.",
        "* Steam inhalation 10-15 min with tincture benzoin; nebulisation for acute asthma; rinse the mouth after steroid inhalers.",
        "* Eye drops in the lower conjunctival sac, inner→outer canthus for cleaning; ear drops warmed, pinna up-and-back in adults, down-and-back in children.",
        "* Enema: left lateral (Sims') position, can 45-50 cm high, tube inserted 7.5-10 cm, solution 500-1000 mL at 40.5-43 °C, retain 5-15 min; contraindicated in suspected appendicitis and obstruction.",
        "* Catheter: female 14-16 Fr / male 16-18 Fr; inflate the balloon only after urine flows, with sterile water; bag below bladder level, closed system, remove early.",
        "* Flatus tube for not more than 20-30 minutes; mustard plaster for 15-20 minutes only.",
    ])



def chapter_12(b):
    b.chapter(12, "Bandaging",
              "Purposes, principles, types of bandages, basic turns, slings, splints and strapping")

    b.section_h("12.1", "Definition and Purposes")
    b.box("def", ["__Bandage__ — a strip or roll of cloth or other material used to hold a dressing in place, to support, immobilise or compress a part, or to correct a deformity.  __Binder__ — a broad bandage applied to a large area such as the chest, abdomen, breast or perineum."])
    b.sub("Purposes of bandaging")
    b.bullets([
        "To __keep a dressing or splint in position__ and protect the wound from injury and infection.",
        "To give __support__ to a part (sprain, muscle strain, hernia, pendulous breast).",
        "To apply __pressure__ — to arrest haemorrhage, to reduce or prevent swelling and oedema, and to prevent varicose veins and deep vein thrombosis (compression bandage/stocking).",
        "To __immobilise and rest__ a part — fracture, dislocation, after tendon repair.",
        "To __restrict movement__, to maintain a limb in a required position, and to correct a deformity.",
        "To __hold an appliance__ (splint, traction, plaster) in place and to hold packs.",
    ])

    b.section_h("12.2", "Types of Bandages and Materials")
    b.table(
        ["Type", "Description", "Common uses"],
        [["__Roller bandage__", "A long strip rolled up; made of cotton, gauze, flannel, crepe, elastic (crepe/elastocrepe), plaster of Paris or a self-adhesive material; has a __head (the roll)__ and a __tail (the free end)__",
          "Most commonly used bandage for limbs, head and trunk"],
         ["__Triangular bandage__", "A square (about 1 m x 1 m) of cloth cut across diagonally, giving a base, a point and two ends; can be used open, as a __broad fold__ or a __narrow fold__",
          "Slings, head, hand, foot, chest, hip and knee dressings; first aid — the most versatile first-aid bandage"],
         ["__T-bandage (single and double T)__", "A horizontal band with one or two vertical tails", "Holding a perineal or rectal dressing; double-T for men"],
         ["__Four-tailed bandage__", "A strip with both ends split into two tails", "Chin/jaw, nose, head and elbow dressings"],
         ["__Many-tailed (Scultetus) bandage__", "Several overlapping strips fixed to a central piece", "Abdomen and chest — easy to change without moving the patient"],
         ["__Suspensory bandage__", "A bag with a waist band", "Support of the scrotum (after hydrocele or vasectomy surgery, orchitis)"],
         ["__Tubular / tubegauze bandage__", "Seamless woven tube applied with an applicator", "Fingers, toes, limbs, head — quick and comfortable"],
         ["__Capeline / Barton / Gibson bandage__", "Special double-headed roller bandages of the head and jaw", "Scalp and jaw injuries"],
         ["__Adhesive strapping (plaster) and tape__", "Zinc oxide, micropore, dynaplast, elastic adhesive", "Fixing dressings, strapping ribs, holding splints"],
         ["__Crepe / elastic compression bandage__", "Stretchable, self-clinging", "Sprains, varicose veins, oedema, venous ulcer, after a fracture"],
         ["__Plaster of Paris (POP) bandage and fibreglass cast__", "Gauze impregnated with gypsum, dipped in water", "Immobilising fractures"],
         ["__Improvised bandages__", "Clean handkerchief, dupatta, towel, sari strip, belt, stockings, necktie", "Emergency and home nursing"]],
        caption="Table 12.1  Types of bandages")
    b.box("num", [
        "__Standard widths of a roller bandage (learn these):__",
        "* __Finger and toe — 1.25-2.5 cm (0.5-1 inch)__",
        "* __Hand, wrist and head — 5 cm (2 inches)__ (head 5-7.5 cm)",
        "* __Arm and forearm — 5-6.5 cm (2-2.5 inches)__",
        "* __Leg and foot — 7.5 cm (3 inches)__ • __Thigh — 9-10 cm__",
        "* __Trunk, chest and abdomen — 10-15 cm (4-6 inches)__",
        "Usual length: 5-6 metres for limb bandages.",
    ])

    b.section_h("12.3", "General Rules and Principles of Bandaging")
    b.numbered([
        "Explain the procedure and place the patient in a __comfortable position__; the nurse stands __facing the part__ to be bandaged and supports the limb.",
        "Bandage the part in the __position in which it is to remain__ — joints slightly flexed, the ankle at a right angle, the fingers slightly flexed; place soft pads between skin surfaces and over bony points.",
        "Work generally from __below upwards and from within outwards (medial to lateral)__, and from the __distal to the proximal end__ (this aids venous return).",
        "Hold the __roll (head) uppermost in the right hand__ with the outer surface applied to the part; unroll only a little at a time, keeping the roll close to the skin.",
        "Fix the bandage with __two circular turns__ at the start, and finish with a circular turn secured by a __safety pin, adhesive tape, a clip or a tie__ — the fastening must be placed on the __outer side, away from the wound, and never over a bony point, a joint or the inner side of a limb__.",
        "Apply with __even, firm but not tight pressure__; each turn should cover __one-half to two-thirds__ of the previous one, and no skin should show between the turns.",
        "Keep the bandage __neat, smooth and free of wrinkles, creases and gaps__; it should be comfortable and light.",
        "__Leave the finger tips and toes exposed whenever possible__ so that the circulation can be watched.",
        "__Never bandage over a wet dressing__, and never apply a wet bandage that will shrink on drying.",
        "__Check the circulation__ after applying, and at intervals; re-bandage if the patient complains of pain, numbness, tingling or throbbing; re-apply a limb bandage at least once a day and keep the part elevated if there is swelling.",
        "Remove a bandage by cutting with blunt-nosed scissors (away from the wound) or by unwinding it, gathering it loosely from hand to hand — ~never drag it across a wound~."
    ])
    b.box("caution", [
        "__Signs that a bandage is too tight (impaired circulation) — remove or loosen at once:__",
        "* Pain, throbbing or a feeling of tightness;  __numbness, tingling (pins and needles) or loss of sensation__",
        "* __Coldness, pallor, then blueness (cyanosis) of the fingers or toes__;  swelling below the bandage",
        "* __Capillary refill slower than 3 seconds__; absent or weak pulse beyond the bandage; inability to move the fingers/toes",
        "* Remember the __5 P's of impaired circulation: Pain, Pallor, Paraesthesia, Pulselessness, Paralysis__ — the warning signs of __compartment syndrome__, a surgical emergency.",
    ])

    b.section_h("12.4", "Basic Bandage Turns")
    b.table(
        ["Turn", "Technique", "Where used"],
        [["__Circular turn__", "Each turn exactly over the previous one", "To begin and end every bandage; wrist, neck, forehead, finger"],
         ["__Spiral turn__", "Turns ascend at a slight angle, each overlapping two-thirds of the previous", "Parts of __uniform thickness__ — finger, upper arm, trunk, wrist"],
         ["__Spiral reverse turn__", "The bandage is reversed (folded on itself) halfway through each turn, with the thumb steadying the fold",
          "Parts of __varying thickness__ — forearm and leg (used with a non-elastic bandage)"],
         ["__Figure-of-eight turn__", "Oblique turns alternately above and below the joint, crossing in front like the figure 8",
          "__Joints — elbow, knee, ankle, wrist__; also for firm support and compression"],
         ["__Spica (a modified figure-of-eight)__", "Alternate ascending and descending turns overlapping to look like an ear of corn",
          "__Shoulder, hip, thumb, groin, breast__ (shoulder spica, hip spica, thumb spica)"],
         ["__Recurrent (capeline) turn__", "Bandage passed back and forth over the tip of the part, then fixed with circular turns",
          "__Finger tip, toe, stump after amputation, head (scalp)__"],
         ["__Divergent / convergent turn__", "Turns spread out from or converge towards the middle of a flexed joint", "Elbow and knee in a flexed position"]],
        caption="Table 12.2  The basic bandage turns")
    b.sub("Bandaging particular parts — key points")
    b.table(
        ["Part", "Bandage and method"],
        [["Finger", "2.5 cm roller — circular at the wrist, oblique to the finger, recurrent over the tip, spiral down the finger, then figure-of-eight back to the wrist"],
         ["Hand and palm", "5 cm roller — figure-of-eight round the hand and wrist, leaving the thumb free"],
         ["Thumb", "__Thumb spica__"],
         ["Forearm and leg", "__Spiral reverse__ turns from the wrist/ankle upwards"],
         ["Elbow and knee", "__Figure-of-eight__ with the joint slightly flexed (divergent turns)"],
         ["Shoulder and hip", "__Spica__"],
         ["Foot and ankle", "Figure-of-eight, starting at the instep, with the ankle at 90 degrees; the heel and toes may be left exposed"],
         ["Heel", "Figure-of-eight with locking turns"],
         ["Head / scalp", "__Capeline (double-headed) or recurrent turns__, or a triangular bandage as a head cap"],
         ["Eye", "Oblique turns round the head and under the ear on the affected side (never over the other eye if it can be avoided)"],
         ["Ear / jaw / chin", "Four-tailed or a barrel bandage"],
         ["Chest and abdomen", "Broad roller, many-tailed (Scultetus) bandage or a binder"],
         ["Breast", "Breast binder or a spica; applied for support and after surgery"],
         ["Stump (after amputation)", "Recurrent turns with firm even pressure to shape the stump"]],
        caption="Table 12.3  Bandaging specific parts")

    b.section_h("12.5", "Slings")
    b.table(
        ["Sling", "Method", "Indication"],
        [["__Arm (large/St John) sling__", "Triangular bandage: point towards the injured elbow, one end over the sound shoulder and round the neck, tied in the hollow above the clavicle; the __hand is supported slightly higher than the elbow__, the fingers visible, the point tucked in and pinned",
          "Fracture/injury of the __forearm, wrist and hand__; after a dressing or plaster; support in rib injury"],
         ["__Collar-and-cuff (triangular) sling__", "A clove-hitch round the wrist with a narrow-fold bandage, tied round the neck, the elbow hanging free",
          "__Fracture of the humerus/upper arm__ and of the clavicle, where the weight of the arm gives traction"],
         ["__Elevation (St John) sling__", "Fingers placed on the opposite shoulder with the forearm across the chest; the bandage is brought round the back and tied, so the hand is well raised",
          "To control __bleeding of the hand/forearm__, with a hand injury or infection, and in a __fractured clavicle or crushed hand__ (elevation reduces swelling)"],
         ["__Figure-of-eight bandage of the shoulders__", "Both shoulders braced back", "__Fractured clavicle__"],
         ["__Triangular bandage as a broad/narrow fold__", "Fixation of splints, tying limbs together", "Fracture immobilisation in first aid"]],
        caption="Table 12.4  Types of slings")

    b.section_h("12.6", "Splints, Strapping and Plaster of Paris")
    b.bullets([
        "__Splint__ — a rigid or semi-rigid appliance used to immobilise and support a fractured or injured part. Types: wooden (Bohler), metal, plastic, air/inflatable, vacuum, moulded thermoplastic, Thomas splint (for the femur), Cramer wire, Kramer, POP slab, cardboard/newspaper and improvised (rolled magazine, umbrella, stick, even the patient's own body).",
        "__Rules for splinting__ — immobilise the __joint above and the joint below__ the fracture; pad the splint well and place padding over bony points; splint __in the position found__ (do not attempt to reduce); check the __pulse, colour, warmth, sensation and movement before and after__ splinting; tie the bandages __firmly but not tightly, and never directly over the fracture site__; remove rings and bangles; elevate afterwards; do not delay transport for perfect splinting in a life-threatening emergency.",
        "__Strapping (adhesive taping)__ — used for rib injury, sprained ankle, fixing a dressing, and to approximate wound edges (Steri-strips). Clean and dry the skin, shave the hair, apply a protective spray or under-wrap, and apply the strips at right angles to the direction of pull, never in a complete circle around a limb.",
        "__Care of a plaster cast__ — keep the limb __elevated__ for 24-48 h; leave the wet cast __uncovered and exposed to the air to dry (24-72 h)__, handle it with the __palms, never the finger tips__ (dents cause pressure sores), do not rest it on a hard edge; keep the cast __dry and clean__, do not insert anything (knitting needle, pencil) inside to scratch, do not remove the padding or cut the cast without an order; encourage exercise of the free joints and isometric exercises of the muscles under the cast.",
        "__Observe and report at once__ — pain (especially increasing or on passive stretch), swelling, __coldness, blueness or numbness of the toes/fingers, inability to move them__, a foul smell or a discharge stain on the cast (infection), a hot spot, or a loose or cracked cast. __Window or bivalve the cast__ if the surgeon orders; keep a cast cutter/shears available.",
        "__Complications of a cast__ — compartment syndrome, pressure sores, nerve palsy (peroneal, ulnar), joint stiffness, muscle atrophy, disuse osteoporosis, deep vein thrombosis, and plaster dermatitis.",
    ])

    b.box("recap", [
        "* Bandage = holds dressings, supports, compresses, immobilises. Binder = broad bandage for the trunk.",
        "* Widths: finger 1.25-2.5 cm, hand/head 5 cm, arm 5-6.5 cm, leg 7.5 cm, thigh 9-10 cm, trunk 10-15 cm.",
        "* Bandage from distal to proximal, medial to lateral, roll uppermost, each turn covering two-thirds of the previous; start and finish with circular turns; fasten on the outer side away from the wound.",
        "* Turns: circular (start/finish), spiral (uniform part), spiral reverse (forearm/leg), figure-of-eight (joints), spica (shoulder/hip/thumb), recurrent (finger tip/stump/head).",
        "* Slings: arm sling = forearm and wrist injury; collar-and-cuff = fractured humerus; elevation sling = bleeding hand, crushed hand, fractured clavicle.",
        "* Too tight: pain, pallor, paraesthesia, pulselessness, paralysis (5 P's) — loosen at once; leave the finger tips exposed.",
        "* Splint the joints above and below; never dent a wet plaster — handle with the palms; keep it elevated, uncovered and dry.",
    ])


def chapter_13(b):
    b.chapter(13, "Further Observations",
              "Specimen collection, bedside tests, fluid balance, danger signals and documentation")

    b.section_h("13.1", "Collection of Specimens — General Rules")
    b.numbered([
        "Check the doctor's order and the __correct container__ (with or without preservative/anticoagulant); explain the procedure to the patient and obtain co-operation.",
        "__Label the container before or immediately after collection__ with the patient's name, age, sex, hospital/bed number, the specimen, the site, the date and __time of collection__, and the test required; fill and attach the requisition form.",
        "Collect the __right specimen, in the right amount, at the right time__ (for example, a fasting sample before breakfast, a sputum sample early in the morning, a blood culture __at the onset of a fever spike and before starting antibiotics__).",
        "Use __standard precautions__ — gloves for every specimen; collect with aseptic technique where sterility is needed; never contaminate the outside of the container; place it in a leak-proof plastic bag ('double bagging').",
        "__Send it to the laboratory at once__; if delayed, follow the preservation rule (refrigerate urine; keep a blood culture bottle at room temperature or in an incubator; never refrigerate cerebrospinal fluid for culture).",
        "__Record__ the collection and dispatch in the nurse's notes, and __follow up the report__ and inform the doctor of an abnormal or critical value."
    ])
    b.table(
        ["Specimen", "How to collect", "Key points"],
        [["__Routine (random) urine__", "10-20 mL in a clean, dry, wide-mouthed container", "Preferably the first morning sample (most concentrated)"],
         ["__Mid-stream clean-catch urine (for culture)__", "Clean the meatus with soap and water/antiseptic (female: front to back); pass the first part into the toilet, collect the middle part in a __sterile container__ without touching the rim, and let the last part go",
          "Never take a culture sample from the urine bag or bedpan; send within 1 hour or refrigerate (up to 24 h); the sample must not be taken while on antibiotics if avoidable"],
         ["__Catheter specimen__", "Aspirate with a sterile syringe from the __sampling port__ after cleaning it with spirit (clamp the tube briefly below the port)", "Never disconnect the closed system or take urine from the bag"],
         ["__24-hour urine__", "Discard the first voiding at the start time and note it; collect __every drop for the next 24 hours__, including the voiding at the end time, in a large container with the correct preservative, kept cool/refrigerated",
          "If one sample is missed, the whole collection must be restarted; used for creatinine clearance, protein, VMA, catecholamines, 17-ketosteroids"],
         ["__Stool__", "A walnut-sized/2-3 spoonful sample from a clean, dry bedpan in a clean container, using a spatula; include portions with blood or mucus",
          "__Must not be contaminated with urine or water__; send a fresh warm sample within 30 minutes for amoebic trophozoites; 3 samples on alternate days for ova/parasites; use a sterile container for culture; occult blood test needs a meat-free, iron-free diet for 3 days"],
         ["__Sputum__", "__Early morning, on rising, before eating or brushing__, after rinsing the mouth with plain water; take a __deep cough__ from the chest (not saliva) into a sterile wide-mouthed container; 5-10 mL; ~2 samples (spot and morning) for tuberculosis__",
          "Explain the difference between sputum and saliva; wear a mask and collect in a well-ventilated place/away from others; send at once or refrigerate; for cytology, send in 70% alcohol"],
         ["__Throat swab__", "Good light, tongue depressor, sterile swab rubbed over both tonsils and the posterior pharynx __avoiding the tongue, teeth and cheeks__; the patient says 'aah'",
          "Best before food or gargling and before antibiotics; may cause gagging"],
         ["__Blood__", "Venepuncture with aseptic technique — the correct vacutainer and the correct __order of draw__; the tourniquet must not stay on for more than 1 minute; mix anticoagulated tubes by gentle inversion (__never shake — it haemolyses the sample__); apply pressure, not massage, afterwards",
          "__Never draw blood from the arm with an IV infusion__ (or take it below the site with the drip stopped); fasting samples need 8-12 h of fasting (water allowed); label at the bedside in the patient's presence"],
         ["__Blood culture__", "2 sets from 2 different sites, __at the onset of a chill/fever and before antibiotics__, 10 mL per bottle in an adult; clean the skin with 70% alcohol then chlorhexidine/povidone-iodine and let it dry; disinfect the bottle top",
          "Skin preparation is critical to avoid contamination; do not refrigerate"],
         ["__Wound swab / pus__", "Sterile swab rotated over the __base and edge of the wound__ (not the surrounding skin or the dry crust) after removing the old dressing and cleaning off the slough with saline; aspirated pus in a sterile syringe is better",
          "Take the sample __before__ applying any antiseptic and before starting antibiotics"],
         ["__Vomitus / gastric aspirate__", "Whole specimen in a clean covered container", "Essential in suspected poisoning — preserve and hand over to the doctor/police"],
         ["__Cerebrospinal fluid, pleural, ascitic and joint fluid__", "Collected by the doctor at lumbar puncture or aspiration; the nurse labels 3 numbered sterile tubes and sends them at once",
          "Handle as highly infectious; never delay or refrigerate a CSF culture sample"]],
        caption="Table 13.1  Collection of common specimens")

    b.section_h("13.2", "Simple Bedside Tests")
    b.table(
        ["Test", "Method", "Interpretation"],
        [["__Urine sugar (Benedict's test)__", "5 mL Benedict's qualitative reagent + __8 drops of urine__, boil for 2 min and cool",
          "Blue = nil • __green = + (0.5%) • yellow = ++ (1%) • orange = +++ (1.5%) • brick red = ++++ (2% or more)__"],
         ["__Urine ketones (Rothera's / strip)__", "Saturate urine with ammonium sulphate, add sodium nitroprusside and ammonia", "A __purple ring__ = ketones present (diabetic ketoacidosis, starvation, vomiting)"],
         ["__Urine protein (heat and acetic acid test)__", "Boil the upper part of the urine in a test tube and add 2-3 drops of acetic acid",
          "Persistent cloudiness (turbidity) = __albuminuria__ (renal disease, pre-eclampsia)"],
         ["__Reagent (dip) strip__", "Dip, remove excess, read against the chart at the exact time",
          "Reads pH, specific gravity, protein, glucose, ketone, blood, nitrite, leucocyte esterase, bilirubin, urobilinogen"],
         ["__Capillary blood glucose (glucometer)__", "Clean the __side of the finger tip__ with spirit and let it dry, prick with a sterile lancet, wipe the first drop, apply the second drop to the strip",
          "Fasting normal __70-100 mg/dL__ (diabetes 126 or more); random/post-prandial under 140 (diabetes 200 or more); __hypoglycaemia under 70 mg/dL__ — an emergency"],
         ["__Pulse oximetry__", "Probe on a clean, warm finger (remove nail polish), read after the waveform stabilises", "Normal __95-100%__; under 90% = hypoxia needing oxygen"],
         ["__Peak expiratory flow (PEFR)__", "Standing, maximum inspiration, then a fast hard blow; best of 3 readings",
          "Compare with the personal best/predicted — under 80% = poor control, __under 50% = severe attack__"],
         ["__Weight and height, BMI, mid-arm circumference__", "Same time of day, same clothes, calibrated scale",
          "A gain of 1 kg = about 1 L of fluid; MUAC under 11.5 cm (6-59 months) = __severe acute malnutrition__"],
         ["__Pregnancy test (urine hCG)__", "First morning urine on the card/strip", "Two lines = positive; detectable about 10-14 days after conception"]],
        caption="Table 13.2  Bedside/point-of-care tests")

    b.section_h("13.3", "Normal Values Every Nurse Should Know")
    b.table(
        ["Investigation", "Normal value"],
        [["Haemoglobin", "__Men 13-17 g/dL, women 12-15 g/dL__; WHO anaemia cut-off: men under 13, women under 12, pregnancy under 11, children 6-59 months under 11 g/dL"],
         ["Total leucocyte count / differential", "__4000-11 000/mm3__; neutrophils 40-75%, lymphocytes 20-45%, eosinophils 1-6%, monocytes 2-10%, basophils 0-1%"],
         ["Platelets", "__1.5-4.5 lakh/mm3 (150 000-450 000)__ — bleeding risk below 50 000, spontaneous bleeding below 20 000"],
         ["ESR", "Men 0-15 mm, women 0-20 mm in the 1st hour"],
         ["Blood sugar", "Fasting __70-100 mg/dL__; 2-hour post-prandial under 140; HbA1c under 5.7% (diabetes 6.5% or more; target under 7%)"],
         ["Blood urea / Serum creatinine", "__Urea 15-40 mg/dL (BUN 7-20); creatinine 0.6-1.2 mg/dL__"],
         ["Serum electrolytes", "__Sodium 135-145 mEq/L; potassium 3.5-5.0 mEq/L__; chloride 96-106; bicarbonate 22-28"],
         ["Serum calcium / uric acid", "Calcium 8.5-10.5 mg/dL; uric acid — men 3.5-7.2, women 2.6-6.0 mg/dL"],
         ["Total bilirubin", "__0.3-1.2 mg/dL__ (jaundice becomes visible above 2-3 mg/dL)"],
         ["Liver enzymes", "SGPT/ALT 7-45 U/L; SGOT/AST 8-40 U/L; alkaline phosphatase 40-130 U/L"],
         ["Serum protein / albumin", "Total protein 6-8 g/dL; albumin 3.5-5.5 g/dL"],
         ["Total cholesterol / LDL / HDL / triglycerides", "Under 200 / under 100 / above 40-50 / under 150 mg/dL"],
         ["Prothrombin time / INR", "PT 11-13.5 s; INR 0.8-1.2 (__therapeutic on warfarin 2-3__)"],
         ["Cerebrospinal fluid", "Clear, pressure 60-150 mm water, protein 15-45 mg/dL, glucose 50-80 (two-thirds of blood), 0-5 lymphocytes/mm3"],
         ["Blood volume / cardiac output", "About 5-6 L (70-80 mL/kg); cardiac output 4-6 L/min"]],
        caption="Table 13.3  Common normal laboratory values")

    b.section_h("13.4", "Fluid Balance, Dehydration and Oedema")
    b.table(
        ["Degree of dehydration", "Signs", "Fluid deficit"],
        [["__No dehydration__", "Alert, normal eyes, drinks normally, skin pinch retracts at once", "Under 3% of body weight"],
         ["__Some (mild-moderate) dehydration__", "Restless or irritable, __sunken eyes, thirsty and drinks eagerly, skin pinch retracts slowly, dry mouth, reduced urine__, sunken fontanelle in infants",
          "__3-9%__ (about 5%)"],
         ["__Severe dehydration__", "__Lethargic or unconscious, very sunken eyes, unable to drink, skin pinch retracts very slowly (over 2 s), weak/absent pulse, cold clammy extremities, low BP, no urine for 6-8 h, deep rapid breathing__",
          "__10% or more__ — needs immediate IV fluids (Ringer lactate)"]],
        caption="Table 13.4  Assessment of dehydration (WHO/IMNCI)")
    b.bullets([
        "__ORS (WHO low-osmolarity formula, per litre)__ — sodium chloride __2.6 g__, glucose (anhydrous) __13.5 g__, potassium chloride __1.5 g__, trisodium citrate dihydrate __2.9 g__; total osmolarity __245 mOsm/L__. Dissolve one packet in __1 litre of clean drinking water__, use within __24 hours__, and never add sugar, salt or milk to it.",
        "Give ORS __75 mL/kg over 4 hours__ for 'some dehydration'; after each loose stool give __50-100 mL (under 2 years), 100-200 mL (2-10 years)__ and as much as wanted above 10 years. Add __zinc 10 mg (under 6 months) or 20 mg (over 6 months) daily for 14 days__ in childhood diarrhoea, and continue feeding and breast feeding.",
        "__Homemade ORS__ — 1 litre of clean water + __1 level teaspoon of salt + 6 level teaspoons of sugar__ (or salt-and-sugar solution); rice kanji/lemon water are useful fluids.",
        "__Oedema__ — abnormal collection of fluid in the tissue spaces: __pitting__ (heart failure, renal disease, hypoproteinaemia, pregnancy) or __non-pitting__ (myxoedema, lymphoedema/filariasis); __dependent__ (feet when sitting, sacrum when lying), __periorbital__ (renal, early morning), __ascites__ (abdomen), __anasarca__ (generalised), __pulmonary oedema__ (breathlessness, pink frothy sputum, crepitations — an emergency).",
        "Nursing care in oedema: daily __weight at the same time__, strict intake-output, __salt and fluid restriction__ as ordered, elevation of the limbs, careful skin care (oedematous skin breaks down easily), measuring the abdominal girth at a marked level, watching for breathlessness, and monitoring electrolytes with diuretic therapy.",
        "__Fluid overload__ — raised JVP, puffy face, breathlessness, crepitations, bounding pulse, rapid weight gain: stop or slow the infusion, sit the patient up, give oxygen and inform the doctor.",
    ])

    b.section_h("13.5", "Observation of Pain")
    b.bullets([
        "Pain is the __'fifth vital sign'__ and is __whatever the patient says it is__ — believe the patient's report.",
        "Assess by __PQRST__: ~Provoking/Palliating factors, Quality (burning, cramping, stabbing, dull), Region and Radiation, Severity, Timing and duration~ (or __SOCRATES__).",
        "__Scales__ — numerical rating (0-10), visual analogue, __Wong-Baker FACES scale (for children 3 years and older)__, FLACC and __neonatal/infant scales (NIPS, CRIES)__ for those who cannot speak; behavioural signs in the non-verbal patient are grimacing, guarding, restlessness, moaning, rigidity, refusal to move, tachycardia, sweating and raised BP.",
        "__Types__ — acute vs chronic; somatic, visceral (deep, poorly localised, with nausea and sweating), __referred__ (gall bladder → right shoulder tip, myocardial infarction → left arm and jaw, appendix → umbilicus then right iliac fossa, diaphragm → shoulder), neuropathic (burning, shooting — diabetes, shingles), phantom limb pain.",
        "__Management__ — the __WHO analgesic ladder__ (step 1 paracetamol/NSAID, step 2 weak opioid ± adjuvant, step 3 strong opioid such as morphine) with drugs given __'by the clock, by the mouth, by the ladder'__; plus non-drug measures — position, rest, splinting, heat/cold, massage, distraction, relaxation, music, TENS, and reassurance.",
        "Always record the pain score __before and 30-60 minutes after__ giving an analgesic, and watch for constipation, sedation and __respiratory depression (respiration under 10-12/min — hold the drug and inform the doctor; antidote naloxone)__ with opioids.",
    ])

    b.section_h("13.6", "Danger Signals — When to Send for the Doctor at Once")
    b.box("caution", [
        "* __Airway/breathing:__ noisy breathing, stridor, choking, severe breathlessness, respiration under 10 or over 30/min, SpO2 under 90%, cyanosis, gasping, apnoea.",
        "* __Circulation:__ systolic BP under 90 mmHg or a fall of over 40 mmHg, pulse under 50 or over 130, thready or absent pulse, chest pain, cold clammy skin, any active bleeding (haematemesis, malaena, haemoptysis, post-partum haemorrhage, bleeding through a dressing).",
        "* __Neurological:__ sudden fall in the level of consciousness (a drop of 2 or more in the GCS), convulsion, sudden severe headache with vomiting, unequal or fixed pupils, sudden weakness of one side, severe confusion or delirium.",
        "* __Others:__ temperature above 40 °C or below 35 °C, no urine for 6-8 hours (under 30 mL/h), persistent vomiting, sudden severe abdominal pain with a rigid abdomen, a reaction during transfusion or injection, a new rash with fever, wound dehiscence, a fall or an injury, and any sudden unexplained change in the patient's condition or 'a feeling that something is wrong'.",
        "__Never wait for the routine round to report a danger signal.__ Stay with the patient, start the appropriate emergency measure (position, oxygen, pressure on a bleeding point), and send someone else for help.",
    ])

    b.section_h("13.7", "Recording and Reporting Observations")
    b.bullets([
        "Record __immediately__ at the bedside or as soon as possible; never record in advance, and never record an observation you have not made.",
        "Use __objective, descriptive language__ with __measurements, not impressions__: write 'drainage 30 mL, thick, yellow, offensive' rather than 'wound looks bad'; write 'passed 150 mL of dark concentrated urine at 10 a.m.' rather than 'urine output poor'.",
        "Use the __SBAR__ format when reporting to a doctor: ~Situation (who and what is wrong), Background (relevant history), Assessment (vital signs and your judgement), Recommendation (what you want done)~.",
        "Every entry must have the __date, time, signature, name and designation__; corrections by a single line with 'error' and initials; use only approved abbreviations.",
        "__Hand-over (change of shift) report__ — identification, diagnosis, current condition and vital signs, treatments due, investigations pending, special observations required, and any patient or family concern.",
        "Document __patient teaching, refusals, incidents and the notification of the doctor__ (with the time and the instruction received) — these are the entries most often examined in a legal enquiry.",
    ])

    b.box("recap", [
        "* Label the container, send at once, record and follow up; use standard precautions for all specimens.",
        "* Mid-stream urine for culture in a sterile container; sputum = early morning deep cough, 2 samples for TB; blood culture before antibiotics at the fever spike; 24-h urine — discard the first voiding, keep the last.",
        "* Benedict's test: blue = nil, green +, yellow ++, orange +++, brick red ++++ (8 drops of urine in 5 mL reagent).",
        "* Fasting sugar 70-100 mg/dL; Hb men 13-17, women 12-15; platelets 1.5-4.5 lakh; potassium 3.5-5.0 mEq/L; creatinine 0.6-1.2 mg/dL; INR on warfarin 2-3.",
        "* ORS (low osmolarity, 245 mOsm/L): NaCl 2.6 g, glucose 13.5 g, KCl 1.5 g, trisodium citrate 2.9 g per litre; use within 24 h; zinc for 14 days in child diarrhoea.",
        "* Severe dehydration (10%+): unconscious, unable to drink, skin pinch over 2 s, no urine — give IV Ringer lactate.",
        "* Pain is the fifth vital sign; assess with PQRST and the 0-10 or FACES scale; WHO ladder 'by the clock, by the mouth, by the ladder'.",
        "* Report using SBAR; 'if it is not recorded, it is not done'.",
    ])
