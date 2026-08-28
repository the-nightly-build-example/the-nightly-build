# writer brief: when-ai-breaks/cnet-ai-articles (01)

Inputs:
- editorial-direction.md   (house standard, paper voice, series prompt, template identity)
- writing-coach/01/voice-guide.md   (how this piece should sound; read before drafting)
- researcher/01/evidence.md   (the complete claim set; read its Contradictions closely)
- the initialized article at library/when-ai-breaks/cnet-ai-articles.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/when-ai-breaks/cnet-ai-articles/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/when-ai-breaks/cnet-ai-articles/library/when-ai-breaks/cnet-ai-articles.html --series when-ai-breaks

Record traps you must respect (the research corrected the commission's framing):
- The "more than half / 41 of 77" correction figure is NOT from CNET. CNET's
  editor-in-chief Connie Guglielmo gave NO number in her editor's note — she said
  only "a small number requiring substantial correction and several stories with
  minor issues." The "41" is a tally of correction notes on the live articles made
  by THE VERGE (Mia Sato and Emma Roth) and Engadget (Igor Bonifacic). Attribute
  the count to that external tally; reserve the word "substantial" for the small
  subset Guglielmo actually described. Do not put the number in CNET's mouth.
- The Verge corrections story is bylined Sato and Roth — NOT James Vincent. Use
  the correct byline.
- The mechanism paper Kalai et al., "Why Language Models Hallucinate," is
  SEPTEMBER 2025 — it postdates the 2023 incident. Use it to explain the class of
  failure, but do NOT present it as contemporaneous analysis of CNET. CNET's
  engine was internally built and its architecture is not public, so the technical
  primaries explain the class of failure, not CNET's specific tool.
- The flagship documented error (verified): the AI wrote that $10,000 in a savings
  account at 3% interest would earn "$10,300 at the end of the first year," when
  the interest earned is $300 (the total is $10,300, the earnings are $300). Get
  this exactly right.
- Do NOT assert that Bankrate or other Red Ventures sister sites published their
  own AI-drafted articles — the record does not establish it.

Mechanism to teach (or link): why fluent AI prose can be confidently wrong (next-
token generation optimizes plausibility, not truth; no step verifies a computed
figure) and why fluency suppresses the scrutiny a rough draft would draw. Link the
course's existing lessons (the-mechanics/hallucination, and a lesson on models
getting arithmetic wrong or sounding confident) rather than re-teaching them.

Continuity / differentiation: this is NOT a chatbot answering a user's question
wrong (ai-overviews, nyc-mycity, air-canada, mata-v-avianca). It is a publisher
passing AI-generated articles to the public as vetted editorial, undisclosed, with
errors — an editorial/trust failure plus fluency-masking-error. Make that distinct.

Furniture: a timeline fits the ordered account; a note could carry the specific
compound-interest error; inline <code> only if a reader must preserve an exact
string (unlikely here). Use only what the record verifies. No verdict block in the
body — the takeaway bookend lands the judgment.

Recent shapes in When AI Breaks to break: "[Actor] [did/failed] [specific]" is the
house style; do not clone the most recent two. Avoid banned dek molds and the
comma-plus-"and" heading join.

nb-meta you own: date 2026-08-28; harness "Claude Code"; model "claude-opus-4-8".
