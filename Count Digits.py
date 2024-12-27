def countd(n):
    c=0
    if(n<0):
        n=-n
    if(n==0):
        return 1;
    while(n>0):
        r=n%10
        c+=1
        n=n//10
    return c    
n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    lst1.append(countd(i))
print(*lst1)    
