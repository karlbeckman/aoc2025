from dataclasses import dataclass
import os
import re
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import Parser, Direction, print_usage

@dataclass
class Rotation:
    direction: Direction
    angle: int

class Day1(Parser):
    START_VALUE = 50

    def __init__(self, filename: str):
        self.current_value = self.START_VALUE
        self.rotations: list[Rotation] = []
        super().__init__(filename)

    def parse(self):
        for line in self.lines:
            dir, ang, _ = re.split(r'(\d+)', line, maxsplit=1)
            if dir == "L":
                self.rotations.append(Rotation(Direction.LEFT, int(ang)))
            else:
                self.rotations.append(Rotation(Direction.RIGHT, int(ang)))

    def rotate(self, steps):
        self.current_value = (self.current_value + steps) % 100

    def count_zeros(self, steps):
        """Brute force"""
        count = 0
        value = self.current_value
        for i in range(abs(steps)):
            if steps < 0:
                value -= 1
            else:
                value += 1
            if value == -1:
                value = 99
            if value == 100:
                value = 0
            if value == 0:
                count += 1
        return count

    def count_zero_crossings(self, steps):
        """A little bit nicer"""
        if steps == 0:
            return 0

        count = abs(steps) // 100
        remaining_steps = abs(steps) % 100

        if steps > 0:
            # include "landing at zero" (equality) in the if statement
            if self.current_value + remaining_steps >= 100:
                count += 1
        #if current_value == 0, we can't hit zero
        if steps < 0 and self.current_value != 0:
            #include "landing at zero" (equality) in the if statement
            if self.current_value - remaining_steps <= 0:
                count += 1

        return count

    def solve(self) -> int:
        code1 = 0
        code2 = 0
        for rotation in self.rotations:
            steps = (
                rotation.angle if rotation.direction == Direction.RIGHT
                else -rotation.angle
            )
            code2 += self.count_zero_crossings(steps)
            self.rotate(steps)
            if self.current_value == 0:
                code1 += 1

        print(f"The solution for part 1 is {code1}")
        print(f"The solution for part 2 is {code2}")

def main(argv):
    if len(argv) < 2:
        print_usage()
        exit(1)
    day1 = Day1(argv[1])
    day1.solve()

main(sys.argv)