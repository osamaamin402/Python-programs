def changevalue(aa):
	aa.append([4,5,6,7])
	print("Inside function: ",aa)
	return

a=[1,2,3]
changevalue(a)
print("outside function :",a)
