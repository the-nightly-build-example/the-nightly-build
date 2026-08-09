# writer brief: when-ai-breaks/tesla-autopilot (01)

Inputs:
- `../../commission.md` — the assignment, the desk's what/why/where shape, and boundaries (the two prior AV lessons are a contrast to draw, not to restage).
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting and every revision.
- `../../researcher/01/evidence.md` — the complete set of claims available to you; the Numbers section is exact; read its Contradictions and its source-access flags.
- The initialized article and template context under the workspace (edit in place).

Output: `draft-handoff.md` (this directory). The article you edit is
`.nb-work/when-ai-breaks/tesla-autopilot/library/when-ai-breaks/tesla-autopilot.html`.

Proof (run from `/home/user/the-nightly-build`, iterate `--no-check-links`,
finish with links until `BLOCK: 0`):

```
./nb check .nb-work/when-ai-breaks/tesla-autopilot/library/when-ai-breaks/tesla-autopilot.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

Two disciplines the evidence imposes — respect both:
- The honest record is multi-causal, not "the software killed them." Both NTSB
  probable causes foreground driver behavior (Brown's overreliance and a truck
  failing to yield; Huang's phone game) alongside Autopilot's design, and at
  Mountain View a crushed, unrepaired crash-attenuator drove the injury
  severity. The lesson's force is the design-versus-misuse dispute, and the point
  that settles it is Tesla's own December 2023 recall (23V-838) of every Autosteer
  car for driver-monitoring controls that "may not be sufficient to prevent driver
  misuse." Build the disputed-cause section around that.
- Do NOT repeat the ~40% crash-reduction figure NHTSA published in 2017 and Tesla
  promoted: it was discredited in 2019 after a FOIA suit and NHTSA disowned it.
  Do not lean on Tesla's miles-per-fatality comparisons either (same
  missing-denominator flaw). The evidence record explains why.

Link-resolution caveat (affects `--check-links`, read the evidence's access
flags): Tesla removed its two blog statements ("A Tragic Loss," 2016; "An Update
on Last Week's Accident," 2018) from its live site, and the QCS reanalysis was
read via a reproduction. Any citation whose `href` no longer resolves will BLOCK
the proof. For each such source, cite a stable resolving address — a
contemporaneous reproduction or a web-archive capture of Tesla's original — and
label the kind honestly (a reproduction carrying Tesla's words is secondary; an
archive of Tesla's own page can stay primary). Every printed href must resolve.

Teach on the spot only as far as needed: SAE Level 2 (what "the driver is still
the driver" means), automation complacency, and operational design domain. Do not
turn the lesson into a taxonomy. Get every name, date, and place exact against the
evidence — a wrong label in the headline/dek/subheads is the costliest error here.

Recent habits to break:
- The desk's Why card recently closed on "By the end of this lesson you will be
  able to say exactly how…". Write the promise in this incident's own terms.
- The last two incident lessons resolved on "the tool was not broken; it did
  exactly what it was built to do." This incident is the opposite shape — a system
  used outside what it was built for — so do not borrow that frame or the line
  "The tool was not broken." Land the takeaway on the two questions a reader
  should carry (what conditions can it not handle; what keeps the human watching),
  in fresh words, not the "the first question is not A, it is B" mold.
- Do not close on "Now you know which one you are looking at." Vary any note
  label; do not default to "In plain language." If you use nb-timeline, confirm
  it is the right primitive, not a default.

nb-meta: set `harness` to `claude-code-routine` and `model` to `claude-opus-4-8`
(writer ran on Opus), matching the library's convention. `nb stamp` writes counts.
