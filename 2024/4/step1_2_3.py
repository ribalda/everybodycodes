import sys
import statistics

nails = tuple(map(int, sys.stdin.readlines()))
min_nail = min(nails)
print("Part 1,2:", sum(map(lambda x: x - min_nail, nails)))

target_nail = int(statistics.median(nails))
print("Part 3:", sum(map(lambda x: abs(x - target_nail), nails)))
