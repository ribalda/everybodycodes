import sys


def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def mul(a, b):
    x1, y1 = a
    x2, y2 = b
    return [x1 * x2 - y1 * y2, x1 * y2 + y1 * x2]

def c_div(x,y):
    if x<0 != y!=0:
        return -(abs(x)//abs(y))
    return x//y

def div(a, b):
    return [c_div(x,y) for x,y in zip(a,b)]


def cycle1(val, a):
    val = mul(val, val)
    val = div(val, [10, 10])
    val = add(val, a)
    return val


def step1(a):
    r = [0, 0]
    for _ in range(3):
        r = cycle1(r, a)
    return r


def cycle2(val, a):
    val = mul(val, val)
    val = div(val, [100000, 100000])
    val = add(val, a)
    return val


def should_paint(a):
    x = [0, 0]
    for _ in range(100):
        x = cycle2(x, a)
        for v in x:
            if v > 1000000 or v < -1000000:
                return False
    return True


def step2_3(a,step):
    pixels = 0
    for x in range(a[0], a[0] + 1000 + 1, step):
        for y in range(a[1], a[1] + 1000 + 1, step):
            pixels += should_paint([x, y])
    return pixels


a = sys.stdin.readline().strip()[3:-1].split(",")
a = list(map(int, a))

print("Step 1:", step1(a))
print("Step 2:", step2_3(a,10))
print("Step 3:", step2_3(a,1))
