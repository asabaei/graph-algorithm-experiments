from graph import Graph
from collections import deque


def bfs(graph: Graph, start: int):
    visited = set()
    q = deque()
    q.append((start, 0))
    visited.add(start)
    farthest = start
    max_distance = 0

    while q:
        node, dist = q.popleft()
        if dist > max_distance:
            max_distance = dist
            farthest = node

        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))

    return farthest, max_distance
    

def get_diameter(graph: Graph) -> int:

    #empty graph
    if graph.get_num_nodes() == 0:
        return 0

    #first bfs from node 0
    farthest_node, distance = bfs(graph, 0)

    #second bfs from farthest node
    other_node, diameter = bfs(graph, farthest_node)

    return diameter


def get_clustering_coefficient(graph: Graph) -> float:
    triangles = 0
    paths = 0

    for node in range(graph.get_num_nodes()):
        neighbors = list(graph.get_neighbors(node))
        degree = len(neighbors)

        paths += degree * (degree - 1) / 2

        neighbor_set = set(neighbors)

        for neighbor in neighbors:
            triangles += len(neighbor_set.intersection(graph.get_neighbors(neighbor)))

    triangles = triangles / 2

    if paths == 0:
        return 0.0

    return triangles / paths


def get_degree_distribution(graph: Graph) -> dict[int, int]:
    degrees = {}
    for node in range(graph.get_num_nodes()):
        degree = len(list(graph.get_neighbors(node)))
        if degree in degrees:
            degrees[degree] += 1
        else:
            degrees[degree] = 1

    return degrees