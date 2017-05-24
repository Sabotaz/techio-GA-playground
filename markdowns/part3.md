# Outils
## Sélection
Chaque individu a un score d'adaptation plus ou moins bon pour le problème donné.
Dans cette étape, nous allons sélectionner les individus qui permettront de créer la génération suivante.
Cette sélection peut être effecuée de la façon suivante :
 * Un individu avec un bon rang (bon fitting) a beaucoup de chance d'être retenu
 * Un individu avec un mauvais rang (donc moins adapté) a moins de chance d'être retenu

@[Sélection des chromosomes]({"stubs":["selection.py"], "command":"tools_tests.SelectionTest", "project":"exercice2"})

## Croisement
Nous devons ensuite compléter notre population avec une nouvelle génération.
Pour créer cette génération, nous allons effectuer des croisements sur la population.
Lors d'un croisement, les deux parents vont échanger leur matériel génétique pour créer un enfant.
Une solution est de prendre 50% du matériel génétique de chaque parent.

@[Croisement des chromosomes]({"stubs":["croisement.py"], "command":"tools_tests.CroisementTest", "project":"exercice2"})

## Mutation
Afin de créer du nouveau matériel génétique, certains individus vont subir des mutations.
Pour cela, un gène va être modifié aléatoirement.

@[Mutation des chromosomes]({"stubs":["mutation.py"], "command":"tools_tests.MutationTest", "project":"exercice2"})