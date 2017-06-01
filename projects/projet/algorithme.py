import random
from solution import est_solution
# Vous pouvez redéfinir ces fonctions avec celles que vous avez écrites précédemment.
# Une implémentation différente est fournie.
from codage import creer_chromosome
from tools import selection, croisement, mutation

def creer_population(pop_size, chrom_size):
    chrom = creer_chromosome(chrom_size)
    return []
    
def generation(population):

    # sélection
    select = selection([])
    
    # reproduction
    ## croisement
    parent1 = bytearray()
    parent2 = bytearray()
    enfant = croisement(parent1, parent2)
    
    ## mutation
    mutation(bytearray())
    
    # retourner la nouvelle génération
    return []

def algorithme():
    # créer la population
    chrom_size = int(input())
    population_size = 0
    
    creer_population(population_size, chrom_size)
    
    solutions = []
    
    # tant qu'une solution n'est pas trouvée:
    while not solutions:
    ## créer la generation suivante
        generation([])
    
    ## vérifier si une solution est trouvée
        if est_solution(bytearray()):
            solutions.append(bytearray())
    
    # afficher la solution
    print("SOLUTION")
    