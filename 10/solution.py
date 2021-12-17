#!/usr/bin/env python

EXPECTED = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

P1_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

P2_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_illegal_chars(line):
    expect = list()
    illegal = list()
    for c in line:
        if c in EXPECTED.keys():
            expect.append(EXPECTED.get(c))
        elif c == expect[-1]:
            expect.pop()
        else:
            illegal.append(c)
    return illegal, reversed(expect)


def part1(puzzlein):
    score = 0
    for line in puzzlein:
        illegal, _ = find_illegal_chars(line)
        if illegal:
            score += P1_SCORES.get(illegal[0])
    return score


def part2(puzzlein):
    scores = list()
    for line in puzzlein:
        score = 0
        illegal, completion = find_illegal_chars(line)
        if not illegal and completion:
            for c in completion:
                score = (score * 5) + P2_SCORES.get(c)
            scores.append(score)
    return sorted(scores)[int(len(scores) / 2)]


def test():
    sampleinput = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]
    assert part1(sampleinput) == 26397
    assert part2(sampleinput) == 288957


if __name__ == "__main__":
    test()
    input = [l.strip() for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))
