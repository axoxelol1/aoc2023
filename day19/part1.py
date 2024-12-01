import re
from typing import override
from abc import ABC, abstractmethod


class Item:
    def __init__(self, x: int, m: int, a: int, s: int):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def attr_sum(self) -> int:
        return self.x + self.m + self.a + self.s

    @override
    def __repr__(self) -> str:
        return f"{{x: {self.x}, m: {self.m}, a: {self.a}, s: {self.s}}}"


class Rule(ABC):
    dst = ""

    @abstractmethod
    def matches(self, item: Item) -> bool:
        pass

    def destination(self) -> str:
        return self.dst


class AlwaysRule(Rule):
    def __init__(self, dst: str):
        self.dst = dst

    @override
    def matches(self, item: Item):
        return True

    @override
    def __repr__(self) -> str:
        return f"Always: {self.dst}"


class LtRule(Rule):
    def __init__(self, attr: str, threshold: int, dst: str):
        self.attr = attr
        self.threshold = threshold
        self.dst = dst

    @override
    def matches(self, item: Item):
        if getattr(item, self.attr) < self.threshold:
            return True
        return False

    @override
    def __repr__(self) -> str:
        return f"{self.attr} < {self.threshold}: {self.dst}"


class GtRule(Rule):
    def __init__(self, attr: str, threshold: int, dst: str):
        self.attr = attr
        self.threshold = threshold
        self.dst = dst

    @override
    def matches(self, item: Item):
        if getattr(item, self.attr) > self.threshold:
            return True
        return False

    @override
    def __repr__(self) -> str:
        return f"{self.attr} > {self.threshold}: {self.dst}"


workflows: dict[str, list[Rule]] = {}
items: list[Item] = []

with open("input.txt") as f:
    lines = f.readlines()
    n = lines.index("\n")
    workflowstrs = lines[:n]
    itemstrs = lines[n + 1 :]
    for itemstr in itemstrs:
        attribs = list(map(int, re.findall(r"\d+", itemstr)))
        items.append(Item(attribs[0], attribs[1], attribs[2], attribs[3]))
    for workflowstr in workflowstrs:
        splitted = workflowstr.split("{")  # "}" silly neovim indent, cba to debug rn
        name, rest = splitted[0], splitted[1][:-2]
        rulestrs = rest.split(",")
        rules: list[Rule] = []
        for rulestr in rulestrs:
            if ":" not in rulestr:
                rules.append(AlwaysRule(rulestr))
            else:
                cond, dst = rulestr.split(":")[:2]
                if "<" in cond:
                    attr, threshold = cond.split("<")[:2]
                    rules.append(LtRule(attr, int(threshold), dst))
                else:
                    attr, threshold = cond.split(">")[:2]
                    rules.append(GtRule(attr, int(threshold), dst))
        workflows[name] = rules


accepted: list[Item] = []
for item in items:
    dst = "in"
    while dst != "R" and dst != "A":
        rules = workflows[dst]
        for rule in rules:
            if rule.matches(item):
                dst = rule.destination()
                break
    if dst == "A":
        accepted.append(item)

part1_sol = sum(map(lambda x: x.attr_sum(), accepted))
print(f"Part 1: {part1_sol}")
