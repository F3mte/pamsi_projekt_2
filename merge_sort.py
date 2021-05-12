import read
from time import time


def merge(s1, s2, s):

    while s1 and s2:

        if s1[0] <= s2[0]:
            x = s1.pop(0)
            s.append(x)

        else:
            x = s2.pop(0)
            s.append(x)

    while s1:
        x = s1.pop(0)
        s.append(x)

    while s2:
        x = s2.pop(0)
        s.append(x)


def merge_sort(s):

    s_len = len(s)

    if s_len > 1:
        s1 = s[:s_len//2]
        s2 = s[s_len//2:]
        merge_sort(s1)
        merge_sort(s2)
        s.clear()
        merge(s1, s2, s)
        return s


# We specify input value and last index
# input_list = read.list_of_values_max

# Testing and measuring time
# start_time = time()
# result = merge_sort(input_list)
# duration_time = time() - start_time

# Printing results
# print(result)
# print(f'Sort time: {duration_time}')
