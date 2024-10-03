# Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

third_set = first_set.intersection(second_set)
print("Intersaction is ",third_set)

for item in third_set:
    first_set.remove(item)

print("first set after removing common element ", first_set)