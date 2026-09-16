# writer brief: the-mechanics/watermarks-in-generated-images (01)

Inputs:
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/editorial-direction.md` — house, slop, headline, press, template, series standards
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/researcher/01/evidence.md` — the complete claim set; draft only from this
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/commission.md` — the behavior, the backward chain, the two mechanisms
- `.nb-work/the-mechanics/watermarks-in-generated-images/library/the-mechanics/watermarks-in-generated-images.html` — the initialized lesson to edit in place
- `.nb-work/the-mechanics/watermarks-in-generated-images/.nb-context/` — effective template contract and furniture catalogs

Output: `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/the-mechanics/watermarks-in-generated-images/library/the-mechanics/watermarks-in-generated-images.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/d5bad8fd-c10f-5854-a93d-2fb67333d30d/scratchpad/library`
(iterate with `--no-check-links` added; final run links included, to `BLOCK: 0`.)

Confirmed Background links (both exist; link, do not re-teach): the letter-
rendering lesson `../the-mechanics/text-in-images.html` (why letters come out
wrong — a different question from why a watermark pattern is there at all) and the
general image-generation lesson `../the-mechanics/image-generation.html`.

Recent shapes to break (do not inherit): the desk has used a second-person
observation opener and a callback closing heading ("So look again ..."). Do not
copy either by reflex; vary heading construction.

This round's focus (all in the evidence record — honor its Contradictions):
keep the two mechanisms distinct — distributional learning of a pervasive mark
versus verbatim memorization of one image — and mark what is settled versus open.
The litigation exhibit the record analyzed is stronger evidence for the
distributional-learning mechanism than for the copying framing its own paragraph
implies; make that correction the way the record supports, keeping the litigant's
allegation attributed to the litigant. Watermark-prevalence figures come from the
dataset owner's blog (self-described as conservative undercounts), not the
peer-reviewed paper, and the dedup-versus-memorization figure was measured only on
a small dataset; state each with its exact scope and do not overreach. Fill
nb-meta dek to match the rendered dekline exactly, and set harness and writer
model (model: claude-sonnet-5).
