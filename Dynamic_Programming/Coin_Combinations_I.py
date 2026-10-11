# https://cses.fi/problemset/task/1635
# 11/10/26

# memo = {}


# def coin_combination(x):

#     if x == 0:
#         return 1

#     if x <= 0:
#         return 0

#     if x in memo:
#         return memo[x]

#     total = 0
#     for c in coins:
#         total += coin_combination(x - c) % MOD

#     memo[x] = total
#     return total


# print(coin_combination(x))

n, x = map(int, input().split())
coins = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x + 1):
    total = 0
    for c in coins:
        if c > i:
            continue
        total += dp[i - c]
    dp[i] = total % MOD

print(dp[x])
