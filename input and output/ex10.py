# Read line number 4 from the following file
with open("input and output/test.txt", "r") as fp:
   
    lines = fp.readlines()
    
    print(lines[3])
