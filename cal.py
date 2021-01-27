class cal:
	def inp(self):
		a=int(input("enter a number : "))

		b=int(input("enter a number : "))

	def add(self):
		c=a+b
		print("Addition is : ",c)

	def sub(self):
		c=a-b
		print("Substraction is : ",c)

	def mul(self):
		c=a*b
		print("Multiplication is : ",c)

	def div(self):
		c=a/b
		print("Division is : ",c)

obj=cal()

s=int(input("enter operation "))
switch(s)
	case1:
		print("Addition")
		obj.add()
	case2:
		print("Substraction")
		obj.sub()
	case3:
		print("Multiplication")
		obj.mul()
	case4:
		print("Division")
		obj.div()
	default:
		exit()
