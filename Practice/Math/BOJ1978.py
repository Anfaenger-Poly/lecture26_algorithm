

n= int(input())
for _ in range(n):
    lst = list(map(int, input().split()))

if n==2:
    lst.append(n)
for i in range(2, n):
    if n % i != 0:
        lst.append(n)

print(lst)