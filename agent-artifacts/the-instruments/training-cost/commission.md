# Commission: the-instruments/training-cost

## The measurement

The dollar cost of training a frontier model: the headline figure of the form
"this model cost $X million to train." The anchoring case is DeepSeek-V3, whose
December 2024 technical report put the training cost of its final run at about
US$5.576 million. The lesson teaches how that kind of number is made, what it
includes and excludes, and the one time it moved the world.

## The angle

A training-cost dollar figure looks like a fact about a company's budget. It is
an arithmetic construction: a count of GPU-hours multiplied by an assumed rental
price per GPU-hour, scoped to one training run. Teach where the number comes from
step by step, then show the real case where reading it as a full budget cost
people enormous sums.

Teach these, in an order the writer sets from the evidence:

- **What the number is, exactly.** From DeepSeek-V3's report: the model used about
  2.788 million H800 GPU-hours for its full training, and the report assumes a
  rental price of US$2 per GPU-hour to reach roughly US$5.576 million. Get every
  figure from the primary (the DeepSeek-V3 technical report / arXiv): the
  GPU-hours, the assumed $2 rate, the resulting total, and the breakdown into
  pre-training, context extension, and post-training if the report gives it.
- **How the number is built.** GPU-hours × assumed price per GPU-hour. Teach that
  both inputs are choices: the hour count is measured for one run, and the price
  is an assumption about what an hour of that hardware costs to rent, not what the
  company paid. Make the arithmetic concrete with the real figures.
- **What it excludes.** State plainly, from the report's own words, what DeepSeek
  said the figure does not cover: prior research, ablation and architecture
  experiments, data, and the salaries of the people. It is the cost of the final
  successful run's compute, not the cost of the model program. Where a credible
  primary or well-sourced secondary estimates the excluded costs (e.g. the capital
  cost of the GPU fleet DeepSeek's parent reportedly owns), report it as an
  estimate with its owner, kept distinct from the reported figure.
- **The case where the number misled, and what it cost.** On Monday 27 January
  2025, US and global tech stocks sold off sharply on the DeepSeek news; Nvidia
  fell about 17 percent in one session, a loss of roughly US$589–600 billion in
  market value, reported as the largest single-day market-value loss for one
  company in US history. Much of the coverage that drove the move read the $5.6M
  as the all-in cost of building a GPT-4-class model, i.e. as evidence that
  frontier AI had suddenly become cheap. Get the Nvidia percentage and dollar
  figure from a primary market source or the company's own filings where possible,
  and attribute the "$5.6M is not the whole cost" correction to primaries
  (DeepSeek's own report caveat, and named analysts who said so at the time).

## Required contribution

The evidence carries the figures. This piece's own work is to take the single
number everyone repeated, $5.6 million, and show its two hidden inputs (a
measured hour-count for one run and an assumed rental price) and its scope (final
run only), then set that against the roughly half-trillion dollars of market value
that moved partly on reading it as something it never claimed to be. The reader
should leave able to ask of any "$X million to train" figure: whose hours, at
what assumed price, and which run.

## Boundaries

- The subject is the dollar cost figure and how it is constructed and misread. It
  is not a DeepSeek company profile and not a rehash of the DeepSeek-R1 reasoning
  method (covered) or the parameter counts (covered). Link, do not re-teach:
  training compute measured in FLOPs, GPU-hours as a throughput idea, and
  per-token price are separate existing lessons; reference them in Background
  rather than re-explaining. The researcher should surface the best links.
- Keep reported fact, estimate, and synthesis distinct, as the standard demands.
  The $5.576M is reported; any all-in figure is an estimate; the claim that the
  market misread it is synthesis that must be shown, not asserted.
- No hype and no doom. Do not editorialize about whether DeepSeek "won." Report
  the number, its construction, and the market event.
- Name no company as an authority. Nvidia and DeepSeek are subjects here.

## Source policy (the-instruments / lesson)

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primaries:
the DeepSeek-V3 technical report (the figure and its caveats), and a primary or
authoritative source for the Nvidia market move (exchange data, Nvidia filing, or
the clearest reporting of the close). Contested figures (excluded costs, GPU
fleet value) need a primary or a clearly-labeled estimate with its owner.

## Production policy

Profile balanced. Roles run as Claude Code sub-agents using this checkout's `nb`.
Model "capable" for every stage. Actual models this run: writing-coach sonnet
(low), researcher opus (high), writer sonnet (medium), editor opus (high). No
`required` directive to deviate from.

## Recent-pattern habits not to inherit

- The-instruments openers often begin "A number for how well X" / "What the
  number is"; several section headings take the mold "The number is the model
  plus the effort." Name headings for this lesson's own steps and vary the
  construction.
- Closer headings shaped "What a high score does not promise" / "Where the same X
  lives" recur. Write this lesson's closer around its own particulars (the
  $5.6M-versus-market-cap gap), not a stock construction.
- `spec/headlines.md` bans the comma-triad and semicolon-reversal dek molds.
  Recent deks lean on figure-packed two-sentence forms; commit the dek to this
  lesson's specific find.

## Neighboring articles in tonight's run (keep distinct)

the-evidence/computing-machinery-and-intelligence; the-mechanics/
text-to-speech-pronunciation; what-could-go-wrong/recommender-radicalization;
when-ai-breaks/amazon-recruiting. This is tonight's only measurement/number
piece.
