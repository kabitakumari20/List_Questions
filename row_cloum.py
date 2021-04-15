row=int(input("enter the row="))
cloum=int(input("enter the cloum="))
i=1
a=1
list1=[]
while i<=row:
    b=a
    j=1
    list2=[]
    while j<=cloum:
        list2.append(b)
        j=j+1
        b=b+1
    list1.append(list2)
    i=i+1
    a=a+cloum
print(list1)


