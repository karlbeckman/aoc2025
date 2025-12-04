import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import Parser, print_usage

class Day3(Parser):
    def __init__(self, filename):
        super().__init__(filename)

    def parse(self):
        # Parse logic here
        pass

    def solve(self):
        # Solution logic here
        sum1, sum2 = 0, 0
        for line in self.lines:
            sum1 += self.find_largest_n_digit_number(line, 2)
            sum2 += self.find_largest_n_digit_number(line, 12)

        print(f"The answer to part 1 is {sum1}")
        print(f"The answer to part 2 is {sum2}")

    def find_largest_n_digit_number(self, line: str, n: int):
        if len(line) < n:
            return 0

        result = []
        remaining_digits_needed = n

        for i in range(len(line)):
            while (
                result and
                len(line) - i > remaining_digits_needed and
                line[i] > result[-1]
            ):
                result.pop()
                remaining_digits_needed += 1

            if remaining_digits_needed > 0:
                result.append(line[i])
                remaining_digits_needed -= 1

        return int(''.join(result))

def main(argv):
    if len(argv) < 2:
       print_usage()
       exit()
    day3 = Day3(argv[1])
    day3.solve()

if __name__ == "__main__":
    main(sys.argv)