# -*- coding: utf-8 -*-
"""Part IV — Chapter 7 (stock books) & Chapter 8 (inventory control)"""


def chapter7(b):
    b.part('PART IV', 'Stock Books & Inventory Control')
    b.chapter(7, 'Keeping of Stock Books',
              'Stock register \u2022 bin card \u2022 stock ledger \u2022 kardex \u2022 posting rules '
              '\u2022 types of stock books \u2022 verification \u2022 valuation')

    b.lead('"Keeping of stock books" is the examiner\u2019s way of asking: *which books, what columns, '
           'who posts them, how are they posted, and how are they proved correct?* Answer in that '
           'order and nothing can be missed.')

    # ------------------------------------------------------------------ 7.1
    b.h2('7.1', 'Stock Book — Meaning and Necessity')
    b.box('def', 'STOCK BOOK',
          'A **stock book (stock register)** is the **permanent, bound book of account of materials** '
          'in which, for every item separately, the **opening balance, all receipts, all issues and '
          'the resulting balance** are recorded in chronological order, with a reference to the '
          'voucher authorising each transaction.')
    b.bullets([
        'It is the **quantitative account** of stores — the equivalent of a cash book for money.',
        'It is maintained **item-wise (one folio/page per item)**, not date-wise.',
        'For drugs it must also carry **batch number and expiry date**, because two units of the '
        'same drug are not interchangeable if their batches differ.',
        'It is a **legally inspectable document** — a Drug Inspector, auditor or accreditation '
        'assessor may demand it at any time.',
        'The **closing balance of the stock book must equal the physical stock on the shelf** at '
        'every moment; that equality is the whole purpose of the book.',
    ])
    b.box('formula', 'THE STOCK BOOK EQUATION',
          '**Closing balance = Opening balance + Total receipts \u2212 Total issues \u2212 '
          'Losses/write-offs + Returns received back**')

    # ------------------------------------------------------------------ 7.2
    b.h2('7.2', 'Bin Card (Stock Card / Bin Tag)')
    b.box('def', 'BIN CARD',
          'A **bin card** is a card (or tag) **attached to the bin, rack or shelf** in which the '
          'material is kept, on which the **store keeper records, at the time of every transaction, '
          'the quantity received, the quantity issued and the resulting balance** of that item.')
    b.h3('7.2.1  Contents of a bin card')
    b.table(['Part of the card', 'Particulars'],
            [['Heading (fixed information)', 'Name & full description of the item \u2022 '
              '**store code number** \u2022 unit of issue \u2022 bin/rack/shelf number \u2022 '
              'storage condition \u2022 **minimum, maximum and re-order levels** \u2022 lead time'],
             ['Body (transaction columns)', 'Date \u2022 reference/voucher number (GRN no. or issue '
              'voucher no.) \u2022 **quantity received** \u2022 **quantity issued** \u2022 '
              '**balance** \u2022 batch number \u2022 expiry date \u2022 initials of the store keeper'],
             ['Foot / remarks', 'Date of physical verification and verifier\u2019s initials; '
              'remarks on shortage, breakage, near expiry']])
    b.table(['Date', 'GRN / Issue Voucher No.', 'Batch No.', 'Expiry', 'Received', 'Issued',
             'Balance', 'Initials'],
            [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '']],
            size=8, first_col_bold=False, min_cm=1.2,
            caption='Format 7.1  Bin card (heading carries item, code, unit, bin no., min/max/'
                    're-order levels)')
    b.h3('7.2.2  Advantages of a bin card')
    b.bullets([
        'The **balance is available at the point of storage**, without going to the office.',
        'Acts as a **ready check at the time of issue** — physical count can be compared instantly.',
        'Shows **minimum, maximum and re-order levels**, so the need to indent is noticed '
        'automatically.',
        'Provides an **independent second record** which, when tallied with the stock ledger, '
        'detects errors and fraud (**two-point recording**).',
        'Helps the stock verifier to compare book and ground balance on the spot.',
        'Simple, cheap and needs no accounting knowledge.',
    ])
    b.h3('7.2.3  Limitations')
    b.bullets([
        'Shows **quantity only** (no value), so it cannot be used for costing.',
        'Cards can be **soiled, torn, lost or manipulated** as they lie in the open store.',
        'Many cards mean **repetitive writing**; errors of posting are possible.',
        'Does not show the **outstanding orders** unless a special column is provided.',
    ])

    # ------------------------------------------------------------------ 7.3
    b.h2('7.3', 'Stock Ledger (Stores Ledger)')
    b.box('def', 'STORES LEDGER',
          'The **stores (stock) ledger** is the book maintained **in the store office / accounts '
          'section**, one folio per item, in which every receipt and issue is posted **from the '
          'vouchers (GRN, issue voucher, transfer voucher)**, showing quantity and \u2014 in a '
          '**priced stores ledger** \u2014 also rate and value of receipts, issues and closing balance.')
    b.table(['Group of columns', 'Particulars'],
            [['Item identification', 'Name, code number, unit, folio number, storage condition, '
              'min/max/re-order level'],
             ['Receipts', 'Date \u2022 GRN no. \u2022 supplier \u2022 PO no. \u2022 batch \u2022 '
              'expiry \u2022 quantity \u2022 rate \u2022 value'],
             ['Issues', 'Date \u2022 issue voucher no. \u2022 indenting department \u2022 batch '
              '\u2022 quantity \u2022 rate \u2022 value'],
             ['Balance', 'Quantity \u2022 rate \u2022 value \u2022 (and in some formats, quantity on '
              'order = dues-in)'],
             ['Verification', 'Date of physical verification, ground balance found, discrepancy, '
              'signature']])
    b.h3('7.3.1  Bin card vs Stores ledger — the classic comparison')
    b.table(['Point of difference', '**Bin card**', '**Stores ledger**'],
            [['Where kept', 'With the material, on/near the bin', 'In the store office / accounts section'],
             ['Who posts it', '**Store keeper**', '**Ledger clerk / accounts clerk**'],
             ['When posted', '**At the time of the transaction** (immediately)',
              'Later, from the vouchers (may be a day or two behind)'],
             ['What it records', '**Quantity only**', 'Quantity **and value** (priced ledger)'],
             ['Basis of entry', 'The physical movement of material itself',
              'The **document/voucher** evidencing the movement'],
             ['Form', 'A loose card or tag', 'A bound register or a set of ledger folios/computer records'],
             ['Individual transactions', 'Each transaction posted separately',
              'Transactions may be posted in summary'],
             ['Main use', 'Physical control, ready reference at the bin, re-ordering',
              'Accounting, costing, valuation, MIS'],
             ['Legal/audit standing', 'Working record', '**Primary book of account for audit**']])
    b.box('exam', 'REMEMBER THE THREE-WORD ANSWERS',
          '*Bin card* \u2192 **store keeper, quantity, at the bin**. *Stores ledger* \u2192 '
          '**ledger clerk, quantity + value, in the office**. Both must be **reconciled '
          'periodically**; a difference means an unposted or wrongly posted voucher.')

    # ------------------------------------------------------------------ 7.4
    b.h2('7.4', 'Kardex, Two-Bin and Location Systems')
    b.kv([
        ('Kardex / visible index card system', 'Cards for all items kept in a **shallow tray or '
                                              'vertical cabinet so that the top line (item name, '
                                              'code and balance) of every card is visible at a '
                                              'glance**; coloured signal clips are attached when '
                                              'stock reaches the re-order level. Excellent for '
                                              'quick review of many items.'),
        ('Two-bin system', 'The stock of an item is kept in **two bins**. Issues are made from the '
                           'first bin; **the moment the first bin is empty, an order is placed**, '
                           'and the second bin (which holds the re-order quantity + safety stock) '
                           'carries the store through the lead time. Simple, visual, needs little '
                           'paper work; suited to **low-value C-class items**.'),
        ('Fixed location system', 'Every item has a **permanent bin address**; easy to memorise and '
                                  'to locate, but space lies idle when the item is out of stock.'),
        ('Random / floating location system', 'An item is placed **wherever space is available** and '
                                             'the location is recorded in the **location index / '
                                             'computer**; gives maximum space utilisation but '
                                             'depends totally on accurate records.'),
        ('Zoned / semi-fixed location', 'A **zone** is fixed for a group (e.g. all injections in '
                                        'zone C) but the exact bin within the zone is flexible — '
                                        'the practical compromise used in most hospital stores.'),
        ('Bin/location index', 'The register (or computer table) that translates **code number '
                               '\u2192 rack/shelf/bin address**; without it a random-location '
                               'store becomes unusable.'),
    ])

    # ------------------------------------------------------------------ 7.5
    b.h2('7.5', 'Rules and Procedure for Posting Stock Books')
    b.numbered([
        'Use a **bound register with machine-numbered pages**; record on the first page a '
        '**certificate of the number of pages**, signed and dated by the officer-in-charge.',
        'Allot a **separate folio (page) to each item**, writing its full description, code number '
        'and unit of issue at the top; maintain an **index of items with folio numbers** at the '
        'beginning of the register.',
        'Post **in ink, on the day of the transaction**, in chronological order.',
        'Every entry must quote its **authority** — GRN number for a receipt, issue voucher number '
        'for an issue, sanction number for a write-off.',
        'Post the **batch number and expiry date** for every drug receipt and issue.',
        'Work out the **balance after every transaction**; do not leave the balance column blank.',
        '**Total and carry forward** at the end of each page and each month; write "Carried over to '
        'page ___" and "Brought forward from page ___".',
        'A wrong entry is **scored out with a single horizontal line**, the correct figure written '
        'above it, and the correction **initialled with date** by the authorised officer. '
        '**No erasing, no overwriting, no whitener, no page torn out.**',
        'Leave **no blank lines or blank pages** between entries; cancel unused space by a diagonal line.',
        'Record **physical verification** on the folio itself: date, ground balance, discrepancy and '
        'the verifier\u2019s signature.',
        '**Reconcile bin card with ledger** at fixed intervals (weekly/monthly) and record the '
        'reconciliation.',
        'Close the register at the end of the financial year, carry the closing balances forward as '
        'the opening balances of the new register, and get them **certified**.',
    ])
    b.box('caution', 'WHAT MAKES A STOCK BOOK WORTHLESS IN AUDIT',
          bullets=['Pencil entries, erasures, overwriting, whitener.',
                   'Loose sheets, missing pages, un-numbered pages.',
                   'Entries without voucher references.',
                   'Balances not struck after each transaction.',
                   'Corrections not attested.',
                   'No record of physical verification.',
                   'Batch and expiry not recorded for drugs.'])

    # ------------------------------------------------------------------ 7.6
    b.h2('7.6', 'Types of Stock Books Maintained in a Drug Store')
    b.table(['Stock book', 'What it covers / special features'],
            [['**Drug (consumable) stock register**', 'All medicines; item-wise folios with batch '
              'and expiry columns'],
             ['**Surgical & dressing stock register**', 'Gauze, bandages, sutures, disposables'],
             ['**Chemical / laboratory reagent register**', 'With hazard and shelf-life remarks'],
             ['**Dead stock (non-consumable / permanent) register**',
              'Equipment, instruments, furniture; columns for **identification/serial number, date '
              'of purchase, cost, warranty, location, condition and date of annual verification**; '
              'items are **never "consumed"** \u2014 they leave the register only on transfer, '
              'loss or **condemnation**'],
             ['**Narcotic / NDPS (Dangerous Drugs) register**',
              'Separate page per drug; daily balance; **kept under lock and countersigned**; '
              'entries in ink, no corrections without attestation; **stock physically tallied '
              'daily/at every shift change**'],
             ['**Schedule X register**', 'Purchase and issue of habit-forming drugs; kept for the '
              'prescribed period; prescriptions retained'],
             ['**Schedule H / H1 register**', 'Sale/issue of prescription drugs; the **H1 register** '
              'records patient name & address, prescriber, drug, quantity and date'],
             ['**Spirit / alcohol (bonded) register**', 'Receipt, issue and permissible wastage of '
              'rectified spirit under excise control'],
             ['**Batch and expiry register**', 'Batch-wise quantity and expiry date; drives **FEFO** '
              'and the near-expiry statement'],
             ['**Expiry / near-expiry register**', 'Items expiring within 3\u20136 months and action '
              'taken (redistribution, return, destruction)'],
             ['**Breakage, damage and loss register**', 'Quantity, value, cause, responsibility, '
              'write-off sanction'],
             ['**Condemnation / disposal register**', 'Board proceedings, mode of disposal, sale '
              'proceeds, destruction certificate'],
             ['**Free supply / donation / sample register**', 'Drugs received without payment'],
             ['**Temperature & humidity log**', 'Store, refrigerator, ILR and deep-freezer readings '
              'twice daily'],
             ['**Equipment maintenance & breakdown register**',
              'For refrigerators, ILRs, generators, autoclaves'],
             ['**Ward / sub-store (departmental) stock register**',
              'Imprest scale, receipts from main store, consumption, balance'],
             ['**Stock verification register**', 'Date, items verified, book vs ground balance, '
              'discrepancy, certificate']])
    b.h3('7.6.1  Consumable vs non-consumable (dead) stock')
    b.table(['Point', 'Consumable (expendable) stock', 'Non-consumable (dead/permanent) stock'],
            [['Nature', 'Used up in a single use or a short period', 'Used repeatedly over years'],
             ['Examples', 'Drugs, dressings, chemicals, stationery, X-ray film',
              'Autoclave, refrigerator, BP apparatus, furniture, surgical instruments'],
             ['Register used', 'Consumable stores register (with batch/expiry)',
              '**Dead stock register** (with identification number, cost, warranty)'],
             ['Accounting head', 'Revenue expenditure', 'Capital expenditure'],
             ['Removal from books', 'By issue/consumption', 'Only by transfer, loss or '
              '**condemnation with sanction**'],
             ['Verification', 'Perpetual + annual quantity verification',
              '**Annual physical verification of every item** with condition noted']])

    # ------------------------------------------------------------------ 7.7
    b.h2('7.7', 'Physical Verification of Stock')
    b.p('(The types \u2014 perpetual, periodic, spot, independent \u2014 were introduced in '
        'Chapter 4. Here are the points most often asked in the context of stock books.)')
    b.table(['Aspect', 'Key points'],
            [['Purpose', 'To prove that the **book balance equals the ground balance**, to detect '
              'pilferage, deterioration, expiry, wrong posting and obsolete stock'],
             ['Who should verify', 'A person **independent of the custodian**; the custodian must be '
              'present during counting'],
             ['Frequency (ABC-linked)', '**A items** \u2014 monthly/quarterly; **B items** \u2014 '
              'half-yearly; **C items** \u2014 annually. Narcotics \u2014 **daily/shift-wise tally** '
              'and surprise checks'],
             ['Method', 'Count/weigh/measure physically; do not accept the custodian\u2019s figure; '
              '"blind" verification (ground balance recorded before seeing the book balance) is ideal'],
             ['Record', '**Verification sheet**, **discrepancy (shortage/excess) statement**, and a '
              '**verification certificate** signed by verifier and custodian; note the date of '
              'verification on the bin card and ledger folio'],
             ['Discrepancy \u2014 first check', 'Unposted vouchers, wrong unit of measurement, '
              'transfers not accounted, breakage not written off, double posting, arithmetical error'],
             ['Shortage', 'Regularised by **write-off sanction** of the competent authority; '
              'recovery from the custodian if negligence is proved; criminal action for theft, and '
              'immediate reporting for narcotics'],
             ['Excess', '**Taken on charge** (credited to stock) so that it cannot be misused'],
             ['Hand-over of charge', 'On transfer of the custodian a **full physical verification** '
              'is done and a **charge (hand-over/take-over) certificate** signed by both officers']])

    # ------------------------------------------------------------------ 7.8
    b.h2('7.8', 'Valuation of Stock (Pricing of Issues)')
    b.table(['Method', 'How the issue is priced', 'Effect / remark'],
            [['**FIFO** (First In First Out)', 'Issues priced at the rate of the **oldest** stock',
              'Closing stock valued at latest (current) prices; matches the physical FIFO practice '
              'in a drug store'],
             ['**LIFO** (Last In First Out)', 'Issues priced at the rate of the **latest** purchase',
              'Closing stock valued at old prices; **not suitable for drugs** because physically '
              'the oldest stock must go out first'],
             ['**Simple average**', 'Average of the rates of the lots in stock',
              'Ignores quantity; rarely used'],
             ['**Weighted average**', '(Total value of stock) \u00F7 (total quantity in stock), '
              'recomputed after every receipt',
              'Smooths out price fluctuations; widely used in computerised systems'],
             ['**Standard price**', 'A pre-determined rate fixed for the year',
              'Simple, good for budgeting; differences go to a price-variance account'],
             ['**Market / replacement price**', 'Current market rate',
              'Used for insurance and for valuing condemned stock'],
             ['**Last purchase price**', 'Rate of the most recent purchase',
              'Simplest; commonly used in government hospital stores for valuing closing stock']])
    b.box('hy', 'FIFO vs FEFO \u2014 do not confuse',
          '**FIFO = First In, First Out** (the *oldest received* stock is issued first). '
          '**FEFO = First Expiry, First Out** (the stock with the *earliest expiry date* is issued '
          'first). For drugs, **FEFO is superior and is the recommended practice**, because a later '
          'purchase may carry an earlier expiry date.')

    # ------------------------------------------------------------------ 7.9
    b.h2('7.9', 'Performance Indicators Derived from Stock Books')
    b.table(['Indicator', 'Formula / definition', 'What it tells'],
            [['**Inventory (stock) turnover ratio**',
              'Annual consumption value \u00F7 Average inventory value held',
              'How many times the stock is used up in a year; **higher = more efficient**. Average '
              'inventory = (opening + closing) \u00F7 2'],
             ['**Months / days of stock in hand**',
              'Closing stock \u00F7 Average monthly (or daily) consumption',
              'How long the present stock will last'],
             ['**Stock-out rate**', '(No. of items out of stock \u00F7 total items) \u00D7 100, or '
              'stock-out days per item',
              'Service level of the store; should be near zero for **vital** items'],
             ['**Expiry / wastage rate**',
              '(Value of drugs expired or damaged \u00F7 total value of drugs consumed) \u00D7 100',
              'Efficiency of forecasting and FEFO discipline'],
             ['**Inventory carrying (holding) cost**',
              'Interest on capital + storage + insurance + handling + obsolescence + expiry; '
              'commonly taken as **about 20\u201325 % of the average inventory value per year**',
              'Why over-stocking is expensive'],
             ['**Lead time**', 'Time from **raising the indent** to **the material being available '
              'for issue**', 'Determines the re-order level'],
             ['**Order frequency**', 'Annual consumption \u00F7 EOQ', 'Number of orders per year'],
             ['**Fill rate**', '(Quantity issued \u00F7 quantity indented) \u00D7 100',
              'Ability of the store to satisfy demand'],
             ['**Percentage of non-moving items**',
              '(No. of items with no issue in 12 months \u00F7 total items) \u00D7 100',
              'Dead stock and obsolescence']])

    # ------------------------------------------------------------------ 7.10
    b.h2('7.10', 'Computerised Stock Keeping')
    b.table(['Aspect', 'Manual system', 'Computerised system'],
            [['Speed & effort', 'Slow; heavy writing work', 'Instant posting and retrieval'],
             ['Accuracy', 'Prone to arithmetical & posting errors',
              'Balances computed automatically'],
             ['Batch/expiry control', 'Depends on the clerk\u2019s vigilance',
              '**Automatic near-expiry alerts and FEFO enforcement**'],
             ['Re-ordering', 'Manual watch on re-order level',
              'Automatic re-order level alert and draft indent generation'],
             ['Reports/MIS', 'Prepared laboriously by hand',
              'ABC/VED analysis, consumption trends, expiry loss at a keystroke'],
             ['Security', 'Physical lock', '**User ID, password, role-based rights, audit trail**'],
             ['Risk', 'Loss/damage of registers',
              'Data loss, power/software failure \u2192 needs **daily back-up** and a manual fallback'],
             ['Legal position', 'Accepted everywhere',
              'Acceptable where rules permit; statutory registers (e.g. narcotics) may still have '
              'to be maintained/printed in physical form']])
    b.box('note', 'DATA INTEGRITY \u2014 "ALCOA"',
          'Records (paper or electronic) must be **A**ttributable, **L**egible, **C**ontemporaneous, '
          '**O**riginal and **A**ccurate. Modern additions ("ALCOA+") are **Complete, Consistent, '
          'Enduring and Available**. This principle is increasingly examined in pharmacy papers.')
    b.page_break()


def chapter8(b):
    b.chapter(8, 'Inventory Control Techniques',
              'Because an indent cannot be prepared without them \u2014 ABC, VED, FSN, HML, XYZ, '
              'SDE, GOLF, SOS \u2022 EOQ \u2022 stock levels \u2022 lead time')

    b.lead('Inventory control is the science of deciding **how much to order and when to order**. '
           'Chapter 9 (preparation of indents) is nothing but the *application* of the formulae in '
           'this chapter, so learn the formulae here thoroughly \u2014 they are pure-mark questions.')

    # ------------------------------------------------------------------ 8.1
    b.h2('8.1', 'Inventory — Meaning, Types and Costs')
    b.box('def', 'INVENTORY',
          '**Inventory** means the **stock of any item or resource held to meet a future demand** — '
          'in a hospital, the drugs, surgicals, reagents, spares and provisions lying in the main '
          'store, sub-stores and wards. **Inventory control** is the technique of maintaining stock '
          'at the **desired level** — enough to serve patients, small enough not to waste money.')
    b.h3('8.1.1  Objectives of inventory control')
    b.bullets([
        'Uninterrupted availability — **no stock-out of vital drugs**.',
        'Minimum **investment** locked up in stock.',
        'Minimum **expiry, deterioration and obsolescence** loss.',
        'Lowest total of **ordering cost + carrying cost**.',
        'Reduction in **emergency/local purchases** (which are always costlier).',
        'Optimum use of **storage space and manpower**.',
        'Reliable information for **budgeting and purchase planning**.',
    ])
    b.h3('8.1.2  Costs associated with inventory')
    b.table(['Cost', 'Components', 'Behaviour'],
            [['**Ordering (procurement) cost**', 'Tendering, correspondence, inspection, '
              'transport, bill processing \u2014 cost *per order*',
              '**Falls** as the order quantity rises (fewer orders per year)'],
             ['**Carrying (holding) cost**', 'Interest on blocked capital, rent, electricity & '
              'refrigeration, insurance, salaries, pilferage, **expiry & obsolescence**',
              '**Rises** as the order quantity rises; usually **20\u201325 % of average inventory '
              'value per annum**'],
             ['**Stock-out (shortage) cost**', 'Emergency purchase at a higher rate, patient harm, '
              'loss of reputation, loss of revenue', 'Rises as stock is cut too fine'],
             ['**Capital / opportunity cost**', 'Return foregone on the money tied up in stock',
              'Proportional to inventory value']])
    b.box('exam', 'EOQ IS THE BALANCE POINT',
          'The **Economic Order Quantity is that order size at which the total ordering cost equals '
          'the total carrying cost**, and therefore the **total inventory cost is minimum**.')

    # ------------------------------------------------------------------ 8.2
    b.h2('8.2', 'Selective Inventory Control Techniques')
    b.p('No store can control 10,000 items with equal attention. **Selective control** means '
        'applying tight control to the few items that matter most. Each technique classifies items '
        'on a *different criterion* — that criterion is what the MCQ tests.')
    b.table(['Technique', 'Criterion of classification', 'Classes and their meaning'],
            [['**ABC analysis**', '**Annual consumption VALUE** (\u2248 Pareto / 80:20 principle)',
              '**A** \u2248 10 % of items \u2192 \u2248 70 % of value; **B** \u2248 20 % of items '
              '\u2192 \u2248 20 % of value; **C** \u2248 70 % of items \u2192 \u2248 10 % of value'],
             ['**VED analysis**', '**Criticality** of the item for patient care / functioning',
              '**V** = Vital (life-saving; stock-out not permissible), **E** = Essential (serious '
              'inconvenience if out of stock), **D** = Desirable (minor effect)'],
             ['**VEN analysis**', 'Same idea, WHO terminology',
              '**V**ital, **E**ssential, **N**on-essential'],
             ['**HML analysis**', '**Unit price** of the item (not annual value)',
              '**H**igh, **M**edium, **L**ow cost per unit \u2014 used to control pilferage-prone '
              'costly items'],
             ['**XYZ analysis**', '**Value of the stock actually lying in store** (closing '
              'inventory value)',
              '**X** = high inventory value, **Y** = moderate, **Z** = low. Used at the time of '
              'physical verification to attack over-stocking'],
             ['**FSN / FSND analysis**', '**Rate of movement / consumption**',
              '**F** = Fast moving, **S** = Slow moving, **N** = Non-moving (**D** = Dead). '
              'Non-moving stock indicates obsolescence'],
             ['**SDE analysis**', '**Availability / difficulty of procurement**',
              '**S** = Scarce (long lead time, imported, short supply), **D** = Difficult, '
              '**E** = Easily available'],
             ['**GOLF analysis**', '**Source of supply**',
              '**G** = Government (e.g. from a government undertaking), **O** = Ordinary/open '
              'market, **L** = Local purchase, **F** = Foreign/imported'],
             ['**SOS analysis**', '**Seasonality** of availability',
              '**S** = Seasonal, **OS** = Off-seasonal. Applies to items whose supply or demand is '
              'seasonal (ORS, antimalarials, herbs)'],
             ['**MUSIC-3D**', 'Multi-unit selective inventory control \u2014 three dimensions',
              'Combines **cost, criticality and availability** in one framework'],
             ['**Two-bin technique**', 'Simplicity of control for cheap items',
              'Order when the first bin empties']])
    b.box('mnem', 'MNEMONICS FOR THE CRITERIA',
          bullets=['**A**BC \u2014 **A**nnual consumption value ("**A** for **A**mount").',
                   '**V**ED \u2014 **V**itality / criticality.',
                   '**H**ML \u2014 **H**igh unit price ("price per piece").',
                   '**X**YZ \u2014 value of stock in the store ("**X** for e**X**isting stock").',
                   '**F**SN \u2014 **F**requency of movement.',
                   '**S**DE \u2014 **S**carcity / ease of purchase.',
                   '**G**OLF \u2014 **G**eographical source of supply.',
                   '**S**OS \u2014 **S**eason.'])
    b.h3('8.2.1  ABC analysis — steps and use')
    b.steps([
        'List every item with its **annual consumption quantity** and **unit price**.',
        'Compute **annual consumption value = quantity \u00D7 unit price** for each item.',
        'Arrange items in **descending order of annual consumption value**.',
        'Compute the **cumulative value and cumulative percentage** of items and of value.',
        'Draw the cut-offs: roughly the first **70 %** of cumulative value = **A**, the next '
        '**20 %** = **B**, the last **10 %** = **C**.',
        'Apply **differential control**: A items \u2014 tight control, low safety stock, frequent '
        'small orders, monthly verification, senior-level approval; C items \u2014 loose control, '
        'bulk annual purchase, two-bin system, annual verification.',
    ])
    b.table(['Control parameter', 'A items', 'B items', 'C items'],
            [['Share of items / of value', '\u2248 10 % / 70 %', '\u2248 20 % / 20 %',
              '\u2248 70 % / 10 %'],
             ['Degree of control', 'Very tight', 'Moderate', 'Loose'],
             ['Safety stock', 'Low (but no stock-out of vital A items)', 'Moderate', 'High'],
             ['Ordering frequency', 'Frequent, small quantities', 'Moderate',
              'Few large orders (once or twice a year)'],
             ['Physical verification', 'Monthly / quarterly', 'Half-yearly', 'Annual'],
             ['Value analysis & negotiation', 'Rigorous', 'Moderate', 'Minimal'],
             ['Level of approval', 'Highest authority', 'Middle level', 'Store keeper level']])
    b.h3('8.2.2  Coupling ABC with VED — the practical matrix')
    b.table(['', '**V (Vital)**', '**E (Essential)**', '**D (Desirable)**'],
            [['**A (costly)**', 'Category **I**', 'Category **I**', 'Category **II**'],
             ['**B**', 'Category **I**', 'Category **II**', 'Category **III**'],
             ['**C (cheap)**', 'Category **I**', 'Category **III**', 'Category **III**']],
            first_col_bold=True,
            caption='Table 8.1  ABC\u2013VED matrix. **Category I** items get the tightest control '
                    'and the top management\u2019s attention; **Category II** moderate; '
                    '**Category III** routine control.')
    b.box('hy', 'WHY COUPLE THEM?',
          'A life-saving injection may cost only a few rupees, so pure **ABC** would put it in the '
          'careless "C" class. **VED** rescues it by calling it **Vital**. Hence *all V items, '
          'whatever their cost, are placed in Category I* and are never allowed to go out of stock.')

    # ------------------------------------------------------------------ 8.3
    b.h2('8.3', 'Economic Order Quantity (EOQ)')
    b.box('formula', 'EOQ (Wilson\u2019s formula)',
          '**EOQ = \u221A(2 \u00D7 A \u00D7 O \u00F7 C)**   where\n'
          '**A** = Annual consumption (demand) in units;  **O** = Ordering cost per order;  '
          '**C** = Carrying (holding) cost per unit per year.\n'
          'If the carrying cost is expressed as a fraction **i** of the unit price **p**, then '
          '**C = i \u00D7 p** and **EOQ = \u221A(2AO \u00F7 ip)**.')
    b.bullets([
        'At the EOQ, **total ordering cost = total carrying cost**, and the total inventory cost '
        'curve is at its **minimum** (the curve is flat near the minimum, so a small error in EOQ '
        'costs little).',
        '**Number of orders per year = A \u00F7 EOQ**;  **interval between orders = 12 \u00F7 (A/EOQ)** '
        'months.',
        '**Average inventory = EOQ \u00F7 2** (plus safety stock).',
        'EOQ **increases** if annual demand or ordering cost rises; it **decreases** if carrying '
        'cost or unit price rises. EOQ varies as the **square root** of demand — doubling the '
        'demand increases EOQ only \u221A2 (\u2248 1.41) times.',
    ])
    b.h3('8.3.1  Assumptions and limitations of EOQ')
    b.table(['Assumption', 'Why it may fail in a drug store'],
            [['Demand is known, uniform and continuous',
              'Epidemics, seasonal disease, change of prescriber preference'],
             ['Lead time is known and constant', 'Tender delays, supplier failure, transport strikes'],
             ['Price is constant (no quantity discount)',
              'Bulk discounts and rate contracts change the economics'],
             ['No stock-out is permitted', 'In practice a calculated stock-out of D items is accepted'],
             ['Ordering and carrying costs are measurable and constant',
              'Difficult to quantify in a hospital'],
             ['The item has an unlimited shelf life',
              '**Drugs expire** \u2014 so EOQ must be capped by the shelf life; this is the biggest '
              'limitation for pharmaceuticals'],
             ['Money and space are unlimited', 'Budget is released in instalments; cold-chain space '
              'is limited']])
    b.box('note', 'SOLVED EXAMPLE',
          'Annual consumption **A = 10,000** vials; ordering cost **O = \u20B9 400** per order; '
          'unit price **p = \u20B9 20**; carrying cost **i = 20 % = 0.20** \u2192 '
          '**C = 0.20 \u00D7 20 = \u20B9 4** per vial per year.\n'
          '**EOQ = \u221A(2 \u00D7 10,000 \u00D7 400 \u00F7 4) = \u221A2,000,000 \u2248 1,414 vials.**\n'
          'Number of orders per year = 10,000 \u00F7 1,414 \u2248 **7 orders**, i.e. about one order '
          'every 7\u20138 weeks.')

    # ------------------------------------------------------------------ 8.4
    b.h2('8.4', 'Stock Levels and Lead Time')
    b.h3('8.4.1  Lead time')
    b.kv([
        ('Lead time (procurement time)', 'The **total time between recognising the need (raising '
                                         'the indent) and the material becoming available for '
                                         'issue**.'),
        ('Components', '**Administrative lead time** (preparing and sanctioning the indent, '
                       'tendering, comparative statement, approval, placing the PO) + '
                       '**supplier/delivery lead time** (manufacturing and despatch) + '
                       '**transit time** + **inspection/testing and taking-on-charge time**.'),
        ('Why it matters', 'The whole purpose of the **re-order level** is to cover the consumption '
                           'during the lead time. Longer or more erratic the lead time, larger the '
                           'safety stock required.'),
    ])
    b.h3('8.4.2  The stock levels — definitions and formulae')
    b.table(['Level', 'Meaning', 'Formula'],
            [['**Safety / buffer / reserve stock**',
              'Cushion held to absorb unexpected demand or delay in supply',
              'Safety stock = (Maximum consumption rate \u2212 Average consumption rate) \u00D7 '
              'Lead time  \n*or* = Average consumption \u00D7 (Maximum lead time \u2212 Average '
              'lead time)  \n*or*, in practice, consumption of a fixed number of weeks/months'],
             ['**Re-order level (ROL) / ordering level**',
              'The balance at which a fresh order **must** be placed',
              '**ROL = (Average consumption per unit time \u00D7 Lead time) + Safety stock**  \n'
              '(*Simplified*: ROL = Maximum consumption \u00D7 Maximum lead time)'],
             ['**Minimum level**', 'The level below which stock should not normally fall (= the '
              'safety stock)',
              'Minimum = ROL \u2212 (Average consumption \u00D7 Average lead time)'],
             ['**Maximum level**', 'The highest stock that should be held, to avoid over-stocking',
              'Maximum = ROL + Re-order (order) quantity \u2212 (Minimum consumption \u00D7 '
              'Minimum lead time)'],
             ['**Danger level**', 'Level at which normal issues are stopped and **emergency '
                                  'purchase** is resorted to',
              'Danger level = Average consumption \u00D7 Emergency (minimum) lead time'],
             ['**Average stock level**', 'For valuation and carrying-cost calculation',
              'Average stock = Minimum level + \u00BD \u00D7 Re-order quantity  \n*or* = '
              '(Maximum + Minimum) \u00F7 2'],
             ['**Re-order (order) quantity**', 'How much to order each time',
              'Usually the **EOQ**, adjusted for shelf life, pack size, budget and discounts']])
    b.box('note', 'SOLVED EXAMPLE — RE-ORDER LEVEL',
          'Average consumption **500 strips/month**; lead time **2 months**; safety stock kept for '
          '**1 month** of consumption.\n'
          '**ROL = (500 \u00D7 2) + 500 = 1,500 strips.** So when the balance on the bin card falls '
          'to 1,500 strips, the indent must be raised.\n'
          'If EOQ = 3,000 strips and minimum consumption \u00D7 minimum lead time = 300 \u00D7 1 = '
          '300, then **Maximum level = 1,500 + 3,000 \u2212 300 = 4,200 strips**.')

    # ------------------------------------------------------------------ 8.5
    b.h2('8.5', 'Systems of Inventory Review and Modern Approaches')
    b.table(['System', 'How it works', 'Suitability'],
            [['**Perpetual / continuous review (Q-system, fixed order quantity)**',
              'Stock is watched continuously; when it touches the **re-order level**, a **fixed '
              'quantity (EOQ)** is ordered. Order *quantity* fixed, order *time* variable',
              'A and B items, vital drugs'],
             ['**Periodic review (P-system, fixed order interval)**',
              'Stock is reviewed at **fixed intervals** (say every quarter) and ordered up to a '
              'predetermined maximum. Order *time* fixed, *quantity* variable',
              'C items, items from the same supplier ordered together'],
             ['**Two-bin system**', 'Order placed when the first bin empties', 'Cheap C items'],
             ['**Min\u2013max system**', 'Stock kept between a fixed minimum and maximum',
              'Ward/sub-store stocks'],
             ['**Imprest / top-up system**', 'Fixed scale replenished to full at each cycle',
              'Wards, OT, emergency trolley'],
             ['**Just-in-Time (JIT)**', 'Material received exactly when needed; near-zero inventory',
              'Possible only with utterly reliable local suppliers; risky for life-saving drugs'],
             ['**Vendor Managed Inventory (VMI) / consignment stock**',
              'Supplier owns and replenishes the stock lying in the hospital; payment on consumption',
              'High-value implants, reagents, some costly injections'],
             ['**Rate contract + call-off orders**', 'No stock held; ordered as and when needed at '
              'pre-fixed rates', 'Most government hospital purchasing'],
             ['**ERP / e-procurement (DVDMS, e-Aushadhi, GeM)**',
              'Computerised demand, purchase, receipt, issue and expiry management across a state',
              'Large public health systems']])
    b.box('hy', 'FORMULA SHEET \u2014 MEMORISE THESE SEVEN',
          bullets=['**EOQ = \u221A(2AO/C)**',
                   '**ROL = (Average consumption \u00D7 Lead time) + Safety stock**',
                   '**Safety stock = (Max. consumption \u2212 Avg. consumption) \u00D7 Lead time**',
                   '**Maximum level = ROL + Order quantity \u2212 (Min. consumption \u00D7 '
                   'Min. lead time)**',
                   '**Danger level = Avg. consumption \u00D7 Emergency lead time**',
                   '**Average stock = Minimum level + \u00BD Order quantity**',
                   '**Inventory turnover ratio = Annual consumption value \u00F7 Average '
                   'inventory value**'])
    b.page_break()
