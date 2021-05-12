import sys
from time import time
import read
import bucket_sort as bs
import quick_sort as qs
import merge_sort as ms

# Specify which algorithm to use and size of test list
sort_alg = sys.argv[1]
list_size = sys.argv[2]
try:
    print_result = sys.argv[3]
except:
    print_result = ''

print(f'Start sorting for {sort_alg} algorithm')
print(f'For list of {list_size} elements')
print('-----------------------------------------')

if sort_alg == 'bucket_sort':
    if list_size == '100':
        BS = bs.BucketSort(read.list_of_values_100, 10)
        BS.sort()
        if print_result == 'result_on':
            BS.print_sort_results()
        BS.print_sort_time()
    if list_size == '10k':
        BS = bs.BucketSort(read.list_of_values_10k, 10)
        BS.sort()
        if print_result == 'result_on':
            BS.print_sort_results()
        BS.print_sort_time()
    if list_size == '100k':
        BS = bs.BucketSort(read.list_of_values_100k, 10)
        BS.sort()
        if print_result == 'result_on':
            BS.print_sort_results()
        BS.print_sort_time()
    if list_size == '500k':
        BS = bs.BucketSort(read.list_of_values_500k, 10)
        BS.sort()
        if print_result == 'result_on':
            BS.print_sort_results()
        BS.print_sort_time()
    if list_size == 'max':
        BS = bs.BucketSort(read.list_of_values_max, 10)
        BS.sort()
        if print_result == 'result_on':
            BS.print_sort_results()
        BS.print_sort_time()

if sort_alg == 'quick_sort':
    if list_size == '100':
        # We specify input value and last index
        input_list = read.list_of_values_100
        last_index = len(input_list) - 1
        # Testing and measuring time
        start_time = time()
        result = qs.quick_sort(input_list, 0)
        # in_place_quick_sort(input_list, 0, last_index)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == '10k':
        # We specify input value and last index
        input_list = read.list_of_values_10k
        last_index = len(input_list) - 1
        # Testing and measuring time
        start_time = time()
        result = qs.quick_sort(input_list, 0)
        # in_place_quick_sort(input_list, 0, last_index)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == '100k':
        # We specify input value and last index
        input_list = read.list_of_values_100k
        last_index = len(input_list) - 1
        # Testing and measuring time
        start_time = time()
        result = qs.quick_sort(input_list, 0)
        # in_place_quick_sort(input_list, 0, last_index)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == '500k':
        # We specify input value and last index
        input_list = read.list_of_values_500k
        last_index = len(input_list) - 1
        # Testing and measuring time
        start_time = time()
        result = qs.quick_sort(input_list, 0)
        # in_place_quick_sort(input_list, 0, last_index)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == 'max':
        # We specify input value and last index
        input_list = read.list_of_values_max
        last_index = len(input_list) - 1
        # Testing and measuring time
        start_time = time()
        result = qs.quick_sort(input_list, 0)
        # in_place_quick_sort(input_list, 0, last_index)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')

if sort_alg == 'merge_sort':
    if list_size == '100':
        # We specify input value and last index
        input_list = read.list_of_values_100
        # Testing and measuring time
        start_time = time()
        result = ms.merge_sort(input_list)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == '10k':
        # We specify input value and last index
        input_list = read.list_of_values_10k
        # Testing and measuring time
        start_time = time()
        result = ms.merge_sort(input_list)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == '100k':
        # We specify input value and last index
        input_list = read.list_of_values_100k
        # Testing and measuring time
        start_time = time()
        result = ms.merge_sort(input_list)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == '500k':
        # We specify input value and last index
        input_list = read.list_of_values_500k
        # Testing and measuring time
        start_time = time()
        result = ms.merge_sort(input_list)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
    if list_size == 'max':
        # We specify input value and last index
        input_list = read.list_of_values_max
        # Testing and measuring time
        start_time = time()
        result = ms.merge_sort(input_list)
        duration_time = time() - start_time
        # Printing results
        if print_result == 'result_on':
            print(result)
        print(f'Sort time: {duration_time}')
