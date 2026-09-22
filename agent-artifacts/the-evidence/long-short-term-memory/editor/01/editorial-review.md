# Editorial review: the-evidence/long-short-term-memory (editor/01)

## Correct

Thesis, stated from the draft alone: a citation of "LSTM" quietly merges two
different machines, and the 1997 paper contains only the smaller one. The claims
under it: (1) plain recurrent networks cannot learn long-range dependencies
because the backpropagated error vanishes or explodes with the time lag; (2) the
1997 paper's fix is a memory cell built on a weight-1.0 self-loop and two
gates, and within its scope that was a strong, genuinely new result; (3) the
evidence for it was small and synthetic by deliberate choice; (4) the speech and
translation the name now carries came later, on a three-gate cell the 1997 paper
never described. All four are stated cleanly in the draft.

I tried to break each against the sources and the record, hardest on the one the
piece most wants to keep, that the 1997 result was strong. It held. The record
and the paper's own experiment sections show LSTM solved >1,000-step tasks that
BPTT and RTRL could not solve at all; the piece credits that plainly and never
implies the paper was weak or flimsy. The "never measured the thing it is famous
for" mold is absent, correctly, because the paper did demonstrate what it is
famous for at small scale. The honest tension (small evidence, load-free
reputation) is intact.

Corrections audited against the primaries:

- Forget gate. I confirmed firsthand in the 1997 PDF that the word "forget"
  occurs zero times and the architecture defines only input and output gates.
  The draft attributes the forget gate to Gers, Schmidhuber and Cummins 2000,
  cites it to the xLSTM paper (s3, "the forget gate has been introduced by
  Gers"), and does not quote the paywalled 2000 paper or list it as a source.
  Correct and within the record.
- 2013 speech. Authorship in prose and in the source list is Graves, Mohamed and
  Hinton (Toronto), Schmidhuber not an author. The 2005 result is correctly
  Graves and Schmidhuber. Both hold.
- Figures. I recomputed each against the record and, where possible, the PDF.
  Page range 1735-1780 is 46 pages ("forty-six" correct). Two to four memory
  cells, weights spanning the table's 93 (adding) through 6,064 (Task 2c), the
  ~10,504-weight largest network (Exp. 2a), the >1,000-step / 1,000-distractor /
  ~6,000-weight / ~49,000-sequence Task 2c row, ~12 synthetic task variants:
  all match. Later figures (69.8%, 17.7%, 34.8 vs 33.3 BLEU, 384M params / 4
  layers of 1,000 cells, 2.7B params on 300B tokens) match the record.

Every citation href resolves to its source. I opened the 1997 PDF directly: the
Fig. 1 locator is the one place the article and the evidence record disagree, and
here the article is right. The record's source note places the Figure 1 caption
on p.9; in the actual PDF the memory-cell caption ("Figure 1: Architecture of
memory cell") is on page 7 and Figure 2 is on page 9. The article's
`data-nb-url` anchor `#page=7` and locator "Fig. 1 &middot; p. 7" land on the
figure. No change; the record's p.9 note is the error. The table caption's
`#page=9` lands at the start of Section 5 (Experiments), where its "Sec. 5,
Tables 1-9" locator points; the tables themselves run pp.12-20, so the anchor
sits at the section head rather than the first table, which is acceptable for a
section-level locator.

`data-nb-kind` audited: s1, s2, s3, s5, s6, s7, s8 are the documents that own
their claims (primary); s4 (Olah) is a third-party explainer used only for what
"LSTM" has come to mean (secondary). Eight sources, seven primary, one
secondary, clearing the series minimum. No website is dressed up as an
independent author.

Teaching order holds: the vanishing gradient is taught in its own section before
the memory cell uses it; backpropagation and gradient descent are plain prose
links, not re-taught; seq2seq and word embeddings are linked where the present
section leans on them.

## Reads well

Two edge sentences went.

The orientation paragraph ended "There is no speech, no text, and no recording
anywhere in it, and the name would later be attached to all three." That is a
tricolon carried by rhythm, and the third item overreaches: the article shows the
name attached to two domains, speech (2005, 2013) and text/translation (2014),
and "recording" is only the medium of speech. Cut to "no speech and no text...
attached to both," which is what the piece actually demonstrates.

The memory-cell section ended "That absence matters for what came later." It
states nothing checkable and only signposts across two sections to the forget
gate. Deleted, not repaired; the paragraph now closes on the concrete "The word
'forget' does not appear anywhere in the paper," which is the stronger line.

I did not find borrowed phrasing from the briefing files or the voice-guide
exemplars. The description of the problem as connecting events "far apart in a
sequence" is the standard technical framing of the vanishing gradient, not a
lifted clause. The bookends address the reader in the template's allowed register
and each sentence belongs to this lesson's particulars. Against the recent-record
notes, the dek is a single declarative sentence with no number, no semicolon
reversal and no comma triad; the headings are built differently from one another
with no "clause, and clause" pattern; the headline's surprise (a 1,000-step
result on a few-thousand-weight network) is this lesson's own, not an echo of the
desk's single-hard-number openers.

Nothing read flat enough to need lifting toward the guide.

## The experience

Three furniture components, all earning their place. The captured Figure 1 shows
the whole 1997 mechanism at a glance: the central cell with its 1.0 self-loop,
the g and h squashing units, and the two gates, with no forget gate. I looked at
the crop and it matches the caption and prose. Its alt text had claimed "three
gate-like units in total and no fourth gate," which miscounts and muddies the
two-gate point; I rewrote the closing line to "The cell has these two gates and
no forget gate," which is what the image shows. The experiments table gives the
scale faster than prose and matches the record. The 1997-to-2024 timeline carries
the arc and every entry checks out.

One interpretation error in a component sat against the article's own thesis: the
2014 interlude called the seq2seq model "the same cell" as 1997. The piece argues
throughout that the later cell has a third gate the 1997 cell lacked, so "the
same cell" is wrong and undercuts the distinction. Changed to "a descendant of
that cell," which keeps the scale contrast (a few thousand weights against 384M
parameters) and states the relationship the record supports.

What the piece gives beyond its sources: it separates the two things "LSTM"
names, the compact two-gate 1997 demonstration and the larger three-gate machine
later groups built and ran, and shows a reader which one any given claim rests
on. That is the draft-handoff's original-work sentence, and it survives the read.
The article is not a restatement of the sources; it does the sorting the sources
never did.

## Edits

- Orientation: cut the "no speech, no text, no recording... all three" tricolon to "no speech and no text... attached to both."
- Memory cell: deleted the empty closing sentence "That absence matters for what came later."
- Scale: changed the weight floor from "a few hundred to a few thousand weights" to "under a hundred to a few thousand weights," to match the table's 93.
- 2014 interlude: changed "the same cell" to "a descendant of that cell," to stop the component contradicting the article's two-gate/three-gate distinction.
- Figure 1 alt text: replaced "There are three gate-like units in total and no fourth gate" with "The cell has these two gates and no forget gate."
- Ran nb stamp (words 2191) and the brief's nb check after the edits: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve — the argument is sound and correctly sourced; the corrections all hold, and everything I found was fixable from the record and this checkout without a new argument.
