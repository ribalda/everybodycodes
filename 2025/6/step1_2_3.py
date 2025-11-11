import sys
from collections import Counter


def count_big(letters):
    dist = 1000
    mult = 1000
    letters *= mult
    cache = dict()
    options = dict()
    for i, l in enumerate(letters):
        if l.isupper():
            continue
        left = max(0, i - dist)
        right = min(len(letters), i + dist + 1)
        roi = "".join(letters[left:right])
        if roi not in cache:
            cache[roi] = Counter(roi)
        options[l] = options.get(l, 0) + cache[roi].get(l.upper(), 0)
    return options


def count_options(letters):
    mentors = dict()
    options = dict()
    for i, l in enumerate(letters):
        if l.isupper():
            mentors[l] = mentors.get(l, 0) + 1
            continue
        options[l] = options.get(l, 0) + mentors.get(l.upper(), 0)
    return options


letters = list(sys.stdin.readline().strip())

print("Step 1:", count_options(letters)["a"])
print("Step 2:", sum(count_options(letters).values()))
print("Step 3:", sum(count_big(letters).values()))
