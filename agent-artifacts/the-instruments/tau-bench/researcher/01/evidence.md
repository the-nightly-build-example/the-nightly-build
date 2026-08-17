# Evidence: the-instruments/tau-bench (01)

The evidence fully supports the commissioned angle. The τ-bench paper (arXiv:2406.12045,
read in full, 50 pages including all appendices) gives every figure the commission
needs first-hand: the exact mechanics of a task (mock database, API tools, an
LM-simulated user, a domain policy), the exact reward rule (final-database-state
match AND a check that the agent's messages to the user carried the required
output information), the headline pass@1 numbers by model and domain, and the
pass^k collapse the angle turns on (gpt-4o: pass^1 61.2% retail / 35.2% airline,
falling to pass^8 <25% in retail — both stated in the paper's own abstract and
Results section). A concrete, fully-quoted task trajectory is available straight
from the paper (Figure 1's JK9O19 example, and the complete Appendix D.2 booking
transcript), so the writer does not need to invent one. The paper's own "Directions
for improvement" section supplies the benchmark's stated limitations verbatim.
A follow-up paper (τ²-bench, arXiv:2506.07982, Sierra, June 2025) independently
re-audited the retail and airline user simulator and found a 40% (retail) and 47%
(airline) conversation-level error rate, 12%/13% of it task-critical — a second,
independent primary source confirming and quantifying the "simulated-user fidelity"
limitation the original paper only stated qualitatively. A 2025 model report
(Anthropic's Claude 3.7 Sonnet announcement, Feb 24 2025) states τ-bench pass@1-style
figures in public use (81.2% retail / 58.4% airline), verified directly from the
underlying chart image, which is exactly the kind of single-number public quotation
the angle describes — though it is worth noting plainly that this specific chart is
not a case of anyone mislabeling a reliability rate as a one-try score; it is a
legitimate pass^1 figure presented with no pass^k figure next to it, run with
different scaffolding (a custom "planning tool" prompt and a step limit raised from
30 to 100) than the paper's own baseline agent. That is a real, sourced illustration
of how a bare percentage travels in public without its reliability context, and it
is honest to describe it that way rather than as an outright misquotation.

The evidence is thinnest in two places. First, I could not open OpenAI's own o1
announcement page (blocked, both live and via the Wayback Machine) to verify the
o1 TAU-bench figures (73.5% retail / 54.2% airline) that appear in Anthropic's
comparison chart; those two numbers are recorded as Anthropic's report of OpenAI's
claim, not independently confirmed against OpenAI's own primary source, and should
not be cited as if verified against OpenAI directly. Second, the original paper's
Figure 4 (the actual pass^k-vs-k curve, k = 1,2,4,8,16,32) is a plotted line chart
with no axis data table; the paper gives exact numbers in text only for k=1 (Table
2) and the single claim "pass^8 <25% in retail," so a chart built "only from figures
the paper reports" can honestly plot those two labeled points and the qualitative
downward shape, but cannot honestly reconstruct the k=2/4/16/32 values without
fabricating data the paper does not print.

## Sources

```text
URL:         https://arxiv.org/abs/2406.12045
Kind:        primary — the τ-bench paper itself; owns every figure and definition attributed to "the paper" below
Establishes: Full mechanics, all main-result figures, the pass^k metric definition, the concrete example task, the paper's own stated limitations
Paraphrase:  Yao, Shinn, Razavi, and Narasimhan (Sierra), "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," preprint, posted 17 Jun 2024. Read in full (all 50 pages via the PDF, including appendices B, C, D).
Locators:    Title page (authors/affiliation); Abstract; §3 (pp.3-5, POMDP formalism, reward, pass^k definition); Table 1 (p.5, domain stats); §5.1/Table 2 (p.7, main pass^1 results); Figure 3 (p.7, method comparison); Figure 4 (p.7, pass^k vs k curves); Table 3 (p.8, policy-ablation); Figure 5 (p.7, failure breakdown); §6 "Directions for improvement" (p.9, stated limitations); Appendix C.2.1 (pp.25-30, Task 0 retail failure trajectory); Appendix D.2 (pp.46-50, Task 0 airline success trajectory)
Quote:       "Existing benchmarks do not test language agents on their interaction with human users or ability to follow domain-specific rules... Our experiments show that even state-of-the-art function calling agents (like gpt-4o) succeed on <50% of the tasks, and are quite inconsistent (pass^8 <25% in retail)." (Abstract, p.1)

URL:         https://arxiv.org/abs/2506.07982
Kind:        primary — the official Sierra follow-up (τ²-bench); owns the dual-control extension, the telecom domain, and its own audit of the original τ-bench user simulator
Establishes: τ²-bench's dual-control extension and its measured error rate of the original τ-bench retail/airline user simulator (independent confirmation of a stated limitation, with numbers the original paper did not give)
Paraphrase:  Barres, Dong, Ray, Si, and Narasimhan (Sierra, and Dong/Si also University of Toronto & Vector Institute), "τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment," posted 9 Jun 2025.
Locators:    Title page (authors/affiliations); Abstract; §1 Introduction (p.2, "state-of-the-art LLMs struggle significantly... pass^1 of 34% for gpt-4.1... on new tasks"); Table 1 (p.5, domain stats incl. original retail/airline task counts of 115/50, matching the original paper); §4.3 "How does dual-control impact benchmark reliability?" and Table 2 (p.9-10, user-simulator error audit)
Quote:       "While for the retail and airline domains we recorded a 40% and 47% error rate for the user simulator (with 12% and 13% being critical errors that prevent task completion)... this rate is much lower for the new telecom domain." (p.10)

URL:         https://github.com/sierra-research/tau-bench
Kind:        primary — Sierra's own code-and-data repository for the original benchmark; owns the frozen leaderboard and the deprecation notice
Establishes: Exact pass^1 through pass^4 leaderboard figures for models released after the original paper (e.g. Claude 3.5 Sonnet), and the repository's own statement that the original retail/airline tasks are frozen and superseded
Paraphrase:  README states in bold: "The tasks in this repo are not updated... Please use τ³-bench for the latest fixed tasks and new domains," and gives full leaderboard tables for both domains.
Locators:    README.md, "Leaderboard" section (Airline and Retail tables, each with Pass^1 through Pass^4 columns)
Quote:       "⚠️ WARNING: The tasks in this repo are not updated. This repository contains outdated versions of the airline and retail tasks." (README, top)
```

```text
Note on access: a plain HTTP fetch (curl) to github.com returns 403 from this
environment's proxy, but the page's content was retrieved successfully through the
sanctioned browser-capable fetch tool (twice, for both the tau-bench and tau2-bench
repos) and again via raw.githubusercontent.com (HTTP 200), confirming the page is
live and its content as quoted above. The URL recorded is the repository's own page,
not the raw-content route used to double-check it.
```

```text
URL:         https://github.com/sierra-research/tau2-bench
Kind:        primary — Sierra's repository for τ²-bench / τ³-bench; owns the successor-benchmark status
Establishes: That τ²-bench itself was subsequently extended into "τ³-bench" (banking domain, voice modality, and fixes to the airline/retail tasks), confirming the original benchmark's tasks are treated by their own authors as needing correction
Paraphrase:  The repository, linked from the original tau-bench README, hosts the current, actively maintained successor benchmark.
Locators:    README.md, "News" banner
Quote:       "The τ²-bench repository has been updated to τ³-bench, which includes a new banking domain, a voice evaluation modality, as well as fixes to the airline and retail domain tasks." (as quoted verbatim in the original tau-bench README, which links here)

URL:         https://www.anthropic.com/news/claude-3-7-sonnet
Kind:        primary — Anthropic's own release announcement; owns the score it reports for its own model
Establishes: A 2025-vintage model report stating τ-bench pass@1-style figures in public use, and the scaffolding caveat attached to them
Paraphrase:  Published 24 Feb 2025. States "Claude 3.7 Sonnet achieves state-of-the-art performance on TAU-bench, a framework that tests AI agents on complex real-world tasks with user and tool interactions," backed by a bar chart titled "Agentic tool use — TAU-bench" with two panels, "TAU-bench (retail)" and "TAU-bench (airline)."
Locators:    Body copy, "Agentic coding and tool use" section; embedded chart image (retrieved directly at https://www-cdn.anthropic.com/images/4zrzovbb/website/787e59d548c230afd7efaed1bda1fb7f7ca207b8-1920x1114.png and read visually — bar values below are read off that image, not OCR'd from surrounding text); Appendix note on methodology in the same page's HTML (searched via saved page source)
Quote:       "Scores were achieved with a prompt addendum to the Airline Agent Policy instructing Claude to better utilize a 'planning' tool... To accommodate the additional steps Claude incurs by utilizing more thinking, the maximum number of steps... was increased from 30 to 100... Additionally, the TAU-bench score for Claude 3.5 Sonnet (new) differs from what we originally reported on release because of small dataset improvements introduced since then."

URL:         https://sierra.ai/blog/tau-bench-shaping-development-evaluation-agents
Kind:        primary — Sierra's own company blog framing its own benchmark
Establishes: How the benchmark's own creator frames the pass^k point for a public audience (i.e., that Sierra itself does not present τ-bench as a single competence number)
Paraphrase:  Published 18 Mar 2025. Restates the paper's own framing: the benchmark "doesn't just test whether an agent can complete a task once; it measures whether it can do so reliably across repeated attempts," and states current best models reach "80% pass^1 in the easier domain (retail)" while stressing that performance "degrades as k increases."
Locators:    Body copy, main sections on purpose and on the pass^k metric
Quote:       "τ-bench doesn't just test whether an agent can complete a task once; it measures whether it can do so reliably across repeated attempts."

URL:         https://www.automationanywhere.com/company/blog/product-insights/ai-agent-benchmark
Kind:        primary — a vendor's own report of its own agent's τ-bench score, for what it establishes about that vendor's own claim
Establishes: A counter-example to the "bare number, no context" pattern: this particular 2026 vendor post reports pass^1 through pass^4 side by side and explicitly explains what each level means, rather than quoting pass^1 alone
Paraphrase:  Published 18 May 2026. Claims pass^1 74.50%, pass^2 67.90%, pass^3 63.60%, pass^4 60.30% for its own agent, and states plainly that "pass^1 measures raw task accuracy. pass^4 measures consistency: the agent must complete the same task correctly across four independent runs."
Locators:    Body copy, the τ-bench results section
Quote:       "Performance that holds across pass^2, pass^3, and pass^4 is a stronger signal of architectural reliability than a single successful run."

URL:         https://benchmarkingagents.com/tau-bench-retail-airline/
Kind:        secondary — independent third-party benchmark-review site, no authorship or stake in τ-bench, reporting on and interpreting published scores
Establishes: Only that the frozen leaderboard numbers and the pass^1/pass^k distinction have been independently reported elsewhere, and articulates the caution the commission's angle depends on; establishes nothing not already confirmed against a primary source above
Paraphrase:  Restates the GitHub leaderboard figures (Claude 3.5 Sonnet 69.2% retail / 46.0% airline; GPT-4o 60.4% / 42.0%, both matching the primary GitHub source above) and warns that cross-model, cross-version comparisons on τ-bench are unreliable without confirming which benchmark version (original, "clean" variant, or τ²-bench) produced a given score.
Locators:    Body copy, leaderboard-figures section and closing editorial note
Quote:       "Read every score as a claim, not a fact." / "pass^k is harsher because it requires reproducible success."
```

## Contradictions

- **The paper contradicts itself on gpt-4o's τ-airline pass^1 figure.** Table 2 (main results, p.6) reports gpt-4o at 35.2% on τ-airline. Table 3 (the policy-ablation table, p.8), reporting the "with policy" baseline for the same model in the same domain, gives 33.2%. These should be the same number (both are the standard function-calling agent with the domain policy in the system prompt) and are not; the discrepancy is under 2 points and does not change any qualitative claim in the commission, but a precision-sensitive citation should use Table 2 (the paper's designated "main results" table) and flag the smaller figure as a discrepancy if both are ever shown side by side.
- **A separate, isolated failure-analysis run reports a different pass^1 for gpt-4o retail.** §5.2 (p.7) states "We sample 115 gpt-4o agent trajectories in τ-retail (1 trial per task), out of which 40 tasks have failed (pass^1=65.2%)" — 75/115 = 65.2%. This is a single-trial run used only for qualitative failure-mode analysis, distinct from Table 2's headline 61.2%, which is an average over "at least 3 trials per task" (§5, p.6). The two are not comparable and the record keeps them separate; a citation of the headline retail number should use 61.2%, not 65.2%.
- **τ²-bench's retail/airline task sets are not the same tasks as the original paper's.** τ²-bench evaluates on "verified" versions of the retail and airline domains (its Table 1 still lists 115 and 50 tasks, matching the original counts, but the GitHub repo's own warning states the underlying tasks were subsequently corrected in τ³-bench). Any pass^1 figure quoted from τ²-bench for gpt-4.1 or similar (74% retail / 56% airline, per τ²-bench Figure 3) should not be read as directly comparable to the original paper's Table 2 figures for older models; they come from a revised task set and a different, later evaluation harness.
- **The Claude 3.7 Sonnet figures are not run under the paper's baseline scaffold.** Anthropic's own appendix note (quoted above) states the 81.2%/58.4% figures used a custom "planning tool" prompt addition and a step limit of 100 rather than the original paper's default limit of 30 agent actions (§5, p.6 of the original paper). This is a real, sourced instance of the same benchmark name producing numbers that are not apples-to-apples with the paper's own baseline — useful evidence for the commission's broader point, distinct from the pass@1-vs-pass^k gap itself.
- **Not every public quotation of a τ-bench score omits the reliability context.** The Automation Anywhere vendor post (May 2026) reports pass^1 through pass^4 side by side with an explanation of what each level means. This does not undermine the commission's core case (the paper's own reliability collapse, and Anthropic's un-paired pass^1 chart, both stand as sourced), but it means the angle should be stated as "a bare single-run number is often the only thing quoted" rather than "always," since at least one identified counter-example reports responsibly.
- Searched specifically for a public case where a company or article quotes a τ-bench pass@1 number explicitly as general "competence" or "reliability" with no reliability caveat anywhere in the same document, beyond the Anthropic chart. None surfaced under my access; the Anthropic chart (a single pass@1-style figure per domain, presented as "state-of-the-art performance," with no pass^k figure in the same visual) is the strongest verified instance and is the one the record relies on.

## Numbers

```text
Figure: gpt-4o, τ-retail, pass^1 = 61.2%
Owner:  τ-bench paper, Table 2 (p.6)
Scope:  Average reward over ≥3 trials per task, across all 115 τ-retail tasks; function-calling agent with domain policy in system prompt

Figure: gpt-4o, τ-airline, pass^1 = 35.2%
Owner:  τ-bench paper, Table 2 (p.6)
Scope:  Average reward over ≥3 trials per task, across all 50 τ-airline tasks; function-calling agent with domain policy in system prompt

Figure: gpt-4o, τ-retail, pass^8 < 25%
Owner:  τ-bench paper, Abstract and §5.1 (p.7), read off Figure 4
Scope:  Chance that all 8 of 8 i.i.d. trials succeed on the same task, averaged across τ-retail tasks; k=8 is the value the paper's own headline claim uses, though Figure 4 plots k = 1, 2, 4, 8, 16, 32

Figure: claude-3-opus, τ-retail / τ-airline, pass^1 = 44.2% / 34.7% (avg 39.5%)
Owner:  τ-bench paper, Table 2 (p.6)
Scope:  Same trial/averaging convention as above; best non-OpenAI model in the original paper

Figure: full pass^1 table (all 12 model/method rows), τ-retail | τ-airline | weighted avg
Owner:  τ-bench paper, Table 2 (p.6)
Scope:  gpt-4o 61.2|35.2|48.2; gpt-4-turbo 57.7|32.4|45.1; gpt-4-32k 56.5|33.0|44.8; gpt-3.5-turbo 20.0|10.8|15.4; claude-3-opus 44.2|34.7|39.5; claude-3-sonnet 26.3|27.6|27.0; claude-3-haiku 19.0|14.4|16.7; gemini-1.5-pro 21.7|14.0|17.9; gemini-1.5-flash 17.4|26.0|21.7; mistral-large 30.7|22.4|26.6; mixtral-8x22b 17.7|31.6|24.7; meta-llama-3-70B 14.8|14.4|14.6 (avg is weighted by domain, not by task count)

Figure: domain size — τ-retail: 500 users, 50 products, 1,000 orders, 115 tasks, 7 write + 8 non-write API tools; τ-airline: 500 users, 300 flights, 2,000 reservations, 50 tasks, 6 write + 7 non-write API tools
Owner:  τ-bench paper, Table 1 (p.5)
Scope:  Full benchmark construction, not a per-model result

Figure: policy-removal ablation, pass^1 with vs. without domain policy in the system prompt — gpt-4o: 61.2%→56.8% (retail), 33.2%→10.8% (airline); gpt-3.5-turbo: 20.0%→14.5% (retail), 10.8%→9.6% (airline)
Owner:  τ-bench paper, Table 3 (p.8)
Scope:  Same trial convention as Table 2; note the airline gpt-4o "with policy" figure here (33.2%) differs from Table 2's 35.2% — see Contradictions

Figure: gpt-4.1, τ²-bench pass^1 = 74% (retail), 56% (airline), 34% (telecom, new domain)
Owner:  τ²-bench paper, §1 Introduction and Figure 3 (p.2, p.7)
Scope:  τ²-bench's own "verified" retail/airline task sets (not the original paper's exact tasks), 4 trials per task, k = 1-4 only (no k=8 reported for retail/airline in this paper)

Figure: original τ-bench user-simulator error rate — retail 40% total (12% critical), airline 47% total (13% critical), out of 50 and 100 manually annotated conversations respectively
Owner:  τ²-bench paper, Table 2 (p.10)
Scope:  Manual two-annotator audit of gpt-4-turbo-generated conversations; "critical" = high-severity errors that prevent task completion; this quantifies the original paper's own qualitative "simulated user has limitations" caveat

Figure: Claude 3.5 Sonnet (20241022), τ-bench leaderboard pass^1 = 69.2% (retail), 46.0% (airline); pass^2/3/4 = 57.6%/50.9%/46.2% (retail), 32.6%/26.3%/22.5% (airline)
Owner:  github.com/sierra-research/tau-bench, README leaderboard table
Scope:  Same original frozen task set as the paper (post-publication addition to the repo, same evaluation code); top of both leaderboards as of the researcher's access

Figure: Claude 3.7 Sonnet, TAU-bench pass@1-style = 81.2% (retail), 58.4% (airline); Claude 3.5 Sonnet (new) = 71.5% / 48.8%; OpenAI o1 = 73.5% / 54.2%
Owner:  anthropic.com/news/claude-3-7-sonnet, "Agentic tool use — TAU-bench" chart (published 24 Feb 2025)
Scope:  Anthropic's own evaluation, non-default scaffolding (planning-tool prompt, 100-step limit vs. the paper's 30); the o1 figure is Anthropic's report of OpenAI's number, not independently confirmed against OpenAI's own page (inaccessible — see Discarded)
```

## Source assets

```text
Asset: Table 2, "Pass^1 across models via function calling" (τ-bench paper, p.6)
Shows: The full model-comparison table the "headline number" claim rests on — every model's single-run success rate side by side, retail and airline
Crop:  Keep the full table (all 12 rows) and both domain columns; the average column is weighted by domain and should not be dropped without saying so

Asset: Figure 4, "pass^k (–) and pass@k (··) in τ-retail" (τ-bench paper, p.7)
Shows: The actual shape of the reliability collapse — five models' pass^k curves falling as k rises from 1 to 32, with pass@k (at-least-once) curves rising over the same range for contrast
Crop:  The chart has no printed axis-value table, so any crop or redrawing must not imply exact intermediate values; keep the axis labels (k on a log scale, 1-32) and the legend distinguishing pass^k from pass@k, since the pass^k vs. pass@k distinction is the whole point of the commission

Asset: Anthropic's "Agentic tool use — TAU-bench" bar chart (anthropic.com/news/claude-3-7-sonnet)
Shows: Exactly what a reader encounters in public use — three models' single-number scores per domain, presented with no reliability figure alongside
Crop:  Keep both panels (retail and airline) and all three models' bars with their labels; do not crop to Claude 3.7 Sonnet alone, since the contrast with o1 and Claude 3.5 Sonnet is what makes the chart legible as "a public score," and do not add a pass^k series to it that Anthropic did not publish alongside it

Asset: Figure 1(b), the JK9O19 example trajectory (τ-bench paper, p.2)
Shows: A short, five-turn concrete walkthrough of exactly what the commission needs to teach — tool call, database read, a policy-driven refusal, and a negotiated resolution (cancel-and-rebook) followed by a database write
Crop:  Keep the whole exchange; it is already short and each turn depends on the one before it
```

## Discarded

```text
URL: https://openai.com/index/o1-and-new-tools-for-developers/ — attempted fetch returns HTTP 403 from this environment both directly and via a browser-style user agent; the Wayback Machine mirror is unreachable from this environment. Not cited as a verified primary source; the o1 TAU-bench figures used in the record are attributed only to Anthropic's report of them (see Numbers), not to OpenAI's own page.
URL: https://arxiv.org/pdf/2406.12045 — same document as https://arxiv.org/abs/2406.12045, cited by its abstract/landing page per the researcher standard of citing the document's own page rather than the fetch route used to read it.
URL: https://arxiv.org/pdf/2506.07982 — same document as https://arxiv.org/abs/2506.07982, same reason.
Note: benchmarkingagents.com's own "Tau-Bench 2026" and "Tau3-Bench" pages, and several other 2026-dated leaderboard/aggregator sites surfaced in search (llm-stats.com, benchlm.ai, qaskills.sh, steel.dev leaderboard, aiwiki.ai, toloka.ai), were not opened or cited. They repeat figures already confirmed against the primary GitHub leaderboard and the two papers, and citing them in addition would not establish anything new; the one third-party site actually opened and cited (benchmarkingagents.com/tau-bench-retail-airline/) meets the commission's secondary-source requirement.
```

## Published neighbors to link (from `nb history --library /home/user/library-checkout`)

```text
the-instruments/swe-bench — "Change which SWE-bench tasks are counted and GPT-4o's score doubles" (2026-07-20)
the-instruments/llm-as-a-judge — "Answer order alone swung a language model's verdict by 80 points" (2026-07-29)
the-instruments/alpacaeval — "An AlpacaEval win rate is a judge's preference, and the longer answer can win it" (2026-08-10)
```

The commission specifically calls for linking llm-as-a-judge where the simulated user
and model-graded outcome connect; note for the writer that τ-bench's simulated user
is not itself an LLM-as-a-judge grader — the τ-bench reward is a rule-based database
comparison, not a model verdict (τ-bench paper, p.4, "Faithful rule-based evaluation").
The connection to draw is narrower than "both use a model to grade": τ-bench uses an
LM only to play the user and generate conversation, while llm-as-a-judge covers an LM
scoring the outcome. Conflating the two would misstate what τ-bench's own reward
mechanism does.
