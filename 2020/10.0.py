from aocd import get_data, submit

data = get_data(day=10, year=2020)
lines = data.splitlines()

adapters = set()
start = 0
one_jolt = 0
three_jolt = 0

for line in lines:
    adapters.add(int(line))

target = max(adapters)+3
adapters.add(target)

while start < target:
    if start+1 in adapters:
        start += 1
        one_jolt += 1
    elif start+2 in adapters:
        start += 2
    elif start+3 in adapters:
        start += 3
        three_jolt += 1

submit(one_jolt*three_jolt, part="a", day=10, year=2020)

# submit(output, part="a", day=1, year=2020)
