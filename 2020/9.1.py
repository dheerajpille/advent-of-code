from aocd import get_data, submit
from collections import deque

data = get_data(day=9, year=2020)
lines = data.splitlines()

preamble = deque()
first_number = None

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
        first_number = target
        break

    preamble.popleft()
    preamble.append(target)

input = []

for line in lines:
    input.append(int(line))

l, r = 0, 0
running_sum = 0

while r < len(input):
    if running_sum == first_number:
        submit(min(input[l:r])+max(input[l:r]), part="b", day=9, year=2020)
        break

    running_sum += input[r]

    while running_sum > first_number:
        running_sum -= input[l]
        l += 1

    r += 1

# submit(output, part="a", day=1, year=2020)
