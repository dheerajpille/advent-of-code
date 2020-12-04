from aocd import get_data, submit

data = get_data(day=4, year=2020)
lines = data.splitlines()

valid_passports = 0
fields = {field: False for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']}

for line in lines:
    if not len(line):
        valid = True

        for field in fields:
            if not fields[field]:
                valid = False
                break
            
        if valid:
            valid_passports += 1

        fields = {field: False for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']}
    else:
        pairs = line.split(' ')
        
        for pair in pairs:
            if pair[:3] in fields:
                fields[pair[:3]] = True

valid = True

for field in fields:
    if not fields[field]:
        valid = False
        break

if valid:
    valid_passports += 1

submit(valid_passports, part="a", day=4, year=2020)

# submit(output, part="a", day=1, year=2020)
