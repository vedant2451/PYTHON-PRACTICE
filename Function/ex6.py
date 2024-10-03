# Create a recursive function
def sum(a) :
    for i in range(a,0,-1) :
        if i == 1 :
            return 1
        else :
            res = sum(a-1) + i
            return res
        
num  =  int(input("Enter number you want to sum : "))
result = sum(num)
print(result)