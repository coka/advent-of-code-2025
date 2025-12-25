type Range = tuple[int, int]


def parse_range(line: str) -> Range:
    start, end = line.split("-")
    return (int(start), int(end))


def number_in_range(n: int, range: Range) -> bool:
    start, end = range
    return start <= n <= end


def merge(ranges: list[Range]) -> list[Range]:
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        prev_start, prev_end = merged[-1]
        if prev_end >= start:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))
    return merged


def integers_in(range: Range) -> int:
    start, end = range
    return end - start + 1


with open("input/05.txt") as f:
    lines = [line.strip() for line in f]

ranges = []
parsing_ranges = True
answer = 0

for line in lines:
    if not line:
        parsing_ranges = False
    elif parsing_ranges:
        ranges.append(parse_range(line))
    else:
        for r in ranges:
            if number_in_range(int(line), r):
                answer += 1
                break

print(answer)  # 598
print(sum([integers_in(r) for r in merge(ranges)]))  # 360341832208407
