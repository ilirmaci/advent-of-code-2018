#!/usr/bin/env python3

from typing import Set, Tuple


class Claim(object):

    def __init__(self, elf_id, x, y, width, length):
        self.id = elf_id
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    def squares(self) -> Set[Tuple[int, int]]:
        x_range = range(self.x, self.x + self.width)
        y_range = range(self.y, self.y + self.length)
        return {(i, j) for i in x_range for j in y_range}
