# Evidence record: when-ai-breaks/google-photos-gorilla (02)

This record supersedes the 01 record. It preserves that record's still-valid work
and repairs the one defect the coordinator flagged: too few readable, firsthand
primaries. The incident's original primaries cannot be opened here (Alciné's
tweets are deleted, Zunger's account is protected, the NYT 2023 article is
paywalled, and the Wayback content host web.archive.org is unreachable from this
environment through every route tried). The repair adds two firsthand primary
studies on the training-data representation cause the "why it fails" section
teaches: Shankar et al. (2017, Google Brain) and Yang et al. (2020, Princeton and
Stanford, FAT* ImageNet audit). Both were downloaded and read in full. The
readable, firsthand primary count is now four: Gender Shades (2018), Wired's 2018
test, Shankar (2017), and Yang (2020). Adding the four contemporaneous secondaries
already read firsthand (Forbes, CBC, The Register, PetaPixel) gives eight sources
that were each opened and read, with four primary among them, so the series floor
(at least four primary, at least eight total) is met cleanly by fully-read sources
alone. The incident primaries (the tweets, Google's statements, the NYT test)
remain in the record as additional primaries with honest access caveats.

The commissioned arc is supported. The strongest caution for the writer is
unchanged and now better bounded: none of the mechanism studies measured Google
Photos' gorilla error itself. Gender Shades measured gender classification on
Microsoft, IBM, and Face++; Shankar and Yang audited the ImageNet and Open Images
datasets and classifiers trained on them. Together they establish the mechanism
(a group underrepresented in training data is recognized worse) in the exact
dataset ecosystem that systems like Google Photos were built on, not the 2015
misclassification as a measured event. A second caution also stands: Wired's 2018
test found Google's Cloud Vision API and Assistant could label a gorilla
correctly, so the Photos block was a deliberate product and risk decision, not a
company-wide inability to recognize the animal.

## Sources

```text
URL:         https://proceedings.mlr.press/v81/buolamwini18a.html
             (PDF: https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf)
Kind:        primary. The paper owns the accuracy measurement it reports; the
             authors built the benchmark and ran the audit. Read in full firsthand.
Establishes: The measured accuracy gap by skin tone and sex in commercial image
             systems. Task: binary gender classification. Systems: Microsoft
             (Cognitive Services Face API), IBM (Watson Visual Recognition),
             Face++. Benchmark: the authors' Pilot Parliaments Benchmark (PPB),
             1,270 parliamentarians from Rwanda, Senegal, South Africa, Iceland,
             Finland, Sweden, balanced by sex and skin type, skin labeled on the
             dermatologist-approved Fitzpatrick scale. All three classifiers were
             worst on darker-skinned women (20.8% error Microsoft to 34.7% IBM)
             and near-perfect on lighter-skinned men (0.0% Microsoft, 0.3% IBM).
Paraphrase:  A group underrepresented in the data was classified far less
             accurately, worst at the intersection of darker skin and female sex.
             The mechanism, measured on real commercial systems, though not on
             Google and not on animal labeling.
Locators:    Abstract (p.1); Section 4.1 "Key Findings" (p.9); Section 4.4
             "Audit Results" (p.10); Table 4.
Quote:       "darker-skinned females are the most misclassified group (with error
             rates of up to 34.7%). The maximum error rate for lighter-skinned
             males is 0.8%." (Abstract).
```

```text
URL:         https://arxiv.org/abs/1711.08536
             (PDF read: https://arxiv.org/pdf/1711.08536)
Kind:        primary. The authors ran the geo-diversity analysis and the classifier
             stress-test and own the findings. Read in full firsthand (added in 02).
Establishes: The training-data representation cause, directly. "No Classification
             without Representation: Assessing Geodiversity Issues in Open Data
             Sets for the Developing World," by Shreya Shankar, Yoni Halpern, Eric
             Breck, James Atwood, Jimbo Wilson, and D. Sculley, Google Brain Team;
             NIPS 2017 (Machine Learning for the Developing World workshop). Two
             standard datasets are geographically skewed: in Open Images, more
             than 32% of geo-located images were US-based and about 60% came from
             the six most-represented North American and European countries, with
             China at ~1% and India at ~2%; in ImageNet, about 45% of the sampled
             images were US-based. Classifiers (Inception V3) trained on these
             datasets recognized images of the same concept (e.g. groom,
             bridegroom) from Hyderabad, India, dramatically less well than the
             standard test images. The people-related labels were classified with
             "a classifier similar to Google Cloud Vision API," a close adjacency
             to the kind of system Google Photos used.
Paraphrase:  When the training data over-represents one part of the world, the
             model recognizes the under-represented part worse. This is the
             general form of the failure the lesson teaches, shown on the datasets
             that underlie consumer image systems, by a Google research team.
Locators:    Abstract and Section 1 (p.1); Section 3 "Analyzing Geo-Diversity"
             (p.2-3, the 32%/60%/45% figures); Section 4 and Figure 3 (the
             Hyderabad stress-test).
Quote:       "these data sets appear to exhibit an observable amerocentric and
             eurocentric representation bias... we find strong differences in the
             relative performance on images from different locales."
```

```text
URL:         https://arxiv.org/abs/1912.07726
             (PDF read: https://arxiv.org/pdf/1912.07726)
Kind:        primary. The authors annotated the dataset and own the demographic
             measurement. Read in full firsthand (added in 02).
Establishes: That the dataset behind modern image classifiers under-represents
             dark skin and carries offensive labels, measured directly. "Towards
             Fairer Datasets: Filtering and Balancing the Distribution of the
             People Subtree in the ImageNet Hierarchy," by Kaiyu Yang, Klint
             Qinami, Li Fei-Fei, Jia Deng, and Olga Russakovsky (Princeton and
             Stanford); FAT* 2020, Barcelona. ImageNet's "person subtree" holds
             2,832 categories (about 8.3% of all ImageNet images); the authors
             judged only 158 of them both safe and reliably imageable, and found
             offensive categories in the vocabulary (including racial and gender
             slurs inherited from WordNet). Annotating 13,900 images across the
             safe, imageable synsets (43,897 attribute labels from 109,545 worker
             judgments), they found the skin-color distribution "mirrors real-world
             biases": the average share of the Dark category across synsets is only
             6.2%, and the synsets heaviest in Dark track stereotypes (rapper 66.4%,
             basketball player 34.5%). Female is likewise underrepresented overall.
Paraphrase:  The reference dataset both under-represents darker-skinned people and
             contains categories that label people offensively. That is the cause
             of the failure and the reason the harm reached dignity, measured in
             the dataset itself.
Locators:    Abstract and Section 1 (p.1); Section 3 (person subtree size, 8.3%);
             Section 4 (offensive synsets); Section 6.2-6.3 and Figure 4 (the 6.2%
             Dark average and the per-synset figures).
Quote:       "The average percentage of the Dark category across all synsets is
             only 6.2%, and the synsets with significant portion of Dark align with
             stereotypes."
```

```text
URL:         https://www.wired.com/story/when-it-comes-to-gorillas-google-photos-remains-blind/
Kind:        primary. Wired conducted its own test of Google Photos and owns the
             result. Commission names it primary. Read in full firsthand (HTTP 200).
Establishes: The 2018 firsthand test that held up. Author Tom Simonite, published
             Jan 11, 2018. Wired tested Google Photos with a collection of 40,000
             images "well-stocked with animals." Photos found pandas and poodles
             but returned "no results" for "gorilla," "chimp," "chimpanzee," and
             "monkey." Searches for "baboon," "gibbon," "marmoset," and "orangutan"
             worked. A Google spokesperson confirmed "gorilla" was censored from
             searches and image tags after the 2015 incident, and that "chimp,"
             "chimpanzee," and "monkey" are also blocked. Google's Cloud Vision API
             demo and Google Assistant identified a gorilla correctly (one photo
             tagged "western gorilla," 94% confidence). Recognition worked
             elsewhere; the Photos block was a choice.
Paraphrase:  Two-plus years after the apology, the "fix" was to remove gorillas
             and several other primates from what consumer Photos could label or
             find, while Google's other vision products labeled them fine.
Locators:    Paragraphs 1-6 (the tests, the 40,000 figure); the spokesperson quote
             (mid-article); the Cloud Vision and Assistant tests (final third).
Quote:       "the service reported 'no results' for the search terms 'gorilla,'
             'chimp,' 'chimpanzee,' and 'monkey.'"
```

```text
URL:         https://www.nytimes.com/2023/05/22/technology/ai-photo-labels-google-apple.html
Kind:        primary. The Times ran its own 2023 test and owns the result.
             Commission names it primary. NOT read firsthand: the page returns HTTP
             403 to this environment and Wayback/archive mirrors are blocked here.
             Findings are established through two independent outlets that read the
             article; treat as gated-and-corroborated, not opened.
Establishes: "Google's Photo App Still Can't Find Gorillas. And Neither Can
             Apple's." By Nico Grant and Kashmir Hill, published May 22, 2023. The
             Times searched its own collection of 44 images in Google Photos: cats
             and kangaroos were found; gorillas, baboons, chimpanzees, orangutans,
             and monkeys were not, though primates were present. Apple Photos had
             the same block (gorilla returned results only when the word appeared
             as text, e.g. Gorilla Tape). Microsoft's OneDrive behaved the same;
             Amazon Photos mislabeled other animals as gorillas. A Google spokesman
             said the company prevented its photo app from labeling anything as a
             monkey or ape because the benefit "does not outweigh the risk of harm."
             Alciné, re-interviewed, said he was disappointed.
Paraphrase:  Eight years on, at four large companies, the safe move was still to
             switch primate labels off rather than risk another misclassification.
Locators:    Reported via PetaPixel (2023-05-22) and The Register (2023-05-29),
             both read firsthand below. The 44-image figure and the "risk of harm"
             quote come from PetaPixel's reading of the Times; the multi-company
             finding is in both.
Quote:       Google spokesman, via PetaPixel quoting the Times: the benefit "does
             not outweigh the risk of harm."
```

```text
URL:         Alcine original: https://twitter.com/jackyalcine/status/615329515909156865
             Alcine follow-up: https://twitter.com/jackyalcine/status/615332439053967360
             Wayback capture (exists, unread): https://web.archive.org/web/20150703000351/https://twitter.com/jackyalcine/status/615329515909156865
Kind:        primary. Alcine's own posts are the origin record. Commission names
             them primary. The live URLs no longer resolve to content: Twitter's
             syndication endpoint returns a TweetTombstone, "This Post was deleted
             by the Post author," for both. A genuine contemporaneous Wayback
             snapshot exists (captured 2015-07-03, four days after the tweet;
             confirmed via the archive.org availability API), but the snapshot
             content host web.archive.org is unreachable from this environment, so
             I could not open and read it. Exact wording is anchored to
             contemporaneous coverage that embedded the tweets (Forbes, CBC).
Establishes: What Alcine posted and when. A photo of Alcine and a friend, both
             Black, was auto-filed by Google Photos under an album labeled
             "Gorillas." He posted the screenshot with: "Google Photos, y'all
             fucked up. My friend's not a gorilla." The tweet ID decodes to
             2015-06-29 01:22:43 UTC, i.e. the evening of Sunday June 28, 2015 in
             New York (EDT); Forbes calls it "Sunday evening." His follow-up (ID
             decodes to 2015-06-29 01:34:20 UTC): "Like I understand HOW this
             happens; the problem is moreso on the WHY."
Paraphrase:  A Brooklyn/New York software developer reported firsthand that the
             product labeled two Black people as gorillas, and posted the
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
Kind:        primary. Google's own words: an engineer speaking for the company and
             official spokesperson statements. Commission names Google's public
             statements primary. The two Zunger tweet URLs no longer resolve: the
             syndication endpoint returns a tombstone, "this account owner limits
             who can view their Posts" (account now protected). Wayback holds later
             captures (closest to 2015 is 2017) but the content host is unreachable
             here. Wording is anchored to contemporaneous coverage.
Establishes: Who responded and what the company said. Yonatan Zunger, Google's
             chief architect of social (he signs the tweet "G+ CA here," Google+
             Chief Architect), replied within about two hours (his tweet ID decodes
             to 2015-06-29 03:07:56 UTC): "Holy fuck. G+ CA here. No, this is not
             how you determine someone's target market. This is 100% Not OK."
             Google's official statement: "We're appalled and genuinely sorry that
             this happened... There is still clearly a lot of work to do with
             automatic image labeling." Zunger said the "gorilla" label would no
             longer be applied to groups of images and that Google was "working on
             longer-term fixes around both linguistics... and image recognition
             itself - e.g. better recognition of dark-skinned faces." The company's
             actual fix was to delete the "gorilla" label and its searchability,
             later extended to other primates and confirmed still in force in 2018
             and 2023.
Paraphrase:  The named engineer was Yonatan Zunger, chief architect of social; the
             company apologized, promised longer-term fixes, and shipped the narrow
             one: remove the label.
Locators:    Forbes (Zunger quote, spokesperson statement); CBC (Zunger quote,
             spokesperson statement); Wired 2018 (2018 confirmation of what was
             blocked); PetaPixel/Register 2023 (still in force).
Quote:       Zunger: "No, this is not how you determine someone's target market.
             This is 100% Not OK."
```

```text
URL:         https://www.forbes.com/sites/mzhang/2015/07/01/google-photos-tags-two-african-americans-as-gorillas-through-facial-recognition-software/
Kind:        secondary. Contemporaneous news coverage. Read firsthand (HTTP 200).
             Embeds the original tweets (permalinks intact in page source), which
             anchors the deleted wording.
Establishes: The timeline and quotes, contemporaneously. Author Maggie Zhang, July
             1, 2015. Alcine logged on "Sunday evening" and found an album titled
             "Gorillas." Carries Zunger's title, his tweet, and the official
             statement. Lists prior parallels (Flickr 2015 "apes"/"animals" tags;
             Nikon 2009 blink detection on Asian faces; an HP webcam that failed to
             track a Black face) reported by Forbes, not independently verified here.
Paraphrase:  Repeats and timestamps the incident; a repetition supports that the
             claim was made, not that it is independently true.
Locators:    Body paragraphs 1-4; parallels in the closing paragraphs.
Quote:       Google spokesperson: "There is still clearly a lot of work to do with
             automatic image labeling."
```

```text
URL:         https://www.cbc.ca/news/trending/google-photos-black-people-gorillas-1.3135754
Kind:        secondary. Contemporaneous news coverage. Read firsthand (HTTP 200).
             Reproduces Alcine's screenshot (credited "Jacky Alcine/Twitter") and
             embeds both key tweets.
Establishes: Independent confirmation of the tweet wording and Zunger's reply, and
             the "appalled and genuinely sorry" statement. Notes the word "also has
             racist connotations." Attributes to the NYT (2015) that Google
             "decided to temporarily remove the gorilla label, including the
             application's ability to search for gorillas." The word "temporarily"
             is the 2015 framing; the 2018 and 2023 tests show the removal was not
             temporary.
Paraphrase:  A second independent outlet carrying the same wording; two retellings
             of one origin corroborate wording, not truth beyond it.
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
Paraphrase:  Second independent outlet reading the Times, matching PetaPixel on the
             multi-company result.
Locators:    Lede and paragraphs 2-5 (the rest of the piece is unrelated briefs).
Quote:       Alcine: "I'm going to forever have no faith in this AI."
```

```text
URL:         https://petapixel.com/2023/05/22/googles-photos-app-is-still-unable-to-find-gorillas/
Kind:        secondary. Same-day coverage of the NYT 2023 test. Read firsthand
             (HTTP 200). Independent of The Register.
Establishes: The detail behind the NYT test: the Times searched a collection of 44
             images; cats and kangaroos found, gorillas/baboons/chimpanzees/
             orangutans/monkeys not. Apple Photos: "It could accurately find photos
             of particular animals, except for most primates," gorilla matched only
             as text (Gorilla Tape). Google spokesman: benefit "does not outweigh
             the risk of harm." Also carries the 2015 Zunger "better recognition of
             dark-skinned faces" quote and the widely repeated claim that Google's
             training data had too few photos of Black people. That training-data
             claim is a causal explanation repeated in coverage; I did not find
             Google stating it in those exact terms in a primary source (Zunger's
             tweet names "better recognition of dark-skinned faces" as a fix area,
             which implies but does not assert the training-gap cause).
Paraphrase:  Supplies the 44-image scope and the 2023 Google "risk of harm"
             framing that a primary I could open does not.
Locators:    Body paragraphs 1-12.
Quote:       Google spokesman: benefit "does not outweigh the risk of harm."
```

## Contradictions

- **Google could recognize gorillas by 2018; the Photos block was a choice, not
  an inability.** Wired's 2018 test (primary) found Google's Cloud Vision API and
  Google Assistant labeled a gorilla correctly (one image, "western gorilla," 94%
  confidence), while consumer Google Photos returned nothing. The 2023 Google
  statement frames it the same way: the benefit "does not outweigh the risk of
  harm." The lesson's non-fix point holds for Photos, but the precise claim is
  "Google chose not to enable primate labels in consumer Photos," not "Google
  never built a classifier that could tell a gorilla from a person."

- **The mechanism studies do not measure the gorilla error itself.** Gender
  Shades measured gender classification on Microsoft/IBM/Face++; Shankar measured
  geo-diversity and classifier performance on ImageNet and Open Images; Yang
  measured the demographic makeup of ImageNet's person subtree. None ran the
  Google Photos animal-labeling task or the 2015 misclassification. They are
  strong, converging evidence for the cause (representation skew produces worse
  recognition for underrepresented groups, and reference datasets under-represent
  dark skin) in the exact dataset ecosystem, and must be presented as the
  mechanism, not as a measurement of this incident.

- **The mechanism studies point at datasets, not at Google Photos' specific
  pipeline.** Google has never published the training set or the failure analysis
  for the 2015 Photos classifier. The representation cause is inferred from how
  this class of system is built and from these audits of the standard datasets,
  reinforced by Zunger's own "better recognition of dark-skinned faces" as a named
  fix area. It is a well-supported inference about cause, not a disclosed internal
  finding. Say so.

- **"Temporarily" vs. permanently.** CBC (2015), citing the NYT, called the label
  removal temporary. The 2018 and 2023 firsthand tests show it was not. If the
  draft quotes the 2015 "temporary" framing, it should be as a promise the record
  later contradicts.

- **The training-data cause is inferred, not quoted from a primary about Google.**
  Coverage widely says Google admitted too few Black faces in its training set.
  The primary I can open (Zunger, via contemporaneous embed) names "better
  recognition of dark-skinned faces" as a fix area, which implies the gap without
  stating it as the confirmed cause. Attribute carefully.

- **Contemporaneous parallels are single-sourced.** Forbes lists Flickr (2015,
  "apes"/"animals"), Nikon (2009, blink detection on Asian faces), and an HP
  webcam that failed to track a Black face. The commission allows a parallel only
  if firsthand-sourced. These come from one secondary outlet and are not verified
  against a firsthand record here; do not present them as confirmed.

## Numbers

```text
Figure: 34.7% - maximum gender-classification error, darker-skinned females (IBM)
Owner:  Gender Shades (Buolamwini & Gebru, 2018)
Scope:  PPB benchmark (1,270 subjects); IBM Watson Visual Recognition.
```

```text
Figure: 20.8% - darker-skinned-female error for the best of the three (Microsoft)
Owner:  Gender Shades
Scope:  PPB benchmark; still the worst subgroup even for the strongest system.
```

```text
Figure: 0.0% and 0.3% - lighter-skinned-male error rates (Microsoft, IBM)
Owner:  Gender Shades
Scope:  PPB benchmark; best-classified subgroup. Face++ best on darker males (0.7%).
```

```text
Figure: darker females = 21.3% of the benchmark but 61.0%-72.4% of all errors
Owner:  Gender Shades (Section 4.4)
Scope:  Share of PPB vs. share of total misclassifications across classifiers.
```

```text
Figure: >32% US-based, ~60% from six North American/European countries (Open Images);
        ~45% US-based (ImageNet); China ~1%, India ~2%
Owner:  Shankar et al. (2017)
Scope:  Country-level geo-location recovered for ~2M of 9M Open Images and a sample
        of ImageNet; shows the amerocentric/eurocentric training skew.
```

```text
Figure: 6.2% - average share of the "Dark" skin-color category across ImageNet
        person-subtree synsets
Owner:  Yang et al. (2020)
Scope:  13,900 annotated images across 158 safe, imageable person synsets; the
        measured under-representation of dark skin in the reference dataset.
```

```text
Figure: 2,832 person-subtree synsets (~8.3% of ImageNet images); only 158 judged
        both safe and imageable
Owner:  Yang et al. (2020)
Scope:  ImageNet person subtree; the rest include non-imageable and offensive
        categories (racial and gender slurs inherited from WordNet).
```

```text
Figure: 40,000 images - Wired's 2018 test collection
Owner:  Wired (Simonite, 2018)
Scope:  Uploaded to Google Photos; no hits for gorilla, chimp, chimpanzee, monkey.
```

```text
Figure: 44 images - the New York Times' 2023 test collection
Owner:  New York Times (2023), via PetaPixel's reading (not verified against the
        Times' own page, which is gated here).
Scope:  Searched in Google Photos; cats/kangaroos found, primates not.
```

```text
Figure: 94% confidence - Google Cloud Vision "western gorilla" tag on one image
Owner:  Wired (Simonite, 2018)
Scope:  Cloud Vision API online demo, single image; recognition worked outside Photos.
```

```text
Figure: ~2 hours - gap from Alcine's first post to Zunger's reply
Owner:  Derived from tweet snowflake IDs (01:22:43 to 03:07:56 UTC, 2015-06-29)
Scope:  Same night; corroborated by Forbes ("within hours").
```

## Source assets

```text
Asset: Gender Shades, Table 4 - gender-classification error rates by subgroup
       (DF/DM/LF/LM) for Microsoft, IBM, Face++.
Shows: The whole mechanism in one grid: near-zero error for lighter males,
       20.8%-34.7% for darker females.
Crop:  Keep the four subgroup columns, all three vendor rows, the error-rate row,
       and the caption naming the systems. Omit nothing that changes the reading.
```

```text
Asset: Shankar et al., Figure 3 - density plots of model confidence for
       groom/bridegroom images from Hyderabad vs. the standard test set.
Shows: The same concept is recognized far less confidently when it comes from an
       under-represented locale. The representation cause made visible.
Crop:  Keep both the Hyderabad curve and the standard-test curve in one panel;
       a single curve loses the comparison that is the point.
```

```text
Asset: Yang et al., Figure 4 - distribution of gender, skin color, and age across
       ImageNet person-subtree synsets.
Shows: The under-representation of dark skin (6.2% average) and of female across
       the dataset that trains image classifiers.
Crop:  Retain the skin-color panel with its axis; do not crop to a single synset.
```

```text
Asset: Alcine's original screenshot - the Google Photos album header reading
       "Gorillas" over the two photos.
Shows: The failure itself, in the product's own interface. The most direct visual
       in the story.
Crop:  Originates from the now-deleted tweet; reproduced in CBC's 2015 report
       credited "Jacky Alcine/Twitter." Rights and provenance must be checked
       before any use, and it is a photo of real people who were harmed; handle
       with the care the commission's sensitivity note requires. Not decorative.
```

## Discarded

```text
URL: https://web.archive.org/web/20150703000351/https://twitter.com/jackyalcine/status/615329515909156865
     (and the Zunger/follow-up snapshots) - Genuine contemporaneous Wayback
     captures of the deleted/protected tweets EXIST (confirmed via the archive.org
     availability API: Alcine's original was captured 2015-07-03). But the snapshot
     content host web.archive.org is unreachable from this environment: curl is
     reset at the tunnel across repeated attempts, WebFetch hard-blocks the domain,
     the Memento aggregator (timetravel.mementoweb.org) no longer resolves, and
     Arquivo.pt returned no captures. I did not open and read the snapshot, so I do
     not cite it as a read source. Recorded here so a later researcher on an
     unrestricted network can retrieve it directly and promote it to a readable
     primary.
```

```text
URL: https://gendershades.org/ - The project's own results site. Did not resolve in
     this environment (connection reset). The peer-reviewed paper is the stronger
     primary and was read in full, so nothing is lost.
```

```text
URL: https://r.jina.ai/... and web.archive.org / archive.ph|li|md|vn for the NYT
     2023 article - All blocked or reset here. Recorded so the access failure is on
     the record. NYT findings are corroborated by two independent outlets instead.
```

```text
URL: https://carmona.mx/2023/05/22/... - An IFTTT auto-repost of the NYT article.
     Carries only headline and dek, not the body. No independent value.
```

```text
URL: Museum of Failure, Colorlines, HuffPost, Gigazine, Slashdot, BoingBoing,
     Techmeme, CNN, CBS, Fox, SBS, gulfnews, Indianapolis Recorder - Additional
     retellings of the same origin. Not cited: they add repetition, not independent
     confirmation, and the record already has enough.
```
