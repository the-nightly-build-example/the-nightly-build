# Voice guide: top-5 accuracy on ImageNet

## How this piece should sound

This is a lesson on one number: top-5 accuracy on ImageNet, written for a reader who is sharp and widely read but has never touched a computer-vision benchmark. The work is to build the number in front of them — the 1,000 classes, the single ground-truth label per image, the rule that counts a hit when any of the model's five guesses matches that one label — and then show, plainly, which comparisons the number can carry and which it cannot. Hold the register Kyle Hewitt holds on the p-value: define the quantity on a concrete instance the moment it appears, and treat the reader as someone smart who has simply never had it explained.

The move worth borrowing first is the one Bergstrom and West make with the barbecue ranking, where two sentences say what the average score actually measures and then name the comparison it cannot make. The same shape is available here: a reader can be shown exactly what top-5 accuracy counts before being shown the distance between that and "the model recognized the image." Keep that separation concrete. When the score and the thing people read into the score come apart, say what each one is in the image's own terms, the way the barbecue piece keeps naming Seattle and Fort Worth so the swap stays visible.

The metric can be taught through a single example image the way Hewitt teaches the p-value through one worked value and Roser teaches growth through one worker and one printing press. An image the reader can actually picture, carried across the lesson, will do more than the 1,000-class task defined in the abstract. Let real numbers do the explaining where they can, and give a figure its plain-language handle, as Hewitt does with "the luck of sampling," so a term of art never lands without something the reader already holds.

The tone leans toward Roser's steadiness more than the barbecue piece's wryness. The register is a serious daily's, so credit the metric for what it was built to do before showing where it stops: top-5 was a deliberate choice by the people who ran the challenge, and the lesson reads more fairly when the reader can see why someone reasonable would pick it. When a computer-vision term would take a sentence up to an abstraction, name it plainly and move on, as Roser does when he calls a measure abstract. A wry line survives here only where it depends on ImageNet's own nouns, the way "order the salmon" depends on Seattle; a line that would fit any benchmark is the kind this paper cuts.

Where the piece has room, the misled case can be one reader making one identifiable mistake. Hewitt earns his correction by naming the exact misreading a person was about to make; the equivalent here is the specific claim a stated ImageNet number gets used to support, set beside what that number, built the way the lesson just built it, actually licenses.

## Carl Bergstrom and Jevin West, "America's Best Barbecue?"

Source: https://callingbullshit.org/case_studies/case_study_barbecue.html

> "What went wrong? So many things. It's hard to even know where to start. But let's focus on the single biggest issue: the data collected are not appropriate to answer the question at hand."

The passage picks one problem out of many and names it in a plain declarative sentence, after openly admitting there are too many to list. The short fragments, "So many things. It's hard to even know where to start," let the reader hear a person deciding where to begin. The diagnosis is taught by stating it, not by decorating it.

> "So what these data tell us is that people in Seattle rate Seattle barbecue higher than people in Fort Worth rate Fort Worth barbecue places. We don't know how people in Seattle would rate Fort Worth barbecue, or how people in Fort Worth would rate Seattle barbecue."

These two sentences are the whole critique: the first says what the average score measures, the second names the comparison the score cannot make. The writers repeat the same two place names so the reader can follow the swap without a chart. The distance between what a number records and what people read into it is carried by words a newcomer already has.

## Max Roser, "What is economic growth? And why is it so important?"

Source: https://ourworldindata.org/what-is-economic-growth

> "Poverty, prosperity, and growth are often measured in monetary terms, most commonly as people's income. However, while monetary measures have some important advantages, they have the big disadvantage of being abstract."

Roser states the common measure and its main weakness in two sentences and softens neither. He credits the measure before he faults it, so the reader takes the criticism as fair rather than as an attack. He calls the abstraction abstract and moves on instead of performing around it.

> "Gutenberg developed a new production technology, and it changed things dramatically. Instead of spending months to produce one book, a worker was now able to produce several books a day. As the printing press spread across Europe, book production soared."

A general idea, productivity growth, is taught through one worker, one product, and a before-and-after count. Roser picks the printing press because the reader can already see it, and the contrast between "months" and "several books a day" does the explaining. The concrete case comes first and the idea rests on it.

## Kyle Hewitt, "What is a p-value? An expert explains the most misunderstood number in science"

Source: https://theconversation.com/what-is-a-p-value-an-expert-explains-the-most-misunderstood-number-in-science-288491

> "If you've ever tried to read a scientific paper, you've almost certainly run into a p-value. And if you found it confusing, you're in good company: plenty of working scientists misunderstand it too."

The opening meets the reader at the point of confusion and tells them the confusion is common, which reassures someone who has just met the term. It makes a claim the piece then has to support, that experts misread the number too, rather than promising a tour. The second person appears once, to include the reader, and is then dropped.

> "To find out, a scientist runs a statistical test which returns a p-value (the 'p' is often understood to stand for 'probability'). Say it comes back as p = 0.06. Here is what that means: if there were genuinely no difference between the countries, a gap at least this large would turn up about 6% of the time through the luck of sampling."

The definition arrives on one worked number inside a running two-country example, so the abstract quantity has something concrete attached the instant it is named. Hewitt writes the conditional out in full rather than compressing it, because the compression is exactly where readers go wrong. The plain phrase "the luck of sampling" delivers the technical idea without a technical word.

> "Now notice what it does not mean. It does not mean there is a 6% chance the result was a fluke, or a 94% chance the two countries really differ. The p-value tells you how likely a difference this big is if nothing real is going on, not how likely it is that nothing real is going on."

Having defined the number, Hewitt immediately names the two ways people misread it, in the reader's own word, "a fluke." The last sentence places the right reading next to the wrong one using the same clause twice with the terms reversed, so the difference is visible in the sentence itself. The correction lands because the misreading it names is the one the reader was about to make.
