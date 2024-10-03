# Create a mixed String using the following rules

s1 = "Abc"
s2 = "Xyz"

l1 = len(s1)
l2 = len(s2)

mid1 = int(l1/2)
mid2 = int(l2/2)

x = s1[0]
x= x + s2[l2-1]

x = x + s1[mid1]
x = x + s2[mid2]

x= x + s1[l1-1]
x = x + s2[0]


print(x)