import time
import random


def is_sorted(array):
    """Checks if the array is sorted"""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


def bubble_sort(values):
    """Bubble Sort"""
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]
    return values

# To see the execution time
time_0 = time.time()
sorted_numbers = bubble_sort([random.randint(0, 99) for _ in range(10000)])
time_1 = time.time()
print(round(time_1 - time_0, 4), "seconds.")
