from typing import Iterable, TypeVar

T = TypeVar("T")


def enumerate_matrix(matrix: list[list[T]]) -> Iterable[tuple[T, int, int]]:
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            yield cell, i, j


def enumerate_neighbors(
    matrix: list[list[T]], row: int, col: int, rows: int, cols: int
) -> Iterable[T]:
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            else:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield matrix[nr][nc]


class PrintingDepartment:
    def __init__(self, input) -> None:
        self.map = []
        for line in input.splitlines():
            row = []
            for col in line:
                row.append(col == "@")
            self.map.append(row)
        self.rows = len(self.map)

    def access(self) -> int:
        accessed = 0
        cleanup_coords = []

        for cell, i, j in enumerate_matrix(self.map):
            if cell:
                rolls = 0
                cols = len(self.map[i])
                for n in enumerate_neighbors(self.map, i, j, self.rows, cols):
                    if n:
                        rolls += 1
                if rolls < 4:
                    accessed += 1
                    cleanup_coords.append((i, j))

        for i, j in cleanup_coords:
            self.map[i][j] = False

        return accessed


with open("input/04.txt") as f:
    printing_department = PrintingDepartment(f.read())

answer = printing_department.access()
print(answer)  # 1523

while (accessed := printing_department.access()) != 0:
    answer += accessed
print(answer)  # 9290
