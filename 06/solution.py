#!/usr/bin/env python
def part1(input):
    return solve(input, 80)


def part2(input):
    return solve(input, 256)


def solve(input, days):
    fish = input
    for _ in range(days):
        fish = age(fish)
    return sum(fish.values())


def age(fish):
    newfish = dict()
    if not isinstance(fish, dict):
        for f in fish:
            newfish[f] = newfish.get(f, 0) + 1
        fish = newfish
        newfish = dict()

    for f in fish.keys():
        if f > 0:
            newfish[f - 1] = newfish.get(f - 1, 0) + fish[f]
        elif f == 0:
            newfish[6] = newfish.get(6, 0) + fish[0]
            newfish[8] = fish[0]
    return newfish


def test():
    sampleinput = [3, 4, 3, 1, 2]
    assert part1(sampleinput) == 5934
    assert part2(sampleinput) == 26984457539


if __name__ == "__main__":
    input = list(map(int, open("input", "r").read().strip().split(",")))
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
