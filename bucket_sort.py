import read
import time


class BucketSort:

    # Class requires a list of values to work with and maximum value in that list
    def __init__(self, list_to_read, max_v):
        self.list_of_values = list_to_read      # List with values to work with
        self.length = len(self.list_of_values)  # Length of list
        self.max = max_v                        # Maximum value in list
        self.start_time = 0                     # Used for measuring time
        self.duration_time = 0                  # Used for measuring time
        self.buckets = []                       # Creating buckets as list of lists
        for i in range(self.max+1):
            self.buckets.append([])

    # Sorting algorithm
    def sort(self):
        # Starting time counting
        self.start_time = time.time()
        # Value is removed from list and inserted in the last
        # position in bucket with index same as removed value
        for i in range(self.length):
            x = self.list_of_values.pop(0)
            self.buckets[x].append(x)
        # For each bucket
        for j in range(self.max+1):
            # For every value in bucket
            for k in range(len(self.buckets[j])):
                # Remove that value and insert it into list
                buck_val = self.buckets[j].pop(0)
                self.list_of_values.append(buck_val)
        # Count duration time
        self.duration_time = time.time() - self.start_time

    # Used to debug mostly
    def print(self):
        print(self.max)
        print(self.length)
        # print(len(self.buckets[1])+len(self.buckets[2])+len(self.buckets[3])+len(self.buckets[4])+len(self.buckets[5])+len(self.buckets[6])+len(self.buckets[7])+len(self.buckets[8])+len(self.buckets[9])+len(self.buckets[10]))
        # print(self.buckets)
        print(self.list_of_values)

    def print_sort_results(self):
        print(f'Sorted list: {self.list_of_values}')

    def print_sort_time(self):
        print(f'Sort time: {self.duration_time}')


# Testing
# BS = BucketSort(read.list_of_values_max, 10)
# BS.sort()
# BS.print_sort_time()
