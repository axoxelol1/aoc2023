import copy

def find_load_p1(input, i, j):
    moves = 0
    for ii in reversed(range(0, i)):
        if input[ii][j] == '#':
            break
        if input[ii][j] == '.':
            moves += 1
    return len(input)-(i-moves)
        
def move_north(input):
    final_locs = []
    o_locs = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'O':
                o_locs.append((i,j))
                moves = 0
                for ii in reversed(range(0, i)):
                    if input[ii][j] == '#':
                        break
                    if input[ii][j] == '.':
                        moves += 1
                final_locs.append((i-moves,j))
    for i,j in o_locs:
        input[i][j] = '.'
    for i,j in final_locs:
        input[i][j] = 'O'

def move_east(input):
    final_locs = []
    o_locs = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'O':
                o_locs.append((i,j))
                moves = 0
                for jj in range(j+1, len(input[0])):
                    if input[i][jj] == '#':
                        break
                    if input[i][jj] == '.':
                        moves += 1
                final_locs.append((i,j+moves))
    for i,j in o_locs:
        input[i][j] = '.'
    for i,j in final_locs:
        input[i][j] = 'O'

def move_south(input):
    final_locs = []
    o_locs = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'O':
                o_locs.append((i,j))
                moves = 0
                for ii in range(i, len(input)):
                    if input[ii][j] == '#':
                        break
                    if input[ii][j] == '.':
                        moves += 1
                final_locs.append((i+moves,j))
    for i,j in o_locs:
        input[i][j] = '.'
    for i,j in final_locs:
        input[i][j] = 'O'

def move_west(input):
    final_locs = []
    o_locs = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'O':
                o_locs.append((i,j))
                moves = 0
                for jj in reversed(range(0, j)):
                    if input[i][jj] == '#':
                        break
                    if input[i][jj] == '.':
                        moves += 1
                final_locs.append((i,j-moves))
    for i,j in o_locs:
        input[i][j] = '.'
    for i,j in final_locs:
        input[i][j] = 'O'

with open("input.txt") as f:
    input = [list(x) for x in f.read().splitlines()]

load = 0
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'O':
            load += find_load_p1(input, i, j)

print("Part 1: ", load)

cycles = [copy.deepcopy(input)]
done = False
c1, c2 = 0, 0
total_cycles = 1000000000
for _ in range(total_cycles):
    for i in range(len(cycles)):
        if done:
            break
        for j in range(i+1, len(cycles)):
            if cycles[i] == cycles[j]:
                c1, c2 = i, j
                done = True
                break
    if done:
        break
    move_north(input)
    move_west(input)
    move_south(input)
    move_east(input)
    cycles.append(copy.deepcopy(input))

repeat_cycles = c2-c1
assert(c2 == len(cycles)-1)
left = ((total_cycles - c2) % repeat_cycles)
for _ in range(left):
    move_north(input)
    move_west(input)
    move_south(input)
    move_east(input)

load = 0
pen = len(input)
for row in input:
    count = 0
    for c in row:
        if c == "O":
            count += 1
    load += count * pen
    pen -= 1

print("Part 2: ", load)
