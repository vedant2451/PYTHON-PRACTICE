# Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

for i in range(3) :
        list1[2][1][2].append(sub_list[i])

print(list1)