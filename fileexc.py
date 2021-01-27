try:
	f=open("file.txt","r")
except IOError:
	print("file not found : ")