new_list = [1, 2, 3]

# Accesing
assert new_list[0] == 1

# Searching
assert 1 in new_list

for item in new_list:
    if item == 1:
        print(True)
        break

numbers = []
assert len(numbers) == 0

# Adding
numbers.append(2)
numbers.append(200)
assert numbers == [2, 200]

# Deleting
del numbers[0]
assert numbers == [200]
