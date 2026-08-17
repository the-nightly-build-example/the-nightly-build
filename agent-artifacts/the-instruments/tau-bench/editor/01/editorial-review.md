# Editorial review: the-instruments/tau-bench (editor/01)

## Skeptic

Thesis: a bare τ-bench percentage hides what matters — what counts as a
success, who plays the customer, and whether the number is a single run or a
repeat-success rate — and the paper's own reliability collapse plus two
documented instances of context-stripped public quoting prove it.

Claims it rests on, each tested against the primary source rather than the
evidence record's paraphrase:

1. **Mechanics and reward.** τ-bench puts a model in a tool-and-policy
   customer-service seat against an LM-played simulated customer, and grades
   by a rule-based check of final database state plus conveyed information,
   not a model's opinion. Checked against the paper itself (arXiv:2406.12045,
   §3, Figure 2's reward definition, and §4.2's "faithful rule-based
   evaluation"): holds exactly. The JK9O19 walkthrough matches Figure 1(b)'s
   trajectory and caption ("propose a new solution (cancel and rebook)").
2. **The pass^1/pass^8 collapse.** GPT-4o: 61.2% pass^1 retail, pass^8 <25%
   retail. Pulled the paper's PDF directly (Table 2, p.7, and the abstract)
   and confirmed both figures verbatim, including the exact abstract sentence
   the article quotes. Holds.
3. **The Table 2/Table 3 discrepancy (35.2% vs. 33.2%).** Confirmed from the
   paper's own Table 2 and Table 3 images: gpt-4o airline "with policy" is
   35.2% in Table 2 and 33.2% in Table 3 for what should be the same
   condition. The article flags rather than resolves it — correct, since the
   paper itself never reconciles the two numbers.
4. **Public quoting strips context.** Anthropic's un-paired TAU-bench chart
   (81.2%/58.4%, nonstandard 100-step scaffold) versus Automation Anywhere's
   paired pass^1-through-pass^4 post. Fetched both primary pages directly:
   the Anthropic methodology footnote and the Automation Anywhere quote match
   the article's quotations exactly, character for character.
5. **The simulated customer's own error rate.** 40%/47% error, 12%/13%
   critical, from τ²-bench's audit. Pulled τ²-bench's PDF directly to Table 2
   (p.10): retail 50 conversations, 12% critical/28% benign/40% total; airline
   100 conversations, 13% critical/34% benign/47% total. Exact match.

**Two breaks found and fixed** (not routed — the right source was already at
hand, so I corrected the quotation directly against it):

- The article quoted Sierra's blog as "it measures whether it can do so
  **reliably across repeated attempts**." The blog's actual sentence reads
  "it measures whether it can do so **consistently multiple times**." This
  is a genuine misquote, not a paraphrase — the evidence record itself
  already carried the wrong wording, so it reached the writer clean. Fixed
  to the verbatim text.
- The article quoted the same blog as reporting "**about** 80% pass^1 in the
  easier domain (retail)." The blog's sentence reads "the best models are
  now **crossing** 80% pass^1 in the easier domain (retail)." Fixed to the
  verbatim fragment ("now crossing 80%…").
- A third, smaller break: the orientation section cited the τ-bench paper
  (source 1) for the claim that τ-bench "is the source behind many of the
  agentic-capability percentages a reader now meets in AI marketing." The
  paper does not say this about itself — it's an editorial observation, and
  restated the Why-this-matters bookend's framing besides. Cut rather than
  re-cited, since it added nothing the bookend hadn't already said and no
  single source establishes it as a general fact (the article proves it
  concretely later, with the Anthropic and Automation Anywhere cases).

No claim in the piece rests on a source I could not verify or a source that
contradicts it. Every remaining inline citation lands on the primary and
supports the specific sentence it's attached to.

## Cut

Ran the placeholder-noun test on every sentence, the edges separately (first
and last of every paragraph, section, and the article), and the
dangling-referent read. Findings:

- The Why-this-matters card opened with `"Our agent handles 58% of customer
  requests"` in quotation marks, unattributed. The draft-handoff itself
  flagged this as illustrative phrasing, not a sourced quote — but the
  quotation marks and a specific number made it readable as a real claim
  from a real company, which the evidence record does not contain. Reworded
  to the same point without quotation marks or an invented figure:
  "Companies now routinely put a specific percentage on how much of a
  customer's request their AI 'agent' can handle."
- Three section headings opened with the same word ("One conversation…",
  "One try…", "One chart…"), an anaphora the recent-pattern brief flagged.
  Rewrote two of the three in the piece's own nouns: "The database state
  that decides whether the agent passed" (orientation) and "The chart that
  leaves out the reliability rate, and the report that doesn't"
  (the-number-in-public). Kept "One try is not the same as eight in a row"
  — it's the strongest of the three and the section is literally about the
  one/eight contrast.
- The retitled the-number-in-public heading also fixed a second problem: its
  old form ("One chart omits the reliability rate; another prints it") was
  a semicolon-reversal construction, the same mold `spec/headlines.md` bans
  in deks ("X did A; Y refuses B"). The new comma-and form drops it.
- One body semicolon failed the same test in ordinary prose: "…covers what
  happens when a language model is the one deciding who passed; τ-bench does
  not do that, since a fixed check…" — two independent clauses in a
  contrastive reversal, not the rare case the punctuation standard reserves
  a semicolon for. Split to a period, with the explanation recast as a colon
  payoff: "τ-bench does not do that: a fixed check of the database renders
  the verdict."
- No other slop-list failure survived the sentence-by-sentence and
  edge-sentence passes: no empty conclusions, no vague attribution, no
  decorative analysis verbs, no puffery, no self-reference in the body, no
  fluff openers. The closer earns its place — it states the third question
  the argument built toward (scaffolding), not a restated moral.
- Checked prompt leakage against the commission, the writer brief, and the
  editorial direction: nothing lifted. The bookends teach the lesson's own
  content, not the brief's planning language.

## Reader

A reader who has only seen a bare τ-bench percentage leaves this piece able
to ask three specific questions of any agent score — what counts as the
task's correct end state, whether the figure is a single run or a repeat
rate, and what scaffolding produced it — and leaves knowing that the last
question is not hypothetical: it is documented against the exact chart
Anthropic published. That third question, and the concrete case that earns
it, is what the sources alone would not hand a reader; the paper doesn't
discuss Anthropic's scaffolding, and Anthropic's page doesn't discuss the
paper's pass^k finding. The piece is what puts them in the same frame.

The prose sits closer to the voice-guide's exemplars than to a median AI
summary: it works the JK9O19 example fully before generalizing, states the
Table 2/Table 3 discrepancy without smoothing it over, and lets the 40–47%
simulated-customer error rate carry its own weight without an inserted
verdict.

The headline, reread as the largest claim: "GPT-4o clears 61% of τ-bench
tasks once and under 25% of them eight times in a row" is exact — both
figures are the paper's own retail-domain pass^1 and pass^8 numbers,
verified directly against Table 2 and the abstract, and the body specifies
"retail" on first use of each so the headline's economy doesn't mislead a
reader who continues past it.

## Edits

1. Reworded the Why-this-matters opener to remove the unattributed
   quotation-mark "58%" example; replaced with an unquoted, unfigured
   general statement of the same pattern.
2. Retitled the orientation heading from "One conversation, checked against
   the database it left behind" to "The database state that decides whether
   the agent passed."
3. Corrected a misquote of Sierra's blog: "reliably across repeated
   attempts" → "consistently multiple times" (verbatim source text).
4. Corrected a second misquote of the same blog: "about 80% pass^1…" →
   "now crossing 80% pass^1…" (verbatim source fragment).
5. Retitled the the-number-in-public heading from "One chart omits the
   reliability rate; another prints it" to "The chart that leaves out the
   reliability rate, and the report that doesn't," removing both the
   anaphora and the semicolon-reversal mold.
6. Split a body semicolon into a period plus a colon-introduced payoff in
   the simulated-customer section ("passed. τ-bench does not do that: a
   fixed check…").
7. Cut a sentence in the orientation section ("It is the source behind many
   of the agentic-capability percentages a reader now meets in AI
   marketing") that cited the τ-bench paper for a claim the paper does not
   make and repeated the Why-this-matters bookend's own framing.

## Required work

None. No item needs the researcher, the writer, or the orchestrator.

## Decision

**Approve.** The thesis and every claim it rests on held against the primary
sources, the two misquotes found were fixable in place because the correct
source text was already at hand, the slop and formula issues the
recent-pattern brief flagged are resolved, and the piece gives its declared
reader three durable questions no single source in its own record supplies
together.
