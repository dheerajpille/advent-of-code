from aocd import get_data, submit

data = get_data(day=1, year=2015)
lines = data.splitlines()

left = 0
right = 0

for i, c in enumerate(lines[0]):
    if c == '(':
        left += 1
    else:
        right += 1

    if left-right == -1:
        submit(i+1, part="b", day=1, year=2015)
        break

# submit(output, part="a", day=1, year=2015)
