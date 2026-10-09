# https://cses.fi/problemset/task/1633
# 9/10/26


def combination(n):
    MOD = 10**9 + 7
    ways = [0] * (n + 1)
    ways[0] = 1

    for i in range(1, n + 1):
        for d in range(1, 7):
            if (i - d) >= 0:
                ways[i] = (ways[i] + ways[i - d]) % MOD
    return ways[n]


n = int(input())
print(combination(n))
