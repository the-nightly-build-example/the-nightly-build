# Writer handoff: what-could-go-wrong/autonomous-weapons (02) — revision

## Original work

Still holds, unchanged by this round: the evidence record supplies the claims
but not the argument. This draft stages a single line of reasoning — the
alarm at full strength, a system-by-system reality test (Belfer's denial, the
UN Libya report's hedge, Harpy's now precisely-dated export history) rendered
as a comparative table, an explicit deployed-vs-speculative line closed with
one earned two-sided verdict, and a named political counterweight (Russia's
CCW position, set against Guterres/Spoljaric) that shows the doom side's
"moral red line" and the dismissal side's "law already covers it" each
outrunning what the record actually proves — a synthesis and a judgment the
evidence itself never renders. Re-anchoring the Harpy date to a sourced
export timeline, rather than dropping the claim, is what keeps that synthesis
standing on real ground instead of an unsourced decade.

## Required items resolved (editor/01 + researcher/02)

1. **Harpy date reframe.** Replaced every "since the 1990s" instance with the
   sourced Sino-Israeli export timeline from researcher/02 (Jamestown/Shichor,
   new source 13): Israel negotiated Harpy's sale to China in the mid-1990s
   and had reportedly delivered about 100 of the drones there by 1999. Updated
   consistently in the nb-meta dek, the rendered dekline (kept identical to
   the dek), the why-this-matters bookend, both Harpy-history sentences in the
   body (what-real-systems-do), the holds-up grid bullet, the-fight-now's
   closing paragraph, and the takeaway. No instance of a bare "1990s" claim
   remains uncited or unanchored to the mid-1990s export finding.
2. **Russell's role.** First mention in the orientation section now reads
   "who helped present the letter," cited to FLI's own 2015 year-in-review
   newsletter (new source 2, first-cited before the renumbered UC Berkeley
   News source), which states Russell and Toby Walsh "presented the
   autonomous weapons open letter" at its July 2015 launch. No instance of
   "drafter" exists in the draft. The second mention (Slaughterbots
   paragraph, "some of the letter's own signatories, Russell among them") is
   left as "signatories," an accurate description researcher/02 confirms
   (KQED) and the brief lists as an acceptable term.
3. **Sentence-density warning.** Found the sentence the tool's flattened text
   was actually merging: the Kallenborn quote closed on the HTML entity
   `&hellip;` immediately before a closing curly quote and a citation number,
   which the proof's sentence-end regex does not recognize as a sentence
   boundary (it looks for a literal `.`, `!`, or `?`), so the parser fused it
   with the following sentence into one 58-word block. Fixed the root cause
   (swapped the entity for a literal `...` so sentence-end detection works)
   and split "offers the closest thing to a positive claim, hedged twice:"
   into two sentences for clarity. No density warning remains.
4. **Preserved the editor's 13 direct edits** (named-person fixes, the
   IHL-distinction plank, the slop cuts, the Kallenborn ellipsis, the
   "Fully Autonomous"-only Harpy quote) — none reopened or reversed.

## Side effects of the above, also resolved

- Adding the sourced Harpy export detail and the cited Russell-role clause
  pushed the article to 2263 words against the lesson band's 1200-2200
  ceiling (a new `W-LENGTH-HIGH` this round's edits caused, not one
  editor/01 flagged). Trimmed genuine fat across the piece — filler openers
  matching the pattern editor/01 already cut elsewhere in this exact section
  ("The deadlock is not a mystery.", "The other side has kept pressing."),
  redundant modifiers ("already," "own," "evidently," "most," "even" where
  they added nothing checkable), and a same-publisher source-list format fix
  — without cutting any claim, citation, or steelman plank. Landed at exactly
  2200 words, the top of the band.
- Two new sources required renumbering every citation in the piece (the
  Russell-role source enters right after source 1; the Harpy export source
  enters right after the old source 11). Both were inserted at their true
  first-citation position and the full source list, hrefs, and sup numbers
  were renumbered 1–17 to keep W-CITE-ORDER clean.

## Proof result

`./nb check .nb-work/what-could-go-wrong/autonomous-weapons/library/what-could-go-wrong/autonomous-weapons.html --series what-could-go-wrong` (links checked, matching the brief exactly):

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

No warnings intentionally left. `nb stamp` wrote words=2200, sources=17,
reading_minutes=10. nb-meta `model` remains `"claude-sonnet-5"`; nb-meta
`dek` and the rendered dekline were checked character-for-character and are
identical.

## Display-text self-test

- Dek: "A radar-seeking weapon Israel was exporting to China by the
  mid-1990s meets the 2015 open letter's definition of one." Checked against
  source 13 (Jamestown/Shichor: negotiated mid-1990s, ~100 units delivered by
  1999) — accurate and not overclaiming a fielding date, only the export one
  the record supports.
- Headline is unchanged from editor/01's approved version; not touched this
  round.
- No banned dek/heading mold introduced (no semicolon reversal, suspended
  question, or comma triad).
- Every new or edited display-text claim (dek, both bookends, holds-up
  bullet, the-fight-now, takeaway) traced back to a source that owns it:
  the Harpy export timeline to Jamestown/Shichor (13), Russell's role to
  FLI's own newsletter (2).

## Open questions

None. No new evidence or voice question outstanding.
