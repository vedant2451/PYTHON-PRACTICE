# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

chars = []
digits = []
symbol = []

for i in str1 :
    if i.isalpha() :
        chars.append(i)
    elif i.isdigit():
        digits.append(i)
    else :
        symbol.append(i)        

c = len(chars)
d = len(digits)
s = len(symbol)

print("Total counts of chars, digit, and symbols \n", "Chars = ",c,"\nDigits = ", d,"\nSymbol = ",s  )