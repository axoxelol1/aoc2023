import rustworkx as rx
from rustworkx.generators import grid_graph
from itertools import product
import numpy as np

n = 15
row_len = 131 * n
start = (131 * 7 + 65) * row_len + 131 * 7 + 65
G = grid_graph(131 * n, 131 * n)

with open("input.txt") as f:
    lines = f.readlines()
    for sx, sy in product([131 * i for i in range(n)], repeat=2):
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    G.remove_node((sy + y) * row_len + sx + x)

counts = []
for full in range(6):
    steps = 131 * full + 65
    shortest = rx.dijkstra_shortest_path_lengths(G, start, lambda _: 1)
    even_steps = steps % 2 == 0
    check = 0 if even_steps else 1
    count = sum(1 for x in shortest.values() if x <= steps and x % 2 == check)
    if even_steps:
        count += 1  # Add the start node
    print(steps, count)
    counts.append(count)

print(counts)
fit = np.polyfit(range(6), counts, 2)
steps = 26501365

full = steps // 131
print(full)
print(fit)

print(fit[0] * full**2 + fit[1] * full + fit[2])
