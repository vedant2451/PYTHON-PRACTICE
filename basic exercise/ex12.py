income = int(input("Enter your income $ : "))

if income <= 10000 :
    print("Your income tax payable is : 0 ")
elif income > 10000 and income <=20000 :
       i = ((income - 10000) * 10)// 100
       print("Your income tax payable is :  ",i)
elif income > 20000 :
      s = (10000 * 0)// 100 + (10000 * 10)// 100 + ((income - 20000)*20) // 100
      print("Your income tax payable is :  ",s)     