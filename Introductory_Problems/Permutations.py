# https://cses.fi/problemset/task/1070
# 9/10/26


def perm(n):
    odd = list(range(1, n + 1, 2))
    even = list(range(2, n + 1, 2))

    return even + odd


n = int(input())
if n in [2, 3]:
    print("NO SOLUTION")
else:
    print(*perm(n))
