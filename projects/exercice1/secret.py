import os

from string import ascii_letters

alphabet = ascii_letters + " !'."

def get_rang(chrom):
    key = os.environ['SECRET_KEY']
    
    score = 0
    for a, b in zip(chrom, key):
        if a == ord(b):
            score += 1
    return score / len(key)
    
def get_mean_rang(population):
    mean = sum(get_rang(chrom) for chrom in population)/len(population)
    return mean