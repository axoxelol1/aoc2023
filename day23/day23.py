from __future__ import annotations
import rustworkx as rx
from rustworkx.generators import directed_grid_graph, grid_graph
from itertools import pairwise

# file_name, dim = "example.txt", 23
file_name, dim = "input.txt", 141

G: rx.PyDiGraph[None, None] = directed_grid_graph(dim, dim, bidirectional=True)
Gp2: rx.PyGraph[None, int] = grid_graph(dim, dim)

for edge in Gp2.edge_indices():
    Gp2.update_edge_by_index(edge, 1)


with open(file_name) as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            if c == "#":
                G.remove_node(i * dim + j)
                Gp2.remove_node(i * dim + j)
            if c == ">":
                out_edges = G.out_edges(i * dim + j)
                for u, v, _ in out_edges:
                    G.remove_edge(u, v)
                _ = G.add_edge(i * dim + j, i * dim + j + 1, None)
            if c == "<":
                out_edges = G.out_edges(i * dim + j)
                for u, v, _ in out_edges:
                    G.remove_edge(u, v)
                _ = G.add_edge(i * dim + j, i * dim + j - 1, None)
            if c == "^":
                out_edges = G.out_edges(i * dim + j)
                for u, v, _ in out_edges:
                    G.remove_edge(u, v)
                _ = G.add_edge(i * dim + j, (i - 1) * dim + j, None)
            if c == "v":
                out_edges = G.out_edges(i * dim + j)
                for u, v, _ in out_edges:
                    G.remove_edge(u, v)
                _ = G.add_edge(i * dim + j, (i + 1) * dim + j, None)

start = 1
end = (dim - 1) * dim + dim - 2

paths = rx.all_simple_paths(G, start, end)
print(f"Part 1: {max(map(len, paths)) - 1}")

for i in Gp2.node_indices():
    out_edges = Gp2.out_edges(i)
    if len(out_edges) == 2:
        Gp2.remove_node(i)
        _ = Gp2.add_edge(
            out_edges[0][1], out_edges[1][1], out_edges[0][2] + out_edges[1][2]
        )

pathsp2 = rx.all_simple_paths(Gp2, start, end)
costs: list[int] = []
for path in pathsp2:
    cost = 0
    for u, v in pairwise(path):
        cost += Gp2.get_edge_data(u, v)
    costs.append(cost)
print(f"Part 2: {max(costs)}")
