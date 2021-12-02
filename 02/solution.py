#!/usr/bin/env python


def part1(input):
    hpos = depth = 0
    for line in input:
        move, units = line.split(" ")
        units = int(units)
        if move == "forward":
            hpos += units
        elif move == "up":
            depth -= units
        elif move == "down":
            depth += units
        else:
            raise Exception
    return hpos * depth


def part2(input):
    hpos = depth = aim = 0
    for line in input:
        move, units = line.split(" ")
        units = int(units)
        if move == "forward":
            hpos += units
            depth += aim * units
        elif move == "up":
            aim -= units
        elif move == "down":
            aim += units
        else:
            raise Exception
    return hpos * depth


def test():
    sampleinput = ("forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2")
    assert part1(sampleinput) == 150
    assert part2(sampleinput) == 900


if __name__ == "__main__":
    input = open("input", "r").readlines()
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
