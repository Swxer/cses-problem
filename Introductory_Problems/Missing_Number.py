# https://cses.fi/problemset/task/1083
# 8/10/26


def missing_num(n, l):
    sum1 = n * (1 + n) // 2
    sum2 = sum(l)
    return sum1 - sum2


n = int(input())
l = input()

print(missing_num(n, [int(x) for x in l.split()]))
