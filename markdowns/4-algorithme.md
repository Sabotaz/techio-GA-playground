# Algorithme
## Schéma général de l'algorithme

1. Génération de la population de base  
On génère une population initiale aléatoire. Chaque individu est représenté par son matériel génétique.
On crée un nouvel individu à l'aide de la fonction `creer_chromosome(taille)` créée précédemment.
2. Évaluation  
Chaque individu est noté suivant son adaptation au problème. Cette phase est effectuée au début de la sélection.
3. Sélection  
Chaque individu a une probabilité d'être tiré proportionnelle à son adaptation au problème.
On ne garde que les individus sélectionnés par la fonction `selection(population)` créée précédemment.
4. Reproduction  
Des couples sont tirés au hasard parmis la population sélectionnée. Chaque couple donne un nouvel individu.
La population totale peut rester constante au court du temps (autant d'individus à chaque générations) ou varier.

À chaque reproduction :
 * Croisement  
Le matériel génétique de l'enfant est une combinaison du matériel génétique des parents (généralement, 50% du matériel génétique de chaque parent).
Une fois les parents choisis, la fonction `croisement(parent1, parent2)` créée précédemment permet de créer un enfant.
 * Mutation  
Probabilité : de 0.1% à 1%
Pour chaque enfant, un gène est modifié au hasard, à l'aide de la fonction `mutation(chromosome)` créée précédemment.

Enfin, la fonction `est_solution(chromosome)` permet de vérifier si un individu est une solution du problème (score de 100%).
Si il n'y a pas de solution, on passe à la génération suivante (phase 2).

![Schéma récapitulatif](/img/Schema_simple_algorithme_genetique.png "Schéma récapitulatif")

Le but de l'exercice est de trouver la phrase secrète grâce à un algorithme génétique, en utilisant les outils codées précédemment.

@[Algorithme génétique]({"stubs":["algorithme.py"], "command":"project_test.ProjectTest", "project":"projet", "layout": "aside"})

Vous pouvez voir .

@[Mars Lander]({"stubs": ["main.js"], "command": "visualisation.VisualisationTest", "project":"viewer-mars-lander"})