# Random Graph Experiments: Barabási-Albert vs. Erdős-Rényi

Python implementations of three graph algorithms (diameter, clustering coefficient, degree distribution), tested experimentally on two random graph models to see how real-world network properties emerge as graphs grow. Built for UCI CS 165 (Project 3).

## Key findings

| Property | Barabási-Albert (d = 5) | Erdős-Rényi (p = 2 ln n / n) |
|---|---|---|
| **Diameter** (n = 2⁷ → 2¹⁸) | 3.3 → 6.1, roughly logarithmic growth | 3.5 → 5, roughly logarithmic and leveling off |
| **Clustering coefficient** | 0.147 → 0.00034 | 0.075 → 0.000095 (matches the theoretical value p) |
| **Degree distribution** | Heavy-tailed, **power law** (log-log slope approaches the theoretical −3 as n grows) | Bell-shaped, **not a power law** |

Both models stay "small world" at scale. Only the Barabási-Albert model produces the hubs and power-law degrees seen in real networks.

## What's implemented

**Algorithms** (`graph_algorithms.py`)
- **Diameter:** double-BFS heuristic. BFS from an arbitrary node to find a farthest node, then BFS again from that node.
- **Clustering coefficient:** global coefficient (3 × triangles / paths of length 2), using set intersections to count triangles efficiently.
- **Degree distribution:** a count of vertices at each degree.

**Graph generators** (`graph_generators.py`)
- **Barabási-Albert:** preferential attachment using a degree list, so higher-degree vertices are proportionally more likely to be chosen.
- **Erdős-Renyi:** each possible edge is included independently with probability p = 2 ln n / n.

**Experiments** (`experiments.py`, `plot_results.py`)
- Diameter and clustering measured for n = 2⁷ to 2¹⁸, averaged over 10 trials per size.
- Degree distributions generated for n = 1,000, 10,000, and 100,000, plotted on lin-lin and log-log scales with a fitted line.

## Selected plots

| Diameter (Barabási-Albert) | Degree distribution, log-log (Barabási-Albert, n = 100,000) |
|---|---|
| ![BA diameter](images/barabasi_diameter_plot.png) | ![BA degree distribution](images/barabasi_100000_degree_loglog.png) |

| Degree distribution, log-log (Erdős-Rényi, n = 100,000) | Clustering coefficient (Barabási-Albert) |
|---|---|
| ![ER degree distribution](images/erdos_100000_degree_loglog.png) | ![BA clustering](images/barabasi_clustering_plot.png) |

## Project structure

- `graph.py`: graph class (adjacency-list representation)
- `graph_algorithms.py`: diameter, clustering coefficient, degree distribution
- `graph_generators.py`: Barabási-Albert and Erdős-Rényi generators
- `experiments.py`: runs all experiments and writes `results.json` and `degree_distributions.json`
- `plot_results.py`: generates all plots from the JSON results
- `erdos/`: generated Erdos plots
- `barbasi/`: generated Barbasi plots
- `project3_tests.py`, `requirements.py`: test harness and interface provided by the course staff

## Run

```bash
pip install numpy matplotlib
python3 experiments.py     # runs all experiments (the largest sizes take a while)
python3 plot_results.py    # generates the plots
```

The graph and algorithm code uses only the Python standard library. `numpy` and `matplotlib` are only needed for plotting.

## Tech

Python, NumPy, Matplotlib
