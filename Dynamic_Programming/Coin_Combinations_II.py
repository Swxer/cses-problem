# https://cses.fi/problemset/task/1636
# 11/10/26

n, x = map(int, input().split())
coins = list(map(int, input().split()))

memo = {}
MOD = 10**9 + 7


def coin_combination(x, i):
    if x == 0:
        return 1

    if x < 0:
        return 0

    if (x, i) in memo:
        return memo[(x, i)]

    total = 0

    for j in range(i, len(coins)):
        if j >= i:
            total += coin_combination(x - coins[j], j)

    memo[(x, i)] = total % MOD
    return total


print(coin_combination(x, 0))
