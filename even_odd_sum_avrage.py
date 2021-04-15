list=[23,14,56,12,19,9,15,25,31,42,43]
i=0
esum=0
osum=0
count1=0
count2=0
avrage1=0
avrage2=0
while i<len(list):
    if list[i]%2==0:
        count1=count1+1
        esum=esum+list[i]
    else:
        count2=count2+1
        osum=osum+list[i]
        avrage=osum//count2
    i+=1
print(count1)
print(count2)
print(count1+count2,"tatal count")
print(esum)
print(osum)
print(esum+osum,"total sum")
print(avrage1)
print(avrage2)
print(avrage1+avrage2,"tatal avrage")