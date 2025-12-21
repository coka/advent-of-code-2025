def joltage_of(bank: str) -> int:
    joltage = 0
    power = len(bank)

    for battery in bank:
        power -= 1
        joltage += int(battery) * 10**power

    return joltage


def max_joltage(bank: str, n: int) -> int:
    removals_allowed = len(bank) - n
    stack = []

    for battery in bank:
        while len(stack) and removals_allowed > 0 and stack[-1] < battery:
            stack.pop()
            removals_allowed -= 1
        stack.append(battery)

    while len(stack) > n:
        stack.pop()

    return joltage_of("".join(stack))


with open("input/03.txt") as f:
    banks = f.read().splitlines()

answer1 = 0
answer2 = 0

for bank in banks:
    answer1 += max_joltage(bank, 2)
    answer2 += max_joltage(bank, 12)

print(answer1)  # 17403
print(answer2)  # 173416889848394
