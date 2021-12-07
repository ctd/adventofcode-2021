#!/usr/bin/env python


def part1(crabs):
    return solve(crabs)


def part2(crabs):
    return solve(crabs, part2=True)


def solve(crabs, part2=False):
    return min(
        map(
            lambda pos: sum(
                map(
                    lambda crab: abs(pos - crab)
                    if not part2
                    else int(abs(pos - crab) * ((abs(pos - crab) + 1) / 2)),
                    crabs,
                )
            ),
            range(min(crabs), max(crabs) + 1),
        )
    )


def test():
    sampleinput = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert part1(sampleinput) == 37
    assert part2(sampleinput) == 168


if __name__ == "__main__":
    input = list(map(int, open("input", "r").read().strip().split(",")))
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
