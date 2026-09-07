# Evidence: the-instruments/math-benchmark (01)

The evidence firmly supports the commission's spine. The MATH paper owns the
dataset's construction (12,500 competition problems, 7,500 train / 5,000 test,
seven subjects, five difficulty levels, answers graded by exact match of a
`\boxed{}` string), and its own models scored in the single digits at release
(best 6.9%). Owning documents from later models trace the rise: Minerva 540B to
33.6% single-sample and 50.3% with majority voting (2022), Qwen2.5-Math-72B to
85.9% on the full test set (2024), and DeepSeek-R1 to 97.3% on MATH-500 (2025).
Three "the number misled" cases are each traceable to an owner: (1) the MATH-500
subset was carved out by OpenAI precisely because 4,500 of the 5,000 test
problems had been put into that lab's training data, and papers now report
"MATH-500" and "MATH" as if interchangeable; (2) exact-match grading both
undercounts correct answers on formatting (Minerva's SymPy fix recovered ~1%)
and overcounts wrong reasoning that reaches a right answer (Minerva found false
positives up to ~30% at Level 5); (3) MathArena documents 10-20% score inflation
on a competition-sourced benchmark it attributes to contamination, the same
web-mirrored provenance MATH has. Where the record is thin: no owning document
quantifies contamination of the MATH test set *specifically* (the cleanest
MATH-specific leakage fact is the PRM800K case); and the rise is not purely
artifact, since a three-time IMO gold medalist scored 90% and grading fixes moved
Minerva by only ~1%. The evidence does not undermine the angle, but it forces the
writer to say plainly that some of the climb is real capability, not only leakage
and loose grading.

## Sources

```text
URL:         https://arxiv.org/abs/2103.03874
Kind:        primary. The paper that introduces MATH; owns the dataset's design,
             size, grading procedure, and release-era model scores.
Establishes: Title "Measuring Mathematical Problem Solving With the MATH Dataset";
             authors Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora,
             Steven Basart, Eric Tang, Dawn Song, Jacob Steinhardt; v1 5 Mar 2021,
             v2 8 Nov 2021; NeurIPS 2021. MATH is 12,500 competition problems,
             each with a full step-by-step solution. An auxiliary pretraining set
             (AMPS) is also released. The paper's thesis: accuracy stays low even
             with very large Transformers, and scaling alone will not get there.
Paraphrase:  MATH holds 12,500 challenging competition math problems, each with a
             worked solution; even large Transformers score low, and the authors
             argue scaling budgets and parameters will be impractical for strong
             math reasoning if trends hold.
Locators:    Abstract; title/author block; submission history.
Quote:       "we introduce MATH, a new dataset of 12,500 challenging competition
             mathematics problems." / "scaling is not currently solving MATH."
```

```text
URL:         https://ar5iv.labs.arxiv.org/abs/2103.03874
Kind:        primary. Full-text HTML of the same paper (arXiv's own render);
             read for the numbers and procedure the abstract omits.
Establishes: Train/test split 7,500 / 5,000. Seven subjects: Prealgebra, Algebra,
             Number Theory, Counting and Probability, Geometry, Intermediate
             Algebra, Precalculus. Difficulty levels 1-5, level 1 easiest (early
             AMC 8-style), level 5 hardest (AIME). Sources include AMC 10, AMC 12,
             AIME and other competitions. Grading: the model must emit the final
             answer inside \boxed{}, and the parser compares that string to the
             ground truth. Release-era scores: GPT-2 with AMPS 5.4% (0.1B), 6.2%
             (0.3B), 6.4% (0.7B), 6.9% (1.5B); GPT-3 13B fine-tuned 5.6%; GPT-3
             175B few-shot 5.2%. Human baselines: a CS PhD student ~40%; a
             three-time IMO gold medalist 90%, his misses "exclusively due to
             small arithmetic mistakes." Step-by-step solutions in training raised
             accuracy ~10% over question-answer-only; making the model generate
             its own steps before answering *decreased* accuracy versus emitting
             the answer directly.
Paraphrase:  Answers are scored by parsing the \boxed{} content and string-matching
             it to the reference; the reported percentage is the fraction of test
             problems whose extracted final answer matches, nothing about the
             reasoning.
Locators:    Dataset section (subjects, levels, split); grading/evaluation section;
             results tables; human-baseline discussion.
Quote:       "We can consequently evaluate a model's output by parsing what is
             inside the `\boxed{}` command and comparing that with the ground truth
             answer."
```

```text
URL:         https://github.com/hendrycks/math
Kind:        primary. The dataset's official repository (the authors' release
             point); owns license and canonical description.
Establishes: License MIT. Repository provides "dataset loaders and evaluation
             code." Citation block confirms NeurIPS 2021. Download now points to a
             Hugging Face mirror (qwedsacf/competition_math) and AMPS via Google
             Drive; the original HF path is gone (see next entry).
Paraphrase:  The authors distribute MATH under MIT with loader and grading code,
             and now route downloads through a third-party HF mirror.
Locators:    README top matter; citation section; download links.
Quote:       (BibTeX) "title={Measuring Mathematical Problem Solving With the MATH
             Dataset}, ... journal={NeurIPS}, year={2021}".
```

```text
URL:         https://huggingface.co/datasets/hendrycks/competition_math
Kind:        primary. The canonical HF dataset card for MATH; owns the record of
             its own removal and the exact field schema.
Establishes: The dataset at this path is DISABLED under a DMCA takedown notice.
             Schema per problem: `problem`, `solution` (step-by-step, final answer
             in \boxed), `level` (Level 1-5), `type` (subject). Counts: 7,500 train,
             5,000 test; total ~7.92 MB. Sources named: AMC 10, AMC 12, AIME. This
             is direct evidence that the problems are copyrighted competition
             content, widely mirrored, which bears on contamination.
Paraphrase:  The most-used distribution of MATH was pulled for copyright; the
             underlying problems are competition IP, which is exactly the material
             that saturates the public web models train on.
Locators:    Dataset card banner (takedown notice); "Data Fields"; "Data Splits".
Quote:       "This dataset has been disabled due to a DMCA takedown notice."
```

```text
URL:         https://arxiv.org/abs/2305.20050
Kind:        primary. Lightman et al. (OpenAI), "Let's Verify Step by Step";
             owns the definition of the MATH-500 subset and why it exists.
Establishes: Authors Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards,
             Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever,
             Karl Cobbe; submitted 31 May 2023. They put 4,500 of the 5,000 MATH
             test problems into their training data (PRM800K), so they evaluate on
             the remaining 500, chosen uniformly at random, and show (their Fig. 5)
             the 500 match the full test set's distribution of subjects and levels.
             Their best process-reward model solves 78.2% of the 500 via best-of-
             1860 sampling.
Paraphrase:  MATH-500 is the 500 test problems OpenAI did NOT train on, defined as
             a workaround after 4,500 test problems leaked into their own training
             set; it is a representative sample, not a harder or curated subset.
Locators:    Evaluation / "MATH" subset section; Figure 5; results.
Quote:       "We selected these 500 test problems uniformly at random." /
             "Our process-supervised model solves 78% of problems from a
             representative subset of the MATH test set."
```

```text
URL:         https://ar5iv.labs.arxiv.org/html/2206.14858
Kind:        primary. Lewkowycz et al. (Google Research), "Solving Quantitative
             Reasoning Problems with Language Models" (Minerva); owns Minerva's
             MATH scores and a documented analysis of automatic-grading error.
Establishes: Minerva MATH accuracy: 8B 14.1%, 62B 27.6%, 540B 33.6% (single
             sample); 540B with majority voting (maj1@64) 50.3%. They cite the
             prior published SOTA on MATH as 6.9% (Hendrycks et al. 2021). Grading:
             answers checked by SymPy equivalence (parse LaTeX, subtract, simplify
             to zero), which improved overall accuracy ~1% over plain string match
             (62B 26.5% -> 27.6%) by catching format-equivalent answers such as
             1/sqrt(3) vs sqrt(3)/3 -- i.e. false negatives from exact match.
             They also manually estimate FALSE POSITIVES (right final answer,
             flawed reasoning): average ~8%, rising with difficulty to ~30% at
             Level 5. They state they cannot automatically verify the reasoning
             chain, only the final answer.
Paraphrase:  Minerva both raised the MATH ceiling and documented that the score is
             a noisy proxy in two directions: exact match wrongly fails correct
             answers written in another notation, and it passes wrong reasoning
             that lands on the right number, worst at the hardest level.
Locators:    Table 3 (scores by size); Section 4.2 / Table 5 (false positives);
             Appendix D.1 / Table 6 (SymPy normalization).
Quote:       "SymPy equivalence is determined by parsing the answers via
             sympy.parsing.latex.parse_latex and then checking whether subtracting
             the two resulting SymPy objects and applying sympy.simplify gives
             zero." / "we do not have an automatic way of verifying the
             correctness of the model's [reasoning]."
```

```text
URL:         https://arxiv.org/html/2409.12122v1
Kind:        primary. Qwen team (Alibaba), Qwen2.5-Math technical report; owns
             its own MATH scores on the full test set.
Establishes: Qwen2.5-Math-72B-Instruct 85.9 on MATH (4-shot chain-of-thought);
             7B-Instruct 83.6; base 72B 66.8. Submitted 18 Sep 2024. The table
             header is "MATH" (4-shot); the report does not state on-page whether
             this is the full 5,000-problem test set or MATH-500 -- an ambiguity
             worth flagging, since the label alone does not disambiguate.
Paraphrase:  By late 2024 a specialized open model reported mid-80s on MATH under
             the plain "MATH" label, without the page pinning down which set.
Locators:    Results table (Table 3), "MATH" column.
Quote:       column header "MATH" "4-shot"; "Qwen2.5-Math-72B-Instruct ... 85.9".
```

```text
URL:         https://arxiv.org/html/2501.12948v1
Kind:        primary. DeepSeek-AI, DeepSeek-R1 report; owns R1's MATH-500 score
             and reports o1/V3 for comparison.
Establishes: DeepSeek-R1 97.3% on MATH-500 (Pass@1); OpenAI o1-1217 96.4%;
             DeepSeek-V3 90.2%. Benchmark labeled "MATH-500 (Pass@1)." Dated
             22 Jan 2025. Note ownership: R1's 97.3% is DeepSeek's own; the o1
             96.4% is DeepSeek reporting a competitor's figure (OpenAI owns that
             number at source), so treat 96.4% as "as reported by DeepSeek."
Paraphrase:  By 2025 frontier reasoning models report MATH-500 at 96-97%, and the
             leading labs report the 500-problem subset, not the full test set --
             the same name the 2021 paper and Minerva used for 5,000 problems.
Locators:    Table 4, "MATH-500 (Pass@1)" column.
Quote:       "MATH-500 (Pass@1)" with "DeepSeek-R1 ... 97.3" and "OpenAI-o1-1217
             ... 96.4".
```

```text
URL:         https://arxiv.org/html/2505.23281v2
Kind:        primary. Balunovic, Dekoninck, Petrov, Jovanovic, Vechev (ETH Zurich
             and INSAIT, Sofia University), "MathArena"; owns a quantified
             contamination finding on competition-sourced math benchmarks.
Establishes: Models sit 10-20% above the human-aligned trend line on AIME 2024,
             which the authors read as contamination-driven inflation; QwQ-Preview-
             32B is an extreme outlier, ~60% above expected. Their stated premise:
             widely-available, web-published competition problems get into training
             data, so real-time evaluation on freshly released competitions is the
             fix. Latest revision 2 Oct 2025 / 14 Jan 2026. This is competition-
             math contamination in general (AIME 2024), not the MATH test set
             specifically, but MATH's problems share the exact provenance.
Paraphrase:  When a math benchmark is built from public competition problems, a
             chunk of the reported score can be memorization; MathArena measures a
             10-20% inflation on one such benchmark and routes around it with fresh
             competitions.
Locators:    Contamination analysis section; introduction (premise on public
             competition data).
Quote:       "Most models lie above this line on AIME with a margin of 10%-20%,
             suggesting inflated performance on AIME 2024 due to data
             contamination." / "Many benchmarks are sourced from publicly
             available math competitions, which are accessible online and often
             used to train LLMs."
```

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary. OpenAI, "GPT-4 Technical Report"; read to check a common
             claim, and it establishes a negative fact.
Establishes: The GPT-4 Technical Report does NOT report a MATH score anywhere. Its
             academic-benchmark table (Table 2) lists MMLU, HellaSwag, ARC,
             WinoGrande, HumanEval, DROP, and GSM-8K, and the appendices/exam
             tables cover SAT/GRE/AP/bar but not the Hendrycks MATH dataset. The
             widely-cited "GPT-4 = 42.5% on MATH" is therefore not owned by this
             document; do not attribute it here.
Paraphrase:  Any "GPT-4 on MATH" figure must be sourced from wherever it actually
             appears, not this report, which omits MATH.
Locators:    Table 2 (academic benchmarks); exam appendix; full-text search for
             "MATH".
Quote:       (none; the relevant fact is an absence.)
```

```text
URL:         https://epoch.ai/benchmarks/about
Kind:        secondary. Epoch AI (independent research org, supported by the UK AI
             Security Institute) reporting on the benchmark landscape from outside
             the model labs; context for saturation, not owner of any model score.
Establishes: Epoch treats MATH Level 5 as reaching saturation and added Mock AIME
             2024-2025 as a harder replacement.
Paraphrase:  An independent evaluator now considers even the hardest MATH tier
             close to saturated and has moved its frontier tracking to harder math.
Locators:    Benchmark selection / rationale section.
Quote:       "added Mock AIME 2024-2025 since it is a harder benchmark of
             mathematics problems than MATH Level 5, which is now reaching
             saturation."
```

## Contradictions

- The angle risks overstating "the number misled." Not all of the climb from ~7%
  to ~97% is artifact. A three-time IMO gold medalist scored 90% on MATH (MATH
  paper), so the ceiling is genuinely reachable by strong human reasoning; and
  Minerva's move from exact-match to SymPy grading recovered only ~1% (Minerva,
  Table 6), so loose grading explains a small slice, not the trajectory. The
  writer must credit real capability gains alongside contamination and grading.

- Grading error points both ways, so "exact match undercounts skill" and "exact
  match overcounts skill" are both true and neither is the whole story. False
  negatives (correct answer, wrong format) understate scores; Minerva's false
  positives (correct answer, flawed reasoning: ~8% average, ~30% at Level 5)
  overstate them. Presenting only one direction would be a half-truth.

- Contamination of the MATH *test set specifically* is asserted more than
  quantified in owning documents. MathArena's 10-20% figure is for AIME 2024, not
  MATH. The strongest MATH-specific, owned contamination fact is Lightman's: 4,500
  of 5,000 MATH test problems went into OpenAI's PRM800K training data, which is
  why MATH-500 exists. The HF DMCA takedown corroborates that the problems are
  copyrighted, web-mirrored competition IP. State the MATH-specific case through
  those two facts, not by borrowing AIME's number.

- Label ambiguity is itself a contradiction in the record: Qwen2.5-Math reports
  "MATH" (4-shot) without pinning full-set vs MATH-500 on the page; DeepSeek-R1
  and o1 report "MATH-500"; the 2021 paper and Minerva report the full 5,000. A
  cross-model "MATH" comparison silently mixes 500-problem and 5,000-problem
  denominators and different metrics (few-shot vs Pass@1 vs maj1@k).

## Numbers

```text
Figure: 12,500 problems total
Owner:  MATH paper (Hendrycks et al. 2021), abstract
Scope:  full dataset, competition math
```
```text
Figure: 7,500 train / 5,000 test
Owner:  MATH paper (ar5iv full text) and HF dataset card
Scope:  the train/test split of the 12,500
```
```text
Figure: 7 subjects, 5 difficulty levels (1 easiest to 5 hardest)
Owner:  MATH paper (ar5iv); levels/subjects also on HF card
Scope:  every problem carries a subject and a level
```
```text
Figure: best paper model 6.9% (GPT-2 1.5B + AMPS); GPT-3 175B few-shot 5.2%
Owner:  MATH paper (ar5iv), results tables
Scope:  accuracy on the 5,000-problem test set at release (2021)
```
```text
Figure: human CS PhD student ~40%; three-time IMO gold medalist 90%
Owner:  MATH paper (ar5iv), human-baseline discussion
Scope:  informal human baselines on MATH test problems
```
```text
Figure: Minerva 540B 33.6% (single sample); 50.3% (maj1@64); 8B 14.1%; 62B 27.6%
Owner:  Minerva paper (Lewkowycz et al. 2022), Table 3
Scope:  full MATH test set; prior SOTA they cite is 6.9%
```
```text
Figure: exact-match false positives ~8% average, up to ~30% at Level 5; SymPy
        normalization gain ~1% (62B 26.5% -> 27.6%)
Owner:  Minerva paper, Section 4.2 / Table 5 (false positives), Table 6 (SymPy)
Scope:  manual analysis of Minerva outputs graded on MATH
```
```text
Figure: MATH-500 = 500 test problems (uniform random); 4,500 test problems placed
        in PRM800K training; best PRM solves 78.2% via best-of-1860
Owner:  Lightman et al. 2023 (OpenAI)
Scope:  the 500 test problems OpenAI did not train on
```
```text
Figure: Qwen2.5-Math-72B-Instruct 85.9 on "MATH" (4-shot CoT); 7B-Instruct 83.6;
        base 72B 66.8
Owner:  Qwen2.5-Math report (2024), results table
Scope:  labeled "MATH"; full-set vs MATH-500 not stated on page
```
```text
Figure: DeepSeek-R1 97.3% MATH-500 (Pass@1); o1-1217 96.4% (as reported);
        DeepSeek-V3 90.2%
Owner:  DeepSeek-R1 report (2025), Table 4
Scope:  the 500-problem subset, single-sample accuracy
```
```text
Figure: 10-20% inflation margin on AIME 2024; QwQ-Preview-32B ~60% above expected
Owner:  MathArena (2025), contamination analysis
Scope:  AIME 2024 (competition-sourced benchmark), not the MATH test set
```

## Source assets

```text
Asset: MATH paper, Figure 1 (worked example problems with \boxed final answers)
Shows: what one MATH item is -- a competition problem, a LaTeX step-by-step
       solution, and the single boxed final answer the grader reads.
Crop:  keep the problem statement and the \boxed{} answer legible; the point is
       that only the boxed string is graded, so that token must be visible.
```
```text
Asset: MATH paper, the scaling figure (accuracy vs model size / compute)
Shows: the paper's own finding that accuracy barely moves with scale in 2021 --
       the "before" state against which later saturation lands.
Crop:  retain the axis labels and the near-flat trend; do not crop out the low
       absolute accuracy, which is the whole point.
```
```text
Asset: Minerva paper, Table 5 (false-positive rate by difficulty level)
Shows: exact-match grading passes wrong reasoning more often on harder problems,
       ~30% at Level 5 -- the score is not a clean count of solved problems.
Crop:  keep the Level column and the rate column paired; do not drop Level 5.
```
```text
Asset: Lightman et al., Figure 5 (subject/level distribution of the 500 subset
       vs the full MATH test set)
Shows: MATH-500 is a representative random sample, not a harder or curated slice
       -- which is why its numbers are comparable in shape but on 500, not 5,000.
Crop:  keep both distributions side by side; the comparison is the evidence.
```
```text
Asset: DeepSeek-R1 report, Table 4 ("MATH-500 (Pass@1)" row)
Shows: frontier models at 96-97% and, plainly, that the reported benchmark is the
       500-problem subset under the MATH name.
Crop:  keep the "MATH-500 (Pass@1)" header attached to the numbers; the header is
       the point, not the numbers alone.
```

## Discarded

```text
URL: https://openai.com/index/learning-to-reason-with-llms/ -- OpenAI's o1
     announcement (owner of o1's oft-cited 94.8% full-MATH figure) returned HTTP
     403 to every fetch attempt; could not read it firsthand, so the o1 full-MATH
     number is not cited. o1's MATH-500 96.4% is instead recorded as reported in
     the DeepSeek-R1 table, with ownership flagged.
```
```text
URL: https://cdn.openai.com/o1-system-card.pdf -- fetched (1.8MB) but the PDF
     could not be parsed to text in this environment (no page renderer), so no
     figure is taken from it.
```
```text
URL: https://huggingface.co/datasets/hendrycks/competition_math (as a live
     download) -- disabled by DMCA; used only as the owner of the takedown fact
     and the field schema, not as a working data source.
```
```text
URL: leaderboard aggregators (e.g. HELM, Papers-with-Code MATH leaderboard) --
     not cited for any model's score. Per the brief, a MATH score is owned by the
     model's card or paper, not an aggregator; each number here is taken from its
     owning document.
```
```text
URL: various secondary explainers surfaced in search (VentureBeat FrontierMath
     piece, survey PDFs on contamination) -- read for orientation, not cited;
     their underlying claims are taken from the primaries that own them.
```
