orig_num = int(input("Enter number : "))
print("orignal number ",orig_num)
num = orig_num
rev_num = 0
while num > 0 :
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10

int(rev_num)
if orig_num == rev_num :
    print("Yes. given number is palindrome number ")
else :
    print("No. given number is not palindrome number ") 