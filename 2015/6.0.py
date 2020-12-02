from aocd import get_data, submit

data = get_data(day=6, year=2015)
lines = data.splitlines()

lights = [[0 for y in range(1000)] for x in range(1000)]
light_count = 0

for line in lines:
    command = line.split(' ')
    
    if command[0] == "turn":
        top_left_coordinate = [int(value) for value in command[2].split(',')]
        bottom_right_coordinate = [int(value) for value in command[4].split(',')]

        if command[1] == "on":
            for i in range(top_left_coordinate[0], bottom_right_coordinate[0]+1):
                for j in range(top_left_coordinate[1], bottom_right_coordinate[1]+1):
                    lights[i][j] = 1
        else:
            for i in range(top_left_coordinate[0], bottom_right_coordinate[0]+1):
                for j in range(top_left_coordinate[1], bottom_right_coordinate[1]+1):
                    lights[i][j] = 0

    else:
        top_left_coordinate = [int(value) for value in command[1].split(',')]
        bottom_right_coordinate = [int(value) for value in command[3].split(',')]
        
        for i in range(top_left_coordinate[0], bottom_right_coordinate[0]+1):
            for j in range(top_left_coordinate[1], bottom_right_coordinate[1]+1):
                lights[i][j] = 1-lights[i][j]

for i in range(1000):
    for j in range(1000):
        light_count += lights[i][j]

submit(light_count, part="a", day=6, year=2015)

# submit(output, part="a", day=1, year=2015)
