workflows: dict[str, list[str]] = {}

with open("input.txt") as f:
    for line in f:
        if line.strip() == "":
            break
        name, rules = line.strip().split("{")  # }
        rules = rules[:-1].split(",")
        workflows[name] = rules


def accepted_by(
    workflow: str, ranges: list[tuple[int, int]], workflows: dict[str, list[str]]
) -> int:
    if workflow == "A":
        combos = ranges[0][1] - ranges[0][0] + 1
        for i in range(1, 4):
            combos *= ranges[i][1] - ranges[i][0] + 1
        return combos
    if workflow == "R":
        return 0
    combos = 0
    for rule in workflows[workflow]:
        if rule == "A":
            combos += accepted_by("A", ranges, workflows)
            return combos
        if rule == "R":
            return combos
        if ":" not in rule:
            return combos + accepted_by(rule, ranges, workflows)
        cond, dst = rule.split(":")
        attr, threshold = cond.split("<" if "<" in cond else ">")
        index = "xmas".index(attr)
        if "<" in cond:
            check_range = ranges.copy()
            check_range[index] = (ranges[index][0], int(threshold) - 1)
            ranges[index] = (int(threshold), ranges[index][1])
            combos += accepted_by(dst, check_range, workflows)
        if ">" in cond:
            check_range = ranges.copy()
            check_range[index] = (int(threshold) + 1, ranges[index][1])
            ranges[index] = (ranges[index][0], int(threshold))
            combos += accepted_by(dst, check_range, workflows)
    print("unreachable")
    return combos


solution = accepted_by("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)], workflows)
print(solution)
