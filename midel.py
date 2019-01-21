//esaikani
a=[]
b=int(input())
for i in range(1,b+1):
    c=int(input())
    a.append(c)
a.sort()
print(a[int((b-1)/2)])
