# Evidence record: when-ai-breaks/google-photos-gorilla (01)

The record supports the commissioned arc. The incident, the names, the words, and
the dates are confirmed, and the non-fix is documented by two independent
firsthand tests years apart. Two primary sources are thin on access, not on
substance: the original posts by Jacky Alciné and the reply thread from the
Google engineer are now deleted or set to a protected account (verified directly,
see below), so their exact wording survives only through contemporaneous
coverage that quoted and embedded them; and the New York Times 2023 test is
paywalled to this environment (HTTP 403, archives blocked), so its findings are
established through two independent outlets that read and reported it, not from
the article's own page. The Wired 2018 test and the Gender Shades study were read
in full firsthand. The strongest caution for the writer is a scope gap: Gender
Shades measured a different task (gender classification) on different vendors
(Microsoft, IBM, Face++), not Google Photos' animal labeling. It is evidence for
the mechanism, not a measurement of this specific failure, and the draft must not
present it as the latter. One finding actively complicates the "recognition was
never made safe" framing: by 2018, Google's own Cloud Vision API and Assistant
could label a gorilla correctly, so the Photos block was a deliberate product and
risk decision, not a company-wide inability.

## Sources

```text
URL:         https://proceedings.mlr.press/v81/buolamwini18a.html
             (PDF: https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf)
Kind:        primary. The paper owns the accuracy measurement it reports; the
             authors built the benchmark and ran the audit.
Establishes: The measured accuracy gap by skin tone and sex in commercial
             image systems. Task: binary gender classification. Systems audited:
             Microsoft (Cognitive Services Face API), IBM (Watson Visual
             Recognition), Face++. Benchmark: the authors' new Pilot Parliaments
             Benchmark (PPB), 1,270 parliamentarians from Rwanda, Senegal, South
             Africa, Iceland, Finland, Sweden, balanced by sex and skin type,
             skin labeled on the dermatologist-approved Fitzpatrick scale. All
             three classifiers were worst on darker-skinned women (error rate
             20.8% Microsoft to 34.7% IBM) and near-perfect on lighter-skinned
             men (0.0% Microsoft, 0.3% IBM).
Paraphrase:  A group underrepresented in the data was classified far less
             accurately, and the intersection of darker skin and female sex was
             worst of all. This is the mechanism the commission asks the lesson
             to teach, measured on real commercial systems, though not on Google
             and not on animal labeling.
Locators:    Abstract (p.1); Section 4.1 "Key Findings" (p.9); Section 4.4
             "Audit Results" (p.10); Table 4 (aggregate error rates by DF/DM/LF/LM).
Quote:       "darker-skinned females are the most misclassified group (with error
             rates of up to 34.7%). The maximum error rate for lighter-skinned
             males is 0.8%." (Abstract). "All classifiers perform worst on darker
             female faces (20.8%-34.7% error rate)" (Section 4.1).
```

```text
URL:         https://www.wired.com/story/when-it-comes-to-gorillas-google-photos-remains-blind/
Kind:        primary. Wired conducted its own test of Google Photos and owns the
             result. Commission names it primary. Read in full firsthand (HTTP 200).
Establishes: The 2018 firsthand test that held up. Author Tom Simonite,
             published Jan 11, 2018. Wired tested Google Photos with a collection
             of 40,000 images "well-stocked with animals." Photos found pandas
             and poodles but returned "no results" for "gorilla," "chimp,"
             "chimpanzee," and "monkey." Searches for "baboon," "gibbon,"
             "marmoset," and "orangutan" worked. A Google spokesperson confirmed
             "gorilla" was censored from searches and image tags after the 2015
             incident, and that "chimp," "chimpanzee," and "monkey" are also
             blocked. Crucially, Google's Cloud Vision API demo and Google
             Assistant identified a gorilla correctly (one photo tagged "western
             gorilla" at 94% confidence). So Google could recognize gorillas
             elsewhere; the Photos block was a choice, not an inability.
Paraphrase:  Two-plus years after the apology, the "fix" was to remove gorillas
             and several other primates from what Photos could label or find,
             while Google's other vision products labeled them fine.
Locators:    Paragraphs 1-6 (the tests and the 40,000-image figure); the
             spokesperson quote (mid-article); the Cloud Vision and Assistant
             tests (final third).
Quote:       "the service reported 'no results' for the search terms 'gorilla,'
             'chimp,' 'chimpanzee,' and 'monkey.'" / Google spokesperson: "Image
             labeling technology is still early and unfortunately it's nowhere
             near perfect."
```

```text
URL:         https://www.nytimes.com/2023/05/22/technology/ai-photo-labels-google-apple.html
Kind:        primary. The Times ran its own 2023 test and owns the result.
             Commission names it primary. NOT read firsthand: the page returns
             HTTP 403 to this environment and Wayback/archive.today mirrors are
             blocked here. Findings below are established through two independent
             outlets that read the article; treat as gated-and-corroborated, not
             opened.
Establishes: "Google's Photo App Still Can't Find Gorillas. And Neither Can
             Apple's." By Nico Grant and Kashmir Hill, published May 22, 2023.
             The Times searched its own collection of 44 images in Google Photos:
             cats and kangaroos were found; gorillas, baboons, chimpanzees,
             orangutans, and monkeys were not, though primates were present.
             Apple Photos had the same block ("It could accurately find photos
             of particular animals, except for most primates"; gorilla returned
             results only when the word appeared as text, e.g. Gorilla Tape).
             Microsoft's OneDrive showed the same behavior; Amazon Photos
             mislabeled other animals as gorillas. A Google spokesman said the
             company prevented its photo app from labeling anything as a monkey
             or ape because the benefit "does not outweigh the risk of harm."
             Alciné, re-interviewed, said he was disappointed the problem was not
             fixed.
Paraphrase:  Eight years on, at four large companies, the safe move was still to
             switch primate labels off rather than risk another misclassification.
Locators:    Reported via PetaPixel (2023-05-22) and The Register (2023-05-29),
             both cited in full below. The 44-image figure and the "risk of harm"
             quote come from PetaPixel's reading of the Times; the multi-company
             finding is corroborated by both.
Quote:       Google spokesman, via PetaPixel quoting the Times: the benefit
             "does not outweigh the risk of harm."
```

```text
URL:         Alcine original: https://twitter.com/jackyalcine/status/615329515909156865
             Alcine follow-up: https://twitter.com/jackyalcine/status/615332439053967360
Kind:        primary. Alcine's own posts are the origin record. Commission names
             them primary. The URLs no longer resolve to content: queried
             directly, Twitter's syndication endpoint returns a TweetTombstone,
             "This Post was deleted by the Post author," for both. Exact wording
             and IDs are preserved by contemporaneous coverage that embedded them.
Establishes: What Alcine posted and when. The photo of Alcine and a friend, both
             Black, was auto-filed by Google Photos under an album labeled
             "Gorillas." He posted the screenshot with: "Google Photos, y'all
             fucked up. My friend's not a gorilla." (media: pic.twitter.com/SMkMCsNVX4,
             reproduced in CBC's report, credited "Jacky Alcine/Twitter"). The
             tweet ID decodes to 2015-06-29 01:22:43 UTC, i.e. the evening of
             Sunday, June 28, 2015 in New York (EDT); Forbes describes it as
             "Sunday evening." His follow-up (ID decodes to 2015-06-29 01:34:20
             UTC): "Like I understand HOW this happens; the problem is moreso on
             the WHY."
Paraphrase:  A Brooklyn/New York software developer reported firsthand that the
             product had labeled two Black people as gorillas, and posted the
             screenshot.
Locators:    Snowflake-ID timestamp decode; wording quoted identically in Forbes
             (2015-07-01) and CBC (2015-07-02), both read firsthand.
Quote:       "Google Photos, y'all fucked up. My friend's not a gorilla."
```

```text
URL:         Zunger reply: https://twitter.com/yonatanzunger/status/615355996114804737
             Zunger next-day: https://twitter.com/yonatanzunger/status/615677702092140544
             Google statement carried in: Forbes and CBC (2015); Wired (2018);
             PetaPixel quoting NYT (2023).
Kind:        primary. Google's own words: an engineer speaking for the company
             and official spokesperson statements. Commission names Google's
             public statements primary. The two Zunger tweet URLs no longer
             resolve to content: the syndication endpoint returns a tombstone,
             "this account owner limits who can view their Posts" (account now
             protected). Wording preserved by contemporaneous coverage.
Establishes: Who responded and what the company said. Yonatan Zunger, Google's
             chief architect of social (he signs the tweet "G+ CA here," Google+
             Chief Architect), replied within about two hours (his tweet ID
             decodes to 2015-06-29 03:07:56 UTC): "Holy fuck. G+ CA here. No,
             this is not how you determine someone's target market. This is 100%
             Not OK." Google's official statement: "We're appalled and genuinely
             sorry that this happened... There is still clearly a lot of work to
             do with automatic image labeling." Zunger said the label "gorilla"
             would no longer be applied to groups of images and that Google was
             "working on longer-term fixes around both linguistics... and image
             recognition itself - e.g. better recognition of dark-skinned faces."
             The company's actual fix was to delete the "gorilla" label and the
             ability to search for it (confirmed as still in force in 2018 and
             2023, and extended to other primates).
Paraphrase:  The named engineer was Yonatan Zunger, chief architect of social;
             the company apologized, promised longer-term fixes, and shipped the
             narrow one: remove the label.
Locators:    Forbes (Zunger quote, spokesperson statement); CBC (Zunger quote,
             spokesperson statement); Wired 2018 (2018 confirmation of what was
             blocked); PetaPixel/Register 2023 (still in force).
Quote:       Zunger: "No, this is not how you determine someone's target market.
             This is 100% Not OK." Google spokesperson: "We're appalled and
             genuinely sorry that this happened."
```

```text
URL:         https://www.forbes.com/sites/mzhang/2015/07/01/google-photos-tags-two-african-americans-as-gorillas-through-facial-recognition-software/
Kind:        secondary. Contemporaneous news coverage reporting on the incident.
             Read firsthand (HTTP 200). Embeds the original tweets (permalinks
             intact in page source), which is how the deleted wording is anchored.
Establishes: The timeline and the quotes, contemporaneously. Author Maggie
             (Mzhang) Zhang, July 1, 2015. Alcine logged on "Sunday evening" and
             found an album titled "Gorillas." Carries Zunger's title ("Google's
             chief architect of social"), his tweet, and the official statement.
             Also lists prior parallels the writer may or may not use: Flickr's
             2015 auto-tags labeling both Black and white people as "animals" and
             "apes"; Nikon's 2009 blink-detection misfiring on Asian faces; an HP
             webcam that failed to track a Black face. These parallels are
             reported by Forbes, not independently verified here.
Paraphrase:  Repeats and timestamps the incident; a repetition supports that the
             claim was made, not that it is independently true.
Locators:    Body paragraphs 1-4; the parallels appear in the closing paragraphs.
Quote:       Google spokesperson: "There is still clearly a lot of work to do
             with automatic image labeling."
```

```text
URL:         https://www.cbc.ca/news/trending/google-photos-black-people-gorillas-1.3135754
Kind:        secondary. Contemporaneous news coverage. Read firsthand (HTTP 200).
             Reproduces Alcine's screenshot (credited "Jacky Alcine/Twitter") and
             embeds both key tweets.
Establishes: Independent confirmation of the tweet wording and Zunger's reply,
             and the "appalled and genuinely sorry" statement. Notes the word
             "also has racist connotations." Attributes to the New York Times
             (2015) that Google "decided to temporarily remove the gorilla label,
             including the application's ability to search for gorillas." The word
             "temporarily" is the 2015 framing; the 2018 and 2023 tests show the
             removal was not temporary.
Paraphrase:  A second independent outlet carrying the same wording; two
             retellings of one origin, so they corroborate wording, not truth
             beyond it.
Locators:    Posted Jul 02, 2015; body paragraphs 1-5.
Quote:       Zunger: "Holy fuck. G+ CA here... This is 100% Not OK."
```

```text
URL:         https://www.theregister.com/2023/05/29/google_photos_ai_still_cant_label_gorillas/427652
Kind:        secondary. Contemporaneous coverage of the NYT 2023 test. Read
             firsthand (HTTP 200). Independent of PetaPixel.
Establishes: Corroborates the NYT 2023 findings: users could search cats and
             kangaroos but not gorillas, baboons, chimpanzees, orangutans, and
             monkeys; Apple Photos and Microsoft OneDrive had the same block;
             Amazon Photos mislabeled other animals as gorillas. Carries Alcine's
             2023 reaction: "I'm going to forever have no faith in this AI."
Paraphrase:  Second independent outlet reading the Times, matching PetaPixel on
             the multi-company result.
Locators:    Lede and paragraphs 2-5 (the rest of the piece is unrelated AI
             briefs).
Quote:       Alcine: "I'm going to forever have no faith in this AI."
```

```text
URL:         https://petapixel.com/2023/05/22/googles-photos-app-is-still-unable-to-find-gorillas/
Kind:        secondary. Same-day coverage of the NYT 2023 test. Read firsthand
             (HTTP 200). Independent of The Register.
Establishes: The detail behind the NYT test: the Times searched a collection of
             44 images; cats and kangaroos found, gorillas/baboons/chimpanzees/
             orangutans/monkeys not. Apple Photos: "It could accurately find
             photos of particular animals, except for most primates," and gorilla
             matched only as text (Gorilla Tape). Google spokesman: the benefit
             "does not outweigh the risk of harm." Also carries the 2015 Zunger
             "longer-term fixes... better recognition of dark-skinned faces"
             quote and the widely repeated claim that Google's training data had
             too few photos of Black people. That training-data claim is a
             causal explanation repeated in coverage; I did not find Google
             stating it in those exact terms in a primary source (Zunger's tweet
             names "better recognition of dark-skinned faces" as a fix area,
             which implies but does not assert the training-gap cause).
Paraphrase:  Supplies the 44-image scope and the 2023 Google "risk of harm"
             framing that a primary I could open does not.
Locators:    Body paragraphs 1-12.
Quote:       Google spokesman: benefit "does not outweigh the risk of harm."
```

## Contradictions

- **Google could recognize gorillas by 2018; the Photos block was a choice, not
  an inability.** Wired's own 2018 test (primary) found Google's Cloud Vision API
  and Google Assistant labeled a gorilla correctly (one image, "western gorilla,"
  94% confidence), while consumer Google Photos returned nothing. This complicates
  a flat reading that "the recognition was never made safe." The recognition
  worked in Google's other products; what stayed off in Photos was the willingness
  to risk labeling a person as a primate. The 2023 Google statement frames it the
  same way: the benefit "does not outweigh the risk of harm." The lesson's "non-fix"
  point still holds for Photos, but the precise claim is "Google chose not to
  enable primate labels in consumer Photos," not "Google never built a classifier
  that could tell a gorilla from a person."

- **Scope gap in the mechanism evidence.** Gender Shades measured gender
  classification error, on Microsoft/IBM/Face++, using a face benchmark. Google
  Photos' failure was animal/scene labeling on consumer photos. The study is
  strong evidence for the general mechanism (a group underrepresented in training
  data is classified worse, worst at the darker-skin/female intersection) but it
  did not measure Google Photos or the gorilla error. The draft must present it as
  the mechanism, anchored in real numbers, and not imply it quantified this
  incident.

- **"Temporarily" vs. permanently.** CBC (2015), citing the NYT, called the label
  removal temporary. The 2018 and 2023 firsthand tests show it was not. If the
  draft quotes the 2015 "temporary" framing, it should be as a promise the record
  later contradicts.

- **The training-data cause is inferred, not quoted from a primary.** Coverage
  widely says Google admitted too few Black faces in its training set. The primary
  I can open (Zunger, via contemporaneous embed) names "better recognition of
  dark-skinned faces" as a fix area, which implies the gap without stating it as
  the confirmed cause. Attribute carefully.

- **Contemporaneous parallels are single-sourced.** Forbes lists Flickr (2015,
  "apes"/"animals" tags), Nikon (2009, blink detection on Asian faces), and an HP
  webcam that failed to track a Black face. The commission allows a parallel only
  if firsthand-sourced. These come from one secondary outlet and are not verified
  against a firsthand record here; do not present them as confirmed without
  further sourcing.

## Numbers

```text
Figure: 34.7% - maximum gender-classification error rate, darker-skinned females (IBM)
Owner:  Gender Shades (Buolamwini & Gebru, 2018)
Scope:  On the PPB benchmark (1,270 subjects); IBM Watson Visual Recognition.
```

```text
Figure: 20.8% - darker-skinned-female error rate for the best of the three (Microsoft)
Owner:  Gender Shades
Scope:  PPB benchmark; still the worst subgroup even for the strongest system.
```

```text
Figure: 0.0% and 0.3% - lighter-skinned-male error rates (Microsoft, IBM)
Owner:  Gender Shades
Scope:  PPB benchmark; the best-classified subgroup. Face++ best on darker males (0.7%).
```

```text
Figure: 34.4 percentage points - maximum error gap, best subgroup to worst
Owner:  Gender Shades (Section 4.1)
Scope:  Across the three audited classifiers on PPB.
```

```text
Figure: darker females = 21.3% of the benchmark but 61.0%-72.4% of all errors
Owner:  Gender Shades (Section 4.4)
Scope:  Share of PPB vs. share of total misclassifications across classifiers.
```

```text
Figure: 79.6% (IJB-A) and 86.2% (Adience) - share of lighter-skinned subjects
Owner:  Gender Shades (Abstract)
Scope:  The two existing face benchmarks the authors characterized; shows the
        underrepresentation that motivates the mechanism.
```

```text
Figure: 40,000 images - size of Wired's 2018 test collection
Owner:  Wired (Simonite, 2018)
Scope:  Uploaded to Google Photos; animals well-represented. Result: no hits for
        gorilla, chimp, chimpanzee, monkey.
```

```text
Figure: 44 images - size of the New York Times' 2023 test collection
Owner:  New York Times (2023), via PetaPixel's reading (not verified against the
        Times' own page, which is gated here).
Scope:  Searched in Google Photos; cats/kangaroos found, primates not.
```

```text
Figure: 94% confidence - Google Cloud Vision "western gorilla" tag on one image
Owner:  Wired (Simonite, 2018)
Scope:  Cloud Vision API online demo, single image; shows recognition worked
        outside consumer Photos.
```

```text
Figure: ~2 hours - gap from Alcine's first post to Zunger's reply
Owner:  Derived from tweet snowflake IDs (01:22:43 UTC to 03:07:56 UTC, 2015-06-29)
Scope:  Same night; corroborated by Forbes ("within hours").
```

## Source assets

```text
Asset: Gender Shades, Table 4 - gender-classification error rates by subgroup
       (DF/DM/LF/LM) for Microsoft, IBM, Face++.
Shows: The whole mechanism in one grid: near-zero error for lighter males,
       20.8%-34.7% for darker females. Carries the argument better than prose.
Crop:  Keep the four subgroup columns and all three vendor rows and the error-rate
       row; keep the caption naming the systems. Omit nothing that changes the
       20.8%-34.7% reading.
```

```text
Asset: Gender Shades, Figure 1 - example images and average faces from PPB.
Shows: What "balanced by skin type" means concretely; the Fitzpatrick spread.
Crop:  Retain the skin-type range; do not crop to a single face, which would lose
       the point of a balanced benchmark.
```

```text
Asset: Alcine's original screenshot - the Google Photos album header reading
       "Gorillas" over the two photos.
Shows: The failure itself, in the product's own interface. The single most direct
       visual in the story.
Crop:  Originates from the now-deleted tweet; reproduced in CBC's 2015 report
       credited "Jacky Alcine/Twitter." Rights and provenance must be checked
       before any use, and it is a photo of real people who were harmed; handle
       with the care the commission's sensitivity note requires. Not a decorative
       image.
```

```text
Asset: Wired 2018 - none essential beyond the reported results.
Shows: n/a
Crop:  n/a
```

## Discarded

```text
URL: https://gendershades.org/  - The project's own results site. Did not resolve
     in this environment (connection reset). The peer-reviewed paper is the
     stronger primary and was read in full, so nothing is lost.
```

```text
URL: https://r.jina.ai/... and web.archive.org / archive.ph|li|md|vn for the NYT
     2023 article - All blocked or reset in this environment. Recorded here so the
     access failure is on the record, not hidden. NYT findings are corroborated by
     two independent outlets instead.
```

```text
URL: https://carmona.mx/2023/05/22/... - An IFTTT auto-repost of the NYT article.
     Carries only the headline and dek, not the body. No independent value.
```

```text
URL: Museum of Failure, Colorlines, HuffPost, Gigazine, Slashdot, BoingBoing,
     Techmeme, CNN, CBS, Fox, SBS, gulfnews, Indianapolis Recorder - Additional
     retellings of the same origin. Not read in full or not cited: they add
     repetition, not independent confirmation, and the record already has enough
     independent corroboration (Forbes, CBC, Register, PetaPixel) plus the two
     primaries read firsthand.
```
