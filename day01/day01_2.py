#!/usr/bin/env python3
raw_input = open('day01_input.txt').readlines()
changes = [int(_.strip()) for _ in raw_input]

# print answer to first puzzle as sanity check
print('The answer to the first puzzle is {}'.format(sum(changes)))

# create an (almost) infinite generator of changes
gg = (changes[i % len(changes)] for i in range(10000000))

seen = set()
tot = 0
while tot not in seen:
    seen.add(tot)
    current = next(gg)
    tot += current

print('The answer to the second puzzle is {}'.format(tot))
