import random
from solution import alphabet

def get_letter():
    return ord(random.choice(alphabet))

def creer_chromosome(size):
    # on crée un nouveau chromosome de la bonne taille sous forme de bytearray
    return bytearray()
    