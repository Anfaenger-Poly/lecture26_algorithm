def getGCD(m, n):
    if m > n:
        m, n = n, m
        result = 1
    for num in range(m, 0, -1):
        if m % num == 0 and n % num == 0:
            result = num
            break
    return result


def getLCM(m, n):
    gcd_value = getGCD(m, n)
    answer = (m * n) // gcd_value
    return answer


count_str = input()
t = int(count_str)


for i in range(t):

    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])
    
    result = getLCM(a, b)
    print(result)