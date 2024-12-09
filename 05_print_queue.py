def parse_rules(input: list[str]) -> dict[int, list[int]]:
    rules: dict[int, list[int]] = {}
    for line in input:
        rule = [int(n) for n in line.split("|")]
        before = rule[0]
        after = rule[1]
        if before in rules:
            rules[before].append(after)
        else:
            rules[before] = [after]
    return rules


type Update = list[int]


def parse_updates(input: list[str]) -> list[Update]:
    return [[int(n) for n in line.split(",")] for line in input]


input = open("input.txt").readlines()
linebreak = input.index("\n")
rules = parse_rules(input[:linebreak])
updates = parse_updates(input[linebreak + 1 :])


def valid(update: Update) -> bool:
    current = 1
    while current < len(update):
        page = update[current]
        after_pages = rules.get(page)
        if after_pages:
            previous = 0
            while previous < current:
                previous_page = update[previous]
                if previous_page in after_pages:
                    return False
                previous += 1
        current += 1
    return True


def fix(update: Update):
    current = 1
    while current < len(update):
        page = update[current]
        after_pages = rules.get(page)
        if after_pages:
            previous = 0
            while previous < current:
                previous_page = update[previous]
                if previous_page in after_pages:
                    update[current] = update[previous]
                    update[previous] = page
                    current = 1
                    break
                else:
                    previous += 1
        current += 1


def middle(update: Update) -> int:
    return update[len(update) // 2]


answer1 = 0
answer2 = 0

for u in updates:
    if valid(u):
        answer1 += middle(u)
    else:
        fix(u)
        answer2 += middle(u)

print(answer1)
print(answer2)
