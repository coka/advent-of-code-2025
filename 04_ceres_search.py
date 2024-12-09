from enum import Enum


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP_LEFT = (-1, -1)
    DOWN_LEFT = (-1, 1)
    UP_RIGHT = (1, -1)
    DOWN_RIGHT = (1, 1)


input = [[c for c in line[:-1]] for line in open("input.txt")]
size = len(input)


def in_bounds(idx):
    return idx > -1 and idx < size


def match(x, y, direction, distance, char):
    dx, dy = direction.value
    xx, yy = x + dx * distance, y + dy * distance
    if in_bounds(xx) and in_bounds(yy) and input[yy][xx] == char:
        return (x, y, direction)
    else:
        return None


# Find every "X" which has an "M" next to it (in any direction).
xs = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "X":
            xs += [m for m in [match(x, y, d, 1, "M") for d in Direction] if m]


# Keep only those which are futher followed by the correct characters.
xs = [m for m in [match(x, y, d, 2, "A") for x, y, d in xs] if m]
xs = [m for m in [match(x, y, d, 3, "S") for x, y, d in xs] if m]

print(len(xs))

# Part Two

# Find every "A" which has a _diagonal_ "M" next to it.
diagonals = [
    Direction.DOWN_LEFT,
    Direction.UP_RIGHT,
    Direction.UP_LEFT,
    Direction.DOWN_RIGHT,
]
_as = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "A":
            _as += [m for m in [match(x, y, d, 1, "M") for d in diagonals] if m]

# Keep only those which have an "S" in the opposite direction.
_as = [m for m in [match(x, y, d, -1, "S") for x, y, d in _as] if m]

# If the same "A" matches twice, it is the center of an X-MAS.
tracker = set()
answer = 0
for a in _as:
    x, y, _ = a
    if (x, y) in tracker:
        answer += 1
    else:
        tracker.add((x, y))

print(answer)
