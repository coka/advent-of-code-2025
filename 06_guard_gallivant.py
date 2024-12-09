import unittest

type Position = tuple[int, int]


class Guard:
    initial_direction: Position = (0, -1)
    turns: dict[Position, Position] = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }

    def __init__(self, x: int, y: int):
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.direction = self.initial_direction

    def move(self):
        dx, dy = self.direction
        self.x += dx
        self.y += dy

    def turn(self):
        self.direction = self.turns[self.direction]

    def target(self) -> Position:
        dx, dy = self.direction
        return self.x + dx, self.y + dy

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.direction = self.initial_direction


class PuzzleMap:
    def __init__(self, input: list[str]):
        ascii_matrix = [[c for c in line[:-1]] for line in input]
        self.size = len(ascii_matrix)  # assume square matrix
        self.obstacles: set[Position] = set()
        for y, row in enumerate(ascii_matrix):
            for x, cell in enumerate(row):
                if cell == "#":
                    self.obstacles.add((x, y))
                elif cell == "^":
                    self.guard = Guard(x, y)
                    self.guard_start = (x, y)
                else:
                    continue

    def follow_protocol(self) -> set[Position]:
        visited_positions: set[Position] = set()
        while self._guard_in_bounds():
            if self.guard.target() in self.obstacles:
                self.guard.turn()
            else:
                visited_positions.add((self.guard.x, self.guard.y))
                self.guard.move()
        return visited_positions

    def is_loop_with_added_obstacle(self, obstacle: Position) -> bool:
        self.guard.reset()
        max_steps = self.size**2  # this is brute force; "raycasting"?
        steps = 0
        modded_obstacles: set[Position] = self.obstacles.union(set([obstacle]))
        while self._guard_in_bounds():
            if steps > max_steps:
                return True
            elif self.guard.target() in modded_obstacles:
                self.guard.turn()
            else:
                self.guard.move()
                steps += 1
        return False

    def _guard_in_bounds(self) -> bool:
        x, y = self.guard.x, self.guard.y
        limit = self.size
        return x > -1 and x < limit and y > -1 and y < limit


def solve_part_one(input: list[str]) -> int:
    puzzle_map = PuzzleMap(input)
    visited_tiles = puzzle_map.follow_protocol()
    return len(visited_tiles)


def solve_part_two(input: list[str]) -> int:
    puzzle_map = PuzzleMap(input)
    visited_tiles = puzzle_map.follow_protocol()
    visited_tiles.remove(puzzle_map.guard_start)
    loops = 0
    for tile in visited_tiles:
        if puzzle_map.is_loop_with_added_obstacle(tile):
            loops += 1
    return loops


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.example_input = open("input/06_example.txt").readlines()
        self.input = open("input/06.txt").readlines()

    def test_example_part_one(self):
        self.assertEqual(solve_part_one(self.example_input), 41)

    def test_example_part_two(self):
        self.assertEqual(solve_part_two(self.example_input), 6)

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.input), 4973)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.input), 1482)


if __name__ == "__main__":
    unittest.main()
