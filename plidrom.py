name=["n","i","t","i","n"]
a=len(name)
i=a-1
b=[ ]
while i>=0:
	b.append(name[i])
	i=i-1
if name==b:
	print("it is palidrom",b)
else:
	print("it is not palidrom",b)