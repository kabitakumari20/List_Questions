a=[20,18,17,20,17,4,2,18,2,4]
i=0
b=[ ]
count=0
while i<len(a):
	if a[i] not in b:
		b.append(a[i])
		count=count+1
	i=i+1
print(b)

