#!/usr/bin/env python


def find_rating(lines, criteria):
    if len(lines) == 1:
        return lines
    c = most_least_common((l[0] for l in lines))[criteria]
    f = find_rating([l[1:] for l in lines if l.startswith(c)], criteria)
    return ["{}{}".format(c, i) for i in f]


def most_least_common(l):
    freq = {"0": 0, "1": 0}
    for i in l:
        freq[i] += 1
    most_common = freq["1"] >= freq["0"]
    return str(int(most_common)), str(int(not most_common))


def part1(input):
    gammas = ""
    epsilons = ""
    bits = len(input[0])
    for i in range(bits):
        m, l = most_least_common((l[i] for l in input))
        gammas += m
        epsilons += l
    return int(gammas, 2) * int(epsilons, 2)


def part2(input):
    oxy = find_rating(input, 0)[0]
    scrub = find_rating(input, 1)[0]
    return int(oxy, 2) * int(scrub, 2)


def test():
    sampleinput = (
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    )

    assert part1(sampleinput) == 198
    assert part2(sampleinput) == 230


if __name__ == "__main__":
    input = [l.strip() for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
