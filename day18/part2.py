def area(xs: list[float], ys: list[float]):
    area = 0
    for i in range(len(xs) - 1):
        area += xs[i] * ys[i + 1] - xs[i + 1] * ys[i]
    return area / 2


xs: list[int] = []
ys: list[int] = []
border_length = 0
with open("input.txt") as f:
    curr = (0, 0)
    for line in f:
        data = line.split()
        n = int(data[2][2:-2], 16)
        d = int(data[2][-2:-1])
        if d == 0:
            curr = (curr[0] + n, curr[1])
        if d == 1:
            curr = (curr[0], curr[1] + n)
        if d == 2:
            curr = (curr[0] - n, curr[1])
        if d == 3:
            curr = (curr[0], curr[1] - n)
        xs.append(curr[0])
        ys.append(curr[1])
        border_length += n

minx = min(xs)
miny = min(ys)

n = len(xs)
outer = (n + 4) / 2
inner = n - outer

a = area(xs, ys) + border_length / 2 + outer * 0.25 + inner * (-0.25)
print(a)
