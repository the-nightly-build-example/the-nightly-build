# editor review-brief: what-could-go-wrong/lethal-trifecta (01)

Inputs:
- editorial-direction.md (house standard, slop/headline/punctuation rules, press voice, lesson identity, The What Could Go Wrong prompt)
- commission.md (assignment, boundaries, original-contribution target)
- writer/01/brief.md (the exact writer brief)
- writing-coach/01/voice-guide.md (read first; register and the quoted exemplars the writer read)
- researcher/01/evidence.md (the claim set; reopen sources to try to break claims)
- writer/01/draft-handoff.md (open the original-work sentence only on the third read)
- the article at library/what-could-go-wrong/lethal-trifecta.html
- template context under .nb-context/

Round focus:
- The demonstrated-vs-speculative line is the spine the desk requires. Confirm the prose keeps
  the four 2025 disclosures (Copilot/EchoLeak CVE-2025-32711, GitLab Duo, GitHub MCP,
  ChatGPT connectors/AgentFlayer) as researcher proof-of-concept, NONE exploited in the wild,
  and holds that demonstrated fact apart from the forecast of autonomous open-ended harm.
  Any sentence that blurs the two is a required fix.
- Framing discipline: this is a security argument, not an alignment one. Flag any drift into
  "the model wants to" / intent language about the model.
- Honesty of the prevalence gap: the writer flagged that "shipped the combination on by
  default" is a synthesis across the four cited products, not a field-wide figure, and the
  article says prevalence is unmeasured. Confirm the prose never implies a prevalence number
  the evidence lacks.
- Attribution care: Willison's post is the framing's origin (cite as that); Aim Labs' own
  EchoLeak writeup was unreachable, so EchoLeak rests on Microsoft's CVE + Willison quoting
  Aim. Confirm the article does not attribute Aim's exact "LLM Scope Violation" phrasing as if
  read firsthand. Open each citation href; confirm it lands on the source itself.
- Distinctness: the piece must link the-mechanics/instructions-are-data for the mechanism and
  not re-teach it; it owns the deployed-agent exfiltration surface, distinct from jailbreaks.
- No working payload or exploit recipe should have crept in.

My recent-pattern notes (catch formulas; compare against the recent library):
- Dek molds: the two-clause "claim, and/so the twist"; the comma-triad; the "The [thing]
  that..." opener. Recent wcgw deks lean on the comma-and twist ("Its authors admit they
  can't yet show how the loop closes, and..."). Cut on sight if present.
- Closing body heading mold: recent wcgw pieces close on a "the confidence outruns the proof"
  verdict heading ("The doom and the dismissal both outrun the evidence," "The reassurances
  run out where it would matter most"). Keep the present/gap content; revise the heading if
  built to that stamp.
- Furniture reflex: nb-note/nb-stat-strip by habit; a holds-up grid or position card is fine
  only if the for/against material wants it. Remove any component doing no work.
- Orientation heading should be its own concrete step, not a paraphrase of the headline.

You edit prose, structure, and documented furniture directly and log every change; route
numbers/claims/evidence gaps to the writer or researcher. The orchestrator stamps and
re-checks after your edits. Decision: approve only when no publication-blocking work remains.
