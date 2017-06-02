import random
from solution import get_score
    
def score(chrom):
    # nombre flottant compris entre 0 et 1 suivant si le chromosome est mauvais ou bon
    return get_score(chrom)
    
def selection(chromosomes_list):
    # trier les individus selon leur adaptation
    # sélectionner les meilleurs
    # sélectionner aléatoirement d'autres individus
    return []
