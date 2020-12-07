from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=7, year=2020)
lines = data.splitlines()

bag_map = defaultdict(list)
bags = 0

for line in lines:
    parts = line.split(' ')
    key = parts[0] + ' ' + parts[1]
    
    for i in range(4, len(parts), 4):
        if parts[i] != "no":
            bag_map[key].append((parts[i+1] + ' ' + parts[i+2], int(parts[i])))

dfs = [("shiny gold", 1)]

while dfs:
    color, factor = dfs.pop()
    
    for neighbor, value in bag_map[color]:
        bags += factor*value
        dfs.append((neighbor, factor*value))

submit(bags, part="b", day=7, year=2020)

# submit(output, part="a", day=1, year=2020)
