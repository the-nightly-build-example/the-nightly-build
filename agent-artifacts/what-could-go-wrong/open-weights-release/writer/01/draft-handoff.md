# Draft handoff: what-could-go-wrong/open-weights-release (writer 01)

Original work: this article takes Seger et al.'s qualitative claim that
undoing a released model's built-in safety training is the "harder" of the
two removal routes (needing a curated dataset, compute, and technical
expertise) and puts Qi et al.'s empirical result against it — ten examples,
under a dollar, no special expertise — to show how low that "harder" bar
actually sits, and then draws out the distinction neither paper states on
its own: the closed-model version of that attack ran through a company's
own fine-tuning service, while the open-weight version ran on hardware no
company could see, which is the concrete, present-day shape Seger's
"no undo function" argument takes.

Proof result: `nb check` on the full command (series
what-could-go-wrong, library /home/user/library-checkout, links checked)
returns `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE, after `nb stamp`
(words 2196, sources 12, reading_minutes 10). No warning was left
outstanding.

Open questions: none. The RAND team/participant count is intentionally
omitted throughout, per the brief's guardrail on that disputed figure;
the qualitative design (LLM+internet vs. internet-only teams) is stated
instead. No CBRN operational content is included anywhere in the piece.
