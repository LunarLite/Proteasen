# Case 9: Protein Pow(d)er

Protein Pow(d)er follows the heuristic case as laid out [here](http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er)
The idea is that the structure that makes up a protein powder can be folded in different ways.
As such, the main question for this case is: what is the best way to fold this structure?

## Getting Started

1. Download/clone this repository
2. either run ```python application.py``` or add commandline arguements when running to bypass the GUI.

Example:
```
python application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH

dimension: 2D/3D
algorithms: Random / Breadth / Breadth_heur / Depth / Randomhillclimber / Simulatedannealing
```

### Prerequisites

1. Python 3.6

```
install Anaconda 3.x
```

2. matplotlib v2.1.1 
    (Not neccesary if you install the latest version of anaconda)

```
python -mpip install -U matplotlib
```

### Installing

1. Download/clone this repository

![alt text](http://puu.sh/yGUk4/0a26513245.png)

2. either run ```python application.py``` or add commandline arguements when running to bypass the GUI.

![alt text](http://puu.sh/yGUnJ/eb9b33f1e9.png)

OR

![alt text](http://puu.sh/yGUq2/68c3681b4c.png)

Using the commandline arguements works as follows:
```
python application.py dimension algorithm chain

dimension: 2D/3D
algorithms: Random / Breadth / Breadth_heur / Depth / Randomhillclimber / Simulatedannealing
chain: CHHCPCHCHCP (any combination of P's, H's and/or C's)
```

## Running the tests

There is no way as of yet to run a multitude of automated tests, for now you'll have to test by hand.

### Break down into end to end tests

We tested the effect of start score on the end score that was achieved with our hillclimber algorithm.
We ran the three versions of the hillclimber algorithm (straight, random, depth) that have different starting points.
For results and a more detailed explanation of our experiment, see 'experiment documentatie.pdf' in the folder
'\application\experiment'.

## Authors

* **Vanessa Botha** - *All work* - [Vanessa](https://github.com/VanessaBotha)
* **Eliene Rietdijk** - *All work* - [Eliene](https://github.com/elinerietdijk)
* **Mick Tozer** - *All work* - [Mick](https://github.com/LunarLite)


## Acknowledgments

Tip of the hat to the following people who helped:
* **Daan Uittenhout** - *Help with heuristic calculations & Simulated annealing* - [Daan](https://github.com/daanuittenhout)


