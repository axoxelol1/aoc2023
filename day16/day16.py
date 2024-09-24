import numpy as np


def energized_count(
    start_beam: tuple[int, int, int, int], input: list[list[str]]
) -> int:
    counts = np.zeros((len(input), len(input)))
    beams = [start_beam]
    beams_set: set[tuple[int, int, int, int]] = set()

    while len(beams) > 0:
        i, j, di, dj = beams[-1]
        if i < 0 or j < 0 or i >= counts.shape[0] or j >= counts.shape[1]:
            _ = beams.pop()
            continue
        if beams[-1] in beams_set:
            _ = beams.pop()
            continue
        counts[i][j] += 1
        beams_set.add(beams[-1])
        tile = input[i][j]
        if tile == ".":
            beams[-1] = (i + di, j + dj, di, dj)
        elif tile == "/":
            if dj == 1:
                beams[-1] = (i - 1, j, -1, 0)
            elif dj == -1:
                beams[-1] = (i + 1, j, 1, 0)
            elif di == -1:
                beams[-1] = (i, j + 1, 0, 1)
            else:
                beams[-1] = (i, j - 1, 0, -1)
        elif tile == "\\":
            if dj == 1:
                beams[-1] = (i + 1, j, 1, 0)
            elif dj == -1:
                beams[-1] = (i - 1, j, -1, 0)
            elif di == -1:
                beams[-1] = (i, j - 1, 0, -1)
            else:
                beams[-1] = (i, j + 1, 0, 1)
        elif tile == "|":
            if dj == 0:
                beams[-1] = (i + di, j + dj, di, dj)
            else:
                beams[-1] = (i + 1, j, 1, 0)
                beams.append((i - 1, j, -1, 0))
        elif tile == "-":
            if di == 0:
                beams[-1] = (i + di, j + dj, di, dj)
            else:
                beams[-1] = (i, j + 1, 0, 1)
                beams.append((i, j - 1, 0, -1))
    return np.count_nonzero(counts)


with open("./input.txt") as f:
    input = [list(x) for x in f.read().splitlines()]

print("Part 1:", energized_count((0, 0, 0, 1), input))

n = len(input)
starter_beams = [(i, 0, 0, 1) for i in range(n)]
starter_beams += [(i, n - 1, 0, -1) for i in range(n)]
starter_beams += [(0, j, 1, 0) for j in range(n)]
starter_beams += [(n - 1, j, -1, 0) for j in range(n)]
print("Part 2:", max(map(lambda beam: energized_count(beam, input), starter_beams)))
