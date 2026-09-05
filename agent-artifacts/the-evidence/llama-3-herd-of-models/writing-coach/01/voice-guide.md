# Voice guide: the-evidence/llama-3-herd-of-models

## How this piece should sound

This lesson reads Meta's Llama 3 technical report for a reader who is fluent and
busy and keeps being handed benchmark tables with no way to check them. The
register is plain and teacherly, closer to explaining a document to a sharp
colleague than to reviewing it. The AI Snake Oil passage "Benchmarks are already
wildly overused in AI... collapsing a multidimensional evaluation into a single
number" shows the register: short declaratives that state a bounded claim and
attribute the standing objection rather than dramatize it. When the report's own
comparison table against GPT-4, GPT-4o, and Claude 3.5 Sonnet is on the page,
that same restraint lets the piece say what a single score leaves out without
reaching for a grand word.

The harder job is to separate what Meta disclosed and measured from what a
downloaded report cannot show. The AI Snake Oil passage about the bar exam does
this by showing its reasoning step by step, from "In a sense" through "So it's
possible that," and holding the conclusion to the strength the evidence
supports. Where this lesson questions whether a reported number measures what it
appears to, the analysis can be built the same way, one visible step after
another, so the reader can follow the doubt rather than take it on trust.

The judgment can be plain and owned. Nathan Lambert writes "I bet a lot of wins
in the ChatBot Leaderboard are just selecting good over bad" and then gives the
mechanism behind the guess. This lesson can state a view about what a
self-reported table does and does not establish, in ordinary words and in the
first person of the desk, as long as the mechanism sits next to it. Lambert's
"we're using one-dimensional tools to make all the decisions for a complex piece
of technology" is available as a frame for the distance between a benchmark
figure and the system it stands in for, when the report leans on the figure.

Scale carries weight when it is concrete. Simon Willison writes "I thought a
model with the capabilities and output quality of GPT-4 needed a datacenter
class server with one or more $40,000+ GPUs," and the exact figure does the work
an adjective would not. The lesson's own numbers, the 8B, 70B, and 405B sizes,
the volume of training tokens, the compute spent on the 405B, land the same way
when they are given as figures rather than described as large. Willison's line
about "environmentally catastrophic plagiarism machines" holds the balance the
desk asks for: he states the critics' strongest case in their own words, grants
the real value in the same sentence, and keeps both on the page. This lesson can
credit the report as an unusually detailed engineering record while it flags the
parts Meta chose to run and disclose, and stay clear of both hype and dismissal.

## Simon Willison, "Things we learned about LLMs in 2024"

Source: https://simonwillison.net/2024/Dec/31/llms-in-2024/

> "This remains astonishing to me. I thought a model with the capabilities and output quality of GPT-4 needed a datacenter class server with one or more $40,000+ GPUs."

The two sentences move from a flat statement of feeling to the concrete thing
that earned it, a specific piece of hardware he had expected to be necessary.
Willison is visible in the first-person admission that his own prior expectation
was wrong, and in choosing the exact "$40,000+ GPUs" instead of a word like
expensive.

> "I think telling people that this whole field is environmentally catastrophic plagiarism machines that constantly make things up is doing those people a disservice, no matter how much truth that represents. There is genuine value to be had here, but getting to that value is unintuitive and needs guidance."

He states the critics' case at full strength and in their own vocabulary, then
says plainly where he parts from it, and grants that the criticism carries truth
even as he sets it aside. The qualifier "no matter how much truth that
represents" is where the person shows: he keeps the credit and the objection
both on the page rather than picking one.

## Nathan Lambert, "Evaluating open LLMs"

Source: https://www.interconnects.ai/p/evaluating-open-llms

> "I bet a lot of wins in the ChatBot Leaderboard are just selecting good over bad. This is the foundation of the signal. When selecting between two answers that are close, really specific training is needed for tiebreaks to see which model is better."

"I bet" marks the first sentence as his own estimate rather than a reported
fact, and the two sentences after it supply the mechanism the guess rests on.
The practitioner is visible in the plain handling of the field's terms,
leaderboard and signal and tiebreaks used without ceremony, and in his
willingness to own an opinion about what a ranking is really measuring.

> "This comes back to the start of the article: we're using one-dimensional tools to make all the decisions for a complex piece of technology."

One sentence names the mismatch the piece has been building toward, a narrow
measuring tool set against a broad system. It reads as a conclusion because the
earlier paragraphs did the work. The colon hands off from the callback to the
claim, and the claim is stated in ordinary words rather than a coined phrase.

## Arvind Narayanan and Sayash Kapoor (AI Snake Oil), "GPT-4 and professional benchmarks: the wrong answer to the wrong question"

Source: https://www.normaltech.ai/p/gpt-4-and-professional-benchmarks

> "Benchmarks are already wildly overused in AI for comparing different models. They have been heavily criticized for collapsing a multidimensional evaluation into a single number."

Two short declaratives that state a standing objection to benchmarks and
attribute it, "have been heavily criticized," rather than presenting it as the
authors' own discovery. The writers are visible in the restraint: the claim is
held to exactly what benchmarks do, compress many dimensions into one number,
and does not stretch past it.

> "In a sense, any two bar exam questions or medical exam questions are more similar to each other than they are to the tasks that professionals do in the real world, because they are drawn from such a constrained space. So it's possible that the inclusion of any exam questions in the training corpus results in an inflated estimate of real-world usefulness."

The reasoning is shown in full. "In a sense" flags an argued point, the clause
after "because" gives the reason, and "So it's possible that" keeps the
conclusion at the strength the evidence supports instead of overstating it. The
care about how hard to press the point is where the authors are visible.
