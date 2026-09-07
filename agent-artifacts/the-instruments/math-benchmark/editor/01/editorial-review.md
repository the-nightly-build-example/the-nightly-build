# Editorial review: the-instruments/math-benchmark (editor/01)

## Skeptic

Thesis: a "MATH score" is nothing but a single boxed final answer string-matched
against a key, so the score never sees the reasoning; and because leading labs
now report "MATH-500" (500 problems, Pass@1) under the same name the 2021 paper
and Minerva used for the full 5,000, cross-model "MATH" numbers silently mix
problem sets and counting rules. The headline carries the sharpest owned claim:
OpenAI defined MATH-500 because 4,500 of the 5,000 test problems had gone into
its own training data.

Claims it stands on, and how each held:

1. The grader reads only the `\boxed{}` string and marks an exact match, so the
   reported score is a fraction of matched final answers, not solved problems. I
   opened the MATH paper (s1) full text: it parses the boxed content and compares
   it to the ground truth. Held.

2. The rise from 6.9% to 97.3% is not pure artifact. I checked the two facts the
   piece leans on. The MATH paper's three-time IMO gold medalist scored 90%
   (18/20), misses "exclusively due to small errors of arithmetic" — verified in
   s1. Minerva's move from string match to SymPy recovered only about a point —
   verified in s2 via the evidence record's Table 6 figures. The piece credits
   real capability rather than telling a one-directional inflation story, which
   is what this round required. Held.

3. Exact-match grading errs both ways: false negatives on formatting (1/√3 vs
   √3/3, SymPy recovered ~1%) and false positives on right-answer/wrong-reasoning
   (~8% average, ~30% at Level 5). Both directions are stated and both sit on
   Minerva (s2). Held.

4. The spine: MATH-500 exists because 4,500 of 5,000 test problems were folded
   into OpenAI's training set. I opened the primary (s5, "Let's Verify Step by
   Step") full text. It states: "In order to avoid the risk of over-fitting on
   the 7,500 MATH training problems, we expanded the training set to include
   4,500 MATH test split problems," and "We therefore evaluate our models only on
   the remaining 500 MATH test problems," selected "uniformly at random" and
   shown representative of the full set's difficulty/subject spread. The headline,
   the two-names section, and the takeaway all match this. Held, including the
   causal "because."

Directional and label checks against the owning primaries:

- The GPT-3 175B figure was mislabeled. The draft called the 175B 5.2% result
  "fine-tuned." The MATH paper (s1) reports 175B **few-shot** at 5.2%; the
  fine-tuned GPT-3 was the 13B model at 5.6%. A wrong method label on a figure,
  corrected directly to "few-shot" against the primary (see Edits). The claim it
  serves (a very large model still scored ~5%) is unchanged.
- The GPT-4 negative fact (s7): the GPT-4 Technical Report reports GSM8K and no
  MATH score, so any "GPT-4 on MATH" figure is unprovenanced. The abstract page
  cannot show Table 2, but this rests on the researcher's full-text read and is a
  well-established fact; the source is primary, is used for a real point, and
  earns its eighth-source place rather than padding.
- The o1 96.4% is correctly attributed as reported by DeepSeek ("the 96.4% it
  lists for OpenAI's o1"), matching the evidence record's ownership flag.
- The AIME 2024 10-20% contamination figure is correctly kept away from MATH; it
  appears nowhere in the piece, and MATH-specific contamination is carried by the
  PRM800K leakage and the Hugging Face DMCA takedown, exactly as the brief
  required.

Every citation href was opened as printed. All eight land on the correct source:
s1 MATH paper, s2 Minerva, s3 Qwen2.5-Math report, s4 DeepSeek-R1, s5 Let's
Verify Step by Step, s6 the Hugging Face card (banner confirms "disabled ... DMCA
Takedown notice"), s7 GPT-4 report, s8 Epoch (confirms "MATH Level 5, which is
now reaching saturation"). The two Go-deeper links resolve (hendrycks/math repo,
MathArena). `data-nb-kind` labels are right: seven primary, one secondary (Epoch,
an outside evaluator, correctly secondary). The source floor holds (8 total, 7
primary, 1 secondary).

One cross-reference was miscited. The inline definition "which is called
contamination" linked to the GSM8K lesson, which only uses the term. The
commission names livecodebench as where contamination is taught, and that lesson
defines it outright ("This is contamination"). Rerouted to livecodebench (see
Edits). The three Background link display texts each match their lesson's actual
headline.

## Cut

The prose is dense with load-bearing nouns and survives the slop test cleanly;
no sentence reduced to an interchangeable pattern. I walked the edges out of
order. The closers that use the "not X, it is Y" shape ("the score is not a count
of problems a model solved. It is a count of final answers that matched the key
...") each correct a misconception the piece actually names and each carry
specific consequences, so they are earned contrasts, not reflex parallelism. The
article's last sentence ("What it measured all along was whether a final boxed
answer matched a key, never whether the reasoning that reached it was sound")
states the conclusion the argument built, and stays.

No self-reference outside the two bookends: the body speaks to no one and never
names the lesson. The Why bookend's "about 97% ... up from under 7%" presents the
naive framing but immediately flags the catch ("why a 97% and a 6.9% score can
wear the same name and still not compare"), so it sets up rather than commits the
error the piece exposes. No prompt leakage: the brief's "denominators and
metrics" survives only as a reported fact about the world, not a lifted clause.

Recent-pattern checks: the dek does not open on a scare-quoted score; the piece
reuses none of "the grader is part of the number," "turns one X into two
measurements," or "A single <score> branded <model> <label>." Headings are the
piece's own nouns and vary in construction. No formula found. Zero sentences
required deletion for slop.

## Reader

Reading straight through as the paper's declared reader: I come away able to say
what a MATH score is (one boxed answer, string-matched), why two numbers both
called "MATH" may not compare (5,000 vs 500 problems; single attempt vs
majority-of-64 vs Pass@1), why MATH-500 exists at all (4,500 test problems went
into OpenAI's training data), and that the grader misjudges in both directions.
That is a synthesis no single source hands over — it takes reading five papers
and noticing the naming collision yourself. The original-work sentence's claim
holds: the piece takes a list of scores apart rather than restating any of them.
The prose sits closer to the voice-guide exemplars than a median summary: it
builds each number forward step by step, in Silver's manner, and lets the
distance between "what the score measures" and "what it is taken to measure"
carry the judgment rather than announcing it. The headline is a specific, sourced
claim with its actor named, and it survives as the largest claim in the piece.

## Edits

- Corrected "a fine-tuned GPT-3 with 175 billion parameters got 5.2%" to "a
  few-shot GPT-3 ...": the MATH paper (s1) reports the 175B 5.2% as few-shot; the
  fine-tuned GPT-3 was 13B at 5.6%.
- Rerouted the inline "contamination" definition link from
  ../the-instruments/gsm8k.html to ../the-instruments/livecodebench.html, the
  lesson that defines the term and that the commission names as its teaching
  home.

## Required work

None. Both defects were fixed directly; no evidence gap for the researcher and no
redraft or reporting for the writer. The orchestrator runs `nb stamp` and
`nb check`; the two edits touch prose and one href only and introduce no banned
terms or punctuation.

## Decision

approve — the spine, the both-directions grading, and the credited real capability
all hold against the owning primaries; the two defects found (a mislabeled method
and a miscited cross-reference) were corrected in place.
