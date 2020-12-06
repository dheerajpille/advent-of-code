from aocd import get_data, submit

data = get_data(day=6, year=2020)
lines = data.splitlines()

counts = 0
questions = set()

for line in lines:
    if len(line) == 0:
        counts += len(questions)
        questions = set()
    else:
        for answer in line:
            questions.add(answer)

counts += len(questions)

submit(counts, part="a", day=6, year=2020)

# submit(output, part="a", day=1, year=2020)
