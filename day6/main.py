import os
import sys
import re

from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import Parser, print_usage

class Day5:
    def __init__(self, filename):
        self.lines = []
        self.problem_grid: list[list[str]] = []
        self.problem_grid_2: list[list[str]] = []
        with open(filename) as file:
            self.lines = file.readlines()

        self.parse()

    def parse(self):
        for line in self.lines:
            self.problem_grid.append(line.split())
            self.problem_grid_2.append(list(line))

    def solve(self):
        self.solve1()
        self.solve2()

    def solve1(self):
        sum = 0
        for column in zip(*self.problem_grid):
            multiply = True if column[-1] == '*' else False
            part_sum = int(column[0])
            for i in range(1, len(column) - 1):
                if multiply:
                    part_sum *= int(column[i])
                else:
                    part_sum += int(column[i])
            sum += part_sum

        print(f"Part 1 answer: {sum}")

    def solve2(self):
        pattern = r'[+*]|\d+'
        sum = 0
        columns_list = []
        multiply = False
        for column in zip(*self.problem_grid_2):
            column_str = ''.join(column).strip()
            if len(column_str) == 0:
                part_sum = int(columns_list[0])
                for i in range(1, len(columns_list)):
                    if multiply:
                        part_sum *= int(columns_list[i])
                    else:
                        part_sum += int(columns_list[i])
                columns_list = []
                multiply = False
                sum += part_sum
            else:
                matches = re.findall(pattern, column_str)
                columns_list.append(matches[0])
                if '*' in matches:
                    multiply = True

        print(f"Part 2 answer: {sum}")

def main(argv):
    if len(argv) < 2:
       print_usage()
       exit()
    day5 = Day5(argv[1])
    day5.solve()

if __name__ == "__main__":
    main(sys.argv)