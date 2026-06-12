n, m = map(int, input().split())
numlst = list(map(int, input().split()))

answer = 0
start = 0
end = 0
sum = 0

answer = 0
start = end = 0
sum = numlst[0]
while end < n:
    if sum == m:
        answer += 1
    if sum <= m:
        end +=1
        if end<n:
            sum += numlst[end]
    else:
        sum -= numlst[start]
        start += 1
print(answer)