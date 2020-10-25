#!/usr/bin/env python3

from typing import Sequence, Tuple
from datetime import datetime, timedelta

SleepType = Sequence[Tuple[int, int]]


class Shift(object):

    def __init__(self, guard_id: int, begin: str, sleeps: SleepType):
        self.id = guard_id
        self.begin = datetime.fromisoformat(begin)
        self.sleeps = sleeps

        # the start timestamp can be from the previous day
        # if so, we should mark the effective date as the next one
        begin_date = self.begin.date()
        if self.begin.hour == 0:
            self.date = begin_date
        else:
            self.date = begin_date + timedelta(hours=1)

    def minutes_asleep(self) -> Sequence[int]:
        '''
        Return all the minutes guard was asleep during this shift
        '''
        return {_ for start, end in self.sleeps for _ in range(start, end)}
