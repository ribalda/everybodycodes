import sys
from math import sqrt, ceil


n = int(sys.stdin.readline())

target_heigth = ceil(sqrt(n))
missing = target_heigth**2 - n
target_width = 2 * target_heigth - 1

print("Step 1:", missing * target_width)
