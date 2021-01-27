class A:
	def div(self):
		try:
	f=open("file.txt","r")
except IOError:
	print("file not found : ")
obj=A()
obj.div()