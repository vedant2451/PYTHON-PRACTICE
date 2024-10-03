# Checks if one set is a subset or superset of another set. If found, delete all elements from that set

first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}


print("First set is subset of second set - " ,first_set.issubset(second_set)) 
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is Super set of second set - " ,first_set.issuperset(second_set))
print("Second set is Super set of First set - " ,second_set.issuperset(first_set))

print("First Set",first_set.clear())  
print("Second Set",second_set)