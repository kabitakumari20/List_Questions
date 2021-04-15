n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i=0
a=[ ]
while i<len(n)-1:
	j=i+1
	while j<len(n):
		if n[i]==n[j]:
			a.append(n[i])
		j=j+1
	i=i+1
b=0
c=[ ]
while b<len(a):
	if a[b] not in c:
		c.append(a[b])
	b=b+1
print(c)