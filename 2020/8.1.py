from aocd import get_data, submit

data = get_data(day=8, year=2020)
lines = data.splitlines()

def backtrack(i, visited, accumulator, change):
    if i >= len(lines):
        submit(accumulator, part="b", day=8, year=2020)
        return

    if i in visited:
        return
    
    parts = lines[i].split(' ')
    value = parts[1][1:]
    visited.add(i)
    
    if parts[0] == "acc":
        if parts[1][0] == '+':
            backtrack(i+1, visited.copy(), accumulator+int(value), change)
        else:
            backtrack(i+1, visited.copy(), accumulator-int(value), change)
    elif parts[0] == "nop":
        backtrack(i+1, visited.copy(), accumulator, change)
        
        if not change:
            if parts[1][0] == '+':
                backtrack(i+int(value), visited.copy(), accumulator, True)
            else:
                backtrack(i-int(value), visited.copy(), accumulator, True)
    else:
        if parts[1][0] == '+':
            backtrack(i+int(value), visited.copy(), accumulator, change)
        else:
            backtrack(i-int(value), visited.copy(), accumulator, change)

        if not change:
            backtrack(i+1, visited.copy(), accumulator, True)

backtrack(0, set(), 0, False)

# submit(output, part="a", day=1, year=2020)
