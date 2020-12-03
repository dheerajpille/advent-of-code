from aocd import get_data, submit
from collections import Counter

data = get_data(day=3, year=2020)
lines = data.splitlines()

tree_count = 0
position = 0

for line in lines:
    if line[position] == '#':
        tree_count += 1
    
    position = (position + 3) % len(line)
    
submit(tree_count, part="a", day=3, year=2020)

# submit(output, part="a", day=1, year=2020)
