# Draft handoff: what-could-go-wrong/lethal-trifecta (01)

## Original-work sentence

The article turns four separately-disclosed 2025 exploits into a single
three-question test a non-specialist can run on any agent they are handed, and
uses that test to hold the demonstrated fact (injected text exfiltrated private
data from shipping products) apart from the forecast it is usually bundled with
(autonomous, open-ended harm), which no source demonstrates.

## Proof result

`./nb check --series what-could-go-wrong --library /home/user/library-checkout`
(links included): BLOCK: 0, WARN: 0, verdict PUBLISHABLE. Stamped words=2197,
reading_minutes=10, sources=8. No warnings left standing.

Model run as: claude-opus-4-8 (recorded in nb-meta; harness claude-code).

## Source composition

8 sources, 7 primary + 1 secondary (s4, Willison's EchoLeak post), meeting the
series floor (>= 8 sources, >= 4 primary, >= 1 secondary). The EchoLeak post is
secondary because Willison reports Aim Labs' disclosure rather than owning it;
the owning primary for EchoLeak's classification/severity/fix is the MITRE CVE
record (s3).

## Calibration and boundaries held

- Demonstrated-vs-speculative line drawn explicitly in the holds-up grid and the
  takeaway: all four cases are researcher proof-of-concept, none reported in the
  wild, and the CVE's "unproven" exploit-code flag is stated as Microsoft's own
  signal.
- The one honest gap is stated plainly and not papered with a prevalence number:
  no measured figure exists for how common the three-leg configuration is; the
  worry rests on the four products shipping it on by default.
- Treated as a security/misuse argument, not alignment. The "nothing here
  requires the model to want anything" line in the orientation forecloses the
  "model wants to betray you" reading the commission warns against.
- instructions-are-data is linked in prose (not a numbered source), per the press
  rule on taught ground; jailbreaks is linked in Background as the neighboring
  surface.
- Aim Labs' own wording (e.g. "LLM Scope Violation") is not used, since it could
  not be read firsthand (Cloudflare 403 in the evidence record). EchoLeak facts
  are carried by the CVE (s3) and Willison's post (s4).
- No working payloads or exploit recipe. The one illustrative injected sentence
  is plainly non-functional; the url_safe bypass and image-exfiltration channels
  are described at the threat-model level, not reproducibly. No source assets or
  charts (evidence named no exact visual the argument spends, and the available
  screenshots risk showing payloads).

## Recent-shape avoidance

- Dek is a single clause, no comma-and twist, no comma-triad, no semicolon
  reversal, no "The [thing] that..." opener.
- Closing body heading ("The defenses that work take away a permission") is a
  concrete mitigation step, not the "confidence outruns the proof" verdict mold;
  the present/gap content sits in that section's closing prose instead.
- Orientation heading ("Three permissions that are each harmless alone") is its
  own step, not a paraphrase of the headline.
- Furniture earned, not stacked: one table (the four-case record, which doubles
  as the reader's checklist) and one holds-up grid (the demonstrated-vs-forecast
  line). No stat strip, no nb-note by reflex.

## Open questions

None blocking. One minor note for the editor: the "shipped the combination on by
default" characterization (orientation/every-case sections) is the evidence
record's synthesis across the four cited cases rather than a figure any single
source states; it is framed as an observation about the four products, not a
field-wide claim.
