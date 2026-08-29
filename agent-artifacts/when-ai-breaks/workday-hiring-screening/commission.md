# Commission: when-ai-breaks/workday-hiring-screening

## Subject / incident
The incident: Derek Mobley v. Workday, Inc. Mobley, an applicant who says he was
rejected from more than 100 jobs screened through Workday's applicant software,
sued Workday itself (not the employers) alleging its AI-enabled screening
discriminated by race, age, and disability. The case matters because a federal
court let it proceed against the software vendor as an "agent" of the employers,
and in 2025 allowed a nationwide age-discrimination collective action. This desk
teaches one deployed system that did harm or failed publicly and left a record;
the record here is a live federal lawsuit.

## Why this incident, now
It is the case testing whether the maker of a hiring algorithm, not just the
employer using it, can be liable for discrimination. That is a genuinely new legal
question and the rulings are recent (2024 order allowing agent theory; 2025
conditional collective certification). It teaches the reader how automated
screening can produce disparate impact and who answers for it.

## Angle / what the lesson teaches
Tell it in order, per the series prompt: what the system was built to do (screen
and rank applicants at scale for employers), what it allegedly did (reject Mobley
and others in patterns he ties to protected traits), who it affected, and what
happened next (the suits, the EEOC's and DOJ's interventions, the court's
rulings). Then explain why this kind of system fails this way: teach disparate
impact plainly (a neutral-looking screen that still filters out a protected group
at higher rates), how models trained on past hiring decisions can encode past
bias, and why opacity makes it hard to catch. Draw the sharp line the series
demands between what is proven and what is alleged: as of now the discrimination
is a claim being litigated, not an established finding; what IS established is the
legal ruling that the vendor can be sued as an agent. Close with where the same
weakness lives today, in the automated screening most job applicants now pass
through.

## The article's distinct contribution
The paper has covered biased hiring/screening tools before (amazon-hiring-tool,
itutorgroup, saferent-tenant-screening). The distinct lane here is the liability
question: those cases targeted the employer or were scrapped internally; Mobley
targets the software vendor, and a court accepted the theory. Teach the "algorithm
as agent" holding and what it would mean for every screening vendor if it stands.
Be scrupulous that the underlying discrimination is unproven; the news is the
legal theory clearing a bar, not a verdict.

## Template & policy
- Template: `lesson`.
- Source policy: min 8 sources; at least 4 primary, at least 1 secondary.
- Production policy (`balanced`, none `required`): researcher high, writer medium,
  editor high, coach low. Models this run: coach on a capable Sonnet-class model;
  researcher/writer/editor on a capable Opus-class model. No `required` directive.
- Tags: none (open item).

## Neighbors in this run (differentiate)
Runs alongside the four other lessons; no subject overlap.

## Prior coverage to stay off
`amazon-hiring-tool`, `itutorgroup-age-discrimination`, `saferent-tenant-screening`,
`compas-recidivism`, `optum-health-algorithm` are published. This is not another
"biased algorithm" lesson: its subject is the vendor-liability ruling. Link
amazon-hiring-tool in Background as the internal-tool precedent; differentiate
sharply. Do not re-teach disparate impact from zero if a Background link covers
it — but a short plain definition in-lesson is fine since the argument rests on it.

## Recent habits not to inherit (from the last week of When AI Breaks)
- Headline mold to avoid: "<Company> never <did diligence>" (DoNotPay "never
  tested"; SafeRent "never counted the voucher"; the "never" reveal has recurred).
  Also avoid the "<Actor> let an AI <do X> under <cover>" build (CNET). State this
  case's actual surprise: that the vendor, not just the employer, is on the hook.
- Deks have leaned on a single vivid victim number (SafeRent's "$2,275,000 without
  admitting", CNET's "$10,300 in a year"). A concrete figure is good, but do not
  copy the "settled for $X without admitting" or single-error-number mold.
- Furniture: nb-note is the reflex, with an occasional timeline. A timeline may
  genuinely earn its place here (2023 filing → 2024 order → 2025 collective), but
  choose furniture for the material, not by recent habit.
