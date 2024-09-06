def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return None


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
# The target 9 is in the index 8 of the array of items
assert linear_search(items, target) == 8
# The target 17 does not exist so the result is None
assert linear_search(items, 17) == None


def binary_search(items, target):
    first = 0
    last = len(items) - 1

    while first <= last:
        middle = (first + last) // 2
        guess = items[middle]
        if guess == target:
            return middle
        elif guess < target:
            first = middle + 1
        else:
            last = middle - 1

    return None


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 2
# The target 2 is in the index 1 of the array of items
assert binary_search(items, target) == 1
# The target 23 is not in the array of items
assert binary_search(items, 23) == None


def binary_search_recursive(items, target):
    if len(items) == 0:
        return False

    middle = len(items) // 2
    guess = items[middle]
    if guess == target:
        return True
    elif guess < target:
        return binary_search_recursive(items[middle + 1 :], target)
    else:
        return binary_search_recursive(items[:middle], target)


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
# The target 9 is in the array of items
assert binary_search_recursive(items, target)
# The target 23 is not in the array of items
assert not binary_search_recursive(items, 23)
