# Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

for i in range(4) :
    print(list1[i],list2[i])

# for x, y in zip(list1, list2[::-1]):
#     print(x, y)