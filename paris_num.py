num=30
list=[10,11,12,14,17,18,19]
i=0
b=[]
while i<len(list)-1:
    j=0
    sum=0
    while j<len(list):
        if list[i]+list[j]==30:
            sum=list[i],list[j]
            b.append(sum)
        j=j+1
    i=i+1
print(b)