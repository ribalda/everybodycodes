import sys
from itertools import combinations


def line2person(line):
    id, dna = line.strip().split(":")
    return int(id), set([(idx, v) for (idx, v) in enumerate(dna)])


def get_parents(persons):
    out = []
    orphans = persons
    for mum, dad in combinations(persons, 2):
        valid = mum[1] | dad[1]
        for p in orphans:
            if p[0] in (mum[0], dad[0]):
                continue
            if p[1] - valid != set():
                continue
            simil = 1
            for _, genes in mum, dad:
                simil *=  len(p[1] & genes)
            out += [(simil, set((p[0], mum[0], dad[0])))]
            orphans.remove(p)
    return out


def find_tribes(parents):
    tribes = [s[1] for s in parents]
    out = []
    for i, t1 in enumerate(tribes):
        for j, t2 in enumerate(tribes[i + 1 :]):
            if t1 & t2:
                tribes[i + j + 1] |= t1
                break
        else:
            out.append(t1)
    return out


persons = list(map(line2person, sys.stdin.readlines()))
parents = list()

parents = get_parents(persons)
simils = tuple([s[0] for s in parents])
print("Step 1:", max(simils))
print("Step 2:", sum(simils))

tribes = find_tribes(parents)
print("Step 3:", sum(max(tribes, key=len)))
