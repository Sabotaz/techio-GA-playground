
import random
from secret import est_solution
# Vous pouvez redéfinir ces fonctions avec celles que vous avez écrites précédemment.
# Une implémentation différente est fournie.
from codage import creer_chromosome
from tools import selection, croisement, mutation

size = int(input())
population = 0

def creer_population():
    chrom = creer_chromosome(size)
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
    creer_population()
    
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
    