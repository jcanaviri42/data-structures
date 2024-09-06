import time
import random


def minimum_index(values):
    index = 0

    for i in range(len(values)):
        if values[i] < values[index]:
            index = i
    return index


def selection_sort(values):
    sorted_list = []

    for _ in range(len(values)):
        index = minimum_index(values)
        sorted_list.append(values.pop(index))
    return sorted_list


time_0 = time.time()
sorted_numbers = selection_sort([random.randint(0, 99) for _ in range(10000)])
time_1 = time.time()
print(round(time_1 - time_0, 4), 'seconds.')
