# max_list=[1,2,3,15,7,18,6,10]
# i=0
# max=max_list[0]
# secound_max=max_list[0]
# while i<len(max_list):
#     if max_list[i]>max:
#         max=max_list[i]
#     i=i+1
#     # print(max)
#     j=0
#     while j<len(max_list):
#         if max>max_list[j] and secound_max<max_list[j]:
#             secound_max=max_list[j]
#         j=j+1
# print(secound_max)

n=[40,23,70,56,12,5,100,7]
max=(n[0])
sec=(n[0])
i=0
while i<len(n):
    if n[i]>max :
        max=n[i]
    i+=1
    j=0
    while j<len(n):
        if max>n[j] and sec<n[j]:
            sec=n[j]
        j=j+1
print(sec)