#!/usr/bin/env python3

from typing import List
import string

raw_input = open('day05_input.txt').readlines()[0].strip()


##################
#  First puzzle  #
##################

lower_upper = [_ + _.upper() for _ in string.ascii_lowercase]
upper_lower = [_.upper() + _ for _ in string.ascii_lowercase]
reactions = lower_upper + upper_lower


def react_once(polymer: str, reactions: List[str]) -> string:
    '''
    Return `polymer` after eleminating all patterns in `reactions`
    in one scan
    '''
    result = polymer
    for rr in reactions:
        result = result.replace(rr, '')
    return result


def react(polymer: str, reactions: List[str]) -> string:
    '''
    Return `polymer` after eleminating all patterns in `reactions`
    '''
    old_length = -1
    result = polymer
    while len(result) != old_length:
        old_length = len(result)
        result = react_once(result, reactions)
    return result


answer1 = len(react(raw_input, reactions))
print('The answer to the first puzzle is {}'.format(answer1))


###################
#  Second puzzle  #
###################


def remove_unit(polymer: str, unit: str) -> str:
    '''
    Return `polymer` with all instances of `unit` removed
    regardless of case
    '''
    return polymer.replace(unit, '').replace(unit.swapcase(), '')


all_polymers = (remove_unit(raw_input, _) for _ in string.ascii_lowercase)
reacted_polymers = (react(_, reactions) for _ in all_polymers)
answer2 = min(len(_) for _ in reacted_polymers)
print('The answer to the second puzzle is {}'.format(answer2))
