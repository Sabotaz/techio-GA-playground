# Outils
Les algorithmes génétiques se basent sur le mécanisme de la sélection naturelle, c'est-à-dire l'avantage reproductif procuré aux individus s'adaptant le mieux à l'environnement.
Ils s'appuient sur plusieurs outils inspirés de la biologie qui permettent à l'espèce d'évoluer à chaque génération.

## Sélection
Cet outil est inspiré de la [sélection naturelle](https://fr.wikipedia.org/wiki/Sélection_naturelle).

![Les girafes qui peuvent manger des feuilles plus hautes survivent mieux](/img/Selection.svg "Les girafes qui peuvent manger des feuilles plus hautes survivent mieux")

Chaque individu a un score d'adaptation plus ou moins bon pour le problème donné.
Dans cette étape, nous allons sélectionner les individus qui permettront de créer la génération suivante.
Cette sélection peut être effecuée de la façon suivante :
 * Un individu avec un bon rang (bon fitting) a beaucoup de chance d'être retenu
 * Un individu avec un mauvais rang (donc moins adapté) a moins de chance d'être retenu

@[Sélection des chromosomes]({"stubs":["selection.py"], "command":"tools_tests.SelectionTest", "project":"exercice2"})

## Opérateurs génétiques
Ce sont des outils qui agiront directement sur le matériel génétique de chaque nouvel individu.
### Croisement
Nous devons ensuite compléter notre population avec une nouvelle génération.
Pour créer cette génération, nous allons effectuer des croisements sur la population.
Lors d'un croisement, les deux parents vont échanger leur matériel génétique pour créer un enfant [(recombinaison génétique)](https://fr.wikipedia.org/wiki/Recombinaison_génétique).

![Croisement entre deux chromosomes](/img/OnePointCrossover.svg "Croisement entre deux chromosomes")

Une solution est de prendre 50% du matériel génétique de chaque parent, en croisant à la moitié du chromosome.
Par exemple, si les parents sont `ABCDEFGH` et `12345678`, l'enfant sera `ABCD5678`.
Les gènes ne changent pas de place.

D'autres types de croisements existent, par exemple prendre 70% du matériel d'un parent et 30% de l'autre, ou de croiser en plusieurs points.

![Croisement en deux points](/img/Computational.science.Genetic.algorithm.Crossover.Two.Point.svg "Croisement en deux points")

@[Croisement des chromosomes]({"stubs":["croisement.py"], "command":"tools_tests.CroisementTest", "project":"exercice2"})

### Mutation
Afin de créer du nouveau matériel génétique, certains individus vont subir des [mutations](https://fr.wikipedia.org/wiki/Mutation_(génétique)).
Pour cela, un gène va être modifié aléatoirement.

![Mutation d'un gène](/img/mutation.png "Mutation d'un gène")

@[Mutation des chromosomes]({"stubs":["mutation.py"], "command":"tools_tests.MutationTest", "project":"exercice2"})