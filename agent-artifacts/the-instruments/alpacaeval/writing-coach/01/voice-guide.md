# Voice guide: the-instruments/alpacaeval (01)

## How this piece should sound

The lesson takes one number that model releases quote, an AlpacaEval win rate, and shows a reader new to benchmark mechanics how it is made and where it misleads. Keep the register plain, the way Matt Yglesias is plain when he explains something he knows well. Define each part as the procedure reaches it: the judge model, the reference answers it compares against, the fixed set of instructions, and the share of those instructions the judge prefers. Where the lesson walks through how the win rate is computed, let the reader follow the count in the order the procedure runs, the way Julia Evans lets a reader watch 4096 times 658 come out to a number they could check. By the end the reader should be able to say, in their own words, what a win rate counts.

The lesson documents a length preference in this judge, and it still treats the win rate as a number worth reading. Hold the balance Tim Harford holds when he warns that scepticism should not curdle into cynicism and still calls statistics a vital tool. Showing the bias is in service of reading an AlpacaEval number well. It is not a case for treating every reported number as worthless. The reader should finish more careful with a reported win rate and still willing to use one.

When the lesson names the length preference, name it in AlpacaEval's own parts, the judge model reading two answers to the same instruction and preferring the longer, the way Dan Luu names higher speed USB polling instead of calling old keyboards bad. Keep separate names for the two cases a win rate can hide, a model the judge genuinely prefers and a model that wins by length, so a reader never has to guess which one a number shows. Any verdict the lesson reaches, such as when two reported win rates can be set side by side, belongs after the judge, the reference, and the length handling behind them have been shown, so the verdict rests on what the reader has seen.

The size of the length effect and the correlation with human preference each hold under a stated scope, one judge, one reference, one set of instructions. Give that scope plainly and let the figures keep it. When the lesson reaches its surprise, that a win rate is a judge's preference under a known length bias, say it in plain words. The desk has lately staged this kind of finding as a reveal of two numbers that disagree, and opened lessons by touring their own sections; this lesson needs neither.

## Tim Harford, "How to Truth with Statistics"

Source: https://timharford.com/2022/01/how-to-truth-with-statistics/

> "That weakness is Huff's tendency to make statistics seem like a game, a stage magician's trick, all good fun but never to be trusted. I worry that we're starting to trust nobody; we're starting to believe that lying with statistics is all anyone ever does. Huff does not help."

Harford names a specific fault in Huff's book, that it makes statistics look like a magician's trick you should never trust, then states his own worry, that readers are coming to believe every statistic is a lie. The three short sentences run from the book to the reader to a flat two-word judgment, "Huff does not help." The worry is his, said in the first person.

> "Scepticism is all very well, but not if it curdles into cynicism. Statistics can be used to deceive but they are also a vital tool in our quest to understand the world around us, like a telescope for an astronomer."

Harford marks the line between scepticism and cynicism in a single sentence, then says what statistics are for, understanding a world too large to see directly. He grants that statistics can deceive in the same breath that he calls them vital. The telescope comparison states the use in plain terms without leaving the sentence.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> "The implication for the former is that measuring is less valuable than building and for the latter that measuring isn't valuable at all (perhaps other than for fame), but I don't see measuring as lesser let alone worthless. If anything, because measurement is, like writing, not generally valued, it's much easier to find high ROI measurement projects than high ROI building projects."

Luu gives his view outright, that he does not see measuring as lesser let alone worthless, and puts the reason in the same sentence, that measurement is under-valued and so its projects have higher returns than building. The reason sits next to the verdict rather than in a separate line of support. A reader hears someone who has done these measurement projects and formed a view about them.

> "I'm reminded of the SRE motto, "hope is not a strategy". Trusting vendors is not a strategy. We know that vendors will lie and cheat to look better at benchmarks. Saying that it's a vendor's fault for lying or cheating can shift the blame, but it won't result in reviews being accurate or useful to consumers."

Luu states a flat verdict, that trusting vendors is not a strategy, and the sentences after it say why: vendors lie and cheat to look better at benchmarks, and blaming them does not make a review accurate. Each short sentence carries one claim before the next begins. The reader meets someone who has read enough reviews to stop trusting a vendor's supplied copy.

> "Now, every major manufacturer of gaming keyboards and mice has fairly low latency devices available whereas, before, companies making gaming devices were focused on buzzword optimizations that had little to no impact (like higher speed USB polling)"

Luu names the exact thing that did not work, higher speed USB polling, and calls it a buzzword optimization with little to no impact, instead of calling the older devices bad. The named detail is what makes the dismissal credible. He is present as the person who measured keyboard latency and saw which changes moved it.

## Julia Evans, "Behind "Hello World" on Linux"

Source: https://jvns.ca/blog/2023/08/03/behind--hello-world/

> "Now, we need to calculate how many bytes into our hard drive "block 658, offset 0x0d00" is on the big array of bytes that is your hard drive. Each block is 4096 bytes, so we need to go 4096 * 658 + 0x0d00 bytes. A calculator tells me that's 2698496"

Evans works the number in front of the reader: block size times block number plus the offset, then the result, 2698496. She writes that a calculator tells her the answer, so the figure reads as something she computed and the reader could compute again. Nothing about the number is presented as handed down.

> "Every file is made up of a bunch of blocks on the hard drive. I think each of these blocks on my system is 4096 bytes, so the minimum size of a file is 4096 bytes – even if the file is only 5 bytes, it still takes up 4KB on disk."

Evans states how a file sits on disk in one plain sentence, then pins it to a number, a 5-byte file still taking 4096 bytes. She writes "I think each of these blocks on my system is 4096 bytes," marking what she has checked against what she is estimating. A reader can tell the sure part from the guess.
