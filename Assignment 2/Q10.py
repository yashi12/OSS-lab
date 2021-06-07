
ofile=open("file.txt","r")
k=ofile.readlines()
for i in k:
    print(i[::-1])