from aocd import get_data, submit
from collections import Counter

data = get_data(day=1, year=2015)
lines = data.splitlines()

count = Counter(lines[0])

submit(count['(']-count[')'], part="a", day=1, year=2015)

# submit(output, part="a", day=1, year=2015)
