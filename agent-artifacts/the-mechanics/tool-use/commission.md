# Commission — the-mechanics/tool-use

## Assignment
Answer the mechanics question: when I ask a chatbot something and it searches the
web, runs code, or calls an API and comes back with a live answer, how does it
actually do that? Work backward from the visible behavior to ground. The reader
has seen an assistant "use a tool"; teach what really happens.

## Angle (work backward to ground, mark settled vs open)
The load-bearing idea: the model cannot do anything. It only emits tokens. "Tool
use" is a loop run OUTSIDE the model by a harness/orchestrator. Steps down to ground:
1. The tools are described to the model as text in the prompt (names, JSON
   schemas of arguments). This is just more tokens. Builds on
   the-mechanics/instructions-are-data (it is all one token stream) — link it.
2. When the model "calls" a tool, it emits a structured span of text (e.g., JSON
   with a tool name and arguments), exactly the way it emits any other tokens.
   Nothing is executed yet. (Ground on autoregressive-generation — link.)
3. The harness parses that span, actually runs the function/search/code, and
   pastes the result back into the context as new tokens.
4. The model runs again on the extended context and continues. Repeat until it
   emits a normal answer instead of a tool call. This outer loop (often called
   ReAct-style: reason, act, observe) is the "agent."
5. Ground: nothing below the token stream changes the answer. The model has no
   channel to the world; every action and every observation is text entering and
   leaving one context window. Training (function-calling fine-tuning), not
   architecture, is what makes the model emit well-formed calls at the right time.

Mark clearly what is settled engineering (the loop, the schema-in-prompt, the
harness executing) versus what is not fully understood (why/when the model
decides to call a tool, reliability of argument-filling, failure modes like
calling a tool it was told not to — connects to instructions-are-data/prompt
injection risk without becoming that lesson).

One concrete worked example: a single realistic turn. E.g., "What's the weather
in Paris?" -> model emits {"tool":"get_weather","args":{"city":"Paris"}} ->
harness calls the API -> pastes {"temp_c":19} back -> model writes the sentence.
Use a real, documented function-calling format (OpenAI/Anthropic tool-use schema)
so the example is faithful, not invented.

Land the judgment: the model is the reasoning core of a loop it does not run;
"the AI searched the web" is shorthand for "a program around the model searched
the web because the model asked it to, in text." This is why tools can fail
silently, why an agent can be hijacked by text in a fetched page, and why the
model never actually "knows" whether the tool ran.

## Intended reader
House reader who has used an AI that browses, runs code, or calls tools and
imagines the model itself is doing it.

## Required contribution
The reader can trace one tool call from prompt to executed action to answer, name
which part is the model and which is the harness, and spot an explanation that
skips the harness (a common error: talking as if the model "accesses" the web).

## Source obligations (the-mechanics: min 8; primary >=4, secondary >=1)
- PRIMARY: official function-calling / tool-use documentation from a major lab
  (OpenAI function calling / tools docs AND/OR Anthropic tool use docs) — the
  owning source of the request/response format. Quote the actual schema shape.
- PRIMARY: the ReAct paper (Yao et al., 2022, "ReAct: Synergizing Reasoning and
  Acting in Language Models", arXiv:2210.03629) — the reason+act+observe loop.
- PRIMARY: the Toolformer paper (Schick et al., 2023, arXiv:2302.04761) OR a
  model card describing tool-use training — evidence that this is a trained
  behavior, not architectural.
- PRIMARY: documentation of an agent framework's loop OR the MCP spec / an
  orchestration doc, to show the harness is external code (that the model output
  is parsed and executed by a program).
- SECONDARY: a clear explainer for context only.
- Seek contradiction: is any of this "built into" the model (e.g., native tool
  use, or models with sandboxed code execution)? Address honestly — even there,
  execution happens outside the weights.

## Starting sources
Anthropic tool-use docs; OpenAI function-calling docs; ReAct (2210.03629);
Toolformer (2302.04761); MCP or an agent-loop doc. Researcher verifies/completes.

## Relevant prior coverage (link, do not re-teach)
- the-mechanics/instructions-are-data — one token stream, no instruction/data
  boundary. Core dependency and the natural risk connection. Link.
- the-mechanics/autoregressive-generation — the model emits tokens one at a time,
  each becomes input. Link for step 2.
- the-mechanics/knowledge-cutoff — why tools/retrieval exist at all (weights are
  frozen; live info arrives through the prompt). Optional Background link.

## Structures NOT to repeat
- the-mechanics desk overuses the "three scenarios" cold open (instructions-are-data
  opens on three; several others open on a small numeric hook). Do not open on a
  scenario triad and do not open on a single cute number. Open on the false
  picture (model reaching out to the world) and correct it by tracing one call.
- No colon-subtitle headline; no hedged-contrast dek; no Verdict block.

## Neighboring articles tonight
Distinct from jailbreaks (that is the risk-argument desk; this is the mechanism).
If tool-use touches hijack-by-fetched-text, keep it to one sentence and defer the
argument to the jailbreaks piece; do not duplicate.

## Template / mode / paths
- template: lesson; mode: open; order: null; date: 2026-08-01.
- article: .nb-work/the-mechanics/tool-use/library/the-mechanics/tool-use.html

## Harness / model
writer: claude-code-routine / claude-sonnet-5 / medium. researcher high, editor
high, coach low; all claude-sonnet-5.

## Tags
Suggest: ["tool-use", "function-calling", "agents", "react"]. Writer finalizes.
