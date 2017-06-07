import os

from string import ascii_letters

alphabet = ascii_letters + " !'."

def get_answer():
    pass

def get_score(chrom):
    key = os.environ['SECRET_KEY']
    
    score = 0
    for a, b in zip(chrom, key):
        if a == b:
            score += 1
    return score / len(key)
    
def get_mean_score(population):
    mean = sum(get_score(chrom) for chrom in population)/len(population)
    return mean
    