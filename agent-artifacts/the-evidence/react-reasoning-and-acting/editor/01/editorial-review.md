# editorial review: the-evidence/react-reasoning-and-acting (01)

Decision: approved. No required change remains; everything below was fixed in
place and nothing false ships.

## Numbers, re-verified against evidence.md

Every figure in the piece was checked against the evidence record, which reads
Table 1, Table 2, Table 3, and Table 4 from the paper PDF.

- HotpotQA EM 27.4 / CoT 29.4 / Standard 28.7: correct. The bad automated
  summary (78/69/39) does not appear anywhere in the draft.
- Comparison table (28.7/57.1, 29.4/56.3, 27.4/60.9, and the ReAct→CoT-SC
  hybrid row 35.1/62.0): all match Table 1.
- FEVER 60.9 vs 56.3, the quoted line "outperforms CoT on Fever (60.9 vs. 56.3)
  and slightly lags behind CoT on HotpotQA (27.4 vs. 29.4)": verbatim to
  evidence. Supervised 67.5 on HotpotQA: correct.
- Hallucination analysis (56% / 0% failure hallucination; 14% / 6% success false
  positive; 47% / 16% reasoning error; 23% search error; 200 trajectories,
  50+50 each): all match Table 2.
- ALFWorld 71 / Act 45 / BUTLER 37, worst ReAct trial beats both (48): matches
  Table 3. WebShop 40 vs ~30, humans ~60: matches Table 4. The 34-point and
  10-point gaps (abstract's "34% and 10%") are placed correctly as the two
  interactive benchmarks only.

## Substantive edits

1. Hybrid claim corrected. The draft said the hybrid gave "its best marks on
   both" benchmarks. Evidence shows the best HotpotQA method is ReAct→CoT-SC
   (35.1) while the best FEVER method is the reverse hybrid CoT-SC→ReAct (64.6),
   a different ordering. Rewrote to claim only the HotpotQA best (35.1), which is
   what the table and the surrounding sentence support.

2. Unsourced figure cut. "built from 1.18 million real Amazon products" — that
   product count is not in evidence.md. Per the brief (cut any figure the source
   record does not settle), removed it; WebShop is now described in general terms
   the record supports ("a simulated shopping site where the model has to buy an
   item matching a written request"). No number was invented to replace it.

3. Overclaim fixed in the takeaway. "that loop roughly doubled the previous
   best" was true for ALFWorld (71 vs 37) but false for WebShop (40 vs 30, a
   third higher, not doubled). Replaced with the actual margins already in the
   body: 34 points on the household game, 10 on the shopping site.

4. Body no longer closes on a verdict-restate. The final body section ended with
   a whole-article results summary ("The specific method... was uneven. It was
   strong on grounding and on the interactive tasks, and behind plain reasoning
   on the trivia benchmark..."), which is the takeaway's job and which the press
   rule bars from the body. Trimmed it so the section lands its own point: what
   carried forward from the paper into today's loops.

5. Last sentence of the article deleted. "What every agent kept is the one line
   worth keeping: think, act, look at what happened, think again" restated the
   loop the takeaway's first sentence already gives, wrapped in an
   unearned-punchline frame ("the one line worth keeping"). Deleted rather than
   repaired; the takeaway now ends on the earned judgment, "its measured result
   is narrower than that reputation."

6. Unsourced universal cut. "and every major provider ships a version of it" —
   the record documents two providers (Anthropic, OpenAI), not all. Cut; the two
   citations already establish the loop is not vendor-specific.

7. Punctuation. A three-clause semicolon chain in the tool-call paragraph became
   two sentences, per the house punctuation rule.

## Headline, dek, headings

- Headline states ReAct's own concrete surprise (it trailed chain-of-thought on
  its home benchmark). It does not use the desk's "credited with X, never Y"
  mold. Kept.
- Dek adds the grounding win (invented facts erased) rather than restating the
  headline loss, and names the who (Yao's team, PaLM-540B, few-shot). It is a
  two-clause comma-and line, not the banned comma-triad or the "did A, lost at
  B" reversal. Kept.
- Headings reconstruct the argument in the piece's own nouns; none is a
  scaffolding slot, and only one is a comma-and construction, so no paper-wide
  mold. Kept.

## Links and citations

Chain-of-thought and tool-use are linked in Background and at first mention in
prose, not re-taught. Inline citations resolve to the right entries under the
article's own numbering (the PaLM claim to s2, the CoT baseline to s3, tool-use
to s4, function-calling to s5, the loose modern usage to s6). Source floor met:
6 sources, 5 primary, 1 secondary.

## Could not verify

The ALFWorld illustration ("putting a pepper shaker on a drawer") is not in
evidence.md, but its stilted "on a drawer" phrasing is the paper's own ALFWorld
task wording, it is descriptive rather than a load-bearing figure, and it is
cited to the paper (s1). Kept as low-risk paper-derived color; flagged here for
the record. Nothing numeric was left unverified.

## Proof

./nb check → verdict PUBLISHABLE, BLOCK 0, WARN 0. Word count 1716 (in band).
