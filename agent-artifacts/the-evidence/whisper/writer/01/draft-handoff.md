# Draft handoff: the-evidence/whisper (01)

## Original-work sentence

The evidence records the robustness result and the hallucination failure as two
separate facts; this lesson shows they are one design property seen from two
sides. A decoder trained to always emit the next plausible token is what carries
Whisper across audio it never trained on, and it is the same decoder that writes
a plausible sentence into silence, so the average-WER robustness the paper proved
and the invented-span failure in deployment are the same mechanism measured
differently, against a per-record guarantee the paper never made.

## Proof result

`./nb stamp` then the full `./nb check ... --series the-evidence --library
/home/user/library-checkout` (links included): BLOCK 0, WARN 0, verdict
PUBLISHABLE. 1847 words, 8 min read, 6 sources (5 primary, 1 secondary; source
floor is 6 with >=3 primary and >=1 secondary). No warnings left standing.

Display-text self-test done: every date, number, name, and title in the
headline, dek, and subheads checked against the evidence record; nb-meta `dek` is
identical to the rendered dekline; `<title>`, `<h1>`, and nb-meta `title` all
match. nb-meta fields the engine cannot compute set by hand: date 2026-08-22,
harness `claude-code-routine`, model `claude-opus-4-8`.

## Decisions worth flagging to the editor

- Lead is robustness, not raw accuracy: orientation states the clean-benchmark
  tie (2.5; wav2vec 2.0 ties at 2.7) and defines robustness as the small
  clean-vs-messy gap. The gap section carries the earned "robustness is a smaller
  jump, not a lower score" contrast; I removed a second negative-parallelism
  ("not lowest error. It is robustness") from the orientation so the mold does
  not read as a house habit.
- No single figure is presented as *the* hallucination rate. Koenecke's 1.4% is
  scoped to short AphasiaBank clips and flagged as rising with non-vocal time and
  concentrated in the aphasia group; the AP field counts (8 of 10; ~half of 100+
  hours; nearly all of 26,000) are labeled uncontrolled practitioner tallies, not
  measured rates.
- The ~438,000-hour English figure (derived) is not used. I preferred printed
  figures: 680,000 total, 117,000 across 96 other languages, 125,000 translation,
  and "about 65 percent of the training computation went to English
  transcription" (Section 4.3) as the English anchor.
- WER is taught with the textbook worked example (6 subs + 3 ins + 1 del over a
  13-word reference = 76.9%, cited to Jurafsky & Martin); zero-shot is not
  re-taught, only linked to the-evidence/gpt-2 at first use with a one-line note
  on why zero-shot testing is fairer to Whisper and harder for the supervised
  baselines.
- Furniture: one block only, a two-condition comparison table built from the
  paper's Table 2 verified numbers (LibriSpeech-clean tie 2.7/2.7; average over
  13 other sets 29.3 vs 12.8; 55.2% relative reduction). I did not run `nb asset`
  on Figure 2: the table lets the reader test the same tie-vs-gap contrast from
  the evidence's verified numbers without capturing an image, and the brief
  said a small table is sufficient. Figure 2's diagonal/human point is described
  in prose instead.
- Dek breaks the "The [X] paper ..." mold (leads with 680,000 hours) and the
  orientation heading avoids the "What 'X' actually names" / "number on the
  model card" openers.

## Open questions

- Source titles for s5 (Koenecke et al.) and s6 (AP) are rendered descriptively,
  because the evidence record does not carry either document's exact printed
  title. If the editor wants the verbatim titles ("Careless Whisper ..." and the
  AP headline), that is a small evidence-lookup, not a claim change.
- The controlled hallucination denominator: the evidence abstract quote says
  "roughly 1%" while the Numbers block and the study's coded result give 1.4%. I
  used 1.4% (the study's own measured figure) and wrote "roughly 1.4 percent";
  flagging in case the editor prefers to mirror the abstract's "roughly 1%".
