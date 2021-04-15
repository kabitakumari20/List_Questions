# magic= [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# i=0
# r1=0
# r2=0
# r3=0
# c1=0
# c2=0
# c3=0
# d1=0
# d2=0
# while i<len(magic):
#         r1=r1+magic([0][i])
#         r2=r2+magic([1][i])
#         r3=r3+magic([2][i])
#         c1=c1+magic([i][0])
#         c2=c2+magic([i][1])
#         c3=c3+magic([i][2])
#         d1=d1+magic([i][i])
#         d2=d2+magic([i][2-i])
#         i=i+1
# if r1==r2==r3==c1==c2==c3==d1==d2:
#     print("magic square")
# else:
#     print("not magic square")

magic= [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
magic = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]]
i=0
while i<len(magic):
    j=0
    row_sum=0
    colum_sum=0
    while j<len(magic[i]):
        colum_sum=colum_sum+magic[i][j]
        row_sum=row_sum+magic[j][i]
        j=j+1
    i=i+1
print(colum_sum)
print(row_sum)
c=0
diagonal_sum=0
while c<len(magic):
    d=0
    while d<len(magic):
        if c==d:
            diagonal_sum=diagonal_sum+magic[c][d]
            d=d+1
        c=c+1
print(diagonal_sum)
if colum_sum==row_sum and colum_sum==diagonal_sum:
    print("it is magic")
else:
    print("it is not magic")
