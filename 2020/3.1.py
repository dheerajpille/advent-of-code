from aocd import get_data, submit
from collections import Counter

data = get_data(day=3, year=2020)
lines = data.splitlines()

tree_product = 1
tree_count = 0
position = 0

for line in lines:
    if line[position] == '#':
        tree_count += 1
    
    position = (position + 1) % len(line)

tree_product *= tree_count
tree_count = 0
position = 0

for line in lines:
    if line[position] == '#':
        tree_count += 1
    
    position = (position + 3) % len(line)

tree_product *= tree_count
tree_count = 0
position = 0

for line in lines:
    if line[position] == '#':
        tree_count += 1
    
    position = (position + 5) % len(line)

tree_product *= tree_count
tree_count = 0
position = 0

for line in lines:
    if line[position] == '#':
        tree_count += 1

    position = (position + 7) % len(line)

tree_product *= tree_count
tree_count = 0
position = 0

for i in range(0, len(lines), 2):
    line = lines[i]

    if line[position] == '#':
        tree_count += 1
    
    position = (position + 1) % len(line)

tree_product *= tree_count
    
submit(tree_product, part="b", day=3, year=2020)

# submit(output, part="a", day=1, year=2020)
