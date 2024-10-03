# Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print("Element at odd index position from list one")
print(l1[1: :2])

print("Element at even index position from list two")
print(l2[ : : 2])

print("Printing final third element")
print(l1[1: :2] + l2[: : 2])