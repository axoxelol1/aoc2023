def hash(string: str):
    val = 0
    for c in string:
        val += ord(c)
        val *= 17
        val %= 256
    return val

with open("input.txt") as f:
    input = f.read().strip().split(',')

print("Part 1:", sum(map(hash,input)))

boxes: list[dict[str, int]] = [{} for _ in range(256)]


for step in input:
    if step.endswith("-"):
        label = step[:-1]
        box = hash(label)
        if label in boxes[box]:
            del boxes[box][label]
    else:
        label, focal = step.split("=")
        focal = int(focal)
        box = hash(label)
        if label in boxes[box]:
            boxes[box][label] = focal
        else: 
            boxes[box][label] = focal

sol: int = 0
for n, box in enumerate(boxes):
    for i, lens in enumerate(box.values()):
        sol += (n+1) * (i+1) * lens

print("Part 2:", sol)
