from aocd import get_data, submit

data = get_data(day=1, year=2020)
lines = data.splitlines()
numbers = [int(line) for line in lines]
numbers.sort()

for i in range(len(numbers)):
    l = i+1
    r = len(numbers)-1

    while l < r:
        if numbers[l]+numbers[r] == 2020-numbers[i]:
            submit(numbers[l]*numbers[r]*numbers[i], part="b", day=1, year=2020)
            l += 1
            r -= 1
        elif numbers[l]+numbers[r] < 2020-numbers[i]:
            l += 1
        else:
            r -= 1

# submit(output, part="a", day=1, year=2020)
