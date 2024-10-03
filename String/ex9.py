# Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
total = 0
cnt = 0
for char in str1 :
    if char.isdigit() :
        total += int(char)
        cnt += 1
    else :
        continue


avg = total / cnt

print("Sum is: ",total ,"Average is ",avg)
        