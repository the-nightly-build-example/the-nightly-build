# Editorial review 01 — what-could-go-wrong/jailbreaks

## Skeptic

Skeptic: thesis "safety training is a learned pattern, not an enforced
boundary, so optimizer-found and other automated jailbreaks transfer and
every published defense still has a residual failure rate — but the stronger
claim that robust refusal is *impossible in principle* is an active,
unresolved conjecture, not a proven fact"; tested 4 claims (GCG's white-box
and transfer ASR figures; constitutional classifiers' residual failure rate
and bug-bounty numbers; many-shot jailbreaking's scaling claim and 61%→2%
mitigation figure; whether the Vassilev-proof section ever slides "empirically
unsolved / suspected hard" into "proven impossible" or the reverse); broke:

- A chronology/attribution error. The draft called Kolter and Fredrikson
  "who would soon co-author GCG" when quoting the *New York Times* — but I
  fetched the cited piece directly (Cade Metz, July 27, 2023) and it is the
  same-day report on GCG's release; it names Kolter "an author of the report"
  at the moment of the quote. The next section then said "Kolter and
  Fredrikson were talking about their own paper," contradicting the "soon."
  Fixed directly: they're now introduced as "two of the report's authors,"
  and the now-redundant reveal sentence is cut.
- A dek precision failure. "Cut a similar attack's success rate from 86% to
  under 5%" implied the constitutional-classifiers figure was measured
  against GCG-style optimizer suffixes specifically. I fetched the paper's
  Section 5.1 directly: the held-out evaluation set is a broad mix of
  published jailbreak techniques, novel internally-discovered attacks, and
  cipher/translation/reformulation transforms — not primarily GCG-style
  suffixes. Fixed the dek (both the JSON `dek` field and the visible
  dekline) to "cut a broad set of jailbreak attempts from 86% success to
  under 5%." The body text already said "held-out red-team attempts"
  correctly; only the dek overreached.
- One unfixable gap, not a broken sentence: the draft never steelmans the
  "jailbreak risk is overstated because the underlying information is
  already public" argument. The commission's source obligations explicitly
  require this ("the best case that it does not matter (dual-use info
  availability). Steelman both."), and this review's brief separately names
  it as a thing to confirm. It is not in the article. The evidence record
  explains why: the one source found (an EA Forum biosecurity playbook)
  hit an HTTP 403 and was not retried through an alternate route, and the
  draft-handoff substitutes the Vassilev-vs-anonymous-critics tension to
  satisfy "check confidence in both directions" instead — a different,
  narrower tension (about whether an impossibility *proof* generalizes) than
  the commission's requested one (about whether jailbreak *risk* is
  overstated given information is already public). This is missing
  evidence, not a prose problem; see Required work below.

Every load-bearing number I recomputed against the primary matched exactly:
GCG Table 1/2 (fetched ar5iv directly, cross-checked the chart-1.py
provenance cell by cell against Table 2), constitutional classifiers'
86%/4.4%/0.38%/23.7% and the bug-bounty figures (fetched both the Anthropic
post and the arXiv paper's Section 4.1/5.2 directly — the post's rounded
">3,000 hours" and the paper's precise "4,720 hours (90% CI...)" are two
different documents' precision, not a contradiction), many-shot's 61%→2%
(fetched the post directly), next-gen's "87% drop" (fetched the post
directly — it is Anthropic's own 0.38%→0.05% computation, correctly
attributed), and Vassilev's theorems, "no recipes" caveat, and NIST
affiliation (fetched the arXiv HTML directly). The central hedge — "robust
refusal is empirically unsolved, theoretically suspected to be hard, and not
proven impossible" — holds the line the brief asked me to test hardest: it
never upgrades "suspected hard" into "proven," and it correctly scopes what
*is* proven (Vassilev's theorem for his own formal "checker" object) from
what critics dispute (whether that object is what a real defense is).

## Cut

Cut: 3 sentences; worst tell: "This lesson keeps them separate" in the Why
this matters bookend — the floor's banned move of a piece narrating its own
method rather than making a claim. Also cut "Kolter and Fredrikson were
talking about their own paper" (redundant once the chronology fix above
already identifies them as the report's authors) and "That ranking does not
hold for every attack" (a signpost the paragraph's own numbers, and its
closing synthesis sentence, already deliver without it).

Separately, not a cut but a reflex-mark fix: 9 of 11 body-prose semicolons
were joining two independent, self-sufficient clauses (parallel stat pairs,
mostly) where the floor's "when in doubt, the period is the default"
applied cleanly — converted to periods with capitalization, no words added
or removed. Kept the 2 semicolons doing real work.

## Reader

Reader: this gives me a pattern no single cited paper states — that "which
model resists best" is not a fixed ranking but flips by attack family (GCG's
suffix attack finds Claude hardest; Wei et al.'s combination attacks find
Claude v1.3 more vulnerable than GPT-4; the poetry paper splits differently
again) — stitched from three independent papers that never cite each other,
plus a clean three-way sort (demonstrated / demonstrated-but-bounded /
conjectured) that lets a reader classify any future jailbreak headline by
what kind of claim it actually is. This matches the draft-handoff's
original-work sentence and survives the cut. Prose reads closer to the
Carlini/Willison exemplars (short declarative sentences, hedge on the exact
clause, method named with the number) than to a median AI summary. The
headline, reread as the largest claim, states exactly what's demonstrated
(transfer occurred) without borrowing the conjecture's weight.

## Direct edits made

1. Fixed the Kolter/Fredrikson chronology error (orientation section) and
   cut the now-redundant "were talking about their own paper" reveal
   (found-not-composed section); named Vicuna-7B for the 99%/98% white-box
   figures that the sentence had left unattributed.
2. Cut "This lesson keeps them separate" (Why this matters) and "That
   ranking does not hold for every attack" (found-not-composed).
3. Fixed the dek's "a similar attack's success rate" to "a broad set of
   jailbreak attempts" in both the JSON `nb-meta` and the visible dekline.
4. Converted 9 reflex semicolons to periods across the piece (orientation,
   found-not-composed, short-of-zero, proof-not-measurement, the takeaway).
5. Updated `nb-meta` "words" from 2197 to 2181 to keep the count honest
   after the cuts (recomputed by stripping tags/scripts from the rendered
   article and calibrating against the pre-edit 2197 baseline; the -16 word
   delta matches exactly). `reading_minutes` stays 11 (2181 still rounds up
   to 11 at ~200 wpm); left the visible "11 min read" byline unchanged.

No markup, script, style, asset, or citation-URL was touched.

## Required work by owner

- **Researcher**: find a genuine, attributable source — a named figure,
  developed argument, or credible outlet, not a fabricated composite — for
  the "jailbreak risk is overstated because the underlying harmful
  information is already publicly accessible" position. This is the
  commission's explicit "dual-use info availability" steelman
  (`commission.md`, Source obligations) and this review's brief separately
  asks me to confirm it. My own search attempts turned up only glancing,
  loosely-related commentary (e.g., a general "no risks beyond other public
  models" remark in an unrelated context) — nothing yet at the bar this
  paper's citation policy requires. Do not let the writer paraphrase around
  the gap; if no adequate source exists, evidence.md should say so plainly
  and the commission should be asked whether the requirement stands.
- **Writer** (after evidence lands): add a passage — most naturally beside
  the CJS severity-scale paragraph in "A mathematical proof is not the same
  as a measurement," where the piece already covers who argues what today —
  steelmanning that dismissive position at full strength, the way the
  doom-side argument is steelmanned in the opening. This is new prose past a
  clause, so it is writer work once the researcher supplies the source.

## Decision

Publication-blocking: the commission's explicit "steelman both" requirement
for the dismissive/info-already-public position is unmet, and no source in
the current evidence record clears the citation bar to fix it. Not a
redraft of what exists — a missing piece the researcher needs to supply
first.
