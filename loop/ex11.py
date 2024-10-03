start = 25
end = 50
print("Prime number between",start, "and" , end, "are:")
for i in range(25,51) :
    if i % 2 == 0 :
        continue
    elif i % 3 == 0 :
        continue
    elif i % 5 == 0 :
        continue
    elif i % 7 == 0 :
        continue
    else :
        print(i)



for num in range(start, end + 1) :
    if num > 1 :
        for i in range(2,num) :
            if(num % i)== 0 :
                break 
        else :
                print(num)       