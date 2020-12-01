from aocd import get_data, submit

data = get_data(day=1, year=2020)
lines = data.splitlines()

cache = set()

for line in lines:
    value = int(line)
    
    if 2020-value in cache:
        submit(str(value*(2020-value)), part="a", day=1, year=2020)
    
    cache.add(value)

# submit(output, part="a", day=1, year=2020)
