import math
from dataclasses import dataclass, field


def parse_operations(line: str) -> list[str]:
    return [op for op in line.strip().split(" ") if op]


def parse_numbers(line: str) -> list[int]:
    return [int(n) for n in parse_operations(line)]


@dataclass
class Problem:
    operation: str
    numbers: list[int] = field(default_factory=list)


def solve(problem: Problem) -> int:
    if problem.operation == "+":
        return sum(problem.numbers)
    else:
        return math.prod(problem.numbers)


# with open("input/06.txt") as f:
with open("example.txt") as f:
    input = f.readlines()

problems: list[Problem] = [
    Problem(operation=op) for op in parse_operations(input.pop())
]

for line in input:
    for i, n in enumerate(parse_numbers(line)):
        problems[i].numbers.append(n)

print(sum([solve(p) for p in problems]))  # 6725216329103
