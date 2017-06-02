import random
from solution import alphabet

def get_letter():
    return ord(random.choice(alphabet))
    
def mutation(chrom):
    # cette fonction ne retourne rien : on peut modifier directement le chromosome
    # mutation aléatoire d'un gène :
    pass
