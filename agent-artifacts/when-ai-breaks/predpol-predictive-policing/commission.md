# Commission: when-ai-breaks/predpol-predictive-policing

## The incident

Place-based predictive policing as sold by PredPol (later Geolitica): software that
told police where crime would happen next, adopted by dozens of US departments,
and then shown by The Markup's 2023 investigation to be almost never right — its
predictions matched later reported crime a tiny fraction of the time — while
researchers had already demonstrated it could entrench a biased feedback loop.
Departments quietly dropped it. When AI Breaks leans toward hallucination, bias,
and liability; this adds a distinct failure: a predictive system whose core output
was both self-reinforcing and, on the record, barely better than noise.

CONFIRMED not previously published (checked against the full when-ai-breaks slug
list). It must stay distinct from three published neighbours: chicago-heat-list
(PERSON-based predictive policing — who, not where), shotspotter-wrongful-arrest
(acoustic gunshot detection), and compas-recidivism (risk scoring at sentencing).
This piece is PLACE-based prediction, its runaway-feedback mechanism, and the
accuracy exposé. Link those lessons; do not retell them.

## The angle

Tell it in order, then explain the mechanism, then where it lives now.

1. What the system was built to do. PredPol grew out of an earthquake-aftershock
   model repurposed for crime: past crime reports predict "hot" 500-by-500-foot
   boxes for the next shift, and patrols are sent there. Name the founders/company,
   the origin (Mohler et al.; LAPD collaboration), and the pitch. Establish plainly
   how it worked and what data it ate (past reported crimes).

2. What it actually did. Report the record: The Markup / Gizmodo 2023 analysis of
   Geolitica predictions (verify the exact accuracy figure — the fraction of
   predictions that matched a later reported crime — and the dataset and period),
   the departments that used and then dropped it, and any city audit (e.g. the LAPD
   Inspector General's findings) and bans (e.g. Santa Cruz). Name places and dates.

3. Why that kind of system fails that way. The teaching core, no code:
   - Feedback loop: the model is trained on RECORDED crime, which reflects where
     police already patrol; sending patrols where it predicts generates more
     recorded crime there, which confirms the prediction — a self-fulfilling loop
     documented formally (Lum & Isaac 2016; Ensign et al. 2018). Distinguish
     recorded crime from actual crime.
   - Base rates and rare events: crime in a given small box on a given shift is
     rare, so most predictions are wrong simply because the event rarely happens
     anywhere — which is how a very low hit rate coexists with a confident-looking
     map. (Link the base-rate reasoning from shotspotter without re-teaching.)
   - What that combination does: a tool that mostly misses, and whose few "hits"
     partly reflect its own patrol pattern, still steers real policing.
   Present Geolitica's / defenders' rebuttals fairly (what they said the accuracy
   number missed) and say what evidence would settle the dispute.

4. Where the weakness lives today. Any system trained on enforcement data to
   predict where to enforce (other predictive-policing vendors, some fraud- and
   inspection-targeting systems). The lesson: when a model's training data is a
   record of past decisions, predicting from it can launder those decisions as
   objective forecasts.

Anchor fact to foreground: the predictions that sent patrols into specific
neighbourhoods matched a later crime only a tiny fraction of the time, and the few
that did partly reflected the patrols the tool itself had ordered — a forecast
grading its own homework.

## Boundaries

- One incident: PredPol/Geolitica place-based prediction. Opendoor/other vendors
  only as brief contrast. Not person-based lists (link chicago-heat-list), not
  gunshot detection (link shotspotter), not sentencing risk (link compas).
- Work from the record: The Markup/Gizmodo investigation and its data, the founding
  papers, city audits, and reporting that held up. Get the accuracy figure from the
  investigation that owns it.
- No code. Teach the feedback-loop and base-rate ideas plainly at first use.

## Required contribution

The reader should finish able to explain why a place-based predictive-policing tool
can be both biased and barely accurate at once (feedback loop on recorded crime;
rare-event base rates), and able to spot the same "predict from a record of past
decisions" trap in other systems. Not "algorithms are biased," but the specific
mechanism and what the record showed.

## Source and production policy

- Sourcing floor (nb source-policy): minimum 8 sources, at least 4 primary, at
  least 1 secondary. Primary = The Markup's investigation (with its methodology/
  data); the founding model paper(s) (Mohler et al.); the feedback-loop papers
  (Lum & Isaac 2016; Ensign et al. 2018); a city audit (e.g. LAPD OIG); a
  company/founder statement. Secondary = reporting that held up.
- Production policy (balanced, no `required` directive): editorial roles run on a
  capable model (Claude Sonnet class) in isolated subagents; effort follows policy
  (coach low, researcher high, writer medium, editor high). No directive traded down.

## Recent-pattern notes (habits not to inherit)

- Opener habit: "By the end you will know..." triad; temporal-generic opening. Break it.
- Takeaway habit: two-part balance closers. End on this incident's own lesson.
- Heading habits over-used across When AI Breaks: "How a bang becomes a gunshot
  alert" (How a X becomes a Y), "Why an alert rarely means a gun crime" / "Why the
  list found the already-policed" (Why X ...), and the closing "Where this kind of
  score lives now" / "A flag that outlived the machine" (the desk's required
  "where it lives now" section keeps getting the same heading shape — give it one in
  this incident's own nouns). Vary construction; do not default to nb-holdsup.
- Dek habit: comma-triad / semicolon-reversal deks (`spec/headlines.md` bans the triad).

## Neighbouring articles in tonight's edition

- the-evidence/flamingo (the 2022 few-shot multimodal paper)
- the-instruments/brier-score (how the Brier forecasting score is made)
- the-mechanics/familiar-pattern-override (why modified classic riddles break models)
- what-could-go-wrong/companion-dependency (the AI-companion-harm argument)
No overlap. This piece adds a place-based predictive-forecasting failure to the desk.
