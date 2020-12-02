from aocd import get_data, submit

data = get_data(day=3, year=2015)
lines = data.splitlines()

santa_position = [0, 0]
robot_position = [0, 0]
visited = set([(0,0)])

for counter, move in enumerate(lines[0]):
    if not counter%2:
        if move == '<':
            santa_position[0] -= 1
        elif move == '>':
            santa_position[0] += 1
        elif move == '^':
            santa_position[1] += 1
        elif move == 'v':
            santa_position[1] -= 1

        visited.add(tuple(santa_position))
    else:
        if move == '<':
            robot_position[0] -= 1
        elif move == '>':
            robot_position[0] += 1
        elif move == '^':
            robot_position[1] += 1
        elif move == 'v':
            robot_position[1] -= 1 
    
        visited.add(tuple(robot_position))

submit(len(visited), part="b", day=3, year=2015)

# submit(output, part="a", day=1, year=2015)
