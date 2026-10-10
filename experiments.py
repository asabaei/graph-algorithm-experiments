import json

from graph_generators import (
    make_erdos_renyi_graph,
    make_barabasi_albert_graph
)

from graph_algorithms import (
    get_diameter,
    get_clustering_coefficient,
    get_degree_distribution
)

# diameter / clustering experiments
n_values = [2**i for i in range(7, 19)]

# degree distribution sizes
degree_sizes = [
    1000,
    10000,
    100000
]

trials = 10

results = {
    "barabasi": {
        "diameter": [],
        "clustering": []
    },
    "erdos": {
        "diameter": [],
        "clustering": []
    }
}

degree_distributions = {
    "barabasi": {},
    "erdos": {}
}


# ---------------- BARABASI ----------------

print("\nRunning Barabasi-Albert experiments...\n")

for n in n_values:

    diameters = []
    clusterings = []

    for t in range(trials):

        print(f"BA n={n} trial={t+1}")

        graph = make_barabasi_albert_graph(n, 5)

        diameters.append(
            get_diameter(graph)
        )

        clusterings.append(
            get_clustering_coefficient(graph)
        )

    results["barabasi"]["diameter"].append(
        sum(diameters) / trials
    )

    results["barabasi"]["clustering"].append(
        sum(clusterings) / trials
    )


for n in degree_sizes:

    print(f"BA degree distribution n={n}")

    graph = make_barabasi_albert_graph(n, 5)

    degree_distributions["barabasi"][str(n)] = (
        get_degree_distribution(graph)
    )


# ---------------- ERDOS ----------------

print("\nRunning Erdos-Renyi experiments...\n")

for n in n_values:

    diameters = []
    clusterings = []

    for t in range(trials):

        print(f"ER n={n} trial={t+1}")

        graph = make_erdos_renyi_graph(n)

        diameters.append(
            get_diameter(graph)
        )

        clusterings.append(
            get_clustering_coefficient(graph)
        )

    results["erdos"]["diameter"].append(
        sum(diameters) / trials
    )

    results["erdos"]["clustering"].append(
        sum(clusterings) / trials
    )


for n in degree_sizes:

    print(f"ER degree distribution n={n}")

    graph = make_erdos_renyi_graph(n)

    degree_distributions["erdos"][str(n)] = (
        get_degree_distribution(graph)
    )


with open("results.json", "w") as f:
    json.dump(results, f, indent=4)

with open("degree_distributions.json", "w") as f:
    json.dump(degree_distributions, f, indent=4)

print("\nFinished experiments\n")