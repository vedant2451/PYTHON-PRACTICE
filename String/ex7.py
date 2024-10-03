# String characters balance Test

def stringcheck(str1,str2) :
    flag = True
    for i in str1 :
        if i in str2 :
            continue
        else :
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = stringcheck(s1,s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = stringcheck(s1, s2)
print("s1 and s2 are balanced:", flag)

