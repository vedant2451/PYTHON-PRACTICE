# Removal all characters from a string except integers

str1 = " I am 25 years and 10 months old "
str2 = []
for char in str1 :
    if char.isdigit() :
        str2.append(char)
my_string = ''.join(str2)        

print(my_string)        