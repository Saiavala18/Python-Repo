def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev    
n=int(input())
n1=n*n
t=rev(n)
t1=t*t
if(n1==rev(t1)):
    print("True")
else:
    print("False")    
