from aocd import get_data, submit

data = get_data(day=3, year=2015)
lines = data.splitlines()

position = [0, 0]
visited = set([(0, 0)])

for move in lines[0]:
    if move == '<':
        position[0] -= 1
    elif move == '>':
        position[0] += 1
    elif move == '^':
        position[1] += 1
    elif move == 'v':
        position[1] -= 1
    
    visited.add(tuple(position))

submit(len(visited), part="a", day=3, year=2015)

# submit(output, part="a", day=1, year=2015)
