import sys

words, text = sys.stdin.read().split("\n\n")

words = words.strip()[6:].split(",")
text = text.strip()

out = set()
for wo in words:
    for w in (wo, wo[::-1]):
        idx = 0
        while True:
            p = text[idx:].find(w)
            if p == -1:
                break

            out |= set(range(idx + p, idx + p + len(w)))
            idx += p + 1
print("Part 2:", len(out))
