import string
def mutate(d):
    res=[]
    for i in range(len(d)+1):
        temp=[d[:i]+a+d[i:] for a in string.ascii_lowercase]
        res.extend(temp)
    temp=[d[:i]+d[i+1:] for i in range(len(d))]
    res.extend(temp)
    for i in range(len(d)+1):
        temp=[d[:i]+a+d[i+1:] for a in string.ascii_lowercase]
        res.extend(temp)
    for i in range(len(d)-1):
        res.append(d[:i]+d[i+1]+d[i]+d[i+2:])
    return res
print(  mutate('hello'))
