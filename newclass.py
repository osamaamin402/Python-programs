class User:
	name =""
	def __init__(self,a):
		self.name=a;
	def printname(self):
		print("my name is : ",self.name);
a=input("Enter name : ")
obj=User(a)
obj.printname()
