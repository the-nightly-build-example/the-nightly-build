# writer brief: when-ai-breaks/apple-intelligence-summaries (01)

Inputs:
- ../../editorial-direction.md — house standard, the paper's voice, the series prompt.
- ../../commission.md — the incident, required structure, boundaries, required contribution, source floor, recent-pattern habits to break.
- ../../writing-coach/01/voice-guide.md — how this piece should sound (read before drafting).
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers exactly and address its Contradictions in the prose.
- Initialized article to edit in place: /home/user/the-nightly-build/.nb-work/when-ai-breaks/apple-intelligence-summaries/library/when-ai-breaks/apple-intelligence-summaries.html
- Template context: /home/user/the-nightly-build/.nb-work/when-ai-breaks/apple-intelligence-summaries/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/when-ai-breaks/apple-intelligence-summaries/agent-artifacts/when-ai-breaks/apple-intelligence-summaries/writer/01/draft-handoff.md

Proof (from repo root /home/user/the-nightly-build; iterate with --no-check-links, final with links until BLOCK: 0):
  ./nb stamp .nb-work/when-ai-breaks/apple-intelligence-summaries/library/when-ai-breaks/apple-intelligence-summaries.html
  ./nb check .nb-work/when-ai-breaks/apple-intelligence-summaries/library/when-ai-breaks/apple-intelligence-summaries.html --series when-ai-breaks

This round (honor these from the evidence Contradictions; they are load-bearing):
- The verbatim wording of the false summaries is uneven. The BBC quotes only the Nadal line exactly and paraphrases Mangione and Littler; the full grouped "Luigi Mangione shoots himself; ..." string comes from user screenshots in secondary coverage, not a primary. Lean on the BBC's own paraphrase; if you show a grouped string, label it as a reader's screenshot, not the BBC's text.
- The "also affected" outlets (Sky News, NYT, Washington Post, the November "Netanyahu arrested" case) rest on single, largely unverified social-media screenshots, and Apple mostly declined to comment, so Apple's side is single-origin to two brief statements. Attribute carefully; do not present screenshot claims as confirmed.
- The Maynez et al. (2020) faithfulness figures (>70% of single-sentence summaries hallucinate; >90% of extrinsic hallucinations erroneous) belong to the XSum extreme-summarization corpus, not Apple's feature. Use them to teach the mechanism (intrinsic vs extrinsic unfaithfulness), attributed to that corpus, not as measurements of Apple Intelligence. Mapping the Apple errors onto intrinsic/extrinsic is your synthesis — present it as reasoning, shown, not as the sources' own label.
- The required contribution: separate lossy compression that changed meaning (a semi-final read as a final; an ICC warrant read as an arrest; one gay player's story attached to another's name) from chatbot-style fabrication, and make the aggravator explicit: the outlet's name and icon sat on top of the machine's sentence. The closest neighbor to distinguish is ai-overviews (there junk was read faithfully; here real news was read unfaithfully under the outlet's name).
- Link, do not re-teach: the-mechanics/hallucination and the-instruments/hallucination-rate are the core Background links; the-instruments/rouge (meaning-reversal scored unchanged) is optional. Name bard-jwst-demo / galactica / ai-overviews only to stay distinct.
- Break the "What OpenAI shipped on April 25" opener mold and the recurring "Where the same X still lives" closer-heading mold; write the close in this incident's own nouns. Fresh dek (a false line under the BBC's name the BBC never wrote), no comma-triad / semicolon-reversal.
- nb-meta: date "2026-09-15", harness "claude-code-routine", model "claude-sonnet-5".
