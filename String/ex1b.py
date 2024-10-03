# Create a string made of the middle three characters
def middle_chars(str1) :

   mi = int(len(str1) / 2)
   res = str1[mi - 1 :mi +2]
   print("Middle three chars are : ",res)


middle_chars("JhonDipPeta")
middle_chars("JaSonAy")