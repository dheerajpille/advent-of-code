from aocd import get_data, submit
from collections import Counter

data = get_data(day=2, year=2020)
lines = data.splitlines()

valid_passwords = 0

for line in lines:
    parts = line.split(' ')
    mi, ma = [int(number) for number in parts[0].split('-')]
    letter = parts[1][0]
    password_counter = Counter(parts[2])

    if mi <= password_counter[letter] <= ma:
        valid_passwords += 1

submit(valid_passwords, part="a", day=2, year=2020)

# submit(output, part="a", day=1, year=2020)
