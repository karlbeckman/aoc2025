import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import Parser, print_usage

class Day4(Parser):
    def __init__(self, filename):
        self.grid: list[list[str]] = []
        super().__init__(filename)

    def parse(self):
        for line in self.lines:
            self.grid.append(list(line))

    def solve(self):
        print(f"The answer to part 1 is {len(self.check_removable_indices())}")
        print(f"The answer to part 2 is {self.solve_part2()}")

    def solve_part2(self):
        can_still_remove = True
        sum = 0
        while can_still_remove:
            removable_indices = self.check_removable_indices()
            sum += len(removable_indices)
            for index in removable_indices:
                self.grid[index[0]][index[1]] = '.'
            can_still_remove = False if len(removable_indices) == 0 else True

        return sum

    def check_removable_indices(self):
        indices_to_remove: list[tuple[int, int]] = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                neighbours = self.check_neighbours(i, j, len(self.lines), len(self.lines[i]))
                if neighbours < 4:
                    indices_to_remove.append((i, j))
        return indices_to_remove

    def check_neighbours(self, i, j, max_i, max_j):
        if self.grid[i][j] != "@":
            return 9
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        sum = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < max_i and 0 <= nj < max_j:
                if self.grid[ni][nj] == "@":
                    sum += 1
        return sum

def main(argv):
    if len(argv) < 2:
       print_usage()
       exit()
    day4 = Day4(argv[1])
    day4.solve()

if __name__ == "__main__":
    main(sys.argv)