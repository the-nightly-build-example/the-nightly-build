# draft-handoff: the-mechanics/attribute-binding (writer 01)

## Original-work sentence

The article turns the evidence record's separate findings into one backward
causal chain, from the visible wrong-colored object to a single ground fact
(the model was never handed the sentence's structure), and it reads the two fix
papers against each other to separate what their combined evidence settles (the
fault sits in the text encoder and the cross-attention, because every working
fix reaches into one of those two parts) from what it leaves open (how the blame
divides), a weighing neither paper performs on its own.

## Proof result

`./nb check .nb-work/the-mechanics/attribute-binding/library/the-mechanics/attribute-binding.html --series the-mechanics --library <scratchpad>/library-checkout`
(links included, after `nb stamp`): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**

Stamped: words 1697 (band 1200-2200), sources 8 (7 primary, 1 secondary; floor
is >=8, >=4 primary, >=1 secondary), reading_minutes 7. Byline and nb-meta dek
match the rendered lines.

## Warnings intentionally left

None. The two W-SELF-COUNT notes cleared on `nb stamp`; two W-SENTENCE-DENSITY
notes were fixed by splitting the over-dense sentences (takeaway; the CLIP-gap
sentence in "Where the binding comes loose"). Final proof is clean.

## Source asset

Kept, not omitted. The evidence flagged Attend-and-Excite Figure 2 but read the
prompt from a rendered summary, so I confirmed it at capture time against the
paper PDF (page 2): the incorrect-attribute-binding column is the prompt
"A yellow bow and a brown bench" (right column; the left column is the
catastrophic-neglect example, which I cropped out as an untaught concept). The
crop keeps the exact prompt label, the baseline Stable Diffusion panels showing
the yellow bench, the corrected Attend-and-Excite panels, and the paper's
"Incorrect Attribute Binding" label; the row identities (baseline vs. corrected)
are carried in the caption. Captioned factually and cited to source 1 with
data-nb-locator="Fig. 2".

## Notes for the editor

- Per the brief's three evidence notes: no single-object-vs-two-object accuracy
  pair is asserted; the honest quantified stand-in is the full-prompt (~0.83)
  vs. worse-served-object (0.60-0.63, lifted to 0.69-0.72) CLIP gap, described as
  what it is. The "bag of concepts" reading is presented as the tidy first
  account and then complicated in front of the reader (Olah move): the larger
  fixable share sits at cross-attention (Attend-and-Excite, encoder untouched)
  while the encoder-side fix (StructureDiffusion) barely moves the numbers
  (19.2% -> 22.7%), and this is marked as competing-method evidence, not a
  controlled split. Settled part (systematic failure; cause in text conditioning
  + cross-attention; reproduces across DALL-E 2 and Stable Diffusion, different
  encoders) and open part (split of blame; fixability, with the 2025 survey's
  architectural steelman) are marked cleanly.
- Benchmark numbers used verbatim from the evidence Numbers section: color
  0.38 (0.3765) and spatial 0.12 (0.1246) B-VQA/UniDet scores on SD v1.4,
  described as 0-1 benchmark scores (not "a third of the time"); Conwell &
  Ullman ~22% of 1,350 DALL-E 2 images. No code.
- Prior lessons linked as plain prose links, not numbered sources: attention,
  clip, denoising-diffusion (also in the Background band, with
  counting-objects-in-images).
- Habits avoided: no colon-subtitle headline; opener is the plain base statement
  (Wolfram move), not a confident-wrong-output line; the "before it draws a
  pixel" framing is not used as a template; heading construction is varied
  (subject-verb / noun phrase / where-clause / how-clause), no comma-and mold;
  dek avoids the comma-and mold.
