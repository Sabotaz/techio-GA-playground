import random
import sys
from solution import est_solution, get_mean_score
# Vous pouvez redéfinir ces fonctions avec celles que vous avez écrites précédemment.
# Une implémentation différente est fournie.
from codage import create_chromosome
from tools import selection, crossover, mutation

def create_population(pop_size, chrom_size):
    # use the previously defined create_chromosome(size) function
    # TODO: create the base population
    chrom = create_chromosome(chrom_size)
    return ???
    
def generation(population):
    
    # selection
    # use the selection(population) function created on exercise 2
    select = selection(population)
    
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    # TODO: implement the reproduction
    while len(children) < ???:
        ## croisement
        parent2 = ??? # randomly selected
        parent1 = ??? # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        enfant = crossover(parent1, parent2)
        
        ## mutation
        # use the mutation(enfant) function created on exercise 2
        enfant = mutation(enfant)
        children.append(enfant)
    
    # return the new generation
    return select + children

def algorithm():
    chrom_size = int(input())
    population_size = ???
    
    # create the base population
    population = create_population(population_size, chrom_size)
    
    solutions = []
    
    # while a solution has not been found :
    while not solutions:
        ## create the next generation
        # TODO: create the next generation using the generation(population) function
        population = ???
        
        ## display the average score of the population (watch it improve)
        print(get_mean_score(population), file=sys.stderr)
    
        ## check if a solution has been found
        for chrom in population:
            if est_solution(chrom):
                solutions.append(chrom)
    
    # TODO: print the solution
    print("SOLUTION")
    