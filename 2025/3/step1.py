import sys


def parse_line(line):
    id, faces, seed = line.split()
    id = int(id[:-1])
    faces = tuple(map(int, faces[7:-1].split(",")))
    seed = int(seed[5:])
    # id pos roll pulse faces seed
    return id, 0, 0, seed, faces, seed


def calc_spin_pulse(roll_number, pulse, seed):
    spin = roll_number * pulse
    pulse = pulse + spin
    pulse = pulse % seed
    pulse = pulse + 1 + roll_number + seed
    return spin, pulse


def roll(dice):
    id, pos, roll, pulse, faces, seed = dice
    roll += 1
    spin, pulse = calc_spin_pulse(roll, pulse, seed)
    pos = (pos + spin) % len(faces)
    return (id, pos, roll, pulse, faces, seed)


lines = sys.stdin.readlines()
dices = tuple(map(parse_line, lines))


total_val = 0
n_rolls = 0
while total_val <= 10000:
    n_rolls += 1
    out_dices = []
    for d in dices:
        d = roll(d)
        total_val += d[4][d[1]]
        out_dices += [d]
    dices = tuple(out_dices)

print("Step 1:", n_rolls)
