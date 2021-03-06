# Algorithm
## Algorithm overview

1. Create the base population
We create a random initial population. Each individual is is defined by its genetic material.
We create a new individual with the previously declared `create_chromosome(size)` function.
2. Evaluation
Each individual is scored on its fitting to the problem. This is done in the beginning of the selection.
3. Selection
Each individual has a chance to be retained proportional to the way it fits the problem.
We only keep the selected individuals returned by the `selection(population)` function.
4. Crossover / reproduction
Random couples are formed in the selected population. Each couple produces a new individual.
The number of individuals in the population can either be constant or vary over time.

On each reproduction :
 * Crossover
The genetic material of a child is a combination of the parents' (generally 50% of each parent's genetic material).
Once the parents have been chosen the ``crossover(parent1, parent2)` function allows the creation of the child.
 * Mutation
Probability : from 0.1% to 1%
Each child have a chance to have a randomly modified gene thanks to the `mutation(chromosome)` function.

Finally, the `is_answer(chromosome)` function checks if the individual is solution to the problem (100% score).
If there is no solution, we go to the next generation (phase 2).

![Recap](/img/Schema_simple_algorithme_genetique.png "Recap")

The goal of this exercise is to find the secret sentence using a genetic algorithm and the tools we created earlier.

@[Genetic algorithm]({"stubs":["algorithm.py"], "command":"algorithm_test.AlgorithmTest", "project":"projet", "layout": "aside"})
