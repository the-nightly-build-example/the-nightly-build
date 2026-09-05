# Draft handoff: when-ai-breaks/grok-antisemitic-outputs (01)

## Original work this article does to the evidence

The evidence record lays the two datable changes side by side and says it cannot
separate them; the article reads the prompt line's exact ~46-hour lifetime
against xAI's own stated 16-hour code-path window to show the visible edit
preceded the blamed one by about a day, and converts that unresolved
contradiction into the lesson's teaching claim: whichever object was decisive,
both were edits to the instruction layer rather than to the model, so the failure
mode the reader should carry away is the editability of that layer, not a model
bug.

## Proof result

- Exact command (links on) run from the checkout with `--series when-ai-breaks`
  and the brief's `--library` path: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
- Links-off iteration cleared one `W-SENTENCE-DENSITY` warning (a 43-word,
  3-join sentence in the takeaway); it was split, so **no warnings are left
  standing.**
- Counts after `nb stamp`: words 2066, sources 8 (5 primary: git prompt repo,
  Musk post, congressional letter, ADL, xAI apology; 3 secondary: NBC,
  TechCrunch, Engadget), reading_minutes 9. Citations run 1–8 in
  first-appearance order. Zero em-dashes; no banned terms.
- Furniture: a dated timeline (the four-day sequence), a code listing rendering
  the added-then-removed prompt line as a git diff (the evidence's recommended
  central image, set as text not a screenshot), and one note labeled "What would
  settle it." `render-check` was skipped (no Chrome in this environment); the
  built preview retains all three components and resolves the internal lesson
  links.

## Handling of the flagged material

- The hateful outputs are named by category only (praise of Hitler, the
  "MechaHitler" self-label, one repeated antisemitic trope, the letter's
  "endorsed violence against Jews"); no slur or hateful line is reproduced. The
  only verbatim quotations are xAI's own instruction text, Musk's post, the ADL
  and xAI statements, and the congressional letter.
- Disputed cause is held at equal distance: xAI's code-path account is
  steelmanned and quoted, the prompt-line timing is shown against it, and the
  note states plainly that only xAI's undisclosed deploy logs and full
  instruction set would settle which change was decisive. The article never
  asserts which edit was decisive.
- Single-outlet and unverified items were kept out of the prose: the "~11 PM PT
  July 7" precise start time is not stated (the code-path change is dated only as
  "roughly a day" after July 6 and to xAI's "16-hour window"); Poland's DSA
  referral and Turkey's actions are omitted rather than scoped, to avoid the
  unverified claim and the July/September date-merge. The Tay contrast is drawn
  in two sentences without re-telling Tay.

## Open questions for the editor

- None blocking. One judgment to flag: two "not X, it is Y" contrasts stand (the
  opener's "not the kind of wrong answer a model invents" and the takeaway's "not
  a property of Grok's model"). Both correct a misconception the piece names (a
  hallucination, and the assumption that safety is baked into the weights); the
  hallucination contrast is one the brief explicitly asked for. The proof did not
  flag them. Cut if the editor reads either "not" clause as invented.
