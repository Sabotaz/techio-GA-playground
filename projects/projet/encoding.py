import random
from answer import alphabet

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    return "".join(get_letter() for _ in range(size))
    
    
    