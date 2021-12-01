#!/usr/bin/env python


def part1(input):
    inc = 0
    for i in range(1, len(input)):
        inc += input[i] - input[i - 1] > 0
    return inc


def part2(input):
    inc = 0
    for i in range(1, len(input) - 2):
        inc += input[i + 2] - input[i - 1] > 0
    return inc


if __name__ == "__main__":
    input = list(map(int, open("input", "r").readlines()))
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
