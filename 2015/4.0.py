from aocd import get_data, submit
import hashlib

data = get_data(day=4, year=2015)
lines = data.splitlines()

secret = lines[0]
number = 1

while True:
    md5_hash = hashlib.md5((secret+str(number)).encode()).hexdigest()
    if md5_hash[0] == md5_hash[1] == md5_hash[2] == md5_hash[3] == md5_hash[4] == '0':
        submit(number, part="a", day=4, year=2015)
        break

    number += 1

# submit(output, part="a", day=1, year=2015)
