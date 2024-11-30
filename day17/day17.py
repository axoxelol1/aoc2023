from heapq import heappop, heappush

with open("input.txt") as f:
    costs = [list(map(int, list(line.strip()))) for line in f.readlines()]

type state = tuple[int, int, int, int]


def shortest_path(
    costs: list[list[int]], p2: bool = False
) -> tuple[dict[state, int], dict[state, state]]:
    n = len(costs)
    queue: list[tuple[int, state]] = []
    dist: dict[state, int] = {}
    dist[(0, 1, 1, 1)] = costs[0][1]
    dist[(1, 0, 2, 1)] = costs[1][0]
    prev: dict[state, state] = {}

    heappush(queue, (costs[0][1], (0, 1, 1, 1)))
    heappush(queue, (costs[1][0], (1, 0, 2, 1)))

    visited: set[state] = set()
    while len(queue) != 0:
        u = heappop(queue)[1]
        if u in visited:
            continue
        visited.add(u)
        i, j, d, steps = u
        neighbours: list[state] = []
        for newi, newj, newd in [
            (i - 1, j, 0),
            (i + 1, j, 2),
            (i, j - 1, 3),
            (i, j + 1, 1),
        ]:
            if p2:
                if newd != d and steps < 4:
                    continue
            if newi < 0 or newj < 0 or newi >= n or newj >= n:
                continue
            if p2:
                maxsteps = 10
            else:
                maxsteps = 3
            if steps == maxsteps and newd == d:
                continue
            if (d == 0 and newi == i + 1) or (d == 2 and newi == i - 1):
                continue
            if (d == 1 and newj == j - 1) or (d == 3 and newj == j + 1):
                continue
            if d != newd:
                neighbours.append((newi, newj, newd, 1))
            else:
                neighbours.append((newi, newj, newd, steps + 1))
        for v in neighbours:
            if v == (0, 2, 2, 1):
                print(u)
            alt = dist[u] + costs[v[0]][v[1]]
            if alt < dist.get(v, 100000000):
                dist[v] = alt
                prev[v] = u
                heappush(queue, (alt, v))

    return dist, prev


n = len(costs)

dist, prev = shortest_path(costs)

sols: list[int] = []
for d in dist:
    if d[0] == n - 1 and d[1] == n - 1:
        sols.append(dist[d])

print("Part 1: " + str(min(sols)))

dist, prev = shortest_path(costs, True)

sols = []
for d in dist:
    if d[0] == n - 1 and d[1] == n - 1 and d[3] >= 4:
        sols.append(dist[d])

print("Part 2: " + str(min(sols)))
