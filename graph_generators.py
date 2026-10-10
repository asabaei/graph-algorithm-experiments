import random
import math
from graph import Graph

#extra credit
def make_erdos_renyi_graph(n):
    edges = set()
    p = (2 * math.log(n)) / n

    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                edges.add((u, v))

    return Graph(n, edges)

#necessary
def make_barabasi_albert_graph(n, d=5):
    edges = set()

    # start with d nodes connected to each other
    degree_list = []

    for i in range(d):
        for j in range(i + 1, d):
            edges.add((i, j))
            degree_list.append(i)
            degree_list.append(j)

    # add the rest of the nodes
    for new_node in range(d, n):
        chosen = set()

        while len(chosen) < d:
            chosen.add(random.choice(degree_list))

        for old_node in chosen:
            edges.add((new_node, old_node))

            # adding each endpoint once gives preferential attachment
            degree_list.append(new_node)
            degree_list.append(old_node)

    return Graph(n, edges)