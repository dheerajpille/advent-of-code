from aocd import get_data, submit

data = get_data(day=2, year=2020)
lines = data.splitlines()

valid_passwords = 0

for line in lines:
    parts = line.split(' ')
    l, r = [int(number) for number in parts[0].split('-')]
    letter = parts[1][0]
    letter_count = 0
    password = parts[2]

    if password[l-1] == letter:
        letter_count += 1
    
    if password[r-1] == letter:
        letter_count += 1
    
    if letter_count == 1:
        valid_passwords += 1

submit(valid_passwords, part="b", day=2, year=2020)

# submit(output, part="a", day=1, year=2020)
