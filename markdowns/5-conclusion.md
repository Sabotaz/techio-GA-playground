# What to do next

Know that you have basic knowledge of Genetic Algorithms the next step is to read more about GAs and try them out for yourself. Here are a few resources on GAs you might find useful:
* [label]
* [label]
* [Magus' article](http://files.magusgeek.com/csb/csb_en.html) on how to solve the [label] puzzle on CodinGame
* [Course on Genetic Algorithms](http://www.obitko.com/tutorials/genetic-algorithms/) with cool visual explanations by M. Obitko
* [Another course on Genetic Algorithm](http://web.cs.ucdavis.edu/~vemuri/classes/ecs271/Genetic%20Algorithms%20Short%20Tutorial.htm) by Alexander Schatten
* [This simulation](http://rednuht.org/genetic_cars_2/) of iterating to design the perfect car

And once you're done, take a look at [(Mars Lander)](https://www.codingame.com/training/easy/mars-lander-episode-1) :

A CodinGame puzzle where you have to land a mars rover and a flat surface. You don't **have to** use GAs to solve it but you can

> ![Mars Lander : simulation](/img/marslander.png "Mars Lander : simulation")
> ![Mars Lander : console](/img/ControlPanel.png "Mars Lander : console")
> The goal is to land, without crashing it, the capsule "Mars Lander" which holds the rover Opportunity.

`[float, int, float, int, float, int...]` the angle (-90° to 90°) and the rocket thrust (0 to 4) on each turn.

Here is an example of solution for solving this puzzle using a genetic algorithm.
Its fitting score is calculated with the final distance to the landing platform.

@[Mars Lander]({"stubs": ["genetic-lander-no-submodule/README.md"], "command": "visualisation.VisualisationTest", "project":"viewer-mars-lander"})

You can also take a look at these problems:

* [Game of Drones](https://www.codingame.com/multiplayer/bot-programming/game-of-drones) puzzle on CodinGame
* [Fantastic Bits](https://www.codingame.com/multiplayer/bot-programming/fantastic-bits) puzzle on CodinGame
* [Lab Rat Race Challenge](https://codegolf.stackexchange.com/questions/44707/lab-rat-race-an-exercise-in-genetic-algorithms) on StackExchange

[label]: https://www.codingame.com/multiplayer/bot-programming/coders-strike-back
