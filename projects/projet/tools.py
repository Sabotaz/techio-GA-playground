import random
from solution import alphabet, get_score

def get_letter():
    return random.choice(alphabet)
    
def score(chrom):
    # [0..1] suivant si le chromosome est mauvais ou bon
    return get_score(chrom)
    
def selection(chromlist):
    chromlist.sort(key = score, reverse = True)
    ind = int(len(chromlist) * 0.3)
    nb_others = int(len(chromlist) * 0.2)
    betters = chromlist[:ind]
    others = random.sample(chromlist[ind:], nb_others)
    return betters + others
    
def crossover(chrom_1, chrom_2):
    mid = len(chrom_1) // 2
    return chrom_1[:mid] + chrom_2[mid:]
    
def mutation(chrom):
    if len(chrom) == 0:
        return chrom
        
    i = random.randint(0,len(chrom)-1)
    genes = [c for c in chrom]
    genes[i] = get_letter()
    return "".join(genes)