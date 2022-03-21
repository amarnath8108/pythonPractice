lsit1 =[1,2,3,3,4,5]
list2= []
for i in range(0,len(lsit1)):
    if lsit1.count(lsit1[i]) > 1 and lsit1[i] not in list2:
        print(lsit1[i])
        list2.append(lsit1[i])
