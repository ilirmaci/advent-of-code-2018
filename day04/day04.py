#!/usr/bin/env python3

from typing import Sequence, Iterable, Dict, Any
from day04_class import Shift


def minutes_from_log(line: str) -> int:
    '''
    Return minutes value from timestamp of line
    starting with '[YYYY-MM-DD HH:mm]'
    '''
    return int(line[15:17])


def process_shift(lines: Sequence[str]) -> Shift:
    '''
    Read the lines describing a shift and return a Shift object from them
    '''
    # get guard details and start timestamp
    guard = lines[0]
    begin = guard[1:17]  # starts with "[YYYY-MM-DD HH:mm]"
    guard_id = int(guard[26:].split()[0])  # "xxx begins shift"

    # the rest are only pairs of lines with start/end minutes respecively
    sleep_schedule = lines[1:]
    sleeps = []
    for ii in range(0, len(sleep_schedule), 2):
        start = minutes_from_log(sleep_schedule[ii])
        end = minutes_from_log(sleep_schedule[ii+1])
        sleeps.append((start, end))
    return Shift(guard_id, begin, sleeps)


def read_data(lines) -> Sequence[Shift]:
    '''
    Return all processed shifts
    '''
    result = []
    current_shift_lines = [lines[0]]
    for line in lines[1:]:
        if 'Guard' in line:
            # restart with current guard
            result.append(process_shift(current_shift_lines))
            current_shift_lines = [line]
        else:
            current_shift_lines.append(line)
    # process the last shift
    result.append(process_shift(current_shift_lines))
    return result


raw_input = sorted(open('day04_input.txt'))
shifts = read_data(raw_input)


##################
#  First puzzle  #
##################


def tabulate(itr: Iterable) -> Dict[Any, int]:
    '''
    Return dict of {item: count} for all items in `iter`
    '''
    result = dict()
    for _ in itr:
        result[_] = result.get(_, 0) + 1
    return result


def max_key(dd: Dict[Any, int]):
    '''
    Return the key with the highest value attached to it
    '''
    return [k for k, v in dd.items() if v == max(dd.values())][0]


guard_minutes = [(s.id, m) for s in shifts for m in s.minutes_asleep()]
the_guard: int = max_key(tabulate(g for g, m in guard_minutes))
the_guard_mins = (m for g, m in guard_minutes if g == the_guard)
the_minute: int = max_key(tabulate(the_guard_mins))

answer1 = the_guard * the_minute
print('The answer to the first puzzle is {}'.format(answer1))


###################
#  Second puzzle  #
###################

guard, minute = max_key(tabulate(guard_minutes))
answer2 = guard * minute
print('The answer to the first puzzle is {}'.format(answer2))
