# https://cses.fi/problemset/task/1158
# 20/10/26

n, x = map(int, input().split())
price = list(map(int, input().split()))
pages = list(map(int, input().split()))


def best(money, i):

    if i == n:
        return 0

    skip = best(money, i + 1)
    take = 0

    if price[i] <= money:
        take = pages[i] + best(money - price[i], i + 1)

    return max(skip, take)


print(best(x, 0))
