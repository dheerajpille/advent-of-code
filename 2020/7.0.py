from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=7, year=2020)
lines = data.splitlines()

bag_map = defaultdict(list)
bag_colors = 0
visited = set()

for line in lines:
    parts = line.split(' ')
    key = parts[0] + ' ' + parts[1]
    
    for i in range(4, len(parts), 4):
        if parts[i] != "no":
            bag_map[parts[i+1] + ' ' + parts[i+2]].append(key)

dfs = ["shiny gold"]

while dfs:
    color = dfs.pop()

    for neighbor in bag_map[color]:
        if neighbor not in visited:
            dfs.append(neighbor)
            visited.add(neighbor)
            bag_colors += 1

submit(bag_colors, part="a", day=7, year=2020)

# submit(output, part="a", day=1, year=2020)
