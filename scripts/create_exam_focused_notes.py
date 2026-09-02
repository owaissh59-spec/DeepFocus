#!/usr/bin/env python3
"""
Exam-focused supplementary notes for the syllabus unit:
  "Preparation of Patient for Operation, Pre & Post Operative Patient Care"

Trimmed version: content is organised in the EXACT order of the syllabus
sub-points, and anything that does not map to a listed sub-point has been cut.
"""

from notes_template import *   # noqa: F401,F403

title("SUPPLEMENTARY NOTES \u2014 EXAM-FOCUSED",
      "Preparation of Patient for Operation \u2022 Pre & Post Operative Patient Care",
      "Only the gaps in the studied PDF (Ch. 1 Perioperative Care of the Patient \u2022 "
      "Ch. 2 Protection of the Patient in Surgery \u2022 Ch. 3 Safety Measures for OR Personnel), "
      "arranged in syllabus order")

alert("SCOPE RULE USED FOR THIS DOCUMENT",
      ["**Sections are numbered to match your syllabus sub-points exactly**, so you can tick them off "
       "one by one.",
       "**Kept:** every gap that sits under a listed sub-point \u2014 admission procedure, transfer/position, "
       "environmental controls, electrosurgery, operative records, counting, **sterilization**, emergencies & "
       "disasters, in-service education, body mechanics, fatigue, radiation safety, infection control, "
       "chemical hazards, plus **post-operative care** (named in the unit heading).",
       "**Cut as off-syllabus:** ASA/Mallampati and cardiac-risk scoring, the routine-investigation list, "
       "premedication pharmacology, peri-operative anticoagulant/herbal management, ERAS, "
       "post-operative fluid and nutrition regimens, analgesic pharmacology in depth, discharge medication "
       "reconciliation, laser classes, local-anaesthetic toxicity, and the single-use-device reuse debate. "
       "These belong to anaesthesia, clinical-pharmacy or equipment units, not to this one.",
       "**Revise from the PDF, not from here:** psychological support (Ch. 1 is excellent), the record forms, "
       "the position figures, the 9 counting rules, orientation and fatigue text. This document only adds what "
       "those pages leave out."])

# ============================================================ 1
h1("1.  Pre-Operative Considerations \u2014 Psychological Support")
para("Your PDF covers this sub-point thoroughly. Only four things are missing, and all four are "
     "one-line answers.")
table(["Point", "Content"],
      [["Sources of pre-operative anxiety",
        "Fear of the **unknown**, of **death**, of **not waking from anaesthesia**, of **pain**, of "
        "**disfigurement/altered body image**, of **loss of control and dependence**; plus separation from family "
        "and financial worry"],
       ["Assessment tools",
        "**STAI** (State\u2013Trait Anxiety Inventory) \u2022 **APAIS** (Amsterdam Preoperative Anxiety and "
        "Information Scale) \u2022 Visual Analogue Anxiety Scale \u2022 **m-YPAS** for children"],
       ["Peak anxiety",
        "**Immediately before transfer to the OR** (also on being told surgery is needed, and the night before)"],
       ["Effects of unrelieved anxiety",
        "\u2191 catecholamines \u2192 tachycardia, hypertension, arrhythmia \u2022 \u2191 anaesthetic requirement "
        "\u2022 **\u2191 post-operative pain scores and analgesic need** \u2022 \u2191 PONV \u2022 delayed wound "
        "healing \u2022 longer stay"],
       ["Most effective intervention",
        "**Structured pre-operative teaching/counselling.** Then relaxation and guided imagery, music, "
        "parental presence at induction in children, allowing spectacles/hearing aids/dentures to stay until "
        "induction"],
       ["Age-specific fears",
        "**1\u20133 y** separation \u2022 **3\u20136 y** mutilation \u2022 **school age** loss of control \u2022 "
        "**elderly** dependency and death (needs slower, repeated explanation)"]],
      widths=[4.0, 15.0])

# ============================================================ 2
h1("2.  Preparation of the Patient for Operation (Physical Preparation)")
para("The PDF reproduces the pre-operative checklist form but never explains the preparation itself.")
h2("2.1  Pre-operative fasting \u2014 remember 2 \u2013 4 \u2013 6 \u2013 8")
table(["Ingested material", "Minimum fast"],
      [["Clear liquids (water, pulp-free juice, black tea/coffee)", "**2 hours**"],
       ["Breast milk", "**4 hours**"],
       ["Infant formula, non-human milk, light meal", "**6 hours**"],
       ["Fried/fatty food, meat, full meal", "**8 hours**"]],
      widths=[7.0, 4.0])
clinical("WHY \u2014 and when the rule does not apply",
         ["Purpose = prevent **pulmonary aspiration of gastric contents (Mendelson's syndrome)** at induction, when "
          "airway reflexes are abolished. Risk rises when gastric volume is **> 25 mL (0.4 mL/kg)** and "
          "**pH < 2.5**.",
          "**Treat as a full stomach regardless of fasting time:** emergency and trauma, pregnancy, obesity, "
          "diabetic gastroparesis, bowel obstruction, severe GERD, opioids \u2192 **rapid sequence induction with "
          "cricoid pressure (Sellick's manoeuvre)** and acid prophylaxis.",
          "**Prolonged \u2018midnight\u2019 fasting is harmful** (dehydration, hypoglycaemia, insulin resistance) "
          "and does **not** reduce gastric volume."])
h2("2.2  Skin preparation and hair removal \u2014 evidence the PDF predates")
table(["Question", "Answer"],
      [["Should hair be removed?", "**No** \u2014 not unless it physically interferes with the procedure or closure"],
       ["If it must be removed?", "**Electric clippers with a single-use head**, or depilatory cream. "
                                  "**Razors are contraindicated** (micro-abrasions become colonised)"],
       ["When?", "**Immediately before surgery, outside the OR.** SSI risk: no removal \u2248 clipping < shaving "
                 "immediately before < **shaving the night before (highest)**"],
       ["Best antiseptic", "**Alcohol-based 2 % chlorhexidine gluconate** > aqueous povidone-iodine. "
                           "Povidone-iodine 10 % = 1 % available iodine and **needs 2\u20133 min contact and must dry**"],
       ["Alcohol + ESU", "Prep must **dry completely (\u2265 3 min) and must never pool** \u2014 pooled alcohol is "
                         "the classic **fuel** in OR fires (\u00a710)"],
       ["Direction", "From the **incision outward** in concentric strokes; the sponge is **never returned to the "
                     "centre**; the dirtiest area (stoma, sinus, perineum, umbilicus, axilla) is prepped **last**"],
       ["Extent", "Wide enough to allow **extension of the incision, new incisions and drain sites** without "
                  "re-prepping"],
       ["Contraindications", "Chlorhexidine \u2014 **middle ear (ototoxic), eye (keratitis), neural tissue**; "
                            "iodophors \u2014 neonates, iodine allergy"]],
      widths=[3.6, 15.4])
h2("2.3  Immediate pre-transfer preparation")
bullets([
    "Patient **voids** immediately before transfer; catheterise only if indicated, and **remove within 24 h** "
    "(CAUTI prevention).",
    "**Remove and document the disposition of:** dentures/bridges, contact lenses, jewellery (tape a wedding ring "
    "if it cannot be removed), **nail polish and artificial nails** (interfere with pulse oximetry and harbour "
    "organisms), hairpins, prostheses, valuables \u2014 exactly what Form 1-1 records.",
    "**Antibiotic prophylaxis: single IV dose within 60 minutes of skin incision** (120 min for vancomycin); "
    "re-dose if surgery exceeds 2 half-lives or blood loss > 1500 mL; **stop within 24 h**. For tourniquet surgery "
    "the infusion must finish **before inflation**.",
    "**Site marked** by the operating surgeon with an indelible marker, with the awake patient participating "
    "(\u00a73).",
    "Confirm **consent, allergies, fasting status, prostheses/implants, blood availability** and that imaging and "
    "old records are in the OR.",
])

# ============================================================ 3
h1("3.  Admission Procedure & Patient Identification")
para("The PDF teaches the Joint Commission Universal Protocol in full. The **WHO Surgical Safety Checklist** is "
     "absent, and it is the internationally examined instrument.")
h2("3.1  WHO Surgical Safety Checklist (2008) \u2014 3 phases, 19 items")
table(["Phase", "When", "Core content"],
      [["**1. SIGN IN**", "Before induction of anaesthesia",
        "Patient confirms **identity, site, procedure, consent** \u2022 site marked \u2022 anaesthesia safety check "
        "\u2022 **pulse oximeter on and working** \u2022 known allergy \u2022 difficult airway / aspiration risk "
        "\u2022 risk of blood loss > 500 mL (7 mL/kg in children) \u2192 access and fluids planned"],
       ["**2. TIME OUT**", "After induction, **before skin incision**",
        "All members **state name and role** \u2022 surgeon, anaesthetist and nurse verbally confirm patient, site, "
        "procedure \u2022 **anticipated critical events** (critical steps, duration, blood loss; anaesthetic "
        "concerns; sterility indicator and equipment issues) \u2022 **antibiotic given in the last 60 min?** \u2022 "
        "imaging displayed \u2022 VTE prophylaxis \u2022 correct position"],
       ["**3. SIGN OUT**", "Before the patient leaves the OR",
        "**Name of the procedure recorded** \u2022 **instrument, sponge and needle counts correct** \u2022 "
        "**specimens labelled and read aloud** \u2022 equipment problems \u2022 **key concerns for recovery**"]],
      widths=[2.4, 4.0, 12.6])
highyield("DISTINGUISH THESE THREE \u2014 favourite MCQ",
          ["**Universal Protocol (JC, July 2004)** = pre-procedure **verification** + **site marking** + "
           "**\u2018time out\u2019** immediately before starting. Aim: prevent wrong-site, wrong-procedure, "
           "wrong-person surgery.",
           "**AORN (March 2005)** added confirmation of the **correct patient position** to the time out.",
           "**WHO Checklist (2008)** = the **3-phase, 19-item** tool; broader \u2014 it also covers airway, blood "
           "loss, antibiotics, imaging, counts and specimen labelling. It cut mortality from 1.5 % to 0.8 %.",
           "**Site marking:** by the **operating surgeon**, **indelible marker**, at/near the incision, "
           "**with the awake patient participating**, **before** entering the OR; mark **laterality and level**; "
           "never mark the non-operative side.",
           "**At least two identifiers**, and the patient **states** their own name \u2014 never "
           "\u201cAre you Mary Jones?\u201d"])

# ============================================================ 4
h1("4.  Transfer Procedure & Position")
h2("4.1  Safe transfer \u2014 the numbers")
bullets([
    "Minimum **two persons**; **\u2265 4 or a mechanical lifter** for an anaesthetised, obese or unstable patient; "
    "**one person on each side** of the table; **lock the wheels** of gurney and table.",
    "Devices that reduce the load: **roller board (Davis), slide sheet, Hoyer pad, air-assisted transfer mattress**.",
    "**NIOSH maximum recommended lift = 51 lb (23 kg)**; for **patient handling the limit is 35 lb (16 kg)** "
    "\u2014 above that, use an aid or a lift team. **Back injury is the commonest occupational injury in health "
    "care.**",
    "**Safety strap across the mid-thighs, \u2248 3 inches (7.5 cm) above the knees** \u2014 the single most "
    "important measure against a fall; two fingers should slide under it.",
    "Protect during transfer: **airway/ET tube, IV, arterial and CVP lines, epidural, Foley, drains** \u2014 and "
    "the **fingers** when table sections are raised.",
    "**Never move an anaesthetised patient without the anaesthetist's permission and direction.** The anaesthetist "
    "guards head/airway/neck, the surgeon protects fractures, the circulator applies padding and the strap.",
])
h2("4.2  Position-specific complications \u2014 the nerve-injury map")
para("The PDF describes each position well but omits the complications, which is what gets asked.")
table(["Position", "Nerve / structure at risk", "Prevention", "Physiological effect"],
      [["**Supine**", "**Ulnar nerve \u2014 commonest peri-operative nerve injury**; brachial plexus; radial n.; "
                      "occiput, sacrum, heels",
        "Arms abducted **\u2264 90\u00b0**, **palms up (supinated)**, elbows padded, legs uncrossed",
        "\u2193 FRC; aorto-caval compression in late pregnancy"],
       ["**Trendelenburg**", "Brachial plexus (shoulder braces), retinal/cerebral congestion, sliding",
        "Braces over the **acromio-clavicular area, never on the soft neck**; limit to 30\u201345\u00b0 and to the "
        "shortest time",
        "**\u2191 venous return, \u2191 ICP, \u2191 IOP, \u2191 CVP; \u2193 FRC and compliance \u2192 atelectasis**; "
        "facial/laryngeal oedema; tube migration; regurgitation"],
       ["**Reverse Trendelenburg / sitting**", "Sciatic stretch, foot drop, venous pooling; **venous air embolism** "
                                               "in the sitting position",
        "Padded footboard, antiembolism stockings + compression device, slow position change",
        "**\u2193 venous return \u2192 hypotension; \u2193 cerebral perfusion**"],
       ["**Lithotomy**", "**Common peroneal nerve \u2014 commonest here \u2192 foot drop**; femoral, obturator, "
                         "saphenous, sciatic; **lower-limb compartment syndrome**",
        "Pad the **fibular head** away from the post; **raise and lower both legs together, slowly, by two people**; "
        "avoid extreme abduction; **limit time (risk rises beyond 2\u20134 h)**",
        "On **lowering the legs \u2192 sudden \u2193 venous return \u2192 hypotension**; \u2193 FRC"],
       ["**Prone**", "Brachial plexus, ulnar; **eye \u2192 corneal abrasion and post-operative visual loss (POVL) "
                     "from ischaemic optic neuropathy**; breasts, genitalia, iliac crests",
        "**Chest rolls from clavicle to iliac crest**; head on a padded donut/horseshoe with the **eyes free of all "
        "pressure**; neutral neck; re-check the ET tube after turning",
        "\u2191 abdominal and epidural venous pressure \u2192 bleeding; \u2193 cardiac index"],
       ["**Lateral (kidney / thoracotomy)**", "Dependent brachial plexus and axillary vessels, dependent common "
                                              "peroneal and ear",
        "**Axillary roll caudal to the axilla \u2014 never in it**; pillow between the legs; head in line with the "
        "spine",
        "**V/Q mismatch \u2014 dependent lung better perfused but less ventilated**; kidney rest \u2193 venous return"],
       ["**Jackknife / Kraske (a PRONE modification)**", "Face, eyes, genitalia, knees",
        "Padding at hips, pillow under pelvis and shins", "Marked \u2193 venous return and \u2193 FRC"],
       ["**Fracture table**", "**Perineal post \u2192 pudendal nerve injury**, perineal pressure necrosis",
        "Well-padded post, minimum effective traction, protect the well leg; **no skin\u2013metal contact** (ESU "
        "burn)", "Blood loss; fat-embolism risk"]],
      widths=[2.8, 4.0, 6.0, 6.2])
mnemonic("POSITIONING \u2014 GOLDEN RULES",
         ["Position is determined by the **surgical approach + patient's condition + anaesthetic technique + "
          "surgeon's preference**. Positioning aids must be **in the room before the patient arrives**.",
          "**PADDING** \u2014 **P**ressure points padded, **A**lignment maintained, **D**ignity/exposure minimised, "
          "**D**evices ready beforehand, **I**V lines protected, **N**erves free of stretch and compression, "
          "**G**entle simultaneous movement.",
          "Modifications of **supine**: Trendelenburg, reverse Trendelenburg, Fowler's/sitting, lithotomy. "
          "Modification of **prone**: Kraske/jackknife.",
          "**Compartment syndrome after lithotomy** = pain out of proportion, tense swollen calf, paraesthesia "
          "\u2192 **fasciotomy**. Always examine and document limb movement and paraesthesia on arrival in PACU."])

# ============================================================ 5
h1("5.  Environmental Controls")
h2("5.1  Operating room design \u2014 the numbers the PDF omits")
table(["Parameter", "Standard", "Exam point"],
      [["Temperature", "**20\u201323 \u00b0C (68\u201375 \u00b0F)**", "Team comfort vs **patient hypothermia**; "
                                                                     "raise for neonates and burns"],
       ["Relative humidity", "**20\u201360 %** (classically 30\u201360 %)",
        "**Too low \u2192 static spark risk; too high \u2192 microbial growth and condensation**"],
       ["Air changes per hour", "Minimum **15**, recommended **20\u201325** (\u2265 3 outdoor air)",
        "Dilutes contaminants and waste anaesthetic gas"],
       ["Air pressure", "**POSITIVE** relative to corridors",
        "Air flows **out** of the OR. Contrast: **TB isolation = NEGATIVE pressure**"],
       ["Airflow", "Unidirectional **downward** over the table, exhaust at floor level",
        "Keeps a clean air column over the sterile field"],
       ["**HEPA filter**", "**\u2265 99.97 % of particles \u2265 0.3 \u00b5m**",
        "The single most asked number. **ULPA = 99.999 % at 0.1 \u00b5m** (smoke evacuators)"],
       ["Laminar / ultraclean flow", "**300\u2013600 air changes/h**", "Used for **joint arthroplasty and implant "
                                                                      "surgery**"],
       ["Noise", "< 45 dB recommended", "Silence is mandatory during **induction** \u2014 **hearing is the last "
                                        "sense to be lost**"]],
      widths=[3.2, 5.0, 10.8])
h2("5.2  Zoning of the OT complex")
table(["Zone", "Also called", "Areas", "Attire"],
      [["**Protective / outer**", "Unrestricted", "Reception, changing rooms, offices, pre-op holding, PACU",
        "Street clothes permitted"],
       ["**Clean**", "Semi-restricted", "Peripheral corridors, storage, utility, instrument processing",
        "**Scrub attire + head cover**; mask not required"],
       ["**Sterile / aseptic**", "Restricted", "Operating room, scrub area, sterile store",
        "Scrub attire + head cover + **mask**; sterile gown and gloves in the field"],
       ["**Disposal / dirty**", "Dirty corridor", "Dirty utility, sluice, disposal corridor", "Scrub attire + PPE"]],
      widths=[3.2, 2.8, 8.0, 5.0])
h2("5.3  Cleaning \u2014 and why fumigation is obsolete")
bullets([
    "**Between cases:** all horizontal surfaces, the table, positioning devices, lights, ESU, suction and the floor "
    "**within 1\u20131.5 m of the field** are wiped with a hospital germicide. The PDF's key point: **every case is "
    "cleaned identically** \u2014 special \u2018ritual\u2019 cleaning after \u2018dirty\u2019 cases is **obsolete**, "
    "because all cases are treated as potentially infectious.",
    "**Terminal (daily) clean:** whole room, walls, ceiling, equipment wheels, scrub sinks, corridors, storage; "
    "wet-vacuum the floor.",
    "**Formaldehyde fumigation is no longer recommended** \u2014 Group 1 carcinogen, mucosal irritant, needs the "
    "room sealed and idle 24\u201348 h, and penetrates crevices unreliably. Modern no-touch options: "
    "**vaporised hydrogen peroxide, chlorine dioxide, UV-C** \u2014 always **after** physical cleaning, never "
    "instead of it.",
    "**Routine environmental culturing is not recommended** \u2014 only for outbreak investigation or after "
    "construction.",
    "**Blood spill:** absorb, then disinfect with **1 % sodium hypochlorite (10 000 ppm)** for 10 min.",
])
h2("5.4  Levels of disinfection (needed for \u00a79 as well)")
table(["Level", "Kills", "Agents", "Use"],
      [["**Sterilization**", "**All microbes including spores**",
        "Steam, EO, H\u2082O\u2082 plasma, glutaraldehyde 10 h, peracetic acid, radiation", "**Critical** items"],
       ["**High-level (HLD)**", "All except large numbers of spores",
        "Glutaraldehyde 2 %, **OPA 0.55 % (12 min)**, H\u2082O\u2082 7.5 % (30 min), peracetic acid",
        "**Semi-critical** \u2014 endoscopes, laryngoscope blades, respiratory equipment"],
       ["**Intermediate**", "Vegetative bacteria, **M. tuberculosis**, most viruses/fungi; **not spores**",
        "Alcohols 60\u201390 %, hypochlorite, iodophors, phenolics", "Soiled non-critical surfaces"],
       ["**Low**", "Most vegetative bacteria; **not TB, not spores**", "Quaternary ammonium compounds",
        "**Non-critical** \u2014 floors, walls, BP cuffs, furniture"]],
      widths=[2.6, 5.0, 6.4, 5.0])
para("**Key agent facts:** **alcohol** \u2014 fastest kill, **no residual action, not sporicidal, inactivated by "
     "organic matter, flammable**. **Chlorhexidine** \u2014 **persistent residual activity, not inactivated by "
     "blood**, but **ototoxic and corneal-toxic**. **Povidone-iodine** \u2014 broad but **inactivated by blood/pus** "
     "and needs contact time to release free iodine. **Hypochlorite** \u2014 broad including spores, but "
     "**corrosive** and **never mixed with acids or ammonia (chlorine gas)**. **Quaternary ammonium compounds** "
     "\u2014 inactivated by soap, hard water and gauze.")
h2("5.5  Aseptic technique and the sterile field \u2014 hard rules")
numbered([
    "Only **sterile items** are used in a sterile field.",
    "The gown is sterile **in front from chest to the level of the field**, and the sleeves from **5 cm above the "
    "elbow to the cuff**. The **back is never sterile**.",
    "A **draped table is sterile only at table-top level** \u2014 anything below the edge is unsterile and is "
    "**never brought back up**.",
    "Sterile persons keep hands **at or above waist level, in front of the body**, and pass **back-to-back** or "
    "**face-to-face**.",
    "Unsterile persons stay **\u2265 30 cm (1 ft)** away, never reach over the field, and always **face** it.",
    "The **edge of any wrapper, package or basin is unsterile** \u2014 conventionally a **2.5 cm (1 inch)** margin.",
    "**Moisture contaminates by capillary action (strike-through)** \u2014 a wet field is a contaminated field.",
    "Packages are opened **farthest corner first, nearest corner last**, held away from the body, so you never "
    "reach over the contents.",
    "Sterile items stay **in view**; anything of **doubtful sterility is unsterile** (\u2018when in doubt, throw it "
    "out\u2019).",
])
h2("5.6  Surgical hand antisepsis")
table(["Item", "Standard"],
      [["Agents", "**4 % chlorhexidine gluconate** or **7.5 % povidone-iodine**, or an alcohol-based surgical hand "
                  "rub (WHO now prefers the rub)"],
       ["Duration", "**First scrub of the day 3\u20135 minutes**; older counted-brush-stroke method = 30 strokes to "
                    "nails, 20 per surface"],
       ["Sequence", "**Nails \u2192 fingers and interdigital spaces \u2192 hands \u2192 wrists \u2192 forearms to "
                    "5 cm above the elbow**; the **cleanest part (hand) is held highest**; rinse fingertips to "
                    "elbow; **never return to a cleaned area**"],
       ["Before scrubbing", "Remove rings, watches, bracelets; nails short and clean, **no polish, gel or artificial "
                            "nails** (AORN \u2014 they harbour Gram-negatives and fungi); **do not scrub with cuts, "
                            "abrasions or dermatitis**"],
       ["After scrubbing", "Hands **above the elbows, in front of the body, above waist and below shoulder level**; "
                           "dry with a sterile towel from fingers to elbow, never back"],
       ["WHO 5 Moments", "**1** before touching a patient \u2022 **2** before a clean/aseptic procedure \u2022 "
                         "**3** after body-fluid exposure risk \u2022 **4** after touching a patient \u2022 "
                         "**5** after touching patient surroundings"],
       ["Rub vs soap", "Alcohol rub routinely; **soap and water is mandatory for visibly soiled hands and for "
                       "Clostridioides difficile** (alcohol is not sporicidal)"],
       ["Double gloving", "Reduces inner-glove perforation by **\u2248 70\u201380 %**; change every "
                          "90\u2013150 min and between patients"]],
      widths=[3.2, 15.8])
h2("5.7  Surgical site infection \u2014 classification")
table(["Wound class", "Definition", "Example", "SSI risk"],
      [["**I \u2013 Clean**", "No inflammation; respiratory/GI/GU tract **not entered**; closed primarily",
        "Thyroidectomy, hernia repair, joint replacement", "**< 2 %**"],
       ["**II \u2013 Clean-contaminated**", "Tract entered under **controlled conditions**, no unusual contamination",
        "Elective cholecystectomy, elective bowel resection, hysterectomy", "**3\u201310 %**"],
       ["**III \u2013 Contaminated**", "Fresh accidental wound; **major break in technique**; gross GI spillage; "
                                       "acute non-purulent inflammation",
        "Fresh trauma, enterotomy with spillage", "**15\u201320 %**"],
       ["**IV \u2013 Dirty / infected**", "Old wound with devitalised tissue; existing infection or **perforated "
                                          "viscus**", "Faecal peritonitis, perforated appendix", "**30\u201340 %**"]],
      widths=[3.4, 6.4, 6.2, 3.0])
bullets([
    "**CDC depth classification:** **superficial incisional** (skin/subcutaneous, within **30 days**); "
    "**deep incisional** (fascia/muscle, within **30 days, or 90 days if an implant** is present); "
    "**organ/space**.",
    "Commonest organism = **Staphylococcus aureus**; commonest **source of contamination = the patient's own "
    "endogenous flora**.",
    "**Proven SSI-prevention bundle:** CHG-alcohol prep, no razor shaving, antibiotic within 60 min, "
    "**normothermia > 36 \u00b0C**, **glucose < 180 mg/dL**, adequate tissue oxygenation, minimal traffic, "
    "good haemostasis and no dead space.",
])



# ============================================================ 6
h1("6.  Electro Surgery")
para("The PDF gives 5 precautions. The mechanism and the injury mechanisms are what carry the marks.")
h2("6.1  Fundamentals")
table(["Concept", "Detail"],
      [["Principle", "**High-frequency alternating current** concentrated at a small active electrode; tissue "
                     "resistance converts it to heat \u2192 **cutting, coagulation or desiccation**. It is **not "
                     "cautery** (true cautery = a passively heated wire, no current through the patient)"],
       ["Frequency", "**300 kHz \u2013 3 MHz (radiofrequency)**. Above **~100 kHz** the current **does not stimulate "
                     "nerve or muscle (the Faradic effect is avoided)** \u2014 which is why RF current cuts but does "
                     "not electrocute"],
       ["**Cut** waveform", "**Continuous, low-voltage, high-current** (100 % duty cycle) \u2192 vaporisation, little "
                            "haemostasis"],
       ["**Coag** waveform", "**Interrupted, high-voltage, low duty cycle (~6 %)** \u2192 coagulum. High voltage "
                             "\u2192 **greater risk of capacitive coupling, insulation breakdown and sparking**"],
       ["**Monopolar** circuit", "Generator \u2192 **active electrode (pencil)** \u2192 patient \u2192 "
                                 "**dispersive/return pad** \u2192 generator. Current crosses the whole body; "
                                 "**the pad is essential**"],
       ["**Bipolar** circuit", "Both electrodes are the **two tines of the forceps**; current passes only between "
                               "them. **No pad needed**, minimal lateral spread, usable in fluid, **safest with "
                               "pacemakers** \u2014 neurosurgery, ophthalmic, microsurgery"],
       ["Pad placement", "**Clean, dry, hair-free, well-vascularised muscle mass**, **as close as practicable to the "
                         "site**, whole surface in uniform contact, **away from ECG electrodes**, bony prominences, "
                         "scar, tattoos, metal implants and pooled fluid"],
       ["**REM / contact-quality monitoring**", "A **split pad** whose two halves are monitored for impedance; the "
                                                "generator **shuts down if contact becomes inadequate** \u2014 has "
                                                "virtually eliminated pad-site burns. Modern generators are "
                                                "**isolated**, not ground-referenced"],
       ["**AEM (active-electrode monitoring)**", "Shielded laparoscopic instruments that drain stray current "
                                                 "\u2014 prevents insulation-failure and capacitive-coupling burns"]],
      widths=[3.8, 15.2])
h2("6.2  The five mechanisms of electrosurgical injury")
numbered([
    "**Return-electrode (pad-site) burn** \u2014 poor or partial pad contact, hair, dried gel, pad over bone or "
    "scar. Prevented by correct placement + REM.",
    "**Alternate-site burn** \u2014 the patient's skin touches a **metal surface** (table edge, stirrup, armboard "
    "screw) which becomes an unintended return path. The PDF states this rule twice: **no skin-to-metal contact**.",
    "**Direct coupling** \u2014 the activated electrode touches another metal instrument (laparoscope, retractor), "
    "which burns adjacent tissue.",
    "**Capacitive coupling** \u2014 current crosses **intact insulation** by an electrostatic field; classic setting "
    "= a **metal instrument through a plastic (hybrid) trocar**, or coiled cords. Worse with **coag mode and long "
    "thin instruments**.",
    "**Insulation failure** \u2014 a pin-hole break delivers current **outside the surgeon's view** \u2192 "
    "**delayed bowel perforation 3\u201310 days post-operatively**. Inspect insulation before every use.",
])
h2("6.3  Other examination points")
bullets([
    "**Repeated requests to increase the power** = poor pad contact, a loose connection, a frayed cord or a failing "
    "generator. **Stop, check the circuit and pad; do not simply turn it up.** Replace and label the unit and "
    "**document the serial numbers and the reason**.",
    "**Keep the pencil in its holster** when not in use; clean eschar with a non-abrasive pad.",
    "**Pacemaker / ICD:** prefer **bipolar**; if monopolar is essential use short bursts at low power with the "
    "current path away from the device, keep the **crash cart with defibrillator immediately available and document "
    "that it is there**, monitor ECG and pulse continuously, and **interrogate the device afterwards**.",
    "**Never use ESU or laser in an oxygen-enriched field** (mouth, oropharynx, tracheostomy, under drapes with "
    "high-flow O\u2082) \u2014 pause the oxygen and allow washout.",
    "**Advanced devices in one line each:** **ultrasonic (Harmonic) scalpel** \u2014 mechanical vibration at "
    "**55.5 kHz**, cavitation at a **lower temperature (50\u2013100 \u00b0C)**, no current through the patient; "
    "**bipolar vessel sealing (LigaSure)** \u2014 seals vessels up to **7 mm**; **argon-enhanced** coagulation "
    "\u2014 thin uniform eschar, gas-embolism risk.",
    "**Surgical smoke (plume):** > 150 chemicals plus viable cells and viral DNA (**documented HPV transmission to "
    "surgeons**). **Ablating 1 g of tissue \u2248 3\u20136 unfiltered cigarettes.** Control = **smoke evacuator with "
    "an ULPA filter (99.999 % at 0.1 \u00b5m) held within 2.5\u20135 cm (1\u20132 in)** plus a **high-filtration "
    "mask or N95** \u2014 a standard mask is **not** adequate.",
])
highyield("EQUIPMENT NUMBERS THAT SHARE THIS SUB-TOPIC",
          ["**Pneumatic tourniquet:** cuff ends overlap **3\u20136 inches**; **never at or near the elbow**; "
           "**upper limb 250\u2013300 mmHg for \u2264 60 min**, **lower limb 300\u2013350 mmHg for \u2264 90\u2013120 "
           "min**; **deflate 10\u201315 min** if longer; exsanguinate with an Esmarch bandage **before** inflation; "
           "**record site, pressure and both inflation and deflation times**. On release: \u2193 BP, transient "
           "acidosis, \u2191 K\u207a, \u2191 EtCO\u2082.",
           "**Laser:** **wavelength-specific eye protection for everyone including the patient**; warning signs on "
           "doors, windows covered, key held by the laser safety officer, **standby mode when not firing, foot pedal "
           "only to the surgeon, matte instruments, wet drapes, saline available, plume evacuator, laser-safe ET tube "
           "with a saline-filled cuff, and never in an oxygen-enriched field.**",
           "**Powered saws/drills:** engineering clearance, test before use, attachments secure and sharp, "
           "**let the rotating part come to a complete standstill before setting it down**, face shield mandatory."])

# ============================================================ 7
h1("7.  Operative Records")
h2("7.1  Specimen handling \u2014 a favourite MCQ the PDF omits")
table(["Specimen", "Handling"],
      [["Routine histopathology", "**10 % neutral buffered formalin**, volume **\u2248 10\u00d7 the specimen**; "
                                  "container labelled with name, ID, date, site/side; **label read aloud during "
                                  "Sign Out**"],
       ["**Frozen section**", "**FRESH, in saline-moistened gauze \u2014 NEVER in formalin** (formalin prevents "
                              "further study and immunohistochemistry); send immediately"],
       ["Culture / microbiology", "**Sterile container, no fixative**; anaerobic transport for anaerobes; "
                                  "**never formalin**"],
       ["Stones/calculi", "Dry container, **no fixative**"],
       ["Implants", "Record **type, manufacturer, size, serial/lot number** in the intra-operative record and the "
                    "**implant log** (traceability for recalls)"],
       ["Lost specimen", "A **serious, irreplaceable incident** \u2014 incident report mandatory"]],
      widths=[3.6, 15.4])
h2("7.2  What makes the record legally sound")
bullets([
    "**JC-mandated minimum content:** surgeon's name and assistants, **pre-operative diagnosis**, procedure "
    "performed, **post-operative diagnosis**, findings, **specimens removed (type and number)**, estimated blood "
    "loss, and the names of all team members giving intra-operative care.",
    "Also document: the **time out**, the **counts and their outcome**, **skin condition before and after prep** and "
    "the solution used, position and positioning aids, **ESU pad site, serial number and settings**, tourniquet "
    "data, drains/catheters/packing, medications and irrigations (name, strength, dose, route, time, who gave them), "
    "implants, intake/output, transfusion checks, and any **unusual event with the actions taken**.",
    "**Rules:** contemporaneous, legible, factual and objective (no opinion or blame), signed and timed; "
    "**correct by a single line-through with initials, date and time \u2014 never erase, overwrite or use correction "
    "fluid**; leave no blank spaces; label late entries.",
    "**Incident (occurrence) report** for: incorrect count, medication error, burn, fall, retained item, equipment "
    "failure, needle-stick, lost specimen, unplanned re-operation and **death in the OR**.",
    "**Only what is documented is a legal fact** \u2014 the most quoted line in your PDF (pp. 8 and 48). An "
    "undocumented event \u2018did not happen\u2019 in court.",
])
h2("7.3  Consent \u2014 the parts the forms do not explain")
table(["Point", "Rule"],
      [["Five elements of valid consent", "**Disclosure \u2022 Capacity \u2022 Voluntariness \u2022 Comprehension "
                                          "\u2022 Documentation**"],
       ["Must be disclosed", "Diagnosis, nature and purpose of the procedure, risks and benefits, **alternatives "
                             "including doing nothing**, and consequences of refusal. **No guarantee of outcome may "
                             "be given**"],
       ["Timing", "**Before sedative premedication** \u2014 hence the wording on Form 1-2, \u201cI am not under the "
                  "influence of any preoperative or other sedating medication\u201d"],
       ["Age", "**18 years** in India (**IPC \u00a7\u00a7 87\u201388**). For a child **under 12** or a person of "
               "unsound mind, the guardian consents (**IPC \u00a7 89**)"],
       ["Emergency / unconscious", "**Doctrine of necessity \u2014 IPC \u00a7 92**: life-saving treatment in good "
                                   "faith without consent when the patient cannot consent and no representative is "
                                   "available"],
       ["Consent obtained by fear or misconception", "**Invalid \u2014 IPC \u00a7 90**"],
       ["Special consent needed for", "**Sterilization** (patient must state understanding of permanent, "
                                      "**irreversible** loss of fertility \u2014 Form 1-3), blood products, "
                                      "photography, implants, organ donation, HIV testing"],
       ["Who obtains vs who verifies", "The **operating surgeon obtains** it. The perioperative practitioner "
                                       "**verifies** that a valid, signed, dated consent exists and matches the "
                                       "procedure, site and side, and **reports any discrepancy**"],
       ["Withdrawal", "May be withdrawn at **any time** while the patient is competent"],
       ["Blood refusal", "Honour it, **document it on the checklist**, and plan cell-saver/tranexamic acid"]],
      widths=[4.4, 14.6])
highyield("MEDICO-LEGAL DOCTRINES \u2014 one-liners",
          ["**Negligence \u2014 the 4 D's:** **D**uty, **D**ereliction (breach of the standard of a reasonably "
           "competent practitioner \u2014 the **Bolam test**), **D**irect causation, **D**amage.",
           "**Res ipsa loquitur** (\u2018the thing speaks for itself\u2019) \u2014 negligence presumed; classic "
           "examples are a **retained sponge or instrument**, wrong-site surgery, and a diathermy burn.",
           "**Vicarious liability / respondeat superior** \u2014 the hospital is liable for its employees' acts.",
           "**Battery** = operating with **no** consent. **Negligence** = operating with **inadequately informed** "
           "consent."])

# ============================================================ 8
h1("8.  Counting Procedure")
para("Learn the 9 counting rules from the PDF. What it lacks is the terminology and epidemiology.")
bullets([
    "A retained item is a **\u2018never event\u2019 / sentinel event**. The **commonest retained item is a "
    "sponge/gauze (\u2248 50\u201370 %)**, then instruments and needles; commonest site = **abdomen/pelvis**.",
    "A retained gauze encased in a foreign-body granuloma = **gossypiboma (textiloma)** \u2014 presents weeks to "
    "years later with a mass, pain, sinus, abscess, obstruction or fistula, and is a classic **res ipsa loquitur** "
    "claim.",
    "**Risk factors:** emergency surgery, **unexpected intra-operative change of procedure**, high BMI, multiple "
    "teams or staff changes, and omitted or incorrect counts.",
    "**Counts are taken:** (1) **before the procedure (baseline)**, (2) when **items are added**, (3) **before "
    "closure of a cavity within a cavity** (uterus, bladder, bowel), (4) when **wound/fascial closure begins**, "
    "(5) at **skin closure**, and (6) at **any change of scrub or circulating personnel**.",
    "**The circulator records the count \u2014 that record is a legal responsibility.** Both persons count "
    "**aloud together** as the scrub person touches each item.",
    "All sponges used in a wound must be **radio-opaque (X-ray detectable)**; **X-ray-detectable sponges are never "
    "used as dressings**, and dressing sponges are never used in the wound. Adjuncts: **bar-coded counting and "
    "radiofrequency (RF) tag detection wands**.",
    "**If the count is incorrect:** repeat it \u2192 **inform the surgeon**, who explores the wound \u2192 if still "
    "missing, **intra-operative X-ray before the patient leaves the OR** \u2192 notify the OR supervisor \u2192 "
    "**document and file an incident report**. **Nothing (linen, trash, instruments, sponges) leaves the room until "
    "the final count is correct.**",
])

# ============================================================ 9
h1("9.  Sterilization  \u2014  highest-yield section in the unit")
h2("9.1  Definitions \u2014 get these exactly right")
table(["Term", "Definition"],
      [["**Sterilization**", "Destruction or removal of **all forms of microbial life, including bacterial and "
                             "fungal spores**. An **absolute** term"],
       ["**Disinfection**", "Destruction of **pathogens but not necessarily spores**; used on **inanimate** objects"],
       ["**Antisepsis**", "Destruction/inhibition of organisms on **living tissue**"],
       ["**Decontamination**", "Making an item safe to handle \u2014 **always the FIRST step**, before disinfection "
                               "or sterilization"],
       ["**Cleaning**", "Physical removal of soil \u2014 **a dirty instrument cannot be sterilized** (organic matter "
                        "blocks the sterilant)"],
       ["**Asepsis**", "**Medical asepsis** = clean technique (reduce numbers); **surgical asepsis** = sterile "
                       "technique (absence of all organisms)"],
       ["**Sporicidal**", "Kills spores \u2014 the property that makes an agent a **sterilant** rather than a "
                          "disinfectant"],
       ["**SAL (Sterility Assurance Level)**", "**10\u207b\u2076** \u2014 probability of \u2264 one viable organism "
                                               "in 10\u2076 items. The definition of \u2018sterile\u2019"],
       ["**D-value**", "Time or dose that reduces the population by **1 log\u2081\u2080 (90 %)**"]],
      widths=[4.2, 14.8])
h2("9.2  Spaulding classification")
table(["Category", "Definition", "Examples", "Processing"],
      [["**Critical**", "Enter **sterile tissue or the vascular system**",
        "Surgical instruments, implants, needles, cardiac and urinary catheters, laparoscopes", "**Sterilization**"],
       ["**Semi-critical**", "Contact **intact mucous membranes or non-intact skin**",
        "Flexible endoscopes, laryngoscope blades, ET tubes, respiratory/anaesthesia equipment",
        "**High-level disinfection**"],
       ["**Non-critical**", "Contact **intact skin only**", "BP cuffs, stethoscopes, OR table, floors, furniture",
        "**Low/intermediate-level disinfection**"]],
      widths=[2.8, 4.6, 7.4, 4.2])
para("**Resistance to killing, most \u2192 least: Prions > bacterial spores > coccidia > mycobacteria > small "
     "non-lipid viruses > fungi > vegetative bacteria > lipid-enveloped viruses (HIV, HBV \u2014 the EASIEST to "
     "kill).** A common MCQ inverts the last point. **Prions:** resist routine autoclaving \u2014 need "
     "**1 N NaOH plus 134 \u00b0C for 18 min**, and single-use instruments where possible.")
h2("9.3  Moist heat \u2014 saturated steam under pressure (autoclave)")
para("**Mechanism: denaturation and coagulation of proteins.** Moist heat beats dry heat because **latent heat of "
     "vaporisation** is released when steam condenses. It is the **method of choice \u2014 fastest, cheapest, most "
     "reliable, non-toxic**.")
table(["Cycle", "Temperature", "Pressure", "Hold time", "Use"],
      [["**Gravity displacement**", "**121 \u00b0C (250 \u00b0F)**", "**15 psi**", "**15\u201320 min** "
        "(wrapped 30 min)", "General load, glassware, rubber, media"],
       ["Gravity \u2014 high temp", "**134 \u00b0C**", "**30 psi**", "**3\u20133.5 min**", "Rapid cycles"],
       ["**Prevacuum (high-vacuum)**", "**132\u2013135 \u00b0C**", "\u2248 30 psi", "**3\u20134 min** + drying",
        "**Wrapped trays, textiles, lumened items** \u2014 air is actively evacuated"],
       ["**Flash / IUSS**", "**132 \u00b0C (270 \u00b0F)**", "\u2248 27\u201330 psi",
        "**3 min unwrapped metal; 10 min** porous/lumened",
        "**Only an urgently needed unwrapped single item** \u2014 never implants or whole sets"],
       ["Prions (CJD)", "134 \u00b0C", "\u2014", "**18 min**", "After NaOH immersion"]],
      widths=[3.4, 2.6, 2.2, 4.4, 6.4])
bullets([
    "**Air is the enemy of the autoclave** \u2014 trapped air lowers the temperature at a given pressure. So: "
    "**do not overload, do not wrap tightly, use mesh-bottom trays, place packs on edge with space between them, "
    "and never position a bowl so that it traps air.**",
    "**Bowie-Dick test** = a **daily test of air removal / steam penetration in a PREVACUUM sterilizer**, run in an "
    "**empty chamber at 134 \u00b0C for 3.5 min**. It is a **Class 2 chemical indicator** and it does **not** prove "
    "sterility.",
    "**Biological indicator at least weekly (daily preferred) and with EVERY implant load** \u2014 implant loads are "
    "quarantined until the result is available. Vacuum leak test weekly.",
    "**Cannot be autoclaved:** sharp cutting edges (blunted), oils, greases, powders, anhydrous materials, "
    "low-melting plastics, lensed endoscopes, heat-labile electronics.",
    "Drying is part of the cycle \u2014 **a wet pack is a contaminated pack**; do not touch or move packs until cool "
    "and dry.",
])
h2("9.4  Dry heat (hot air oven)")
para("**Mechanism: oxidation** \u2014 needs much higher temperature and longer time than moist heat.")
table(["Temperature", "Holding time"],
      [["**160 \u00b0C**", "**2 hours** (the pair most often asked)"],
       ["**170 \u00b0C**", "**1 hour**"],
       ["**180 \u00b0C**", "**30 minutes**"]],
      widths=[4.0, 6.0])
bullets([
    "**Uses:** glassware, **sharp instruments (does not blunt or corrode them)**, oils, greases, powders, anhydrous "
    "fats, glass syringes. **Not for** rubber, plastics or fabrics.",
    "Load loosely for air circulation; **allow to cool before opening**.",
    "**Other dry-heat methods:** **incineration** (\u2265 1100\u20131200 \u00b0C, final disposal of contaminated and "
    "anatomical waste), **red-heat flaming** (loops), **glass-bead steriliser** (250 \u00b0C, 20\u201340 s).",
    "**Biological indicator: Bacillus atrophaeus.**",
])
h2("9.5  Ethylene oxide gas")
table(["Parameter", "Value"],
      [["Mechanism", "**Alkylation** of DNA, RNA and protein"],
       ["**The 4 critical variables**", "**Gas concentration 450\u20131200 mg/L \u2022 temperature 37\u201363 "
                                        "\u00b0C \u2022 relative humidity 40\u201380 % \u2022 exposure 1\u20136 h** "
                                        "(the PDF quotes 3\u20137 h cycles) \u2014 **all four must be met**"],
       ["**Aeration is mandatory**", "**Mechanical aerator 8\u201312 h at 50\u201360 \u00b0C** (air changed \u2265 4 "
                                     "times/h), **or a ventilated room for 7 days at 18\u201322 \u00b0C**. Residual "
                                     "EO causes chemical burns and haemolysis"],
       ["Uses", "**Heat- and moisture-sensitive items** \u2014 flexible endoscopes, cardiac catheters, plastics, "
                "electrical and electronic equipment, prosthetic valves, pacemakers, delicate optics"],
       ["Rule", "**Anything that can withstand steam should NOT be gas-sterilized**"],
       ["Hazards", "**Toxic, irritant, mutagenic, teratogenic, carcinogenic (leukaemia/lymphoma), flammable and "
                   "explosive**; **OSHA PEL 1 ppm (8-h TWA)**, excursion 5 ppm/15 min"],
       ["Biological indicator", "**Bacillus atrophaeus**"],
       ["Note on the indicator", "An EO chemical indicator shows the item was **exposed** to EO \u2014 it does "
                                 "**not** prove sterilization occurred"]],
      widths=[3.4, 15.6])
h2("9.6  Low-temperature hydrogen peroxide gas plasma (STERRAD)")
bullets([
    "**58 % hydrogen peroxide** vaporised under vacuum, then excited by **radiofrequency energy** into a plasma of "
    "free radicals \u2192 kills bacteria, fungi, viruses **and spores**.",
    "**45\u201350 \u00b0C, cycle \u2248 1 hour; by-products are only water vapour and oxygen \u2192 NO aeration or "
    "cooling needed**, no toxic residue.",
    "Ideal for **fibre-optic cables, endoscopes, microsurgical and electrical equipment, glass, ceramics, metals**.",
    "**Cannot be used for cellulose \u2014 paper, cotton, linen, gauze, dressings** (they absorb the sterilant) "
    "\u2014 nor for liquids, powders or long narrow lumens. High capital cost.",
    "**Biological indicator: Geobacillus stearothermophilus.**",
])
h2("9.7  Liquid chemical sterilization / high-level disinfection")
table(["Agent", "Sterilization", "High-level disinfection", "Notes"],
      [["**Glutaraldehyde 2 % (activated \u2014 Cidex)**", "**10 hours**",
        "**20\u201345 min at 20\u201325 \u00b0C** (your PDF says 10 min \u2014 quote the textbook if the question is "
        "from it)",
        "**Does not corrode lenses or metal** \u2192 endoscopes. **Rinse in sterile distilled water.** "
        "**Test potency with a strip before each use.** Irritant/sensitiser \u2014 **asthma, dermatitis**; "
        "**ceiling 0.05 ppm**; wear polyethylene or double gloves"],
       ["**OPA 0.55 %**", "\u2014", "**12 min at 20 \u00b0C**", "Faster, less irritant; stains skin grey"],
       ["**Peracetic acid 0.2 % (Steris)**", "**12 min at 50\u201356 \u00b0C**", "\u2014",
        "Single-use, automatic dilution, effective **even with organic soil**, low surface tension \u2192 reaches "
        "lumens; **decomposes to acetic acid + water + oxygen**"],
       ["**Hydrogen peroxide 7.5 %**", "6 hours", "**30 min**", "Non-toxic breakdown products"]],
      widths=[4.0, 2.8, 4.0, 8.2])
h2("9.8  Radiation and filtration")
table(["Method", "Detail"],
      [["**Ionising (\u03b3) radiation**", "**Cobalt-60**, dose **25 kGy (2.5 Mrad)**. A **cold, industrial** method "
                                           "for pre-packed **single-use disposables** \u2014 syringes, needles, "
                                           "gloves, catheters, sutures, blades, heart valves, bone grafts. "
                                           "**Not used inside hospitals.** BI = **Bacillus pumilus**"],
       ["**Non-ionising UV-C (254 nm)**", "**Surface and air disinfection only \u2014 poor penetration** (blocked by "
                                          "glass, paper, water film). A **disinfectant, not a steriliser**. "
                                          "**Hazard: keratoconjunctivitis and erythema** \u2014 never run with the "
                                          "room occupied"],
       ["**Filtration**", "**0.22 \u00b5m** membrane for **heat-labile liquids** (sera, antibiotic and vaccine "
                          "solutions, media). **Removes but does not kill**, and **does not retain viruses or "
                          "mycoplasma** (needs 0.1 \u00b5m). Air equivalent = **HEPA** (\u00a75.1)"]],
      widths=[3.6, 15.4])
h2("9.9  Monitoring \u2014 the three-indicator system")
table(["Type", "What it is", "What it proves", "Examples"],
      [["**Physical / mechanical**", "Gauges, printout, chart recorder, cycle log",
        "That the **machine** reached the parameters; read and signed **every cycle**", "Sterilizer printout"],
       ["**Chemical (ISO 11140, classes 1\u20136)**", "Heat/chemical-sensitive dyes on tape, strips, cards",
        "**Exposure to the process \u2014 NOT sterility**",
        "**Class 1** process indicator (external autoclave tape) \u2022 **Class 2** = **Bowie-Dick** \u2022 "
        "**Class 3** single-variable \u2022 **Class 4** multi-variable \u2022 **Class 5 integrating** (all critical "
        "variables, correlates with the BI) \u2022 **Class 6 emulating** (most stringent). An **internal** indicator "
        "goes in the **centre of every pack**"],
       ["**Biological (BI) \u2014 GOLD STANDARD**", "Calibrated **highly resistant bacterial spores** processed with "
                                                   "the load, then incubated",
        "**The only indicator that proves the process actually killed spores**",
        "**Steam & H\u2082O\u2082 plasma \u2192 Geobacillus stearothermophilus** (incubate 55\u201360 \u00b0C) "
        "\u2022 **Dry heat & EO \u2192 Bacillus atrophaeus** (35\u201337 \u00b0C) \u2022 "
        "**\u03b3-radiation \u2192 Bacillus pumilus**"]],
      widths=[3.6, 4.2, 4.6, 6.6])
highyield("PACKAGING, STORAGE AND THE PROCESSING SEQUENCE",
          ["Packaging must **allow sterilant penetration, be a microbial barrier, permit aseptic opening and resist "
           "moisture**: double-thickness muslin, non-woven polypropylene, crepe paper, paper\u2013plastic peel "
           "pouches, rigid containers with filters. **Never closed metal containers or foil for steam.**",
           "**Shelf-life is EVENT-RELATED, not TIME-RELATED** \u2014 a pack is sterile **until an event compromises "
           "it** (wet, torn, punctured, soiled, seal broken, dropped, over-handled). The old \u201csterile for 30 "
           "days\u201d rule is obsolete.",
           "Storage: clean, dry, dust-free, closed cupboard, **20\u201323 \u00b0C, humidity 30\u201360 %**, "
           "**\u2265 20\u201325 cm above the floor, 45 cm below the ceiling/sprinkler, 5 cm from outside walls**; "
           "stock rotated **FIFO**.",
           "**Processing sequence:** point-of-use enzymatic spray in the OR \u2192 closed transport \u2192 "
           "**decontamination/washer-disinfector** \u2192 **ultrasonic cleaner (cavitation reaches box locks, "
           "serrations and lumens)** \u2192 rinse and dry \u2192 inspect, lubricate, assemble with "
           "**hinges and box locks OPEN** \u2192 pack with an internal indicator \u2192 sterilize \u2192 cool/dry "
           "\u2192 store."])



# ============================================================ 10
h1("10.  Emergencies and Disasters")
h2("10.1  Cardiac arrest in the OR \u2014 the numbers")
table(["Item", "Value"],
      [["Sequence", "**C\u2013A\u2013B**; high-quality compressions are the priority"],
       ["Rate / depth", "**100\u2013120 per minute**; **\u2265 5 cm and \u2264 6 cm** in adults (\u2153 of chest "
                        "depth in children)"],
       ["Compression : ventilation", "**30 : 2** unintubated adult; **continuous compressions with 1 breath every "
                                     "6 s** once an advanced airway is in; **15 : 2** two-rescuer paediatric"],
       ["Quality", "Interruptions **< 10 s**, **full recoil**, change compressor **every 2 min**, compression "
                   "fraction **> 60\u201380 %**; **EtCO\u2082 < 10 mmHg = poor CPR, a sudden rise suggests ROSC**"],
       ["Defibrillation", "**Biphasic 120\u2013200 J** (monophasic 360 J). **Shockable = VF and pulseless VT only; "
                          "PEA and asystole are NOT shockable**"],
       ["Drugs", "**Adrenaline 1 mg IV every 3\u20135 min**; **amiodarone 300 mg** then 150 mg for refractory "
                 "VF/pVT"],
       ["Reversible causes", "**4 H's** \u2014 Hypoxia, Hypovolaemia, Hypo/Hyperkalaemia-metabolic, Hypothermia; "
                             "**4 T's** \u2014 Tension pneumothorax, Tamponade, Toxins, Thrombosis"],
       ["Crash cart", "**Defibrillator + monitor**, airway drawer (laryngoscope, ET tubes, LMA, oral airways, "
                      "suction, **bag-valve-mask**), **in-date emergency drugs**, IV access and fluids, "
                      "**checked and re-sealed after every use and each shift with a signed checklist**"],
       ["Paediatric", "**PALS** competency required; shock **2 J/kg then 4 J/kg**; adrenaline **0.01 mg/kg**"],
       ["Documentation", "Every drug, dose, route, time, intervention and the person giving it \u2014 "
                         "**undocumented care is legally non-existent**"]],
      widths=[3.6, 15.4])
h2("10.2  Malignant hyperthermia \u2014 full protocol")
table(["Item", "Detail"],
      [["Genetics", "**Autosomal dominant**; **RYR1 (ryanodine receptor) gene on chromosome 19**; uncontrolled "
                    "Ca\u00b2\u207a release \u2192 sustained contracture and a **hypermetabolic crisis**"],
       ["**Triggers**", "**All volatile inhalational agents + SUCCINYLCHOLINE.** "
                        "**Safe: propofol, thiopentone, benzodiazepines, opioids, nitrous oxide, non-depolarising "
                        "relaxants, all local anaesthetics**"],
       ["Earliest sign", "**Unexplained rise in EtCO\u2082** with tachycardia/tachypnoea; **masseter spasm** after "
                         "succinylcholine. **Hyperthermia is a LATE sign** \u2014 do not wait for it"],
       ["Full picture", "Rigidity, hypercarbia, mixed acidosis, **hyperkalaemia**, arrhythmias, temperature rising "
                        "1\u20132 \u00b0C every 5 min, **myoglobinuria/rhabdomyolysis**, raised CK, DIC, renal "
                        "failure"],
       ["**Management**", "**1** Call for help and the MH cart \u2022 **2** **stop all triggers**, change circuit, "
                          "**hyperventilate with 100 % O\u2082 at \u2265 10 L/min** \u2022 **3** **DANTROLENE "
                          "2.5 mg/kg IV bolus, repeat every 5\u201310 min up to 10 mg/kg (may need 30)** \u2022 "
                          "**4** finish/abandon surgery quickly \u2022 **5** **active cooling** \u2014 iced IV "
                          "saline, ice packs, cold lavage of cavities; **stop at 38 \u00b0C** \u2022 **6** treat "
                          "hyperkalaemia and arrhythmias (**avoid calcium-channel blockers with dantrolene**) \u2022 "
                          "**7** maintain urine output **> 1\u20132 mL/kg/h** \u2022 **8** monitor core temperature, "
                          "ABG, K\u207a, CK, coagulation \u2022 **9** ICU **\u2265 24\u201336 h** (recrudescence up "
                          "to 25 %) \u2022 **10** counsel family, refer for **caffeine-halothane contracture or "
                          "genetic testing**, issue an alert card"],
       ["Dantrolene", "**20 mg lyophilised vials reconstituted with 60 mL sterile water**; keep a ~36-vial stock"],
       ["Mortality", "**> 70\u201380 % untreated \u2192 < 5\u201310 % with prompt dantrolene**"]],
      widths=[3.2, 15.8])
h2("10.3  Anaphylaxis in the OR")
bullets([
    "Commonest triggers: **neuromuscular blocking agents, antibiotics, chlorhexidine, LATEX, colloids, contrast**.",
    "**Latex anaphylaxis is typically DELAYED 20\u201360 min** after exposure (absorption across mucosa/peritoneum) "
    "\u2014 a favourite MCQ. Highest risk: **spina bifida, children with multiple operations, health-care workers**. "
    "**Cross-reacting foods: banana, avocado, chestnut, kiwi.**",
    "Signs under anaesthesia: **unexplained hypotension and tachycardia (commonest), high airway pressure / "
    "bronchospasm, desaturation**, flushing, angio-oedema, arrest.",
    "**Management: stop the trigger \u2192 100 % O\u2082 and secure the airway \u2192 ADRENALINE 0.5 mg IM "
    "(0.5 mL of 1:1000) into the antero-lateral thigh, repeat every 5 min** (or **50 \u00b5g IV boluses** if "
    "monitored and experienced) **\u2192 rapid IV crystalloid 20 mL/kg, legs up \u2192 chlorpheniramine 10 mg, "
    "hydrocortisone 200 mg, nebulised salbutamol.** Take **mast-cell tryptase** samples and refer for allergy "
    "testing.",
    "**Latex-safe environment:** first case of the day, latex-free gloves/tubing/catheters, a dedicated "
    "**latex-free crash cart**, signage on the door.",
])
h2("10.4  Fire in the operating room")
table(["Element", "Detail"],
      [["**Fire triangle**", "**FUEL + OXIDISER + IGNITION (heat)** \u2014 all three abound in an OR"],
       ["Commonest **ignition** source", "**Electrosurgical unit (\u2248 70\u201390 % of OR fires)**, then laser, "
                                         "then fibre-optic light cables"],
       ["Commonest **fuel**", "**Alcohol-based skin prep** (pooled or not dry), then drapes, gowns, gauze, hair, "
                              "ET tubes"],
       ["**Oxidiser**", "**Oxygen and nitrous oxide** \u2014 O\u2082 pools under drapes near the head (the classic "
                        "head-and-neck fire)"],
       ["Prevention", "Let alcohol **dry \u2265 3 min**, never allow pooling, blot puddles; keep FiO\u2082 "
                      "**< 30 %** for head/neck work; **pause oxygen before activating ESU/laser in the airway**; "
                      "moisten sponges and drapes; holster the pencil"],
       ["**Response \u2014 R A C E**", "**R**escue \u2022 **A**larm (call the code, e.g. **CODE RED**) \u2022 "
                                       "**C**onfine (close doors, shut off medical gases) \u2022 "
                                       "**E**xtinguish/**E**vacuate"],
       ["**Extinguisher \u2014 P A S S**", "**P**ull the pin \u2022 **A**im at the **base** of the fire \u2022 "
                                           "**S**queeze \u2022 **S**weep"],
       ["Extinguisher classes", "**A** ordinary combustibles \u2022 **B** flammable liquids \u2022 "
                                "**C electrical \u2192 CO\u2082 or dry chemical, NEVER water** \u2022 "
                                "**D** metals \u2022 **K** kitchen fats. The OR stocks **CO\u2082 or ABC dry "
                                "chemical**; CO\u2082 is preferred around equipment (no residue)"],
       ["**Airway fire drill**", "**Stop ventilation and disconnect the oxygen \u2192 REMOVE the ET tube and burning "
                                 "material \u2192 pour saline into the airway \u2192 ventilate on air \u2192 "
                                 "re-intubate and bronchoscope \u2192 steroids/ICU**; then incident report and "
                                 "device reporting"],
       ["Drills", "**At least twice a year, unannounced.** Everyone must know the code name and the location of the "
                  "alarm, extinguishers, gas shut-off valves and evacuation route. **Drapes and gowns are fire-"
                  "RETARDANT, not fire-PROOF**"]],
      widths=[3.4, 15.6])
h2("10.5  Disaster preparedness and triage")
table(["Concept", "Content"],
      [["Types", "**Internal** \u2014 fire, power/gas failure, structural, violent intruder; **External** \u2014 "
                 "earthquake, flood, road/rail crash, blast, chemical leak, epidemic"],
       ["Framework", "A written **Hospital Disaster Management Plan** based on a **Hazard Vulnerability Analysis**, "
                     "run through a **Hospital Incident Command System**, with call-tree, surge capacity and "
                     "**mock drills at least annually**"],
       ["**START triage**", "**S**imple **T**riage **A**nd **R**apid **T**reatment \u2014 **\u2264 60 s per "
                            "casualty**, assessing **RPM: Respiration, Perfusion, Mental status**"],
       ["**Triage colours**", "**RED = Priority I, immediate** (RR > 30, absent radial pulse / capillary refill > 2 s, "
                              "or not obeying commands \u2014 airway obstruction, major haemorrhage, shock) \u2022 "
                              "**YELLOW = Priority II, delayed** (can wait 1\u20134 h) \u2022 "
                              "**GREEN = Priority III, minor / walking wounded** \u2022 "
                              "**BLACK = Priority 0, dead or expectant** (not breathing after the airway is opened)"],
       ["Key principle", "In a mass casualty the aim shifts from \u2018the best for each individual\u2019 to "
                         "**\u2018the greatest good for the greatest number\u2019**; **triage is dynamic \u2014 "
                         "re-triage at every stage**"],
       ["Power failure", "Automatic **emergency generator** back-up, **UPS** for monitors and ventilators; everyone "
                         "must know where the **high-intensity torches** are kept, and where the "
                         "**self-inflating bag and reserve oxygen cylinder** are for medical-gas failure"],
       ["Emergency signal", "Each OR has a **special emergency signal (usually a flashing red light)** operable from "
                            "within that room"],
       ["Code colours (institution-specific)", "Typically **Blue** cardiac arrest \u2022 **Red** fire \u2022 "
                                               "**Pink** infant abduction \u2022 **Orange** mass casualty \u2022 "
                                               "**Black** bomb threat \u2022 **Brown** evacuation \u2022 "
                                               "**Grey** violent person. **Answer per your own institution's list**"],
       ["Pharmacist's disaster role", "Maintain and rotate **disaster drug stock and antidote kits** "
                                      "(atropine\u2013pralidoxime, potassium iodide, naloxone, antivenom, tetanus "
                                      "toxoid), bulk-prepare fluids and analgesics, control narcotic documentation, "
                                      "advise on dosing in renal failure/crush injury, manage the cold chain"]],
      widths=[3.6, 15.4])

# ============================================================ 11
h1("11.  In-Service Education, Body Mechanics and Fatigue Factors")
para("The PDF covers all three well. Only the quantitative anchors are missing.")
bullets([
    "**Orientation** = initial familiarisation with policies and the environment (**AORN recommends a mentor / buddy "
    "system**). **In-service education** = ongoing, employer-provided, job-specific \u2014 perioperative departments "
    "hold it **monthly**. **Continuing education** = professional development beyond the employer.",
    "**Mandatory recurring training:** fire safety with **drills at least twice a year (unannounced)**, disaster "
    "drill annually, infection control and hand hygiene, biomedical waste, needle-stick protocol, radiation safety, "
    "laser safety, electrical safety, hazard communication, **BLS recertification every 2 years**, ergonomics, and "
    "**competency validation for every new device before use**.",
    "**Body mechanics:** lift by **bending the knees and hips with the back straight**, position your body under the "
    "load, hold it close, feet apart, **straighten the legs so the lower-limb muscles do the work**, "
    "**pivot with the feet \u2014 never twist the spine**, push rather than pull, lift in unison on a count.",
    "**NIOSH maximum recommended load = 51 lb (23 kg)**; **patient-handling limit 35 lb (16 kg)**. OSHA (2002) "
    "requires facilities to reduce ergonomic injury; **lift teams** are cost-effective because back injury is the "
    "commonest occupational injury in health care.",
    "**Fatigue:** AORN recommends **\u2264 12 consecutive hours** of direct patient care, **\u2264 60 h/week "
    "including on-call**, and **8 h of uninterrupted sleep**. Being awake **17\u201319 hours** impairs performance "
    "about as much as a blood alcohol of 0.05 %. **Working with impaired judgement is an ethical breach, not just a "
    "personal risk.**",
    "**Other occupational hazards:** prolonged standing (varicose veins), repetitive strain in laparoscopy, "
    "**noise > 85 dB** from saws and drills, sharps injury, latex, and burnout.",
])

# ============================================================ 12
h1("12.  Radiation Safety")
h2("12.1  Units")
table(["Quantity", "SI unit", "Old unit", "Conversion"],
      [["**Absorbed dose**", "**Gray (Gy) = 1 J/kg**", "rad", "**1 Gy = 100 rad**"],
       ["**Equivalent / effective dose**", "**Sievert (Sv)**", "rem",
        "**1 Sv = 100 rem** \u2014 the unit used for **all dose limits and personnel monitoring**"],
       ["**Activity**", "**Becquerel (Bq)**", "Curie (Ci)", "1 Ci = 3.7 \u00d7 10\u00b9\u2070 Bq"],
       ["Exposure", "Coulomb/kg", "Roentgen (R)", "Ionisation in air"]],
      widths=[4.6, 4.6, 2.8, 7.0])
h2("12.2  Dose limits (ICRP / AERB)")
table(["Category", "Limit"],
      [["**Occupational, whole body**", "**20 mSv/year averaged over 5 years (100 mSv/5 y), maximum 50 mSv in any "
                                        "one year**"],
       ["Occupational, lens of the eye", "**20 mSv/year** (ICRP 2011 revision; formerly 150 mSv)"],
       ["Occupational, skin / extremities", "**500 mSv/year**"],
       ["**Declared pregnancy**", "**\u2264 1 mSv to the fetus** for the remainder of the pregnancy "
                                  "(**0.5 mSv/month**)"],
       ["**Public**", "**1 mSv/year**"]],
      widths=[5.4, 13.6])
h2("12.3  Protection \u2014 three cardinal principles under ALARA")
table(["Principle", "Application"],
      [["**1. Time**", "Minimise screening time; **pulsed fluoroscopy, last-image hold, collimation**; record total "
                       "screening time"],
       ["**2. Distance \u2014 INVERSE SQUARE LAW**", "**Intensity \u221d 1/d\u00b2**, so **doubling the distance "
                                                    "gives \u00bc the exposure** and tripling gives \u2153\u00b2 = "
                                                    "\u2151. Stand **\u2265 2 m (6 ft)** away or leave the room; "
                                                    "in lateral views stand on the **image-intensifier side, away "
                                                    "from the tube** (scatter is highest on the tube side)"],
       ["**3. Shielding**", "**Lead apron 0.25\u20130.5 mm lead equivalence** (0.5 mm attenuates \u2248 95\u201399 % "
                            "at 100 kVp), **thyroid collar, lead glasses, lead gloves for holding cassettes, mobile "
                            "lead screens**. Aprons are **hung, never folded**, and **screened annually for cracks**"],
       ["**ALARA**", "**A**s **L**ow **A**s **R**easonably **A**chievable \u2014 with ICRP's **justification, "
                     "optimisation and dose limitation**"],
       ["Monitoring", "Dosimeter worn **OUTSIDE the lead apron at chest/collar level** (a second one **inside at "
                      "waist level** in pregnancy). **TLD** is commonest; also film badge, OSL, electronic personal "
                      "dosimeter. Records kept for life"],
       ["Personnel rules", "Non-essential staff **leave the room or wear a lead apron**; scrubbed staff **don the "
                           "apron BEFORE scrubbing**; **never hand-hold the cassette or patient** if avoidable; "
                           "**pregnant staff avoid all radiation cases**"],
       ["Patient rules", "**Ask every woman of child-bearing age if she is or could be pregnant**; shield "
                         "**gonads and thyroid** when the beam cannot be collimated; lowest diagnostic exposure"],
       ["Radioactive implants", "Handle with **long forceps, never fingers**; lead pot in the room; limit and rotate "
                                "staff time; exclude pregnant staff and children; **survey the room and linen with a "
                                "Geiger-M\u00fcller counter** afterwards"]],
      widths=[3.8, 15.2])
h2("12.4  Biological effects")
table(["Effect", "Nature", "Examples"],
      [["**Deterministic (non-stochastic)**", "Has a **threshold**; **severity** increases with dose",
        "Skin erythema, epilation, **cataract**, sterility, marrow suppression, fetal malformation"],
       ["**Stochastic**", "**No threshold**; **probability** increases with dose (linear-no-threshold)",
        "**Carcinogenesis and heritable mutation**"]],
      widths=[4.4, 5.6, 9.0])
para("**Most radiosensitive:** bone marrow and lymphoid tissue, gonads, intestinal crypts, skin basal layer, lens, "
     "and the **fetus (most sensitive in weeks 2\u20138, organogenesis)**. **Least sensitive:** adult nerve, muscle "
     "and bone.")

# ============================================================ 13
h1("13.  Infection Control")
h2("13.1  Standard vs transmission-based precautions")
table(["Category", "Applies to", "Requirements", "Examples"],
      [["**Standard Precautions** (CDC 1996; absorbed the older **Universal Precautions**)",
        "**Every patient, every time** \u2014 all blood, body fluids, secretions and excretions **except sweat**, "
        "non-intact skin, mucous membranes",
        "**Hand hygiene \u2022 gloves \u2022 gown \u2022 mask/eye protection when splash is likely \u2022 safe "
        "injection and sharps practice \u2022 respiratory hygiene \u2022 safe handling of equipment, linen and waste "
        "\u2022 environmental cleaning**", "Universal application in the OR"],
       ["**Contact**", "Direct/indirect contact",
        "Standard + **gown and gloves for all contact**, dedicated equipment, single room preferred",
        "**MRSA, VRE, CRE, C. difficile (soap and water; hypochlorite for surfaces), scabies, RSV**"],
       ["**Droplet**", "Large droplets > 5 \u00b5m travelling **\u2248 1\u20132 m (3\u20136 ft)**",
        "Standard + **surgical mask within 1\u20132 m**, single room, mask the patient during transport",
        "**Influenza, pertussis, mumps, rubella, N. meningitidis, diphtheria**"],
       ["**Airborne**", "Droplet nuclei \u2264 5 \u00b5m that stay suspended",
        "Standard + **fit-tested N95**, and an **Airborne Infection Isolation Room \u2014 NEGATIVE pressure with "
        "\u2265 12 air changes/hour**, door closed",
        "**Pulmonary/laryngeal TB, measles, varicella**"]],
      widths=[4.0, 4.0, 6.0, 5.0])
h2("13.2  PPE sequence \u2014 rote-learn the order")
table(["Donning (put on)", "Doffing (take off)"],
      [["**1** Hand hygiene \u2192 **2 Gown** \u2192 **3 Mask/respirator** (fit-check) \u2192 "
        "**4 Goggles/face shield** \u2192 **5 Gloves**",
        "**1 Gloves** \u2192 **2 Goggles/face shield** \u2192 **3 Gown** \u2192 **4 Mask/respirator** (remove "
        "**outside** the room, by the ties only) \u2192 **5 Hand hygiene**"]],
      widths=[9.5, 9.5])
para("**The most contaminated item comes off first (gloves) and the respirator comes off last**, because it protects "
     "you until you have left the room.")
h2("13.3  Sharps injury and post-exposure prophylaxis")
table(["Item", "Detail"],
      [["**Transmission risk per percutaneous needle-stick**", "**Hepatitis B 6\u201330 %** (up to 30 % if "
                                                              "HBeAg-positive \u2014 the **highest**) \u2022 "
                                                              "**Hepatitis C \u2248 1.8 %** \u2022 "
                                                              "**HIV \u2248 0.3 % (1 in 300)**; mucous-membrane HIV "
                                                              "exposure **\u2248 0.09 %**"],
       ["**Immediate first aid**", "**Do NOT squeeze, suck, or apply bleach/alcohol/iodine into the wound.** "
                                   "**Wash with soap and running water**; irrigate eye/mucosa with water or saline "
                                   "for **10\u201315 min**; allow to bleed, dry and cover"],
       ["Then", "**Report immediately** \u2192 assess the exposure \u2192 **baseline serology of both parties** "
                "\u2192 **start PEP** \u2192 counselling \u2192 follow-up at **6 weeks, 3 months, 6 months** \u2192 "
                "**document and file an incident report**"],
       ["**HIV PEP**", "**As early as possible \u2014 ideally within 2 hours, never later than 72 hours**; "
                       "**3-drug regimen for 28 days**"],
       ["**Hepatitis B PEP**", "Unvaccinated or non-responder \u2192 **HBIG 0.06 mL/kg IM within 24 hours** "
                              "**plus** start the vaccine course. A **vaccinated responder (anti-HBs \u2265 10 "
                              "mIU/mL) needs nothing**. **HBV vaccination (0, 1, 6 months) is mandatory for "
                              "health-care workers**"],
       ["**Hepatitis C**", "**No vaccine and no PEP** \u2014 monitor and treat early infection with direct-acting "
                          "antivirals"],
       ["Prevention hierarchy", "**Elimination/substitution (needleless systems) \u2192 engineering controls "
                                "(retractable/sheathed needles, blunt suture needles, sharps container filled to "
                                "\u00be) \u2192 work-practice controls (never recap by hand \u2014 if unavoidable use "
                                "the one-handed \u2018scoop\u2019; **never pass a sharp hand-to-hand \u2014 use a "
                                "neutral zone / hands-free technique with a magnetic pad**; mount blades with a "
                                "needle holder) \u2192 PPE (**double gloving cuts inner-glove perforation by "
                                "70\u201380 %**, face shield)**"]],
      widths=[4.2, 14.8])
h2("13.4  Biomedical waste segregation \u2014 BMW Rules 2016 (India)")
table(["Colour", "Contents", "Treatment / disposal"],
      [["**YELLOW**", "**Human and animal anatomical waste**, soiled waste (dressings, cotton, blood-soaked items, "
                      "plaster casts), **expired and discarded medicines**, chemical waste, contaminated linen, "
                      "microbiology and laboratory waste, and **cytotoxic waste in a separate yellow "
                      "\u2018cytotoxic\u2019 container**",
        "**Incineration / plasma pyrolysis / deep burial** (deep burial only in towns < 500 000). "
        "**Cytotoxic waste \u2192 incineration at \u2265 1200 \u00b0C** or return to the manufacturer"],
       ["**RED**", "**Contaminated recyclable plastics** \u2014 IV tubing and sets, catheters, urine bags, "
                   "**syringes without needles**, gloves",
        "**Autoclave / microwave / hydroclave, then shred \u2192 registered recycler.** No chemical pre-treatment, "
        "no landfilling"],
       ["**WHITE** (translucent, puncture- and leak-proof)", "**Waste sharps including metals** \u2014 needles, "
                                                            "**syringes with fixed needles**, scalpels, blades",
        "**Autoclave or dry-heat sterilise, then shred/mutilate**; final disposal by **encapsulation in a concrete "
        "sharps pit** or to an iron foundry"],
       ["**BLUE**", "**Glassware** (broken/discarded contaminated glass, medicine vials and ampoules) and "
                    "**metallic body implants**",
        "**Disinfection (1 % hypochlorite) or autoclaving, then recycling**"]],
      widths=[3.4, 7.6, 8.0])
bullets([
    "**Golden rule: segregate at the point of generation, by the person generating the waste.** Bags filled to "
    "**\u00be**, tied (not stapled), labelled with the **biohazard/cytotoxic symbol**, stored **\u2264 48 hours**.",
    "**Never recap, bend or break needles by hand** \u2014 use a needle-tip cutter at the point of use; the needle "
    "goes to the **white** container.",
    "**Glass vials contaminated with cytotoxics go to YELLOW, not blue** \u2014 a classic trick question.",
    "**Mercury spill:** do **not** vacuum; collect with a syringe/adhesive tape or a spill kit into a sealed "
    "container of water and dispose as hazardous waste.",
    "Requirements: annual report to the Pollution Control Board, waste register, **annual health check-up and "
    "immunisation (hepatitis B, tetanus) of waste handlers**, PPE, and reporting of any major accident within 24 h. "
    "**Radioactive waste is governed separately by the AERB** (decay-in-storage).",
])

# ============================================================ 14
h1("14.  Chemical Hazards")
h2("14.1  Occupational exposure limits worth memorising")
table(["Agent", "Limit", "Effects and control"],
      [["**Nitrous oxide**", "**NIOSH REL 25 ppm**", "Megaloblastic change, neuropathy, **\u2191 spontaneous abortion "
                                                    "and reduced fertility**. Control: **scavenging system, no "
                                                    "leaks, tight masks, adequate air changes**"],
       ["**Halogenated volatiles**", "**NIOSH REL 2 ppm** (0.5 ppm with N\u2082O)",
        "Headache, fatigue, **impaired mental performance, audiovisual ability and manual dexterity**; "
        "hepatotoxicity; teratogenic concern"],
       ["**Ethylene oxide**", "**OSHA PEL 1 ppm**; excursion 5 ppm/15 min",
        "Irritant, **mutagen, carcinogen, flammable/explosive**. Dedicated ventilated room, gas monitors, aeration "
        "cabinet, personal badges"],
       ["**Formaldehyde**", "**OSHA PEL 0.75 ppm; STEL 2 ppm**",
        "Irritation, asthma, dermatitis, **Group 1 carcinogen** \u2014 why OT fumigation is abandoned. Handle "
        "specimens in a **ventilated hood**"],
       ["**Glutaraldehyde**", "**ACGIH ceiling 0.05 ppm**",
        "**Occupational asthma, rhinitis, conjunctivitis, contact dermatitis, epistaxis.** Use a **covered basin "
        "with local exhaust, nitrile or butyl gloves (NOT latex \u2014 it permeates), goggles and apron**"],
       ["**Methyl methacrylate** (bone cement)", "**OSHA PEL 100 ppm**",
        "Irritant, dermatitis, headache; and in the patient **cement implantation syndrome \u2014 hypotension, "
        "hypoxia, arrhythmia, arrest during cementing**. **Mix in a closed vacuum system with local exhaust**"],
       ["**Noise**", "OSHA action level **85 dB (8-h TWA)**", "Saws, drills, suction, alarms \u2014 hearing "
                                                             "protection; also impairs communication"],
       ["**Compressed gases**", "\u2014", "**Secure every cylinder upright; never drop one or let cylinders strike "
                                          "each other; valve cap on for transport; never oil or grease an oxygen "
                                          "valve; segregate full and empty.** A falling cylinder becomes a missile"]],
      widths=[3.6, 3.8, 11.6])
h2("14.2  Hazard communication, cytotoxics and spills")
bullets([
    "**Hazard Communication / \u2018Right to Know\u2019:** every hazardous chemical needs a **Safety Data Sheet "
    "(SDS, formerly MSDS) in 16 standardised sections**, accessible to all staff at all times, plus **GHS labelling** "
    "with the signal word **\u2018Danger\u2019** or **\u2018Warning\u2019** and the nine pictograms.",
    "**Hierarchy of controls, in order: elimination \u2192 substitution \u2192 engineering controls (ventilation, "
    "closed systems, scavenging) \u2192 administrative / work-practice controls \u2192 PPE (the LAST and weakest "
    "line).** The ranking itself is commonly asked.",
    "**Cytotoxic handling:** prepare in a **Class II Type B biological safety cabinet or containment isolator in a "
    "negatively-pressured, externally-vented room**; use **closed-system transfer devices** and Luer-lock syringes; "
    "PPE = **two pairs of chemotherapy-tested gloves (changed every 30\u201360 min), an impermeable back-closing "
    "gown, eye protection and a respirator**; **never crush or split cytotoxic tablets**; "
    "**pregnant and breast-feeding staff must not handle them**; dispose in the **yellow cytotoxic stream**; keep a "
    "**spill kit**.",
    "**Chemical spill: evacuate and restrict access \u2192 identify the agent from the SDS \u2192 don PPE \u2192 "
    "contain and absorb from the outside inwards \u2192 neutralise \u2192 bag as hazardous waste \u2192 ventilate "
    "\u2192 report and document.** For a **skin or eye splash, irrigate at the eyewash station or shower for a "
    "minimum of 15 minutes.**",
    "**Waste anaesthetic gas control** (the PDF's topic, with the mechanism added): an efficient **scavenger "
    "system**, a leak-free circuit with well-fitting masks and connectors, **air-conditioning with HEPA filters that "
    "do not recirculate air**, **anaesthetic gas leak detectors**, and the same ventilation standard extended to the "
    "**PACU** because it adjoins the surgical suite.",
])



# ============================================================ 15
h1("15.  Post-Operative Patient Care")
alert("WHY THIS SECTION IS KEPT",
      ["Your syllabus heading is \u201cPreparation of Patient for Operation, **Pre & Post Operative Patient "
       "Care**\u201d, but Chapter 1 of the PDF ends at the PACU hand-over and only reproduces a blank post-operative "
       "form. Everything below is new material.",
       "It has been trimmed to the **examinable core**: PACU and scoring systems, immediate complications, the fever "
       "timeline, wound complications and drains. Fluid regimens, nutrition and analgesic pharmacology have been "
       "cut as off-syllabus."])
h2("15.1  Phases of recovery and the PACU")
table(["Phase", "Location", "Focus"],
      [["**Phase I \u2014 immediate**", "PACU / recovery room, **1 nurse : 1\u20132 patients**",
        "Emergence; airway, breathing, circulation, consciousness, temperature, pain, haemorrhage"],
       ["**Phase II \u2014 intermediate**", "Step-down or ambulatory unit, ward",
        "Preparation for discharge home or to the ward; oral intake, ambulation, teaching"],
       ["**Phase III \u2014 extended**", "Ward, home", "Rehabilitation, wound care, complication surveillance"]],
      widths=[3.8, 5.6, 9.6])
bullets([
    "**Hand-over must include:** procedure and findings, **type of anaesthesia and reversal**, airway status, "
    "**allergies**, co-morbidity, intra-operative events and vital-sign trends, **blood loss, fluids and blood "
    "products given, urine output**, drains/catheters/packs, **analgesia and antiemetics given with times**, "
    "laterality, post-operative orders and whom to call. **The anaesthetist does not leave until the PACU nurse "
    "accepts the patient and the hand-over is documented.**",
    "**Monitoring: vital signs every 5\u201315 min** initially, then 15-minutely until stable \u2014 "
    "**RR and pattern, SpO\u2082, BP, pulse, temperature, ECG, pain score, level of consciousness**, plus "
    "**hourly urine and drain output**.",
    "**Position: lateral or head-up 15\u201330\u00b0** (keeps the tongue forward, lets secretions drain); "
    "**supine flat** after spinal anaesthesia or with hypotension. **Side rails up, oxygen on, suction and an Ambu "
    "bag at the bedside, and the patient is never left unattended.**",
    "**Check:** dressing for ooze, drain patency and character, IV site, **peripheral pulses and capillary refill "
    "distal to any cast or tourniquet, ability to move limbs and any paraesthesia** (rules out a positioning injury "
    "and assesses spinal regression), and bladder distension.",
    "**Warm actively** \u2014 forced-air blanket, warmed fluids; aim for core temperature **> 36 \u00b0C** before "
    "discharge from PACU.",
])
h2("15.2  Aldrete Score \u2014 memorise this table")
table(["Parameter", "2", "1", "0"],
      [["**A**ctivity", "Moves **all four limbs** on command", "Moves **two** extremities", "Unable to move"],
       ["**R**espiration", "Breathes deeply and **coughs freely**", "Dyspnoeic or shallow", "Apnoeic / ventilated"],
       ["**C**irculation (BP)", "**Within \u00b1 20 %** of pre-anaesthetic level", "\u00b1 20\u201349 %",
        "\u00b1 \u2265 50 %"],
       ["**C**onsciousness", "**Fully awake**", "Rousable on calling", "Not responding"],
       ["**O**xygen saturation", "**SpO\u2082 > 92 % on room air**", "Needs O\u2082 to keep SpO\u2082 > 90 %",
        "< 90 % even with O\u2082"]],
      widths=[4.2, 5.6, 4.8, 4.4])
highyield("SCORING \u2014 EXAM POINTS",
          ["**Maximum 10; discharge from PACU requires \u2265 9** with no parameter scoring 0, plus stable vitals, "
           "controlled pain and PONV, no active bleeding and normothermia. Mnemonic **A-R-C-C-O**.",
           "The **original 1970 Aldrete score used skin COLOUR**; the **modified score replaced colour with "
           "pulse-oximetry SpO\u2082**.",
           "**Pain and nausea are NOT in the Aldrete score** \u2014 they belong to the **PADSS**. This inversion is a "
           "classic MCQ.",
           "**PADSS** (Post-Anaesthesia Discharge Scoring System, for discharge **home** after day surgery) scores "
           "0\u20132 each for **vital signs \u2022 ambulation \u2022 nausea/vomiting \u2022 pain \u2022 surgical "
           "bleeding**; **\u2265 9 required**, plus a **responsible escort, written instructions and tolerance of "
           "oral fluids**.",
           "Counsel: **no driving, machinery, legal documents, alcohol or sole care of a child for at least 24 hours** "
           "after general anaesthesia or sedation.",
           "After spinal/epidural anaesthesia also document **return of motor power, sensation and the sensory "
           "level**."])
h2("15.3  Immediate post-operative complications")
table(["Complication", "Cause", "Recognition", "Management"],
      [["**Airway obstruction \u2014 the commonest immediate PACU emergency**",
        "**Tongue falling back against the posterior pharynx** in the sedated supine patient; secretions, blood, "
        "laryngeal oedema",
        "**Snoring or stridor, see-saw (paradoxical) chest movement, tracheal tug**, desaturation",
        "**Head tilt\u2013chin lift / jaw thrust**, lateral position, suction, oral or nasal airway, 100 % O\u2082; "
        "re-intubate if needed"],
       ["**Laryngospasm**", "Cord stimulation in light anaesthesia, secretions, blood",
        "**Inspiratory stridor progressing to complete silence**, paradoxical effort",
        "Remove the stimulus, suction, **100 % O\u2082 with CPAP and jaw thrust**; if persistent \u2014 propofol then "
        "**succinylcholine** and intubate"],
       ["**Hypoventilation**", "**Residual anaesthetic, opioids, incomplete reversal of neuromuscular blockade**, "
                               "pain splinting, obesity, hypothermia",
        "Slow shallow breathing, \u2191 EtCO\u2082, drowsiness, pin-point pupils",
        "Stimulate, O\u2082, support ventilation; **naloxone 40\u201380 \u00b5g increments** for opioids, "
        "**neostigmine/sugammadex** for relaxant, **flumazenil** for benzodiazepines"],
       ["**Atelectasis \u2014 the commonest post-op pulmonary complication**",
        "Shallow breathing, retained secretions, upper-abdominal or thoracic incision",
        "**Low-grade fever POD 1\u20132**, reduced basal breath sounds, tachypnoea",
        "**Deep breathing and incentive spirometry (10 breaths hourly), splinted coughing, early ambulation, "
        "adequate analgesia, physiotherapy** \u2014 not antibiotics"],
       ["**Hypotension**", "**Hypovolaemia (commonest \u2014 blood loss, third-space loss)**, residual anaesthetic, "
                           "sympathetic block from spinal/epidural, arrhythmia, ischaemia, sepsis, anaphylaxis",
        "**Check the surgical site and drains for bleeding FIRST**; tachycardia and a narrow pulse pressure precede "
        "hypotension",
        "Head-down/legs up, O\u2082, **crystalloid bolus 10\u201320 mL/kg**, vasopressor if needed, ECG, Hb, "
        "cross-matched blood; **surgical control is definitive**"],
       ["**Hypertension**", "**Pain (commonest) and bladder distension**, hypoxia/hypercarbia, hypothermic shivering, "
                            "omitted antihypertensives, fluid overload",
        "Raised BP with restlessness", "**Treat the cause first \u2014 analgesia, empty the bladder, oxygenate, "
                                       "warm** \u2014 before giving antihypertensives"],
       ["**Delayed emergence**", "Residual drugs; **hypoglycaemia, hypoxia, hypercarbia, hyponatraemia, hypothermia "
                                 "(< 33 \u00b0C prevents awakening)**; stroke, seizure",
        "Failure to wake as expected", "**Check glucose, ABG, electrolytes and pupils**; reverse opioids and "
                                      "benzodiazepines; **think stroke if there are focal signs**"],
       ["**Emergence delirium / agitation**", "Commonest in **children and the elderly**; also hypoxia, pain, full "
                                              "bladder, ketamine, withdrawal",
        "Restlessness, disorientation, thrashing", "**Always exclude hypoxia first**, then pain and a full bladder; "
                                                   "reassure and orientate; avoid physical restraint"],
       ["**Hypothermia and shivering**", "Cold OR, anaesthetic vasodilatation, cold fluids, large exposed cavity, "
                                         "elderly and neonates",
        "Core < 36 \u00b0C; shivering **raises O\u2082 consumption up to 400 %**; causes **coagulopathy, \u2191 blood "
        "loss, \u2191 SSI, arrhythmia, delayed drug metabolism**",
        "**Forced-air warming, warmed fluids and irrigation, raised room temperature**; oxygen; "
        "**pethidine (meperidine) 12.5\u201325 mg IV** is the most effective drug for shivering"],
       ["**Haemorrhage**", "**Reactionary \u2014 within 24 h** (slipped ligature, clot dislodged as BP rises); "
                           "**Secondary \u2014 POD 7\u201314 from infection eroding a vessel**",
        "Tachycardia, narrow pulse pressure, restlessness, cool clammy skin, oliguria, brisk drain output",
        "Two large-bore cannulae, crystalloid, **cross-matched blood / massive transfusion protocol**, tranexamic "
        "acid, keep warm, **return to theatre**"]],
      widths=[3.2, 4.4, 4.8, 6.6])
h2("15.4  Post-operative nausea and vomiting (PONV) \u2014 in brief")
bullets([
    "Incidence **20\u201330 %**, up to **80 %** in high-risk patients; the commonest reason for unplanned admission "
    "after day surgery.",
    "**Apfel score \u2014 1 point each for: female sex \u2022 non-smoker \u2022 previous PONV or motion sickness "
    "\u2022 expected post-operative opioid use.** Risk for 0/1/2/3/4 factors \u2248 **10 / 20 / 40 / 60 / 80 %**. "
    "**Smoking is protective.**",
    "Other risks: volatile agents and **nitrous oxide**, long anaesthesia, and gynaecological, laparoscopic, "
    "middle-ear, squint and breast surgery.",
    "**Drugs by receptor:** **5-HT\u2083 antagonist \u2014 ondansetron 4\u20138 mg IV, given at the END of surgery** "
    "(watch **QT prolongation**) \u2022 **steroid \u2014 dexamethasone 4\u20138 mg at induction** \u2022 "
    "**D\u2082 antagonist \u2014 metoclopramide** (extrapyramidal effects; avoid in obstruction) \u2022 "
    "**NK\u2081 \u2014 aprepitant** \u2022 **antihistamine \u2014 cyclizine** \u2022 "
    "**anticholinergic \u2014 hyoscine patch** \u2022 **propofol TIVA** is itself antiemetic.",
    "**Strategy: 1\u20132 risk factors \u2192 two agents from DIFFERENT classes; \u2265 3 \u2192 three or four agents "
    "plus propofol TIVA, avoiding nitrous oxide and sparing opioids.** For breakthrough PONV use a class **not "
    "already given**.",
])
h2("15.5  Post-operative fever \u2014 the \u201cW's\u201d timeline (very high yield)")
table(["Onset", "\u201cW\u201d", "Cause", "Action"],
      [["**During or within 24 h**", "**W**hat we did / **W**onder drugs",
        "Inflammatory (cytokine) response to surgery, **drug or transfusion reaction, MALIGNANT HYPERTHERMIA**, "
        "pre-existing infection", "**Usually NOT infective.** Rigidity + \u2191 EtCO\u2082 \u2192 dantrolene; stop "
                                  "any transfusion"],
       ["**POD 1\u20132**", "**W**ind", "**ATELECTASIS \u2014 the commonest cause of early post-op fever**; "
                                       "aspiration, early pneumonia",
        "Incentive spirometry, deep breathing, ambulation, analgesia, physiotherapy"],
       ["**POD 3\u20135**", "**W**ater", "**Urinary tract infection** (catheter-associated)",
        "Urinalysis and culture; **remove or change the catheter**; antibiotics"],
       ["**POD 4\u20136**", "**W**alking", "**Deep-vein thrombosis / pulmonary embolism**",
        "Calf pain and unilateral swelling, or sudden dyspnoea and hypoxia \u2192 Doppler / CTPA; anticoagulate"],
       ["**POD 5\u20137**", "**W**ound", "**Surgical site infection**; also **anastomotic leak** (with tachycardia "
                                        "and ileus)", "Inspect \u2192 **open, drain and culture**; suspect a leak if "
                                                      "the patient is \u2018not doing well\u2019"],
       ["**> POD 7**", "**W**onder drugs", "**Drug fever**, abscess/collection, C. difficile colitis, IV-site "
                                          "thrombophlebitis, line infection",
        "Review the drug chart; culture blood, urine and line tips; CT for a collection"]],
      widths=[3.0, 2.6, 6.4, 7.0])
mnemonic("MNEMONIC \u2014 Wind, Water, Walking, Wound, Wonder drugs",
         ["Time order: **Wind (1\u20132) \u2192 Water (3\u20135) \u2192 Walking (4\u20136) \u2192 Wound (5\u20137) "
          "\u2192 Wonder drugs (> 7)**.",
          "**Fever in the first 24 hours is usually NOT infection.** **Fever after POD 5 with wound signs is "
          "infection until proved otherwise.**"])
h2("15.6  Wound healing and wound complications")
table(["Phase", "Timing", "Events", "Dominant cell"],
      [["**Haemostasis**", "Minutes\u2013hours", "Vasoconstriction, platelet plug, fibrin clot", "Platelets"],
       ["**Inflammatory (lag)**", "**Day 0\u20134/5**", "Vasodilatation, exudate, phagocytosis, debridement; wound "
                                                       "held only by clot and sutures",
        "**Neutrophils (24\u201348 h) \u2192 MACROPHAGES (48\u201372 h \u2014 the key cell)**"],
       ["**Proliferative (fibroplasia)**", "**Day 4\u201321", "**Collagen III** deposition, angiogenesis, granulation "
                                                              "tissue, epithelialisation, contraction",
        "**Fibroblasts**"],
       ["**Maturation / remodelling**", "**Day 21 \u2192 1\u20132 years**", "**Collagen III replaced by collagen I**, "
                                                                           "cross-linking, scar pales and flattens",
        "Fibroblasts, collagenase"]],
      widths=[4.0, 3.0, 7.6, 4.4])
bullets([
    "**Tensile strength: \u2248 5\u201310 % at 1 week, 30\u201350 % at 1 month, maximum only 70\u201380 % of normal "
    "skin** \u2014 which is why dehiscence peaks in the first week and lifting is restricted for six weeks.",
    "**Types of healing:** **primary (first) intention** \u2014 apposed edges, fine scar; **secondary intention** "
    "\u2014 left open, heals by granulation and contraction (contaminated wounds, abscess cavities); "
    "**tertiary / delayed primary closure** \u2014 left open 3\u20135 days then closed.",
    "**Factors delaying healing** \u2014 local: **infection, ischaemia, haematoma, foreign body, tension, dead "
    "space, movement, radiation**; systemic: **age, diabetes, malnutrition (protein, vitamin C, vitamin A, zinc), "
    "anaemia and hypoxia, obesity, smoking, steroids and immunosuppressants, chemotherapy, jaundice, uraemia, "
    "malignancy**.",
    "**Dressings:** the first dressing over a primarily closed wound is left undisturbed **24\u201348 h** "
    "(epithelialisation is complete and it acts as a bacterial barrier); thereafter change with **aseptic technique**, "
    "inspect and document; change immediately if soaked (**strike-through**).",
    "**Suture removal:** face and neck **3\u20135 days**; scalp **7\u201310**; trunk/abdomen **7\u201310**; "
    "upper and lower limb **10\u201314**; over joints, back, palms and soles **14 days**.",
])
table(["Complication", "Timing and features", "Management"],
      [["**Haematoma**", "24\u201348 h; swelling, discoloration, pain. **A neck haematoma after thyroidectomy is an "
                         "AIRWAY EMERGENCY**",
        "Small \u2192 observe; expanding or compressive \u2192 **open and evacuate** (at the bedside for the neck)"],
       ["**Seroma**", "Day 3\u201310, especially after **mastectomy, axillary or groin dissection, mesh hernia "
                      "repair**; fluctuant, painless", "Aseptic aspiration, compression, drains"],
       ["**Surgical site infection**", "**POD 5\u20137**; pain, erythema, warmth, induration, purulent discharge, "
                                       "fever. **Spreading cellulitis or crepitus on POD 1\u20132 \u2192 suspect "
                                       "streptococcal or clostridial necrotising infection \u2014 a surgical "
                                       "emergency**",
        "**Open, drain, culture, debride, pack for secondary healing**, culture-guided antibiotics \u2014 "
        "\u2018the treatment of pus is drainage\u2019"],
       ["**Dehiscence**", "**POD 5\u201310 (classically day 7\u20138)**; the herald sign is a **sudden "
                          "serosanguineous \u2018salmon-pink\u2019 discharge** with a palpable gap, often after a "
                          "cough",
        "Abdominal binder, avoid straining, **inform the surgeon \u2192 usually re-suturing in theatre**"],
       ["**Evisceration (burst abdomen)**", "Protrusion of viscera through the wound",
        "**EMERGENCY: stay with the patient; supine, low Fowler's with knees flexed; COVER the viscera with sterile "
        "gauze soaked in WARM sterile normal saline \u2014 never dry gauze and never push the bowel back; keep nil by "
        "mouth; IV access and fluids; monitor for shock; analgesia; notify the surgeon and prepare for immediate "
        "theatre**"],
       ["**Incisional hernia**", "Weeks to years later \u2014 the late consequence of subclinical dehiscence or "
                                 "infection", "Elective mesh repair"],
       ["**Hypertrophic scar vs keloid**", "**Hypertrophic** stays **within** the original margins and tends to "
                                           "regress; **keloid extends BEYOND** the margins, does not regress and "
                                           "recurs after excision (commoner in darker skin, sternum, shoulder, ear "
                                           "lobe)", "Silicone sheeting, pressure, intralesional steroid"]],
      widths=[3.2, 8.2, 7.6])
h2("15.7  Drains, and the rest of the routine")
table(["Drain", "Type", "Key point"],
      [["**Penrose / corrugated**", "**Passive, open**", "Gravity or capillary action; higher infection risk"],
       ["**Jackson-Pratt (bulb)**", "**Closed, active**", "**Re-compress the bulb after emptying** \u2014 a fully "
                                                         "expanded bulb means suction has been lost"],
       ["**Hemovac / Redivac**", "**Closed, active (spring / high vacuum)**", "Orthopaedic, breast and neck surgery"],
       ["**Chest (intercostal) drain**", "**Closed, underwater seal**",
        "**Keep the bottle below chest level; never clamp a bubbling drain; \u2018swinging\u2019 = patent, continuous "
        "bubbling = air leak.** If disconnected \u2192 place the end in sterile water; if it falls out \u2192 "
        "occlusive dressing taped on **three sides**"],
       ["**Nasogastric tube**", "Decompression / feeding", "Confirm position by **pH < 5.5 on aspirate or X-ray** "
                                                          "\u2014 the auscultation \u2018whoosh\u2019 test is "
                                                          "unreliable and unsafe"],
       ["**Urinary catheter**", "Closed drainage", "**Closed system, bag below bladder level and off the floor, no "
                                                  "dependent loops, remove within 24 h.** **CAUTI is the commonest "
                                                  "healthcare-associated infection**"]],
      widths=[3.6, 3.6, 11.8])
bullets([
    "**Drain care:** secure against traction, keep patent, chart **volume, colour and character** each shift, aseptic "
    "site dressing, and **never advance a drain back in**. **Brisk bright-red output \u2192 haemorrhage; faecal or "
    "bilious output \u2192 anastomotic leak; cloudy or foul \u2192 infection** \u2014 report immediately.",
    "**Bowel function returns in the order: small intestine \u2248 24 h \u2192 stomach 24\u201348 h \u2192 COLON "
    "48\u201372 h (last).** Resolution is judged by the **passage of flatus or stool**, not bowel sounds. "
    "**Ileus** \u2014 absent bowel sounds and generalised distension; **mechanical obstruction** \u2014 colicky pain "
    "with high-pitched tinkling sounds.",
    "**Urine output must exceed 0.5 mL/kg/h (\u2248 30 mL/h).** Post-operative oliguria is **most often "
    "hypovolaemia**; **urinary retention** (commonest after anorectal, hernia, pelvic and spinal-anaesthetic surgery) "
    "shows as suprapubic fullness, restlessness and overflow dribbling \u2192 privacy, upright position, warm "
    "compress, analgesia, then **in-and-out catheterisation**.",
    "**DVT peaks POD 5\u201310** and is often silent; **PE** presents as sudden dyspnoea, pleuritic pain, tachycardia "
    "and hypoxia, and is a leading cause of **preventable** post-operative death. Prevention = **early ambulation, "
    "ankle exercises, TED stockings, intermittent pneumatic compression, LMWH, hydration and adequate analgesia so "
    "the patient can move**.",
    "**Respiratory bundle:** semi-Fowler's position, **incentive spirometry 10 breaths hourly**, **splinted "
    "coughing**, adequate analgesia, **ambulation within 24 h**, oral hygiene, humidified oxygen.",
    "**Red flags to teach the patient before discharge:** fever, increasing pain, spreading redness, purulent or "
    "foul discharge, wound gaping, bleeding, calf pain or swelling, chest pain or breathlessness, persistent "
    "vomiting, inability to pass urine.",
])
highyield("MEDICATION SAFETY IN THE OR \u2014 the pharmacist's angle on this unit",
          ["Extend the PDF's **five rights** to the **eight rights**: right **patient, drug, dose, route, time**, "
           "plus right **documentation, indication and response**.",
           "**Every medication on the sterile field is labelled immediately** with name, strength and concentration; "
           "**unlabelled medications are ALWAYS discarded**; **all vials and syringes stay in the room until the end "
           "of the case**; labelled medications are **shown to the relief person** at hand-over; "
           "**calculations are independently double-checked by a second licensed professional**.",
           "**High-alert drugs in the OR:** concentrated **potassium chloride**, insulin, heparin, "
           "**neuromuscular blockers (\u2018paralysing agent \u2014 warning\u2019 label)**, concentrated adrenaline, "
           "local anaesthetics, oxytocin, and **look-alike/sound-alike pairs** (ephedrine/epinephrine).",
           "**Constraints recommended by AORN:** minimise the number of calculations required, stock "
           "**dose-specific ready-to-use concentrations**, standardise concentrations, use pre-filled syringes, and "
           "assess competency regularly.",
           "Also the pharmacist's OT duties: crash-cart stock, expiry and seal checks, **cold-chain logs**, "
           "**narcotic accounting (NDPS register)**, sterile dilution of injectables, **ADR reporting "
           "(pharmacovigilance)** and in-service education on new drugs and devices."])

# ============================================================ 16
h1("16.  The Numbers Sheet")
table(["Topic", "Number"],
      [["Fasting", "**2 h clear fluids \u2022 4 h breast milk \u2022 6 h formula/light meal \u2022 8 h fatty meal**; "
                   "aspiration risk if gastric volume **> 25 mL** and **pH < 2.5**"],
       ["Antibiotic prophylaxis", "**Within 60 min of incision**; re-dose after **2 half-lives** or **> 1500 mL** "
                                 "blood loss; **stop within 24 h**"],
       ["Identification", "**\u2265 2 identifiers**; WHO checklist = **3 phases, 19 items**; Universal Protocol "
                          "**July 2004**; AORN position addition **March 2005**"],
       ["Safety strap", "Mid-thighs, **\u2248 3 inches (7.5 cm) above the knees**; arms abducted **\u2264 90\u00b0**; "
                        "Trendelenburg **30\u201345\u00b0**"],
       ["Sterile field", "Wrapper edge unsterile **2.5 cm (1 in)** \u2022 unsterile person keeps **30 cm (1 ft)** away "
                         "\u2022 gown sleeves sterile to **5 cm above the elbow**"],
       ["Scrub", "First scrub of the day **3\u20135 min**; double gloving cuts perforation **70\u201380 %**"],
       ["OR environment", "**20\u201323 \u00b0C \u2022 RH 20\u201360 % \u2022 \u2265 15 (ideally 20\u201325) air "
                          "changes/h \u2022 POSITIVE pressure \u2022 HEPA 99.97 % at 0.3 \u00b5m \u2022 "
                          "laminar flow 300\u2013600 ACH \u2022 noise < 45 dB**"],
       ["Wound class SSI risk", "**Clean < 2 % \u2022 clean-contaminated 3\u201310 % \u2022 contaminated "
                                "15\u201320 % \u2022 dirty 30\u201340 %**; SSI window **30 days (90 with an "
                                "implant)**"],
       ["Autoclave", "**121 \u00b0C / 15 psi / 15\u201320 min \u2022 134 \u00b0C / 30 psi / 3\u20133.5 min \u2022 "
                     "prevacuum 132\u2013135 \u00b0C / 3\u20134 min \u2022 flash 132 \u00b0C / 3 min unwrapped "
                     "(10 min lumened) \u2022 prions 134 \u00b0C / 18 min**"],
       ["Hot air oven", "**160 \u00b0C / 2 h \u2022 170 \u00b0C / 1 h \u2022 180 \u00b0C / 30 min**"],
       ["Bowie-Dick", "**134 \u00b0C for 3.5 min in an EMPTY prevacuum chamber, daily** \u2014 tests **air removal**"],
       ["Ethylene oxide", "**450\u20131200 mg/L \u2022 37\u201363 \u00b0C \u2022 RH 40\u201380 % \u2022 1\u20136 h**; "
                          "aeration **8\u201312 h at 50\u201360 \u00b0C** or **7 days** at room temperature"],
       ["H\u2082O\u2082 plasma", "**58 % H\u2082O\u2082 \u2022 45\u201350 \u00b0C \u2022 \u2248 1 h \u2022 no "
                                "cellulose, no liquids**"],
       ["Liquid chemicals", "**Glutaraldehyde 2 % \u2014 10 h sterilization / 20\u201345 min HLD \u2022 OPA 0.55 % "
                            "\u2014 12 min \u2022 peracetic acid \u2014 12 min at 50\u201356 \u00b0C \u2022 "
                            "H\u2082O\u2082 7.5 % \u2014 30 min HLD**"],
       ["Sterility", "**SAL 10\u207b\u2076** \u2022 \u03b3-radiation **25 kGy** \u2022 filter **0.22 \u00b5m** "
                     "\u2022 shelf-life is **event-related**"],
       ["Biological indicators", "**Steam & plasma \u2192 Geobacillus stearothermophilus \u2022 dry heat & EO \u2192 "
                                 "Bacillus atrophaeus \u2022 radiation \u2192 Bacillus pumilus**"],
       ["Electrosurgery", "**300 kHz \u2013 3 MHz**; no nerve stimulation above **~100 kHz**; ultrasonic scalpel "
                          "**55.5 kHz**; LigaSure seals **7 mm**; smoke \u2014 1 g tissue \u2248 **3\u20136 "
                          "cigarettes**, evacuator within **1\u20132 in**, **ULPA 99.999 % at 0.1 \u00b5m**"],
       ["Tourniquet", "**Upper limb 250\u2013300 mmHg / \u2264 60 min \u2022 lower limb 300\u2013350 mmHg / "
                      "\u2264 90\u2013120 min**; overlap **3\u20136 in**; deflate **10\u201315 min** if longer"],
       ["CPR", "**100\u2013120/min \u2022 5\u20136 cm \u2022 30:2 \u2022 biphasic 120\u2013200 J \u2022 adrenaline "
               "1 mg q3\u20135 min \u2022 amiodarone 300 mg**"],
       ["Anaphylaxis", "**Adrenaline 0.5 mg IM (1:1000)**, repeat q5 min; IV **50 \u00b5g** boluses; fluid "
                       "**20 mL/kg**"],
       ["Malignant hyperthermia", "**Dantrolene 2.5 mg/kg up to 10 (\u201330) mg/kg \u2022 O\u2082 10 L/min \u2022 "
                                  "cool to 38 \u00b0C \u2022 urine > 1\u20132 mL/kg/h \u2022 RYR1, chromosome 19**"],
       ["Radiation", "**1 Gy = 100 rad \u2022 1 Sv = 100 rem**; occupational **20 mSv/y (max 50 in one year)**; "
                     "public **1 mSv/y**; eye **20 mSv/y**; extremities **500 mSv/y**; fetus **1 mSv** "
                     "(0.5 mSv/month); apron **0.25\u20130.5 mm Pb**; stand **\u2265 2 m**; doubling distance "
                     "\u2192 **\u00bc**"],
       ["Needle-stick", "**HBV 6\u201330 % \u2022 HCV 1.8 % \u2022 HIV 0.3 %**; HIV PEP within **2 h (max 72 h) for "
                        "28 days**; **HBIG 0.06 mL/kg within 24 h**"],
       ["Chemical limits", "**EO 1 ppm \u2022 formaldehyde 0.75 ppm \u2022 glutaraldehyde 0.05 ppm ceiling \u2022 "
                           "N\u2082O 25 ppm \u2022 volatiles 2 ppm \u2022 methyl methacrylate 100 ppm \u2022 "
                           "noise 85 dB**"],
       ["Lifting", "**NIOSH 51 lb (23 kg)**; patient handling **35 lb (16 kg)**"],
       ["Waste", "**Yellow** anatomical/soiled/expired drugs/cytotoxic \u2022 **Red** recyclable plastics \u2022 "
                 "**White** sharps \u2022 **Blue** glass and metallic implants; bags to **\u00be**; cytotoxic "
                 "incineration **\u2265 1200 \u00b0C**; storage **\u2264 48 h**"],
       ["Fatigue & drills", "**\u2264 12 consecutive hours \u2022 \u2264 60 h/week \u2022 8 h sleep**; fire drills "
                            "**\u2265 2/year**; BLS recertification **every 2 years**"],
       ["Recovery scores", "**Aldrete max 10, discharge \u2265 9** (A-R-C-C-O) \u2022 **PADSS \u2265 9** \u2022 "
                           "**Apfel 4 factors \u2192 10/20/40/60/80 %**"],
       ["Post-op timeline", "**Fever: Wind 1\u20132 \u2022 Water 3\u20135 \u2022 Walking 4\u20136 \u2022 Wound "
                            "5\u20137 \u2022 Drugs > 7** \u2022 **dehiscence POD 5\u201310** \u2022 "
                            "**secondary haemorrhage POD 7\u201314** \u2022 **DVT POD 5\u201310**"],
       ["Wound healing", "Inflammatory **0\u20134 d** \u2022 proliferative **4\u201321 d** \u2022 remodelling "
                         "**21 d\u20131 y**; tensile strength **5\u201310 % at 1 wk, 30\u201350 % at 1 month, max "
                         "70\u201380 %**; sutures out **face 3\u20135, trunk 7\u201310, limbs 10\u201314, joints "
                         "14 d**"],
       ["Bowel & urine", "**Small bowel 24 h \u2192 stomach 24\u201348 h \u2192 colon 48\u201372 h**; urine output "
                         "**> 0.5 mL/kg/h**"]],
      widths=[4.0, 15.0])



# ============================================================ 17  MCQ
h1("17.  MCQ Bank \u2014 77 Questions, Syllabus-Weighted")
alert("ABOUT THESE QUESTIONS",
      ["**77 questions**, every one mapped to a listed syllabus sub-point. Questions on off-syllabus topics "
       "(ASA grading, premedication pharmacology, analgesic choice, fluid regimens) have been removed from the "
       "earlier draft.",
       "They are **modelled on the pattern and difficulty of previous-year questions** in Indian pharmacy, nursing "
       "and OT-technology papers, and **written from the standard sources** \u2014 AORN Guidelines, "
       "Berry & Kohn's Operating Room Technique, CDC/HICPAC guidelines, WHO, ICRP/AERB, OSHA/NIOSH, "
       "BMW Rules 2016 and Bailey & Love. They are **not verbatim reproductions** of any single paper.",
       "Weighting, matched to where the marks fall: **sterilization 14 \u2022 post-operative care 13 \u2022 "
       "environment/asepsis/SSI 10 \u2022 electrosurgery & equipment 9 \u2022 pre-op preparation, identification, "
       "records & counting 9 \u2022 positioning 8 \u2022 emergencies 7 \u2022 radiation, chemical hazards & waste 7.**"])

h2("A \u2014 Pre-Operative Preparation, Identification and Records")
mcq("The minimum fasting period for clear liquids before elective surgery in a healthy adult is",
    ["1 hour", "2 hours", "4 hours", "6 hours"], 1,
    "Remember **2-4-6-8**: clear fluids 2 h, breast milk 4 h, formula/light meal 6 h, fatty meal 8 h. The purpose is "
    "to prevent **aspiration (Mendelson's syndrome)**; prolonged fasting is harmful and does not reduce gastric "
    "volume.")
mcq("The preferred method of pre-operative hair removal is",
    ["Shaving with a razor the night before", "Shaving with a razor in the OR",
     "Electric clippers immediately before surgery", "Hair is always left intact"], 2,
    "Ideally hair is **not removed**; if it interferes, use **clippers immediately before surgery, outside the OR**. "
    "Razor shaving \u2014 especially the night before \u2014 creates micro-abrasions and carries the **highest** SSI "
    "risk.")
mcq("The WHO Surgical Safety Checklist consists of how many phases?",
    ["Two", "Three", "Four", "Five"], 1,
    "**Three: Sign In** (before induction), **Time Out** (after induction, before incision), **Sign Out** (before "
    "leaving the OR) \u2014 19 items. It reduced mortality from 1.5 % to 0.8 %.")
mcq("The surgical \u201ctime out\u201d must be performed",
    ["On admission to the ward", "In the holding area", "After induction but before skin incision",
     "Immediately after wound closure"], 2,
    "The time out is the whole-team verbal pause **immediately before incision**. The **Universal Protocol** was "
    "mandated by the Joint Commission in **July 2004**; **AORN added the correct patient position in March 2005**.")
mcq("Which of the following is verified during the \u201cSign Out\u201d phase?",
    ["Pulse oximeter functioning", "Site marking", "Correctness of instrument, sponge and needle counts",
     "Difficult airway risk"], 2,
    "Sign Out covers the **name of the procedure recorded, correctness of counts, specimen labelling read aloud, "
    "equipment problems and key recovery concerns**. Pulse oximetry, site marking and airway risk belong to "
    "**Sign In**.")
mcq("A specimen for frozen section must be sent",
    ["In 10 % formalin", "Fresh, in saline-moistened gauze", "In absolute alcohol", "In 2 % glutaraldehyde"], 1,
    "**Frozen sections go FRESH \u2014 never in formalin**, which prevents further processing and "
    "immunohistochemistry. Routine histopathology goes in **10 % neutral buffered formalin at \u2248 10\u00d7 the "
    "specimen volume**; culture specimens go in a sterile container with no fixative.")
mcq("Consent for surgery on a 10-year-old child is governed by which section of the IPC?",
    ["Section 87", "Section 88", "Section 89", "Section 92"], 2,
    "**\u00a7 89** \u2014 acts done in good faith for a **child under 12** or a person of unsound mind, with the "
    "guardian's consent. **\u00a7 90** \u2014 consent given under fear or misconception is invalid. "
    "**\u00a7 92** \u2014 acts in good faith **without** consent in an emergency.")
mcq("A retained surgical sponge presenting years later as an abdominal mass is called a",
    ["Granuloma annulare", "Gossypiboma", "Pseudocyst", "Phlegmon"], 1,
    "**Gossypiboma (textiloma)** \u2014 gauze encased in a foreign-body granuloma. The sponge is the **commonest "
    "retained item (50\u201370 %)** and this is a classic **res ipsa loquitur** claim. Risk factors: emergency "
    "surgery, **unexpected change of procedure** and high BMI.")
mcq("The legal responsibility for recording the surgical count rests with the",
    ["Surgeon", "Scrub person", "Circulator", "Anaesthetist"], 2,
    "Both count **aloud together** as the scrub person touches each item, but **keeping the written record is the "
    "circulator's legal responsibility**, and the circulator initials every addition.")

h2("B \u2014 Transfer and Positioning")
mcq("The single most important measure to prevent a patient falling from the operating table is",
    ["Side rails", "A safety strap firmly applied across the mid-thighs", "Padded armboards",
     "Two staff at the bedside"], 1,
    "The strap across the **mid-thighs, \u2248 3 inches (7.5 cm) above the knees**, firm but not tight enough to "
    "impair venous return. The patient is also **never left unattended** in the OR.")
mcq("The nerve most commonly injured in the lithotomy position is the",
    ["Femoral nerve", "Sciatic nerve", "Common peroneal nerve", "Obturator nerve"], 2,
    "The **common peroneal nerve** is compressed against the **fibular head** by the stirrup post \u2192 **foot "
    "drop** and loss of dorsal foot sensation. Lithotomy also risks **lower-limb compartment syndrome** if prolonged.")
mcq("The commonest peripheral nerve injury in the supine position involves the",
    ["Radial nerve", "Ulnar nerve", "Median nerve", "Axillary nerve"], 1,
    "**Ulnar neuropathy** is the commonest peri-operative nerve injury overall. Prevent by abducting the arms "
    "**\u2264 90\u00b0**, padding the elbows and placing the **palms up (supinated)**.")
mcq("All of the following occur in the Trendelenburg position EXCEPT",
    ["Increased intracranial pressure", "Increased venous return", "Increased functional residual capacity",
     "Cephalad displacement of the diaphragm"], 2,
    "Trendelenburg **decreases** FRC and compliance because abdominal contents push the diaphragm cephalad \u2192 "
    "atelectasis. It increases venous return, CVP, **ICP and IOP**, and risks facial/laryngeal oedema and tube "
    "migration.")
mcq("Reverse Trendelenburg position is typically used for",
    ["Abdominal hysterectomy", "Thyroidectomy", "Haemorrhoidectomy", "Nephrectomy"], 1,
    "Reverse Trendelenburg (head up) is used for **neck surgery \u2014 thyroidectomy, parathyroidectomy, scalene node "
    "biopsy \u2014 and laparoscopic cholecystectomy**. Trendelenburg is for pelvic surgery, lithotomy/jackknife for "
    "anorectal, lateral kidney for nephrectomy.")
mcq("The Kraske (jackknife) position is a modification of the",
    ["Supine position", "Prone position", "Lateral position", "Fowler's position"], 1,
    "**Kraske/jackknife is a PRONE modification** exposing the sacrococcygeal and anorectal area. "
    "**Trendelenburg, reverse Trendelenburg, Fowler's and lithotomy are all modifications of SUPINE.**")
mcq("Both legs must be lowered slowly and simultaneously from the lithotomy position mainly to prevent",
    ["Nerve traction", "A sudden fall in blood pressure", "Wound dehiscence", "Deep vein thrombosis"], 1,
    "Lowering the legs shifts blood into the lower limbs \u2192 **sudden reduction in venous return and a "
    "precipitous fall in blood pressure**. Two persons lower them together, slowly.")
mcq("In the lateral position the axillary (chest) roll should be placed",
    ["Directly in the axilla", "Just caudal to the axilla under the chest wall", "Under the iliac crest",
     "Between the knees"], 1,
    "It goes **caudal to (below) the axilla** to lift the chest wall off the **dependent brachial plexus and axillary "
    "vessels**. Placing it **in** the axilla causes the very injury it should prevent.")

h2("C \u2014 Environment, Asepsis and SSI")
mcq("A HEPA filter removes",
    ["99.97 % of particles \u2265 0.3 \u00b5m", "99.9 % of particles \u2265 1 \u00b5m",
     "95 % of particles \u2265 0.5 \u00b5m", "99.999 % of particles \u2265 0.1 \u00b5m"], 0,
    "**HEPA = 99.97 % of particles 0.3 \u00b5m and larger.** The 99.999 % at 0.1 \u00b5m figure is an **ULPA** "
    "filter, used in surgical-smoke evacuators.")
mcq("The operating room is maintained at which pressure relative to the corridor?",
    ["Negative", "Positive", "Equal", "Alternating"], 1,
    "**Positive**, so air flows **out** of the OR. **Negative pressure with \u2265 12 air changes/hour** is used for "
    "**airborne isolation \u2014 tuberculosis, measles, varicella**.")
mcq("The recommended relative humidity in an operating room is",
    ["Below 20 %", "20\u201360 %", "70\u201380 %", "Above 80 %"], 1,
    "**20\u201360 %** (classically 30\u201360 %). **Too low \u2192 static electricity and spark risk; too high "
    "\u2192 microbial growth and condensation.** Temperature **20\u201323 \u00b0C** with **\u2265 15 air "
    "changes/hour**.")
mcq("The single most effective measure for preventing healthcare-associated infection is",
    ["Prophylactic antibiotics", "Hand hygiene", "Ultraviolet irradiation", "Routine fumigation"], 1,
    "**Hand hygiene with an antimicrobial agent** \u2014 stated explicitly in your PDF as the greatest single factor "
    "in preventing nosocomial infection. Routine formaldehyde fumigation is obsolete and UV is only an adjunct.")
mcq("A draped instrument table is considered sterile",
    ["To 30 cm below the table top", "Only at and above table-top level", "Down to the floor",
     "Only in the central third"], 1,
    "**Anything below table-top level is unsterile and is never brought back up.** Related: the wrapper edge "
    "(**1 inch / 2.5 cm**) is unsterile, the **gown back** is unsterile, and **moisture contaminates by "
    "strike-through**.")
mcq("An elective cholecystectomy without spillage is classified as",
    ["Clean", "Clean-contaminated", "Contaminated", "Dirty"], 1,
    "Entry into the biliary/GI tract under controlled conditions = **clean-contaminated (Class II), SSI 3\u201310 %**. "
    "Clean **< 2 %**, contaminated **15\u201320 %**, dirty/infected **30\u201340 %**.")
mcq("The commonest organism causing surgical site infection is",
    ["Escherichia coli", "Pseudomonas aeruginosa", "Staphylococcus aureus", "Clostridium perfringens"], 2,
    "**Staphylococcus aureus**, then coagulase-negative staphylococci, Enterococcus and E. coli. The commonest "
    "**source** of contamination is the **patient's own endogenous flora**.")
mcq("Alcohol-based hand rub is ineffective, and soap and water must be used, against",
    ["MRSA", "Clostridioides difficile", "Influenza virus", "Pseudomonas aeruginosa"], 1,
    "**Alcohol is not sporicidal**, so **C. difficile spores need mechanical removal with soap and water** (plus "
    "contact precautions and hypochlorite for surfaces). Soap and water is also mandatory for **visibly soiled "
    "hands**.")
mcq("Artificial fingernails are prohibited in the OR chiefly because they",
    ["Tear surgical gloves", "Harbour Gram-negative bacteria and fungi", "Interfere with pulse oximetry",
     "Absorb chlorhexidine"], 1,
    "AORN prohibits artificial nails and chipped polish because the **subungual space harbours Gram-negative bacilli "
    "and fungi** and cannot be decontaminated. (Polish does also affect pulse oximetry, but infection control is the "
    "reason asked.)")
mcq("The correct sequence for REMOVING (doffing) personal protective equipment is",
    ["Gown \u2192 gloves \u2192 mask \u2192 goggles", "Gloves \u2192 goggles \u2192 gown \u2192 mask",
     "Mask \u2192 gown \u2192 gloves \u2192 goggles", "Goggles \u2192 gloves \u2192 mask \u2192 gown"], 1,
    "**Doffing: gloves \u2192 goggles/face shield \u2192 gown \u2192 mask/respirator (outside the room) \u2192 hand "
    "hygiene.** The most contaminated item comes off first and the respirator last. **Donning is the reverse: gown "
    "\u2192 mask \u2192 goggles \u2192 gloves.**")

h2("D \u2014 Electro Surgery and Equipment")
mcq("Electrosurgical units operate in which frequency range?",
    ["50\u201360 Hz", "1\u201310 kHz", "300 kHz \u2013 3 MHz", "10\u2013100 MHz"], 2,
    "**Radiofrequency, 300 kHz \u2013 3 MHz.** Above about **100 kHz** the current no longer stimulates nerve or "
    "muscle (**the Faradic effect is avoided**), which is why RF current cuts and coagulates without electrocuting.")
mcq("Which statement about bipolar electrosurgery is TRUE?",
    ["It requires a dispersive return pad", "Current passes through the whole patient", "No dispersive pad is required",
     "It cannot be used in patients with pacemakers"], 2,
    "Both electrodes are the **two tines of the forceps**, so current passes only between them. **No pad is needed**, "
    "lateral spread is minimal, and it is the **safest mode with a pacemaker**.")
mcq("The coagulation waveform of an ESU is",
    ["Continuous low-voltage current", "Interrupted high-voltage current", "Direct current",
     "Continuous current at 50 Hz"], 1,
    "**Coag = interrupted, high-voltage, low duty cycle (~6 %)**; **cut = continuous, low-voltage, high-current "
    "(100 % duty cycle)**. Coag's high voltage explains its greater risk of **capacitive coupling and insulation "
    "breakdown**.")
mcq("Capacitive coupling in laparoscopic electrosurgery is most likely when",
    ["Bipolar forceps are used", "A metal instrument passes through a plastic (hybrid) trocar",
     "The pad is on the thigh", "Cut mode is used at low power"], 1,
    "A **hybrid metal\u2013plastic trocar** lets current be induced through **intact insulation** into surrounding "
    "tissue. Use all-metal or all-plastic systems, lowest power, cut rather than coag, short activations and "
    "**active-electrode monitoring**.")
mcq("A pin-hole break in the insulation of a laparoscopic electrode classically causes",
    ["An immediately visible spark", "A return-electrode burn", "Delayed bowel perforation several days later",
     "Failure of the generator to activate"], 2,
    "**Insulation failure** discharges current **outside the surgeon's field of view** \u2192 a full-thickness bowel "
    "burn perforating **3\u201310 days post-operatively** with peritonitis. Inspect insulation before every use.")
mcq("A return-electrode contact quality monitoring (REM) system prevents",
    ["Alternate-site burns from metal contact", "Pad-site burns from inadequate pad contact", "Capacitive coupling",
     "Surgical smoke exposure"], 1,
    "A **split pad** whose halves are monitored for impedance; the generator **shuts down when contact becomes "
    "inadequate**, virtually eliminating **return-electrode (pad-site) burns**.")
mcq("The surgeon repeatedly asks for higher ESU power. The correct action is to",
    ["Increase the power as requested", "Switch to bipolar",
     "Stop, check all connections and the dispersive pad, and replace the unit if faulty",
     "Reposition the ECG electrodes"], 2,
    "Repeated requests indicate a **fault \u2014 poor pad contact, a loose connection, a frayed cord or a failing "
    "generator**. Check the circuit; if no cause is found, **turn off and unplug the unit, label it, get another, and "
    "document the occurrence and serial numbers**.")
mcq("Which statement about surgical smoke is correct?",
    ["A standard surgical mask is adequate protection",
     "Ablating 1 g of tissue is roughly equivalent to 3\u20136 unfiltered cigarettes", "It is sterile and harmless",
     "A HEPA rather than an ULPA filter is required in the evacuator"], 1,
    "Smoke contains **> 150 chemicals** plus viable cells and viral DNA (**documented HPV transmission to "
    "surgeons**). Control = **smoke evacuator with an ULPA filter held within 1\u20132 inches** plus a "
    "**high-filtration mask or N95** \u2014 a standard mask is **not** sufficient.")
mcq("For an average adult, maximum recommended tourniquet time and pressure for the LOWER limb are",
    ["30 min at 200 mmHg", "60 min at 250 mmHg", "90\u2013120 min at 300\u2013350 mmHg", "3 hours at 400 mmHg"], 2,
    "**Lower limb 300\u2013350 mmHg for \u2264 90\u2013120 min; upper limb 250\u2013300 mmHg for \u2264 60 min.** "
    "**Deflate for 10\u201315 min** if longer, and record site, pressure and both inflation and deflation times.")

h2("E \u2014 Sterilization and Disinfection")
mcq("Standard gravity-displacement autoclave conditions are",
    ["100 \u00b0C at atmospheric pressure for 30 min", "121 \u00b0C at 15 psi for 15\u201320 min",
     "134 \u00b0C at 15 psi for 30 min", "160 \u00b0C for 2 hours"], 1,
    "**121 \u00b0C (250 \u00b0F) at 15 psi for 15\u201320 minutes**, or **134 \u00b0C at 30 psi for 3\u20133.5 "
    "minutes**. 160 \u00b0C for 2 h is a **hot air oven (dry heat)** cycle.")
mcq("Flash (immediate-use) steam sterilization of an unwrapped metal instrument is carried out at",
    ["121 \u00b0C for 20 min", "132 \u00b0C for 3 min", "132 \u00b0C for 30 min", "160 \u00b0C for 1 hour"], 1,
    "**132 \u00b0C (270 \u00b0F) for 3 minutes** unwrapped non-porous metal; **10 minutes** for porous, lumened or "
    "complex items. IUSS is **only for an urgently needed single item** \u2014 never implants, sets, or convenience.")
mcq("The Bowie-Dick test detects",
    ["Inadequate air removal in a prevacuum sterilizer", "Adequate ethylene oxide concentration",
     "Spore-killing efficacy", "Steam superheating only"], 0,
    "A **Class 2 chemical indicator** run **daily in an EMPTY prevacuum chamber at 134 \u00b0C for 3.5 min** to test "
    "**air removal / steam penetration**. It does **not** prove sterility \u2014 only a **biological indicator** "
    "does.")
mcq("The biological indicator for steam sterilization is",
    ["Bacillus atrophaeus", "Geobacillus stearothermophilus", "Bacillus pumilus", "Clostridium sporogenes"], 1,
    "**Geobacillus stearothermophilus** (thermophile, incubated 55\u201360 \u00b0C) for **steam and hydrogen peroxide "
    "plasma**; **Bacillus atrophaeus** for **dry heat and ethylene oxide**; **Bacillus pumilus** for "
    "**gamma radiation**.")
mcq("Dry heat sterilization in a hot air oven requires",
    ["121 \u00b0C for 15 min", "134 \u00b0C for 3 min", "160 \u00b0C for 2 hours", "180 \u00b0C for 2 hours"], 2,
    "**160 \u00b0C for 2 h** (or 170 \u00b0C for 1 h, 180 \u00b0C for 30 min). It is preferred for **glassware, oils, "
    "powders, greases and sharp instruments \u2014 it does not blunt or corrode them** \u2014 but not for rubber, "
    "plastics or linen.")
mcq("Which item CANNOT be processed in a hydrogen peroxide gas plasma (STERRAD) sterilizer?",
    ["A fibre-optic cable", "A stainless-steel instrument", "Cotton gauze and paper drapes",
     "A microsurgical instrument"], 2,
    "**Cellulose \u2014 paper, cotton, linen, gauze, dressings \u2014 absorbs the sterilant**, as do liquids, powders "
    "and long narrow lumens. Advantages: **45\u201350 \u00b0C, \u2248 1 h cycle, and NO aeration** because "
    "by-products are only water and oxygen.")
mcq("Sterilization with 2 % activated glutaraldehyde requires immersion for",
    ["10 minutes", "30 minutes", "3 hours", "10 hours"], 3,
    "**10 hours for sterilization**; **high-level disinfection** in **20\u201345 minutes** (your PDF quotes 10 min "
    "\u2014 quote the textbook if the question comes from it). Rinse in **sterile distilled water** and "
    "**test potency with a strip** before each use.")
mcq("After use, peracetic acid decomposes into",
    ["Formaldehyde and water", "Acetic acid, water and oxygen", "Chlorine and water", "Ethylene glycol"], 1,
    "**Acetic acid (vinegar), water and oxygen** \u2014 so it is environmentally safe and can go down an ordinary "
    "drain. It also works **in the presence of organic soil** and its low surface tension reaches lumens.")
mcq("Under the Spaulding classification, a flexible gastrointestinal endoscope is",
    ["Critical \u2014 needs sterilization", "Semi-critical \u2014 needs high-level disinfection",
     "Non-critical \u2014 needs low-level disinfection", "Non-critical \u2014 needs only cleaning"], 1,
    "Endoscopes contact **intact mucous membranes** \u2192 **semi-critical \u2192 high-level disinfection**. "
    "**Critical** items enter sterile tissue or the vascular system (sterilization); **non-critical** items touch only "
    "intact skin.")
mcq("The internationally accepted Sterility Assurance Level is",
    ["10\u207b\u00b3", "10\u207b\u2074", "10\u207b\u2076", "10\u207b\u00b9\u00b2"], 2,
    "**SAL = 10\u207b\u2076** \u2014 no more than one viable organism per million sterilized items. This is the "
    "quantitative definition of \u2018sterile\u2019.")
mcq("Which is the MOST resistant to sterilization and disinfection?",
    ["HIV", "Mycobacterium tuberculosis", "Bacterial spores", "Prions"], 3,
    "Decreasing resistance: **prions > bacterial spores > coccidia > mycobacteria > small non-lipid viruses > fungi "
    "> vegetative bacteria > lipid-enveloped viruses (HIV, HBV \u2014 the easiest to kill)**. Prions need "
    "**1 N NaOH plus 134 \u00b0C for 18 min**.")
mcq("The shelf-life of a sterilized wrapped pack is determined by",
    ["A fixed 7-day limit", "A fixed 30-day limit", "Event-related sterility", "The class of chemical indicator used"],
    2,
    "**Event-related sterility** \u2014 the pack is sterile until an event compromises it (wet, torn, punctured, "
    "seal broken, dropped, over-handled). The old \u201c30 days\u201d rule is obsolete.")
mcq("Gamma radiation sterilization uses a cobalt-60 source at a dose of",
    ["2.5 kGy", "25 kGy", "250 kGy", "2500 kGy"], 1,
    "**25 kGy (2.5 Mrad)** \u2014 a **cold, industrial** method for pre-packed **single-use disposables** (syringes, "
    "gloves, catheters, sutures, blades, heart valves), **not used inside hospitals** because of cost and shielding.")
mcq("Membrane filtration of a heat-labile solution uses a pore size of",
    ["0.45 \u00b5m", "0.22 \u00b5m", "1.2 \u00b5m", "5 \u00b5m"], 1,
    "**0.22 \u00b5m** retains bacteria and is used for sera, antibiotic and vaccine solutions and media. Note it "
    "**removes but does not kill**, and **does not retain viruses or mycoplasma** (0.1 \u00b5m is needed).")

h2("F \u2014 Emergencies and Disasters")
mcq("Malignant hyperthermia is triggered by",
    ["Propofol and nitrous oxide", "Volatile inhalational agents and succinylcholine",
     "Non-depolarising muscle relaxants", "Local anaesthetics"], 1,
    "Triggers are **all volatile agents and succinylcholine**. **Safe: propofol, thiopentone, benzodiazepines, "
    "opioids, nitrous oxide, non-depolarising relaxants and all local anaesthetics.** The defect is in the "
    "**RYR1 gene on chromosome 19**.")
mcq("The initial dose of dantrolene in malignant hyperthermia is",
    ["0.5 mg/kg", "1 mg/kg", "2.5 mg/kg", "10 mg/kg immediately"], 2,
    "**2.5 mg/kg IV bolus, repeated every 5\u201310 min up to 10 mg/kg** (occasionally 30). Simultaneously stop the "
    "triggers, **hyperventilate with 100 % O\u2082 at \u2265 10 L/min**, cool actively (**stop at 38 \u00b0C**), "
    "treat hyperkalaemia, and keep urine output **> 1\u20132 mL/kg/h**.")
mcq("The earliest sign of malignant hyperthermia under general anaesthesia is",
    ["Hyperthermia", "An unexplained rise in end-tidal CO\u2082", "Myoglobinuria", "Hypotension"], 1,
    "**Rising EtCO\u2082** with tachycardia and tachypnoea; **masseter spasm** after succinylcholine is the classic "
    "clue. **Hyperthermia is a LATE sign** \u2014 waiting for it costs lives.")
mcq("The adult intramuscular dose of adrenaline in anaphylaxis is",
    ["0.1 mg of 1:10 000", "0.5 mg of 1:1000 into the antero-lateral thigh", "1 mg of 1:1000 subcutaneously",
     "5 mg nebulised"], 1,
    "**0.5 mg IM (0.5 mL of 1:1000) into the antero-lateral thigh, repeated every 5 min**; **50 \u00b5g IV boluses** "
    "if monitored and experienced. Then **crystalloid 20 mL/kg**, chlorpheniramine, hydrocortisone and salbutamol.")
mcq("Latex anaphylaxis under anaesthesia characteristically",
    ["Never causes hypotension", "Is typically delayed 20\u201360 minutes after exposure", "Occurs only in adults",
     "Responds only to steroids"], 1,
    "Absorption across **mucosa or peritoneum** makes latex reactions **delayed 20\u201360 min** rather than "
    "immediate. Highest risk: **spina bifida, children with multiple operations, health-care workers**. "
    "Cross-reacting foods: **banana, avocado, chestnut, kiwi**.")
mcq("The extinguisher of choice for an electrical fire in the OR is",
    ["Water", "Foam", "Carbon dioxide (Class C)", "Class D dry powder"], 2,
    "**CO\u2082 or ABC dry chemical for Class C electrical fires \u2014 never water.** CO\u2082 is preferred around "
    "equipment because it leaves no residue. The commonest **ignition** source of OR fires is the **ESU "
    "(70\u201390 %)** and the commonest **fuel** is **alcohol-based prep**.")
mcq("In START triage, a casualty who is not breathing even after the airway is opened is tagged",
    ["Red", "Yellow", "Green", "Black"], 3,
    "**Black = dead/expectant.** **Red** = immediate (RR > 30, absent radial pulse or capillary refill > 2 s, or not "
    "obeying commands); **Yellow** = delayed; **Green** = minor/walking. START assesses **RPM \u2014 Respiration, "
    "Perfusion, Mental status** in under a minute.")

h2("G \u2014 Radiation, Chemical Hazards and Waste")
mcq("The SI unit of equivalent dose of radiation is the",
    ["Gray", "Sievert", "Becquerel", "Roentgen"], 1,
    "**Sievert (Sv)** \u2014 used for **all dose limits and personnel monitoring** (**1 Sv = 100 rem**). The **Gray** "
    "is absorbed dose (1 Gy = 100 rad) and the **Becquerel** is activity.")
mcq("The annual occupational whole-body radiation dose limit is",
    ["1 mSv", "20 mSv averaged over 5 years", "50 mSv every year without restriction", "150 mSv"], 1,
    "**20 mSv/year averaged over 5 consecutive years (100 mSv/5 y), with a maximum of 50 mSv in any single year.** "
    "Public **1 mSv/y**; lens **20 mSv/y**; extremities **500 mSv/y**; declared pregnancy **\u2264 1 mSv to the "
    "fetus (0.5 mSv/month)**.")
mcq("If the distance from a radiation source is doubled, exposure is reduced to",
    ["One half", "One quarter", "One eighth", "One sixteenth"], 1,
    "**Inverse square law \u2014 intensity \u221d 1/d\u00b2**, so doubling gives **one quarter** and tripling gives "
    "one ninth. Stand **\u2265 2 m (6 ft)** away or leave the room. The three principles are **time, distance and "
    "shielding**, under **ALARA**.")
mcq("A personal radiation dosimeter should be worn",
    ["Inside the lead apron at waist level", "Outside the lead apron at chest/collar level", "On the wrist",
     "On the X-ray machine"], 1,
    "**Outside the apron at chest or collar level**, to record dose to the unshielded neck, head and lens. A "
    "**pregnant** worker wears a **second badge under the apron at waist level**. **TLD** is the commonest type.")
mcq("Radiation-induced carcinogenesis is an example of a",
    ["Deterministic effect with a threshold", "Stochastic effect with no threshold", "Acute deterministic effect",
     "Non-radiation effect"], 1,
    "**Stochastic** effects (**cancer, heritable mutation**) have **no threshold** \u2014 **probability** rises with "
    "dose. **Deterministic** effects (erythema, epilation, **cataract**, sterility, marrow suppression) have a "
    "threshold and their **severity** rises with dose.")
mcq("The OSHA permissible exposure limit (8-h TWA) for ethylene oxide is",
    ["0.05 ppm", "1 ppm", "25 ppm", "100 ppm"], 1,
    "**EO = 1 ppm** (excursion 5 ppm/15 min). Others: **glutaraldehyde ceiling 0.05 ppm**, **formaldehyde 0.75 ppm**, "
    "**nitrous oxide 25 ppm (NIOSH)**, **halogenated volatiles 2 ppm**, **methyl methacrylate 100 ppm**.")
mcq("Under the Biomedical Waste Management Rules 2016, a used syringe with a fixed needle is discarded into a",
    ["Yellow bag", "Red bag", "White translucent puncture-proof container", "Blue container"], 2,
    "**Sharps, including syringes with fixed needles, go in the WHITE translucent puncture-proof container** "
    "\u2192 autoclaved and shredded, then encapsulated or sent to a foundry. **Red** = recyclable plastics (syringes "
    "**without** needles); **Yellow** = anatomical, soiled, expired drugs, cytotoxics; **Blue** = glass and metallic "
    "implants.")

h2("H \u2014 Post-Operative Patient Care")
mcq("Which of the following is NOT a component of the modified Aldrete score?",
    ["Respiration", "Circulation", "Pain", "Oxygen saturation"], 2,
    "The modified Aldrete score assesses **Activity, Respiration, Circulation, Consciousness and Oxygen saturation "
    "(A-R-C-C-O)**, each 0\u20132, maximum 10, **discharge \u2265 9**. **Pain and nausea belong to the PADSS**, used "
    "for discharge home after day surgery.")
mcq("The original Aldrete score used which parameter that the modified score replaced with pulse oximetry?",
    ["Temperature", "Skin colour", "Urine output", "Bowel sounds"], 1,
    "The 1970 score used **skin colour**; the modified score substituted **SpO\u2082**, which is objective and more "
    "sensitive.")
mcq("The commonest cause of upper airway obstruction in the immediate post-anaesthesia period is",
    ["Laryngospasm", "The tongue falling back against the posterior pharynx", "Bronchospasm",
     "Vocal cord paralysis"], 1,
    "Loss of pharyngeal tone in the sedated supine patient lets the **tongue fall backwards** \u2014 recognised by "
    "**snoring and see-saw (paradoxical) chest movement**. Treat with **jaw thrust or head tilt\u2013chin lift, "
    "lateral position, suction and an airway**.")
mcq("The commonest post-operative pulmonary complication is",
    ["Pneumonia", "Atelectasis", "Pulmonary embolism", "Pneumothorax"], 1,
    "**Atelectasis** \u2014 typically low-grade fever on **POD 1\u20132** with reduced basal breath sounds. "
    "Treatment is **deep breathing, incentive spirometry, splinted coughing, early ambulation and adequate "
    "analgesia** \u2014 not antibiotics.")
mcq("Fever on the second post-operative day is most likely due to",
    ["Wound infection", "Atelectasis", "Deep vein thrombosis", "Urinary tract infection"], 1,
    "Follow the W's in time order: **Wind (atelectasis, POD 1\u20132) \u2192 Water (UTI, POD 3\u20135) \u2192 "
    "Walking (DVT, POD 4\u20136) \u2192 Wound (SSI, POD 5\u20137) \u2192 Wonder drugs (> POD 7)**. Fever in the "
    "**first 24 h is usually not infective**.")
mcq("Fever on the sixth post-operative day with wound erythema and purulent discharge indicates",
    ["Atelectasis", "Drug fever", "Surgical site infection", "Malignant hyperthermia"], 2,
    "**SSI classically declares itself on POD 5\u20137.** Management: **open, drain and culture the wound, debride "
    "and pack for healing by secondary intention**, with culture-guided antibiotics.")
mcq("Wound dehiscence most commonly occurs on which post-operative day, and its herald sign is",
    ["POD 1\u20132; bright red bleeding", "POD 5\u201310; serosanguineous \u2018salmon-pink\u2019 discharge",
     "POD 14\u201321; purulent discharge", "POD 30; a palpable lump"], 1,
    "Dehiscence peaks at **POD 5\u201310 (classically day 7\u20138)**, when the wound has only **5\u201310 %** of its "
    "final tensile strength. The warning sign is a **sudden serosanguineous (salmon-pink) discharge** with a palpable "
    "gap.")
mcq("The correct immediate action for post-operative wound evisceration is to",
    ["Push the viscera back and apply a dry dressing",
     "Cover the viscera with sterile gauze soaked in warm sterile saline, position low Fowler's with knees flexed, "
     "keep nil by mouth and call the surgeon",
     "Sit the patient upright and give oral fluids", "Apply a tight binder and discharge"], 1,
    "**Never replace the viscera and never use dry gauze.** Cover with **warm sterile saline-moistened gauze**, "
    "position supine/low Fowler's with knees flexed to reduce tension, keep **nil by mouth**, secure IV access, "
    "monitor for shock and **prepare for immediate theatre**.")
mcq("Sutures on the face are typically removed on day",
    ["3\u20135", "7\u201310", "10\u201314", "14\u201321"], 0,
    "**Face and neck 3\u20135 days** (rich blood supply, cosmesis); scalp and trunk **7\u201310**; limbs "
    "**10\u201314**; joints, back, palms and soles **14 days**.")
mcq("Post-operative return of bowel function occurs in which order?",
    ["Colon \u2192 stomach \u2192 small bowel", "Small bowel \u2192 stomach \u2192 colon",
     "Stomach \u2192 colon \u2192 small bowel", "All simultaneously at 72 hours"], 1,
    "**Small intestine \u2248 24 h \u2192 stomach 24\u201348 h \u2192 COLON 48\u201372 h (last to recover).** "
    "Resolution is judged by the **passage of flatus or stool**, not bowel sounds.")
mcq("Which is a CLOSED active suction drain?",
    ["Penrose drain", "Corrugated drain", "Jackson-Pratt drain", "Open sump drain"], 2,
    "**Jackson-Pratt (bulb)** and **Hemovac/Redivac (spring or high vacuum)** are **closed active** systems with a "
    "lower infection risk; **Penrose and corrugated drains are passive and open**. A fully re-expanded JP bulb means "
    "suction has been lost \u2014 re-compress it after emptying.")
mcq("According to the Apfel score, which is NOT a risk factor for PONV?",
    ["Female sex", "Non-smoking status", "Smoking", "Expected post-operative opioid use"], 2,
    "The four Apfel factors are **female sex, non-smoker, previous PONV or motion sickness, and expected "
    "post-operative opioid use** \u2014 giving \u2248 **10/20/40/60/80 %** risk for 0\u20134 factors. "
    "**Smoking is protective.**")
mcq("Secondary haemorrhage after surgery classically occurs on which day, and why?",
    ["Day 0; slipped ligature", "Within 24 h; clot dislodged as blood pressure rises",
     "POD 7\u201314; infection eroding a vessel wall", "POD 30; false aneurysm"], 2,
    "**Primary** = during surgery; **reactionary** = within 24 h (slipped ligature or clot dislodged as BP rises and "
    "vasoconstriction wears off); **secondary = POD 7\u201314 from infection eroding the vessel wall**.")

# ============================================================ 18
h1("18.  Rapid Revision")
h2("Mnemonics")
table(["Mnemonic", "Stands for"],
      [["**2 \u2013 4 \u2013 6 \u2013 8**", "Fasting: clear fluids 2 h, breast milk 4 h, formula/light meal 6 h, "
                                           "fatty meal 8 h"],
       ["**Sign In \u2013 Time Out \u2013 Sign Out**", "The 3 phases of the WHO Surgical Safety Checklist"],
       ["**PADDING**", "Positioning: **P**ressure points padded, **A**lignment, **D**ignity, **D**evices ready, "
                       "**I**V lines protected, **N**erves free, **G**entle movement"],
       ["**Critical \u2013 Semi-critical \u2013 Non-critical**", "Spaulding: sterilize \u2013 high-level disinfect "
                                                                "\u2013 low-level disinfect"],
       ["**Geo = Steam ; Atro = Air & EO**", "**Geo**bacillus stearothermophilus \u2192 **steam** and plasma; "
                                             "Bacillus **atro**phaeus \u2192 dry heat (air) and **E**thylene oxide"],
       ["**R \u2013 A \u2013 C \u2013 E**", "Fire: **R**escue, **A**larm, **C**onfine, **E**xtinguish/Evacuate"],
       ["**P \u2013 A \u2013 S \u2013 S**", "Extinguisher: **P**ull, **A**im at the base, **S**queeze, **S**weep"],
       ["**R \u2013 P \u2013 M**", "START triage: **R**espiration, **P**erfusion, **M**ental status"],
       ["**4 H's & 4 T's**", "Reversible causes of arrest: Hypoxia, Hypovolaemia, Hypo/Hyperkalaemia-metabolic, "
                             "Hypothermia; Tension pneumothorax, Tamponade, Toxins, Thrombosis"],
       ["**4 D's**", "Negligence: **D**uty, **D**ereliction, **D**irect causation, **D**amage"],
       ["**A \u2013 R \u2013 C \u2013 C \u2013 O**", "Aldrete: **A**ctivity, **R**espiration, **C**irculation, "
                                                    "**C**onsciousness, **O**xygen saturation \u2014 max 10, "
                                                    "discharge \u2265 9"],
       ["**Wind \u2013 Water \u2013 Walking \u2013 Wound \u2013 Wonder drugs**",
        "Post-op fever by day: 1\u20132 \u2192 3\u20135 \u2192 4\u20136 \u2192 5\u20137 \u2192 > 7"],
       ["**Time \u2013 Distance \u2013 Shielding**", "Radiation protection, under ALARA"],
       ["**Yellow burns \u2022 Red recycles \u2022 White is sharp \u2022 Blue is glass**", "Biomedical waste colours"],
       ["**\u2018Only what is documented is a legal fact\u2019**", "Perioperative documentation"],
       ["**\u2018When in doubt, throw it out\u2019**", "Doubtful sterility = unsterile"],
       ["**\u2018The treatment of pus is drainage\u2019**", "Surgical site infection"]],
      widths=[5.4, 13.6])
h2("The 25 statements most likely to be a one-mark question")
numbered([
    "The **circulator** keeps the legal record of the count and is the **patient's advocate**.",
    "**At least two identifiers**, and the patient **states** their own name.",
    "The site is marked by the **operating surgeon** with an **indelible marker**, with the patient participating.",
    "The **time out** is **after induction, before skin incision**; the WHO checklist has **3 phases**.",
    "**Hearing is the last sense to be lost** \u2014 silence during induction.",
    "The **safety strap across the mid-thighs** is the key measure against a fall from the table.",
    "**Ulnar nerve** \u2014 commonest peri-operative nerve injury; **common peroneal** in lithotomy (**foot drop**).",
    "**Trendelenburg raises ICP and IOP and lowers FRC**; **Kraske/jackknife is a PRONE modification**.",
    "**Never move an anaesthetised patient without the anaesthetist's permission.**",
    "The patient's **skin must never touch metal** when the ESU is in use (alternate-site burn), and the "
    "**pencil stays in its holster**.",
    "ESU works at **300 kHz\u20133 MHz**; **bipolar needs no pad** and is safest with a pacemaker; "
    "**coag = interrupted high voltage**.",
    "**Autoclave 121 \u00b0C / 15 psi / 15\u201320 min**; **hot air oven 160 \u00b0C / 2 h**; "
    "**flash 132 \u00b0C / 3 min**.",
    "**Bowie-Dick tests air removal**; the **biological indicator is the only proof of sterilizing efficacy**; "
    "**SAL = 10\u207b\u2076**.",
    "**EO requires aeration**; **plasma cannot be used for cellulose**; **glutaraldehyde 10 h sterilizes**.",
    "**HEPA = 99.97 % at 0.3 \u00b5m**; the OR is **positive** pressure with **\u2265 15 air changes/hour**.",
    "**Hand hygiene is the single most effective measure** against healthcare-associated infection.",
    "A **draped table is sterile only at table-top level**; the wrapper edge (**1 inch**) is unsterile; "
    "**moisture = contamination**.",
    "**X-ray-detectable sponges are never used as dressings**; **nothing leaves the OR until the final count is "
    "correct**.",
    "**MH: volatile agents + succinylcholine; dantrolene 2.5 mg/kg; earliest sign is rising EtCO\u2082.**",
    "**Anaphylaxis: adrenaline 0.5 mg IM 1:1000**; **latex reactions are delayed 20\u201360 min**.",
    "The commonest **ignition** source of OR fires is the **ESU**; the commonest **fuel** is **alcohol prep**; "
    "**CO\u2082 for electrical fires**.",
    "**Aldrete \u2265 9** to leave PACU; **PADSS \u2265 9** to go home; **pain is in PADSS, not Aldrete**.",
    "Commonest immediate PACU emergency = **airway obstruction from the tongue**; commonest post-op pulmonary "
    "complication = **atelectasis**.",
    "**Dehiscence POD 5\u201310** with **serosanguineous discharge**; **evisceration \u2192 warm sterile "
    "saline-soaked gauze and call the surgeon**.",
    "**Radiation: 20 mSv/year; doubling the distance quarters exposure; the dosimeter goes OUTSIDE the apron.**",
])

closing("End of exam-focused notes  \u2022  Revise the PDF for the Chapter 1\u20133 core text, "
        "and these 18 sections for every gap.")
footer("Exam-Focused Supplementary Notes \u2014 Perioperative Patient Care & OT Safety")
save("/projects/sandbox/DeepFocus/Perioperative_Care_Notes_EXAM_FOCUSED.docx")
