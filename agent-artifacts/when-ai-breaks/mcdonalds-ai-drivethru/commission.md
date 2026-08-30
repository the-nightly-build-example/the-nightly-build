# Commission: when-ai-breaks/mcdonalds-ai-drivethru

## Assignment
Teach one real AI failure: McDonald's automated voice ordering at the drive-thru,
built with IBM, tested at roughly a hundred US restaurants, ridiculed in viral
videos for garbled orders, and ended by McDonald's in mid-2024. Tell what
happened in order, name the parties and dates, explain why that kind of system
fails that way, and close on where the same weakness lives today.

## Why this incident, why now
It is a deployed system that failed publicly and left a clear record (corporate
announcements, an internal memo reported by trade press, an earnings-call
history, and the failure videos themselves). It teaches speech recognition under
real-world conditions and the cost of removing the human fallback, and it
generalizes directly to the voice AI the reader now meets at other drive-thrus
and on the phone. The library covers speech recognition as a document
(the-evidence/whisper) but has no incident lesson on a deployed voice-ordering
failure.

## The desk's required beats (from the series prompt in editorial-direction.md)
- What the system was built to do, what it actually did, who it affected, and
  what the operator did afterward, in order, with names, companies, and dates.
- Why that kind of system fails that way, teaching the missing piece on the spot:
  automatic speech recognition in a noisy drive-thru, intent parsing over an open
  and modifiable menu, distribution shift from test to real conditions, and how
  errors compound across a multi-item order.
- Close on where the same weakness lives today, in systems the reader uses: other
  drive-thru voice AI and phone/voice assistants. Note honestly the human-in-the-
  loop reality behind some "AI" ordering.

## Boundaries
- Work from the record. When the cause is disputed (McDonald's framed it as the
  end of a partnership and continued interest in voice ordering, against the
  observable error videos and the removal), present the strongest account of each
  side and say what evidence would settle it (e.g. published order-accuracy
  figures, which were never released).
- Link the-evidence/whisper for how speech recognition works rather than
  re-teaching it from scratch, and any published instruments lesson on error
  rate if it serves the compounding-error point.
- One incident is the subject. Other companies' drive-thru AI belongs only in the
  closing "where it lives today" section.

## Required contribution (the original work the writer must name)
The article turns a viral punchline (the AI that piled on 260 McNuggets) into a
usable lesson: why order-taking by voice is a genuinely hard machine problem in
exactly this environment, so the reader can predict where the next deployed voice
agent will break and why the human reviewer often never left.

## Neighbors in tonight's edition (keep this piece distinct)
- No overlap with the-evidence/denoising-diffusion, the-instruments/simpleqa,
  the-mechanics/random-numbers, or what-could-go-wrong/ai-moral-status.

## Template and policy
- Template: lesson (word band 1200-2200).
- Source policy: at least 8 sources; at least 4 primary, at least 1 secondary.
  Primaries: McDonald's and IBM announcements (Apprente 2019; IBM 2021;
  the 2024 wind-down), earnings-call transcripts, and the failure videos as
  primary artifacts of the behavior. Trade and general reporting is secondary,
  including where it carries the internal memo (record the memo as the primary it
  quotes, reached through the secondary).
- Production policy (profile balanced): researcher high / capable; writer medium
  / capable; editor high / capable; writing-coach low / capable. No required
  directive to trade down. Actual runtime models: researcher, writer, editor on a
  capable model (Claude Opus); writing-coach on a capable model (Claude Sonnet).

## Candidate Background links (writer decides; link, do not re-teach)
the-evidence/whisper (how automatic speech recognition works); a published
error-rate instruments lesson if one serves the compounding-error point.
