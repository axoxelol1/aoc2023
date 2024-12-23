from typing import override


class Brick:
    def __init__(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2

    def overlaps(self, other: "Brick") -> bool:
        return (
            (self.x2 >= other.x1 and self.x1 <= other.x2)
            and (self.y2 >= other.y1 and self.y1 <= other.y2)
            and (self.z2 >= other.z1 and self.z1 <= other.z2)
        )

    def overlaps_xy(self, other: "Brick") -> bool:
        return (self.x2 >= other.x1 and self.x1 <= other.x2) and (
            self.y2 >= other.y1 and self.y1 <= other.y2
        )

    def supports(self, other: "Brick") -> bool:
        return self.overlaps_xy(other) and self.z2 == other.z1 - 1

    @override
    def __repr__(self) -> str:
        return f"(({self.x1}, {self.y1}, {self.z1}), ({self.x2}, {self.y2}, {self.z2}))"


bricks: list[Brick] = []

with open("input.txt") as f:
    for line in f:
        c1, c2 = map(lambda c: tuple(map(int, c.split(","))), line.split("~"))
        bricks.append(Brick(*c1, *c2))

bricks.sort(key=lambda brick: (brick.z1))

max_z = 0
for i, brick in enumerate(bricks):
    move_down = brick.z1 - max_z - 1
    brick.z1 -= move_down
    brick.z2 -= move_down
    while True:
        if brick.z1 == 1:
            break
        brick.z1 -= 1
        brick.z2 -= 1
        if any(brick.overlaps(bricks[j]) for j in range(i) if i != j):
            brick.z1 += 1
            brick.z2 += 1
            break
    max_z = max(brick.z2, max_z)

supports: dict[int, set[int]] = {i: set() for i in range(len(bricks))}
supported_by: dict[int, set[int]] = {i: set() for i in range(len(bricks))}
for i, brick in enumerate(bricks):
    for j, other in enumerate(bricks):
        if i != j and brick.supports(other):
            supports[i].add(j)
            supported_by[j].add(i)


not_disintegratable: set[int] = set()
for supporters in supported_by.values():
    if len(supporters) == 1:
        not_disintegratable.add(list(supporters)[0])


print(f"Part 1: {len(bricks) - len(not_disintegratable)}")

p2 = 0
for b in range(len(bricks)):
    fallen: set[int] = set([b])
    queue = [b]
    while queue:
        i = queue.pop()
        if all(j in fallen for j in supported_by[i]):
            fallen.add(i)
        for j in supports[i]:
            queue.append(j)
    p2 += len(fallen) - 1

print(f"Part 2: {p2}")
