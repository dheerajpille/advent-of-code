from aocd import get_data, submit

data = get_data(day=2, year=2015)
lines = data.splitlines()

ribbon_distance = 0

for line in lines:
    values = line.split('x')
    sides = [int(side) for side in values]
    min_side = float('inf')

    for i in range(len(sides)-1):
        for j in range(i+1, len(sides)):
            perimeter = 2*sides[i]+2*sides[j]
            min_side = min(min_side, perimeter)

    volume = 1

    for side in sides:
        volume *= side

    ribbon_distance += min_side + volume

submit(ribbon_distance, part="b", day=2, year=2015)

# submit(output, part="a", day=1, year=2015)
