# https://cses.fi/problemset/task/1069
# 8/10/26


def repetitions(s):
    longest_substring = 1
    current_substring = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_substring += 1
        else:
            current_substring = 1
        longest_substring = max(longest_substring, current_substring)

    return longest_substring


s = input()
print(repetitions(s))
