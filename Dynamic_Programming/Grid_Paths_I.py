# https://cses.fi/problemset/task/1638
# 14/10/2026
import sys

sys.setrecursionlimit(10000)
n = int(input())
grid = [input() for _ in range(n)]

MOD = 10**9 + 7

# memo = {}


# def paths(row, col):
#     if row >= n or col >= n:
#         return 0
#     if grid[row][col] == "*":
#         return 0
#     if (row, col) == (n - 1, n - 1):
#         return 1
#     if (row, col) in memo:
#         return memo[(row, col)]

#     count = 0
#     count += (paths(row + 1, col) + paths(row, col + 1)) % MOD

#     memo[(row, col)] = count
#     return count


# print(paths(0, 0))

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1 if grid[0][0] == "." else 0

for row in range(n):
    for col in range(n):
        if grid[row][col] == "*":
            dp[row][col] = 0
        elif (row, col) != (0, 0):
            above = dp[row - 1][col] if row > 0 else 0
            left = dp[row][col - 1] if col > 0 else 0
            dp[row][col] = (left + above) % MOD

print(dp[n - 1][n - 1])
