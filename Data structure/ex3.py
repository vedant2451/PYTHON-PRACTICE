# Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l = len(sample_list) #length of list
d = l/3  #divide list in 3 equal part
n = 1 
             
for i in range(0,l,3) :
     print("Chunk ",n )
     s = sample_list[i:i+3] 
     print(s)
     print("After reversing it ",list(reversed(s)))
     n += 1