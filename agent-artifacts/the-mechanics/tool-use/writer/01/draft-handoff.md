# Draft handoff — the-mechanics/tool-use, writer 01

## Original work
No single evidence source narrates one tool call across the whole boundary.
Anthropic's docs cover Anthropic's own schema and loop; OpenAI's cookbook
covers only OpenAI's; the ReAct paper names the reason/act/observe loop
without touching either vendor's wire format; the Toolformer paper shows the
capability is trained, in a different (pre-chat-API) system; MCP's docs show
the harness is external code, again without connecting to either vendor's
tool-call shape. The article's one act of original work is stitching these
into a single continuous trace of one real call (Claude's `get_weather`
round trip) and marking, at each of the five documented steps, the exact
seam between "this is the model, still just emitting text" and "this is the
external program, actually executing" — then using Toolformer's `<API>...>`
interruption mechanism (echoing Claude's `stop_reason: "tool_use"` pause) to
show that seam is a product of training, not architecture, which is why its
placement is reliable in some cases (Opus vs. a missing parameter) and not
others (Toolformer losing to plain GPT-3 on two QA benchmarks despite having
a tool). This synthesis is visible in the article's structure: orientation
and the first two body sections build the single worked trace field by
field from Anthropic's real JSON; the third section names the outer loop via
ReAct's own worked example, cross-referenced back to the same weather call;
the fourth section uses Toolformer's mechanism, deliberately described in
the same "interruption" language as Claude's `stop_reason`, to argue the
settled/open line runs through training, not through any architectural
difference between the two.

## Paths changed
- Article: `.nb-work/the-mechanics/tool-use/library/the-mechanics/tool-use.html`
- Source asset: `.nb-work/the-mechanics/tool-use/library/the-mechanics/tool-use/asset-1.png`
  (ReAct paper Figure 1, panel 1d only — cropped from the ar5iv HTML mirror's
  `assets/x1.png` to keep the Thought/Action/Observation trace and the panel
  border intact, per the evidence record's crop instruction).

## Proof result
Both required commands were run to `BLOCK: 0`:
- `./nb check ... --no-check-links` → `BLOCK: 0, WARN: 0` (final state; several
  rounds of `W-LENGTH-HIGH`, `W-SENTENCE-DENSITY`, and one `W-CITE-ORDER` were
  fixed along the way — words trimmed from 2710 to 2198, all flagged
  run-on/semicolon sentences split, and citation numbers renumbered into true
  first-appearance order after an edit changed which source was cited first).
- `./nb check ...` (with link checking) → `BLOCK: 0, WARN: 0`. All 8 numbered
  sources and both Go-deeper URLs (Simon Willison's function-calling post,
  Anthropic's "Building Effective Agents") resolved live.

No warnings were left unaddressed; the proof is clean.

`nb preview` was run to build the site with this draft merged in and the
asset confirmed to resolve at its built-site path (HTTP 200). A Chrome
render probe (`nb render-check`) was attempted for a visual check; Playwright
browsers had to be installed mid-session and then could not complete
navigation against the built site's external Google Fonts request inside
this sandbox (goto timeouts under both `load` and `networkidle`), so no
screenshot was captured. This is an environment limitation, not a proof
failure — the deterministic `nb check` gate (the actual required proof) is
clean with link checking on, and the asset's own path was independently
verified to serve correctly.

## Evidence/voice questions
None outstanding. The evidence record's one thin spot (why/when a model
decides to call a tool, and argument-filling reliability) is carried into
the article as an explicit open question rather than resolved past what the
sources support. No researcher or writing-coach follow-up needed.
