from enum import Enum

def print_usage():
    print("Run program with: python3 main.py <input file>")
    print("E.g. python3 main.py input.txt")

class Direction(Enum):
    """Direction enum containing directions left, right, up, down"""
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class Parser:
    def __init__(self, filename: str):
        self.lines: list[str] = []
        with open(filename) as file:
            for line in file.readlines():
                self.lines.append(line.strip())

        self.parse()

    def parse(self):
        raise NotImplementedError("Must be implemented by the child class")