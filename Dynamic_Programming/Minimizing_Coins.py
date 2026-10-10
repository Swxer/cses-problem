# https://cses.fi/problemset/task/1634
# 10/10/26

# memo = {}


# def min_coins(x):
#     if x == 0:
#         return 0

#     if x < 0:
#         return INF

#     if x in memo:
#         return memo[x]

#     best = INF
#     for c in coins:
#         best = min(best, 1 + min_coins(x - c))

#     memo[x] = best
#     return best


# result = min_coins(x)
n, x = map(int, input().split())
coins = sorted(set(map(int, input().split())))

INF = 10**9
dp = [INF] * (x + 1)
dp[0] = 0

for total in range(1, x + 1):
    best = INF
    for c in coins:
        if c > total:
            break
        v = dp[total - c]
        if v < best:
            best = v
    dp[total] = best + 1

print(-1 if dp[x] >= INF else dp[x])
