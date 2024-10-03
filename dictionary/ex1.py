# Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

list_dict = dict()
for key in keys :
    for value in values :
        list_dict[key] = value
        values.remove(value)
        break
print("Resultant dictionary is : " ,list_dict)    
