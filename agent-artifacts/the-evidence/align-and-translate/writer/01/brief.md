# writer brief: the-evidence/align-and-translate (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — the governing standard, slop, headline, press-voice, template, and series rules.
- commission.md (../../commission.md) — the assignment, boundaries, the angle, and the post-research angle correction. Read the angle correction carefully.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — how this piece should sound; reread before drafting.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — the complete set of claims available to you. Use the Numbers section exactly.

Output:
- /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/agent-artifacts/the-evidence/align-and-translate/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/library/the-evidence/align-and-translate.html --series the-evidence --repo /home/user/the-nightly-build

The article file to edit is the one nb start-article created:
/home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/library/the-evidence/align-and-translate.html

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me (the
orchestrator) rather than inventing it or expanding the claim set.

## This round's focus

- Draft to the corrected angle in commission.md: the correction is about SCOPE,
  not vocabulary. The paper did name the mechanism "attention" (Sec 3.1) and did
  credit Graves 2013 (Sec 6.1). Do not claim the authors spoke only of
  alignment. The honest correction: it demonstrated soft attention/alignment
  only inside an RNN translator on one language pair, and did not propose the
  Transformer, self-attention, or LM pretraining.
- Honor the BLEU caveat: do not present Sutskever's 34.8 vs RNNsearch's 26.75 as
  a head-to-head loss for alignment (different protocols). The in-paper contrast
  is RNNsearch vs RNNencdec (Table 1) and the BLEU-vs-length figure (Fig. 2).
- State, in draft-handoff.md, the one sentence saying what this article does to
  the evidence that the evidence does not do itself, and make that work visible
  on the page.

## Do not echo the neighbouring published lesson

the-evidence/attention-is-all-you-need is already published with headline "The
paper credited with starting the LLM era never trained a language model" and
headings like "Eight authors, two language pairs, one new architecture" and
"Five mentions of 'language model,' zero about this one." Your piece is its
predecessor and sits right beside it. Build your headline, dek, and headings on
a different pattern. Do not use a "credited with X, never did Y" headline mold, a
"N authors, M language pairs" heading, or a "X mentions of Y, zero about Z"
heading. Link attention-is-all-you-need in Background and draw the line between
the two papers in the body.

## Recent shapes to break (the-evidence)

- Recent openers use "Every large language model ..." (elmo) and "You keep
  hearing ..." (deep-double-descent). Do not default to a second-person or
  "every X" opener; find this lesson's own way in.
- Recent openers close on "By the end you will know A, B, and C." Do not use
  that three-item cadence.
- Check your dek against recent the-evidence deks (elmo, deep-double-descent,
  mamba, llama-3) so it is not built to the same mold.

## Craft reminders from your skill

- Lesson form: Why this matters (bookend), body, The takeaway (bookend). Write
  the body first, both bookends after. Bookends address the reader and carry no
  citations; the body speaks to no one and never mentions the lesson.
- Teach a short list of ideas completely; each gets a plain statement, a worked
  example with real numbers or a real case, and why it matters here.
- Cite per-section (why and takeaway are cite-exempt). Number sources in
  first-citation order; carry each source's kind into data-nb-kind from the
  evidence record; prefer a real locator (data-nb-locator / data-nb-url) over a
  homepage link.
- Reach for a table or figure where it shows something faster than prose. The
  BLEU-vs-length figure (Fig. 2) and the alignment heatmap (Fig. 3) and the
  BLEU results (Table 1) are the candidates; use `nb asset` if you capture a
  source figure, or an nb-table for the BLEU numbers. Inspect any rendered
  image. Only use a chart/asset the evidence record supports.
- Fill nb-meta (dates, harness, writer model). Set harness to "Claude Code
  (nb-orchestrator edition)" and model to the model you are running as. Run
  `nb stamp` then the exact `nb check` above until BLOCK: 0. Run with
  --no-check-links while iterating; run the full check (links included) before
  handoff.
- Check the display text (headline, dek, subheads) against the evidence record
  and against spec/headlines.md and spec/slop.md before handoff. The nb-meta dek
  and the rendered dekline must be identical.

Write draft-handoff.md with the original-work sentence, the proof result (and
any warning you left on purpose with the reason), and any open evidence or voice
question. Report the handoff path and any warning left.
