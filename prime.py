list=[1,2,3,4,5,6,7,8,9,11,23,45,67,89]
print(len(list))
i=2
while i<len(list):
    b=2
    while b<i:
        if i%b==0:
            print(i,"it is not prime num")
            break
        b=b+1
    else:
        print(i,"it is prime num")
    i=i+1
    
