#!/usr/bin/env python

from math import prod


def is_lowpoint(puzzle, x, y):
    maxx = len(puzzle[0]) - 1
    maxy = len(puzzle) - 1
    for point in (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ):
        if (
            maxx >= point[0] >= 0
            and maxy >= point[1] >= 0
            and puzzle[y][x] >= puzzle[point[1]][point[0]]
        ):
            return False
    return True


def risk_level(puzzle, x, y):
    return 1 + puzzle[y][x]


def basin_size(puzzle, x, y, seen=None):
    if puzzle[y][x] == 9:
        return 0
    if not seen:
        seen = set()
    seen.add((x, y))
    s = 1
    for point in (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ):
        if point in seen:
            continue
        if (
            len(puzzle) > point[1] >= 0
            and len(puzzle[point[1]]) > point[0] >= 0
            and puzzle[point[1]][point[0]] > puzzle[y][x]
        ):
            s += basin_size(puzzle, point[0], point[1], seen)
    return s


def get_lowpoints(puzzle):
    lp = set()
    for y, row in enumerate(puzzle):
        for x, _ in enumerate(row):
            if is_lowpoint(puzzle, x, y):
                lp.add((x, y,))
    return lp


def parse_puzzle(puzzlein):
    return [[int(c) for c in row] for row in puzzlein]


def part1(puzzlein):
    puzzle = parse_puzzle(puzzlein)
    return sum(map(lambda point: risk_level(puzzle, *point), get_lowpoints(puzzle)))


def part2(puzzlein):
    puzzle = parse_puzzle(puzzlein)
    basin_sizes = [basin_size(puzzle, x, y) for x, y in get_lowpoints(puzzle)]
    return prod(sorted(basin_sizes)[-3:])


def test():
    sampleinput = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]
    assert part1(sampleinput) == 15
    assert part2(sampleinput) == 1134


if __name__ == "__main__":
    test()
    input = [l.strip() for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
