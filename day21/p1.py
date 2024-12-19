import networkx as nx

# input_file, dim, steps = "example.txt", 11, 6
input_file, dim, steps = "input.txt", 131, 64

G = nx.grid_2d_graph(dim, dim)

start = None
with open(input_file) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == "#":
                G.remove_node((x, y))
            elif c == "S":
                start = (x, y)

shortest = nx.single_source_dijkstra_path_length(G, start)
count = sum(1 for x in shortest.values() if x <= steps and x % 2 == 0)
print(count)
