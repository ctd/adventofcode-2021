#!/usr/bin/env python


class Cave:
    def __init__(self, name):
        self.name = name
        self.connected = set()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def connect(self, other_cave):
        self.connected.add(other_cave)

    def is_small(self):
        return self.name.islower()


def parse_puzzle(puzzlein):
    caves = {}
    for left, right in [l.split("-") for l in puzzlein]:
        if (left, right,) not in caves:
            caves[left] = caves.get(left, Cave(left))
            caves[right] = caves.get(right, Cave(right))
        caves[left].connect(caves[right])
        caves[right].connect(caves[left])
    return caves


def get_paths_to(start, end, history, paths, part2=False):
    if start == end:
        paths.append([*history, end])
        return
    for cave in start.connected:
        if cave.name == "start":
            continue
        if (
            part2
            and cave.is_small()
            and cave in history
            and any([[*history, start].count(c) > 1 for c in history if c.is_small()])
        ):
            continue
        if not part2 and cave.is_small() and cave in history:
            continue
        get_paths_to(cave, end, [*history, start], paths, part2)
    return paths


def part1(puzzlein):
    caves = parse_puzzle(puzzlein)
    return len(get_paths_to(caves["start"], caves["end"], [], []))


def part2(puzzlein):
    caves = parse_puzzle(puzzlein)
    return len(get_paths_to(caves["start"], caves["end"], [], [], part2=True))


def test():
    sampleinput = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]
    assert part1(sampleinput) == 10
    assert part2(sampleinput) == 36

    sampleinput = [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc",
    ]
    assert part1(sampleinput) == 19
    assert part2(sampleinput) == 103

    sampleinput = [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW",
    ]
    assert part1(sampleinput) == 226
    assert part2(sampleinput) == 3509


if __name__ == "__main__":
    input = [l.strip() for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
