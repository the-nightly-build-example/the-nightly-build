# Editorial review: what-could-go-wrong/lethal-trifecta (editor/01)

## Skeptic

The thesis: an AI agent that at once can reach private data, takes in untrusted
content, and can communicate outward can be hijacked by an instruction hidden in
that content into leaking its user's data; this was shown against four shipping
products in 2025, all researcher proof-of-concept and none used on a real
victim, while the leap to autonomous open-ended harm stays a forecast, and the
defense that holds is to remove one of the three permissions.

The claims it stands on, and how each held:

1. The three-permission definition and the prompt-injection mechanism (s1).
   Willison's post carries both the definition and the reasoning, and the article
   states the mechanism without intent language: "Nothing here requires the model
   to want anything." The orientation paragraph actively forecloses the alignment
   reading the commission warns against. Holds.

2. Four 2025 cases each moved real private data out of a live product. I reopened
   all four owning primaries. GitHub MCP (s2): a public issue drives the agent to
   copy private-repo contents into a public PR; published 2025-05-26. GitLab Duo
   (s6): hidden instructions exfiltrate private source through an image URL;
   disclosed 2025-02-12. EchoLeak / M365 Copilot (s3): CVE-2025-32711, CVSS 9.3
   Critical, zero-click. AgentFlayer / ChatGPT (s5): a shared Drive document
   exfiltrates secrets through auto-loaded image rendering; published 2025-08-06.
   The table's "injected through / data left via / disclosed and response" cells
   match each source. Holds.

3. All four are proof-of-concept, none in the wild; the CVE marks exploit code
   unproven (s3). Verified against the CVE vector (E:U). The holds-up grid and
   takeaway both hold this line open and apart from the forecast. Holds.

4. Detection defenses keep being beaten: OpenAI's url_safe bypassed via Azure
   storage links (s5), Willison's "95% is a failing grade" (s1). Verified at both
   sources. Holds.

5. The working defense removes a leg: GitLab blocked external image domains (s6);
   Willison advises not combining the three (s1). Holds.

6. CaMeL as the strongest counter: 77% of tasks solved with provable security vs
   84% undefended on AgentDojo (s8). Quote and the seven-point arithmetic verified
   at the source. Holds.

Display text: the headline ("Researchers pulled private data out of four shipping
AI agents with hidden text") is the largest claim and the piece defends it, with
actors and count concrete. The dek adds the framing's author and his detection
claim without restating the headline, and it carries none of the banned dek molds
(no comma-triad, no semicolon reversal, no suspended question, no "The [thing]
that" opener; the single "and" is a compound predicate, not the comma-and twist).
The three authored subheads are each a concrete step, not scaffolding, and the
orientation heading is its own step rather than a paraphrase of the headline. The
closing body heading is a concrete mitigation claim, not the "confidence outruns
the proof" verdict mold the desk flagged.

Two breaks found, both routed to the writer:

- Misquote (s2). The article prints the Invariant quote as "GitHub alone cannot
  resolve through server-side patches." The source reads "GitHub alone cannot
  resolve this vulnerability through server-side patches." Words are dropped
  inside the quotation marks with no ellipsis. A quotation is the writer's to
  repair; restore the dropped words or mark the elision.

- Under-sourced attack-channel detail (EchoLeak). "It was zero-click: a crafted
  email was enough" sits under s3, but the CVE record establishes only the
  no-interaction rating (AV:N/UI:N), not the email delivery channel; its
  description is "AI command injection in M365 Copilot allows an unauthorized
  attacker to disclose information over a network," with no mention of email.
  The email vector is owned by the EchoLeak disclosure (reported in Willison's
  s4). Attach the source that carries the email channel or recast, so the claim
  is cited to a source that establishes it.

Citation hrefs: I opened all eight as the article prints them. Each lands on the
source itself. The one data-nb-kind I checked hardest, s4, is correctly labeled
secondary (Willison reports Aim rather than owning EchoLeak); the other seven are
correctly primary. Attribution care held: the article never uses Aim's "LLM Scope
Violation" phrasing, and rests EchoLeak on the CVE plus Willison. No working
payload or exploit recipe is present; the one illustrative injected sentence is
non-functional and the exfiltration channels are described at the threat-model
level.

## Cut

Two sentences failed the slop test and were cut.

- "That is also where the evidence stops, and the gap matters as much as the
  finding." A signpost that grades the argument's balance rather than adding a
  fact; the two sentences before it already establish that prevalence is
  unmeasured and that the finding is scoped to four products. The paragraph now
  ends on the fact-carrying "in each one a researcher made it leak," and the
  holds-up grid that follows makes the gap concrete.

- "Set the camps side by side and the honest state of the argument shows." A
  throat-clearing opener that announces the move instead of making it; it
  reduces to a sentence anyone could write about anything. The paragraph now
  opens on the stronger "The dismissal, that a classifier has this handled, is
  contradicted by the record."

The surviving negative-parallelism constructions were each checked against a
named misconception and kept as earned: "through a feature, not a bug" (the
piece names that the tools were never compromised), "not merely doubted in
theory" (the demonstrated-vs-speculative spine), "CaMeL is not a sharper filter,"
and "The cause is not neglect." No prompt leakage: the bookends state what the
lesson covers, which the template allows, and do so in reworded terms rather than
lifted brief framing. No em-dashes; colons and the one compound sentence obey the
punctuation rules. Furniture is earned and not stacked: one table for the
four-case record and one holds-up grid for the demonstrated-vs-forecast line, no
stat strip and no note by reflex, and the press rule against a closing Verdict
note is observed.

## Reader

Read straight through as the paper's reader, I come away with something no single
source gives me: a three-question test I can run on any agent I am handed, built
from four separately disclosed exploits, and a clean separation of the
demonstrated fact (injected text pulled private data out of shipping products)
from the forecast it travels with (autonomous open-ended harm, which no source
shows). The original-work sentence claims exactly that, and it survives. The prose
sits closer to the voice-guide exemplars than to a median summary: it states its
verdicts flatly, tests the strong words instead of borrowing them, and keeps the
line between shown and supposed in the open. Cutting the two signpost sentences
moved it further from the median.

## Edits

- Orientation opener: "showed that working against four products" to "showed it
  working against four products" for clarity; no change of fact.
- Cut the every-case-leaked closing sentence "That is also where the evidence
  stops, and the gap matters as much as the finding" as a self-grading signpost.
- Cut the defenses-section opener "Set the camps side by side and the honest
  state of the argument shows" as throat-clearing.

## Required work

- writer: Repair the Invariant quotation (s2). Printed "GitHub alone cannot
  resolve through server-side patches"; source reads "GitHub alone cannot resolve
  this vulnerability through server-side patches." Restore the dropped words or
  mark the elision.
- writer: Source the EchoLeak email-delivery detail. "a crafted email was enough"
  is not established by the CVE (s3), which carries only the no-interaction
  rating; cite the source that owns the email channel (Willison's s4) or recast.
- orchestrator: Re-stamp and re-run the proof after these edits. Three sentences
  changed (one reworded, two cut), so word count and link set have shifted.

## Decision

Revise. The argument and its calibration hold and my prose cuts are made, but a
quotation is misquoted and one attack-channel detail is cited to a source that
does not establish it; both are the writer's to fix before publication.
