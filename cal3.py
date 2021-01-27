class A:
	def __init__(self,c,d):
		self.aa=c
		self.bb=d
	def add(self):
		return self.aa+self.bb
	def sub(self):
		return self.aa-self.bb
	def mul(self):
		return self.aa*self.bb
	def div(self):
		return self.aa/self.bb
	
a=int(input("enter a number : "))

b=int(input("enter a number : "))
obj=A(a,b)
print("0 for Exit")
print("1 for Addition")
print("2 for Substraction")
print("3 for Multiplication")
print("4 for Devision")
ch=1
while ch !=0:
	ch=int(input("enter choice : "))
	if ch==1:
		print("my Addition is :",obj.add())

	elif ch==2:
		print("my Addition is :",obj.div())
	elif ch==3:
		print("my Addition is :",obj.mul())
	elif ch==4:
		print("my Addition is :",obj.div())			