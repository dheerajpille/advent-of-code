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
            key = pair[:3]
            value = pair[4:]

            if key == "byr" and 1920 <= int(value) <= 2002:
                fields[key] = True
            elif key == "iyr" and 2010 <= int(value) <= 2020:
                fields[key] = True
            elif key == "eyr" and 2020 <= int(value) <= 2030:
                fields[key] = True
            elif key == "hgt":
                measurement = value[:-2]
                unit = value[-2:]
                
                if unit == "cm" and 150 <= int(measurement) <= 193:
                    fields[key] = True
                elif unit == "in" and 59 <= int(measurement) <= 76:
                    fields[key] = True
            elif key == "hcl":
                valid_hcl = True

                for i in range(1, len(value)):
                    if value[i].isnumeric():
                        continue
                    elif value[i].isalpha():
                        if not ('a' <= value[i].lower() <= 'f'):
                            valid_hcl = False
                            break
                    else:
                        valid_hcl = False
                        break


                if valid_hcl and len(value) == 7 and value[0] == '#':
                    fields[key] = True
            elif key == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                fields[key] = True
            elif key == "pid" and len(value) == 9:
                if value.isnumeric():
                    fields[key] = True

valid = True

for field in fields:
    if not fields[field]:
        valid = False
        break

if valid:
    valid_passports += 1

submit(valid_passports, part="b", day=4, year=2020)

# submit(output, part="a", day=1, year=2020)
