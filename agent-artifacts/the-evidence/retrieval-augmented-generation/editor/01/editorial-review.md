# Editorial review: the-evidence/retrieval-augmented-generation (editor/01)

## Skeptic

The article's thesis is that "RAG" now names two systems: the 2020 Lewis et al.
research model that fine-tuned DPR's query encoder together with a BART
generator against a frozen document encoder and FAISS index, and today's "Naive
RAG" pipeline that fine-tunes neither piece. It stands on four claims: that
Lewis et al.'s joint training was narrower than the shorthand suggests (only
the query encoder and BART, per §2.4); that the paper's headline benchmark
wins were measured on that specific system; that the paper's Jeopardy
factuality result is a 452-item pairwise human eval against BART, not a
general hallucination rate; and that the primary studies on the modern
pipeline (Xu, Liu, Niu, Barnett) measure quantities the paper never measured
and do not translate back onto it.

Verifications against the primaries and the evidence record settled every
figure the argument spends. DPR indexed 21,015,324 Wikipedia passages
(Karpukhin §4.1); BART-large is 400M parameters (Lewis §2.3); RAG-Sequence NQ
44.5 vs T5-11B 34.5 gives the 8.0-point gap the article names; the Jeopardy
pairwise numbers (42.7% RAG better, 7.1% BART better, 452 pairs) match Lewis
§4.3; the index-hot-swap 70/4 and 68/12 match §4.5; Xu et al.'s Llama2-70B
seven-task averages match Table 2; RAGTruth's 450-instance rates and 43.1%
whole-corpus rate match Niu Tables 7 and 2; Barnett's 4,017-document /
15,000-document abstract-vs-case-study inconsistency is carried in prose per
the researcher's guidance.

Three findings needed action.

First, "Xu Peng and colleagues at NVIDIA" reversed the first author's name;
the arXiv record and paper metadata give "Peng Xu" as the first author (surname
Xu, given name Peng). Fixed in place.

Second, "Yuxin Niu and colleagues" named a person who is not RAGTruth's first
author. The ACL Anthology entry gives the first author as "Cheng Niu." A
misnamed author in display prose is a wrong label that reaches every reader.
Fixed in place.

Third, the Barnett paragraph closed with "None of the seven failure points
would have been resolved by the training loop the paper used, because none of
the seven exist in the paper's system. Its retriever and generator had been
fitted to each other." The claim overreaches. Several failure points (FP2
missed top-ranked, FP4 not extracted) could exist in the paper's system in
principle; the paper simply did not evaluate against Barnett's taxonomy. And
"retriever and generator had been fitted to each other" contradicts the
article's own earlier precision that only the query encoder — not the passage
encoder — was fine-tuned to the generator. Cut and replaced with a
narrower closer that stays inside what the evidence supports: the taxonomy was
cataloged on production pipelines that train neither piece, and Lewis et al.
never measured against it.

The Bai/Xu long-context disagreement carries through Xu et al.'s own
acknowledgment; the writer's option to leave Bai unsourced is honest given the
evidence record's Bai gap, and the article's phrasing does not overclaim.

Headline and dek verify as claims about the world, not method grades. Section
subheads each step the argument. All eight citation hrefs resolve to the
correct primaries; all eight data-nb-kind labels match the primary/secondary
test (Gao is the sole secondary, correctly labeled).

The TriviaQA column in the paper's Table 1 reproduction silently mixed splits:
RAG-Sequence 56.8 and DPR-extractive 57.9 are on TQA-open, but T5-11B+SSM's
60.5 is on TQA-Wiki (the split the paper uses for closed-book baselines, since
those models have no open-test number). The article's body prose is careful
(it names "on the open test" for the RAG-vs-DPR comparison and puts the T5
comparison on NQ only), but the table alone reads as if the numbers are
directly comparable. Fixed by extending the caption to name the split
difference.

## Cut

Deleted one signpost from the Orientation section: "Where the label held and
where it drifted is what the paper's own numbers are useful for." Fails the
slop test — reduces to "Where the X held and where it Y is what the Z's own
numbers are useful for" — and the section that follows walks into the paper's
numbers without needing the signpost.

Removed the closing Verdict block from the body. This is a press-level
requirement, not an editor preference: `press/editorial.md` says the takeaway
bookend is where a lesson lands its judgment and instructs "Do not close the
body with a Verdict note, or any block that restates the finding. Some older
articles still carry that block from the paper's earlier template. It is a
leftover, not a model to copy." The removed block also duplicated the takeaway
in shape and payload (both close on "when a modern claim about RAG…" tests).
Removing it lands the article's judgment in the takeaway alone, as the press
directs.

Ran the delete test on the remaining edges and did not cut further. "Both are
called RAG." reads short but is a specific transitional line the next section
picks up. "Change the index, change the answers." is a fragment carrying real
content, not decorative. The Why bookend's closer ("Reading the paper against
the primary studies on the shipping pipeline gives you the vocabulary")
addresses the reader (allowed on lesson bookends) and names what the reader
gets; it does not match the recent-pattern "By the end you will know what A,
B, C, and D" mold. The takeaway closer ("When a claim about 'RAG' reaches for
the paper's numbers, ask which of the two systems is really being described")
gives a concrete test the piece has earned; it does not match the "That is
real, and it is what X" formula the recent-pattern notes flag.

Voice: the prose sits close to the Lee/Raschka/Willison exemplars — figures
anchored to comparisons the reader already holds (400M generator vs 11.3B
closed-book model on questions the closed-book model had to hold in weights),
paper-specific mechanics named (frozen document encoder, FAISS index,
query-encoder-only fine-tuning), and hedges kept on the record (the paper's
Jeopardy 452-pair pairwise is not a general hallucination rate; RAGTruth
answers a different question than "does retrieval reduce hallucination"). No
borrowed clauses from the voice guide's quotations. No headline or dek matches
the recent-pattern molds (no comma-and clause pair, no comma triad, no
semicolon reversal, no suspended question). No sentence flagged as decorative
copula or vague attribution. Em-dashes appear only inside table cells as
missing-value markers; no prose em-dashes; semicolon count low and each in
tight parallel or contrast.

## Reader

Read straight through, the article gives one thing a reader could not get
from any single source: a pairing between each of Lewis et al.'s specific
claims (four benchmark wins, frozen-index training loop, 452-pair Jeopardy
factuality, world-leaders index hot-swap) and what the modern pipeline has
been measured on (Xu on long-context vs retrieval, Liu on lost-in-middle, Niu
on RAGTruth hallucination densities without a matched no-retrieval condition,
Barnett on engineering failure modes), with the explicit test that a claim
about "RAG" using the paper's numbers may be borrowing one system's evidence
for a different system. This matches the draft-handoff's original-work
sentence — the article delivers what the sentence promises.

Prose sits closer to the voice-guide exemplars than a median AI summary: named
authors, specific measurements, comparisons the reader can hold, hedges named
where the evidence stops.

Headline as claim: "Today's RAG pipelines fine-tune neither piece the paper
trained together" is the article's most compressed statement of the thesis
and the body defends it directly (the paper fine-tuned query encoder + BART;
today's pipelines fine-tune neither the retriever nor the generator).
Verified.

## Edits

- Removed the signpost sentence "Where the label held and where it drifted is what the paper's own numbers are useful for." from the end of the Orientation section.
- Fixed "Xu Peng and colleagues at NVIDIA" to "Peng Xu and colleagues at NVIDIA" (correct first-author name for arXiv 2310.03025).
- Fixed "Yuxin Niu and colleagues" to "Cheng Niu and colleagues" (correct first-author name for RAGTruth, ACL 2024).
- Rewrote the Barnett paragraph's last two sentences ("None of the seven failure points would have been resolved by the training loop the paper used, because none of the seven exist in the paper's system. Its retriever and generator had been fitted to each other.") to "Barnett's taxonomy was cataloged on production pipelines that train neither piece, and Lewis et al. never measured their system against it." — closer stays inside what the evidence supports and no longer contradicts the article's own earlier precision on which encoders were fine-tuned.
- Removed the closing Verdict `nb-note nb-note-strong` block from the body, per press/editorial.md's explicit ban on closing the body with a Verdict block.
- Extended the Table 1 caption to name that RAG-Sequence and DPR-extractive TriviaQA figures are on the open-test split while T5-11B+SSM's 60.5 is on the TQA-Wiki subsplit, so the reader who reads only the table is not misled by the mixed splits.

## Required work

- orchestrator: re-stamp the article. The nb-meta block still reports words=1911, which is now stale after the removal of the Verdict block and the signpost sentence and the small caption expansion. Re-running `nb stamp` updates the word count and reading minutes before the PR is prepared.
- writer: after the stamp updates, re-run `./nb check ... --library /home/user/library-checkout` on the edited article to confirm the proof still verdicts PUBLISHABLE. My edits touched only prose, a caption, one author-name fix in two places, and one furniture removal, so no BLOCK is expected, but the proof is the writer's to run.

## Decision

approve, with the direct edits above — the article now teaches the paper honestly, distinguishes the two systems the name "RAG" points at, and lands its judgment in the takeaway alone as the press directs; the remaining items are a re-stamp and the writer's proof, neither of which blocks publication of the substance.
