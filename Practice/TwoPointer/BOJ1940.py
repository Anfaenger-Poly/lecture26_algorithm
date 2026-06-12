
n = int(input())
m = int(input())
numlst = list(map(int, input().split()))
numlst.sort()

answer = 0
start = 0      
end = n - 1    


while start < end:
    sum = numlst[start] + numlst[end]
    
    if sum == m:
        answer += 1
        start += 1
        end -= 1
    elif sum < m:
        start += 1
    else:
        end -= 1

print(answer)