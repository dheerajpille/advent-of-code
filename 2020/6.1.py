from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=6, year=2020)
lines = data.splitlines()

counts = 0
questions = defaultdict(int)
group_size = 0

for line in lines:
    if len(line) == 0:
        for question in questions:
            if questions[question] == group_size:
                counts += 1

        questions = defaultdict(int)
        group_size = 0
    else:
        for answer in line:
            questions[answer] += 1

        group_size += 1

for question in questions:
    if questions[question] == group_size:
        counts += 1

submit(counts, part="b", day=6, year=2020)

# submit(output, part="a", day=1, year=2020)
