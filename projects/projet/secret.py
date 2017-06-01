import os

from string import ascii_letters

alphabet = ascii_letters + " !'."

def get_score(chrom):
    key = os.environ['SECRET_KEY']
    
    score = 0
    for a, b in zip(chrom, key):
        if a == ord(b):
            score += 1
    return score / len(key)
    
def est_solution(chrom):
    key = os.environ['SECRET_KEY']
    return key == chrom.decode("ascii")
    
def get_mean_score(population):
    mean = sum(get_rang(chrom) for chrom in population)/len(population)
    return mean