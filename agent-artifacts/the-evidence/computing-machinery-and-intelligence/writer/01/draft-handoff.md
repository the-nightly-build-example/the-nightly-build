# Draft handoff: the-evidence/computing-machinery-and-intelligence (01)

## Original work

The evidence record gives Turing's forecast and Jones & Bergen's 2025 numbers
as separate facts; this draft does the arithmetic the evidence doesn't do
itself, flipping Turing's "no more than 70 percent chance of a right
identification" into its complement (the machine needed to fool the
interrogator at least 30 percent of the time to clear his bar), and uses that
flip to show that GPT-4.5 clears Turing's bar with no persona coaching at all
(36 percent, unprompted) while the 73 percent headline figure is a distinct
achievement that depends entirely on the persona script — a distinction no
single source in the record states.

## Proof result

`./nb stamp` then `./nb check --series the-evidence`, iterated with
`--no-check-links` and finished with `--check-links`: **BLOCK: 0** on every
run, verdict PUBLISHABLE. Final state: 1,908 words (band 1200-2200), 7
sources.

Two WARNs intentionally left, both because fixing them would require altering
quoted or titled primary-source text:

- `W-SENTENCE-DENSITY`, 78 words: this is Turing's own single-sentence
  forecast, quoted verbatim ("I believe that in about fifty years' time...
  after five minutes of questioning"). The voice guide asks for this exact
  sentence stated once, exactly as Turing states it; splitting or trimming it
  would misquote the primary.
- `W-BANNED-TERM`, 'machinery' (1 use, limit 0): the sole use is inside the
  paper's own title, "Computing Machinery and Intelligence," stated once when
  identifying the document per the series prompt. Renaming it would misstate
  the source's actual title.

All other WARNs from the first pass (six W-SENTENCE-DENSITY hits) were fixed
by splitting sentences, not by re-proving one at a time.

## Open questions

None. The evidence record settled every teaching point and both contradictions
the commission named (two-party vs. three-party, and what the test measures
per its own authors and per Hayes & Ford); no researcher or voice-guide gap
had to be routed back.
