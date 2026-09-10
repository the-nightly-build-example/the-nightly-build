# editor review brief: the-evidence/palm (editor/01)

Inputs:
  ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
  ../../commission.md — the document, angle, distinctness lines, reader
  ../../writer/01/brief.md — the exact writer brief (check for prompt leakage against it)
  ../../writing-coach/01/voice-guide.md — the register and the quoted exemplars to compare against
  ../../researcher/01/evidence.md — the claim set the draft must not exceed
  ../../writer/01/draft-handoff.md — the original-work sentence (open only at the third read)
  ../../../../library/the-evidence/palm.html — the article to edit in place
  ../../../../.nb-context/ — effective template contract and furniture catalogs

Recent-pattern notes (compare edges, dek, headings against these):
- The Evidence habitually leads the headline with a number and builds the dek as a
  concrete clause + comma + "and"/"while" twist. Break either if the draft slipped
  into it.
- Headings should be argument-step sentences in the piece's own nouns.

Round's focus:
- Verify the load-bearing comparison descriptor by descriptor: 540.35B params on
  780B tokens = 1.44 tokens/param, against Chinchilla's ~20 tokens/param (~11T for
  a ~520B model) => ~one-fourteenth. The whole thesis rests on these; recompute.
- Check the two honesty points against the primary: GSM8K 58% used an external
  calculator and plain chain-of-thought was 54% (below the 55% prior SOTA); the
  emergence/discontinuity claim is contested (Schaeffer "mirage"). Confirm the
  draft presents emergence as claim-then-challenge, not fact.
- The writer reports respecting the figure-read caveat (textual aggregates only,
  no per-task percentages, no Figure 5). Confirm no figure-read number slipped in.
- The two evidence-flagged quotes (PaLM 2 scaling line; Schaeffer abstract) should
  be paraphrased, not quoted; the unverified "NeurIPS 2023" venue omitted. Verify.
- Confirm "undertrained means inefficient, not weak" is earned and fair (PaLM beat
  the smaller Chinchilla by spending more compute; Chinchilla appeared ~a week
  before PaLM). Distinctness: chinchilla / scaling-laws-kaplan / MFU / react /
  emergent-abilities linked, not re-taught.
