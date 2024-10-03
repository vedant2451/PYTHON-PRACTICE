# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]



s = list(filter(None,str_list))
print("Original list of sting\n" ,str_list)

print("After removing empty strings\n", s)