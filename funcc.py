class A:
	
	def add(self):
		a=int(input("Enter a number : "))
		b=int(input("Enter a number : "))
		c=a+b
		print(c)

class B(A):
	def sub(self):
		a=int(input("Enter a number : "))
		b=int(input("Enter a number : "))
		
		c=a-b
		print(c)

class C(B):
	def mul(self):
		a=int(input("Enter a number : "))
		b=int(input("Enter a number : "))
		
		c=a*b
		print(c)
class D(C):
	def fileh(self):
		try:
			f=open("a.txt","r")
		except Exception as e:
			print("file not found")
		
obj=D()
obj.add()
obj.sub()
obj.mul()
obj.fileh()