import random
from solution import alphabet

def get_letter():
    return random.choice(alphabet)

def creer_chromosome(size):
    return "".join(get_letter() for _ in range(size))
    
    
    