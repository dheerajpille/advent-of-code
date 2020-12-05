from aocd import get_data, submit

data = get_data(day=5, year=2020)
lines = data.splitlines()

seats = set()

for line in lines:
    row = ""
    col = ""

    for i in range(7):
        if line[i] == 'F':
            row += '0'
        else:
            row += '1'

    for i in range(7, 10):
        if line[i] == 'L':
            col += '0'
        else:
            col += '1'
    
    row = int(row, 2)
    col = int(col, 2)

    id = row*8+col
    
    seats.add(id)

for i in range(128):
    for j in range(8):
        id = i*8+j

        if id not in seats and id-1 in seats and id+1 in seats:
            submit(id, part="b", day=5, year=2020)

# submit(output, part="a", day=1, year=2020)
