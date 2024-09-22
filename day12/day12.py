import numpy as np

def can_match(num: int, string: str) -> bool:
    if num > len(string):
        return False
    if "." not in string[:num] and \
            (num == len(string) or string[num] != "#"):
        return True
    return False

def solve(rows: list[tuple[str, list[int]]]):
    sum = 0
    for row in rows:
        springs, nums = row
        dp = np.zeros((len(nums)+1, len(springs)+1), dtype=np.int64)
        for j in reversed(range(len(dp[0]))):
            if springs[j:].startswith("#"):
                break
            dp[0][j] = 1
        for i in range(1, dp.shape[0]):
            n = nums[-i]
            for j in reversed(range(len(springs))):
                if springs[j] == ".":
                    try:
                        opt = dp[i][j+1]
                    except IndexError:
                        opt = 0
                elif springs[j] == "#":
                    if can_match(n, springs[j:]):
                        try:
                            opt = dp[i-1][j+n+1]
                        except IndexError:
                            opt = 1 if i == 1 else 0
                    else:
                        opt = 0
                else:
                    try:
                        hash = dp[i-1][j+n+1] if can_match(n, springs[j:]) else 0
                    except IndexError:
                        hash = 1 if i == 1 else 0
                    opt = dp[i][j+1] + hash
                dp[i][j] = opt
            sum += dp[-1][0]
    return sum

rows: list[tuple[str, list[int]]] = []

with open("input.txt") as f:
    for line in f:
        springs, nums = line.split()
        nums = list(map(int, nums.split(",")))
        rows.append((springs, nums))

part2_rows = [ (((springs + "?") * 5)[:-1], num*5) for (springs, num) in rows]

print("Part 1: ", solve(rows))
print("Part 2: ", solve(part2_rows))
