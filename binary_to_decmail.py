binary = [1, 0, 0, 1, 1, 0, 1, 1]
a=len(binary)-1
sum=0
mult=1
while a>=0:
    sum=sum+(binary[a]*mult)
    mult=mult*2
    a=a-1
print(sum)


