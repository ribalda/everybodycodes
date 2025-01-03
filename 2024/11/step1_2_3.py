import sys
from math import inf


def simulate(termites, repro):
    out = dict()
    for t in termites:
        if t not in repro:
            continue
        for r in repro[t]:
            if r not in out:
                out[r] = 0
            out[r] += termites[t]
    return out


repro = dict()
lines = sys.stdin.readlines()
for l in lines:
    name, dest = l.strip().split(":")
    repro[name] = dest.split(",")

termites = dict()
termites["A"] = 1
for i in range(4):
    termites = simulate(termites, repro)
print("Step 1:", sum(termites.values()))

termites = dict()
termites["Z"] = 1
for i in range(10):
    termites = simulate(termites, repro)
print("Step 2:", sum(termites.values()))

min_ter = inf
max_ter = 0
for r in repro:
    termites = dict()
    termites[r] = 1
    for i in range(20):
        termites = simulate(termites, repro)
    s = sum(termites.values())
    min_ter = min(s, min_ter)
    max_ter = max(s, max_ter)
print("Step 3:", max_ter - min_ter)
