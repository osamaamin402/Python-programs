class Family:
	def __init__(self,name):
		self.name = name


class Father(Family):
	def __init__(self,name,age):
		#self.name=name
		self.age=age
		Family.__init__(self,name)

obj=Father("Amin",20)
print(obj.name)
print(obj.age)