from aocd import get_data, submit

data = get_data(day=8, year=2020)
lines = data.splitlines()

counter = 0
instructions = set()
accumulator = 0

while counter < len(lines):
    if counter in instructions:
        submit(accumulator, part="a", day=8, year=2020)
        break

    parts = lines[counter].split(' ')
    value = parts[1][1:]
    instructions.add(counter)

    if parts[0] == "acc":
        if parts[1][0] == '+':
            accumulator += int(value)
        else:
            accumulator -= int(value)
        counter += 1
    elif parts[0] == "nop":
        counter += 1
    else:
        if parts[1][0] == '+':
            counter += int(value)
        else:
            counter -= int(value)

# submit(output, part="a", day=1, year=2020)
