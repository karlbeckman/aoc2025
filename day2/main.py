import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import Parser, print_usage


class DayX(Parser):
    def __init__(self, filename):
        self.id_id_ranges: list[tuple[int, int]] = []
        super().__init__(filename)


    def parse(self):
        for line in self.lines:
            id_ranges = line.split(",")
            for id_range in id_ranges:
                id_range_min, id_range_max = id_range.split("-")
                self.id_id_ranges.append((int(id_range_min), int(id_range_max)))

    def solve(self):
        part1_sum = 0
        part2_sum = 0
        for id_range in self.id_id_ranges:
            for num in range(id_range[0], id_range[1] + 1):
                part1_sum += self.has_repeated_number_sequence(num)
                part2_sum += self.has_repeated_number_sequence_at_least_twice(num)

        print(f"The answer to the first part is {part1_sum}")
        print(f"The answer to the second part is {part2_sum}")

    def has_repeated_number_sequence(self, number: int):
        s = str(number)
        length = len(s)

        if length % 2 != 0:
            return 0

        mid = length // 2
        first_half = s[:mid]
        second_half = s[mid:]

        if first_half == second_half:
            return number
        else:
            return 0

    def has_repeated_number_sequence_at_least_twice(self, number: int):
        s = str(number)
        length = len(s)

        # Try all possible pattern lengths from 1 to half the string
        for pattern_length in range(1, length // 2 + 1):
            if length % pattern_length == 0:  # String length must be divisible by pattern length
                repetitions = length // pattern_length
                if repetitions >= 2:  # At least twice
                    pattern = s[:pattern_length]
                    if pattern * repetitions == s:
                        return number

        return 0

def main(argv):
    if len(argv) < 2:
        print_usage()
        exit(1)
    dayX = DayX(argv[1])
    dayX.solve()

if __name__ == "__main__":
    main(sys.argv)