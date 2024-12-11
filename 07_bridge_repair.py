from dataclasses import dataclass
from itertools import product


@dataclass
class Equation:
    target: int
    numbers: list[int]


def parse(line: str) -> Equation:
    foo = line.split(":")
    target = int(foo[0])
    numbers = [int(n) for n in foo[1].split()]
    return Equation(target, numbers)


equations = [parse(line) for line in open("input.txt")]
answer = 0
for e in equations:
    repeat = len(e.numbers) - 1
    operation_permutations = product("+*|", repeat=repeat)
    for permutation in operation_permutations:
        result = e.numbers[0]
        for i, operation in enumerate(permutation):
            n = e.numbers[i + 1]
            if operation == "+":
                result += n
            elif operation == "*":
                result *= n
            elif operation == "|":
                result = int(str(result) + str(n))
        if result == e.target:
            answer += result
            break

print(answer)
