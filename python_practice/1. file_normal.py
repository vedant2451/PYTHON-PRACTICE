# # Reading a File
# file = open("python_practice/example.txt", "r")
# # content = file.read()
# content1 = file.readline()
# print(content1)
# file.close()

# # Writing to a File
# file = open("python_practice/example.txt", "w")
# file.write("This is an example of writing to a file.\n    hello i am vedant suthar \n")
# file.write("This will overwrite the file if it already exists.\n")
# file.close()

# # Appending to a File
# file = open("python_practice/example.txt", "a")
# file.write("This line is added to the file without overwriting existing content.\n")
# file.close()

# # Reading a File Line by Line
# file = open("python_practice/example.txt", "r")
# for line in file:
#     print(line)  # strip() removes newline characters
# file.close()

# # Writing a List of Lines to a File
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# file = open("python_practice/example.txt", "w")
# file.writelines(lines)
# file.close()
