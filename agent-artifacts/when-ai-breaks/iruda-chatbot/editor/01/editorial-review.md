# Editorial review: when-ai-breaks/iruda-chatbot (editor/01)

## Correct

Thesis, stated from the draft alone: Iruda's slurs and its leaked private data
were two results of one decision, to build a fluency-tuned chatbot directly on
9.4 billion real KakaoTalk messages, and Korea punished the data handling, not
the slurs. The claims under it: the corpus was real users' private chat, taken
without meaningful consent; the model both memorized private strings and
reproduced the toxicity of the text it imitated; the PIPC's eight findings were
all about data and named the hate speech only as the trigger; the same recipe
now underlies large language models generally. All four are on the page.

I tried to break the one the piece most needs, that the regulator punished the
data and not the slurs, by reopening the record. The PIPC briefing (s4) and
press release (s5), both authored by 개인정보보호위원회 and dated 28 April 2021,
carry the figures the piece rests on: 94억여 건 (9.4 billion) messages from 약 60만
명 (600,000) users, the 약 1억 건 (100 million) response database, the GitHub
1,431 / 22 / 34 disclosure, the 55.5M surcharge + 47.8M fine = 103.3 million won,
the under-14 counts (48k / 120k / 39k), and the finding that none of the names,
numbers, or addresses were deleted or encrypted. The article's numbers match the
owning documents figure for figure. Boannews (s6) and FPF (s7) confirm the
eight-violation total, the 103.3M figure, and that Article 28-2(2) is the only
provision cited by number. The "1.033 billion" and "~10 billion" errors the brief
warned about are nowhere in the piece; the 9.4 billion figure is stated correctly
even though one secondary I opened (boannews, via a lossy render) mis-scaled 94억
to "940 million." The privacy/enforcement spine holds throughout: the slurs are
introduced as the trigger and explicitly excluded from the eight punished
violations, and no article number beyond 28-2(2) is attached anywhere.

Leakage scope: the piece sits exactly at PIPC's confirmed set. It states names,
place names, gender, and relationship for the GitHub release; untreated names,
phone numbers, and addresses for the training corpus; and Scatter Lab's own
admission that mechanical filtering left real names and bank *names* in replies.
It asserts no surfaced bank-account number as a PIPC finding. Correct.

Hangul and romanization check out against the evidence: 이루다 / "Lee Luda",
㈜스캐터랩, 연애의 과학 / "Science of Love", 텍스트앳 / Text At, 핑퐁 / Pingpong, 김종윤 /
Kim Jong-yoon, 윤종인 / Yoon Jong-in, 개인정보보호위원회 / PIPC, 개인정보 보호법 / PIPA. The
display text (title, dek, subheads, timeline) carries no name or figure that the
owning document contradicts.

href audit: I opened all nine citation addresses as printed. Every one lands on
its source. s4 and s5 resolve to the PIPC-authored korea.kr pages; s6, s7, s8
land on Boannews, FPF, and Digital Policy Alert; s1 and s2 land on the AI Times
and Platum pages carrying Scatter Lab's own launch announcement and January
statement; s3 lands on The Next Web's report of the outputs.

data-nb-kind audit and the source-9 resolution: source 9's href
(news.koreanbar.or.kr, idxno=33912) opens on a 법조신문 (Korean Bar Association
News) article reporting on the judgment, not the court's own judgment document.
Under the primary/secondary test, a report that summarizes a ruling is not the
authoring document, so I changed data-nb-kind from "primary" to "secondary." The
link text already reads "as reported by the Korean Bar Association news," so the
carriage was honest; only the label was wrong. This drops the primary count from
five to four (s1, s2, s4, s5), which still meets the series floor of four
primary, one secondary, eight total, and nb check passes the policy after the
change. I kept s1 and s2 as primary: both carry the primary actor's own words
verbatim (Scatter Lab's launch announcement and its 11-12 January statement and
Q&A), which is primary-by-authorship carried in an outlet, not a different
outlet's independent retelling. The distinction from s9 is that s9's outlet
paraphrases a document it did not reproduce. s3, s6, s7, s8 are correctly
secondary.

Two figures I let stand as the record owns them rather than as a source I opened
rendered them. The plaintiff count is 246 (the number the judgment partly upheld,
per the evidence record); a lossy render of the koreanbar page returned a filing
figure and per-tier counts, but the evidence record owns 246 and the tiered award
100k/300k/400k, so I did not alter the number. The disabled-people, pregnant-seat,
and forum-harassment outputs are attributed to s3; the evidence record documents
all of them as carried by that source with independent corroboration (The
Conversation, AI Incident Database 106), while a partial render of the page
surfaced only the lesbians and Black-people lines. I did not change the
attribution, because the record owns it and the render is unreliable; I flag it
as a residual rather than a fix.

## Reads well

One sentence went because it said nothing the dates did not already say: "The
public reaction was fast; the legal reckoning was not." It reduces to "the X was
fast; the Y was not," a rhythmic antithesis on a semicolon, and the gap it
gestures at is carried by the 12 January shutdown and the 28 April fine sitting
side by side. Deleted, not repaired.

One phrase went because the evidence record does not own it: "most of them
young," describing Iruda's 750,000 users. The user figure is Scatter Lab's; the
age skew is not in any owning document in the record, only in the commission's
framing. I narrowed the sentence to the figure the source owns. This is
narrowing to what the record supports, not hiding thin reporting.

I checked the edges for borrowed phrasing against the writer brief and
commission and found none lifted whole; the piece states the incident in its own
clauses. The headline's "for its training data, not its slurs" is the banned
antithesis form, and it stays for the one reason the standard allows: the
misconception it corrects (that the slurs were the punished offense) is real and
is the article's whole subject. The closer is in this incident's own terms, not
the desk's "the same flaw wherever X" mold: it names the recipe, the external
safety layer, and the data-as-exposure point. No comma-triad or semicolon-reversal
dek; no "clause, and clause" heading. The five headings reconstruct the argument
in the piece's own nouns.

## The experience

Read from the top, the page teaches in order: what Iruda was, the two failures,
what the regulator punished, the one root, and where the recipe lives now. The
timeline component earns its place, six verified dated events a reader can scan,
each tied to an owning document. Nothing on the rendered page implies a figure
the record does not hold. What the piece gives beyond its sources: it resolves a
record scattered across a regulator's briefing, a company apology, and years of
court reporting into one causal claim a newcomer can carry, and it shows from the
primary documents that not one of the eight punished violations was the hate
speech that opened the case. That matches the original-work sentence in the
handoff, and it survives.

## Edits

- Changed source 9 data-nb-kind from "primary" to "secondary": its href lands on 법조신문 reporting about the judgment, not the court's judgment text.
- Deleted "The public reaction was fast; the legal reckoning was not." (slop: rhythmic antithesis that adds no fact the flanking dates do not).
- Removed "most of them young" from the 750,000-user sentence (age skew is not owned by any document in the evidence record).
- Ran nb stamp (words 2126) and the brief's nb check with links to BLOCK: 0, WARN: 0.

## Decision

approve — the piece is correct against the record, keeps the privacy-not-slurs
spine, and does original work; every remaining issue was fixable here without a
different argument.
