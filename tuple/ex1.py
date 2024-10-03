# Reverse the tuple

tuple1 = (10, 20, 30, 40, 50)
temp = list(tuple1)
temp.reverse()
tuple1 = tuple(temp)
print(tuple1)