# https://cses.fi/problemset/task/1638
# 14/10/2026
import sys

sys.setrecursionlimit(10000)
n = int(input())
grid = [input() for _ in range(n)]

MOD = 10**9 + 7

memo = {}


def paths(row, col):
    if row >= n or col >= n:
        return 0
    if grid[row][col] == "*":
        return 0
    if (row, col) == (n - 1, n - 1):
        return 1
    if (row, col) in memo:
        return memo[(row, col)]

    count = 0
    count += (paths(row + 1, col) + paths(row, col + 1)) % MOD

    memo[(row, col)] = count
    return count


print(paths(0, 0))
