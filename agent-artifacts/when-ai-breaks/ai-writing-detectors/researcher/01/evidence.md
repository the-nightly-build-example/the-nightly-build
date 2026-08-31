# Evidence record: when-ai-breaks/ai-writing-detectors (01)

The record supports the commissioned angle firsthand. The incident is verified
end to end from owning sources: Turnitin launched an AI-writing detector in April
2023 with a claimed false-positive rate under 1% and later conceded through its
own chief product officer that the real-world rate ran higher; a peer-reviewed
study (Liang et al., Patterns, 2023) measured a 61.22% average false-positive
rate on non-native English (TOEFL) essays against near-perfect accuracy on native
US essays, and tied the gap to text perplexity; a second peer-reviewed study
(Sadasivan et al., 2023) proved a mathematical ceiling on any detector and showed
paraphrasing collapses real detectors; OpenAI withdrew its own AI Text Classifier
on July 20, 2023 after it identified only 26% of AI text while false-flagging
human text 9% of the time; and Vanderbilt University disabled Turnitin's detector
on August 16, 2023, citing the 1% claim against its own 75,000-paper volume and
the non-native bias. The evidence is thin in two places, both recorded below: the
two vendor/primary pages that most directly own their figures (OpenAI's blog post
and Turnitin's own blog) return HTTP 403 to automated fetch, so their exact
numbers are recorded from the primary text as reproduced verbatim across
independent secondaries and cross-checked, rather than read off the owning page in
this pass; and the harshest false-positive numbers come from mid-2023 detector
versions and from specific or small samples, which the record marks so the writer
does not generalize them past their scope.

## Sources

```text
URL:         https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/
Kind:        primary — OpenAI's own announcement of its AI Text Classifier; OpenAI
             owns the accuracy figures and the withdrawal note. Gated: the page
             returns HTTP 403 to automated fetch (not dead). Figures below are the
             primary's own wording as reproduced verbatim in the secondaries cited
             (Search Engine Land, TechCrunch, and the classifier's widely quoted
             launch text); confirm on the live page before publication.
Establishes: OpenAI launched the classifier Jan 31, 2023; at launch it correctly
             identified 26% of AI-written text as "likely AI-written" (true
             positives) and mislabeled human text as AI 9% of the time (false
             positives); OpenAI itself warned reliable detection of all AI text is
             impossible; OpenAI withdrew the tool on July 20, 2023 for low accuracy.
Paraphrase:  A first-party classifier from the largest AI vendor performed poorly on
             its own numbers and was pulled within six months, which is the strongest
             possible admission that this class of detector does not reliably work.
Locators:    Body of the launch post; the reliability caveat in the same post; the
             July 20, 2023 editor's note appended to the top of the post.
Quote:       Editor's note (verbatim, confirmed via Search Engine Land): "As of July
             20, 2023, the AI classifier is no longer available due to its low rate
             of accuracy." Launch figures (verbatim): "our classifier correctly
             identifies 26% of AI-written text (true positives) as 'likely
             AI-written,' while incorrectly labeling human-written text as AI-written
             9% of the time (false positives)."
```

```text
URL:         https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7
             (published version; gated 403 to automated fetch)
             Full text read at the authors' arXiv preprint: https://arxiv.org/abs/2304.02819
Kind:        primary — peer-reviewed study; the five authors own the measurements.
Establishes: The bias against non-native English writers, quantified, and the
             perplexity mechanism behind it.
Paraphrase:  Seven commercial GPT detectors were run on human-written corpora. On
             TOEFL essays by non-native English speakers the detectors averaged a
             61.22% false-positive rate, and all seven unanimously flagged 18 of 91
             TOEFL essays (19.78%) as AI-authored, while accuracy on native US
             eighth-grade essays was near-perfect. The unanimously flagged essays had
             significantly lower text perplexity, and rewriting TOEFL essays with
             richer vocabulary cut the average false-positive rate from 61.22% to
             11.77%. This isolates the signature detectors key on: predictable,
             lower-perplexity word choice, which is exactly what limited-vocabulary
             or non-native writing produces.
Locators:    Results (detector false-positive rates on TOEFL vs. US essays);
             perplexity analysis; the word-enhancement experiment.
Quote:       "average false positive rate: 61.22%"; "All seven detectors unanimously
             identified 18 of the 91 TOEFL essays (19.78%) as AI-authored"; on
             enhancement "the average false positive rate decreasing by 49.45% (from
             61.22% to 11.77%)".
```

```text
URL:         https://arxiv.org/abs/2303.11156
Kind:        primary — peer-reviewed study (arXiv, later published in Transactions
             on Machine Learning Research); the five authors own the theorem and the
             attack measurements.
Establishes: A theoretical ceiling on any detector, and that paraphrasing defeats
             deployed detectors.
Paraphrase:  The paper proves the AUROC of the best-possible detector is bounded by
             the total-variation distance between human and AI text distributions:
             as models get better at imitating human text that distance shrinks and
             the best detector approaches a coin flip. Empirically, a light
             paraphraser applied on top of a language model collapses real detectors:
             DetectGPT's AUROC falls from 96.5% to 25.2%; OpenAI's own
             RoBERTa-Large detector drops from 100% to 60% true-positive rate at a 1%
             false-positive rate; a retrieval-based detector falls from 100% to below
             60%; and recursive paraphrasing drops watermark detection from 99.3% to
             9.7%, while human raters judged 77% of paraphrased passages to preserve
             content and 89% to keep grammar.
Locators:    Abstract; Theorem 1 / Section 4 (the bound); Section 3 and Figure 7
             (attack and spoofing results).
Quote:       Bound: "AUROC(D) ≤ 1/2 + TV(M,H) − TV(M,H)²/2". Attacks (abstract):
             DetectGPT AUROC "from 96.5% to 25.2%"; RoBERTa-Large detector TPR@1%FPR
             "from 100% to 60%"; watermark detection "from 99.3% to 9.7%".
```

```text
URL:         https://www.vanderbilt.edu/brightspace/2023/08/16/guidance-on-ai-detection-and-why-were-disabling-turnitins-ai-detector/
Kind:        primary — the university's own published decision; Vanderbilt owns the
             fact that it disabled the tool and its stated reasons.
Establishes: A named institution disabling Turnitin's detector, with date and its
             own scaling of the risk; independent restatement of Turnitin's 1% claim
             and of the non-native bias.
Paraphrase:  Vanderbilt's Brightspace/Center for Teaching announced on August 16,
             2023 that it had disabled Turnitin's AI detection tool "for the
             foreseeable future." It scaled the risk against its own volume: at
             Turnitin's claimed 1% false-positive rate, of the roughly 75,000 papers
             Vanderbilt submitted to Turnitin in 2022, about 750 could have been
             wrongly flagged. It cited false accusations, the documented bias against
             non-native English speakers, Turnitin's refusal to explain its method,
             the collapse of competing detectors, privacy, and the possibility that
             reliable detection is not achievable.
Locators:    Full announcement, dated August 16, 2023, 7:00 AM.
Quote:       "Turnitin claimed that its detection tool had a 1% false positive rate";
             "around 750 student papers could have been incorrectly labeled" out of
             the ~75,000 submitted in 2022; "AI detectors have been more likely to
             label text written by non-native English speakers as AI-written."
```

```text
URL:         https://www.turnitin.com/blog/the-launch-of-turnitins-ai-writing-detector-and-the-road-ahead
Kind:        primary — Turnitin's own launch statement; Turnitin owns the launch
             date and its claimed false-positive rate. Gated: the whole turnitin.com
             domain returns HTTP 403 to automated fetch (not dead). The central claim
             (April 2023 launch, sub-1% claimed false-positive rate) is confirmed
             independently by Vanderbilt and Inside Higher Ed below.
Establishes: Turnitin launched its AI-writing detector in April 2023 and claimed a
             false-positive rate under 1%.
Paraphrase:  Turnitin turned the detector on for its existing customer base in April
             2023 and marketed a sub-1% false-positive rate. The scale is the
             installed base of Turnitin itself (thousands of institutions, millions
             of students), not a separate rollout.
Locators:    Launch blog post; Turnitin's press page and product guidance carry the
             same claim.
Quote:       Claim as restated by Vanderbilt and by Inside Higher Ed: "a less than 1
             percent false positive rate." (Direct quotation from the owning page not
             captured this pass because turnitin.com refused automated fetch.)
```

```text
URL:         https://www.insidehighered.com/news/quick-takes/2023/06/01/turnitins-ai-detector-higher-expected-false-positives
Kind:        secondary — trade reporting; reports Turnitin's own walk-back from
             outside the company.
Establishes: The vendor's own concession that real-world false positives ran higher
             than claimed, and the specific mitigations.
Paraphrase:  Annie Chechitelli, Turnitin's chief product officer, said the detector
             has a higher false-positive rate than the company originally asserted,
             attributing the gap to the difference between lab testing and real-world
             use. Turnitin gave a sentence-level false-positive rate of roughly 4%,
             against the document-level under-1% it claimed at the April 2023 launch,
             and added an asterisk warning on any result under 20% AI, where false
             positives concentrate.
Locators:    Article dated June 1, 2023.
Quote:       Chechitelli is "Turnitin's chief product officer"; the sentence-level
             false-positive rate is "approximately 4 percent"; the tool now shows "an
             asterisk with a message casting some doubt" below 20%.
```

```text
URL:         https://www.k12dive.com/news/turnitin-false-positives-AI-detector/652221/
Kind:        secondary — trade reporting; reports Turnitin's own usage figures and
             concession.
Establishes: Deployment scale in the first weeks and the concentration of false
             positives below 20% AI.
Paraphrase:  As of May 14, 2023, 38.5 million submissions had gone through Turnitin's
             detector; 9.6% of documents were reported as over 20% AI writing and
             3.5% as over 80%. Turnitin acknowledged a higher incidence of false
             positives when a document reads under 20% AI, and added the asterisk for
             that band. Chechitelli did not disclose the exact discovered
             false-positive rate.
Locators:    Article dated June 7, 2023.
Quote:       "As of May 14, 38.5 million submissions have gone through the tool, with
             9.6% of those documents reporting over 20% of AI writing and 3.5% over
             80% of AI writing."
```

```text
URL:         https://www.washingtonpost.com/technology/2023/08/14/prove-false-positive-ai-detection-turnitin-gptzero/
Kind:        secondary — reporting on named student cases. Gated: paywall/403 to
             automated fetch this pass; the concrete case details should be read from
             the live article before the writer names any student.
Establishes: Real students were accused on detector output, and a small hands-on
             test produced a high false-positive rate.
Paraphrase:  The Post reported students at several universities falsely accused of AI
             use, with graduation delayed in some cases, and describes a small test in
             which detectors false-flagged a large share of human-written essays
             (reported around 50% on a small sample). Treat the ~50% as a small-sample
             illustration, not a measured rate.
Locators:    Article dated August 14, 2023. Specific student names not captured this
             pass (paywall); retrieve from the live page.
Quote:       Not captured verbatim this pass (gated). Turnitin's standing guidance,
             widely quoted from this period: its detection "should not be used as the
             sole basis for adverse actions against a student."
```

```text
URL:         https://searchengineland.com/openai-ai-classifier-no-longer-available-429912
Kind:        secondary — reporting that reproduces OpenAI's editor's note verbatim.
Establishes: The exact wording and date of OpenAI's withdrawal note, and OpenAI's
             launch caveat.
Paraphrase:  Confirms the July 20, 2023 note added to OpenAI's original post and that
             OpenAI had warned at launch it was impossible to reliably detect all
             AI-written text.
Locators:    Article dated July 2023.
Quote:       "As of July 20, 2023, the AI classifier is no longer available due to its
             low rate of accuracy."
```

```text
URL:         https://techcrunch.com/2023/07/25/openai-scuttles-ai-written-text-detector-over-low-rate-of-accuracy/
Kind:        secondary — reporting confirming the withdrawal.
Establishes: Independent second confirmation of the July 20, 2023 addendum and
             OpenAI's stated follow-up.
Paraphrase:  Reports the July 20 addendum to the classifier post and OpenAI's
             statement that it was researching more effective provenance techniques.
Locators:    Article dated July 25, 2023.
Quote:       OpenAI addendum as quoted: "We are working to incorporate feedback and
             are currently researching more effective provenance techniques for text."
```

## Contradictions

- Vendor claim versus independent measurement (the commission's central dispute).
  Turnitin marketed a false-positive rate under 1% at the April 2023 launch
  [turnitin.com launch post, restated by Vanderbilt and Inside Higher Ed].
  Independent and peer-reviewed measurement is far worse for specific populations
  and setups: Liang et al. found a 61.22% average false-positive rate on non-native
  TOEFL essays [Patterns], and the Washington Post's small hands-on test flagged
  roughly half of human essays [WaPo]. The strongest version of Turnitin's side is
  that these are not the same quantity: Turnitin's under-1% is a document-level rate
  on general submissions, while Liang's 61% is a per-document rate on a specifically
  hard, non-native corpus and the WaPo figure is a tiny sample. The strongest
  version of the critics' side is that Turnitin's own chief product officer conceded
  the real-world rate is higher than claimed, quoted a ~4% sentence-level rate, and
  bolted on an under-20% asterisk [Inside Higher Ed; K12 Dive] — the vendor moved
  toward the critics. What would settle it: a single, pre-registered false-positive
  rate on a defined population (including non-native writers) at a fixed decision
  threshold, measured on the shipping model, published by an independent party. No
  such agreed figure exists in the record.

- OpenAI's own numbers contradict the premise that detection works. OpenAI, which
  builds the models being detected, could identify only 26% of AI text and
  false-flagged human text 9% of the time, and withdrew the tool [OpenAI]. This
  undercuts any vendor claim of reliable detection, including near-perfect marketing
  numbers.

- Withdrawal versus caveat. OpenAI fully withdrew its classifier [OpenAI]. Turnitin
  did not withdraw; it kept selling the detector and added warnings and an asterisk
  [Inside Higher Ed; K12 Dive]. The commission's phrase "operators walked back" is
  accurate for OpenAI (withdrawal) but for Turnitin means caveated, not removed —
  keep that distinction in the draft.

- Theory versus market. Sadasivan et al. prove the best-possible detector approaches
  chance as models improve, and that paraphrasing collapses deployed detectors
  [arXiv 2303.11156], while vendors continued to sell detection into consequential
  academic decisions. This is the "where the weakness lives now" contradiction the
  commission asks the close to carry.

## Numbers

```text
Figure: 26% of AI-written text correctly identified (true positives)
Owner:  OpenAI, "New AI classifier for indicating AI-written text"
Scope:  OpenAI's "challenge set" of English texts, at launch (Jan 31, 2023)
```

```text
Figure: 9% of human-written text incorrectly labeled AI (false positives)
Owner:  OpenAI, same post
Scope:  Same challenge set, at launch
```

```text
Figure: withdrawn July 20, 2023 for "low rate of accuracy"; launched Jan 31, 2023
Owner:  OpenAI, editor's note on the same post
Scope:  The AI Text Classifier product, whole lifetime under six months
```

```text
Figure: under 1% false-positive rate (claimed at launch, document level)
Owner:  Turnitin, launch blog post (restated by Vanderbilt and Inside Higher Ed)
Scope:  April 2023 launch marketing; document level, general submissions
```

```text
Figure: ~4% false-positive rate (sentence level, conceded)
Owner:  Annie Chechitelli, Turnitin chief product officer (via Inside Higher Ed)
Scope:  Real-world use, sentence level, ~June 2023
```

```text
Figure: 38.5 million submissions processed; 9.6% flagged >20% AI, 3.5% >80% AI
Owner:  Turnitin (via K12 Dive)
Scope:  As of May 14, 2023, cumulative since April launch
```

```text
Figure: 61.22% average false-positive rate on non-native (TOEFL) essays
Owner:  Liang et al., Patterns (2023)
Scope:  7 commercial GPT detectors, 91 TOEFL essays by non-native English speakers
```

```text
Figure: 18 of 91 TOEFL essays (19.78%) flagged AI unanimously by all seven detectors
Owner:  Liang et al., Patterns (2023)
Scope:  Same 91-essay TOEFL corpus; these had significantly lower text perplexity
```

```text
Figure: near-perfect accuracy on native US eighth-grade essays
Owner:  Liang et al., Patterns (2023)
Scope:  US 8th-grade student essay corpus; contrast to the 61.22% above
```

```text
Figure: false-positive rate fell 61.22% -> 11.77% after vocabulary enhancement
Owner:  Liang et al., Patterns (2023)
Scope:  TOEFL essays rewritten with richer word choice; isolates the perplexity signal
```

```text
Figure: best-possible detector AUROC <= 1/2 + TV(M,H) - TV(M,H)^2/2
Owner:  Sadasivan et al. (2023), Theorem 1
Scope:  Any detector; TV is total-variation distance between human and AI text
```

```text
Figure: DetectGPT AUROC 96.5% -> 25.2% under paraphrasing
Owner:  Sadasivan et al. (2023)
Scope:  Zero-shot detector, paraphrasing attack
```

```text
Figure: OpenAI RoBERTa-Large detector TPR@1%FPR 100% -> 60% under paraphrasing
Owner:  Sadasivan et al. (2023)
Scope:  Trained neural detector, paraphrasing attack
```

```text
Figure: watermark detection rate 99.3% -> 9.7% under recursive paraphrasing
Owner:  Sadasivan et al. (2023)
Scope:  Watermarking scheme, recursive paraphrasing attack
```

```text
Figure: ~750 of ~75,000 papers potentially wrongly flagged
Owner:  Vanderbilt University (Aug 16, 2023 announcement)
Scope:  Vanderbilt's 2022 Turnitin volume at Turnitin's claimed 1% false-positive rate
```

## Source assets

```text
Asset: Liang et al., Patterns — the bar chart of per-detector false-positive rates
       on TOEFL (non-native) essays versus US eighth-grade (native) essays (Figure 1).
Shows: The whole thesis in one image: the same seven detectors are near-perfect on
       native essays and wildly wrong on non-native ones.
Crop:  Must keep both the TOEFL and US-essay bars and the detector labels so the
       contrast is legible; omit nothing that carries the axis scale.
```

```text
Asset: Liang et al., Patterns — the perplexity comparison of unanimously flagged
       TOEFL essays versus the rest.
Shows: The mechanism — flagged essays have measurably lower perplexity (more
       predictable word choice).
Crop:  Retain the axis label naming perplexity and both groups.
```

```text
Asset: Sadasivan et al. (2023) — ROC curves before and after paraphrasing.
Shows: A detector's curve collapsing toward the diagonal (chance) once text is
       paraphrased.
Crop:  Keep the diagonal reference line and both curves; omit unrelated panels.
```

```text
Asset: OpenAI blog post — the launch text stating 26% true-positive / 9%
       false-positive on the challenge set, plus the July 20, 2023 editor's note.
Shows: A first-party admission, in the vendor's own words, that its detector barely
       worked and was pulled.
Crop:  The editor's note line and the one sentence carrying both percentages.
```

```text
Asset: Vanderbilt announcement — the passage scaling 1% against ~75,000 papers to
       ~750 students.
Shows: How a "low" rate becomes hundreds of accusations at institutional scale.
Crop:  The sentence with both the 75,000 and 750 figures.
```

## Discarded

```text
URL: https://web.archive.org/web/2023id_/https://openai.com/blog/new-ai-classifier... — fetch tool cannot reach web.archive.org; could not use to recover the gated OpenAI page.
URL: https://cdn.production.openai.com/blog/new-ai-classifier-for-indicating-ai-written-text — DNS did not resolve; OpenAI CDN not reachable.
URL: https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf — returned raw binary PDF, unreadable as text; superseded by the arXiv full text.
URL: https://fast.io/resources/turnitin-ai-detector-review-2026/ — vendor-adjacent SEO review, not an owning source for any figure.
URL: https://www.popularai.org/... , https://undetectable.ai/... , https://humanizerai.com/... , https://www.undetectedgpt.ai/... — "AI humanizer" marketing blogs with a stake in the claim; not usable as evidence.
URL: https://www.sciencedaily.com/releases/2023/07/230710113921.htm — press-release retelling of Liang et al.; the primary paper is cited instead.
URL: https://qz.com/... , https://decrypt.co/... , https://dig.watch/... , https://www.searchenginejournal.com/... — further retellings of the OpenAI withdrawal; two secondaries (Search Engine Land, TechCrunch) already confirm it.
```
