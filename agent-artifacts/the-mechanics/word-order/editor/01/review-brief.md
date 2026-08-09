# review-brief: the-mechanics/word-order (editor/01)

Inputs:
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writer/01/brief.md` — the exact writer brief (for spotting instruction leakage).
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; read first.
- `../../researcher/01/evidence.md` — the evidence to test claims against.
- `../../writer/01/draft-handoff.md` — the original-work sentence (open on the third read) and the writer's 2 intentional density warnings.
- The article: `.nb-work/the-mechanics/word-order/library/the-mechanics/word-order.html`
- Template context under `.nb-context/`.

Round focus / a continuity check only you can make:
- A published sibling, `the-mechanics/attention`, already contains the
  order-blindness demonstration under its heading "Reorder the tokens and nothing
  moves but the labels." This lesson's title and opening are built on that same
  point. Confirm the lesson treats order-blindness as established ground it links
  (a Background row to `the-mechanics/attention`) and builds past — into how order
  is supplied (positional encoding) and whether it holds past the trained length —
  rather than presenting the order-blindness demo as a fresh discovery. If the
  Background link to `attention` is missing, that is required work for the writer;
  the lesson must not cover taught ground as if it were new. The distinct,
  unwritten material here (positional encoding: sinusoidal, learned, RoPE, ALiBi,
  and the open length-extrapolation question) is what justifies the lesson.
- The evidence flags two seams to hold the writer to: the clean order-blindness
  claim is exact for an unmasked layer, and a causal decoder leaks some position
  from the mask (Haviv); and RoPE being relative does not mean it extrapolates
  (it degrades past trained length; YaRN/interpolation exist). Check the draft did
  not overstate either.
- Assess the writer's two intentional `W-SENTENCE-DENSITY` warnings (takeaway
  arc-enumeration; the NoPE sentence) — keep or route as your read decides.
- The ALiBi Fig. 1 asset (`asset-1.png`) is used; inspect that its crop retains
  the evidence the argument spends and its caption is a factual cited label.

Recent-pattern notes (compare against the recent library; the writer cannot see
a formula one article makes):
- Openers across the desk lean on "Every [behavior] you have seen…" and close the
  Why card on a near-verbatim "By the end you can look at any … and say which…".
  Flag if this piece's Why card falls into that mold.
- The last two mechanics lessons (why-replies-stop, thinking-out-loud) resolved on
  a clean two-way split and a takeaway that turns to the reader with "Now you know
  which one you are looking at." Flag that closer and any "So when you meet X, the
  first question is not A, it is B" construction.
- "None of this makes X worthless/fake" was used twice last week — cut any echo.
- The "In plain language" note label recurs across the shelf; if this piece uses a
  note, check the label names the move it makes rather than defaulting.
- Check headings are not all built the same way (comma + "and" joins recur across
  the paper).
