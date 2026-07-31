# Voice guide — the-mechanics/instructions-are-data

## Directive

Register: plain expository prose, the register of someone who has actually
looked at the mechanism and is describing what is there, not someone building
suspense around it. No alarm, no wonder, no "here's the scary part." State
the fact and let its concreteness carry the interest.

Reader relationship: teacher, not tour guide. The reader is smart and has
watched a model obey a stray instruction; the piece owes them the mechanism,
not reassurance and not a warning. Do not address the reader directly ("you,"
"imagine") — the house floor already bans this — but do use the reader's own
puzzlement as the entry point the way a good explainer starts from the
symptom before naming the disease. Diagnose, don't narrate the diagnosis.

Moves that change sentences here:

- **Carry the whole explanation on one assembled example.** Build one
  concrete prompt early — system text, user text, injected text, concatenated
  — and keep pointing back at its actual tokens as the argument descends
  through each layer (concatenation, attention, training). Do not introduce a
  second toy example partway through; a reader who has to re-anchor loses the
  thread. Every generalization should be traceable to something visible in
  that one example.
- **Descend in one direction, naming the real part at each layer before
  generalizing from it.** Familiar behavior, then the layer under it, then
  the layer under that, stopping only when a further layer would not change
  the answer. Do not summarize the destination before the reader has taken
  the steps down to it.
- **Consider and dismiss the naive fix before stating what actually happens.**
  The strongest version of this explanation shows why the obvious guess
  (there's a protected channel, the system prompt has enforced priority)
  fails, in the same paragraph that replaces it with the real mechanism. This
  is more persuasive than asserting the mechanism cold.
- **Mark settled and open at the point the argument reaches them, not as a
  hedge tacked on.** A settled step gets stated flatly, no qualifier. An open
  step gets named as open in the sentence that raises it — what is known,
  what is tried, what still fails — not folded into a closing disclaimer.
- **Let one frame do the reducing.** The piece's job is to show that hidden
  system prompts, jailbreaks, and prompt injection are one mechanism wearing
  three names. Name that mechanism once, early, in plain terms, then treat
  each of the three as an instance of it rather than writing three
  mini-explanations that converge at the end. The naming has to happen before
  the instances, or the reduction never lands.
- **Sentence rhythm: short declaratives for what is established, longer
  causal sentences for how one layer produces the next.** A paragraph should
  not hold more than one mechanism.

Recently used, do not reuse:
- A crisp numeric surprise as the opener (a token-id triple, a percentage
  pair). This lesson is qualitative — no manufactured statistic to fake that
  shape.
- A colon-subtitle headline.
- The "X is not Y; it is Z" thesis mold.
- The heading cadence of the last few Mechanics pieces — vary the shape.

## Exemplars

```text
## Ken Shirriff, "How the 8086 processor's microcode engine works"
Source: http://www.righto.com/2022/11/how-8086-processors-microcode-engine.html
Craft:
- cadence: short declaratives establish a fact, then a longer sentence explains
  why it's built that way; paragraphs run two to eight sentences and never
  hold two mechanisms at once
- argument: descends in one direction only — instruction, then microcode,
  then the engine that sequences the microcode — never doubling back to
  re-explain a lower layer once it's been named
- evidence: die photographs and specific numbers (512 micro-instructions, 21
  bits wide, a 13-bit address register) stand in for claims; he shows what he
  looked at rather than asserting a conclusion
- stance: confident where the die photo settles the question, hedged and
  sourced where it doesn't ("based on the patent," a Wikipedia comparison
  flagged as a comparison, not a fact)
- notice: catches on the point where a straightforward-sounding engineering
  choice turns out to be a real design tradeoff, and stops there long enough
  to explain the tradeoff
- diction: names the actual circuit or register at each step; never reaches
  for a generic word to cover something specific
- reader: assumes competence, never condescends, thanks the reader for
  sticking to the end without performing false modesty
- the move the axes miss: he states the naive circuit design first ("the
  straightforward approach is...") and only then explains why it fails and
  what replaced it — the wrong answer does explanatory work before the right
  one arrives
Calibration: "The straightforward approach is to build a circuit from
flip-flops and gates that moves through the various steps and generates the
control signals. However, this circuitry is complicated and error-prone."

## Julia Evans, "New zine: How DNS Works!"
Source: https://jvns.ca/blog/2022/04/26/new-zine--how-dns-works-/
Craft:
- cadence: short, punchy declaratives building momentum, broken by one longer
  clarifying sentence once the short ones have earned it
- argument: starts from the reader's actual confusion (a DNS problem that
  felt inexplicable) and only then supplies the piece of the system that
  resolves it — comprehension arrives as the payoff of a specific frustration,
  not as a definition offered cold
- evidence: a real, nameable failure mode rather than a hypothetical; the
  system is only as real as the broken case it explains
- stance: draws the line plainly between what she'll cover and what she
  won't ("still seems to be evolving"), so the reader knows the edge of the
  explanation without a hedge dragging through the whole piece
- notice: catches exactly where a system feels "magical" to a newcomer and
  treats that feeling as the thing to dissolve, not to preserve for effect
- diction: plain words for technical objects, technical terms introduced only
  once they're needed and then reused exactly
- reader: warm without performing warmth — enthusiasm for the mechanism
  itself, not for the reader's presence
- the move the axes miss: she never returns to the abstract statement of the
  problem once she's moved to the concrete case; the concrete case *is* the
  explanation from that point on, not an illustration alongside it
Calibration: "DNS is very frustrating! I've run into some VERY weird DNS
problems over the years, and it can feel magical and incomprehensible if you
don't know how it works. But once you learn how DNS works, these problems
all become totally possible to understand."

## Troy Hunt, "Everything you wanted to know about SQL injection (but were afraid to ask)"
Source: https://www.troyhunt.com/everything-you-wanted-to-know-about-sql/
Craft:
- cadence: mixes short punchy statements with longer explanatory runs; never
  settles into one rhythm long enough to feel like a template
- argument: names the mechanism first in one line ("breaking out of the data
  context and entering the query context"), then spends the rest of the
  piece cashing that one line out against a single running example
- evidence: one URL parameter and one SQL statement, shown side by side,
  carried through the whole explanation rather than swapped for a fresh
  example each time a new wrinkle appears
- stance: direct about what a fix does and doesn't cover — frameworks that
  parameterize input reduce the risk without eliminating bad code, stated as
  a limit, not a caveat
- notice: catches the exact moment user input stops being data and starts
  being executed, and slows down there instead of rushing past it
- diction: plain, occasionally colloquial, but the vulnerability itself is
  always named precisely — never "an issue" or "a flaw"
- reader: assumed to be intelligent and non-specialist; explained to, not
  performed for
- the move the axes miss: he holds the same artifact — the same URL
  parameter — from the definition through every subsequent variation of the
  attack, so the reader's mental model of "what's happening" never has to
  reset
Calibration: "In a nutshell, it's about breaking out of the data context and
entering the query context."

## Bruce Schneier, "Class Breaks"
Source: https://www.schneier.com/blog/archives/2017/01/class_breaks.html
Craft:
- cadence: short factual sentences to establish a case, a longer sentence to
  draw the general pattern out of it, then another short case
- argument: names the pattern once, in plain language, before using it —
  every subsequent example is presented as an instance of the named pattern
  rather than a new thing needing its own explanation
- evidence: paired, concrete cases (a picked mechanical lock versus a
  compromised electronic one) that share nothing except the pattern being
  named, which is exactly what proves the pattern is real
- stance: separates what's already observed (locks have been picked one at a
  time for centuries) from what's projected (networked devices fail all at
  once), and marks the shift from one to the other in the sentence where it
  happens
- notice: catches that people still reason about computer failure using the
  mental model built for a different kind of failure, and treats that
  mismatch as the actual subject
- diction: no jargon where a plain noun works; the technical term appears
  only once the plain version has done its job
- reader: intelligent and general, walked toward a reframing rather than
  handed one
- the move the axes miss: the essay's whole argument is the act of reduction
  itself — showing that several things people treat as separate problems are
  one problem under a different name — which is the same move this lesson
  has to make with hidden system prompts, jailbreaks, and prompt injection
Calibration: "Picking a mechanical door lock requires both skill and time.
Each lock is a new job, and success at one lock doesn't guarantee success
with another of the same design."
```
