# https://cses.fi/problemset/task/1094
# 9/10/26


# def increasing_arr(n, l):
#     min_move = 0

#     for i in range(1, n):
#         if l[i] < l[i - 1]:
#             diff = l[i - 1] - l[i]
#             l[i] = l[i - 1]
#             min_move += diff

#     return min_move


def increasing_arr(l):
    total = 0
    highest = l[0]

    for x in l[1:]:
        if x < highest:
            total += highest - x
        else:
            highest = x

    return total


n = int(input())
l = [int(x) for x in input().split()]
print(increasing_arr(l))
