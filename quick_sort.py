import read
from time import time
from random import randint


def in_place_partition(list_of_values, a, b):
    pivot = list_of_values[b]   # Pivot at the last index
    l = a                       # First index in partition
    r = b-1                     # Last index in partition
    # We loop until l is bigger then r
    while l <= r:
        # We increment l, until we find value bigger then our pivot
        while l <= r and list_of_values[l] <= pivot:
            l = l + 1
        # We decrement r, until we find value smaller then our pivot
        while l <= r and list_of_values[r] >= pivot:
            r = r - 1
        # We have to check if l <= r, otherwise at the end of partitioning we may swap unnecessarily
        if l <= r:
            # We swap found values
            list_of_values[l], list_of_values[r] = list_of_values[r], list_of_values[l]
        else:
            # At the end, we let main loop check if l <= r, end let it end
            pass
    # We swap pivot at last index with value at index l
    list_of_values[l], pivot = pivot, list_of_values[l]
    # We return current pivot position
    return l


def in_place_quick_sort(list_of_values, a, b):

    if a >= b:                     # If first index of segment is equal or greater than last last, sorting is done
        return

    i = randint(a, b)                                                                # We pick random index as pivot
    list_of_values[i], list_of_values[b] = list_of_values[b], list_of_values[i]      # We swap pivot with last index

    l = in_place_partition(list_of_values, a, b)         # Partition
    in_place_quick_sort(list_of_values, a, l - 1)        # Sort for first half
    in_place_quick_sort(list_of_values, l + 1, b)        # Sort for second half


def quick_sort(array, pivot_index):

    # If list has only 1 value, sorting is done
    if len(array) <= 1:
        return array

    l = []      # List for values smaller than pivot
    e = []      # List for values equal to pivot
    g = []      # List for values bigger than pivot

    # We remove pivot from list
    x_p = array.pop(pivot_index)

    # For every value in list
    for i in range(len(array)):
        y = array.pop(0)    # First value in list is removed
        if y < x_p:         # If first value is smaller than pivot, its added at the end of list l
            l.append(y)
        elif y == x_p:      # If first value is equal to pivot, its added at the end of list e
            e.append(y)
        elif y > x_p:       # If first value is greater than pivot, its added at the end of list g
            g.append(y)
    # Return list e, on others, we still perform sorting
    return quick_sort(l, 0)+e+quick_sort(g, 0)


# We specify input value and last index
# input_list = read.list_of_values_10k
# last_index = len(input_list)-1

# Testing and measuring time
# start_time = time()
# result = quick_sort(input_list, 0)
# in_place_quick_sort(input_list, 0, last_index)
# duration_time = time() - start_time

# Printing results
# print(result)
# print(f'Sort time: {duration_time}')
