import sys

stack=[]

input=sys.stdin.readline

N = int(input())
for _ in range(N):
    operation = input().split()
    if operation[0] == 'push':
        data = int(operation[1])
        stack.append(data)
    elif operation[0] == 'pop':
        # if satck: 스택에 뭐가 있을 때
        if stack: 
            data = stack.pop()
            print(data)
        else:
            print(-1)
    elif operation[0] == 'size':
        print(len(stack))
    elif operation[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif operation[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)