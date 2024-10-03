# Find the sum of the series up to n terms
n = 5
start = 2 
sum_sqn = 0
for i in range(1,6) :
    print(start , end =" ")
    sum_sqn += start
    start = start * 10 + 2
print("\nsum of above series is : ",sum_sqn)    
