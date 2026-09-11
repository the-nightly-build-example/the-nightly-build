# Editorial review: what-could-go-wrong/lethal-trifecta (editor/02)

This is a confirmation read of writer/02, checking the two required items from
editor/01 and the prose immediately around them. I did not reopen the settled
skeptic, cut, and reader reads.

## Skeptic

Both routed breaks are now closed, each checked against the source as the article
prints it.

1. Invariant quotation (s2). The article now prints "GitHub alone cannot resolve
   this vulnerability through server-side patches." I opened
   invariantlabs.ai/blog/mcp-github-vulnerability and the sentence reads exactly
   that, word for word, with the dropped "this vulnerability" restored and no
   stray change to the surrounding clause ("is not a flaw in the GitHub MCP
   server code itself"). The quotation is verbatim. Holds.

2. EchoLeak attack channel. The detail is now split so each clause sits under the
   source that owns it. "The attack arrived as a crafted email" is cited to s4
   (Willison's June 11 EchoLeak post), which establishes the email vector: the
   post states the classifier was "bypassed simply by phrasing the email that
   contained malicious instructions as if the instructions were aimed at the
   recipient." The zero-click / no-interaction claim and the "unproven" exploit
   line stay under s3, and I confirmed the CVE record carries UI:N in its vector
   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N/E:U/RL:O/RC:C) and does not
   mention email anywhere. So the CVE now carries only what it owns, and the
   email channel is attributed to the source that owns it. The Willison
   trifecta-classification sentence remains correctly on s4. Holds.

Nothing adjacent regressed. The demonstrated-vs-speculative spine is intact: the
holds-up grid still splits the shown fact from the forecast, the closing
paragraph still holds "they do not show an agent causing the open-ended,
autonomous harm," and "twice with no action from the victim at all" still points
only at EchoLeak and AgentFlayer, matching the evidence record.

## Cut

No new slop entered with the revision. The added clause "with nothing for the
victim to open or approve" carries a fact (the no-interaction rating in plain
words) rather than restating zero-click emptily, and "The attack arrived as a
crafted email" is a bare reported fact. The split produced no comma splice or
run-on; each of the four resulting sentences is grammatical and single-purpose.

The writer's "same record" to "CVE record" change reads cleanly and fixes the
antecedent it was meant to: "unproven" now attaches unambiguously to the CVE.
The phrasing "the detail the rest of this lesson turns on" is unchanged from
editor/01 and was not reopened.

## Reader

Unchanged from editor/01 and still true: the piece hands the reader a
three-question test built from four separately disclosed exploits and keeps the
demonstrated fact apart from the forecast. The two fixes strengthen that, because
the EchoLeak paragraph now attributes the email delivery to the source a reader
could check it against. Prose still sits closer to the voice-guide exemplars than
to a median summary.

## Edits

None. The two fixes held on inspection and no adjacent regression needed repair.

## Required work

- orchestrator: Re-stamp and re-run the proof. The EchoLeak sentence was split
  and a clause added, so word count (nb-meta still reads 2172) and the link set
  have shifted. This was already routed in editor/01 and is restated here only so
  it is not lost.

## Decision

Approve. The Invariant quotation is now verbatim, the EchoLeak email channel is
cited to the source that owns it while the CVE carries only the no-interaction
and unproven-exploit facts, and nothing adjacent regressed.
