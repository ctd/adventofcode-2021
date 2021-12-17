#!/usr/bin/env python


def parse_puzzle(puzzlein):
    return [[int(c) for c in line] for line in puzzlein]


def step(octopuses):
    flashed = set()
    for y, row in enumerate(octopuses):
        for x, i in enumerate(row):
            octopuses[y][x] += 1
    while len(flashed) < len([i for row in octopuses for i in row if i > 9]):
        for y, row in enumerate(octopuses):
            for x, i in enumerate(row):
                if i > 9 and (y, x,) not in flashed:
                    flashed.add((y, x,))
                    for adj in (
                        (y + 1, x - 1),
                        (y + 1, x),
                        (y + 1, x + 1),
                        (y, x - 1),
                        (y, x + 1),
                        (y - 1, x - 1),
                        (y - 1, x),
                        (y - 1, x + 1),
                    ):
                        if (
                            len(octopuses) > adj[0] >= 0
                            and len(octopuses[adj[0]]) > adj[1] >= 0
                            and adj not in flashed
                        ):
                            octopuses[adj[0]][adj[1]] += 1
    for y, x in flashed:
        octopuses[y][x] = 0
    return len(flashed)


def part1(puzzlein):
    puzzle = parse_puzzle(puzzlein)
    flashes = 0
    for i in range(100):
        flashes += step(puzzle)
    return flashes


def part2(puzzlein):
    puzzle = parse_puzzle(puzzlein)
    targetflashes = len(puzzle) * len(puzzle[0])
    i = 1
    while step(puzzle) != targetflashes:
        i += 1
    return i


def test():
    sampleinput = [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526",
    ]
    assert part1(sampleinput) == 1656
    assert part2(sampleinput) == 195


if __name__ == "__main__":
    test()
    input = [l.strip() for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
