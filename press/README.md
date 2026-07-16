# The AI Reader

This directory is the paper's side of the repository. Everything outside it is
the updateable engine.

The opening term has six daily desks, published in this reading order:

1. AI Foundations
2. Mathematical Intuition
3. History of AI
4. Transformers from First Principles
5. Canon Papers
6. AI in the World

Each desk is a 28-item sequence. Before the final items are published, append
the next synchronized term to every sequence; published items are permanent and
the engine will continue with the newly appended tail. Change the paper-wide
reader model in `editorial.md`, an individual desk's scope in its `prompt.md`,
and mechanics such as cadence or source floors in `series.yaml`.
