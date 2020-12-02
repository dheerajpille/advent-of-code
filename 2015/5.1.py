from aocd import get_data, submit

data = get_data(day=5, year=2015)
lines = data.splitlines()

nice_string_count = 0

for line in lines:
    row_dictionary = {}
    row_pair = False
    pair_between = False

    for i in range(len(line)-1):
        row = line[i]+line[i+1]

        if row in row_dictionary and row_dictionary[row][1] < i:
            row_pair = True
        elif row not in row_dictionary:
            row_dictionary[row] = (i, i+1)
    
    for j in range(len(line)-2):
        if line[j] == line[j+2]:
            pair_between = True

    if row_pair and pair_between:
        nice_string_count += 1

submit(nice_string_count, part="b", day=5, year=2015)

# submit(output, part="a", day=1, year=2015)
