# Voice guide: the-mechanics/prefill-and-decode

## Directive

Register stays the house default: a serious paper, plain claims, concrete
stakes, no fuss. Reader relationship: the reader has felt the exact thing
this lesson explains — they sent a message, waited, then watched the answer
arrive word by word — so address that felt sequence directly and use it as
the argument's spine, not as a color opener to leave behind. Two moves
change sentences here specifically:

1. **Ground each named part in the timing before naming it.** Don't write
   "prefill is compute-bound" and then reach for an example. Write the wait,
   then say what fills it; write the word-by-word arrival, then say what
   produces it. The mechanism earns its name by explaining a duration the
   reader already sat through.
2. **Mark variance by naming its actual cause, not by hedging in general.**
   When a number could be challenged (how long the pause lasts, how fast the
   stream runs), the sentence names what it depends on — prompt length,
   hardware, batch size — rather than softening with "roughly" or "it
   depends" alone. A cause named is a claim. A hedge with no cause is fog.

Spend the piece's one earned contrast (`spec/editorial.md`'s ceiling of one
or two) on the actual inversion this mechanism produces: a long prompt,
which took real effort to type, is the cheap part; a short reply, generated
one word at a time, is the slow and expensive part. That reversal is the
lesson's real news. Don't spend the ceiling on a lesser contrast and don't
take two.

## Licenses

```text
form: threshold sentence
move: kipply ("Transformer Inference Arithmetic") names the exact point
      where one computational regime flips to another as a discovered fact,
      not a formula: "if we're going to compute kv for one token, it'll
      take the same amount of time to compute for up to 208 tokens!
      Anything below, we're memory bandwidth bound. Above, flops bound."
      The number is hardware-specific; the move worth taking is stating a
      real flip point plainly, as a thing that is true, not as an aside.
bar:  the sentence names a real, source-backed threshold behavior (e.g.,
      decode cost scales with output length, not prompt length) without
      hanging it on a specific throughput or hardware figure this piece
      cannot defend. It fails if it borrows kipply's number or invents
      one of its own to sound precise.
```

```text
form: named-cause variance
move: Dan Luu ("Computer latency: 1977-2017") rounds every measurement
      and says why: "Results in the tables are results of multiple runs
      and are rounded to the nearest 10 ms to avoid the impression of
      false precision." He also names, per device, exactly what makes a
      number uncertain ("The number of transistors for some modern
      machines is a rough estimate because exact numbers aren't public").
bar:  a variance claim in this lesson names the specific thing that
      varies it (batch size, hardware generation, prompt length) rather
      than a bare "it depends" or a smoothed-over average. It fails if it
      states a precise figure with no named cause for its range, or hedges
      with no content at all.
```

```text
form: familiar-to-mechanism ladder
move: Simon Willison ("Catching up on the weird world of LLMs") never
      opens on the abstraction. He starts at a phone keyboard suggesting
      "breakfast" after "I enjoy eating," then scales the same mechanism
      up in visible steps to the full model. The abstraction arrives only
      once its familiar seed is on the page.
bar:  a paragraph introducing prefill, decode, or the cache opens on the
      reader's own observed timing or an ordinary comparison already in
      the lesson (not a fresh unrelated analogy), and only then names the
      mechanism. It fails if the technical term appears before the
      concrete seed, or if the seed is decorative rather than the actual
      hook the definition hangs on.
```

An empty license keeps the house default. No form here licenses direct
reader address beyond what the commission's own opening already uses
("you send a long message"); that voice is inherited from the assignment,
not newly licensed, and stays within the house ban on gesturing at a
hypothetical reader ("a reader will notice").

## Recently used, do not reuse

This series has run the "A model that X never Y" and "The instant a model
writes a token" declarative-mechanism headline three times running
(tool-use, losing-the-thread, autoregressive-generation). This lesson's
headline names the prefill/decode split or the pause-then-stream itself,
in a different frame entirely — not a fourth declarative-mechanism sentence
with different nouns slotted in.

Comma-triad and semicolon-reversal deks are also spent. The dek here should
carry the one detail that makes this lesson unmistakable (the cache, the
memory-bandwidth bound, or the cost asymmetry) as a single plain claim, not
three clauses chained with commas or a semicolon splitting two halves
against each other.

The felt pause-then-stream is the honest way into this piece. It is not
overused; it is the actual subject. Let it open the lesson directly rather
than routing around it for a fresher-sounding opener.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

Craft:
- cadence: builds incrementally, one measured claim at a time, then breaks
  for a short colloquial aside ("It's a bit absurd that a modern gaming
  machine running at 4,000x the speed of an Apple 2...") before returning
  to evidence.
- argument: the felt complaint ("this feels slow") is bracketed with
  distrust of unaided perception, then re-earned through direct
  measurement rather than survey or anecdote.
- evidence: a high-speed camera and a table of real devices, sorted by
  latency rather than by year, so the pattern (older often faster) has to
  be noticed rather than announced.
- stance: skeptical of easy causal stories ("if we'd pick one root cause,
  we might say it's 'complexity'") and willing to complicate its own
  thesis once the neat version threatens to oversimplify.
- notice: catches the reader's likely assumption (newer means faster) and
  times its correction for right after the table, not before it.
- diction: plain and exact — "handoffs across process boundaries" sits next
  to "the latency dark ages" without friction.
- reader: intelligent and willing to check the claim itself: "One easy way
  to see that this is false is to go into your terminal and try
  `sleep 0; echo 'pong'`."
- expectation-inversion: the piece orders its evidence so the reader
  discovers the counter-intuitive pattern from the sorted table before the
  writer states it in words. The surprise is structural, not announced.

## kipply, "Transformer Inference Arithmetic"

Source: https://kipp.ly/transformer-inference-arithmetic/

Craft:
- cadence: alternates dense technical statements with plain asides ("Oh no!
  This doesn't fit in one GPU!"), which keeps a long derivation from
  reading as one unbroken slab.
- argument: builds the compute/memory distinction from a single ratio
  worked out on the page, then states what falls on each side of it, so
  the conclusion is a consequence the reader watched arrive.
- evidence: concrete hardware numbers (flops/sec, bytes/sec) carried
  through to a real model size, then checked against a published benchmark
  at the end rather than left as pure theory.
- stance: confident about the arithmetic, candid about what it leaves out:
  "doesn't factor in softmaxes, assumes zero comms latency and ignores
  many other smaller factors."
- notice: catches the moment a formula becomes an insight and marks it
  with a beat of genuine surprise rather than gliding past it.
- diction: technical terms are used, not decorated; a coined phrase
  ("math bandwidth") is flagged as informal ("really cute") rather than
  presented as settled vocabulary.
- reader: assumed to be following the reasoning step by step, not skimming
  for a conclusion — the piece narrates its own derivation in progress
  ("Now we'll build it into equations").
- threshold-as-payoff: the regime-flip point is delivered as a discovery
  the math just produced, exclamation and all, rather than as a fact
  handed down. The payoff is earned by the derivation immediately before it.

## Simon Willison, "Catching up on the weird world of LLMs"

Source: https://simonwillison.net/2023/Aug/3/weird-world-of-llms/

Craft:
- cadence: short, satisfied sentences at the moment a capability lands
  ("It's a really bad poem. My laptop just wrote a poem!"), longer
  explanatory sentences when precision is the point.
- argument: scales one mechanism up in visible steps — phone autocomplete,
  then a function completing text, then a model writing a poem, then
  billions of parameters — so the abstraction is never asked to stand on
  its own.
- evidence: a real file on disk (`ggml-vicuna-7b-1.1-q4_2.bin`, 4.21GB)
  and a real autocomplete suggestion, not a hypothetical instance.
- stance: direct about the limits of anyone's understanding — "capabilities
  of these models emerge at certain sizes and nobody knows why" — without
  letting that gap excuse vagueness about what is known.
- notice: catches the reader's likely mental model (a smart program) and
  corrects it with an image (a giant blob of numbers) rather than a
  denial.
- diction: colloquial and technical terms sit in the same sentence without
  either one apologizing for the other.
- reader: treated as capable of following the mechanism, not talked down
  to and not assumed to already know it.
- familiar-to-mechanism ladder: the axes above cover tone and evidence, but
  the load-bearing move is sequencing — every abstract term is preceded by
  the ordinary thing it generalizes, in the same paragraph, so the reader
  meets the concrete case first every time.
