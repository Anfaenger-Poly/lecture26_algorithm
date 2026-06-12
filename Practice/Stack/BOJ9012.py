T=int(input())

for _ in range(T):
    a=input()
    flag = 0
    stack=[]
    for i in a:
        if i =='(':
            stack.append('(')
        if i == ')':
            if len(stack) == 0:
                print('NO')
                flag = 1
                break
            stack.pop()
    if flag == 0:
        if len(stack) !=0:
            print('NO')
            continue
        print('YES')