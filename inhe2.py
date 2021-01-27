class Father:
	fname="1213121"
	def show(self):
		print(self.fname)

		


class Mother:
	mname="121212121"
	def show2(self):
		print(self.mnane)


class Son(Father,Mother):
	sname="jhsad"
	def show3(self):
		print(self.sname)
		print(self.mname)
		print(self.fname)


obj=Son()
obj.show3()