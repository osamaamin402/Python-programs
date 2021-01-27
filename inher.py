class User:
	name =""
	def __init__(self,a):
		self.name=a;
	def printname(self):
		print("my name is : ",self.name);
class B(User):
	def __init__(self,b):
		self.name=b
	def pt(self):
		print("hi")	

a=input("Enter name : ")
obg=B(a)
obg.printname()
obg.pt()
