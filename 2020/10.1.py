from aocd import get_data, submit

data = get_data(day=10, year=2020)
lines = data.splitlines()

adapters = []

for line in lines:
    adapters.append(int(line))

target = max(adapters)+3
adapters.append(target)

adapters.sort()

dp = [0 for _ in range(target+1)]
dp[0] = 1

for adapter in adapters:
    dp[adapter] = dp[adapter-1]+dp[adapter-2]+dp[adapter-3]

submit(dp[target], part="b", day=10, year=2020)

# submit(output, part="a", day=1, year=2020)
