from aocd import get_data, submit

data = get_data(day=2, year=2015)
lines = data.splitlines()

surface_area = 0

for line in lines:
    values = line.split('x')
    sides = [int(side) for side in values]
    min_side = float('inf')

    for i in range(len(sides)-1):
        for j in range(i+1, len(sides)):
            side = sides[i]*sides[j]
            surface_area += 2*side
            min_side = min(min_side, side)

    surface_area += min_side

submit(surface_area, part="a", day=2, year=2015)

# submit(output, part="a", day=1, year=2015)
