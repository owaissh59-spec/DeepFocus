# -*- coding: utf-8 -*-
"""Part V — Chapter 9: Preparation of indents"""


def chapter9(b):
    b.part('PART V', 'Indents')
    b.chapter(9, 'Preparation of Indents',
              'Definition \u2022 types \u2022 indenting authority \u2022 contents of the form '
              '\u2022 step-by-step preparation \u2022 quantity calculation \u2022 emergency purchase')

    b.lead('An indent is the written demand that starts every purchase and every issue. The '
           'examiner\u2019s question "preparation of indents" has three parts: *what an indent is, '
           'what it must contain, and how the quantity is worked out*. The third part is where '
           'marks are won.')

    # ------------------------------------------------------------------ 9.1
    b.h2('9.1', 'Indent — Definition and Related Terms')
    b.box('def', 'INDENT',
          'An **indent** is a **formal written requisition** by which a store or a user department '
          '**demands the supply of specified materials, in specified quantities, from a specified '
          'source** \u2014 either from the purchase section (*external indent*, leading to a '
          'purchase) or from the main store (*internal indent*, leading to an issue).')
    b.table(['Term', 'Meaning', 'Who raises it', 'On whom'],
            [['**Indent / requisition (internal)**', 'Demand for issue of material already in stock',
              'Ward, OT, dispensary, sub-store', 'Main store'],
             ['**Indent / purchase requisition (external)**', 'Demand to **buy** material',
              'Main store / user department', 'Purchase section'],
             ['**Purchase Order (PO)**', 'The actual **order/contract to supply**',
              'Purchase section', 'The supplier'],
             ['**Issue voucher**', 'Document by which the store **hands over** the material',
              'Main store', '(given to the indenting department)'],
             ['**Bill of materials**', 'Pre-printed list of all items needed for one procedure/kit',
              'User department', 'Store']])
    b.box('hy', 'INDENT vs PURCHASE ORDER \u2014 sure MCQ',
          'An **indent is an internal demand** (no legal obligation on anyone outside the '
          'organisation). A **purchase order is an external contract** with the supplier. '
          'The indent **precedes** the purchase order.')

    # ------------------------------------------------------------------ 9.2
    b.h2('9.2', 'Indenting Authority and Financial Powers')
    b.bullets([
        'Only the **authorised indenting officer** (e.g. Head of the department, Ward Sister/Nursing '
        'In-charge, Chief Pharmacist, Store Officer) may sign an indent; a **specimen signature '
        'list** is kept in the store.',
        'The store must **refuse** an indent signed by an unauthorised person or exceeding the '
        'delegated **financial powers**.',
        'Indents involving purchase need **technical scrutiny** (is the item in the formulary? is '
        'the specification correct?) and **financial sanction** (is budget available under the '
        'correct head?).',
        'Indents for **narcotics, Schedule X drugs, spirit and costly items** require the '
        'countersignature of a senior/designated officer.',
        'A **budget certificate** ("funds are available under head ___") is usually recorded on the '
        'indent before it is processed.',
    ])

    # ------------------------------------------------------------------ 9.3
    b.h2('9.3', 'Types of Indents')
    b.table(['Type of indent', 'Purpose / features'],
            [['**Regular / routine / periodic indent**',
              'Raised at fixed intervals (weekly, monthly, quarterly) for items in regular use; the '
              'backbone of supply'],
             ['**Annual / bulk indent**',
              'Consolidated yearly demand used for annual tendering or rate contracts; based on '
              'last year\u2019s consumption plus growth'],
             ['**Emergency / urgent indent**',
              'For a life-saving or suddenly needed item; processed out of turn, often leading to '
              '**local/spot purchase**; must state the reason for urgency and be signed by a '
              'senior officer'],
             ['**Special / non-stock indent**',
              'For an item **not normally stocked** (a new drug, a special implant, a named-patient '
              'drug); needs approval of the PTC/competent authority'],
             ['**Standing indent**',
              'One indent covering supplies for a whole period, drawn in instalments as needed'],
             ['**Imprest / top-up indent**',
              'Sub-store/ward indent for only the quantity consumed, to restore the fixed imprest scale'],
             ['**Capital / equipment indent**',
              'For non-consumable (dead stock) items; needs capital budget sanction and technical '
              'specification committee approval'],
             ['**Transfer indent**',
              'Demand on another institution/store for transfer of surplus or urgently needed stock'],
             ['**Supplementary / additional indent**',
              'Raised when the quantity already indented proves insufficient before the next cycle'],
             ['**Local purchase (LP) indent**',
              'Purchase from the local market within delegated powers, when the item is out of '
              'stock/rate contract and urgently needed']])

    # ------------------------------------------------------------------ 9.4
    b.h2('9.4', 'Contents (Columns) of an Indent Form')
    b.table(['Group', 'Columns / particulars'],
            [['Identification', '**Indent number and date**; name of the indenting department/'
              'institution; period for which the demand is made; type (routine/emergency)'],
             ['Item description', 'Sl. no.; **store code number**; **full description with generic '
              'name, strength, dosage form and pack size**; specification/standard (IP/BP/USP); '
              'unit of issue'],
             ['Requirement data', '**Quantity required**; **average monthly/annual consumption**; '
              '**stock in hand (balance as per bin card)**; **quantity already on order (dues-in)**; '
              'period of cover required'],
             ['Justification', 'Purpose/patient load; reason for urgency; reason for any deviation '
              'from the previous pattern; whether the item is in the **hospital formulary/NLEM**'],
             ['Financial data', 'Last purchase rate; estimated value; **budget head and balance of '
                                'funds**; rate contract number if any'],
             ['Office use', 'Quantity sanctioned ("passed for"); reduction with reasons; ledger '
              'folio/bin card reference; issue voucher no. or PO no.; date of supply'],
             ['Signatures', '**Indenting officer** (with name, designation, date) \u2022 verifying/'
              'scrutinising officer \u2022 **sanctioning authority** \u2022 store keeper who issues '
              '\u2022 receiver']])
    b.h3('9.4.1  Specimen format — Indent / Requisition')
    b.table(['Sl.', 'Code No.', 'Item, strength & dosage form', 'Unit', 'Avg. monthly consumption',
             'Stock in hand', 'On order', 'Qty indented', 'Qty sanctioned', 'Remarks'],
            [['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', '', '']],
            size=8, first_col_bold=False, min_cm=1.0,
            caption='Format 9.1  Indent form (header: indent no. & date, department, period; '
                    'footer: signatures of indenting officer, scrutinising officer and '
                    'sanctioning authority)')

    # ------------------------------------------------------------------ 9.5
    b.h2('9.5', 'Step-by-Step Procedure for Preparing an Indent')
    b.steps([
        '**Identify the need.** Either the balance on the bin card has touched the **re-order '
        'level**, or the periodic indenting date has arrived, or a user department has demanded an '
        'item, or a new drug has been approved by the PTC.',
        '**Take out the consumption data.** From the stock ledger/consumption register, extract the '
        'issues of the last 6\u201312 months and compute the **average monthly consumption (AMC)**. '
        'Ignore abnormal months (epidemic, camp) or note them separately.',
        '**Ascertain the present stock in hand** \u2014 physically verify it; do not rely on the '
        'ledger alone. Deduct any quantity that is **near expiry, quarantined, damaged or '
        'reserved**, because it is not really usable.',
        '**Ascertain the quantity already on order (dues-in)** from the pending-order register. '
        '*Failure to deduct dues-in is the commonest cause of double ordering.*',
        '**Fix the period of cover** (how many months the supply should last) in the light of the '
        '**lead time**, budget release pattern, shelf life, storage space and cold-chain capacity.',
        '**Compute the quantity to be indented** using the formula in 9.6, then **round it off to a '
        'convenient pack/multiple** (you cannot indent 1,013 tablets if the pack is 10 \u00D7 10).',
        '**Cap the quantity by shelf life.** Never indent more than can be consumed well before '
        'expiry; for short-shelf-life items (vaccines, sera, some antibiotics) indent small '
        'quantities more often.',
        '**Check the specification and unit.** Write the **generic name, strength, dosage form, '
        'pack size and pharmacopoeial standard**; never indent by brand name alone in government '
        'purchase; state the unit of issue unambiguously.',
        '**Check the formulary/NLEM status and the code number**; indent only approved items, and '
        'quote the correct store code.',
        '**Check budget availability** under the correct head and record the funds certificate; '
        'obtain the rate contract reference and the last purchase rate for costing.',
        '**Fill the indent form**, number it serially and enter it in the **indent register**.',
        '**Obtain signatures** \u2014 the indenting officer signs, the scrutinising officer verifies '
        'consumption and stock figures, and the competent authority **sanctions** the quantity.',
        '**Despatch** the indent to the purchase section (external) or to the main store (internal) '
        'and retain the office copy.',
        '**Follow up** \u2014 watch the dues-in register, send reminders, and on receipt verify that '
        'the supply matches the indent; record any short supply for the next indent.',
    ])
    b.flow(['Re-order level reached', 'Consumption data', 'Stock in hand',
            'Less dues-in', 'Compute quantity', 'Round off to pack',
            'Sanction', 'Indent register', 'Despatch', 'Follow-up'])

    # ------------------------------------------------------------------ 9.6
    b.h2('9.6', 'Calculation of the Indent Quantity')
    b.box('formula', 'THE WORKING FORMULA',
          '**Quantity to be indented = (Average monthly consumption \u00D7 [Period of cover + '
          'Lead time in months]) + Safety (buffer) stock \u2212 Stock in hand \u2212 Quantity '
          'already on order**')
    b.p('Some manuals write the same thing as: **Indent quantity = Maximum stock level \u2212 '
        '(Stock in hand + Dues-in)**, where the maximum level already contains the lead-time '
        'consumption and the buffer.')
    b.h3('9.6.1  Solved example 1 — a routine drug')
    b.table(['Data', 'Value'],
            [['Average monthly consumption (AMC)', '2,000 tablets'],
             ['Period of cover required', '6 months'],
             ['Lead time', '2 months'],
             ['Safety stock policy', '1 month\u2019s consumption'],
             ['Stock in hand (usable)', '3,500 tablets'],
             ['Quantity already on order (dues-in)', '1,000 tablets']])
    b.bullets([
        'Requirement for cover + lead time = 2,000 \u00D7 (6 + 2) = **16,000** tablets.',
        'Add safety stock = 2,000 \u2192 total requirement = **18,000** tablets.',
        'Deduct stock in hand and dues-in = 18,000 \u2212 3,500 \u2212 1,000 = **13,500 tablets**.',
        'Round off to the pack (10 \u00D7 10 = 100 tablets per box) \u2192 **indent 13,500 tablets '
        '(135 boxes)**.',
    ])
    b.h3('9.6.2  Solved example 2 — annual indent with growth factor')
    b.bullets([
        'Last year\u2019s consumption = 48,000 vials; expected increase in patient load = 10 %.',
        'Estimated annual requirement = 48,000 \u00D7 1.10 = **52,800** vials.',
        'Add buffer of 2 months = 52,800 \u00D7 2/12 = 8,800 \u2192 **61,600** vials.',
        'Deduct closing stock 6,000 and dues-in 4,000 \u2192 **annual indent = 51,600 vials**.',
        'If the shelf life is only 18 months, this is acceptable; if it were 9 months, the indent '
        'would be split into **two or more staggered deliveries**.',
    ])
    b.h3('9.6.3  Methods of estimating requirement')
    b.table(['Method', 'Basis', 'Remarks'],
            [['**Consumption (past usage) method**',
              'Actual issues of the past 6\u201312 months, adjusted for stock-out days, growth and '
              'seasonality',
              '**Most commonly used and most reliable** where records are good'],
             ['**Morbidity (disease pattern) method**',
              'Number of expected cases of each disease \u00D7 standard treatment schedule \u00D7 '
              'course duration',
              'Best for a **new** hospital/programme with no consumption history; needs reliable '
              'epidemiological data'],
             ['**Bed-occupancy / service-level method**',
              'Consumption per bed per day \u00D7 number of beds \u00D7 occupancy \u00D7 days',
              'Quick estimate for hospital planning'],
             ['**Budget (adjusted) method**',
              'Requirement trimmed to fit the money available, prioritised by VED/NLEM',
              'Reality in most government institutions'],
             ['**Proxy / extrapolation method**',
              'Data of a comparable institution scaled to the size of this one',
              'Rough; used when no other data exist']])
    b.box('exam', 'REMEMBER',
      'The **consumption method** uses *past issues*; the **morbidity method** uses *disease '
      'incidence and standard treatment guidelines*. For a brand-new facility with no past data, '
      'the **morbidity method** is the correct choice.')

    # ------------------------------------------------------------------ 9.7
    b.h2('9.7', 'Factors to be Considered While Indenting')
    b.table(['Factor', 'Effect on the indent'],
            [['Average consumption & trend', 'The base figure of the calculation'],
             ['Lead time and its reliability', 'Longer/erratic lead time \u2192 larger buffer'],
             ['Stock in hand and dues-in', 'Deducted from the requirement'],
             ['**Shelf life / expiry**', 'Caps the maximum quantity; short-life items indented '
              'frequently in small lots'],
             ['Storage space & cold-chain capacity', 'You cannot indent what you cannot store'],
             ['Budget provision and its release pattern', 'Determines both quantity and timing'],
             ['Pack size and unit of issue', 'Quantity rounded to full packs'],
             ['ABC / VED status of the item', 'Vital items get generous buffer; C items bulk-ordered'],
             ['Seasonality and epidemics', 'ORS, antimalarials, antivenom, vaccines'],
             ['Change in prescribing pattern / formulary revision',
              'A discarded drug must not be re-indented'],
             ['Quantity discounts and rate contracts', 'May justify a larger order'],
             ['Statutory restrictions', 'Narcotics/Schedule X quantities limited by permit'],
             ['New schemes, camps, programmes', 'Additional demand to be added separately'],
             ['Supplier reliability / past short supply', 'Larger buffer or split ordering'],
             ['Price trend', 'Rising prices may justify earlier/bulk purchase (within shelf life)']])

    # ------------------------------------------------------------------ 9.8
    b.h2('9.8', 'Scrutiny, Sanction and the Indent Register')
    b.h3('9.8.1  Points checked while scrutinising an indent')
    b.bullets([
        'Is the indent on the **prescribed form**, serially numbered, dated and **signed by an '
        'authorised officer**?',
        'Is the item **in the formulary/NLEM** and is the **code number** correct?',
        'Is the **specification complete** (generic name, strength, dosage form, pack, '
        'pharmacopoeial standard)?',
        'Are the **consumption, stock-in-hand and dues-in figures correct** (verified against the '
        'ledger and bin card)?',
        'Is the **quantity reasonable** in relation to consumption, shelf life, storage space and '
        'budget?',
        'Is the **budget head correct** and are funds available?',
        'Is there any **duplication** with an earlier indent still pending?',
        'For an emergency indent \u2014 is the **reason for urgency recorded** and approved?',
        'For a non-stock/new item \u2014 is the **PTC/competent authority approval** attached?',
    ])
    b.h3('9.8.2  Indent register')
    b.table(['Sl. No.', 'Date', 'Indenting dept.', 'Item(s)', 'Qty indented', 'Qty sanctioned',
             'Issue voucher / PO No.', 'Date of supply', 'Remarks'],
            [['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '']],
            size=8, first_col_bold=False, min_cm=1.1,
            caption='Format 9.2  Indent register')

    # ------------------------------------------------------------------ 9.9
    b.h2('9.9', 'Common Mistakes and Precautions in Indenting')
    b.table(['Mistake', 'Consequence', 'Precaution'],
            [['Dues-in not deducted', 'Double supply, over-stocking, expiry',
              'Consult the pending-order register every time'],
             ['Stock in hand taken from the ledger without physical check',
              'Wrong quantity indented', 'Verify the shelf physically'],
             ['Near-expiry stock counted as usable stock', 'Stock-out despite "stock in hand"',
              'Deduct near-expiry, quarantined and damaged stock'],
             ['Indenting by brand name only', 'Restricts competition; audit objection',
              'Indent by **generic name + strength + dosage form + IP standard**'],
             ['Unit of issue not stated / ambiguous ("1 bottle")',
              'Wrong quantity supplied (10 ml vs 100 ml)', 'State the exact unit and pack size'],
             ['Over-indenting to be "safe"', 'Blocked capital, expiry loss, shortage of space',
              'Base the quantity on AMC, lead time and shelf life'],
             ['Under-indenting / indenting late', 'Stock-out, costly emergency purchase',
              'Indent when the **re-order level** is reached, not when stock is exhausted'],
             ['Ignoring shelf life', 'Expiry of large quantities', 'Cap by shelf life; stagger deliveries'],
             ['Ignoring seasonality/epidemic', 'Shortage at the peak', 'Study last year\u2019s '
              'month-wise consumption'],
             ['All emergency indents', 'Loss of tender discount, audit objection',
              'Plan routine indents properly; emergency route only for genuine emergencies'],
             ['Indent not signed / signed by unauthorised person', 'Indent invalid; supply irregular',
              'Maintain a specimen-signature list']])

    # ------------------------------------------------------------------ 9.10
    b.h2('9.10', 'Emergency and Local Purchase')
    b.steps([
        'The item is found **out of stock or insufficient**, and the need is **immediate and '
        'life-saving**.',
        'The pharmacist records the **non-availability** (from the stock register) and certifies '
        'that the item is **not available on rate contract / from the main store**.',
        'An **emergency indent** is prepared stating the reason for urgency and the quantity for the '
        'shortest reasonable period (usually a few days to a month).',
        'Sanction of the officer having **delegated financial powers for local purchase** is obtained.',
        'Quotations are obtained from **local licensed dealers** (at least 2\u20133 wherever '
        'possible) or purchase is made from the nearest approved chemist.',
        'The material is received, **checked for batch, expiry and MRP**, entered in the stock '
        'register and issued.',
        'The **cash memo/bill**, sanction order and certificate of urgency are filed together for '
        'audit.',
        'The event is analysed: *why did the stock-out happen?* \u2014 and the routine indent is '
        'corrected so that it does not recur.',
    ])
    b.box('caution', 'WHY EMERGENCY PURCHASE IS DISCOURAGED',
          bullets=['Price is higher (no competitive tender, no bulk discount).',
                   'Quality assurance is weaker (no pre-despatch testing).',
                   'Heavy paper work and audit scrutiny.',
                   'It is evidence of **failure of indenting and inventory control** \u2014 '
                   'a high proportion of emergency purchases is a recognised indicator of poor '
                   'store management.'])

    # ------------------------------------------------------------------ 9.11
    b.h2('9.11', 'From Indent to Issue — The Complete Internal Cycle')
    b.flow(['Ward indent', 'Scrutiny in main store', 'Sanction', 'Issue voucher',
            'FEFO picking', 'Receiver signs', 'Bin card & ledger posted',
            'Ward register posted', 'Consumption data', 'Next indent'])
    b.table(['Stage', 'Document created', 'Record posted'],
            [['Ward raises demand', 'Indent (2 copies)', 'Indent register'],
             ['Store sanctions', 'Sanction noted on the indent', 'Indent register'],
             ['Store issues', 'Issue voucher', 'Bin card, stock ledger, batch/expiry register'],
             ['Ward receives', 'Signature on the issue voucher',
              'Ward/sub-store stock register (imprest)'],
             ['Ward consumes', 'Ward consumption sheet / patient records',
              'Ward register, patient charge sheet'],
             ['Unused material returned', 'Material Return Note', 'Stock ledger (receipt entry)'],
             ['Month end', 'Consumption statement', 'Monthly consumption register, MIS report']])
    b.box('hy', 'CHAPTER 9 IN ONE BOX',
          bullets=['Indent = **internal written demand**; PO = **external contract**.',
                   'Types: routine, annual/bulk, emergency, special/non-stock, standing, imprest, '
                   'capital, transfer, supplementary, local purchase.',
                   '**Quantity = AMC \u00D7 (cover + lead time) + buffer \u2212 stock in hand '
                   '\u2212 dues-in**, rounded to pack size and capped by shelf life.',
                   'Estimation methods: **consumption** (past issues) and **morbidity** (disease '
                   'pattern + standard treatment).',
                   'Indent when the **re-order level** is reached \u2014 never after the stock is '
                   'exhausted.',
                   'Always deduct **dues-in**; always verify **stock physically**; always indent by '
                   '**generic name with strength, dosage form and pack**.'])
    b.page_break()
