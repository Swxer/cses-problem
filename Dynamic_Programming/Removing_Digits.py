# https://cses.fi/problemset/task/1637
# 13/10/2026


n = int(input())
# memo = {}


# def remove_digit(x):
#     if x == 0:
#         return 0

#     if x in memo:
#         return memo[x]

#     best = float("INF")
#     for d in str(x):
#         digit = int(d)
#         if digit > 0:
#             best = min(best, 1 + remove_digit(x - digit))

#     memo[x] = best

#     return best


dp = [float("INF")] * (n + 1)
dp[0] = 0

for x in range(1, n + 1):
    for d in str(x):
        digit = int(d)
        if digit > 0:
            dp[x] = min(dp[x], 1 + dp[x - digit])

print(dp[n])
