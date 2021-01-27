import math
class Polygon:
	def no_of_site(self):
		return 0

	def area(self):
		return 0

	def parameter(self):
		return 0




class Trangle(Polygon):
	def no_of_site(self):
		return print("no_of_site : ",3)
	def area(self,h,w):
		return print("Area : ",h*w)

	def parameter(self,a,b,c):
		if a+b>c:
			return a+b+c
		else:
			return print("grater")





class Rohimbus(Polygon):
	def no_of_site(self):
		return print("no_of_site : ",4)

	def area(self,a,b):
		return print("area",((a*b)/2))

	def parameter(self,a):
		return 4*a
		
	
class Pentagon(Polygon):
	def no_of_site(self):
		return print("no_of_site : ",5)

	def area(self,a):
		return print("Area",(1/4 * math.sqrt(5*(5+2*math.sqrt(5)))*a**2))
		
	def parameter(self,a):
		return 5*a
t=Trangle()
t.no_of_site()
t.area(2,4)
t.parameter(2,3,9)

r=Rohimbus()
r.no_of_site()
r.area(4,5)
r.parameter(6)

p=Pentagon()
p.no_of_site()
p.area(5)
p.parameter(6)