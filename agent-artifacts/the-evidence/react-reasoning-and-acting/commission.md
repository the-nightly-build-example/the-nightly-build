# Commission: the-evidence/react-reasoning-and-acting

## Authorized work
Scheduled `nb duty` for 2026-09-09 returned `the-evidence` in open mode. This
commission authorizes exactly one lesson reading the ReAct paper, Yao et al.,
"ReAct: Synergizing Reasoning and Acting in Language Models" (2022; ICLR 2023).
Template: lesson. Series floor: >=6 sources, >=3 primary, >=1 secondary. Word
band 1200-2200. Verified against the full published library: no the-evidence
lesson reads an LLM-agent paper; ReAct is a genuine gap.

## Why this document, and the honest angle
The Evidence reads a famous document so the reader learns what it actually says.
ReAct is the paper the whole "AI agent" idea is credited to: interleave a
model's reasoning ("thought") with actions it takes in an environment
("act") and the results it reads back ("observation"), in a loop. State what the
paper actually did: few-shot prompting (not fine-tuning) of PaLM-540B (and
GPT-3) on HotpotQA, FEVER, ALFWorld, and WebShop, with a Wikipedia-search API as
the tool; report the actual, uneven results (where ReAct beat chain-of-thought
and where it lost, and that its headline gains were task-specific). Then bring it
to the present: today's agents run native tool-calling / function-calling loops
that depart from the paper's hand-written thought/act/observation prompt format,
and "ReAct" is now invoked far more loosely than the paper's method. Say plainly
where the document's actual result is narrower than the blueprint it is credited
with.

## What the lesson teaches (short, complete)
1. What ReAct proposed: the thought/act/observation loop, with a worked trace on
   one real task (e.g. a HotpotQA multi-hop question and its Wikipedia lookups).
2. What the paper actually measured, honestly: the models, the four benchmarks,
   where ReAct beat chain-of-thought and where it did not, and the size of the
   result. Show the foundation under the "agents started here" claim.
3. How today's practice diverged: native function-calling loops vs the paper's
   prompted format, and what the paper got right (grounding reasoning in real
   observations reduces certain hallucinations) versus what later systems
   changed.

## Boundaries and neighbors
- Do not re-teach `chain-of-thought` (the CoT paper is already a the-evidence
  lesson); link it in Background. Tool-use as a mechanism is a the-mechanics
  lesson (`tool-use`); this piece reads the ReAct document, it does not re-teach
  how tool calls execute. Do not re-teach `retrieval-augmented-generation`.
- Tonight's edition also ships: the-instruments/model-flops-utilization,
  the-mechanics/speculative-decoding, what-could-go-wrong/flash-crash-risk,
  when-ai-breaks/cigna-pxdx. Stay on this document.
- Required contribution: the reader leaves able to say what ReAct actually
  showed, on what, and how far today's agent loops have moved from it.

## Sources plan
Claims come from the paper itself. Primary: the ReAct arXiv paper (2210.03629)
for the method, benchmarks, and numbers; the chain-of-thought paper (Wei et al.)
only as the baseline it is compared against; a primary source for modern
function-calling (an official function-calling / tool-use spec) to ground the
"how practice diverged" claim. Secondary: a careful explainer for context. Every
source URL must resolve; cite only what was read. NOTE: github.com is blocked in
this environment (egress 403) — do not rely on a GitHub URL as a source; use the
arXiv/official-docs versions instead.

## Recent patterns to break (habits, not rules)
- This desk's headlines heavily use the corrective-twist mold "The paper credited
  with X never did Y" / "The [doc] credited with Z [failed at W]" (see
  attention-is-all-you-need: "The paper credited with starting the LLM era never
  trained a language model"; foundation-models; gans; gpt-4-technical-report).
  Do NOT mirror that "credited with starting the X era, never Y" construction for
  ReAct. Find ReAct's own concrete surprise and state it.
- Deks: avoid the "X did A, and lost at B" comma-tail reversal (t5, alphazero).
- Section headings: do not name a final body section "How far the X reaches";
  that shape recurs paper-wide. Vary heading construction; avoid every heading
  being a comma-and clause.

## Production policy (recorded)
Profile balanced. Stages, none `required`: writing-coach effort low, researcher
effort high, writer effort medium, editor effort high; model tier "capable".
Executed with capable (Claude Opus-class) models at closest available effort. No
`required` directive traded down.
