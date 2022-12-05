# file1 = open('/home/bcox/advent/12_03/test_input.txt')
file1 = open('/home/bcox/advent/12_03/advent_3_input.txt')
total = 0

for line in file1:
    line = line.strip()
    first, second = line[:len(line)//2], line[len(line)//2:] 

    if (set(first) & set(second)):
        oops = (set(first) & set(second)).pop() #failed to follow this rule for exactly one item type per rucksack.
        total += ord(oops)-96 if oops.islower() else ord(oops)-38

print(total)
file1.seek(0)

badges = file1.readlines()
import itertools
badge_total = 0
for a, b, c, in zip(*[iter(badges)]*3):
    badge = ((set(a.strip()) & set(b.strip())) & set(c.strip())).pop()
    badge_total += ord(badge)-96 if badge.islower() else ord(badge)-38
print(badge_total)