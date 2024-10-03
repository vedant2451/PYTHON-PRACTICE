str = input("enter String : ")
print("orignal string : ",str)
print("Printing only even index char")
size = len(str)
for i in range(0,size-1,2) :
    print(str[i])


