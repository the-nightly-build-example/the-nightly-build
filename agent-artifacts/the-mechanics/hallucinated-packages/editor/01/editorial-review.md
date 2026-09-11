# Editorial review: the-mechanics/hallucinated-packages (editor/01)

## Skeptic

Thesis: a coding assistant names a package by predicting text, with no step that
checks a registry, so it sometimes writes a name that does not exist; the
load-bearing fact is that the same invented name recurs across runs and across
models, and that predictability is what lets an attacker register the name ahead
of the developer (slopsquatting). The threat is demonstrated-plausible, not
realized in the wild.

Claims it stands on, and how each held:

1. The invention is prediction, not a failed lookup. Stated briefly and linked
   to the hallucination lesson rather than re-taught. Holds; this is the base
   mechanism the piece correctly refuses to re-explain.
2. The same invented name recurs. Within-model: 58% recurred in more than one of
   ten runs, 43% in all ten, 39% in none, from 500 prompts that each produced at
   least one hallucination, re-run ten times (s2). Cross-model: 215 shared names
   across four models (s1); 127 names all five 2026 frontier models invented
   identically (s3). Every figure matches the evidence Numbers section exactly,
   and the article correctly frames the three Spracklen figures as separate
   readings of one rerun set, not a partition that sums to 100 — the exact
   arithmetic trap the evidence's Contradictions section flagged. The two
   "repeatability" measurements (Spracklen within-model, Lanyado cross-model) are
   kept distinct, not conflated. Holds.
3. Recurrence is the hinge that turns invention into a registrable attack (s4,
   s6). Holds; the Lanyado quote ("persistence ... is the key to turning AI
   whimsy into a functional attack") is used for exactly what it says.
4. The threat is not realized. "No malicious slopsquatting attack has been
   documented in the wild"; the one registered name was Lanyado's harmless
   huggingface-cli proof of concept; "A malicious campaign is plausible, not
   observed." Sourced to s5, s1, s6 and matches the evidence. Holds, and is the
   honest state the round focus demanded.
5. The "~20%" rate is an average dominated by older open models and is falling
   (5.2% commercial vs 21.7% open, 13 of 16 models open; frontier 4.62–6.10% in
   2026). Matches s2 and s3. The rate is the fifth section, not the lead, and the
   section deflates it rather than trading on it. Holds.
6. The fix is to ground the assistant in the registry, with mitigation figures
   (RAG 16.14%→12.24%, fine-tuning →2.66%, self-detection 89%/82%) and the open
   questions named. Matches s2 and s8. Holds.

Settled-vs-open line: the recurrence section ends by marking the empirical
recurrence as established and the token-level "why this exact name" as synthesis
on the base mechanism, not a proven cause; what-fixes-it restates it. Honest; the
prose does not assert a proven token-level mechanism.

Distinctness from the hallucination lesson (the round's load-bearing question):
the base mechanism is two sentences and a link; the lesson spends itself on
repeatability and the supply-chain risk. No re-teaching of "why models invent
things." Holds.

Citations: opened all nine hrefs as the article prints them. Every link lands on
the source itself. The three 2026/earlier arXiv papers (s2 2406.10279, s3
2605.17062, s8 2606.13918) all resolve to real papers whose titles and figures
match what is cited. The GitHub repo (s7) confirms the withheld-list claim. The
four internal lesson links (hallucination, tool-use, retrieval,
sampling-temperature) all resolve to published library files.

Display-title checks against the live pages turned up three source-entry labels
that did not match the published titles; I fixed each (see Edits). One the writer
flagged (s9 Help Net) was in fact exact and needed no change. data-nb-kind labels
audited: the primaries are authors'-own or firms'-own documents; s4 is mixed
(Socket's own threat framing is primary, the coining attribution it reports is
secondary), but the coining line is double-cited with s5, so the label is
defensible. No kind change required.

## Cut

Ran the sentence-by-sentence slop pass, the edges-alone pass, the
arrived-from-a-link pass, and the delete test across body, display text, and the
table caption. Zero sentences required cutting. The edges that usually collect
slop carry real content: the section closers ("A lower rate with stable,
registrable names is still a fixed address an attacker can sit on"; "The
recurrence is the hinge") each state a claim the argument earned rather than
grading the piece. The negative-parallelism constructions ("not a lookup that
fetched the wrong entry"; "rather than spray fresh ones") each correct a
misconception the piece explicitly set up ("you would expect a fresh piece of
nonsense each time"), so they are earned, not reflex.

Punctuation: zero em-dashes. Two prose semicolons, both genuine balanced
contrasts (5.2% vs 21.7%; a one-off name vs a recurring one), not splices or
run-on patches — left in place.

Prompt-leakage and borrowed-phrasing passes: no instruction language, planning
labels, or assignment-fulfilled claims leaked into the body; the bookends' direct
address is the template's sanctioned exception. No distinctive clause is lifted
from the voice-guide exemplars (Evans, Luu, Cloudflare). The piece adopts the
directed moves — concrete named opening case, how/why-now separation, plain
marking of the limit of what is known — without borrowing their wording.

Formula pass against the recent library: the dek leads with "Because" and closes
with "so", breaking the recurring "X, and/because Y" comma mold and avoiding the
banned comma-triad. The closing body heading ("The fix is to let the assistant
check the registry") is a concrete fix statement, not the terse verdict-of-limits
stamp the brief warned against. The orientation heading ("The package it told you
to install was never published") is its own concrete step, distinct from the
headline. Headings skim-reconstruct the argument.

Furniture: one nb-table (rate by model group and year), which does real work
showing the spread beneath the 19.7% average — the point of the rate section; its
cells are all cited in nearby prose. No reflexive nb-note; none owed. The
repeatability figures stay in prose, which is correct: a stat strip of 58/43/39
would misread as a partition. No missed component.

## Reader

Read straight through as the paper's declared reader (smart, widely read, no time
in a codebase). What I have that the sources alone would not give me: a single
backward-working chain — predicted text, no lookup, the same name recurs, a
recurring name is a fixed address, a fixed address is registrable, so the attack
is possible though not yet seen, and the rate is falling while the predictable
names survive, therefore check before installing. No single source assembles that
chain; the draft-handoff's original-work sentence claims exactly this synthesis,
and it survives comparison with the article. The reader can now explain why an
assistant invents a library, why the same fake returns, and why repeatability
turns a nuisance into a guardable attack — the commission's contribution target.
The prose sits closer to the voice-guide exemplars than to a median summary:
concrete named case, terms defined in-line, sober sizing of the risk, explicit
settled/open marking, no hype or doom. The headline ("A coding assistant invents
the same fake package run after run") is the largest claim and the piece defends
it; the dek supplies the attack the headline leaves out.

## Edits

- s1 source title: "Can you trust AI package recommendations? (2024)" → "Diving Deeper into AI Package Hallucinations (2024)" (the live Lasso page's actual published title).
- s6 source title: "AI bots hallucinate software packages and devs download them (2024)" → "AI hallucinates software packages and devs download them (2024)" (removed "bots", which is not in the published Register headline).
- s4 source title: added the published "The Rise of" prefix, so it reads "The Rise of Slopsquatting: How AI Hallucinations Are Fueling a New Class of Supply Chain Attacks (2025)".

## Required work

None blocking. All three edits above are display-label corrections I made
directly from the live sources; no work is routed to researcher or writer.
Orchestrator: re-stamp and re-run the proof (including links) after these edits
before preparing the PR. The changes touch only source-entry display text — no
href, citation target, source count, or primary/secondary kind changed — so the
proof is expected to stay at BLOCK 0.

## Decision

approve — the argument holds claim by claim, the numbers match the evidence
exactly, the threat state and the settled/open lines are honest, the distinctness
from the hallucination lesson is clean, and the only defects found (three
source-title labels) are fixed in place.
