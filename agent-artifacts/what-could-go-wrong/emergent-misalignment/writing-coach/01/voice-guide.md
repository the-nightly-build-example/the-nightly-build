# Voice guide: what-could-go-wrong/emergent-misalignment (01)

## How this piece should sound

This lesson teaches one contested result to a reader who is quick and widely read but has never run a finetuning job and cannot check the papers for themselves. It puts a real worry at full strength, holds that worry against what particular models actually did once they were finetuned, and keeps the measured result apart from what the result is taken to imply. The register is plain and explanatory, the voice of someone walking a reader through evidence they will weigh for themselves.

Give the worry its strongest form before testing it, the way Ritchie writes "I agree ... I agree" before he disagrees and the way Yong hands the sharpest doubts to named researchers. The claim that finetuning a model to do one narrow bad thing can make it broadly bad is most convincing when the reasoning a careful defender would give is fully on the page, rather than a weak version assembled to be knocked down.

Let the numbers stand on their own. Yong writes "97 percent ... just 36 percent" and glosses a p-value in the same sentence; Alexander gives raw counts like "86 hospitalizations vs. 95"; Ritchie reports an effect of "absolutely zero" in the same flat voice he uses for the positive ones. The measured rates of misaligned responses across conditions, and which models and which finetuning data produced them, can be figures the reader holds directly, carrying no adjective that tells them how alarmed to be.

Keep the seam between what was shown and what is inferred inside the sentences. Yong's "Does this mean ... ? Not quite" turns a headline number back into a question before he extends it. As the piece moves from what the insecure-code finetuning demonstrably produced to what it might mean for models nobody trained this way, the reader should be able to see where the demonstrated result ends and the extrapolation starts.

Say plainly where the evidence runs out, as Ritchie does when he lists the open questions and then writes "We don't know yet" without softening it. Whether broad misalignment shows up without deliberate finetuning, and how much its size varies across GPT-4o and the other models, can be left standing as open questions where the work itself leaves them open.

Show the weighing instead of announcing a verdict. Alexander bounds a study he half-trusts between its two extremes and admits that his own analytic choices moved the p-value, and the reader believes the reading because the steps are on the page. Where the effect is strong under one finetuning setup and faint under another, or where a backdoor trigger or a steerable persona direction cuts against the simple story, the piece can show how it reaches its reading.

Define each unfamiliar term as it arrives, the way Ritchie sets down the decline effect in a single sentence and Yong explains effect size mid-clause. Finetuning, a held-out prompt, a backdoor, a latent persona direction: each can go into plain words the first time it is used, so a reader meeting it for the first time never has to carry an unexplained term.

## Scott Alexander, "Ivermectin: Much More Than You Wanted To Know"

Source: https://www.astralcodexten.com/p/ivermectin-much-more-than-you-wanted

> "I think this paper is legitimate and that its findings need to be seriously considered. Serious consideration doesn't always meant they're true - sometimes if we have strong evidence otherwise we can dismiss things without understanding why. And there's always the chance it was a fluke, right? Can something have a p-value less than 0.001 and still be a fluke?"

He separates two things a reader usually runs together: that a study is well-run and deserves to be taken seriously, and that its result is true. The questions at the end are ones he actually goes on to answer, so you watch him deciding how much to believe rather than being told a conclusion.

> "I guess all we can do is try to bound the damage. Even if the confounding is 100% real and bad, there's no way to make this study consistent with the crazy super-pro-ivermectin results of studies like Espitia-Hernandez and Aref. And even if we deny any confounding, we see the same slight pro-ivermectin trend - 86 hospitalizations vs. 95 - that we've seen in so many other studies."

Faced with a study he cannot fully trust, he neither accepts nor discards it; he works out what it can support at each extreme and reports the raw counts, 86 against 95, so the reader sees how small the effect is. The reasoning is all on the page, which is how the reader follows him to a middle position instead of being handed one.

> "Now it's p = 0.04, seemingly significant, but I had to make some unprincipled decisions to get there. I don't think I specifically replaced negative findings with positive ones, but I can't prove that even to myself, let alone to you."

He tells the reader that the result only crossed the significance line because of judgment calls he made, and that he cannot fully clear himself of bias. The admission is specific, about which choices moved the number, rather than a general disclaimer, and that specificity is what makes the rest of his analysis trustworthy.

## Ed Yong, "How Reliable Are Psychology Studies?"

Source: https://www.theatlantic.com/science/archive/2015/08/psychology-studies-reliability-reproducability-nosek/402466/

> "Does this mean that only a third of psychology results are "true"? Not quite. A result is typically said to be statistically significant if its p-value is less than 0.05—briefly, this means that if you did the study again, your odds of fluking your way to the same results (or better) would be less than 1 in 20."

He states the striking figure, then immediately asks whether it means what it looks like it means, and defines the p-value in a single plain clause so a lay reader can follow the rest. The definition sits inside the sentence rather than in a sidebar, and Yong's care shows in his refusal to let the number carry more than it can.

> "But even though the project is historic in scope, its results are still hard to interpret. Let's say that only a third of studies are replicable. What does that mean? It seems low, but is it? "Science needs to involve taking risks and pushing frontiers, so even an optimal science will generate false positives," says Sanjay Srivastava, an associate professor of psychology at the University of Oregon. "If 36 percent of replications are getting statistically significant results, it is not at all clear what that number should be.""

Instead of telling the reader what the replication rate proves, he gives the doubt to a named researcher who explains why even a healthy science would fail to replicate some results. Attaching the uncertainty to a specific person, with his title and field, is how the piece stays even-handed without going vague about who is unsure.

> "More generally, failed replications don't discredit the original studies, any more than successful ones enshrine them as truth. There are many reasons why two attempts to run the same experiment might produce different results. There's random chance. The original might be flawed. So might the replication."

He lays out the ordinary reasons two runs of an experiment can disagree and keeps them apart, giving none of them more weight than the evidence allows. The short flat sentences do the teaching, and his refusal to let a failed replication settle the question is visible in the first line.

## Stuart Ritchie, "How growth mindset shrank"

Source: https://www.sciencefictions.org/p/growth-mindset-decline

> "I have mixed feelings about this. On the one hand, I agree that effects of smaller size are to be expected in the real world; I agree that large effects, particularly for psychology-based interventions, but for tons of other things too, generally don't exist in educational research."

Before he pushes back on the proponents, he grants the part of their defense that is genuinely right, in his own words and at some length. Conceding the strong version of the other side is what earns the disagreement that follows, and you can hear him working to be fair rather than to score a point.

> "So, do mindset interventions only work in the US? Only online? Only in older adolescents rather than younger kids? We don't know yet. We should be open-minded, but in all the wrangling over the what and where of the effect, one thing is for sure: growth mindset doesn't have the enormous effect that it sounds like it has in Dweck's TED Talk."

He lists the questions the evidence has not answered, says plainly that they are unanswered, and then names the single thing that is now settled. Keeping the open questions and the settled point in separate sentences is what lets the reader see exactly how far the result reaches and no further.

> "The decline effect is the idea that scientific findings get smaller over time. That is, initial findings tend to report effect sizes that then crumble away—sometimes to nothing—with subsequent research. You can see how this presages the replication crisis, which is all about later scientists being unable to find the same, or the same-sized, findings as earlier ones."

He introduces a term by defining it in the same sentence, then restates it more concretely with "That is," so no reader is left behind. The explanation assumes no prior knowledge and still moves quickly, which is how a specialist writes for a general audience without talking down.
