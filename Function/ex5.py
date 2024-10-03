# Create an inner function to calculate the addition in the following way
def func1(a,b) :
    def func2(a,b) :
        
        return a + b
    add = func2(a,b)
    return add + 5

result = func1(5,2)
print(result)
    
    