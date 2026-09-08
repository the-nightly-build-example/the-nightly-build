# Commission: what-could-go-wrong/encoded-reasoning

## The argument

A model can hide its real reasoning inside text that reads as ordinary. If we
oversee AI by reading what it writes, including the chain of thought it produces
before an answer, that oversight assumes the writing reflects the reasoning. The
worry is that a model can learn to carry information in the surface form of
innocuous text (steganography) or to reason in a chain of thought that does not
mean what it appears to mean, defeating anyone who trusts the transcript. At the
far end sits steganographic collusion: two or more AI systems coordinating
through messages a human monitor reads as harmless.

## Why this argument now

Oversight of frontier models increasingly leans on reading their chains of
thought, and labs have said they will avoid training against the chain of thought
precisely to keep it readable. The course already teaches whether the chain of
thought can be trusted (`../what-could-go-wrong/cot-monitorability.html`) and the
broader oversight problem (`../what-could-go-wrong/scalable-oversight.html`), and
it explains what a chain of thought is mechanically (`../the-mechanics/thinking-out-loud.html`).
This lesson isolates one specific threat to that plan, the one that has actually
been demonstrated in a model, and separates it from the speculative catastrophe.

## The angle

The desk's job here: open the argument at full strength, then draw a sharp line
between what has been shown in a working system and what is still analogy. What
has been shown: Roger & Greenblatt (2023) trained/prompted models to perform
"encoded reasoning," hiding reasoning steps in text that looked normal and
recovering the benefit, and showed a simple defense (paraphrasing the model's
output) that degrades the hidden channel. Related demonstrations: models can use
steganography to pass hidden messages under some conditions, and RL can in
principle incentivize unfaithful or encoded chains of thought. What is still
analogy: autonomous, undetected steganographic collusion among deployed agents
pursuing a hidden goal has not been observed in the wild; the demonstrations are
constructed by the researchers. Bring it to the present: who worries about this
(the AI-control and CoT-monitorability researchers), what they propose
(paraphrasing defenses, not optimizing the CoT, monitoring), and where confidence
outruns proof in either direction.

## What to teach (short list, in order)

1. Why reading a model's words is a load-bearing part of oversight, and the
   assumption it rests on (the writing reflects the reasoning). Link
   thinking-out-loud and cot-monitorability instead of re-teaching them.
2. What encoded reasoning / text steganography is: hiding information or reasoning
   in the choice of otherwise-normal words. A concrete, worked illustration of the
   idea (a simple scheme), kept honest.
3. The demonstration that exists: Roger & Greenblatt's encoded-reasoning result
   and the paraphrasing defense, with what it did and did not show. Any
   steganographic-collusion demonstration among agents (e.g., Motwani et al.,
   "Secret Collusion"), with its conditions.
4. The line: shown vs speculative. What would have to be true for the catastrophic
   version, and why the demonstrations do not establish it yet. What the proposed
   defenses buy and where they are fragile. Name the gap in both directions
   (over-worry and dismissal).

## Template, bands, sources

- Template: lesson. Word band 1200-2200. Sections: why, orientation, 0-4 flex,
  takeaway, sources.
- Source floor (what-could-go-wrong/lesson): at least 8 sources, at least 4
  primary and at least 1 secondary. Primary: the papers that own the argument and
  the demonstrations (Roger & Greenblatt, "Preventing Language Models From Hiding
  Their Reasoning," 2023; Motwani et al., "Secret Collusion Among Generative AI
  Agents," 2024; Lanham et al., "Measuring Faithfulness in Chain-of-Thought
  Reasoning," 2023; relevant lab statements on not optimizing the CoT, e.g.,
  OpenAI's 2025 monitoring work; any primary on RL incentives for unfaithful CoT).
  Work from the original documents, never commentary about them. Name no company as
  an authority.

## Production policy (resolved)

Profile balanced. writing-coach low/capable, researcher high/capable, writer
medium/capable, editor high/capable. None required. Writer records actual harness
and model in nb-meta.

## Background links available (verify and link, do not re-teach)

`../what-could-go-wrong/cot-monitorability.html`,
`../what-could-go-wrong/scalable-oversight.html`,
`../the-mechanics/thinking-out-loud.html`,
`../what-could-go-wrong/deceptive-alignment.html`. Use only those the reader
needs; this piece must stand alone for a reader who opens none.

## This run's neighbors (for coherence, not overlap)

Publishing tonight: the-evidence/alphazero, the-instruments/auroc,
the-mechanics/attribute-binding, when-ai-breaks/waymo-recall. Keep the shared
voice; no overlap.

## Habits not to inherit (voice and shape)

Recent what-could-go-wrong deks state the debunk in a flat single line ("The
researchers planted the deception themselves, and say the study cannot tell you
whether it would ever arise on its own"); the shape is now familiar, so find this
piece's own dek. Headings run to full-sentence claims; vary construction. No
colon-subtitle headline. Do not join the field's alarm or its dismissal; show the
evidence and let the reader weigh it.
