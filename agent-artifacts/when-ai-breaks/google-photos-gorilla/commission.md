# Commission: when-ai-breaks/google-photos-gorilla

## Authorization

Scheduled run for 2026-08-15 (Sat). `nb duty` returned when-ai-breaks as an open
section: choose a topic within the beat, do not repeat a published slug. One of
five articles commissioned tonight, one per due series. No open-item tags.

## The incident

In 2015, Google Photos' automatic tagging filed photos of Jacky Alciné, a
Brooklyn software developer, and a friend, both of them Black, under the label
"Gorillas." Alciné posted the screenshots; a senior Google engineer apologized
publicly and the company's fix was to delete the label. Years later, testing
found Google Photos still returned nothing for "gorilla" and several other
primates, because the underlying recognition was never made safe. The desk tells
the incident in order, explains why that kind of system fails that way, and shows
where the same weakness sits in systems the reader uses now.

## Angle

Follow the desk's arc, from the record.

1. What happened, in order, with names and dates the researcher confirms: what
   Google Photos was built to do (search your photos by automatically labeling
   what is in them), what it did to Alciné's photos, when he reported it, who at
   Google responded and what they said, and what the company actually did in
   response. Draw out the fix precisely: Google removed the "gorilla" label, and
   related primate labels, rather than correct the classifier. Follow-up testing
   (Wired in 2018, the New York Times in 2023) found the labels still switched
   off years later, at Google and at least one competitor. The label carries a
   specific racist history; report that plainly and without ornament, because it
   is why the harm was to dignity and not a neutral mistake.
2. Why that kind of system fails that way. Name the missing piece and teach it: an
   image classifier learns from labeled examples and is tuned for accuracy on the
   whole set, so a group underrepresented in the training data gets worse
   treatment, and the model carries none of the social knowledge that makes this
   particular confusion unthinkable to a person. Anchor the mechanism in measured
   evidence: the Gender Shades study (Buolamwini and Gebru, 2018) found commercial
   image systems far less accurate on darker-skinned faces. Then read the fix as
   evidence: deleting the label instead of solving the confusion says the
   recognition problem was not solved.
3. Where the weakness lives now. The same training-data skew runs through today's
   image classifiers and generative image models. Connect and distinguish the
   published cases: this is a classification failure from underrepresentation,
   distinct from the generation overcorrection in gemini-image-generation, and
   related to the demographic error gaps behind the facial-recognition cases.

## Boundaries and neighbors

- Template: `lesson`. Section: Working Knowledge.
- Source policy: at least 8 sources, at least 4 primary and at least 1 secondary.
  Primary is the record itself: Alciné's own posts, Google's public statements,
  and the firsthand testing reports that held up (Wired 2018, New York Times
  2023), plus the Gender Shades study for the mechanism. Secondary is
  contemporaneous news coverage. Work from the record, not commentary about it.
- Link when-ai-breaks/gemini-image-generation and distinguish it clearly
  (generation overcorrection, not classification). Link the demographic-error gap
  taught in the facial-recognition pieces (facial-recognition-wrongful-arrest,
  rite-aid-facial-recognition) rather than re-teaching it.
- This is the 2015 Google Photos tagging incident and its non-fix specifically.
  Keep it there.

## Recent-desk caution

- Do not open the "Why this matters" bookend with the house "by the end you will
  be able to" formula. Give this incident its own reason to read.
- This desk keeps closing on a section titled for where the weakness lives now
  (chicago-heat-list: "Where this kind of score lives now"; rite-aid: "Where the
  same weakness runs now"). The prompt asks for that substance, so deliver it, but
  title the section and write the closing in this incident's own nouns. Do not
  reuse that heading shape.
- Two of the last five when-ai-breaks headlines are comma-continuation or "X, not
  Y" constructions. Vary this one; state the finding directly.
- Handle the racist label with care: report it, do not sensationalize it, and
  keep the register serious throughout.

## Production record

- Profile: balanced. Stages (model / effort, none required): writing-coach
  capable / low, researcher capable / high, writer capable / medium, editor
  capable / high.
- Harness: each role runs as an isolated subagent on the configured capable
  model (this runtime's Claude model). Deviations recorded per role.
- Workspace: `.nb-work/when-ai-breaks/google-photos-gorilla`.
- Article: `library/when-ai-breaks/google-photos-gorilla.html` under that
  workspace.
