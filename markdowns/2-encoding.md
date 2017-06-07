# Individuals, chromosoms and genes

![Human chromosome 16 genes](/img/Human_chromosome_16_with_ASD_genes_from_IJMS-16-06464.png "Human chromosome 16 genes")

A human has several chromosoms, each carrying thousands of genes. Likewise, in our model, each individual is to be represented by its genes, organised in chromosomes. For the sake of readability,
we will use either "chromosome" or "individual" to refer to the genetic material of an individual.

In analogy with the evolution theory, these algorithms are based on the evolution of a population over time.

# Overview

A genetic algorithm consist in the following steps :
 * Creation of the base population
 * Individual evalution (is the individual fit to solve the problem ?)
 * Individuals seletion (the more fitting an individual, the more survival chances)
 * Crossover / reproduction (Crossover of two individuals creates a new individual whose genes comes from both parents)
 * Mutation (Some of the children's genes can mutate to create new genes)

## The problem
Let's take a concrete example.
This exercise consist in guessing a character string like `My password is hard !` or `IQlCqnWXVoVDDRFKFevaFzxmUxTxONwlLSwfkxmG`.
Authorised characters are :
```python
alphabet = string.ascii_letters + " !'."
```
There are 56 authorised characters. For a 100 characters long string, we would need $`6.59.10^{+174}`$ tries to test every possible solution !

Bruteforcing it would be inefficient. Instead, we will try to guess the solution from two informations :
 * The string length
 * The fitting score of each solution (comprised between 0 and 1; The closer to 1, the better the solution is)

# Creation of the base population
 
The first step is to create individuals for our base population.

A chromosome is a set of genes. We could encode it in different ways :
 * A binary encoding : a binary string (set of 0s or 1s)
 * multiple characters encoding : a string of characters

On the crossover step, we seek to have a wide genetic recombination. The binary encoding has a finer granularity for the creossing location but is not really natural and not fit for real data (for instance, modifying a certain bit in a floating number can result in invalid values).

In practice, we will use a different encoding regarding the problem to solve.

 * The Knapsack problem :

> ![Knapsack problem](/img/Knapsack.png "Knapsack problem")
> The Knapsack problem : What boxes do we choose in order to maximize the carried weigth without exceeding 15kg?

`0110001`, each bit is refering to an object and indicates if it has been placed in the bag.

 * Steer a robot [(mars lander)](https://www.codingame.com/training/easy/mars-lander-episode-1) :

> ![Mars Lander : simulation](/img/marslander.png "Mars Lander : simulation")
> ![Mars Lander : console](/img/ControlPanel.png "Mars Lander : console")
> The goal is to land, without crashing it, the capsule "Mars Lander" which holds the rover Opportunity.

`[float, int, float, int, loat, int...]` the angle (-90° to 90°) and the rocket thrust (0 to 4) on each turn.

 * Find a string of characters :

`"Aoljfon oaeznFjlf"`, each character in the string is to be found.

In the following exercise, you will code the function creating a new individual. The chromosome will be stored as a string.

@[chromosome encoding]({"stubs":["encoding.py"], "command":"encoding_tests.ChromosomeTest", "project":"exercice1"})