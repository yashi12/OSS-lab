l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
print(l2)