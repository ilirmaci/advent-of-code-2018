#!/usr/bin/env python3

from typing import Iterable, Set, Dict, Any

raw_input = open('day02_input.txt')
boxes = [_.strip() for _ in raw_input]

##################
#  First puzzle  #
##################


def tabulate(itr: Iterable) -> Dict[Any, int]:
    '''
    Return dict of {item: count} for all items in `itr`
    '''
    result = dict()
    for _ in itr:
        result[_] = result.get(_, 0) + 1
    return result


box_counts = (tabulate(_) for _ in boxes)
count2 = 0
count3 = 0
for word_summary in box_counts:
    count2 += 1 if 2 in word_summary.values() else 0
    count3 += 1 if 3 in word_summary.values() else 0

answer1 = count2 * count3
print('The answer to the first puzzle is {}'.format(answer1))


###################
#  Second puzzle  #
###################


def compare_boxes(b1: str, b2: str) -> Set[str]:
    '''
    Return indices of places where boxes `b1` and `b2` differ
    '''
    return {i for i in range(len(b1)) if b1[i] != b2[i]}


for i in range(len(boxes)):
    for j in range(i, len(boxes)):
        b1 = boxes[i]
        b2 = boxes[j]
        difference = compare_boxes(b1, b2)
        if len(difference) == 1:
            result = list(b1)
            dummy = result.pop(difference.pop())
            answer2 = ''.join(result)
            break

print('The answer to the first puzzle is {}'.format(answer2))
