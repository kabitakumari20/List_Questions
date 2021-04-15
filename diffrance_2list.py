lista=[1,2,3,4,5,6]
listb=[2,3,1,0,6,7]
listc=[ ]
i=0
while i<len(lista):
	if lista[i] not in listb:
		listc.append(lista[i])
	i=i+1
print(listc)

