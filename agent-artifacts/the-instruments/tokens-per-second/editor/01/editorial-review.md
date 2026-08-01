# Editorial review 01 — the-instruments/tokens-per-second

## Skeptic
Skeptic: thesis "a bare tokens-per-second figure is uninterpretable until you
name which phase was timed, how many requests shared the chip, whose
tokenizer counted, and what hardware/context produced it"; tested 4 pillar
claims plus the misuse-case comparison (Groq/Anyscale, NVIDIA press/audited,
Cerebras, MLPerf Server/Interactive); broke: the pillar-2 batch-size worked
example (and its chart) misstates its own primary source's conditions, and a
citation on the headline's own load-bearing number points to a page that
never mentions the claim it is cited for.

Verified against primaries directly (not just the evidence record): Groq's
270+ tok/s claim and its own explanation for the Anyscale gap
(groq.com/blog), the MLPerf Server/Offline/Interactive definitions and the
2,000/200ms and 450/40ms latency bounds (MLCommons's rules doc, its 2024 and
2025 posts), NVIDIA's audited B200 NVL8 figures (98,443/98,858) and the
Interactive bound restated in its own blog, IEEE Spectrum's "unverified"
869,200 tok/s framing, Cerebras's 2,100 tok/s and 20%-variance disclaimer,
and — by pulling `summary_results.json` directly — the exact Nebius
B200x8 Server/Interactive/Offline row (101,611 / 59,622.7 / 101,246), which
confirms the article's "41 percent drop on identical silicon" arithmetic.
All of these hold.

Two things broke:

1. **The batch-size worked example (pillar 2) misrepresents its own primary.**
   The article and its chart claim "a Llama-13B model on a single H200 GPU,
   128 input and 128 output tokens held fixed... an 8.8-fold range with
   nothing changed but the request count." I fetched the cited primary
   directly (`NVIDIA/TensorRT-LLM/.../H200launch.md`). Its table shows three
   *different* input/output configurations at the three batch sizes actually
   used: batch 64 is 2,048-in/128-out, batch 128 is 128-in/2,048-out, and
   only batch 1,024 is 128-in/128-out. The 1,349 → 4,750 → 11,819 tok/s figures
   are accurate quotes, but "held fixed" and "nothing changed but the request
   count" are false — prompt length and output length change at every step,
   confounded with batch size. This is not a citation slip; it is the
   pillar's central worked-arithmetic claim (the voice guide's required
   device for every variable) and it anchors chart-1.png and its caption
   ("same 128-in/128-out prompt length"), which inherits the same error. The
   evidence record itself (Numbers table, row "TensorRT-LLM, Llama-13B, H200,
   batch-size sweep") states "same model/HW/context" and "128 input / 128
   output tokens" for all three rows — that extraction from the primary is
   what is wrong, and the writer built faithfully on it. This traces to a
   researcher extraction error, not a writer invention.

2. **A related, softer version of the same problem in pillar 4.** The
   context-length paragraph cites the same primary for "1.9 times the
   throughput on a 2,048-input summarization job, only 1.6 times on an
   80-input chat exchange... changing with the workload alone." The 1.9x/1.6x
   figures are accurate quotes, but the primary's own two examples differ in
   model (Llama-70B vs. GPT-3 175B) and tensor-parallel configuration (TP1 vs.
   TP8), not context length alone. "Workload alone" overstates what the
   comparison isolates. Lower severity than #1 (no chart rides on it, and
   "workload" is loosely defensible as covering model+shape together), but it
   comes from the same primary and the same evidence-extraction gap, so it
   should be fixed in the same pass.

3. **Miscitation on the headline's own number.** Source `s2` was cited three
   times for Anyscale's 185 tok/s Groq measurement (orientation section,
   "Where the stopwatch starts," and the comparison table), and its `href`
   pointed to `anyscale.com/blog/reproducible-performance-metrics-for-llm-inference`.
   I fetched that page directly: it names only Anyscale Endpoints, Fireworks,
   and Perplexity as tested providers; "Groq" does not appear anywhere on it.
   The 185/184/148–208 tok/s and 0.22s-TTFT figures live on
   `github.com/ray-project/llmperf-leaderboard`, which the evidence record
   already documents as part of the same source (its own locator says the
   Groq figures come from "the leaderboard table... shown in the GitHub
   README," distinct from the blog). I fixed this myself — see Direct edits —
   since the right source was already at hand in the evidence record.

I did not find a case where a vendor-peak number was actually indefensible;
the Cerebras and per-GPU-normalized NVIDIA cases both check out as reported,
fairly.

## Cut
Cut: 0 sentences removed outright (the prose is already tight; the only
padding I found requires more than a clause to fix); worst tell: the
takeaway's opening — "Tokens per second is not one measurement. It is a
family of them." — is a lightly rewritten version of the commission's own
assignment language ("'tokens per second' is not one number; it is a family
of numbers"), i.e. the piece fulfilling its brief instead of stating its own
conclusion. I could not repair this with a clause-level cut: deleting it
strands "which member got measured" two sentences later with no antecedent,
and any replacement is new prose. Flagged to the writer below. No other
prompt-leakage, formula openers/closers, hedged-contrast, or manufactured
punchlines survived scrutiny — the guess-then-reveal structure, the
short/long sentence variation, and the four-variable worked examples all
follow the voice guide's calibrated moves rather than a generic AI median.

## Reader
Reader: this gives me the four questions to ask any tokens-per-second claim,
and — the part no single cited source supplies — a six-way comparison table
that puts Groq's dashboard figure, Anyscale's independent measurement of the
same service, Cerebras's two claims, NVIDIA's unverified press figure, its
own audited MLPerf number, and MLPerf's own Interactive-scenario number on
one common basis (phase, concurrency, latency bound). No single source in the
record assembles that; it matches the draft-handoff's original-work
sentence. The per-GPU normalization that resolves the NVIDIA press-vs-audited
"disagreement" (≈12,357 vs. ≈12,072 tok/s/GPU) is a real earned insight, not
a restatement. Prose register sits with the voice-guide exemplars —
short declaratives carrying facts, one longer causal sentence per mechanism,
no semicolon chains — closer to Dan Luu/Marc Brooker than a median AI
summary. The headline commits to a real, checked claim: both 270 and 185 are
genuine measurements of the same Groq service, confirmed against both
primaries.

## Direct edits made
- Fixed source `s2`'s citation (Sources list only — no prose or word-count
  change): swapped its `href` from the Anyscale blog (which never mentions
  Groq) to `https://github.com/ray-project/llmperf-leaderboard` (the page
  that actually carries the 185/184/148–208 tok/s and 0.22s-TTFT figures
  the article cites it for three times), and updated the title text and
  `data-nb-locator` to match. `data-nb-kind` unchanged (primary — Anyscale/Ray
  built and ran this measurement). The right source was already documented
  in the evidence record (source 15), so this is a miscitation fix, not new
  sourcing.

## Required work by owner

**Researcher** (blocking — send first):
- Re-extract the NVIDIA/TensorRT-LLM H200 launch blog's performance table
  (`docs/source/blogs/H200launch.md`). The current evidence record's Numbers
  row for "TensorRT-LLM, Llama-13B, H200, batch-size sweep" claims "same
  model/HW/context" and "128 input / 128 output tokens" for all three
  batch-size figures (1,349/4,750/11,819). The primary's table actually shows
  three different input/output configurations (2,048/128 at batch 64,
  128/2,048 at batch 128, 128/128 at batch 1,024) — batch size is confounded
  with prompt/output length in the source data itself. Either confirm there
  is no matched-conditions row set in this table (the table has only three
  llama_13b rows total) and locate a genuine same-model/same-context,
  batch-size-only sweep elsewhere (the llama_70b rows in the same table have
  the identical confound), or supply the corrected characterization of what
  actually varies row to row so the writer can rebuild the example honestly.

**Writer** (after researcher, same pass):
- Rebuild the pillar-2 batch-size worked example and `chart-1.py`/`chart-1.png`
  once the researcher supplies accurate conditions — the current chart
  caption ("same 128-in/128-out prompt length... batch size alone moves
  throughput 8.8x") and its provenance script's docstring both assert a
  held-fixed condition the primary does not support.
- Loosen or re-anchor the pillar-4 "changing with the workload alone" claim
  (1.9x/1.6x H200-vs-H100 comparison) to acknowledge the model and
  tensor-parallel configuration also differ between the two cited examples,
  or find/request a cleaner same-model, same-TP, context-length-only
  comparison.
- Rewrite the takeaway's opening two sentences ("Tokens per second is not one
  measurement. It is a family of them.") away from the commission's own
  assignment phrasing, adjusting the downstream "which member got measured"
  callback to match whatever replaces "family."
- Re-run both proof passes (`--no-check-links` then the full check) after
  these changes; word count may shift and needs to stay in band.

## Decision
Not publishable as-is: a central worked-arithmetic claim and its chart
misstate the primary source they are built on, tracing to a researcher
extraction error. Sending to the researcher first, with the writer's
follow-on work recorded above for the orchestrator to route next.
