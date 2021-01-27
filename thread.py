import threading
class A:
	def cube(self,a):
		print("cube is : ",(a*a*a))

	def sqr(self,a):
		print("Square is : ",(a*a))

if __name__ =="__main__":
	ab=A()
	t1=threading.Thread(target=ab.cube,args=(10,))
	t2=threading.Thread(target=ab.sqr,args=(20,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

			
		