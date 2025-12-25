from typing import Iterable


def parse(input: str) -> Iterable[Iterable[int]]:
    return [
        range(int(start), int(end) + 1)
        for start, end in (sequence.split("-") for sequence in input.split(","))
    ]


with open("input/02.txt") as f:
    ranges = parse(f.read().strip())

answer = 0
for r in ranges:
    for n in r:
        n_str = str(n)
        digits = len(n_str)
        if digits % 2 == 1:
            continue
        half = digits // 2
        if n_str[:half] == n_str[half:]:
            answer += n

answer2 = 0
for r in ranges:
    for n in r:
        n_str = str(n)
        digits = len(n_str)
        for divisor in range(1, digits):
            if digits % divisor == 0:
                part = n_str[:divisor]
                if part * (digits // divisor) == n_str:
                    answer2 += n
                    break


print(answer)  # 23701357374
print(answer2)  # 34284458938
