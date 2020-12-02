from aocd import get_data, submit

data = get_data(day=5, year=2015)
lines = data.splitlines()

nice_string_count = 0

for line in lines:
    vowel_set = set(['a', 'e', 'i', 'o', 'u'])
    vowel_count = 0
    row = False
    forbidden_set = set(["ab", "cd", "pq", "xy"])
    forbidden = False

    for character in line:
        if character in vowel_set:
            vowel_count += 1
    
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            row = True

        if line[i]+line[i+1] in forbidden_set:
            forbidden = True

    if vowel_count >= 3 and row and not forbidden:
        nice_string_count += 1

submit(nice_string_count, part="a", day=5, year=2015)

# submit(output, part="a", day=1, year=2015)
