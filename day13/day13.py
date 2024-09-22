import numpy as np

def find_horiz(pattern: np.ndarray):
    for i in range(1, pattern.shape[0]):
        if not np.any(pattern[i] - pattern[i-1]):
            count = min(i, pattern.shape[0]-i)
            if not np.any(pattern[i:i+count] - np.flip(pattern[i-count:i], axis=0)):
                return i
    return 0

def find_vert(pattern: np.ndarray):
    for j in range(1, pattern.shape[1]):
        if not np.any(pattern[:,j] - pattern[:,j-1]):
            count = min(j, pattern.shape[1]-j)
            if not np.any(pattern[:,j:j+count] - np.flip(pattern[:,j-count:j], axis=1)):
                return j
    return 0

def find_horiz_p2(pattern: np.ndarray):
    for i in range(1, pattern.shape[0]):
        count = min(i, pattern.shape[0]-i)
        if np.sum(np.abs(pattern[i:i+count] - np.flip(pattern[i-count:i], axis=0))) == 1:
            return i
    return 0

def find_vert_p2(pattern: np.ndarray):
    for j in range(1, pattern.shape[1]):
        count = min(j, pattern.shape[1]-j)
        if np.sum(np.abs(pattern[:,j:j+count] - np.flip(pattern[:,j-count:j], axis=1))) == 1:
            return j
    return 0

patterns = []
with open("input.txt") as f:
    for pattern in f.read()[:-1].split("\n\n"):
        def charMap(x):
            return 1 if x == '#' else 0
        patterns.append(np.array([list(map(charMap, line)) for line in pattern.split('\n')]))

part1 = sum(map(find_vert, patterns)) + 100 * sum(map(find_horiz, patterns)) 
print("Part 1: ", part1)

part2 = sum(map(find_vert_p2, patterns)) + 100 * sum(map(find_horiz_p2, patterns)) 
print("Part 2: ", part2)
