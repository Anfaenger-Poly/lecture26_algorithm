alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

l = int(input())
s = input().strip()

r = 31
M = 1234567891

H = 0
p = 1
for i in range(l):
    a = ord(s[i]) - ord('a') + 1
    H = (H + a * p) % M
    p = (p * r) % M

print(H)