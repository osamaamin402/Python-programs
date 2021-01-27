class A:
	def div(self):
		try:
			a=int(input("enter a number : "))
			b=int(input("enter a number : "))
			c=a/b;
			print(c)
		except Exception:
			print("value is infinity ")
obj=A()
obj.div()