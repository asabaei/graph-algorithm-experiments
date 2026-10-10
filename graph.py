from collections.abc import Iterable

class Graph:
    def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
        self.num_nodes = num_nodes
        self.num_edges = 0

        # adj list
        self.adj = {i: set() for i in range(num_nodes)}

        for u, v in edges:
            # avoid dup edge
            if v not in self.adj[u]:
                self.adj[u].add(v)
                self.adj[v].add(u)
                self.num_edges += 1

    def get_num_nodes(self) -> int:
        return self.num_nodes

    def get_num_edges(self) -> int:
        return self.num_edges

    def get_neighbors(self, node: int) -> Iterable[int]:
        return self.adj[node]