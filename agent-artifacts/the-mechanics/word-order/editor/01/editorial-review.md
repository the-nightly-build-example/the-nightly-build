# Editorial review: the-mechanics/word-order (editor/01)

## Skeptic

**Thesis.** A transformer respects word order even though the operation
underneath it cannot see order at all; position is supplied from outside by one
of several schemes, and the scheme most models now use (RoPE) fails not far past
the length it trained on, with no scheme settled as best. The draft states this
cleanly and the reader can recover it from the display text alone.

**Load-bearing claims, each tested against the owning primary:**

1. *Self-attention is order-blind / a transformer is invariant to input order.*
   Cited s1 (Dufter survey) and s2 (Vaswani). The survey states the invariance
   "by definition"; Vaswani states position must be injected "since our model
   contains no recurrence and no convolution." The draft scopes the blindness to
   "the bare operation" and does not overstate. Holds.

2. *The clean order-blindness claim has a causal-mask exception.* Cited s3
   (Haviv). Haviv: causal attention lets a token infer the number of predecessors,
   approximating absolute position. The draft says the mask "leaks a little order
   for free," calls the count "a weak signal," and links
   `the-mechanics/autoregressive-generation` rather than re-teaching the mask.
   This is exactly the first seam the brief flagged, handled without overstating.
   Holds.

3. *RoPE, though relative, does not extrapolate; it is engineered around.* Cited
   s9 (YaRN). Verified the YaRN abstract: RoPE models "fail to generalize past the
   sequence length they were trained on." The draft presents interpolation, NTK
   scaling, and YaRN as after-the-fact patches and reasons "if RoPE handled length
   on its own, none of them would need to exist." The dek was scoped to RoPE, not
   to "no scheme handles longer" (which would be false for ALiBi). This is the
   second seam; not overstated. Holds.

4. *ALiBi extrapolates, at the cost of locality.* Cited s10 (Press et al.). Train
   1024 → test past 2048, 11% faster; penalty grows with distance so far tokens
   are pushed toward irrelevance. Matches the evidence and the contradiction note.
   Holds.

5. *No scheme is settled best; a no-encoding decoder can win on small tasks.*
   Cited s11 (Kazemnejad) and s1. NoPE beat absolute, rotary, and ALiBi on small
   reasoning tasks; bounded to small models on algorithmic problems, which the
   draft states. Holds.

I pushed hardest on claim 3, the one the piece most wants, and could not retire
it: the primary (YaRN) says plainly that RoPE fails past trained length, and the
figure shows the rotary curve climbing. No sentence in the cited sources retires
the thesis.

**Numbers** all check against the evidence's exact figures: +1.3 BLEU En-De
(Shaw), 512-token ceiling (BERT), 1024→2048 and 11% faster (ALiBi), ~10x fewer
tokens (YaRN). Directional claims (relative > absolute on translation; rotary
perplexity rises past training length while ALiBi holds flat; NoPE > the three
explicit schemes) all match source direction.

**Display text, descriptor by descriptor.** Headline is a true claim the piece
defends. Dek makes a world-claim (not a grade of the article's method), scoped
correctly to RoPE. All four subheads are steps of the argument in the piece's own
nouns ("Attention sees a bag of words", "Position gets added to the vectors",
"From a word's slot to the gap between words", "Past the training length, the
schemes diverge") and a reader skimming only them can reconstruct the descent. No
named person carries a title/role/affiliation claim in display text; the body's
author names (Shaw, Su, Press, Devlin, Radford, Touvron, Kazemnejad, Haviv) match
the verified source pages.

**data-nb-kind audit.** s2–s8, s10, s11 are the papers that own their claims:
primary, correct. s1 (Dufter survey, authored none of the schemes): secondary,
correct. s9 (YaRN) is marked secondary — correct for its load-bearing use here,
which is reporting RoPE's failure from outside the RoPE authors; labeling it
secondary is the honest choice and does not hide a missing independent source
(the RoPE-fails claim genuinely needs an outside party, and YaRN is one). No
sourcing failures.

**Citation hrefs.** Opened all eleven source `href`s as printed plus the figure
locator (`arxiv.org/pdf/2108.12409#page=2`) and both Go-deeper links. Every one
resolves to the source itself. s4 (GPT-1) is the OpenAI-hosted PDF: it returns as
a real 528KB PDF at the printed address — the link lands on the owning document
(local PDF rendering was unavailable, and the evidence record already confirmed
the "learned position embeddings instead of the sinusoidal version" quote). No
broken or redirected links.

**Continuity (the check the brief reserved for me).** The published sibling
`the-mechanics/attention` carries the order-blindness demo under "Reorder the
tokens and nothing moves but the labels." This lesson does not present that demo
as a fresh discovery: it links `attention` in the Background band (row 01) *and*
inline in the orientation section ("an earlier lesson worked through its
arithmetic"), uses a compressed scrambled-sentence pass only as the premise, and
spends the body on the genuinely unwritten material — the positional-encoding
family and the open length-extrapolation question. The voice guide explicitly
asks for one concrete pass through the operation, so keeping the demo is correct.
The Background link the brief made a hard requirement is present. Satisfied.

## Cut

I read every sentence, including display text and the figure caption, against
`spec/slop.md`. The draft is clean; the failures were few and local, all cut
directly rather than routed:

- **Self-reference / windup (3).** "That is worth stopping on, because…" is the
  exact pre-twist windup the voice guide (Ciechanowski) says to drop; cut, leaving
  the plain statement. "The rest of this lesson is how." narrates the article
  ("what follows"); cut, and the section heading carries the transition. "and the
  sources are firm on it" reassures about sourcing that the inline citation already
  supplies; cut.
- **Announced stakes / brief-vocabulary leak (1).** "and this is the seam where
  settled engineering runs into an open problem" announces significance before the
  next sentence earns it, and imports the brief's own framing word "seam." Cut;
  "It does." answers the rhetorical question and the RoPE sentence delivers the
  content. The settled/open marking the series requires survives in the section's
  closing "floor of the descent" line and in the takeaway.
- **Self-grading (1).** "narrower and more interesting" tells the reader the
  finding is interesting instead of showing it; cut "and more interesting."

**Delete test / signposts.** The Why-card forecast ("This lesson follows the gap
between the two. First… Then… And last…") is the template's mandated "what you
will understand by the end," rendered in this lesson's own particulars
(order-blindness → position added → length failure), so it fails the slop test's
portability check and stays. The "floor of the descent" line fulfills the series'
"keep going down until the reader hits ground" instruction and carries real
content (builders are still guessing), so it stays.

**Punctuation.** Two reflex semicolons repaired to periods per the editorial
direction: "Nothing is learned; the pattern…" and the figure caption "…what the
model trained on; ALiBi's…". No em-dashes in the piece; the surviving colons
(list/payoff introductions) are correct uses. No comma splices found.

**Prompt leakage.** Compared authored text to the writer brief. The only genuine
import was "seam," now cut. "Descent" is the writer's own metaphor (not an
instruction label); "settled"/"open" read as subject vocabulary, not planning
labels.

**Formula / recent-pattern comparison.** Checked against the desk's recent record.
Opener does *not* use "Every [behavior] you have seen…"; the Why card does *not*
close on "By the end you can look at any…"; the takeaway does *not* close on "Now
you know which one you are looking at" or "So when you meet X…"; no "None of this
makes X worthless/fake" echo; the note label ("Same blend, either order") names
its move rather than defaulting to "In plain language"; headings are varied and
avoid the comma-and join that recurs elsewhere on the shelf. One watch-item, not a
block: the dek's "X, and Y" compound shares its shape with why-replies-stop's dek.
It is a plain compound, not the banned comma-triad, and passes the dek test, so I
did not route a rewrite — flagged for the desk to vary next run.

**Density warnings.** Both intentional `W-SENTENCE-DENSITY` sentences kept. The
takeaway's arc enumeration shows the whole progression at a glance and is a long
sentence under control; the NoPE appositive ("leaning entirely on the order the
causal mask leaks") explains the mechanism inside the clause it modifies. Editorial
permits both.

## Reader

Read straight through as the paper's declared reader — smart, widely read, no
codebase. What I have that the sources alone would not give me: the two claims the
literature keeps tangled — *position is supplied* (settled) and *any length is
handled* (open) — pulled apart and walked down one descent across the whole scheme
family, ending on the honest floor that no scheme is settled best. That matches
the draft-handoff's original-work sentence, and no single cited source draws that
line; the article does. Both answers survive, so the piece is not a restatement of
its sources.

The prose sits closer to the voice-guide exemplars than to a median summary: the
naive setup stated then denied before the fix arrives (Ciechanowski), the
side-by-side scrambled pair doing the explaining in the note (Evans), and
uncertainty scoped to one plain claim in "the people building the systems are
still guessing here too" (Luu). The headline, reread as the largest claim, is one
the body earns.

## Edits

- Cut "That is worth stopping on, because" from the Why card; plain statement now
  stands on its own.
- Cut "and the sources are firm on it" from the orientation caveat.
- Cut the signpost sentence "The rest of this lesson is how."
- Changed "Nothing is learned; the pattern…" semicolon to a period.
- Cut "and this is the seam where settled engineering runs into an open problem";
  "It does." now answers the question directly.
- Changed the figure caption's "…what the model trained on; ALiBi's…" semicolon to
  a period.
- Cut "and more interesting" from the takeaway ("the honest picture is narrower").
- Ran `./nb stamp`: words 1896 → 1860, reading 8 min, sources 11.

## Required work

None. No researcher gap and no writer prose/structure/markup/asset work remains;
the asset crop and caption are correct and the continuity link is present. The
writer still runs the full proof.

## Decision

approve — every load-bearing claim held against its primary, all citations resolve
and are correctly kinded, display text and the two evidence seams are accurate, and
the local slop and punctuation faults were cut directly.
