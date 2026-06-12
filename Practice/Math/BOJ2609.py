
def getGCD(m, n):
    if m>n:
        # m이 작은 수가 되도록
        m, n = n, m

    for num in range(m, 0 ,-1):
        if m%num == 0 and n%num ==0 :
            # 최대공약수
            return num

def getLCM(m, n):
    if m>n:
        # m이 작은 수가 되도록
        m, n = n, m
    # 큰 숫자 n의 배수를 구하면서,m의 베수인지 확인
    # 최소공배수 -> 공배수 중 가장 작은 애 -> 처음 만나는 애
    i = 1
    while True:
        mulitiple = n*i
        # m의 배수인지 확인
        if mulitiple%m == 0:
            return mulitiple
        i += 1

m, n = map(int,input().split())

print(getGCD(m, n))
print(getLCM(m, n))
