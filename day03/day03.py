#!/usr/bin/env python3

from day03_class import Claim
from typing import Any, Dict, Iterable, Tuple


def read_input(line: str) -> Tuple[int, int, int, int, int]:
    elf_id, useless, corner, dims = line.strip().split()
    elf_id = int(elf_id.replace('#', ''))
    x, y = [int(_) for _ in corner[:-1].split(',')]
    width, length = [int(_) for _ in dims.split('x')]
    return Claim(elf_id, x, y, width, length)


raw_input = open('day03_input.txt').readlines()
claims = [read_input(_) for _ in raw_input]

##################
#  First puzzle  #
##################


def tabulate(lst: Iterable) -> Dict[Any, int]:
    '''
    Return dict of {item: count} for all items in lst
    '''
    result = {}
    for _ in lst:
        result[_] = result.get(_, 0) + 1
    return result


squares = (_ for claim in claims for _ in claim.squares())
square_counts = tabulate(squares)

answer = len([_ for _, count in square_counts.items() if count > 1])
print('The answer to the first puzzle is {}'.format(answer))


###################
#  Second puzzle  #
###################

single_squares = {_ for _, count in square_counts.items() if count == 1}
for claim in claims:
    if claim.squares().issubset(single_squares):
        break

answer2 = claim.id
print('The answer to the second puzzle is {}'.format(answer2))
