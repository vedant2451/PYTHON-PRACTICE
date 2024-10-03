# Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
print("Orignal string is : ")

lower = []
upper = []

for char in str1 : 
    if char.islower():
        lower.append(char)
    else :
        upper.append(char)
            
sorted_str ="" .join(lower + upper)

print("Result :",sorted_str)            