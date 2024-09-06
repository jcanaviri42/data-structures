import time
import random


def quicksort(values):
    if len(values) <= 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []

    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


time_0 = time.time()
sorted_numbers = quicksort([random.randint(0, 99) for _ in range(10000)])
time_1 = time.time()
print(round(time_1 - time_0, 4), "seconds.")
