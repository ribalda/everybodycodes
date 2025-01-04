bignum = 384400
bignum -= 5  # Left
cycle = "+...+...+..."

out = 0
while bignum:
    v = cycle[out % len(cycle)]
    if v == "+":
        bignum += 1
    else:
        bignum -= 1
    out += 1

print("Step 3:", out)
