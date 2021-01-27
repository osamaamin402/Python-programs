fileptr=open("myfile.txt","r")
count=fileptr.read()
print(count)
print("word count :",fileptr.tell())
