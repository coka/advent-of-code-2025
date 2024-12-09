import re

input = open("input.txt").read()

matches = re.finditer("mul\((\d+),(\d+)\)", input)
numbers = [[int(n) for n in m.groups()] for m in matches]
print(sum([x * y for x, y in numbers]))

# Part Two

matches = re.finditer("mul\((\d+),(\d+)\)|do\(\)|don't\(\)", input)
answer = 0
instructions_enabled = True
for m in matches:
    text = m.group(0)
    if text == "do()":
        instructions_enabled = True
    elif text == "don't()":
        instructions_enabled = False
    elif instructions_enabled:
        x, y = [int(n) for n in m.groups()]
        answer += x * y
print(answer)
