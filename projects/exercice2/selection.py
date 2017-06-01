import random
from solution import get_score
    
def score(chrom):
    # [0..1] suivant si le chromosome est mauvais ou bon
    return get_score(chrom)
    
def selection(chromosomes_list):
    return []
