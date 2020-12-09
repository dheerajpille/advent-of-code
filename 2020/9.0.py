from aocd import get_data, submit
from collections import deque

data = get_data(day=9, year=2020)
lines = data.splitlines()

preamble = deque()

for i in range(25):
    preamble.append(int(lines[i]))

for j in range(25, len(lines)):
    target = int(lines[j])
    property = False
    
    for element in preamble:
        if target-element != element and target-element in preamble:
            property = True
            break

    if not property:
        submit(target, part="a", day=9, year=2020)
        break

    preamble.popleft()
    preamble.append(target)

# submit(output, part="a", day=1, year=2020)
