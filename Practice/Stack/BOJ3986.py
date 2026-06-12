import sys

n = int(sys.stdin.readline().strip())
gd_wd_count = 0

for _ in range(n):
    wd = sys.stdin.readline().strip()
    stack = []
    
    for char in wd:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    if not stack:
        gd_wd_count += 1

print(gd_wd_count)