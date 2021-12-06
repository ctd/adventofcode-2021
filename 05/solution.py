#!/usr/bin/env python

import re


def parse_puzzle(puzzlein):
    lines = list()
    for l in re.findall("(\d+),(\d+) -> (\d+),(\d+)", puzzlein):
        lines.append(Line((int(l[0]), int(l[1])), (int(l[2]), int(l[3]))))
    return lines


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_horizontal(self):
        return self.start[1] == self.end[1]

    def is_vertical(self):
        return self.start[0] == self.end[0]

    def get_points(self, part2=False):
        points = set()
        if self.is_horizontal():
            for i in range(
                min(self.start[0], self.end[0]), max(self.start[0], self.end[0]) + 1
            ):
                points.add((i, self.start[1]))
        elif self.is_vertical():
            for i in range(
                min(self.start[1], self.end[1]), max(self.start[1], self.end[1]) + 1
            ):
                points.add((self.start[0], i))
        elif part2:
            hdiff = self.end[0] - self.start[0]
            vdiff = self.end[1] - self.start[1]
            hstep = int(hdiff / abs(hdiff))
            vstep = int(vdiff / abs(vdiff))
            assert abs(hdiff) == abs(vdiff)
            for i in range(abs(hdiff) + 1):
                points.add((self.start[0] + (i * hstep), self.start[1] + (i * vstep)))
        return points


def solve(lines, part2=False):
    points = dict()
    for line in lines:
        for point in line.get_points(part2):
            points[point] = points.get(point, 0) + 1
    return sum(i > 1 for i in points.values())


if __name__ == "__main__":
    input = open("input", "r").read()
    lines = parse_puzzle(input)
    print("Part 1: {}".format(solve(lines)))
    print("Part 2: {}".format(solve(lines, True)))
