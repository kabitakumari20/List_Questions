a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
j=0
c=[ ]
while i<len(a):
	b=a[i][j]
	j=j+1
	c.append(b)
	i=i+1
print(c)


# 1,5,9


# a=[[4,5,6],[7,8,9],[10,11,12]]
# i=0
# j=2
# while i<len(a):
# 	print(a[i][j])
# 	j=j-1
# 	i=i+1