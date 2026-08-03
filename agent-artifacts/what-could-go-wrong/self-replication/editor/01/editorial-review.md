# Editorial review: what-could-go-wrong/self-replication (editor/01)

## Skeptic

Thesis: the headline self-replication numbers each measure a different, mostly
hand-held task, so none of them measures the framework capability — an unaided
loop of acquiring compute and money, seizing machines, evading an operator, and
sustaining copies at scale — and both the alarm and the dismissal read the gap
in their own favor.

The claims it stands on:

1. The four labs defined ARA the same way, as an unaided loop. Checked against
   the OpenAI PF v2 quote (s2), the DeepMind FSF v1.0 "hardware it rents" framing
   (s3), and the article's own gloss. Holds. The verbatim note block quotes
   OpenAI's definition exactly.
2. The strongest alarmist result is narrow. The Fudan setup — weights,
   `start.py`, and `deploy_api_server_llama31_70b.py` pre-placed in the working
   directory, a second LAN machine provided, a direct "replicate yourself"
   order — is reported accurately against evidence and the primary (s4), and the
   four missing ARA elements (rent, account, money, operator) are named. The
   outside review (s10, correctly labeled secondary) corroborates "rather
   trivial." Holds.
3. No public eval measures the end-to-end loop. Stated as the spine in the final
   body paragraph and the takeaway. Holds; the evidence record agrees no public
   eval builds that situation.
4. The labs demoted ARA without clearing it. Each move is attributed to its own
   document: OpenAI → Research Category (s2), Anthropic → non-triggering
   checkpoint with the automated-R&D trigger quantified (s11), DeepMind → Autonomy
   domain removed into misalignment (s12). Not blurred. Holds.

The one I pushed hardest to break — the load-bearing "every number carries its
harness condition" — held for OpenAI (0/100, tools supplied, end-to-end),
Fudan (90%/50%, weights pre-placed), AISI (20–40%, tools/retries/elicitation),
Apollo ("heavily nudged," server and shutdown written in), and Shanghai
(realistic cluster, 21 models). It broke on **one number**: the METR o1-preview
~35 min. The sentence attributes a "bare harness of a shell, Python, and a
submit-answer tool" to both GPT-4o and o1-preview, but METR's o1-preview report
(s9, in evidence) invested most of its scaffolding effort in a heavier "advisor"
architecture. That is exactly the dimension this piece polices, and the error
runs in the costly direction — it understates the help and makes the model look
more capable under less scaffolding than it actually got. Routed to the writer.

Display text verified descriptor by descriptor. Headline states the finding
with actors, no colon tell, no triad, no question. Dek adds the two concrete
specifics (0/100, the pre-placed folder) without restating the headline and
avoids the banned molds. Model names, affiliations (Alibaba/Qwen, Meta/Llama,
Fudan, Shanghai AI Laboratory), trial counts (9/10, 5/10, 100 trials), and the
>85% Apollo figure all match their owning primaries. Every `data-nb-kind` is
correct: the twelve framework/eval/paper sources are primary, and only the
LessWrong review is secondary. The four headline figures are never stacked —
the "these figures cannot be stacked" sentence and the table caption both make
the different-tasks point explicit.

## Cut

One direct cut. The steelman section closed with "At face value, ARA had moved
into the present tense, **and the rest of this lesson is what 'at face value'
leaves out.**" The trailing clause narrates the lesson's own structure (the
"what follows" self-reference the standard bans) and undercuts the steelman
inside its own section, which the voice guide reserves for the later evidence
section. Removing it ends the alarm at full strength on "ARA had moved into the
present tense" — a cleaner, undercut-free steelman close.

No prompt leakage: the spine language ("acquire compute and money, evade an
operator") is reported fact, not lifted instruction; the Why-this-matters
"you will learn" lines are the template's licensed bookend function, not a
claim the assignment was fulfilled. The recent-pattern deks and the agent-noun
opener are both absent. Paragraph endings do not settle into a formula; the
recurring real-vs-labeled contrast is the argument itself, worded differently
each time, not a stamped shape. Furniture earns its place: the definition note
anchors the threshold in a lab's own words, the table is the load-bearing
anti-stacking act, and the chart shows the agree/know-how/finish gap the prose
argues.

## Reader

What the piece gives beyond its sources: every headline number set beside the
exact harness condition that produced it in one frame, then the demotion story
attributed document by document, then the Shanghai reframing that success rate
is a poor proxy for risk (100% replication, 100% vs 0% overuse). That is the
draft-handoff's stated original act, and it survives the read — a reader who
opened only the primaries would not have them reconciled this way. The prose
sits closer to the voice-guide exemplars (Saad's discipline of pairing each
result with its scope condition in the same sentence) than to a median summary.

## Inspect visual evidence

Chart `chart-1.png`, provenance `chart-1.py`. The committed script cites Fudan
Fig. 4 and encodes Qwen [100, 100, 90] and Llama [100, 70, 50] — matching the
evidence record exactly (agree 10/10 both; know-how 10/10 Qwen, 7/10 Llama;
live copy 9/10 and 5/10) and the primary. Read as a reader: grouped bars, legend
present, y-axis "Percentage of 10 trials" on a full 0–100 scale, no truncation,
labels honest. The image is sound and needs no correction.

One caption-precision note (caption is a factual label; not editable by me).
The figcaption says the models "agree and know how far more often than they
finish." True for Llama (100 → 50), but for Qwen the finish rate is 90% against
100% agree, so "far more often" overstates that gap. Routed to the writer as a
minor tightening.

## Edits

- Cut the self-referential signpost clause "and the rest of this lesson is what
  'at face value' leaves out" from the close of "When one deletion is no longer
  enough."
- Ran `./nb stamp` after the cut: words=2187, reading_minutes=10, sources=13.

## Required work

- **writer** — The METR o1-preview ~35 min figure is attributed to the "bare
  harness" alongside GPT-4o, but METR's o1-preview report (s9) used a heavier
  "advisor" scaffold. Correct the harness clause so this number carries its true
  condition; the evidence record holds the advisor detail, and the fix sharpens
  the dismissive point rather than weakening it. This is the piece's load-bearing
  dimension, so it blocks.
- **writer / orchestrator** — Byline reads "8 min read"; stamped reading_minutes
  is 10 (words 2187). Reset the byline to match before PR. Per the brief the
  orchestrator sets the byline last, after the count settles.
- **writer** (minor) — Figcaption "far more often than they finish" overstates
  the Qwen gap (90% finish vs 100% agree); tighten to fit both models.

## Decision

revise — the chart, sourcing, dual-use neutrality, and anti-stacking spine all
hold, but one capability number (METR o1-preview) carries the wrong harness
condition on the exact dimension this piece polices, and the byline/reading
mismatch must be corrected before publication.
