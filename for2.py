a=int(input("Enter a value "))
b=int(input("Enter a value "))
c=int(input("Enter value to skip "))
d=int(input("Enter value to skip "))
for x in range(a,b):
	if (x==c) or (x==d):
		continue;
	
	print(x)