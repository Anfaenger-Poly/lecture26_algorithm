p, q = map(int,input().split())
a=[]
for i in range(p):
    if p%(i+1) == 0:
        a.append(i+1)
        
if len(a) < q:
    print(0)

else:
    print(a[q-1])
