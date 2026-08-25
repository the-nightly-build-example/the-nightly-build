# Evidence: when-ai-breaks/facebook-translation-arrest (01)

The record supports the commission's core narrative and its two-part teaching.
The incident is firmly attested: in mid-October 2017 a Palestinian construction
worker posted an Arabic greeting beside a photo of himself at a bulldozer in the
West Bank settlement Beitar Illit; Facebook's automatic translation rendered it
"attack them" (Hebrew) and "hurt them" (English); Israeli police arrested him,
questioned him for a few hours with no Arabic-speaking officer reading the
original, and released him once the error was clear; Facebook apologized in a
named, quoted statement. Two anchors carry the teaching: a peer-reviewed NMT
paper (Zbib et al., NAACL-HLT 2012) that quantifies why Modern-Standard-trained
Arabic MT fails on dialect, and the automation-bias literature (Cummings; Skitka
et al. 1999) that names and measures exactly the failure the police committed.
"Where it lives today" is documented with sources I opened firsthand: machine
translation in US asylum processing (Respond Crisis Translation on CBP One) and
in Meta's own products again (the October 2023 Instagram Arabic-to-"terrorist"
mistranslation).

Two things are thin, both recorded in full below. First, the arrest narrative
essentially traces to one origin, Haaretz; the other outlets repeat it, so the
"independent corroboration" is weaker than a headcount of outlets suggests, with
one real exception (Facebook's own statement, and police context, carried by
Gizmodo). Second, the exact Arabic word is best attested by linguists in a
comment thread and the commission, not by the news outlets, which describe only
"good morning" and a one-letter resemblance. A live sensitivity problem: the
origin (Haaretz) did not name the worker; a name ("Halawim Halawi") appears only
in downstream coverage and should not be treated as verified.

## Sources

```text
URL:         https://www.haaretz.com/israel-news/2017-10-22/ty-article/palestinian-arrested-over-mistranslated-good-morning-facebook-post/0000017f-db61-d856-a37f-ffe181000000
Kind:        Secondary, but the origin account and closest to the record. News
             reporting on the incident from outside; Haaretz broke the story and
             every later outlet cites it. Treat as the primary factual anchor
             per the commission, while noting it is not a document that owns the
             underlying event.
Establishes: The full incident: a Palestinian worker posted "Good morning" in
             Arabic beside a photo of himself leaning against a bulldozer at the
             construction site where he works in Beitar Ilit (West Bank, near
             Jerusalem); Facebook's automatic translation gave "attack them" in
             Hebrew and "hurt them" in English; no Arabic-speaking officer read
             the post before the arrest; he was released after a few hours of
             questioning when police realized the mistake.
Paraphrase:  Israeli police arrested the worker relying on Facebook's automatic
             translation of his post; the caption in Arabic was "Good morning";
             the software rendered it "attack them" (Hebrew) / "hurt them"
             (English); the picture showed him beside a bulldozer, a vehicle used
             in past ramming attacks; officers questioned him for hours and freed
             him once the error surfaced. The worker declined to speak to
             Haaretz.
Locators:    Body; published 2017-10-22, arrest described as "last week."
Quote:       "No Arabic-speaking police officer read the post before arresting
             the man." "The Palestinian man declined to speak with Haaretz."
```

```text
URL:         https://gizmodo.com/palestinian-man-arrested-after-facebook-auto-translates-1819782902
Kind:        Mixed. Secondary retelling (credits Haaretz), but carries a PRIMARY
             source firsthand: Facebook's own named statement. The statement is
             primary because Facebook owns the apology and the admission of
             error.
Establishes: Facebook's verbatim apology and admission, attributed to a named
             engineering manager; and the linguistic note that the transliterated
             string was not a real Arabic word but resembled a verb "to hurt."
Paraphrase:  Facebook acknowledged its translation system erred, said it had
             taken steps to fix the specific issue, and apologized to the man and
             his family; Arabic speakers said the transliteration Facebook used
             was not an actual Arabic word but could resemble the verb "to hurt,"
             and that any Arabic speaker could see it did not match the output.
Locators:    Body; published 2017-10-23.
Quote:       Necip Fazil Ayan, engineering manager in Facebook's language
             technologies group: "Unfortunately, our translation systems made an
             error last week that misinterpreted what this individual posted.
             Even though our translations are getting better each day, mistakes
             like these might happen from time to time and we've taken steps to
             address this particular issue. We apologize to him and his family
             for the mistake and the disruption this caused."
             On the wording: the transliteration "is not an actual word in Arabic
             but could look like the verb 'to hurt'—even though any Arabic speaker
             could clearly see the transliteration did not match the translation."
```

```text
URL:         https://www.timesofisrael.com/israeli-police-arrest-palestinian-for-good-morning-facebook-post/
Kind:        Secondary. Israeli-outlet retelling; largely tracks Haaretz but adds
             the charge basis and the sharpest plain-language statement of the
             linguistic closeness.
Establishes: The suspected offense (incitement); the "one letter" closeness
             between the colloquial greeting and the mistranslation; that no
             Arabic-speaking officer was consulted before arrest.
Paraphrase:  The worker was held on suspicion of incitement after officers relied
             solely on Facebook's automatic translation; there is only one
             letter's difference between the colloquial Arabic for "good morning
             to you all" and the string read as "hurt them"; he was released once
             the error was found.
Locators:    Body; published October 2017. Does NOT name the worker.
Quote:       "only one letter's difference between the colloquial Arabic phrase
             for 'good morning to you all' and 'hurt them.'"
             "No Arabic-speaking officer read the post prior to the arrest, which
             was carried out by officers who relied solely on Facebook's automatic
             translation."
```

```text
URL:         https://www.ibtimes.co.uk/palestinian-man-arrested-by-israeli-police-after-facebook-mistranslated-his-good-morning-post-1644154
Kind:        Secondary. Downstream retelling (attributes facts to Haaretz / local
             media). Recorded mainly because it is the source of the disputed
             name and to document that dispute, not as an independent confirmation.
Establishes: That a name, "Halawim Halawi," entered coverage; the incitement
             charge; release after hours.
Paraphrase:  IBTimes calls the worker "Halawim Halawi," a construction worker in
             Beitar Ilit, arrested on suspicion of incitement and released hours
             later; it attributes the translation facts to Haaretz and says local
             media reported no Arabic speaker was consulted.
Locators:    Body; published 2017-10-23.
Quote:       Names the man "Halawim Halawi." Attribution for underlying facts:
             "according to Haaretz"; "local media reported."
```

```text
URL:         https://languagelog.ldc.upenn.edu/nll/?p=35108
Kind:        Secondary/expert commentary. Post authored by Mark Liberman
             (computational linguist, University of Pennsylvania); the specific
             Arabic morphological analysis is in the COMMENT thread by named
             contributors (notably "Lameen," i.e. the Jabal al-Lughat linguistics
             blog, and "Shachar"). Comment-thread attribution is weaker than a
             signed article; treat the exact-word analysis as expert opinion, not
             settled record.
Establishes: The best available account of the exact Arabic word and why NMT
             mishandled it: the posted string was يصبحهم, a colloquial greeting
             short for "الله يصبحهم بالخير" ("may God make them spend the morning
             well"), i.e. a good-morning wish; the standard greeting any Arabic
             speaker knows is صباح الخير (sabah al-khair). The system reportedly
             selected a rare dictionary sense ("to attack by morning") that has no
             colloquial currency; the string also resembles يصبهم ("it hurts,"
             medical sense), a plausible confuser.
Paraphrase:  Commenters identify the posted word as يصبحهم, a colloquial
             morning-blessing not present in Facebook's training data in that
             sense; the mistranslation reflects choosing a low-probability sense
             of the root that a sensible probability weighting would never pick,
             compounded by the string's resemblance to a "hurt" form.
Locators:    Post dated 2017-10-24; body plus comments by "Lameen" and "Shachar."
Quote:       (Lameen) the phrase is short for the colloquial "الله يصبحهم بالخير";
             (Lameen) Facebook "opted for a sense of the word ... that certainly
             has no currency in colloquial use: 'to attack by morning'."
```

```text
URL:         https://aclanthology.org/N12-1006.pdf
Kind:        Primary. Peer-reviewed research paper; owns its claims and BLEU
             measurements. "Machine Translation of Arabic Dialects," Rabih Zbib,
             Erika Malchiodi, Jacob Devlin, David Stallard, Spyros Matsoukas,
             Richard Schwartz, John Makhoul (Raytheon BBN); Omar F. Zaidan
             (Microsoft Research); Chris Callison-Burch (Johns Hopkins).
             NAACL-HLT 2012, pp. 49-59.
Establishes: The mechanism anchor specific to Arabic. Arabic is diglossic: formal
             Modern Standard Arabic (MSA), used in writing, differs sharply in
             grammar from the spoken dialects acquired natively. Dialectal Arabic
             lacks linguistic resources, is user-generated and noisy, and has no
             standardized orthography, so users improvise spelling. Systems built
             on MSA data translate dialect badly; adding matched dialectal data
             has a large effect.
Paraphrase:  Because most Arabic MT is trained on formal MSA and dialects have
             scarce parallel data and no fixed spelling, an MSA-trained system is
             a poor fit for colloquial input; the paper shows a system trained on
             1.5M words of dialectal data beats one trained on 100x more
             mismatched MSA data by 6.3-7.0 BLEU.
Locators:    Abstract; §1 Introduction, p. 49.
Quote:       "Dialectal text, which is usually user-generated, is also noisy, and
             the lack of standardized orthography means that users often improvise
             spelling."
             "When trained on 1.5M words of dialectal data, our system performs
             6.3 to 7.0 BLEU points higher than when it is trained on 100 times
             more MSA data from a mismatching domain."
             "Significant differences in the phonology, morphology, lexicon and
             even syntax render some of these varieties mutually incomprehensible."
```

```text
URL:         https://scholar.lib.vt.edu/ejournals/JOTS/v32/v32n1/pdf/cummings.pdf
Kind:        Primary for the definition and framing it authors (Mary L. Cummings,
             "Automation and Accountability in Decision Support System Interface
             Design," The Journal of Technology Studies, vol. 32 no. 1). Secondary
             for the 39/40 experimental figure, which it cites to Skitka, Mosier &
             Burdick (1999).
Establishes: Automation bias as a named, studied phenomenon, and a concrete
             measure of it. Definition: the human tendency to disregard or not
             search for contradictory information when a computer-generated
             solution is accepted as correct. Commission errors: following an
             incorrect automated directive despite available contra-indications
             and the possibility of verification. This is precisely the police
             behavior: acting on the machine output without the cheap check.
Paraphrase:  Cummings defines automation bias (citing Mosier & Skitka 1996;
             Parasuraman & Riley 1997) and reports the Skitka et al. finding that
             39 of 40 subjects made commission errors, following incorrect
             automated recommendations even though contra-indications existed and
             verification was possible.
Locators:    Body, "automation bias" discussion; reference list (Skitka, Mosier &
             Burdick, 1999, Int. J. Human-Computer Studies 51(5):991-1006).
Quote:       "Known as automation bias, humans have a tendency to disregard or not
             search for contradictory information in light of a computer-generated
             solution that is accepted as correct (Mosier & Skitka, 1996;
             Parasuraman & Riley, 1997)."
             "39 out of 40 subjects committed errors of commission, i.e., these
             subjects almost always followed incorrect automated directives or
             recommendations, despite the fact that contraindications existed and
             verification was possible (Skitka et al., 1999)."
```

```text
URL:         https://respondcrisistranslation.org/en/blog/cbp-ones-obscene-language-errors-create-more-barriers-for-asylum-seekers
Kind:        Primary. The organization's own firsthand documentation of machine
             translation errors in the US Customs and Border Protection "CBP One"
             app. Respond Crisis Translation is a translator coalition; it owns
             these findings. Advocacy stance noted; the specific translation
             examples are its own analysis.
Establishes: A current, consequential setting where unchecked MT runs: US asylum
             access. Documents concrete Arabic-adjacent and other errors in a
             government app relied on by asylum seekers.
Paraphrase:  The CBP One app's machine translations produce errors that block
             asylum access: in Haitian Creole it renders "Customs" as "koutim"
             (social customs/traditions) instead of "ladwan" (the trade/border
             sense); missing spaces produce nonsense strings in Haitian Creole and
             Russian factsheets; the org attributes the failures to CBP's use of
             machine translation that performs inconsistently across languages.
Locators:    Blog post; published 2024-04-01.
Quote:       "The app uses the incorrect word for 'Customs' in its Haitian Creole
             translation ... 'koutim' instead of 'ladwan.' However, the word
             'koutim' refers to social customs and traditions, not to trade and
             the immigration system."
```

```text
URL:         https://multilingual.com/instagram-egregiously-mistranslates-palestinian-user-bios-inserting-word-terrorist/
Kind:        Secondary. Trade-press reporting on the October 2023 Instagram
             mistranslation. Recorded for the concrete "same weakness, today, in
             Meta's own product" parallel: the exact bio and wrong output.
Establishes: That in October 2023 Instagram's auto-translation turned Arabic bios
             into a "terrorist" slur, an MT-in-moderation harm directly analogous
             to 2017.
Paraphrase:  Bios pairing "Palestinian," a flag emoji and "alhamdulillah" (praise
             be to God) were auto-translated to "Praise be to god, Palestinian
             terrorists are fighting for their freedom"; discovered ~2023-10-19.
             Researchers at the Center for Democracy and Technology (Gabriel
             Nicholas, Aliya Bhatia) linked it to prejudiced patterns in training
             data.
Locators:    Body; October 2023.
Quote:       Output produced: "Praise be to god, Palestinian terrorists are
             fighting for their freedom."
```

```text
URL:         https://www.scmp.com/news/world/middle-east/article/3238713/meta-apologises-after-auto-translate-added-terrorist-biographies-palestine-supporters-instagram
Kind:        Mixed. Secondary reporting carrying a PRIMARY source firsthand:
             Meta's own apology for the October 2023 incident.
Establishes: Meta's verbatim 2023 apology, confirming the operator again
             acknowledged an Arabic MT failure in its products.
Paraphrase:  A Meta spokesperson said the company fixed a problem that briefly
             caused inappropriate Arabic translations and apologized.
Locators:    Body; published 2023-10-20; spokesperson unnamed.
Quote:       "We fixed a problem that briefly caused inappropriate Arabic
             translations in some of our products. We sincerely apologise that
             this happened."
```

## Contradictions

- The worker's name. The origin, Haaretz, did NOT name him and states he
  "declined to speak with Haaretz." Times of Israel also does not name him. A
  name, "Halawim Halawi," appears in downstream coverage (IBTimes, and reportedly
  Guardian-derived pieces). It is uncorroborated by the origin and reads like a
  possibly garbled transliteration. What would settle it: a named on-record
  source or the man's own confirmation, neither of which exists in the record.
  Recommendation for the writer: do not name him; describe him as the Haaretz
  account does (a Palestinian construction worker). This is the commission's
  flagged sensitivity and the record's sharpest limitation on a factual detail.

- The arrest date. Haaretz (published 2017-10-22) says "last week." IBTimes/Times
  of Israel place it around 2017-10-15. Safe formulation: mid-October 2017, the
  week before Haaretz's Oct 22 report. No source gives a firm calendar date on
  the record.

- Whether police relied "solely" on the machine translation. Every account
  asserts no Arabic-speaking officer read the post and that officers acted on the
  auto-translation; all of this traces to Haaretz. I found no on-record police
  statement confirming or denying it. Gizmodo adds that police were alert because
  bulldozers have been used in ramming attacks, which is context for the arrest,
  not a denial. The reliance claim is therefore well-reported but single-origin;
  it has not been independently confirmed by the police themselves. What would
  settle it: an Israel Police statement or an internal record.

- The exact Arabic word. News outlets say only "good morning" and (Times of
  Israel) that one letter separates the greeting from the "hurt them" reading.
  The specific word يصبحهم and its morphology come from linguists in the Language
  Log comment thread and match the commission's "yusbihuhum / يصبحهم." No
  news outlet prints the Arabic string, so the exact word rests on expert
  commentary, not primary reporting. Treat the word itself as expert-attested.

- Hurt vs attack. Consistent across sources: Hebrew output "attack them," English
  output "hurt them." No contradiction, but worth stating both precisely so the
  writer does not collapse them into one.

## Numbers

```text
Figure: 6.3 to 7.0 BLEU points (dialectal-trained MT over MSA-trained MT)
Owner:  Zbib et al., NAACL-HLT 2012 (aclanthology.org/N12-1006.pdf)
Scope:  A system trained on 1.5M words of dialectal Arabic vs one trained on 100x
        more (150M-word) MSA data from a mismatching domain, on Egyptian and
        Levantine test sets. Shows the size of the MSA-to-dialect penalty.
```

```text
Figure: 39 out of 40 subjects made commission errors
Owner:  Skitka, Mosier & Burdick 1999, as reported by Cummings (JOTS v32n1)
Scope:  A simulated flight-monitoring task; subjects followed incorrect automated
        directives despite existing contra-indications and available verification.
        The definitional core of automation bias, and the closest experimental
        analogue to the police behavior.
```

```text
Figure: "only one letter's difference"
Owner:  Times of Israel (secondary)
Scope:  Between the colloquial Arabic greeting ("good morning to you all") and the
        string read as "hurt them." A qualitative claim, not a measured figure;
        use as reported, attributed.
```

```text
Figure: Hebrew "attack them" / English "hurt them"
Owner:  Haaretz (origin), corroborated by Gizmodo, Times of Israel
Scope:  The two machine-translation outputs Facebook produced from the one Arabic
        post. State both; do not merge.
```

## Source assets

```text
Asset: The bulldozer photo — the worker leaning against a bulldozer at the Beitar
       Illit site, with the Arabic "good morning" caption, as described in Haaretz
       and shown in some coverage.
Shows: The visual that made the mistranslation read as a threat to officers (a
       bulldozer, associated with past ramming attacks).
Crop:  DO NOT reproduce. This is a photo of a named/identifiable private
       individual wrongfully detained, in a charged setting; publishing it re-
       exposes him. If the scene must be shown, describe it in prose. Flag to the
       editor.
```

```text
Asset: The word-to-output comparison (Arabic يصبحهم -> Hebrew "attack them" ->
       English "hurt them"), plus the standard greeting صباح الخير.
Shows: How one colloquial string diverged into two different violent readings and
       how far it sits from the ordinary greeting.
Crop:  This is not a single source visual; it would be an in-house table built
       from the Language Log analysis and the reporting, not a lifted image.
       Build it, cite the word to Language Log and the outputs to Haaretz/Gizmodo.
```

```text
Asset: Zbib et al. 2012 BLEU comparison (dialectal-trained vs MSA-trained system),
       in the paper's results tables.
Shows: The measured penalty for using MSA-trained MT on dialect — the mechanism,
       quantified.
Crop:  If used, render in-house per spec/charts.md from the paper's figures; do
       not lift the PDF table image. Label axes and cite the paper.
```

## Discarded

```text
URL: https://www.theguardian.com/technology/2017/oct/24/facebook-palestine-israel-translates-good-morning-attack-them-arrest
     Named in the commission but the fetch tool cannot retrieve theguardian.com
     (blocked, not dead — resolves in a browser). Not cited as read. Its facts are
     fully covered by sources I did open (Haaretz, Gizmodo, Times of Israel).
URL: https://restofworld.org/2023/ai-translation-errors-afghan-refugees-asylum/
     403 to the fetch tool (gated, resolves in a browser). Strong asylum-MT
     material (Pashto/Dari errors; a rejected Afghan claim) but not opened, so not
     cited. Respond Crisis Translation covers the same "MT in asylum" point from a
     source I read firsthand.
URL: https://www.bsr.org/en/blog/human-rights-due-diligence-of-meta-impacts-in-israel-and-palestine-may-2021
     403 to the fetch tool. Would corroborate over-enforcement of Arabic content
     moderation, but not opened. The 2023 Instagram incident carries the
     content-moderation "today" point from sources I did open.
URL: https://arxiv.org/pdf/1712.06273
     PDF returned only as binary to the fetch tool and did not decode to text.
     Superseded by Zbib et al. 2012 (N12-1006), which I read in full and which is
     the stronger, more-cited Arabic-dialect-MT anchor.
URL: https://pubmed.ncbi.nlm.nih.gov/11540946/
     Cookie wall to the fetch tool; abstract not retrievable directly. The Skitka
     et al. finding and the automation-bias definition are established firsthand
     via Cummings (JOTS), which quotes and cites them.
URL: https://incidentdatabase.ai/cite/72/
     Aggregator index of this incident; useful as a pointer but not itself a
     source that owns any claim. Not cited.
```
