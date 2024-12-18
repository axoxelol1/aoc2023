from collections import deque
import math

broadcaster: list[str] = []
flip_flops: dict[str, tuple[bool, list[str]]] = {}
conjunctions: dict[str, tuple[dict[str, bool], list[str]]] = {}
with open("input.txt") as file:
    for line in file:
        fr, to = line.split(" -> ")
        if fr[0] == "%":
            flip_flops[fr[1:]] = (False, to.strip().split(", "))
        elif fr[0] == "&":
            conjunctions[fr[1:]] = ({}, to.strip().split(", "))
        else:
            broadcaster = to.strip().split(", ")

for dest in broadcaster:
    if dest in conjunctions:
        conjunctions[dest][0]["broadcaster"] = False
for name, (_, dests) in flip_flops.items():
    for dest in dests:
        if dest in conjunctions:
            conjunctions[dest][0][name] = False
for name, (_, dests) in conjunctions.items():
    for dest in dests:
        if dest in conjunctions:
            conjunctions[dest][0][name] = False

signals: deque[tuple[str, str, bool]] = deque([])

highs_to_ll: dict[str, list[int]] = {"kl": [], "vm": [], "kv": [], "vb": []}

low_count = 0
high_count = 0
for press in range(100000):
    signals.append(("button", "broadcaster", False))
    if press == 1000:
        print(f"Part 1: {low_count * high_count}")
    while signals:
        fr, to, is_high = signals.popleft()
        if to == "ll" and is_high:
            highs_to_ll[fr].append(press)
        if to == "rx" and not is_high:
            print(f"Found after {press} presses")
        # print(fr, "-high->" if is_high else "-low->", to)
        if is_high:
            high_count += 1
        else:
            low_count += 1
        if to == "broadcaster":
            for dest in broadcaster:
                signals.append((to, dest, is_high))
        elif to in flip_flops:
            state, dests = flip_flops[to]
            if is_high:
                continue
            state = not state
            flip_flops[to] = (state, dests)
            for dest in dests:
                signals.append((to, dest, state))
        elif to in conjunctions:
            conjunctions[to][0][fr] = is_high
            send_low = all(conjunctions[to][0].values())
            for dest in conjunctions[to][1]:
                signals.append((to, dest, not send_low))


# print("highs:")
# for key, val in highs_to_ll.items():
#     print(key)
#     print(val[:3])
#     print(val[1] - val[0])


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


first = lcm(3917, 4051)
second = lcm(first, 4013)
third = lcm(second, 3793)
print("Part 2:", third)
