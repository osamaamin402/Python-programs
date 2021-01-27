class A:
    a,b =0,0
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def add(self):
        print(self.a + self.b)
        
class B(A):
    a,b =0,0
   
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def sub(self):
        print(self.a - self.b)    

class C(B):
    a,b =0,0
    
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def mul(self):
        print(self.a * self.b)
class D(C):
    a,b =0,0
    
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def div(self):
        try:
            print(self.a / self.b)
        except Exception as e:
            print("Exception Occoured",e)
        
class E(B):
    a,b =0,0
    
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def mul(self):
        print(self.a * self.b)
    
a = int(input("Enter a Number: "))    
b = int(input("Enter a Number: "))    
obj = D(a,b)
obj.add()
obj.sub()
obj.mul()
obj.div()