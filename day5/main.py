import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import Parser, print_usage

class Day5(Parser):
    def __init__(self, filename):
        self.ranges: list[tuple[int, int]] = []
        self.ids: list[int] = []
        super().__init__(filename)

    def parse(self):
        for line in self.lines:
            if '-' in line:
                range_min, range_max = line.split('-')
                self.ranges.append((int(range_min), int(range_max)))
            else:
                if len(line) > 0:
                    self.ids.append(int(line))

        self.ranges.sort()

    def solve1(self):
        valid_ids = 0
        for id in self.ids:
            for r in self.ranges:
                if r[0] <= id <= r[1]:
                    valid_ids += 1
                    break

        return valid_ids

    def solve2(self):
        total_count = 0
        current_start, current_end = self.ranges[0]

        for start, end in self.ranges[1:]:
            if start <= current_end + 1:
                current_end = max(current_end, end)
            else:
                total_count += current_end - current_start + 1
                current_start, current_end = start, end

        total_count += current_end - current_start + 1
        return total_count

    def solve(self):
        print(f"Part 1 answer: {self.solve1()}")
        print(f"Part 2 answer: {self.solve2()}")

def main(argv):
    if len(argv) < 2:
       print_usage()
       exit()
    day5 = Day5(argv[1])
    day5.solve()

if __name__ == "__main__":
    main(sys.argv)