def is_sorted(row):
    asc=all(row[i]<=row[i+1] for i in range(len(row)-1))
    dec=all(row[i]>=row[i+1] for i in range(len(row)-1))
    return asc or dec
def sortedrow(mat):
    c=0
    for row in mat:
        if is_sorted(row):
            c+=1
    return c        
row,col=map(int,input().split())
mat=[]
for i in range(row):
    row=list(map(int,input().split()))
    mat.append(row)
count=sortedrow(mat)  
print(count)  