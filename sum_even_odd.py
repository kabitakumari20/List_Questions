list=[23,14,56,12,19,9,15,25,31,42,43]
count_even=0
count_odd=0
i=0
sum1=0
sum2=0
while i<len(list):
    if list[i]%2==0:
        count_even=count_even+1
        sum1=sum1+list[i]
    else:
        count_odd=count_odd+1
        sum2=sum2+list[i]
    i=i+1
print(sum1)
print(sum2)
print(count_even)
print(count_odd)