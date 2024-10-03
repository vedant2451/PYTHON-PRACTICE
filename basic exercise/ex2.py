print("Printing current and previous number sum in a range(10)")
previous_num = 0
for i in range(0,10) :
    s = previous_num + i
    print("Current Number ", i , "Previous Number ", previous_num , "Sum : ", s)
    previous_num = i
      