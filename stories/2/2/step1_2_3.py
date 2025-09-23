import sys
from collections import deque

sequence = "RGB"


def calc_line(line):
    idx = 0
    next_idx = 0

    for l in line:
        idx = next_idx
        if l != sequence[idx % len(sequence)]:
            next_idx = idx + 1

    return idx + 1


def calc_circle(circle):
    idx = 0
    circle = deque(circle)

    while circle:
        m = sequence[idx % len(sequence)]
        idx += 1
        if m != circle[0] or len(circle) % 2 != 0:
            circle.popleft()
            continue
        bad_idx = len(circle) // 2
        circle.rotate(-bad_idx)
        circle.popleft()
        circle.rotate(bad_idx)
        circle.popleft()

    return idx

def calc_circle_opti(circle):
    idx = 0

    middle = len(circle)//2
    left = deque(circle[:middle])
    right = deque(circle[middle:])
    del circle

    while(len(left)+len(right)):
        idx +=1

        if len(left) != len(right):
            left.popleft()
            continue
        first = left.popleft()
        x = right.popleft()
        if first != sequence[(idx-1) % len(sequence)]:
            left.append(x)

    return idx


line = sys.stdin.readline().strip()


print("Step 1: ", calc_line(line))
print("Step 2: ", calc_circle(line * 100))
print("Step 2: ", calc_circle_opti(line * 100))
print("Step 3: ", calc_circle_opti(line * 100000))