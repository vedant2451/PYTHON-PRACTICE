# Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
mid = int(len(s1)/2)

x = s1[ :mid: ]
x = x + s2
x = x + s1[mid : ]
print(x)