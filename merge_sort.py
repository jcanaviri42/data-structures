import time
import random


def split(array):
    """Returns two sublist left an right
    Takes O(log n) time"""
    middle = len(array) // 2

    return array[:middle], array[middle:]


def merge(left, right):
    """Merges two arrays sorting them in the process
    Runs in O(n) time"""
    l = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def merge_sort(array):
    """Sorts a array in ascending orden
    Takes O(n log n) time"""
    # Divide: find the midpoint of the array
    # Conquer: Recursively sort the subarrays
    # Combine: Merge the sorted subarrays
    if len(array) <= 1:
        return array

    left_half, right_half = split(array)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def verify_sorted(array):
    if len(array) == 0 or len(array) == 1:
        return True

    return array[0] < array[1] and verify_sorted(array[1:])


time_0 = time.time()
sorted_numbers = merge_sort([random.randint(0, 99) for _ in range(10000)])
time_1 = time.time()
print(round(time_1 - time_0, 4), 'seconds.')
