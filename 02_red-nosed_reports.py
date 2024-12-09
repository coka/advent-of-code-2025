def drop(index, report):
    new_report = report.copy()
    del new_report[index]
    return new_report


def is_safe(report, dampener=False):
    increasing = report[0] < report[1]
    current = report[0]
    for index, next in enumerate(report[1:]):
        diff = next - current if increasing else current - next
        if diff < 1 or diff > 3:
            if dampener:
                return is_safe(drop(index, report)) or \
                    is_safe(drop(index - 1, report)) or \
                    is_safe(drop(index + 1, report))
            else:
                return False
        else:
            current = next
    return True


def is_tolerable(report):
    return is_safe(report, True)


reports = [[int(n) for n in line.split()] for line in open("input.txt")]
print(sum(map(is_safe, reports)))
print(sum(map(is_tolerable, reports)))
