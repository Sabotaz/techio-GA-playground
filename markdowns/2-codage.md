# Individus, chromosomes et gènes

![Gènes du chromosome 16 humain](/img/Human_chromosome_16_with_ASD_genes_from_IJMS-16-06464.png "Gènes du chromosome 16 humain")

L'humain a plusieurs chromosomes qui comportent chacun des miliers de gènes. Similairement, dans notre modèle, chaque individu sera décris par ses gènes, qui sont regroupés en chromosomes. Par facilité, nous utiliserons chromosome et individu alternativement pour désigner l'ensemble du matériel génétique de l'individu.

Par analogie avec la théorie de l'évolution, Ces algorithmes sont basées sur l'évolution d'une population au cours du temps.

# Schéma général

Un algorithme génétique est organisé en plusieurs étapes :
 * Création de la population de base
 * Évaluation des individus (l'individu est-il bien adapté au problème ?)
 * Sélection des individus (plus un individu s'adapte au problème, plus il a de chances de survivre)
 * Croisement (le croisement de deux parents donne naissance à un enfant dont les gènes proviennent des parents)
 * Mutation (certains gènes des enfants peuvent muter pour créer de nouveaux gènes)

## Présentation du problème
Pour illustrer ce cours, nous allons prendre un exemple concret.
Le but de l'exercice va être de deviner une chaine de caractère, par exemple `Mon mot de passe est difficile !` ou `IQlCqnWXVoVDDRFKFevaFzxmUxTxONwlLSwfkxmG`.
Les caractères autorisés seront les suivants :
```python
alphabet = string.ascii_letters + " !'."
```
Il y a 56 caractères autorisés. Pour une chaine de caractère de longueur 100, il faudrait $`6.59.10^{+174}`$ essais pour tester toutes les solutions possibles !

Nous allons donc créer un algorithme génétique pour deviner la solution, à partir de deux informations :
 * la taille de la chaine de caractères
 * le score d'adaptation de chaque solution (entre 0 et 1, plus le score est proche de 1, plus la solution est bonne).
 
# Création de la pupopulation de base

La première étape est de créer des individus, afin de constituer notre population de départ.

Un chromosome se compose d'un ensemble de gènes. Plusieurs codages sont possibles :
 * codage binaire : une chaîne de bits (0 ou 1)
 * codage à caractères multiples : une chaîne de caractères
 
Lors de la phase de croisement, on cherche à obtenir un plus grand brassage génétique, le codage binaire propose une plus grande granularité pour le lieu du croisement, car il permet de tout découper au maximum. 

Mais ce codage est peu naturel, et peu adapté au codage des données réels (par exemple, la modification de certains bits d'un nombre flottant peut créer des valeurs invalides).

Dans la pratique, on utilisera un codage différent suivant le type de problème à résoudre.

 * Problème du sac à dos :
 
> ![Problème du sac à dos](/img/Knapsack.svg "Problème du sac à dos")
> Le problème du sac à dos : quelles boîtes choisir afin de maximiser la somme emportée tout en ne dépassant pas les 15 kg autorisés ?
 
`0110001`, chaque bit correspond à un objet et indique si oui ou non celui-ci a été placé dans le sac.

 * Diriger un robot [(mars lander)](https://www.codingame.com/training/easy/mars-lander-episode-1):
 
![Mars Lander : simulateur](/img/marslander.png "blah" 400x260)

test

> 
> ![Mars Lander : console](/img/ControlPanel.png "Mars Lander : console")
> L'objectif est de faire atterrir, sans crash, la capsule "Mars Lander" qui contient le rover Opportunity.
 
`[float, int, float, int, float, int...]` l'angle (-90° à 90°) et la puissance des fusées (0 à 4) à chaque tour.

 * Trouver une chaine de caractères :

`"Aoljfon oaeznFjlf"`, chaque caractère indique un caractère de la chaîne à trouver.

Dans l'exercice suivant, vous devez coder la fonction permettant de créer un nouvel individu. le chromosome sera stoqué sous la forme d'une chaine de caractères.

@[Codage d'un chromosome]({"stubs":["codage.py"], "command":"codage_tests.ChromosomeTest", "project":"exercice1"})