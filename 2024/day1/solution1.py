import re
import math

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

list1 = []
list2 = []

for line in data:
    (a1, a2) = re.split("\s+", line)
    list1.append(int(a1))
    list2.append(int(a2))

list1s = sorted(list1)
list2s = sorted(list2)

total_distance = 0

for i in range(len(list1s)):
    total_distance += abs(list1s[i] - list2s[i])

print(total_distance)