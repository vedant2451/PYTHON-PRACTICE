# Create a function with variable length of arguments
def func1(*num) :
    print("Printing values ")
   
    for i in num :
        print(i)

func1(20,40,60)
func1(80,100)