# https://cses.fi/problemset/task/1068
# 8/10/2026


def weird_algo(n):
    result = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        result.append(n)
    return result


n = int(input())
print(*weird_algo(n))
