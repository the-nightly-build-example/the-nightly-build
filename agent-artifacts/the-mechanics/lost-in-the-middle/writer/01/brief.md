# writer brief: the-mechanics/lost-in-the-middle (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writing-coach/01/voice-guide.md (how this piece should sound)
- ../../researcher/01/evidence.md       (the complete claim set; do not exceed it)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/the-mechanics/lost-in-the-middle/library/the-mechanics/lost-in-the-middle.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/the-mechanics/lost-in-the-middle/.nb-context/

Output: ./draft-handoff.md

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then
full including links until BLOCK: 0):
  ./nb check .nb-work/the-mechanics/lost-in-the-middle/library/the-mechanics/lost-in-the-middle.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/f68f1d9c-d5c2-58e1-960b-5ffb60cad58d/scratchpad/library-checkout
Run `nb stamp` before the final check.

This round's focus and decisions the inputs do not carry:
- Do not overstate the effect. It is sharply model-dependent even in Liu et al.'s
  own 2023 data (GPT-3.5-Turbo drops ~22 points, 75.8% to 53.8%, across 20
  documents; Claude-1.3 moves ~4 points over the same span), so "models are lost
  in the middle" overstates the flat cases. The correct magnitude is "more than
  20%" / a max gap of ~22-23 points; secondary coverage quoting ">30%" is wrong,
  do not repeat it.
- Persistence in current frontier models is not directly replicated in the record.
  Hedge it to what the proxies support (RULER effective-vs-claimed context, NoLiMa
  length falloff, Levy et al. length isolation, Liu's own GPT-4 subset), and do not
  assert the specific position-of-answer U in a named 2024-2025 model.
- Mark the mechanism as genuinely open. Do not attribute the effect to
  "positional-encoding decay" alone: RoPE's long-term decay predicts recency, not
  a middle dip, a step none of the primaries take. Present positional-encoding
  effects, attention behavior, and training-distribution effects as candidate
  causes, settled where a primary settles them and open otherwise. The
  not-cured-by-a-bigger-window point is settled (extended and base curves nearly
  superimpose).
- Link the-mechanics/irrelevant-context and the-mechanics/attention in Background
  (both exist); distinguish this behavior from irrelevant-context (distractors) and
  from the needle-in-a-haystack test. No code.
- Commission's "Recent habits not to inherit" is binding: no paired before/after
  headline rhythm, no negative parallelism in headline/dek, vary the first heading,
  no "Today's..." closer. Fill `nb-meta` harness "Claude Code", model
  "claude-opus-4-8".
