n, m = map(int, input().split())
lsst = []
pa = list(map(int, input().split()))
pb = list(map(int, input().split()))
x=0
y=0
        
while x < n and y < m:
    if pa[x] < pb[y]:
        lsst.append(pa[x])
        x += 1
    elif pa[x] >= pb[y]:
        lsst.append(pb[y])
        y += 1
while x < n:
    lsst.append(pa[x])
    x += 1
while y < m:
    lsst.append(pb[y])
    y += 1

for i in lsst:
    print(i, end=" ")