# Commission: when-ai-breaks/iruda-chatbot

## The assignment
This desk teaches one real AI failure with a record. Tonight's incident: "Iruda"
(이루다, "Lee Luda"), a Korean chatbot launched by the Seoul startup Scatter Lab in
December 2020 and shut down within about three weeks, in January 2021, after two
distinct failures — it emitted hate speech (slurs against women, sexual
minorities, and disabled people) under ordinary use, and it was found to have been
built on, and to leak, the real private KakaoTalk messages of Scatter Lab's other
apps' users, who had not meaningfully consented. Korea's Personal Information
Protection Commission (PIPC) investigated and, in April 2021, fined and ordered
corrective action against Scatter Lab.

Tell it in order, with names, companies, and dates:
1. What Iruda was built to do (a 20-year-old-woman persona chatbot on Facebook
   Messenger, marketed as a natural conversational "AI friend," reaching hundreds
   of thousands of mostly young users).
2. What it actually did: the toxic outputs users elicited, and the separate
   discovery that it responded with real names, addresses, and bank-account-like
   snippets — because Scatter Lab trained it on ~10 billion (figure to verify)
   KakaoTalk messages harvested from its "Science of Love" (연애의 과학) dating-advice
   apps without proper consent.
3. Who it affected and what the operator did: the public backlash, the shutdown,
   the class action by affected users, and PIPC's ruling and fine (verify the
   exact amount, ~₩103 million, and the specific violations of Korea's PIPA).
4. Why this kind of system fails this way — teach the missing pieces on the spot:
   training on real conversation logs means a model can regurgitate memorized
   personal data, and a model tuned only for human-like fluency inherits the
   toxicity of its training text with no filter. Link the library's
   `the-mechanics/memorization` and `the-mechanics/hallucination` only where they
   help; teach what the reader needs here.
5. Where the same weakness lives today: models trained on scraped human data still
   memorize and can surface private strings, and chat models still require added
   safety layers to suppress toxic completions.

## The one-sentence contribution this article owes
Show that Iruda was two failures with one root — a model trained directly on real
users' private chats — and that the privacy violation, not the slurs, is what the
regulator actually punished, marking one of the first major AI-specific data
enforcement actions.

## Boundaries and what not to re-teach
- `when-ai-breaks/microsoft-tay` (2016) is the obvious cousin (a chatbot turned
  toxic). Link it in Background and make Iruda's distinct angle — training-data
  privacy and the regulator's enforcement — the spine, so this is not a second Tay.
- Do not re-teach memorization or toxicity from scratch; teach only the piece the
  incident needs and link the library.
- Keep to the record: PIPC ruling, court filings, contemporaneous reporting that
  held up. Where the cause or a figure is disputed, give the strongest account of
  each side and say what would settle it.

## Source obligations (resolved)
`nb source-policy --series when-ai-breaks`: minimum 8 sources; at least 4 primary,
at least 1 secondary. Primary: the PIPC decision / official press release (April
2021) for the violations and fine; Scatter Lab's own statements/apology; the
class-action or court filing if available; primary Korean-government or
data-protection-authority documents; an academic case study that quotes the
primary record (e.g. the several 2021–2022 papers analyzing the Iruda incident) —
used for the primary facts they reproduce, classified honestly. Secondary:
reputable English/Korean reporting (MIT Tech Review, The Korea Herald, Yonhap) for
context only, never as the owner of a number. Verify the message-count figure, the
user-count figure, the fine amount, and every date against a document that owns
it; two retellings of one origin count as one.

## Production record (resolved)
`nb production-policy --series when-ai-breaks`: profile balanced. researcher high /
capable; writer medium / capable; editor high / capable; writing-coach low /
capable. None required; use the most capable available model per role, record
actuals in `nb-meta`.

## Tonight's neighbours (one paper, no overlap)
- the-evidence/long-short-term-memory.
- the-instruments/helm.
- the-mechanics/answer-length-bias.
- what-could-go-wrong/responsibility-gap — accountability doctrine, illustrated by
  Western self-driving cases. Different incident and different lens; no overlap.

## Recent shapes and habits to break (from the last ~2 weeks of this desk)
- This desk closes on "where the same weakness lives today / the same flaw,
  wherever X" (chatgpt-data-leak, predpol). That closing beat is the series form,
  but write it in this incident's own terms, not that mold.
- Recent deks add a second sentence that widens the scope ("...and it lived in an
  open-source library much of the web shares"). Fine as a form; make it carry a
  specific fact, not a flourish.
- Avoid comma-triad and semicolon-reversal deks; vary heading construction, no
  comma-and headings.
- Names and non-English terms must be exact: verify the Hangul, the romanization
  (Lee Luda / Iruda), the company name (Scatter Lab), and the app name.
