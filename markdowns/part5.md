# Algorithme
## Schéma général de l'algorithme

1. Génération de la population de base  
On génère une population initiale aléatoire. Chaque individu est représenté par son matériel génétique.
2. Évaluation  
Chaque individu est noté suivant son adaptation au problème.
3. Sélection  
Chaque individu a une probabilité d'être tiré proportionnelle à son adaptation au problème.
4. Reproduction  
Des couples sont tirés au hasard parmis la population sélectionnée. Chaque couple donne un nouvel individu.
La population totale peut rester constante au court du temps (autant d'individus à chaque générations) ou varier.

À chaque reproduction :
 * Croisement  
Le matériel génétique de l'enfant est une combinaison du matériel génétique des parents
(généralement, 50% du matériel génétique de chaque parent).
 * Mutation  
Probabilité : de 0.1% à 1%
Pour chaque enfant, un gène est modifié au hasard.