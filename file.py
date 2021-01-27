#File I/O
#f=open(name,mode,buffer)


f=open("myfile.txt","r+")

f.write("#For loop")
a=f.read()
print(a)
f.close()	