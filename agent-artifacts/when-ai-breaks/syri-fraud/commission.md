# Commission: when-ai-breaks/syri-fraud

## The incident

SyRI (Systeem Risico Indicatie / System Risk Indication): a Dutch government
system that pooled personal data across agencies and ran a secret risk model to
flag people likely to commit benefit, tax, or labour-law fraud. It was deployed
in specific low-income neighbourhoods, and on 5 February 2020 The Hague District
Court ruled the legislation behind it unlawful under Article 8 of the European
Convention on Human Rights and ordered it stopped. This desk teaches one
documented incident; this is it.

## The assignment

1. Tell what happened, in order, with names and dates.
   - What it was built to do: the SyRI legal instrument (in the SUWI Act, from
     2014), letting bodies such as the tax authority, the benefits agency, and
     municipalities link large amounts of personal data and generate risk
     reports on individuals. Name the agencies and the mechanism.
   - What it actually did: it ran in projects in specific neighbourhoods, the
     risk model and its indicators were never disclosed, and people flagged
     could not see or contest why. Say plainly that the targeted areas were poor
     neighbourhoods. Use the municipalities the judgment names (Rotterdam's
     Bloemhof and Hillesluis / Afrikaanderwijk, Capelle aan den IJssel, Haarlem's
     Schalkwijk); treat Eindhoven as reported in secondary sources, not
     adjudicated, if you use it at all.
   - Who it affected and who fought it: the residents of those areas; and the
     coalition that sued the Dutch State (the NJCM, the Dutch section of the
     International Commission of Jurists, with other civil-society groups and
     individual claimants), with UN Special Rapporteur on extreme poverty Philip
     Alston filing an amicus brief.
   - What the operator did afterward: the court's ruling (ECLI reference from the
     record), the ground it decided on, the government stopping SyRI and not
     appealing, and the broader successor law it later pursued (the WGS / "Super
     SyRI") and the criticism that drew.
2. Explain why this kind of system fails this way. Teach, on the spot, the
   mechanisms: the base-rate/false-positive problem when screening a whole
   population for a rare behaviour; proxy discrimination when the data and the
   targeting track poverty (and, through it, other protected traits); and opacity
   defeating contestability, so a wrong flag cannot be challenged. Be precise
   about what the court actually decided: it ruled on proportionality and
   transparency under the ECHR, not on a measured error rate, because the model's
   accuracy was never disclosed. That evidentiary hole is itself part of the
   lesson.
3. Close with where the same weakness lives today, in systems the reader's
   country runs: welfare and tax fraud risk-scoring generally, the WGS successor,
   and the related Dutch childcare-benefits scandal (link it, below).

## Disputed cause — present both sides

The State's position: SyRI was a lawful, necessary, proportionate fraud-fighting
tool with adequate safeguards. The claimants' and court's position: it was
opaque, disproportionate, and discriminatory in effect. Present the strongest
version of each, and say what evidence would have settled it (public disclosure
of the model, its indicators, and its false-positive rate), which never came.

## The one thing this article does that the sources do not

Show the reader that a court stopped this system without any proof of a wrongful
flag, on the ground that a secret risk model aimed at poor neighbourhoods could
not be checked at all, and draw out why unfalsifiable opacity, not a measured
error, was the decisive failure.

## Angle refinement (post-research, orchestrator decision)

The record met the source policy (10 sources; ~7 primary) and the angle holds:
opacity and proportionality, not a measured error, were decisive. Draft to these
and do not overstate:

1. SyRI was NOT established to be machine learning. The State told the court it
   compared files "with the aid of a simple decision tree" (indicators + data
   links + a fixed cut-off), and the court accepted as fact that no deep
   learning or data mining was in use; the scholars note the exact technology
   was never disclosed. Frame SyRI honestly as a SECRET, RULE-BASED automated
   risk-scoring system whose method was never revealed, not as a proven AI model.
   Earn its place on this desk through the present-day tie: this is the failure
   mode of opaque automated risk-scoring that AI systems now scale, and the
   court's transparency/proportionality reasoning is the template now aimed at
   AI. Make that bridge explicit rather than calling SyRI something it was not.
2. The court found a RISK of discrimination against people of "lower
   socio-economic status or an immigration background," not realised
   discrimination, and it declined to order disclosure of the model. Do not
   upgrade "risk" to a finding, and do not claim the court forced the model open.
3. The decisive ground: the legislation was struck under Article 8(2) ECHR as
   insufficiently transparent and verifiable (judgment paras around 6.86-6.95),
   with no finding of a proven wrongful flag; the State never disclosed the
   model, its indicators, or any error rate, so accuracy could not be tested at
   all (paras around 6.49, 6.65, 6.89). This unfalsifiable opacity is the lesson.
4. Dates/names to use: ruling 5 February 2020; ECLI:NL:RBDHA:2020:1878 (English
   translation), Dutch original 2020:865; Section 65 SUWI Act and Chapter 5a of
   the SUWI Decree (Besluit SUWI, Staatsblad 2014, 320); UN report A/74/493;
   government did not appeal (State Secretary Tamara van Ark, 23 April 2020);
   successor WGS ("Super SyRI") adopted by the Senate 18 June 2024 over the
   privacy regulator's objection. Court = The Hague District Court (Rechtbank Den
   Haag). Admissible claimants include NJCM (Dutch Section of the International
   Commission of Jurists), Stichting Platform Bescherming Burgerrechten,
   Stichting Privacy First, and others; Philip Alston = UN Special Rapporteur on
   extreme poverty and human rights. Get exact titles right; a wrong label
   reaches the headline.
5. Verification caveats from the record: Alston's amicus PDF is a scanned image
   with no text layer, so do not print a direct verbatim quote from it (his
   points are confirmed via A/74/493 and the judgment); OHCHR press-release
   quotes came via search indexing because the live page blocks automated
   fetches, so verify any verbatim OHCHR quote against a resolving source before
   printing it.
6. Keep SyRI strictly separate from the childcare-benefits scandal
   (toeslagenaffaire): different system, different lead body (Ministry of Social
   Affairs and Employment / the Inspectorate vs the Tax and Customs
   Administration), different legal event (a civil-court ruling on legislation vs
   the parliamentary inquiry and cabinet resignation). The ~26,000 wrongly
   accused families belong ONLY to the childcare scandal, never to SyRI.

## Boundaries — do not re-teach, and distinguish the neighbour

Link at first use; do not re-teach:
- when-ai-breaks/dutch-childcare-benefits — the toeslagenaffaire, the tax
  authority's childcare-benefit fraud dragnet that used nationality as a risk
  factor and wrongly accused tens of thousands. SyRI is a SEPARATE system: a
  broader cross-agency data-linking instrument struck down by a court on
  transparency/proportionality grounds. State the difference explicitly so the
  two do not read as the same story.
- what-could-go-wrong/automation-bias — over-reliance on a usually-right system;
  link if used.
If a statistical idea (base rate, false positive) needs teaching, teach it
briefly on the spot; assume algebra and probability.

## Sources (when-ai-breaks policy: min 8, primary >=4, secondary >=1)

Primary must include: the court judgment itself (Rechtbank Den Haag, 5 Feb 2020,
with its ECLI number; an official English translation exists on rechtspraak.nl);
the SyRI legal provisions (SUWI Act / Besluit SUWI); Philip Alston's amicus brief
(2019) and/or the UN Special Rapporteur's 2019 report on the digital welfare
state (A/74/493). Cite each figure and quote to the document that owns it, at a
real locator (paragraph number of the judgment where possible). Secondary:
contemporaneous reporting on the ruling and a scholarly analysis (for example van
Bekkum & Zuiderveen Borgesius 2021 on the SyRI judgment).

## Recent shapes to break (compare against the recent library)

- Do not default to the "When you ..." / "You have probably heard" opener or the
  "By the end you will know A, B, and C" closer.
- Check the dek and headings against recent when-ai-breaks pieces
  (babylon-health, iruda-chatbot, dutch-childcare-benefits, predpol,
  amazon-rekognition-congress) so this one is built differently. This desk's
  headlines name who did what; keep that, but do not copy dutch-childcare's
  "turned a passport into a fraud score" shape.

## Production record

Profile balanced. Models "capable" for all roles. Effort targets: researcher
high, writer medium, editor high, writing-coach low. Roles run as isolated
subagents on a capable model (Claude Opus-class); per-role reasoning-effort not
separately dialed in this harness (recorded deviation). No `required` directive
traded down.
