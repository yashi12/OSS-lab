# read the entire file as one string
myfile = open('file.txt') 
data = myfile.read()
print(data)
myfile.close()   

myfile = open('file.txt') 
myline = myfile.readline()
while myline:
    print(myline)
    myline = myfile.readline()
myfile.close()   
# process the lines


with open('filename.txt' , 'wt') as f:
    f.write ('hi there, this is a first line of file.\n')
    f.write ('and another line.\n')

f = open("filename.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()