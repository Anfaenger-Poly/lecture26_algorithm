from collections import deque

queue = deque()

n = int(input())

for _ in range(n):
    oplst = input().split()

    if oplst[0] == 'push':
        data = int(oplst[1])
        queue.append(data)

    elif oplst[0] == 'pop':
        # queue에 뭐가 있으면 -> if queue: (len써도 되지만 길다)
        if queue:
            data = queue.popleft()
            print(data)
        else:
            print(-1)
    elif oplst[0] == 'size':
        print(len(queue))
    elif oplst[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif oplst[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif oplst[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
