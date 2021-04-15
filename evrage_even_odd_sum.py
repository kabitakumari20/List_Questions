list=[23,14,56,12,19,9,15,25,31,42,43]
odd=0
even=0
i=0
esum=0
osum=0
avrage1=0
avrage2=0
while i<len(list):
    if list[i]%2==0:
        esum=esum+list[i]
    else:
        osum=osum+list[i]
    i=i+1
    avrage1=esum//4
    avrage2=osum//7
print(avrage2)
print(avrage2)