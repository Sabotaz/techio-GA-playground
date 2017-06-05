import random
import sys
from solution import est_solution, get_mean_score
# Vous pouvez redéfinir ces fonctions avec celles que vous avez écrites précédemment.
# Une implémentation différente est fournie.
from codage import creer_chromosome
from tools import selection, croisement, mutation

def creer_population(pop_size, chrom_size):
    # on utilise la fonction creer_chromosome(chrom_size) créée précédemment
    # TODO: créer la population
    chrom = creer_chromosome(chrom_size)
    return ???
    
def generation(population):
    
    # sélection
    # on utilise la fonction selection(population) créée précédemment
    select = selection(population)
    
    # reproduction
    # tant que notre population n'a pas la bonne taille, on complète notre population par des enfants
    children = []
    # TODO: implémenter la reproduction
    while len(children) < ???:
        ## croisement
        parent1 = ??? # choisi aléatoirement
        parent2 = ??? # choisi aléatoirement
        # on utilise la fonction croisement(parent1, parent2) créée précédemment
        enfant = croisement(parent1, parent2)
        
        ## mutation
        # on utilise la fonction mutation(enfant) créée précédemment
        enfant = mutation(enfant)
        children.append(enfant)
    
    # retourner la nouvelle génération
    return select + children

def algorithme():
    chrom_size = int(input())
    population_size = ???
    
    # créer la population
    population = creer_population(population_size, chrom_size)
    
    solutions = []
    
    # tant qu'une solution n'est pas trouvée:
    while not solutions:
        ## créer la generation suivante
        # TODO: créer la génération suivante à l'aide de la fonction generation(population)
        population = ???
        
        ## on affiche le score moyen de notre population (on voit que ça progresse ! )
        print(get_mean_score(population), file=sys.stderr)
    
        ## vérifier si une solution est trouvée
        for chrom in population:
            if est_solution(chrom):
                solutions.append(chrom)
    
    # TODO: afficher la solution
    print("SOLUTION")
    