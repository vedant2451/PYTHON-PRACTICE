num = int(input("Enter number you want to reverse : "))
s = str(num)
length = len(s)
result = 01
for i in range(0,length ) :
    i = num % 10
    result = result * 10 + i
    num = num //10
print(result)    

