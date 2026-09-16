# Commission: the-instruments/mean-opinion-score

## The measurement

Mean Opinion Score (MOS): the number reported for how natural or how good a
piece of synthesized speech sounds. The lesson teaches where this number comes
from and what it can and cannot support. The researcher confirms the standard,
the scale, and every cited figure before the writer uses them.

## Why this number, now

Every text-to-speech and voice-cloning release now reports a MOS, and the strong
ones use it to claim their synthetic voice reaches or passes human recordings.
The reader meets "human parity" and "4.5 out of 5" claims and has no way to check
them. MOS is unusually easy to misread because it looks absolute: a score on a
fixed 1-to-5 scale seems to mean the same thing everywhere. It does not. The
lesson gives the reader the one thing that lets them read a MOS claim correctly,
which is knowing what the number is a mean of and what it is not comparable
across.

## The declared reader and the fit

The reader is smart and has never run a listening test. Algebra and averaging
need no introduction; everything else is built up. Define the rating scale, the
listening-test setup, and any term of art (naturalness, the confidence interval
reported beside a MOS) where it first appears.

## What the lesson teaches (a short, complete list)

Teach in dependency order; cut rather than compress.

1. What MOS literally is: the arithmetic mean of listeners' category ratings on a
   fixed scale, standardized for this use. Name the standard that defines it and
   the labeled points of the scale. Give a worked example: a handful of ratings
   and the mean they produce, with the confidence interval that should travel
   with it.
2. Where the number comes from, step by step: who is recruited to listen, how
   samples are chosen and presented, and how the ratings are collected and
   averaged. Cover crowdsourced listening tests and the standard written for
   them, since that is how most current numbers are produced.
3. What the number can support: a within-test ranking of systems judged by the
   same listeners on the same samples under the same instructions.
4. What it cannot support, and the real case where it misled people. MOS is not
   an absolute, portable measure: it moves with the rater pool, the other systems
   in the test, the instructions, and the audio conditions. Show at least one
   real, cited instance where this bit: a "human parity" or cross-paper MOS
   comparison that treated two incompatible tests as one scale, including how the
   score of genuine human recordings itself varies from test to test. Say what
   the mistaken comparison cost or claimed.
5. What people do about it: comparison-based scoring, reporting confidence
   intervals and test conditions, and automatic MOS predictors, with an honest
   note on what each does and does not fix.

The original work is idea 4 made concrete: the reader should be able to look at
two papers each reporting a MOS and say why the two numbers cannot simply be
compared.

## Sources plan

Template and series floor: eight sources, at least four primary and one
secondary. Primary here is the standards body's own recommendation defining MOS
and the crowdsourced-test procedure, plus the speech-synthesis papers that report
the specific MOS figures the lesson cites (read their tables and test setups, not
their abstracts), and any peer-reviewed study measuring MOS reliability or its
cross-study variance. Secondary reporting may add context only. Every MOS figure
carries its scope: the scale, the number and kind of listeners, the samples, and
the systems compared.

## Continuity and neighbors

The library teaches other evaluation numbers, several of them subjective or human-
judged; link the closest one in Background rather than re-teaching what a
benchmark score is, and check its exact slug first. Word error rate is already a
lesson and measures a different thing (transcription accuracy, not perceived
quality); if it helps the reader separate accuracy from quality, link it. One of
tonight's other lessons is on watermarks in generated images, another kind of
generative-model output; keep this piece strictly about the speech-quality
number and its test, with no shared framing to blur them.

## Recent shapes to break

The Instruments has lately opened with a headline stating a surprising empirical
finding about the metric, then a dek that explains where the trust in it came
from. That mold is now visible across several pieces. Find this lesson's own
headline shape. Vary heading construction and avoid a neighbor's exact rhythm.

## Production record

Roles run on a capable-tier model (Claude Sonnet) via isolated subagents.
Effort per the balanced profile: researcher high, writer medium, editor high,
writing-coach low. No required directive was traded down.
