# Individus, chromosomes et gènes

Ces algorithmes sont basées sur l'évolution d'une population au cours du temps. Par analogie avec la biologie, chaque individu est décris par ses gènes, qui sont regroupés en chromosomes. Par facilité, nous utiliserons chromosome et individu alternativement pour désigner l'ensemble du matériel génétique de l'individu.

![Gènes du chromosome 16 humain](/img/Human_chromosome_16_with_ASD_genes_from_IJMS-16-06464.png "Gènes du chromosome 16 humain")

L'humain a plusieurs chromosomes qui comportent chacun des miliers de gènes.

# Présentation du problème
Pour illustrer ce cours, nous allons prendre un exemple concret.
Le but de l'exercice va être de deviner une chaine de caractère, par exemple `Mon mot de passe est difficile !` ou `IQlCqnWXVoVDDRFKFevaFzxmUxTxONwlLSwfkxmG`.

```python
alphabet = string.ascii_letters + " !'."
```
Il y a 56 caractères autorisés. Pour une chaine de caractère de longueur 100, il faudrait $`6.59.10^{+174}`$ essais pour tester toutes les solutions possibles !

Nous allons donc créer un algorithme génétique pour deviner la solution, à partir de deux informations :
 * la taille de la chaine de caractères
 * le score d'adaptation de chaque solution (entre 0 et 1, plus le score est proche de 1, plus la solution est bonne).

La première étape est de créer des individus, afin de constituer notre population de départ.

Un chromosome se compose d'un ensemble de gènes. Plusieurs codages sont possibles :
 * codage binaire : une chaîne de bits (0 ou 1)
 * codage à caractères multiples : une chaîne de caractères
 
Un des principaux intérets du codage binaire est de permettre un plus grand brassage génétique.

En effet, lors de la phase de croisement, on dispose d'une plus grande granularité pour le lieu du croisement.

Mais ce codage est peu naturel, et peu adapté au codage des données réels (par exemple, la modification de certains bits d'un nombre flottant peut créer des valeurs invalides).

Dans la pratique, on utilisera un codage différent suivant le type de problème à résoudre.

 * Problème du sac à dos :
 
`0110001`, chaque bit indique si oui ou non l'objet a été placé dans le sac.

 * Diriger un robot [(mars lander)](https://www.codingame.com/training/easy/mars-lander-episode-1):
 
`[float, int, float, int, float, int...]` l'angle (-90° à 90°) et la puissance des fusées (0 à 4) à chaque tour.

 * Trouver une chaine de caractères :

`"Aoljfon oaeznFjlf"`, chaque caractère indique un caractère de la chaîne à trouver.

Pour l'exercice suivant, le chromosome sera stoqué sous la forme d'une `bytearray`.

@[Codage d'un chromosome]({"stubs":["codage.py"], "command":"codage_tests.ChromosomeTest", "project":"exercice1"})