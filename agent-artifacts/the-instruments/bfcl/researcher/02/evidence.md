# Evidence: the-instruments/bfcl (02)

This is a single-owner repair of researcher/01. All primary sourcing and every
figure in 01 stand unchanged and are preserved in full below. The only change is
the article's lone secondary. The editor's blocking item (editor/01, "Required
work") is that s5 — Emergent Mind's BFCL V4 topic page — is cited for the
"outside overview of the board lands on the same shape: top models ace the
one-shot questions and stumble on multi-turn" framing, and neither the editor's
two reads nor a third firsthand read for this repair can find that framing on
that page; the page instead lists the five single-turn category types and frames
multi-turn as *improving*. The underlying claim is not in danger — the ICML
primary (s1) owns it fully, cited in the same paragraph. The task was to restore
a legitimate secondary that genuinely carries the single-turn-strong /
multi-turn-weak framing, because s5 is the article's only secondary and cannot be
cut without breaching the >=1-secondary floor.

The repair: a different secondary that is, by its own title and purpose, an
outside overview of the board and that states the framing plainly — an
independent third-party analysis, "From Tool Use to Holistic Agent Evaluation: An
In-Depth Analysis of the Berkeley Function Calling Leaderboard (BFCL)." It names
a distinct "agentic chasm" between single-turn calls and stateful/memory tasks,
and says models that excel at one-shot questions struggle in extended
conversations. This is recorded below as the new secondary (s5'). Its one
limitation is provenance: the document carries no named author, so it is treated
strictly as a secondary/repetition — it supports that the outside characterization
was made and matches the article's shape, not the truth of the claim, which the
primary (s1) owns. The >=1-secondary composition floor is satisfiable: swapping
the article's single secondary citation from Emergent Mind to s5' keeps exactly
one legitimate secondary. A fully-verified fallback that also keeps the floor is
recorded after the sources (option b), in case the editor judges s5''s provenance
too thin. The dense per-subcategory cells of ICML Table 1 remain the one place to
reconfirm any single sub-cell against the typeset table before quoting it
precisely; the overall-accuracy column and the paper's prose findings are
unambiguous.

## Sources

```text
URL:         https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html
Kind:        primary — the Gorilla/UC Berkeley team's own blog post defining BFCL v1's dataset and scoring; it owns these claims.
Establishes: BFCL v1 = 2,000 question-function-answer pairs. AST evaluation checks (1) exact function-name match against the documentation, (2) presence of required parameters, (3) parameter type (strict, with a Python int->float exception), (4) parameter values (exact for most types; case-insensitive/whitespace-normalized for strings), (5) no hallucinated parameters outside the docs — and runs NOTHING. Executable evaluation runs the call and compares by exact match, real-time match (within a 20% threshold for numeric results), or structural match (type/shape only). Relevance/irrelevance: the model is given functions unrelated to the query and must output "no function call"; scored on correctly abstaining. Cost-per-1,000-calls and latency formulas are defined here. v1 leader at release: GPT-4, with OpenFunctions-v2, Mistral-medium, and Claude-2.1 close behind.
Paraphrase:  v1 grades one proposed call against a known-correct answer, mostly by parsing (AST) and sometimes by executing; a separate category tests whether the model declines when no function is relevant.
Locators:    Dataset composition table; "AST Evaluation" and "Executable Evaluation" sections; "Function Relevance Detection"; cost/latency section. Post authored by Fanjia Yan, Huanzhi Mao, Charlie Cheng-Jie Ji, Ion Stoica, Joseph E. Gonzalez, Tianjun Zhang, Shishir G. Patil. Blog index dates it 2024-02-26; the page footer reads "Last updated: 2024-08-19".
Quote:       "Execution involves running the specified function and examining its output."
```

```text
URL:         https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html
Kind:        primary — the team's own post defining the v2 "Live" dataset and why it exists.
Establishes: BFCL v2 Live = 2,251 question-function-answer pairs from user-contributed, real-world data, built to counter three named problems with v1: data contamination (models may have trained on the public v1 set), bias/fairness (v1 rested on researcher assumptions), and generalization to real scenarios. Category breakdown: Simple 258, Multiple 1,053, Parallel 16, Parallel Multiple 24, Irrelevance Detection 882, Relevance Detection 18. The live distribution is heavily weighted toward "multiple" (choosing which of several tools to use) and away from parallel calls, versus v1's researcher-set 400/200/200/200. Contamination is diagnosed by a scatterplot: models whose live score sits well below the y=x line versus their v1 score may have been contaminated on v1.
Paraphrase:  v2 replaced researcher-invented cases with real user queries specifically to expose v1 contamination and bias; the shape of real demand differs sharply from v1's assumed shape.
Locators:    Opening rationale paragraph; category-count table; contamination scatterplot discussion. Authors: Huanzhi Mao, Charlie Cheng-Jie Ji, Fanjia Yan, Tianjun Zhang, Shishir G. Patil. Blog index dates it 2024-08-14; page footer "Last updated: 2024-08-19".
Quote:       "To tackle the issues of data contamination, bias and fairness, and need to generalize functions (tools) to real-world scenarios, we are excited to release BFCL V2 * Live."
```

```text
URL:         https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html
Kind:        primary — the team's own post defining the v3 multi-turn dataset and its scoring.
Establishes: BFCL v3 adds 1,000 multi-turn entries across categories: Base Multi-Turn 200, Missing Parameters 200, Missing Functions 200, Long-Context Multi-Turn 200, Composite 200. Scored two ways at once: state-based evaluation (compare the backend system's state after execution to the ground-truth state) and response-based/subset-matched evaluation (the model must call the necessary functions, allowing valid alternative trajectories). Release date 2024-09-19; last updated 2024-12-10. The post explicitly flags its own leaderboard snapshot as outdated and points forward to the BFCL V4 blog. It does NOT itself publish a numeric single-turn-vs-multi-turn gap.
Paraphrase:  v3 is the first version to score a whole conversation rather than one call, by checking both the end state of the system and the sequence of calls; it is young and points to V4 for current numbers.
Locators:    "Multi-turn" category definitions; "state-based"/"response-based" scoring section; the outdated-composition note. Authors: Huanzhi Mao, Fanjia Yan, Charlie Cheng-Jie Ji, Jason Huang, Vishnu Suresh, Yixin Huang, Xiaowen Yu, Joseph E. Gonzalez, Shishir G. Patil.
Quote:       "Note: This leaderboard composition is now outdated. For the most updated composition, please refer to the [BFCL V4 blog]."
```

```text
URL:         https://proceedings.mlr.press/v267/patil25a.html   (PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)
Kind:        primary — the team's peer-reviewed paper (ICML 2025 / PMLR v267), the authoritative single owner of BFCL's full design, scoring, and a fixed results snapshot.
Establishes: BFCL is described as "a diverse dataset of 5,551 question-function-answer pairs" in four parts: single-turn; crowd-sourced (2,251 curated from >67,000 community datapoints, collected 2024-02-26 to 2024-04-01, deduplicated via ROUGE-L and embeddings, public sets excluded to avoid contamination); multi-turn (eight curated API suites, 1,000 queries); and agentic (web search, memory, SQL). Scoring by category: Single-Turn uses BOTH AST-substring matching and execution-response matching; Crowd-Sourced uses AST only; Multi-Turn combines state-based and response-based checks (an entry is correct only if it passes BOTH checks on ALL turns); Agentic uses strict exact-match on a dedicated answer field. AST rule stated precisely: "A function call is correct if the function name matches exactly and if all parameter values fall within their respective possible answers" — parameters are checked against a set of valid values, not by exact match. Execution matching has three modes: exact match, real-time simultaneous execution for time-sensitive outputs, and structure matching (list length + dict-key presence) for nested outputs. The paper validates AST against execution: Figure 3 shows AST scores are "strongly correlated" with execution-based scores on the single-turn set. Table 1 (headline result): gpt-4o-2024-11-20 (Prompt) tops the board at 66.4% Overall Accuracy; (FC) 65.8; GPT-4-turbo-2024-04-09 (FC) 60.9; o1-2024-12-17 (Prompt) 59.1. The paper's own verdict: single-turn/crowd-sourced/hallucination metrics are strong while "there remains significant room for improvement in multi-turn and agentic tasks, particularly in memory management." Agentic Memory cells for the top models are near zero.
Paraphrase:  The paper is the definitive statement that BFCL's original core is single-call grading validated against execution, and that even after adding multi-turn and agentic categories, the best models score in the mid-60s overall and collapse on memory and long-horizon agentic tasks.
Locators:    Abstract; Section 1 (four-part structure, 5,551 pairs); Section 3.1-3.4 (dataset); Section 4.1-4.5 (AST, execution, state/response, exact-match); Section 4.3 + Figure 3 (AST-execution correlation); Section 5.1 + Table 1 (results). Authors: Shishir G. Patil, Huanzhi Mao, Fanjia Yan, Charlie Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, Joseph E. Gonzalez. Venue: Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, 2025.
Quote:       "while state-of-the-art LLMs excel at single-turn calls, memory, dynamic decision-making, and long-horizon reasoning remain open challenges."
```

```text
URL:         https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/CHANGELOG.md   (raw, read firsthand: https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md)
Kind:        primary — the repository's own changelog; it owns the record of what data was corrected and when. (Blob page 403s to automated fetch — gated, not dead; the raw file returns 200 and was read in full.)
Establishes: BFCL has repeatedly corrected its own live test data after release. Documented entries include: 2024-04-19 [#377] executable-category overhaul replacing an "evaluation_result" field with verified ground truth; 2024-08-23 [#600] fixes to 12 simple, 3 multiple, 3 parallel, 6 parallel_multiple; 2024-08-27 [#608] fixes to 16 simple, 5 multiple; 2024-10-16 [#661] "Bug fix in the dataset and possible answers" affecting 1 irrelevance, 2 parallel_multiple, 104 live_simple, 547 live_multiple, 11 live_parallel, 17 live_parallel_multiple; 2024-11-22 [#777/#778] fixing 55 entries whose function docs used illegal Python parameter names (such as "class"); 2024-12-26 [#826/#829] enum type-mismatch fixes to 7 live_simple, 176 live_multiple, 3 live_parallel_multiple, 70 live_irrelevance. Multi-turn categories had their metric overhauled on 2024-10-30 [#725/#733] (a response-based checker added alongside the state-based checker; irrelevance detection removed for multi-turn) plus several dataset/ground-truth fixes the same day.
Paraphrase:  The owners themselves rewrote large slices of the live set after publishing scores against it — most strikingly, the October 2024 fix touched 547 of the ~1,053 live_multiple cases, i.e. more than half that category.
Locators:    Dated entries by PR number as above; concentrate on the 2024 block spanning v1 through v3.
Quote:       "Bug fix in the dataset and possible answers ... 547 live_multiple ..." (2024-10-16, [#661]).
```

```text
URL:         https://arxiv.org/abs/2406.12045   (PDF read firsthand: https://arxiv.org/pdf/2406.12045)
Kind:        primary — the τ-bench paper; it owns the pass^k reliability figures used for the contrast.
Establishes: τ-bench ("A Benchmark for Tool-Agent-User Interaction in Real-World Domains," Yao, Shinn, Razavi, Narasimhan; submitted 2024-06-17) measures agents that use native function calling in two domains, retail and airline. pass^1 (single-attempt task success) for the best model, gpt-4o via function calling: 61.2% retail, 35.2% airline, 48.2 average (Table 2). pass^k is defined as the probability that all k of k i.i.d. trials of the same task succeed. The paper's headline reliability finding: for the same gpt-4o function-calling agent with >60% average success, pass^8 drops to below 25% on retail. Cost: pairing the gpt-4o FC agent with a gpt-4 user simulator on retail costs $0.38 (agent) / $0.23 (user) per task, ~$200 for one trial across the set; 95.9% of agent cost is the input prompt. The agents here use the same capability BFCL scores — native function calling — which is why the contrast is direct: strong single-call ability does not carry to multi-step reliability.
Paraphrase:  The single best function-calling model gets a task right about 61% of the time once, but right eight-for-eight less than a quarter of the time; reliability, not single-call accuracy, is what collapses.
Locators:    Abstract; Section 4 (pass^k definition, eq. after Table 1); Table 2 (per-model pass^1); Section 5.1 "Agent consistency via pass^k" and "Cost analysis"; Figure 4 (pass^k vs k). pass^k formula: pass^k = E_task[ C(c,k) / C(n,k) ], c = successful trials, n = total trials.
Quote:       "Even for the best-performing gpt-4o function calling agent which has a >60% average task success, pass^8 drops to <25%."
```

```text
URL:         https://gorilla.cs.berkeley.edu/leaderboard.html
Kind:        primary — the live leaderboard, the artifact the article examines. Resolves (200); the ranked table is rendered client-side and was not extractable as text.
Establishes: The current live board is BFCL V4, page "last updated 2026-04-12," evaluated at a pinned commit. "Overall Accuracy is the unweighted average of all the sub-categories." Confirms the leaderboard has moved past v3 into agentic (V4) territory.
Paraphrase:  The public number a lab cites today is a V4 overall accuracy: an unweighted mean across single-turn, live, multi-turn, and agentic sub-scores.
Locators:    Header/version line and the Overall Accuracy definition note. For a stable, citable numeric snapshot use ICML Table 1 (above); the live board changes.
```

```text
URL:         https://gorilla.cs.berkeley.edu/blog.html
Kind:        primary — the Gorilla blog index; owns the canonical post URLs and publication dates.
Establishes: Canonical dates/URLs: v1 = 2024-02-26 (/blogs/8_...); v2 Live = 2024-08-14 (/blogs/12_...); v3 Multi-turn = 2024-09-19 (/blogs/13_...); V4 Agentic series = 2025-07-17 (/blogs/15_,16_,17_...). Used to reconcile the "last updated" footers on the version posts against true publication dates.
Locators:    Blog list entries.
```

```text
URL:         https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/README.md
Kind:        primary — the eval harness README (repository-owned). Read firsthand; blob page 403s to automated fetch (gated).
Establishes: The current repository references BFCL V4 ("BFCL V4 Part 3: Agentic Format Sensitivity"), distinguishes Non-Live (single-turn), Live (single-turn), and Multi-Turn categories, and points to TEST_CATEGORIES.md and CHANGELOG.md for the enumerated categories and correction history. It does not itself restate scoring mechanics or counts.
Locators:    Category reference line; pointers to TEST_CATEGORIES.md / CHANGELOG.md.
```

### Secondary source (repaired — new s5', replaces Emergent Mind as the article's secondary)

```text
URL:         https://huggingface.co/datasets/tuandunghcmut/BFCL_v4_information/blob/main/From%20Tool%20Use%20to%20Holistic%20Agent%20Evaluation_%20An%20In-Depth%20Analysis%20of%20the%20Berkeley%20Function%20Calling%20Leaderboard%20(BFCL).md
             (Rendered document page resolves 200; raw text also at the same path with /raw/ substituted for /blob/. The blob URL above is the document's own page and is what the article should cite.)
Kind:        secondary — an independent third-party analytical report on BFCL, titled "From Tool Use to Holistic Agent Evaluation: An In-Depth Analysis of the Berkeley Function Calling Leaderboard (BFCL)." It reports on the leaderboard from outside the Gorilla/UC Berkeley authoring team (it summarizes and interprets the team's papers and blogs; it does not own BFCL). By the authorship-and-stake test it is secondary: it repeats and characterizes findings the Gorilla team owns. Provenance limitation: the document carries no named author or institution (see note below), so it is used strictly as a secondary/repetition — it corroborates that an outside overview lands on the same shape, not the truth of the claim, which s1 owns.
Establishes: An outside overview of the board that lands on exactly the article's shape — top models are strong on single-turn/one-shot function calls and stumble on multi-turn, stateful, memory-bearing tasks. It names this a distinct "agentic chasm." It also enumerates the same single-turn category structure and reports the near-floor agentic-memory scores that the primary owns. This is the framing s5 (Emergent Mind) was cited for but could not support; s5' supports it directly and in the source's own words.
Paraphrase:  A third-party analysis reviewing BFCL's evolution concludes there is a large, distinct gap ("agentic chasm") between models' ability to execute a single-turn call and their ability to handle stateful, memory-heavy, multi-turn tasks; early results already showed models that ace one-shot questions faltering across a longer conversation.
Locators:    "Report Summary" section (the "agentic chasm" sentence); Section 2.1 "Beyond Single-Turn: Evaluating Sequential and Conversational Reasoning" (the one-shot-vs-extended-conversation sentence); Section 3.2 "Core Agentic Capabilities Under Scrutiny," Memory Management subsection (the ~12% agentic-memory figure, attributed by the report to "the literature," i.e. the primary — do not cite s5' for that number; s1/Table 1 owns it).
Quote:       "An analysis of the leaderboard results reveals a distinct 'agentic chasm'—a significant performance gap between the ability to execute simple, single-turn function calls and the ability to perform tasks requiring complex, stateful reasoning and memory." And, from Section 2.1: "Early results showed that models excelling at one-shot questions struggled in extended conversations."
```

```text
URL:         https://www.emergentmind.com/topics/berkeley-function-calling-leaderboard-v4-bfclv4
Kind:        secondary — a topic aggregator summarizing BFCL V4; reports on the leaderboard from outside the authoring team. (This was s5 in researcher/01.)
Establishes: Corroborates the five single-turn category types (Simple, Multiple, Parallel, Parallel Multiple, Relevance Detection). It does NOT support the single-turn-strong / multi-turn-weak "stumble" framing the article attached to it: a third firsthand read for this repair confirms the editor's two reads — the page lists the single-turn categories and describes multi-turn work as an emerging advancement that is "now improved significantly," i.e. improving, not as a weakness where top models stumble. Its per-model percentage table is unsourced/mixed-vintage and is NOT relied on for any figure.
Paraphrase:  Verified support: the five single-turn category types. Verified non-support: the single-vs-multi "stumble" framing. Because the article cites its lone secondary only once — for the framing sentence — Emergent Mind is no longer the right citation for that sentence and is superseded by s5'. It remains available only if the writer instead takes fallback option (b) below (attach it to the five-category structure).
Locators:    Category-structure section (supports the five types); multi-turn passages describe multi-turn as improving ("now improved significantly over early SFT and standard RL baselines"), not as a stumble.
```

## Note on the repair and a verified fallback

- Primary fix (option a, recommended): the writer swaps the single secondary
  citation on "An outside overview of the board lands on the same shape: the top
  models ace the one-shot questions and stumble once they must remember context,
  manage a long conversation, or decide not to act" from Emergent Mind to s5'
  (the HuggingFace In-Depth Analysis). s5' states this framing in its own words
  ("agentic chasm"; "models excelling at one-shot questions struggled in extended
  conversations"), so the sentence's claim is unchanged and now rests on a
  secondary that genuinely supports it. The primary (s1) continues to own the
  claim's truth in the same paragraph. The article still has exactly one
  secondary; the >=1-secondary floor holds.

- s5''s one weakness is provenance: the analysis document names no author. It is
  therefore used only as an outside overview that echoes the shape (a
  repetition), never as the owner of any figure or of the claim's truth. Nothing
  in the article rests on its reliability.

- Verified fallback (option b), if the editor judges s5''s provenance too thin to
  be the article's sole secondary: re-cite the "outside overview" sentence to the
  primary (s1, which owns the framing outright) and instead attach the article's
  secondary to a claim Emergent Mind genuinely and durably supports — the five
  single-turn category types (Simple, Multiple, Parallel, Parallel Multiple,
  Relevance Detection), verified firsthand on the Emergent Mind V4 page. That
  keeps one legitimate, reputably-hosted secondary in the piece and satisfies the
  floor without depending on s5''s authorship. Under either option the article
  retains exactly one secondary and clears the composition floor.

## Contradictions

Nothing here undermines the commissioned angle; the strongest counter-points actually
sharpen it. Two things a fair lesson must state:

1. AST matching is validated, for what it measures. The ICML paper (Section 4.3,
   Figure 3) shows AST scores are strongly correlated with execution-based scores on
   the single-turn set. So the criticism is not that AST grading is inaccurate — it is
   a faithful proxy for whether the single call is right. The point is narrower and
   exactly the commission's: a faithful single-call grade is still only a single-call
   grade.

2. BFCL is not ignoring the gap — it is chasing it. The whole v3 (multi-turn) and V4
   (agentic: web search, memory, SQL) expansion exists to measure sustained,
   stateful, multi-step behavior. If anything closes the gap the commission warns
   about, it is these categories. But the owners' own results show the gap is still
   wide open: mid-60s overall for the best model, with multi-turn and especially
   agentic memory scoring far lower. The multi-turn category is young (first released
   2024-09-19) and small (1,000 entries) next to the single-turn + live core
   (~4,250 entries), and its scoring metric was itself overhauled six weeks after
   release. So "the multi-turn category closes the gap" is not yet supported by the
   record; the record shows it revealing the gap, not closing it.

Repair-specific contradiction to record: the article's original secondary
(Emergent Mind) leans the other way on multi-turn — it describes multi-turn
capability as *improving* ("now improved significantly"), not as a place where top
models stumble. That is precisely why it could not carry the framing sentence.
The replacement secondary (s5') and the primary (s1) both carry the stumble
framing; the honest reading is that multi-turn is simultaneously improving and
still far below single-turn, and the article's claim is about the size of the
remaining gap, not about the absence of progress.

No source claims a high BFCL score reliably predicts real multi-step agent success.
The τ-bench evidence is the direct rebuttal to any such claim.

## Numbers

```text
Figure: BFCL v1 = 2,000 question-function-answer pairs
Owner:  BFCL v1 blog (gorilla, 2024-02-26)
Scope:  Full v1 set. Breakdown: AST Simple 400, AST Multiple 200, AST Parallel 200, AST Parallel-Multiple 200, Java 100, JavaScript 50; Executable Simple 100, REST 70, Exec Multiple 50, Exec Parallel 50, Exec Parallel-Multiple 40; Relevance Detection 240; SQL 100 (excluded from leaderboard). By language: 1,680 Python, 100 Java, 50 JavaScript, 70 REST, 100 SQL.
```

```text
Figure: BFCL v2 Live = 2,251 question-function-answer pairs
Owner:  BFCL v2 Live blog (gorilla, 2024-08-14)
Scope:  Full live set. Breakdown: Simple 258, Multiple 1,053, Parallel 16, Parallel Multiple 24, Irrelevance Detection 882, Relevance Detection 18.
```

```text
Figure: BFCL v3 Multi-turn = 1,000 entries
Owner:  BFCL v3 blog (gorilla, 2024-09-19)
Scope:  Base 200, Missing Parameters 200, Missing Functions 200, Long-Context 200, Composite 200.
```

```text
Figure: 5,551 total question-function-answer pairs; crowd-sourced 2,251 drawn from >67,000 (64,517 collected)
Owner:  BFCL ICML 2025 paper (Patil et al.), Section 1 and 3.2
Scope:  Aggregate across single-turn + crowd-sourced + multi-turn + agentic as counted in the paper. Crowd-sourced collected 2024-02-26 to 2024-04-01. (Note: this aggregate does not arithmetically equal 2,000 + 2,251 + 1,000; each is the team's own count at a different snapshot. Treat per-version blog counts as authoritative for each version and the 5,551 as the paper's aggregate.)
```

```text
Figure: 66.4% Overall Accuracy — top model on the paper's board
Owner:  BFCL ICML 2025 paper, Table 1
Scope:  gpt-4o-2024-11-20 (Prompt), overall unweighted mean across all sub-categories. Next: gpt-4o-2024-11-20 (FC) 65.8; GPT-4-turbo-2024-04-09 (FC) 60.9; GPT-4o-mini (FC) 60.6; o1-2024-12-17 (Prompt) 59.1. Single-turn AST/execute sub-scores for these models sit in the high-80s to 100; the Agentic "Memory" sub-scores sit near 0-12 and drag the overall down. (Exact per-subcategory cells extracted from the PDF; reconfirm any single sub-cell against the typeset Table 1 or the live board before quoting it. Overall-accuracy column is unambiguous.)
```

```text
Figure: pass^1 = 61.2% (retail), 35.2% (airline), 48.2 avg; pass^8 < 25% (retail)
Owner:  τ-bench paper (Yao et al., 2024), Table 2 and Section 5.1
Scope:  gpt-4o via native function calling; >=3 trials per task, agent temp 0.0 / user temp 1.0, <=30 actions per task. pass^8 = probability of succeeding on all 8 of 8 i.i.d. trials of the same task.
```

```text
Figure: ~$0.38 agent + $0.23 user simulation per task; ~$200 per full single-trial run
Owner:  τ-bench paper, Section 5.1 "Cost analysis"
Scope:  gpt-4o FC agent paired with gpt-4 user simulator on τ-retail; 95.9% of agent cost is the input prompt (long domain policy + function definitions).
```

```text
Figure: 547 live_multiple entries corrected in one fix
Owner:  gorilla CHANGELOG.md, 2024-10-16 [#661]
Scope:  Of ~1,053 live_multiple cases in the v2 Live set; same fix also touched 104 live_simple and others. Illustrates the scale of post-release data correction. The changelog does NOT publish the resulting leaderboard score deltas.
```

## Source assets

```text
Asset: BFCL v1 blog — the dataset-composition table (category -> count) and the paired AST-vs-Executable evaluation diagram.
Shows: At a glance, that the bulk of BFCL is AST-graded single calls and only a small slice is executed; exactly which categories run code and which are parsed.
Crop:  Keep the category labels and counts legible; a crop may drop the cost/latency rows, which are a separate point.
```

```text
Asset: BFCL v2 Live blog — the contamination scatterplot (v1 score vs live score per model, with the y=x reference line).
Shows: How the team detects contamination: models far below the diagonal likely trained on the public v1 set. A concrete picture of why a leaderboard revises its own data.
Crop:  Must retain the y=x line and both axis labels; without the diagonal the point is lost.
```

```text
Asset: BFCL ICML 2025 paper — Figure 3 (AST-summary vs Exec-summary correlation).
Shows: That AST grading tracks execution grading on single-turn tasks — the validity claim for AST, and the honest counterweight in the lesson.
Crop:  Keep both axes and the correlation trend; do not crop to imply a tighter fit than shown.
```

```text
Asset: BFCL ICML 2025 paper — Table 1, specifically the contrast between the high single-turn columns and the near-zero Agentic "Memory" column for the same model row.
Shows: In one row, a model that is near-perfect on single calls and near-zero on stateful memory — the lesson's entire thesis in one line.
Crop:  A crop must keep the model name, the Overall Accuracy cell, a representative high single-turn cell, and the Memory cell together; dropping either end destroys the contrast. Reconfirm cell values against the typeset table first.
```

```text
Asset: τ-bench paper — Figure 4 (pass^k curve falling as k rises, for gpt-4o and peers on τ-retail).
Shows: The reliability collapse visually: the curve starts near 61% at k=1 and falls under 25% by k=8. This is the strongest single image for the "single call is not agent reliability" point.
Crop:  Keep the k-axis (1..8+) and the y-axis percentage; label which line is gpt-4o.
```

## Discarded

```text
URL: https://arxiv.org/html/2406.12045v2  — 404; the HTML render lives at the unversioned /html/2406.12045. No content lost (figures verified from the PDF).
URL: emergentmind V4 per-model percentage table — retained the page for category corroboration only; its numbers are unsourced and mixed-vintage, so no figure is drawn from it, and (per the repair) it does not support the single-vs-multi framing. ICML Table 1 is used for numbers; s5' carries the framing.
URL: TEST_CATEGORIES.md (raw, resolves 200) — read but discarded for counts: it lists category names and descriptions without per-category test-case counts. Counts taken from the version blogs and the ICML paper, which own them.
URL: https://www.emergentmind.com/topics/berkeley-function-calling-benchmark-bfcl — a second Emergent Mind topic page read for this repair; lists the single-turn categories and multi-turn accuracy definition but does not carry the single-turn-strong / multi-turn-weak framing (its only failure statement is about sub-1B models, not top models). Not used.
URL: https://llm-stats.com/benchmarks/bfcl-v3-multiturn — third-party BFCL v3 multi-turn leaderboard; a legitimate secondary but describes only multi-turn methodology and shows table numbers, with no prose contrasting strong single-turn against weak multi-turn. Does not support the framing sentence. Not used.
URL: https://arxiv.org/abs/2510.22898 (CoreThink/MAVEN, independent authors) and https://arxiv.org/abs/2511.22138 (TinyLLM) — read for a background sentence characterizing BFCL's single-vs-multi gap; neither states the framing in a clean quotable form (CoreThink's related work describes benchmarks without the comparative performance claim). Not used.
```
</content>
</invoke>
