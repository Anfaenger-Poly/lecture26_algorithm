from collections import deque


n, k = map(int, input().split())
# queue에 숫자를 모두 집어넣어라
queue = deque()
for i in range(1, n+1):
    queue.append(i)

count = 1
print('<', end='')
while len(queue) > 1:
    person = queue.popleft()
    if count != k:
        queue.append(person)
        count +=1
    else:
        # 출력이 (숫자,공백 숫자)이 나오게
        print(person, end=', ')
        count = 1
        
print(queue.popleft(), end='>')


