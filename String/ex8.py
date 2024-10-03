# Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
s = str1.lower()
countstring = s.count("usa")
print("The USA count is: " ,countstring)