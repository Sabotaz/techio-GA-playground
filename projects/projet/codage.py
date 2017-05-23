import random
from secret import alphabet

def get_letter():
    return ord(random.choice(alphabet))

size = int(input())

def creer_chromosome():
    return bytearray(get_letter() for _ in range(size))
    
    
    