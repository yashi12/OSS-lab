def func(val):
    return val%2==0

def filter(f,a):
    x1=[x for x in a if func(x) ]
    return x1

x=[234,341,3,16,4621,453,26,4531,312,246]
print(filter(func,x))