n = int(input())

count = 1  
start = 1
end = 1
total_sum = 1

while end != n:
    if total_sum == n:
        count += 1
        end += 1
        total_sum += end
    elif total_sum < n:
        end += 1
        total_sum += end
    else:
        total_sum -= start
        start += 1

print(count)