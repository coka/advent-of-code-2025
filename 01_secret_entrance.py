def parse(rotation: str) -> int:
    distance = int(rotation[1:])
    return distance if rotation[0] == "R" else -distance


def signed_last_two_digits(n: int) -> int:
    return n % 100 if n > 0 else -((-n) % 100)


class Dial:
    def __init__(self):
        self.position = 50
        self.zero_points = 0

    def rotate(self, distance: int) -> int:
        full_turns = abs(distance) // 100
        self.zero_points += full_turns
        remaining_distance = signed_last_two_digits(distance)
        new_position = (self.position + remaining_distance) % 100
        if new_position == 0 or (
            self.position != 0
            and new_position != self.position + remaining_distance
        ):
            self.zero_points += 1
        self.position = new_position
        return self.position


with open("input/01.txt") as f:
    dial = Dial()
    zero_lands = 0
    for line in f:
        if dial.rotate(parse(line)) == 0:
            zero_lands += 1
    print(zero_lands)  # 1147
    print(dial.zero_points)  # 6789
