occurence= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
a=[ ]
i=0
while i<len(occurence):
	j=0
	b=[ ]
	count=0
	while j<len(occurence):
		if occurence[i]==occurence[j]:
			count=count+1
		j=j+1
	b.append(occurence[i])
	b.append(count)
	if b not in a:
		a.append(b)
	i=i+1
print(a)