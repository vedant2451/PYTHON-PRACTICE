import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

replace_char = "#"

for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)