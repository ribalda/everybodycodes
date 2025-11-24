import sys
from collections import deque

def print_world(walls, start, end, visited=set()):
    for i in range(-20,20):
        out = ""
        for j in range(-20,20):
            if complex(i,j) == 0:
                out += "S"
                continue
            if complex(i,j) == start:
                out += "*"
                continue
            if complex(i,j) == end:
                out += "E"
                continue
            if complex(i,j) in visited:
                out += "."
                continue
            if complex(i,j) in walls:
                out += "#"
                continue
            out += " "
        print(out)
    print()


def make_map(ins):
    out = set()
    d2c = {
        'L': complex(0,1),
        'R': complex(0,-1),
    }
    d, pos = complex(-1,0), complex(0,0)
    for i in ins:
        lr, n  = d2c[i[0]],  int(i[1:])
        d *=lr
        for _ in range(n):
            pos += d
            out.add(pos)
    return out, pos

def find_dist(walls, end):
    todo = deque([(0,complex(0,0))])
    visited = set()

    while todo:
        dist, pos = todo.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        new_dist = dist +1
        for d in complex(0,1), complex(0,-1), complex(1,0), complex(-1,0):
            new_pos = pos +d
            if new_pos == end:
                return new_dist
            
            if new_pos  in visited:
                continue
            if new_pos in walls:
                continue

            todo.append((new_dist,new_pos))
    return None
        

ins = tuple(sys.stdin.readline().split(","))

walls, end = make_map(ins)

print ("Step 1,2:", find_dist(walls, end))