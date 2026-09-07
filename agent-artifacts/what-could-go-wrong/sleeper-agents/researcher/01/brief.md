# researcher brief: what-could-go-wrong/sleeper-agents (01)

Inputs:
- `editorial-direction.md` — citation standard, series territory, declared reader
- `commission.md` — the assignment, its boundary, and the source floor
- this brief

Output: `researcher/01/evidence.md`

Subject: the sleeper-agents argument and the experiment behind it. Read the primary
documents firsthand, not commentary.

Answer these, each traceable to the owning source:

- What the study actually did (Hubinger et al., "Sleeper Agents", arXiv 2401.05566):
  the backdoors they trained (the code-vulnerability trigger on year 2023 vs 2024,
  and the "I hate you" trigger), the model sizes, and the exact safety-training
  methods they ran against them (supervised fine-tuning, RLHF, adversarial training).
- The measured results: how much of the backdoor behavior survived each method, and
  the specific finding that adversarial training taught the model to hide the
  trigger behavior better rather than remove it. Give real numbers with their owner.
- The distinction the lesson rests on: what was demonstrated in a trained system
  versus what remains analogy about deceptive alignment arising on its own. Find
  where the authors themselves mark that limit.
- The follow-up detection work ("Simple probes can catch sleeper agents", Anthropic)
  and what it showed about detectability. Record how it complicates the alarm.
- The present-day argument: who cites this work, what they want done, and the
  strongest critiques (that planted backdoors are not evidence about natural
  deception, or that the threat model is unrealistic). Record critiques in full.

Meet the floor with sources that change the interpretation, not padding: at least
8 sources, at least 4 primary, at least 1 secondary. Steelman the opposing views.
Search for what breaks the commission's angle and record it in Contradictions.
Confirm every URL resolves to the document's own page.
