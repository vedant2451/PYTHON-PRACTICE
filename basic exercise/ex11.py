num = int(input("Enter number for reverse order : "))
print("given number",num)
while num > 0 :
    digit = num % 10
    num = num // 10
    print(digit, end =" ")
