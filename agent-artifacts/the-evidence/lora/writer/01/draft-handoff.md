# Draft handoff: the-evidence/lora (01)

## Original-work sentence

The article sets the LoRA paper's own "matches full fine-tuning" result beside
the 2024 limitation study and the current Hugging Face adoption counts to show
that the parity is bounded to the constrained language benchmarks the paper ran,
and to mark the exact regime, continued pretraining on a large new domain like
code or math, where today's shorthand claims more than the paper ever showed.

## Proof result

`./nb check ... --series the-evidence --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** Stamped words=1947,
reading_minutes=8, sources=6. No warnings left standing. A preview build merging
the draft succeeded (190 articles), confirming the stat strip and comparison
table render.

Source floor met: 6 sources, 5 primary (LoRA, Aghajanyan, Biderman 2024, HF Hub
measurement, QLoRA) and 1 secondary (PEFT library), in first-citation order.

## Brief cautions honored

- The parity claim is presented with its scope throughout, not as a law; the
  honest tension (bounded result vs. Biderman 2024 on code/math) is the spine of
  the "Parity" section and the takeaway.
- Discarded figures avoided: no "97-99% of full FT on GLUE," no Gartner "85% by
  2027."
- Biderman 2024 is cited by its arXiv page and never called a TMLR paper (venue
  unconfirmed).
- parameter-count and gradient-descent are linked (Background band plus inline at
  first use), not re-taught; attention is linked inline rather than taught.

## Open questions

- Minor, editor's call: source 4 (the Hugging Face Hub-measurement blog) is
  titled descriptively as "PEFT beyond LoRA: Hub usage measurements (2026)"
  because the evidence record gave the URL and the counts but not the exact blog
  title. The URL is authoritative; the display title could be tightened to the
  real page title if the editor opens it.

No open evidence holes and no unresolved voice question: the evidence supported
the commissioned angle firsthand.
