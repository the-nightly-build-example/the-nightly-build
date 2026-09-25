# Commission: when-ai-breaks/babylon-health

## The incident

Babylon Health, the UK digital-health company whose "GP at Hand" app and symptom
checker / triage chatbot were marketed as matching or beating doctors. Its
diagnostic-triage claims, built on a 2018 study Babylon presented as showing the
AI performing at or above human GPs, were publicly challenged by clinicians;
the triage chatbot was shown to miss serious presentations; UK regulators and a
whistleblowing consultant scrutinized it; and the company, once valued in the
billions, collapsed into bankruptcy in 2023. A deployed medical-AI system whose
public claims outran its evidence, with a clear record.

## The angle and the desk's method

Tell it in order, from the record: what Babylon built and claimed (an AI symptom
checker and triage chatbot; the 2018 "AI vs doctors" study and its marketing);
what it actually did (missed or under-triaged serious cases in documented
tests; the study's design was criticized as not supporting the claim); who it
affected (NHS patients using GP at Hand / the symptom checker) and who raised
the alarm (consultant oncologist David Watkins / "@DrMurphy11"; the Royal
College / Lancet correspondence by Fraser, Coiera & Wong; regulator MHRA);
and what happened after (Babylon's responses, regulatory attention, the 2023
collapse). Name people, companies, dates.

Then explain why that kind of system fails that way, teaching the missing piece
on the spot: a triage/symptom model optimized and demonstrated on curated
vignettes can look excellent while failing on the long tail of real
presentations that matter most, and a "beats doctors" score depends entirely on
the test set and the comparison protocol. Close with where the same weakness
lives today, in systems the reader uses: consumer AI symptom checkers and the
new wave of LLM medical advice, where a fluent, confident answer is easy and
calibrated safety on rare-but-dangerous cases is the hard, unmeasured part.

Original work for the writer: Babylon's headline was "as good as a doctor," but
the number came from vignette tests the company designed, and the failures that
mattered were exactly the serious presentations a curated test underweights;
the gap between a demo score and safe triage is the whole story. State that and
show it from the study, the clinical critiques, and the documented failures.

## What the lesson teaches (short list, in order)

1. What happened, in order, with the record: what Babylon built and claimed, the
   2018 study and its "AI vs GP" framing, the documented triage failures, the
   critics and regulators, and the 2023 collapse. Names and dates.
2. Why a "beats doctors" medical-AI claim is fragile: it depends on the test set
   (curated vignettes vs real presentations), the comparison protocol, and
   whether the dangerous rare cases are represented. Teach vignette-vs-real and
   why under-triage (missing a serious case) is the costly error. Link a prior
   medical-AI lesson if useful (e.g. when-ai-breaks/retinopathy-field-study for
   deployment gap, or epic-sepsis-model) rather than re-teaching.
3. What the operator and authorities did: Babylon's public responses to critics,
   the regulatory scrutiny (MHRA), and the company's financial collapse.
4. Where the same weakness lives now: consumer symptom checkers and LLM medical
   advice, where fluency is cheap and calibrated safety on rare dangerous cases
   is the unmeasured hard part.

## Boundaries

- One incident (Babylon's diagnostic/triage claims and their fallout). Do not
  turn into a survey of medical AI. Name IBM Watson / others only to place it.
- Distinguish the two failures cleanly: (a) the oversold "beats doctors" claim
  (a study/evidence problem) and (b) documented triage misses (a safety
  problem). Both are the story; keep them distinct.
- Work from the record: the 2018 study, the Lancet/BMJ clinical critiques, the
  documented test failures, regulator statements, reporting that held up. When a
  cause or claim is disputed (Babylon defended its system), present the
  strongest version of each side and say what evidence bears on it.
- Be fair to Babylon: state its claims and defenses in its own words before
  taking them apart.

## Neighbouring articles this run (avoid overlap)

Tonight also runs the-evidence/elmo, the-instruments/mlperf,
the-mechanics/hangman, what-could-go-wrong/ai-environmental-cost. No overlap.

## Recent-pattern notes (habits to break)

when-ai-breaks recently opened with "A chatbot sold as a friend," "A stranger's
chat titles in your sidebar," "Two collisions with the same towed pickup," and
several pieces close on a "the same X, wherever/where Y" or "did not end with Z"
relocation line (iruda: "did not end with Iruda"; chatgpt-data-leak: "wherever
state is cached"). Do NOT reuse that closing mold. Do not mirror the Waymo
piece's "Perception, then prediction" nb-note heading. Dek: one lean sentence
with a concrete detail; no "The same X also..." or comma-triad mold. Headings
distinct from each other.

## Source obligations

lesson under when-ai-breaks: min 8 sources, >=4 primary, >=1 secondary. Primary:
the 2018 Babylon triage/diagnosis study (the document Babylon's claim rests on);
the Lancet correspondence by Fraser, Coiera & Wong critiquing it; any BMJ / peer
critique; the whistleblower's documented test cases (Watkins/@DrMurphy11 where
verifiable, or coverage that reproduces the transcripts); MHRA or NHS regulator
statements; primary reporting on the 2023 bankruptcy (court/company filings or
solid reporting). Secondary: reputable reporting (e.g. Financial Times, The
Guardian, WIRED) for framing and narrative, never for a clinical number the
study or critique owns.

## Production record

Profile balanced. Recorded (policy "capable"): writing-coach Opus 4.8/low,
researcher Opus 4.8/high, writer Opus 4.8/medium, editor Opus 4.8/high. No
required directive; no deviation.

## Bookend link candidates

Background: `when-ai-breaks/retinopathy-field-study` (a model accurate in the
lab, failing in deployment), `when-ai-breaks/epic-sepsis-model` (a deployed
clinical model that underperformed its billing). Go deeper (beyond this paper):
the Lancet critique; solid longform on Babylon's rise and fall. Lesson works for
a reader who opens none.
