# Tools

Genetic algorithms bas themselves on natural selection, meaning the reproductive advantage of an individual that fits better in said environment.
They make use of tools inspired by biology allowing the specie to evolve through generations.

## Selection

This tool resemble the [natural selection](https://en.wikipedia.org/wiki/Natural_selection).

![The giraffes able to eat high leaves are better at surviving](/img/Selection.svg "The giraffes able to eat high leaves are better at surviving")

Each individual gets a fitting score, depending on the given problem.
In this step, we will select individuals in order to create the next generation.
This selection can be done that way :
 * A well fitted individual (high fitting score) has good chances at being selected
 * The lesser the fitting score, the lesser the chances at being selected

The first thing to do is to create a fitting function. It will score each individual.
The function generally returns a floating number between 0 (bad score) and 1 (good score).

In this exercise, you will implement the fitting function. We will simply compare the chromosome with the solution.

@[Fitting function]({"stubs":["fitting.py"], "command":"tools_tests.FittingTest", "project":"exercice2"})

Once the fitting function has been defined, we can apply a selection on our population.
The goal is to keep the best fitted individuals.

An example of selection function would be :
 * Select the best 30% individuals
 * Randomly select 20% of the rest

If only the best ones were to be kept (elitism), the risk is to head towards a local minimum without having the possibility to explore other potentially rewarding ways.

In the next exercise, we will implement the selection function.

@[Chromosoms selection]({"stubs":["selection.py"], "command":"tools_tests.SelectionTest", "project":"exercice2"})

## Genetic operators
These tools will directly impact the genetic material of a new individual.

### Crossover / reproduction
We now need to fill our population with a new generation.
In order to create this generation, we will make individuals reproduce.
During this step, the parents will be exchanging their genetic material to produce a child [Genetic recombination](https://en.wikipedia.org/wiki/Genetic_recombination)

![Crossover of two chromosoms](/img/OnePointCrossover.scg "Crossover of two chromosoms")

A solution is to take each parent 50% of their genetic material, making the crossover in the middle of the chromosome.
For instance if the parents are `ABCDEFGH` and `1345678`, the child will be `ABCD5678`.
There is no change in the genes' places.

There are other types of crossovers. 
One can take 70% of the genetic material of a parent and 30% of the other.
Or we could do the crossover on multiple locations.

![Two-points crossover](/img/Computational.science.Genetic.algorithm.Crossover.Two.Point.svg "Two-points crossover")

@[Chromosome crossover]({"stubs":["croisement.py"], "command":"tools_tests.CroisementTest", "project":"exercice2"})

### Mutation
In order to create new genetic material, some individuals will [mutate](https://en.wikipedia.org/wiki/Mutation).
A gene will randomly be mutated.

![Gene mutation](/img/mutation.png "Gene mutation")

@[Mutation]({"stubs":["mutation.py"], "command":"tools_tests.MutationTest", "project":"exercice2"})