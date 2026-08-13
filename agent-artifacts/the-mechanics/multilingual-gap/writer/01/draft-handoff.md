# Draft handoff: the-mechanics/multilingual-gap (writer 01)

## Original-work sentence

The article assembles the evidence record's separated figures into one ordered
diagnostic: it ranks the reproduced UDHR token series into a chart (English 33 to
Burmese 512 under cl100k_base) and sets the data-share numbers beside it so the
reader can predict which languages come out worst and tell a data-scarcity
explanation from a tokenizer one — and it foregrounds the raw-web-to-corpus jump
(about 41% English on Common Crawl up to GPT-3's 93%) as a finding in its own
right, a step the evidence notes but never builds into the argument.

## Proof result

`./nb check … --series the-mechanics --library /home/user/library-checkout`
(links included): `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE. All nine source
URLs resolve. `nb stamp`: words 1981, reading_minutes 9, sources 9.

No warnings left standing.

## How the round's requirements were met

- Data distribution leads (training-share section); the token tax is the
  secondary amplifier (token-tax section). The ordering is stated in the
  orientation ("the larger effect comes first") and enforced in the which-cause
  section via the French/Japanese case.
- All four caveats carried, marked settled vs open where the record marks them:
  (1) token disparity is not always a data-share artifact — Ahia's script/feature
  caution, in which-cause; (2) the benchmark is machine-translated, so part of the
  English-vs-other gap is translation quality — orientation, second paragraph;
  (3) the gap narrows but does not close — which-cause close, with the progress
  reading also given; (4) the premium is a property of the tokenizer's training,
  not the script — MuRIL at 1.21x Telugu, end of token-tax.
- Dated proxy handled honestly: 93% is attributed to GPT-3 (2020), flagged as a
  two-generations-old proxy no current model discloses, and paired with the
  current raw-web Common Crawl share. Tokenization is linked at first use
  (transformers-first-principles/tokenization.html), not re-taught, and is a prose
  link, not a numbered source.
- Habits avoided: Why-this-matters does not use the "By the end you will know X"
  formula; no "the thing that feels like X is not what happens" opener; the
  closing section is named for its content ("Nobody can yet split the blame…");
  the takeaway does not land on negative parallelism; the dek avoids the banned
  molds.

## Chart provenance

chart-1.py beside the article carries the full reproduced series and the method
(tiktoken 0.13.0, cl100k_base, UDHR Article 1 per language, unicode-org/udhr).
The 13-language series is used verbatim from the evidence Numbers block.

## Notes for the editor (no open questions)

- The secondary source (s9, ai-tldr.dev) is used for one sentence establishing the
  finding has reached practitioner material. Its 4-5-to-15-20 multipliers are
  presented as what the tutorial tells engineers, not as a sourced measurement,
  per the evidence's caution that they are general patterns.
- Common Crawl's 40.58% is given as "40.6%" in the sentence that states it and
  "41%" in the running comparison; both are within the record's "about 41%."
- No researcher request needed: every fact the argument rests on is in the
  evidence record.
