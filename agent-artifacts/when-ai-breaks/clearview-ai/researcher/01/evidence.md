# Evidence record: when-ai-breaks/clearview-ai (01)

The record supports the lesson's spine: Clearview AI built a facial-recognition
product by scraping billions of photographs from the public web without consent,
turned each into a biometric code, and sold identification searches against that
database to police, and regulators on four continents found the practice
unlawful. The scraped-database scale is firmly established and grows by date: a
regulator (OAIC) confirms "more than three billion images" in 2021, a UK court
records "over 20 billion" in October 2022, and the Dutch regulator records "more
than 30 billion" in 2024. Every European fine (France, Italy, Greece, the
Netherlands) rests on the same two findings I could read in full: the images
become Article 9 biometric data, and Clearview had no lawful basis and no consent
for them. The consent failure is unambiguous. The accuracy story is more precise
than the commission's angle assumes and is set out under Contradictions:
Clearview markets a 1:1 NIST verification score of 99%+, but that test is not the
1:many identification its product performs, and the one regulator to rule on
identification accuracy (OAIC) found Clearview took no reasonable steps to ensure
the matches it disclosed were accurate.

The record is thin in three places, each flagged below: the ICO fine is currently
unenforced and its substance is still undecided (jurisdiction reinstated on appeal
in 2025, remitted, further appeal pending); the European fines are largely
uncollected because Clearview has no EU establishment; and Kashmir Hill's
originating NYT investigation is paywalled and I could not open it directly, so
its scale figure rests here on the OAIC's independent finding of the same number.

## Sources

```
URL:         https://www.oaic.gov.au/news/media-centre/clearview-ai-breached-australians-privacy
Kind:        primary — the Australian Information Commissioner's own determination announcement; the regulator owns the finding.
Establishes: OAIC determination of 3 November 2021 (Commissioner-initiated investigation, determination [2021] AICmr 54). Commissioner Angelene Falk found Clearview breached the Privacy Act 1988 by collecting Australians' sensitive information without consent, by unfair means, without notice; by failing to take reasonable steps to ensure the personal information it DISCLOSED was accurate; and by failing to implement compliance systems. Ordered Clearview to cease collecting facial images/biometric templates from people in Australia and destroy existing ones. Database "more than three billion images."
Paraphrase:  Australia's regulator ruled the scraping-and-matching practice unlawful, ordered cessation and destruction, and — uniquely — faulted the accuracy of the identifications Clearview handed to clients, not just the collection.
Locators:    Media release body; findings list; Falk quotes.
Quote:       "When Australians use social media or professional networking sites, they don't expect their facial images to be collected without their consent by a commercial entity to create biometric templates for completely unrelated identification purposes." / "The covert collection of this kind of sensitive information is unreasonably intrusive and unfair." / "By its nature, this biometric identity information cannot be reissued or cancelled."
```

```
URL:         https://www.dpa.gr/en/en/enimerwtiko/prakseisArxis/imposition-fine-clearview-ai-inc
Kind:        primary — the Hellenic Data Protection Authority's own decision page.
Establishes: HDPA Decision 35/2022, 13 July 2022, EUR 20,000,000 fine. Breaches of GDPR Articles 5(1)(a), 6, 9, and 12/14/15/27. The Authority held the images become biometric data processed without an Article 9 legal ground; prohibited further collection/processing of people in Greece by facial recognition; ordered deletion of data already held. Case opened on a complaint by the NGO Homo Digitalis on behalf of a data subject whose access request Clearview did not satisfy.
Paraphrase:  Greece's regulator imposed its then-largest fine and a processing ban, on the same biometric-data and no-legal-basis grounds as the other EU authorities, triggered by an ignored access request.
Locators:    Decision summary; article list; complaint origin.
Quote:       Found the company "violated the principles of lawfulness and transparency."
```

```
URL:         https://caselaw.nationalarchives.gov.uk/ukftt/grc/2023/819
Kind:        primary — the UK First-tier Tribunal's judgment, Clearview AI Inc v The Information Commissioner [2023] UKFTT 819 (GRC).
Establishes: The ICO issued an Enforcement Notice and a Monetary Penalty Notice to Clearview on 18 May 2022, alleging infringements of GDPR/UK GDPR Articles 5, 6, 9, 14, 15-17, 21, 22 and the Article 35 DPIA duty. The database was estimated at "over 20 billion images" in October 2022 and rising. All Clearview clients "carry out criminal law enforcement and/or national security functions," in the USA and countries including Panama, Brazil, Mexico and the Dominican Republic. The Tribunal ALLOWED Clearview's appeal on 17 October 2023, holding the ICO lacked jurisdiction: the processing was related to monitoring UK behaviour but fell outside the material scope of the GDPR because it was carried out for foreign states' law-enforcement/national-security functions (Article 2(2)(a) GDPR; not "relevant processing" under Article 3(2A) UK GDPR).
Paraphrase:  The court that heard the UK fine records how the product works, the 20-billion figure, the breaches alleged, and then set the fine aside on a jurisdiction point — not on the merits of the privacy findings.
Locators:    paras 3-4 (notices, articles alleged); para 24 (client countries); para 26 (clients' functions); para 40 (over 20 billion images); paras 1-2, 155-156 (disposition and jurisdiction reasoning).
Quote:       "In October 2022 it was estimated that the Database included over 20 billion images and increasing as new images are scraped." / "All of CV's clients carry out criminal law enforcement and/or national security functions."
```

```
URL:         https://www.gov.uk/administrative-appeals-tribunal-decisions/the-information-commissioners-office-v-clearview-ai-inc-privacy-international-intervening-2025-ukut-319-aac
Kind:        primary — the Upper Tribunal's judgment, Information Commissioner v Clearview AI Inc [2025] UKUT 319 (AAC).
Establishes: On 6 October 2025 the Upper Tribunal (Mrs Justice Heather Williams, Judges Church and Butler) set aside the FTT decision, holding the FTT "erred materially in law" and that the ICO DID have jurisdiction: Clearview's processing is within the territorial scope of the UK GDPR and is "monitoring of behaviour," read broadly to include automated collection, sorting, classification and storage without human involvement. It upheld three of the ICO's four grounds and remitted the case to the FTT to decide the substance of the notices. (Per the ICO, Clearview was later granted permission to appeal to the Court of Appeal — see Contradictions; this is the live status.)
Paraphrase:  The higher court reinstated the ICO's authority over Clearview and sent the fine's substance back to be decided; the jurisdiction question is resolved for now, the validity of the fine itself is not.
Locators:    Decision summary; disposition; behavioural-monitoring holding.
Quote:       The FTT "erred materially in law in finding that the Respondent's processing was outside the material scope of the GDPRs by operation of Article 2(2)(a)." / disposition: "allowed the appeal, set aside the decision of the First-tier Tribunal, and remitted the matter to the First-tier Tribunal."
```

```
URL:         https://www.aclu-il.org/cases/aclu-v-clearview-ai/
Kind:        primary (party) — the ACLU of Illinois's account of the case it litigated and settled. Party to the settlement; frames its own win.
Establishes: ACLU v. Clearview AI, filed in the Circuit Court of Cook County, Illinois on 28 May 2020 under the Illinois Biometric Information Privacy Act (BIPA), which requires written consent before capturing a person's biometric identifier (including a faceprint). Clearview's motion to dismiss was denied in August 2021. A court-approved settlement (May 2022) permanently bans Clearview, nationwide, from selling access to its faceprint database to most private entities, and for five years bars access to any Illinois state/local agency, including police.
Paraphrase:  The US outcome came under a state biometric-consent law, not federal privacy law; the settlement restricts who Clearview may sell to rather than shutting the database.
Locators:    Case page: court, filing date, claim, settlement terms.
Quote:       (settlement effect, from ACLU) "Clearview can no longer treat people's unique biometric identifiers as an unrestricted source of profit."
```

```
URL:         https://www.aclu.org/press-releases/big-win-settlement-ensures-clearview-ai-complies-with-groundbreaking-illinois
Kind:        primary (party) — the national ACLU's settlement announcement. Corroborates and adds detail to the ACLU-IL entry.
Establishes: Settlement filed 9 May 2022. Terms: permanent nationwide bar on giving paid or free access to the faceprint database to private entities (a narrow BIPA financial-institution exception aside); five-year bar on access for Illinois state/local government and private entities; an opt-out form for Illinois residents backed by $50,000 in advertising; an end to free trial accounts for individual officers acting without their department's authorization; continued filtering of Illinois-sourced photographs. Attributed to Nathan Freed Wessler (ACLU).
Paraphrase:  Gives the enforceable terms of the US settlement in the plaintiff's words.
Locators:    Press release body; terms list.
Quote:       "Clearview can no longer treat people's unique biometric identifiers as an unrestricted source of profit."
```

```
URL:         https://www.clearview.ai/press-room/clearview-ai-wins-appeal-against-uk-information-commissioner-office-ico-fine
Kind:        primary (party) — Clearview AI's own statement. Owns Clearview's characterization of itself and its defense; NOT independent verification of any fact.
Establishes: Clearview's public self-description and defenses: it "provides powerful and reliable facial recognition search engine technology to government agencies"; its data is "sourced from public-only web sources, including news media, mugshot websites, public social media, and many other open sources"; it welcomed the FTT reversal of "the ICO's 7.5 million pound fine and data deletion order." It rests its lawfulness case on public-source data and on serving law enforcement, and on the jurisdiction ruling rather than on consent.
Paraphrase:  Clearview does not claim it obtained consent; its defense is that the data was public and its customers are police, and (in the UK) that the regulator had no jurisdiction.
Locators:    Press statement body.
Quote:       "We are pleased with the tribunal's decision to reverse the U.K. ICO's unlawful order against Clearview AI." / data "sourced from public-only web sources."
```

```
URL:         https://www.clearview.ai/press-room/clearview-ais-facial-recognition-platform-achieves-superior-accuracy-and-reliability-across-all-demographics-in-nist-testing
Kind:        primary (party) — Clearview AI's own accuracy claim. Owns what Clearview asserts about accuracy; the underlying NIST result is public but the framing is Clearview's.
Establishes: Clearview submitted its algorithm to the NIST Facial Recognition Vendor Test (FRVT) 1:1 verification track (result dated 28 October 2021) and reports 99.81% on visa photos, 99.76% on mugshots, 99.7% on visa-border, 99.42% on border photos, and ">99 percent accuracy across all demographics." CEO Hoan Ton-That calls it "an unmistakable validation." The test is 1:1 verification (does probe photo A match reference photo A), not the 1:many identification (find this face among billions of scraped images) that Clearview's product performs.
Paraphrase:  Clearview's headline accuracy number measures a different task than its product does; see Contradictions.
Locators:    Press release body; NIST percentages; Ton-That quote; test-type note.
Quote:       "In another key test that evaluates demographic accuracy, Clearview AI's algorithm consistently achieved greater than 99 percent accuracy across all demographics."
```

```
URL:         https://www.hunton.com/privacy-and-cybersecurity-law-blog/cnil-fines-clearview-ai-20-million-euros-for-unlawful-use-of-facial-recognition-technology
Kind:        secondary — law-firm reporting of the CNIL decision. Used because the CNIL's own decision page (cnil.fr/en/facial-recognition-20-million-euros-penalty-against-clearview-ai) is where the decision lives but has been withdrawn/anonymized and no longer serves the text; figures here are uncontested and match the EDPB record.
Establishes: France's CNIL fined Clearview EUR 20 million on 17 October 2022, ordered it to stop collecting and to delete data of people in France within two months, on pain of EUR 100,000 per day thereafter. Findings: no consent for collection/use of images; no valid legitimate-interest basis given the intrusive collection and subjects' unawareness; failure to facilitate access and erasure rights; no response to the November 2021 formal notice.
Paraphrase:  France's fine turns squarely on absence of consent and of any lawful basis, plus non-cooperation.
Locators:    Article body; enforcement-order list.
Quote:       Clearview "was not collecting data subjects' consent for the collection and use of their picture" and could not rely on legitimate interests given "the intrusive character of the data collection and data subjects' lack of awareness."
```

```
URL:         https://www.lewissilkin.com/insights/2022/06/01/clearview-ai-not-in-the-clear-italian-dpa-fines-clearview-ai-20-million-102ho68
Kind:        secondary — law-firm reporting of the Italian Garante decision. Uncontested figures matching the EDPB record; used as a readable stand-in for the Garante decision text.
Establishes: Italy's Garante fined Clearview EUR 20 million (decision February 2022, published 9 March 2022), ordered deletion of data on people in Italy, and banned further processing of their facial biometrics. Breaches: Articles 5(1)(a)(b)(e) (transparency, purpose limitation, indefinite storage), 6 (no lawful basis), 9 (biometric data), 12, 13/14, 15, 27 (no EU representative). Database described as "over 10 billion faces" (February 2022) — a useful earlier point on the growth curve.
Paraphrase:  Italy's fine matches the French and Greek grounds and adds the storage-limitation and EU-representative failures; its 10-billion figure dates the database eight months before the UK court's 20-billion figure.
Locators:    Article body; GDPR-article list; database figure.
Quote:       Clearview "violated the storage limitation principle by keeping data indefinitely"; the Garante "ordered the controversial company to delete any data on Italian citizens it holds and banned it from carrying out any further processing of Italian citizens' facial biometrics."
```

```
URL:         https://www.hunton.com/privacy-and-information-security-law/dutch-regulator-fines-clearview-ai-30-5-million-euros
Kind:        secondary — law-firm reporting of the Dutch DPA decision. The regulator's own page (autoriteitpersoonsgegevens.nl) was unreachable to me (403/503); figures here are uncontested and match the EDPB record.
Establishes: The Dutch DPA (Autoriteit Persoonsgegevens) decided on 16 May 2024, announced 3 September 2024, a EUR 30.5 million fine. Database "more than 30 billion photos." Clearview "converts each photo into a unique biometric code" — Article 9 biometric data with no available exception, so processing is unlawful; also failures to inform individuals and to honour access requests. Ordered to stop, with further penalty payments if it does not. This is the most recent and largest European fine, and shows the same failure mode continuing in 2024.
Paraphrase:  The recurrence point: two years after the first EU fines, the practice, the scale (now 30 billion), and the legal defect are unchanged, and the fine is larger.
Locators:    Article body; database figure; Article 9 finding.
Quote:       "After collecting these photos from the Internet, Clearview AI converts each photo into a unique biometric code." / Clearview "cannot rely on any of the Article 9 exceptions to the general prohibition of processing sensitive data."
```

```
URL:         https://techcrunch.com/2022/05/23/clearview-uk-ico-fine/
Kind:        secondary — contemporaneous reporting of the ICO fine, used to confirm the fine amount and the Commissioner's words (the ICO's own page ico.org.uk was unreachable to me; 403).
Establishes: The ICO fine was "just over £7.5 million" (commonly reported exact figure £7,552,800), announced 23 May 2022 (notices dated 18 May 2022 per the FTT judgment). Clearview was ordered to stop obtaining and using UK residents' publicly available data and to delete it; database "20 billion+" images. Quote from Information Commissioner John Edwards.
Paraphrase:  Fixes the UK fine amount and the Commissioner on record, since the primary ICO page could not be opened here.
Locators:    Article body; fine figure; Edwards quote.
Quote:       John Edwards: "People expect that their personal information will be respected, regardless of where in the world their data is being used."
```

```
URL:         https://www.techdirt.com/2020/01/29/facial-recognition-company-clearview-lied-about-crime-solving-power-pitches-to-law-enforcement-agencies/
Kind:        secondary — reporting on Clearview's early marketing claims versus the NYPD's account.
Establishes: In early 2020 Clearview claimed it had "cracked a case of alleged terrorism in a New York City subway station ... in a matter of seconds"; the NYPD stated it "did not use Clearview technology to identify the suspect in the August 16th rice cooker incident" and named its own separate process. The NYPD also rejected Clearview's claims on an assault suspect (who "turned himself in") and a groping case (solved via tips). At that time Clearview reported it "finds matches 75% of the time" — meaning it surfaces some photo, not necessarily the right person — gave no false-positive rate, and had not submitted to NIST's testing.
Paraphrase:  Before its 2021 NIST submission, Clearview's accuracy case rested on sales claims a police department publicly disputed, and on a 75% "finds a match" figure that is not an identification-accuracy figure.
Locators:    Article body; NYPD statement; 75% figure.
Quote:       NYPD: "The NYPD did not use Clearview technology to identify the suspect in the August 16th rice cooker incident."
```

## Contradictions

- **Database size is a moving target, not a single number.** Every figure is
  true for its date: OAIC "more than three billion" (2021, echoing Hill's Jan
  2020 NYT figure); Garante "over 10 billion" (Feb 2022); FTT "over 20 billion"
  (Oct 2022); Dutch DPA "more than 30 billion" (2024). Clearview's own later
  self-reported figures (30 billion in March 2023, and CEO claims of 40-50
  billion) are company assertions without regulator confirmation and should be
  labelled as Clearview's claims, dated, not stated flat. What settles a figure:
  tie each number to its source and date; do not blend them.

- **The UK fine is not enforced, and its merits are undecided.** ICO fine imposed
  18 May 2022 → FTT set it aside on jurisdiction 17 October 2023 → UT reinstated
  ICO jurisdiction 6 October 2025 and remitted the substance to the FTT → per the
  ICO, Clearview was granted permission to appeal to the Court of Appeal
  (reported December 2025). So as of this record no UK penalty is currently
  payable and no court has ruled on whether the privacy findings themselves stand.
  The lesson must not say "the ICO fined Clearview £7.5m" without the appeal
  history. What would settle it: the FTT's remitted substantive decision and any
  Court of Appeal ruling.

- **Accuracy: the marketed number measures a different task than the product
  does.** Clearview's headline is NIST FRVT 1:1 *verification* (99%+): given two
  photos, are they the same person. Its product does 1:many *identification*:
  find one face among 20-30 billion scraped images, where false-match risk scales
  with database size and image quality. NIST's FRVT 1:1 result does not measure
  that. The only regulator to rule on the identifications Clearview actually
  delivered — the OAIC — found it took no reasonable steps to ensure their
  accuracy, and in 2020 Clearview offered only a 75% "finds a match" rate and no
  false-positive rate (Techdirt). Steelmanned both ways: Clearview's algorithm is
  genuinely strong at verification and NIST-tested; that is not evidence its
  police-facing identifications are accurate, and no independent 1:many
  identification-accuracy test on its scraped database is in this record. What
  would settle it: an independent 1:many identification-accuracy and
  false-positive evaluation on the deployed database, which does not exist here.

- **Fines imposed are not fines collected.** The EU fines (France, Italy, Greece,
  Netherlands) target a US company with no EU establishment; contemporaneous
  reporting (e.g. Italy's regulator, 2025) indicates the fines remain largely
  uncollected. If the lesson implies the fines were paid, that overstates the
  record. What would settle it: a regulator statement of amounts actually
  recovered.

- **Consent is not disputed by anyone, including Clearview.** No source, Clearview
  included, claims Clearview obtained consent. Clearview's defense is that the
  images were public and its customers are law enforcement, and (in the UK) that
  the regulator lacked jurisdiction. This is agreement on the facts, disagreement
  on whether they are lawful — worth stating plainly rather than as a clash of
  accounts.

## Numbers

```
Figure: more than 3 billion images (scraped)
Owner:  OAIC determination (3 Nov 2021), corroborating Kashmir Hill / NYT (18 Jan 2020)
Scope:  cumulative database as of ~2020-2021; images scraped from Facebook, YouTube, Venmo and other public web sources
```
```
Figure: over 10 billion faces
Owner:  Italian Garante (decision Feb 2022, published 9 Mar 2022)
Scope:  cumulative database as of early 2022
```
```
Figure: over 20 billion images
Owner:  UK First-tier Tribunal judgment [2023] UKFTT 819, para 40, citing October 2022 estimate
Scope:  cumulative database as of Oct 2022, "increasing as new images are scraped"
```
```
Figure: more than 30 billion photos
Owner:  Dutch DPA (decision 16 May 2024, announced 3 Sep 2024)
Scope:  cumulative database as of 2024
```
```
Figure: about £7.5 million (reported exact £7,552,800)
Owner:  ICO Monetary Penalty Notice, 18 May 2022 (currently set aside/unenforced pending remittal — see Contradictions)
Scope:  single UK penalty for processing UK residents' data
```
```
Figure: EUR 20 million (each)
Owner:  France CNIL (17 Oct 2022), Italy Garante (Feb 2022), Greece HDPA (Decision 35/2022, 13 Jul 2022)
Scope:  separate national penalties, each the maximum or near-maximum for that authority at the time; largely uncollected
```
```
Figure: EUR 5.2 million overdue penalty
Owner:  France CNIL (13 Apr 2023, announced 10 May 2023) for non-compliance with the Oct 2022 order
Scope:  additional to the EUR 20 million; over EUR 100,000/day accrual basis
```
```
Figure: EUR 30.5 million (plus up to EUR 5.1 million further penalty)
Owner:  Dutch DPA (16 May 2024 / 3 Sep 2024)
Scope:  largest single European penalty against Clearview to date
```
```
Figure: 99.81% / 99.76% / 99.7% / 99.42%
Owner:  Clearview AI, reporting NIST FRVT 1:1 verification (28 Oct 2021)
Scope:  1:1 verification on visa, mugshot, visa-border, border photo sets — NOT 1:many identification on the scraped database
```
```
Figure: ~75% "finds a match"; no false-positive rate given
Owner:  Clearview (as reported by Techdirt, Jan 2020)
Scope:  rate at which a search surfaces some photo, not identification accuracy
```
```
Figure: more than 600 law-enforcement agencies (2020), later 2,400+ (2023)
Owner:  Kashmir Hill / NYT (2020, origin, not opened directly here); later figure via 2023 reporting
Scope:  US agencies using or trialling the tool; treat the 2020 and 2023 figures as separate dated points
```

## Source assets

```
Asset: First-tier Tribunal judgment [2023] UKFTT 819, paras 24-26 — the plain description of how the product works (client uploads a "Probe Image"; the system returns matching scraped photos with source URLs; all clients are law-enforcement/national-security).
Shows: the mechanism, in a court's neutral words, for teaching how the tool actually operates without overstating the internal technology.
Crop:  text, not visual; quote the mechanism sentences rather than crop.
```
```
Asset: Database-size-over-time series (3B in 2020 → 10B Feb 2022 → 20B Oct 2022 → 30B 2024), each point owned by a named regulator or court.
Shows: the scraping never stopped and outran every fine; a small honest line/step chart of dated figures would carry this better than prose.
Crop:  if charted, label each point with its owner and date and mark that later Clearview self-reported figures (40-50B) are unverified company claims, kept distinct from regulator/court figures.
```
```
Asset: Clearview AI's own NIST press release — the ranked percentage table (99.81% etc.).
Shows: exactly what Clearview claims and on which test, so the lesson can set the marketed 1:1 number beside the untested 1:many reality.
Crop:  if shown, retain the test-type label (FRVT 1:1 verification); omitting it would let the number read as identification accuracy.
```
```
Asset: OAIC, HDPA, CNIL, Garante, Dutch DPA decisions — regulator text, no charts.
Shows: None found (no visual evidence beyond the decision text).
```

## Discarded

```
URL: https://www.cnil.fr/en/facial-recognition-20-million-euros-penalty-against-clearview-ai — the CNIL's own decision page; now returns a "no longer available" notice (CNIL anonymizes/withdraws published sanctions after a time limit). The decision text was not readable; substituted the Hunton report and noted the withdrawal.
URL: https://www.nytimes.com/2020/01/18/technology/clearview-privacy-facial-recognition.html — Kashmir Hill's originating investigation; paywalled and not fetchable here (nytimes.com blocked; web.archive.org and archive.today also unreachable). Its 3-billion figure is anchored instead on the OAIC primary, which independently found the same number. This is the record's one unopened load-bearing source.
URL: https://www.edpb.europa.eu/news/national-news/... — EDPB national-news article URLs resolved to the current news index rather than the archived items, so the DPA reproductions could not be read there; used the DPAs' own pages where reachable (HDPA) and readable reporting where not (CNIL, Garante, Dutch DPA).
URL: https://ico.org.uk/... (2022 fine and 2025 UT news pages) — returned 403 to my fetcher (gated, not dead; the pages resolve in a browser). The UK record is instead built on the court judgments themselves (National Archives FTT, GOV.UK UT), with TechCrunch confirming the fine figure and the Commissioner's quote.
URL: https://www.rollingstone.com/... (Hill book excerpt) — redirected to a paywall proxy (tollbit); not readable.
```
