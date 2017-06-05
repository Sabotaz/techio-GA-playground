import random
from solution import get_score
    
def score(chrom):
    # nombre flottant compris entre 0 et 1 suivant si le chromosome est mauvais ou bon
    # c'est la fonction qui a été codée à l'exercice précédent
    return get_score(chrom)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # pourcentage des meilleurs individus retenus
    NONGRADED_RETAIN_PERCENT = 0.2  # pourcentage d'individus retenus aléatoirement parmis les individus restants
    # TODO: implémenter la fonction de sélection
    #  * trier les individus selon leur adaptation
    #  * sélectionner les meilleurs individus
    #  * sélectionner aléatoirement d'autres individus
    return []
