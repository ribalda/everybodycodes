import sys
from math import lcm


def step_snail(snail, n):
    modulus, rem = snail
    return modulus, (rem + n) % modulus


def parse_snail(line):
    x, y = map(lambda x: int(x[2:]), line.split())

    modulus = x + y - 1
    rem = x - 1
    return modulus, rem


def pos_snail(s):
    modulus, rem = s
    x = rem + 1
    y = modulus - x + 1
    return x, y


def find_golden(snails):
    rems = tuple(x[0] - x[1] - 1 for x in snails)
    modulus = tuple(x[0] for x in snails)
    prod = lcm(*modulus)

    result = 0
    for i, mod in enumerate(modulus):
        prod_i = prod // mod
        inv_i = pow(prod_i, -1, mod)
        result += rems[i] * prod_i * inv_i

    return result % prod


def find_golden_slow(snails):
    snails_in = snails[:]
    i = 0
    while True:
        snails_out = []
        for s in snails_in:
            s = step_snail(s, 1)
            snails_out.append(s)

        if sum(list(x[1] for x in snails_out)) == 0:
            return i
        snails_in = snails_out
        i += 1


snails_in = list(map(parse_snail, sys.stdin.readlines()))

out = 0
for s in snails_in:
    s = step_snail(s, 100)
    x, y = pos_snail(s)
    out += x + 100 * y

print("Step 1:", out)

print("Step 2,3:", find_golden(snails_in))
print("Step 2,3:", find_golden_slow(snails_in))
