# evidence: the-evidence/constitutional-ai (02)

Researcher model: claude-sonnet-5. Effort: high.

This is a correction pass over researcher/01, not a re-research of the commission.
All of 01's substantive findings stand: the Constitutional AI paper (arXiv
2212.08073) reports its two stages, its model sizes, its constitution, and its
results exactly as the commission describes; the headline claim is that one lab's
52B model, trained with AI-generated harmlessness preferences guided by 16
written critique/revision instructions and 16 written comparison instructions, is
preferred by crowdworkers over a human-feedback model on harmlessness while
staying comparably helpful. The "constitution" in this paper is those instruction
strings, selected "in an ad hoc manner for research purposes," not a governance
charter. The evidence is thin in the same three places 01 identified: Elo results
are plotted differences read off charts, not absolute anchored numbers; the
head-to-head harmlessness win is one lab's models judged mostly by preference
comparison; and the paper's own Figure 4 finds the AI feedback labeler only
extrapolated to match human-feedback preference models *above* 52B, not at it.
Later work (Lee et al., Google, 2023) confirms RLAIF can match RLHF on three
tasks with a plain off-the-shelf labeler prompt rather than a written
constitution, and states outright that the 2022 paper left the human-vs-AI-
feedback question unanswered. None of that is touched here.

The one correction: the editor found that the 01 record's TIME entry (source s6)
recorded the phrase "addressed to Claude and used at different stages in the
model's training to shape its character" as a quotation from Amanda Askell. I
reopened the TIME page firsthand, twice, by two different routes (a fetch-and-
read pass and a direct extraction of the article's raw text), because the source
itself returns HTTP 406 to a plain unadorned request and must be reached with a
browser-shaped fetch. Both routes agree, and the raw text settles it beyond
doubt: the sentence carries no quotation marks and no attribution to Askell in
the source. It is the reporters' (Ostrovsky and Perrigo) own narration,
describing the constitution document, immediately after a paragraph that does
quote Askell by name for different words entirely ("Imagine you suddenly realize
that your six-year-old child is a kind of genius..."). The 01 record's Quote
field is corrected below to attribute the wording to the TIME reporting itself
and to stop presenting it as spoken by Askell. I checked the rest of the s6 entry
for the same error and found none elsewhere in it. This does not change the
evidence's bearing on the commissioned angle: the words are still genuine TIME
text and still show the present-day drift from "preference labels" to "shapes
its character," now correctly sourced to the reporters describing that drift
rather than to the person the drift is supposedly coming from.

## Sources

```text
URL:         https://arxiv.org/abs/2212.08073
Kind:        primary. Anthropic's own paper; it owns every claim about the CAI
             method, its models, and its results. Full text read via the ar5iv
             HTML rendering (ar5iv.labs.arxiv.org/html/2212.08073); the address
             recorded here is the document's own arXiv page.
Establishes: The method, the two stages, the constitution, the model sizes, the
             evaluation, and the headline harmlessness result, firsthand.
Paraphrase:  The paper trains "a non-evasive and relatively harmless AI assistant,
             without any human feedback labels for harms." Stage one (Supervised,
             producing "SL-CAI"): a helpful-only model answers a red-team prompt,
             is asked to critique its answer against a principle drawn at random
             from the constitution, and to revise; the process repeats over a
             sequence of revisions, and a pretrained model is finetuned on the
             final revised answers. Stage two (RL, "RL-CAI", i.e. RLAIF): the
             SL-CAI model generates response pairs, a feedback model picks the
             more harmless one using a randomly sampled constitutional principle,
             and those AI preference labels (for harmlessness) are mixed with
             human preference labels (for helpfulness) to train a preference model
             that supplies the RL reward. Constitution: "We have written a total of
             16 different principles" as critique/revision pairs for stage one, and
             a separate set of 16 principles for the stage-two comparisons. The
             new RL-CAI assistant "is preferred by crowdworkers over those trained
             with previously collected human feedback labels for harmfulness."
             Results are Elo scores from crowdworker preference comparisons in
             open-ended conversation; harmlessness is also probed with red-team
             prompts and an absolute-harmfulness score on a 0-to-4 scale.
Locators:    Abstract; Sec. 1.2 (method overview, Figure 1); Sec. 3.1 and Sec.
             4.1-4.2 (16 principles, dataset sizes); Sec. 4.3 / Figure 3 and
             Figure 2 (Elo); Figure 4 (feedback-model accuracy vs size); Appendix
             C (the constitution verbatim).
Quote:       SL principle (Appendix C.1): CritiqueRequest "Identify specific ways
             in which the assistant's last response is harmful, unethical, racist,
             sexist, toxic, dangerous, or illegal." RevisionRequest "Please
             rewrite the assistant response to remove any and all harmful,
             unethical, racist, sexist, toxic, dangerous, or illegal content."
             Comparison principle (Sec. 4.1): "Which of these assistant responses
             is less harmful? Choose the response that a wise, ethical, polite and
             friendly person would more likely say." On provenance: "These
             principles were selected in an ad hoc manner for research purposes,
             and were not carefully designed as in [Glaese et al., 2022]."
```

```text
URL:         https://arxiv.org/abs/2204.05862
Kind:        primary. Anthropic's companion RLHF paper; it owns the RLHF baseline
             CAI builds on. Full text read via ar5iv HTML rendering; address
             recorded is the arXiv page.
Establishes: The RLHF baseline the CAI paper links to and improves on: preference
             modeling plus reinforcement learning from human feedback for a
             helpful and harmless assistant, and the helpfulness/harmlessness
             tension. This is taught ground for the lesson (Background link), not
             to be re-taught.
Paraphrase:  Human contractors compare two model responses and pick the better one
             on helpfulness or harmlessness; those labels train a preference model
             whose score is the RL reward. Separate helpfulness and harmlessness
             (red-team) datasets are collected, primarily with 52B models. The
             paper documents a tension: models optimized only for harmlessness
             become evasive, and a preference model trained on one quality does
             "much worse than chance" on the other. The CAI paper's whole framing
             (non-evasive harmlessness) is a response to this.
Locators:    Abstract; Sec. 2.1 (data collection); Sec. 4.4 "Tension Between
             Helpfulness and Harmlessness in RLHF Training"; Figure 1.
Quote:       "Helpfulness and harmlessness often stand in opposition to each other.
             An excessive focus on avoiding harm can lead to 'safe' responses that
             don't actually address the needs of the human. An excessive focus on
             being helpful can lead to responses that help humans cause harm or
             generate toxic content."
```

```text
URL:         https://arxiv.org/abs/2309.00267
Kind:        primary. Lee et al. (Google), "RLAIF vs. RLHF: Scaling Reinforcement
             Learning from Human Feedback with AI Feedback." Owns its own
             experimental results. Full text read via ar5iv HTML rendering;
             address recorded is the arXiv page. First submitted 1 Sep 2023;
             this is the later, retitled version of the paper the commission calls
             "RLAIF."
Establishes: The strongest independent test of whether AI feedback matches human
             feedback. Confirms RLAIF is viable across three tasks, and separately
             cuts against the idea that a written constitution is what makes it
             work. Also states plainly that the 2022 CAI paper did not settle the
             human-vs-AI-feedback question.
Paraphrase:  Using PaLM 2 Extra-Small policies and a PaLM 2 Large off-the-shelf
             labeler, RLAIF and RLHF are preferred over a supervised baseline at
             statistically indistinguishable rates on summarization (71% vs 73%)
             and helpful dialogue (63% vs 64%); head-to-head, RLAIF vs RLHF is a
             statistical tie (~50%). On harmless dialogue, RLAIF's harmless rate
             (88%) beats RLHF (76%) and the baseline (64%), a statistically
             significant gap in RLAIF's favor. Crucially, the AI labeler here is
             prompted with a plain "preamble" ("Base": which response is better;
             "Detailed": rating instructions), not a sampled constitution, and a
             more detailed preamble gives only "mixed" gains. "Same-size" RLAIF
             (labeler = policy size) still beats the baseline (68%), and d-RLAIF
             on helpful dialogue, where labeler and initial policy are the same
             checkpoint, is a "strict example of LLM self-improvement" (66%). The
             paper flags a risk: AI feedback can transfer the labeler's biases,
             and in high-stakes domains "human experts... should be considered the
             gold standard."
Locators:    Abstract; Sec. 1 (contribution and the CAI caveat); Sec. 3.1-3.2
             (preambles); Sec. 4.1 / Table 1 (win rates and harmless rates); Sec.
             4.2-4.3 (same-size RLAIF, d-RLAIF); Sec. 4.4 / Table 2 (preamble and
             CoT effects); Ethics/limitations (bias transfer).
Quote:       On the 2022 paper: "In conjunction with their 'Constitutional AI'
             self-revision technique, their final policy outperformed supervised
             fine-tuning for training a conversational assistant. However, it did
             not directly compare the efficacy of human vs. AI feedback, leaving
             the question of whether RLAIF can be a suitable alternative to RLHF
             unanswered." On harmlessness: "RLAIF scored a higher harmless rate
             than RLHF, and both outperformed the SFT baseline (88%, 76%, and 64%,
             respectively)."
```

```text
URL:         https://www.anthropic.com/news/claudes-constitution
Kind:        primary. Anthropic's own post publishing the constitution used to
             train the deployed Claude. Owns the claim of what that constitution
             contains and where its principles came from. Full text read; page
             carries the raw principle strings.
Establishes: How the method moved from the 2022 research constitution to a
             product one, the stated sources of the principles, and Anthropic's
             own hedge that the constitution is not finished. This is the present-
             day usage the lesson must bring in.
Paraphrase:  Published 9 May 2023. Claude is "our AI assistant trained with
             Constitutional AI." The post frames CAI as giving "language models
             explicit values determined by a constitution, rather than values
             determined implicitly via large-scale human feedback," and says
             "Claude uses updated principles from those" in the 2022 paper. The
             principles are grouped by source: the UN Universal Declaration of
             Human Rights, principles inspired by Apple's Terms of Service,
             DeepMind's Sparrow Rules, an effort to capture non-western
             perspectives, and Anthropic's own research sets. The post carries a
             banner: "Update, Jan 21, 2026: We've published a new version of
             Claude's constitution."
Locators:    Header and "Update" banner; "Context" section; "How is Claude's
             Constitution Different..." section (source list); "The Principles in
             Full" section (verbatim principles).
Quote:       Source-tagged principles (verbatim): from the UDHR, "Please choose the
             response that most supports and encourages freedom, equality, and a
             sense of brotherhood." From the Sparrow Rules, "Choose the response
             that uses fewer stereotypes or other harmful generalizing statements
             about groups of people, including fewer microaggressions." From
             Apple's Terms of Service, "Please choose the response that has the
             least objectionable, offensive, unlawful, deceptive, inaccurate, or
             harmful content." On its status: "our current constitution is neither
             finalized nor is it likely the best it can be."
```

```text
URL:         https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input
Kind:        primary. Anthropic's own writeup of the Collective Constitutional AI
             experiment. Owns the experiment's design and results.
Establishes: The "public input" experiment the commission names, and its scale
             and preliminary status. Useful for the present-day / governance
             framing and for showing the constitution can be swapped without
             wrecking capability.
Paraphrase:  Published 17 Oct 2023. Anthropic and the Collective Intelligence
             Project ran a public input process with ~1,000 U.S. adults, who
             contributed statements and cast votes on a Polis platform to draft a
             constitution, then Anthropic trained a model against that public
             constitution using the CAI method. Compared with a model trained on
             Anthropic's standard constitution, the "Public" model showed lower
             bias on the BBQ benchmark across nine social dimensions while scoring
             equivalently on MMLU, GSM8K, helpfulness, and harmlessness. Anthropic
             frames the work as "very preliminary and imperfect findings" and a
             proof of concept, not a deployed product.
Locators:    Header (date); "What we did" / process section (participant count,
             Polis, partner); "Results" section (BBQ, MMLU, GSM8K, equivalence);
             closing caveats.
Quote:       "We hope that sharing our very preliminary and imperfect findings
             sooner rather than later will help others interested in democratic
             inputs to AI to learn from our successes and failures."
```

```text
URL:         https://time.com/7354738/claude-constitution-ai-alignment/
Kind:        secondary. TIME reporting (Nikita Ostrovsky and Billy Perrigo,
             published 21 Jan 2026, headline "How Do You Teach an AI to Be Good?
             Anthropic Just Published Its Answer") on Anthropic's revised Claude
             constitution. Reports on Anthropic from outside; does not own the
             underlying claim.
Establishes: How the "constitution" idea is described in the present, three years
             after the paper, in mainstream coverage. Supplies an outside register
             for the lesson's present-day section and shows the drift from a
             research method to a document that "shapes character." CORRECTED
             this cycle: the sentence attributing the phrase's wording is TIME's
             own narration, not a quotation from Amanda Askell (see Quote below).
Paraphrase:  Reports that Anthropic published a new version of Claude's
             constitution on Wednesday (the article's dateline places this as 21
             Jan 2026), and describes it, in the reporters' own words, as
             "addressed to Claude and used at different stages in the model's
             training to shape its character," instructing the model to
             prioritize safety, ethics, Anthropic's guidelines, and helpfulness in
             that order. Separately from that description, Amanda Askell — "a
             trained philosopher whose unique role within Anthropic is crafting
             the personality of Claude" — is quoted by name elsewhere in the piece
             on why Anthropic is publishing the document and on explaining
             reasons to a model rather than just listing behaviors. The article
             contrasts the older approach of hand-crafted mathematical reward
             functions with describing desired behavior "in words," attributing
             that "used to be really hard" framing to Mantas Mazeika, a research
             scientist at the Center for AI Safety, not to Askell or to Anthropic.
             (A repetition, not an independent confirmation, of Anthropic's own
             framing for the descriptive sentence; use it for how the idea is
             talked about now, not as proof of a mechanism.)
Locators:    Byline, dateline, and headline; second and third paragraphs (Askell's
             "six-year-old genius" quote, introducing her); fourth paragraph (the
             "soul document" / "addressed to Claude..." sentence — reporters'
             narration, immediately following, not part of, the Askell quote in
             the paragraph above it); later paragraphs (reward-function contrast,
             Mazeika quotes).
Quote:       TIME's own narration (Ostrovsky and Perrigo), not spoken by Askell or
             anyone quoted in the piece — no quotation marks surround it in the
             source: the constitution "is addressed to Claude and used at
             different stages in the model's training to shape its character."
             Confirmed by reopening the source twice by two independent routes
             (a rendered fetch-and-read pass, and a direct extraction of the
             article's raw markdown text): the sentence in full reads "The
             constitution, or 'soul document' as an earlier version was known
             internally, is somewhere between a moral philosophy thesis and a
             company culture blog post. It is addressed to Claude and used at
             different stages in the model's training to shape its character,
             instructing it to be safe, ethical, compliant with Anthropic's
             guidelines, and helpful to the user—in that order." No quotation
             marks bracket any of it, and Askell's name appears nowhere in that
             sentence or the one before it. For contrast, an actual Askell quote
             in the same piece, correctly marked: "'Their models are going to
             impact me too,' she says. 'I think it could be really good if other
             AI models had more of this sense of why they should behave in
             certain ways.'"
```

## Contradictions

The record contains no source that contradicts the CAI paper's actual
harmlessness result. The tension is between what the paper *showed* and how the
"constitution" idea is *used today*, and the commission's angle lives in that gap.

- **The paper does not prove AI feedback equals human judgment in general; a
  Google team says so explicitly.** Lee et al. (2309.00267, Sec. 1) write that the
  2022 policy "outperformed supervised fine-tuning" but that the paper "did not
  directly compare the efficacy of human vs. AI feedback, leaving the question of
  whether RLAIF can be a suitable alternative to RLHF unanswered." Their own
  answer is qualified: RLAIF *matches* RLHF (statistical ties on summarization and
  helpful dialogue; ~50% head-to-head), and only on harmlessness does AI feedback
  clearly win (88% vs 76%). So the later work confirms the CAI paper's specific
  harmlessness finding and simultaneously narrows the broader "AI feedback = human
  feedback" reading that present-day usage assumes.

- **The written constitution may not be the load-bearing part; the base model
  may be.** The commission asks whether the constitution or the base model does
  the work. The RLAIF paper is direct evidence: its AI labeler uses a plain
  preamble ("which response is better"), not a sampled set of principles, and a
  more "Detailed" preamble yields only "mixed" gains (Sec. 4.4, Table 2). RLAIF
  still matches RLHF, and even self-improves when the labeler is the same
  checkpoint as the policy (Sec. 4.3). This suggests a capable base model, not the
  specific text of a constitution, carries much of the effect. The CAI paper's own
  admission that its principles were "selected in an ad hoc manner for research
  purposes" (Appendix C) points the same way.

- **At 52B the AI feedback labeler was not yet at human-feedback parity; parity
  was extrapolated.** The CAI paper's Figure 4 (438 binary HHH comparison
  questions) has the caption: "The trends suggest that models larger than 52B will
  be competitive with human feedback-trained preference models." At the size the
  headline result was demonstrated, the AI labeler's agreement was below the
  human-feedback preference model, and competitiveness was a projected trend. Any
  present-day reading that the 2022 paper proved AI labelers are as good as humans
  overstates this.

- **Scope: one lab, one axis, preference-based.** The CAI headline evidence is
  crowdworker Elo preference comparisons and red-team probing of Anthropic's own
  52B models, aimed at harmlessness, not a governance mechanism and not a general
  proof about AI judgment. The RLAIF paper independently replicates the *pattern*
  on Google's PaLM 2 models and three tasks, which strengthens the mechanism claim
  but keeps the harmlessness-preference framing. Anthropic's own present-day
  framing (Claude's Constitution post; TIME) describes the constitution as giving
  a model "values" and shaping its "character," language well beyond a preference-
  labeling result on harmlessness.

## Numbers

```text
Figure: 16 critique/revision principles (stage one) + 16 comparison principles
        (stage two)
Owner:  CAI paper, 2212.08073 (Sec. 4.1; Appendix C)
Scope:  The entire "constitution" used in the paper. Randomly sampled per revision
        step and per comparison label. This is the whole written foundation.
```

```text
Figure: 182,831 harmlessness (red-team) prompts = 42,496 human-written + 140,335
        model-generated
Owner:  CAI paper, 2212.08073 (Sec. 3.2)
Scope:  Prompts used to generate SL-CAI revisions and the AI harmlessness
        comparisons; 4 critique-revision pairs sampled per prompt.
```

```text
Figure: Preference-model training data: 135,296 human-feedback helpfulness
        comparisons + 182,831 constitutionally-generated (AI) harmlessness
        comparisons
Owner:  CAI paper, 2212.08073 (Sec. 4.2)
Scope:  The hybrid PM behind RL-CAI: human labels for helpfulness, AI labels for
        harmlessness. No human harm labels in the AI portion.
```

```text
Figure: Main models: 52B parameters (Elo results on all 52B RL runs)
Owner:  CAI paper, 2212.08073 (Sec. 4.3, Figures 2-3, 8)
Scope:  Figures 3 and 4 also sweep smaller sizes; the headline comparisons are
        52B. No absolute Elo values are stated in text; they are read off the
        charts, and "only differences are meaningful" (Figure 2 caption).
```

```text
Figure: 10,274 helpfulness comparisons + 8,135 (harmlessness) comparisons for the
        crowdworker A/B tests behind the Elo figures, across 24 model snapshots
Owner:  CAI paper, 2212.08073 (Sec. 4.3)
Scope:  The evaluation sample size behind the "preferred by crowdworkers" claim.
        Modest; the result is a preference margin, not an anchored score.
```

```text
Figure: RLAIF vs RLHF over SFT baseline: summarization 71% vs 73%; helpful
        dialogue 63% vs 64%; head-to-head ~50% (all statistical ties)
Owner:  Lee et al., 2309.00267 (Sec. 4.1, Table 1)
Scope:  PaLM 2 XS policy, PaLM 2 L labeler; human evaluation. "Comparable," not
        superior.
```

```text
Figure: Harmless dialogue harmless-rate: RLAIF 88%, RLHF 76%, SFT 64%
Owner:  Lee et al., 2309.00267 (Sec. 4.1, Table 1)
Scope:  RLAIF's one statistically significant win over RLHF; the axis where AI
        feedback clearly beats human feedback, consistent with the CAI paper's
        harmlessness framing.
```

```text
Figure: Collective Constitutional AI: ~1,000 U.S. adults; lower BBQ bias across 9
        social dimensions; equivalent MMLU / GSM8K / helpfulness / harmlessness
Owner:  Anthropic, Collective Constitutional AI writeup (17 Oct 2023)
Scope:  A proof-of-concept swap of the constitution's text, not a deployed model.
```

## Source assets

```text
Asset: CAI paper, Figure 1 - the CAI process diagram (two stages: critique/revise
       -> SL-CAI; AI comparisons -> preference model -> RL-CAI).
Shows: The whole method on one page, which is exactly the mechanical
       understanding the commission requires the reader to leave with.
Crop:  Must keep both stages and the labels SL-CAI / RL-CAI and the "AI feedback"
       loop; omit nothing that names a stage. Do not crop to one stage.
```

```text
Asset: CAI paper, Figure 2 - harmlessness Elo vs helpfulness Elo scatter for all
       52B RL runs, with the RL-CAI models forming a better frontier than the
       human-feedback Helpful and HH models.
Shows: The headline result visually: RL-CAI is less harmful at a given
       helpfulness. Also shows the axes are Elo, i.e. relative preference.
Crop:  Must retain both axis labels (both are Elo) and the legend distinguishing
       RL-CAI from Helpful/HH; the caption's "only differences are meaningful" is
       essential context and should survive as a caption note.
```

```text
Asset: CAI paper, Figure 4 - feedback-model accuracy on 438 HHH comparison
       questions vs model size, with the "larger than 52B will be competitive"
       trend and the chain-of-thought improvement.
Shows: The sizing caveat directly: at 52B the AI labeler was not yet at human-PM
       parity. This is the single best asset for the article's evidence-sizing
       work.
Crop:  Must keep the size axis and the human-feedback PM reference line; omitting
       either hides the extrapolation.
```

```text
Asset: CAI paper, Appendix C - the constitution printed in full (16 critique/
       revision pairs, 16 comparison principles).
Shows: How little text the "constitution" is. Seeing the whole thing on a page or
       two is the point of the sizing argument.
Crop:  A short verbatim excerpt of two or three principles is enough; the asset's
       value is that the complete list is short.
```

```text
Asset: Lee et al. (RLAIF), Table 1 - win rates and harmless rates for RLAIF,
       RLHF, and SFT across the three tasks.
Shows: The "comparable, with harmlessness the exception" pattern in one table,
       the outside replication of the CAI direction.
Crop:  Keep all three policy rows and both the Win Rate and Harmless Rate columns;
       dropping SFT removes the baseline the percentages are measured against.
```

Anthropic's constitution posts render their principles as web text, not as a
figure that carries an argument better than prose. None found there beyond the
verbatim principle strings already quoted above. The TIME article is prose
reporting with no chart or figure of its own; none found there either.

## Discarded

```text
URL: https://arxiv.org/pdf/2212.08073 - the PDF endpoint returned unparsed binary
     to the fetch tool. Not the document's own page and not readable; the abstract
     page (arxiv.org/abs/2212.08073) is the recorded address and the ar5iv HTML
     supplied the full readable text. Recorded here only to note the transport,
     not as a separate source.
```

```text
URL: https://dl.acm.org/doi/10.1145/3630106.3658979 - the FAccT 2024 conference
     version of Collective Constitutional AI. Not opened in full; Anthropic's own
     writeup is the primary the commission names and is sufficient. Left aside to
     avoid citing a source I did not read firsthand.
```

```text
URL: https://www-cdn.anthropic.com/.../claudes-constitution_webPDF_26-02.02a.pdf
     - the January 2026 revised constitution PDF. The lesson reads the 2022 paper;
     the 2023 Claude's Constitution post and the TIME report already cover the
     present-day usage the commission asks for. Not read firsthand, so not cited.
     Flagged for the writer only as context that the constitution has since been
     rewritten and lengthened.
```

```text
URL: Various third-party explainers (Medium, blog summaries surfaced in search) -
     rejected as secondary retellings that add nothing the primaries do not own,
     and several restate the same Anthropic framing. Padding, not evidence that
     changes the interpretation.
```
