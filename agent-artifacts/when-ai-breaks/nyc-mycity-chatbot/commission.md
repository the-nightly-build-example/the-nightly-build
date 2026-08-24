# Commission: when-ai-breaks/nyc-mycity-chatbot

## The incident

New York City's MyCity chatbot, launched by Mayor Eric Adams in October 2023 to
answer questions about running a business in the city, told users that
landlords could take housing vouchers off the table, that a boss could take
workers' tips, that restaurants could serve rats, and that they could fire
workers for complaining about sexual harassment. The Markup published an
investigation in March 2024 documenting these outputs and the exact prompts
that produced them. The city acknowledged the failures, kept the chatbot in
"beta," and continued to run it. The lesson tells that story and teaches why
the system failed that way.

## The angle

Tell it from the record: what the chatbot was built to do, who built it (the
city plus Microsoft Azure OpenAI service), what specific answers it produced
that contradicted city and federal law, how the mayor and the city responded,
what the tool disclaimed on the page while producing those answers, and where
it stands now. Name the reporters, the officials, the dates, and the specific
laws the answers ran against.

Then teach why the system failed that way. It is a generative model with
retrieval over city documents; retrieval does not enforce the answer, and the
model can still generate a plain, confident sentence that is legally wrong. The
disclaimer that says "verify the answer with an official source" does not make
the answer correct. Teach the deployment lesson too: a tool a city posts as its
own answer is the city's answer for many practical purposes, whatever the fine
print says, and the harm accrues to the users least likely to know they need to
verify. Close on where the same weakness lives now, in the many public-sector
generative chatbots deployed since.

## Teach, in this order

1. The incident, in order: what the chatbot was for, what it told people that
   was contrary to law, and what the city did (and did not do) about it.
2. Why a retrieval-plus-generation chatbot produces confident wrong answers on
   questions about rules and law: link the earlier lessons on hallucination and
   retrieval rather than re-teaching them, and teach only the piece specific to
   an "official" chatbot restating a fabricated rule.
3. Where the same weakness lives today: the many public-sector or high-liability
   deployments of the same architecture, and what would have to change to
   prevent a repeat.

## Sources

Series policy requires at least eight sources, at least four primary and at
least one secondary. The Markup's investigation with the reproduced prompts is
the anchor primary for the specific outputs. City statements and the MyCity
site itself are further primaries. Follow-up reporting (AP, The Verge, WNYC,
Ars Technica) provides context and additional documented prompts; use them for
what they add and always resolve a citation to the document's own page. The
researcher records where accounts differ and surfaces primary documentation
for every quoted output.

## Boundaries and neighbors

The 2026-08-24 edition runs this alongside the-evidence/retrieval-augmented-
generation, the-instruments/rewardbench, the-mechanics/first-token-latency,
and what-could-go-wrong/algorithmic-monoculture. The-evidence's RAG piece
teaches the paper that named retrieval-augmented generation; this lesson is
about the deployed system failing in the city's name, a distinct thing.

Within when-ai-breaks, the published air-canada-chatbot lesson covers a
chatbot answering with a fabricated policy and its operator being held liable;
this incident is different in a specific way — the deployer is a city, the
"policy" is law, and no court intervened. Keep those distinct, do not retread
the air-canada framing, and link ai-overviews (the Google incident on
misleading generated answers) if useful for the mechanism.

## Production record

Template: lesson. Series: when-ai-breaks (open section, self-chosen topic).
Production policy resolved to the balanced profile: writing-coach effort low,
researcher effort high, writer effort medium, editor effort high, model
"capable" for every role. No `required` directive applies.
