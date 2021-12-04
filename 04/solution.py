#!/usr/bin/env python

import re


class board:
    def __init__(self, str_def):
        self.rows = list()
        row_str = str_def.split("\n")
        for r in row_str:
            if r:
                self.rows.append(list(map(int, re.findall("(\d+)", r))))

    def bingo(self, called):
        for r in self.rows:
            if all(n in called for n in r):
                return True

        for c in range(len(self.rows[0])):
            col = [r[c] for r in self.rows]
            if all(n in called for n in col):
                return True

    def sum_of_unmarked(self, called):
        all_numbers = [n for col in self.rows for n in col]
        return sum(filter(lambda x: x not in called, all_numbers))


def parse_puzzle_input(puzzle_input):
    sections = puzzle_input.split("\n\n")
    called = list(map(int, sections.pop(0).strip().split(",")))
    boards = list()
    for b in sections:
        boards.append(board(b))
    return called, boards


def solve(numbers, boards, part2=False):
    called = set()
    for n in numbers:
        called.add(n)
        for b in boards:
            if b.bingo(called):
                if part2 and len(boards) > 1:
                    boards.remove(b)
                else:
                    return b.sum_of_unmarked(called) * n


def test():
    input = open("test-input", "r").read()
    numbers, boards = parse_puzzle_input(input)
    assert solve(numbers, boards) == 4512
    assert solve(numbers, boards, part2=True) == 1924


if __name__ == "__main__":
    input = open("input", "r").read()
    numbers, boards = parse_puzzle_input(input)
    print("Part 1: {}".format(solve(numbers, boards)))
    print("Part 2: {}".format(solve(numbers, boards, part2=True)))
