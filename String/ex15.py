# Remove special symbols / punctuation from a string
import string
str1 = "/*Jon is @developer & musician"
print("Orignal string is ",str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)