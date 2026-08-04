# Voice guide: the-mechanics/retrieval (01)

## Directive

Write this as a descent, not a survey. The reader has seen the behavior and
holds a plausible wrong model of it ("the chatbot read my document and learned
it"). Each section takes one rung down from that behavior and answers the only
question the rung above leaves open: how does *that* step actually happen. The
reader is a curious peer being walked down a ladder, not a student being
lectured; you know where the ground is and you are showing the path to it.

Three moves will change sentences here, beyond the house's plain register:

- **Open at the behavior, then pull down.** A section earns its place by
  resolving something the previous one left dangling, not by introducing the
  next named part. The named part arrives because the behavior demanded it.
- **Thread one query, not a fresh toy per section.** Pick a single concrete
  query and a single retrieved passage early, and reuse them to carry every
  step: why this chunk is embedded near that query, why closeness ranks it
  first, why the model quotes it, and, at the failure, why the quote does not
  support the claim. Real tokens and a real number beat a new illustration each
  section.
- **Keep the real term; make the geometry physical.** "Embedding," "cosine
  closeness," "nearest neighbor," "top-k" all stay by name. Their meaning is
  carried by a spatial image of things landing near each other, never by a
  slogan that replaces the term.

Attribute the visible failure to one named step, plainly, without a drumroll.
The whole piece has been building the ladder that lets you point at the exact
rung; point, and stop.

## Licenses

form: second person, placing the reader at the behavior
move: Evans writes "you're waiting for cached records to expire" to stand the
      reader at the scene of the thing they misread. Use it only to name the
      shared observable behavior and the felt failure.
bar:  each "you" sits at something the reader has actually done or seen (uploaded
      the PDF, read the confident citation). Once inside the mechanism, drop to
      plain third person. A "you" that only softens a technical sentence is cut.

form: the earned misconception-correction
move: Evans names the wrong model ("propagation") before giving the right one
      ("caches expiring"). This article holds two real ones: frozen weights did
      not "learn" your document, and the paper that named RAG built a
      jointly-trained system, not the embed-search-stuff pipeline the term now
      denotes.
bar:  the wrong belief is one a smart reader genuinely holds, named in plain
      words before the correction. House ceiling of two in the piece. No
      invented "not X" strawman to knock down for momentum.

form: the flat admission that no one knows
move: Willison writes "Nobody fully understands what those individual numbers
      mean, but we know that their locations can be used to find out useful
      things." The series requires marking settled engineering against open
      questions; say the open part without hedging.
bar:  names the specific unsettled question (does the model use what it
      retrieved; which chunking is right) and what stays settled around it. The
      admission does not leak hedging into the settled steps. No "it's
      complicated" that names nothing.

## Recently used, do not reuse

- The stacked short subject-verb declarative heading, the desk's recent default
  ("The pause is the model reading your prompt," "The stream is slow because
  each word rereads the whole cache," "The transcript is the only memory a chat
  model has," "Running out of room is one real failure"). Vary shape and length
  across the heading set so a reader skimming only headings hears an argument,
  not a metronome. No two adjacent headings share the same mold.
- The "The X is the Y" identity heading specifically ("The pause is the model
  reading your prompt," "The transcript is the only memory a chat model has").
- The "X because Y" / "X is slow because Y" causal heading and the same shape in
  the dek.
- The "Where X ..." heading. Used two runs running ("Where to run the two phases
  is still unsettled," "Where the U-shape actually comes from"). Skip it even
  though your open-questions section wants exactly that slot.
- Dek molds: the house-banned three (semicolon reversal, suspended question,
  comma triad) plus the recently-run stat-contrast dek ("worse than the 56.1%
  it scored with no documents at all") and the "X because Y" causal dek.
- The neighbor lesson `losing-the-thread` owns the behavior "the right document
  is present and the model still fails" (its middle-goes-quiet / U-shape
  framing). You link it; do not reprise its behavior or its framing as your
  own. Your behavior is the confident citation to a passage that does not
  support the claim.

## Simon Willison, "Embeddings: What they are and why they matter"
Source: https://simonwillison.net/2023/Oct/23/embeddings/
Craft:
- cadence: short punchy claim ("Embeddings are a really neat trick") followed by
  a longer chain that unpacks it; paragraphs stay short, so the rhythm feels like
  unfolding rather than exposition.
- argument: works backward from a thing he built (related-content on his blog) to
  the mechanism underneath, so the abstraction is always answering a concrete
  "how did that happen."
- evidence: a real model named exactly (all-MiniLM-L6-v2), real output shown, real
  numbers; nothing gestured at.
- stance: confident on mechanism, unembarrassed about the parts nobody
  understands.
- notice: catches the exact place jargon intimidates and disarms it before
  proceeding.
- diction: conversational but precise; technical terms kept, not swapped for
  cutesy stand-ins. Warning for this house: his "vibes-based search" is too
  casual for the Yglesias register. Steal the physical image, not the slogan.
- reader: assumes intelligence, not embeddings knowledge; scaffolds without
  condescending.
- important move: renders invisible infrastructure as a visible ordered sequence,
  each stage named and connected to the next, so the pipeline becomes something
  the reader can trace with a finger.

## Jay Alammar, "The Illustrated Retrieval Transformer"
Source: https://jalammar.github.io/illustrated-retrieval-transformer/
Craft:
- cadence: short declaratives dominate ("The database is a key-value store,"
  "That vector is then used to query the database"); longer sentences reserved for
  topic sentences that introduce a new complication.
- argument: sequential decomposition. Embedding, nearest-neighbor lookup,
  generation are isolated as discrete steps, then shown connecting; each heading
  is a waypoint in the causal chain.
- evidence: a minimal concrete case (a Dune sentence) establishes *why* retrieval
  matters before the machinery arrives.
- stance: presents settled structure as observed fact; defers the parts he will
  not justify rather than bluffing them.
- notice: separates factual knowledge the model looks up from linguistic
  knowledge it already holds, the distinction this article's behavior turns on.
- diction: technical terms embedded in accessible phrasing; verbs stay active and
  visual ("breaks," "glance," "incorporate").
- reader: "you and I working through this together" without the collaboration
  becoming filler.
- important move: restraint. He does not trace one query through the entire
  system, which is exactly the move this article should make and he leaves on the
  table. Thread the single query he doesn't.

## Julia Evans, "DNS 'propagation' is actually caches expiring"
Source: https://jvns.ca/blog/2021/12/06/dns-doesn-t-propagate/
Craft:
- cadence: dramatic variation. Short declaratives ("DNS is pull, not push")
  against longer speculative stretches; the rhythm mirrors a mind working, not a
  document reciting.
- argument: names a widespread wrong model, then reveals the real mechanism and
  shows the wrong model was really a misleading word. The correction is the
  spine.
- evidence: her own domain, a real record, a real TTL number (3600), and the
  actual command output; the worked example is lived, not hypothetical.
- stance: corrects the reader's model while blaming the terminology, never the
  reader.
- notice: catches where a common term ("propagation") does the misleading, and
  fixes the word.
- diction: plain and friendly, occasional fragment for emphasis; playful edges
  ("very rudely, some resolvers will ignore your TTL") that this house should keep
  quieter but can learn the warmth from.
- reader: peers. Anticipates the objection the reader is about to raise and
  answers it in the next line.
- important move: marks her own uncertainty out loud ("I don't know exactly how
  long this takes or why") and it raises trust rather than lowering it. That is the
  model for this article's open-questions step.
