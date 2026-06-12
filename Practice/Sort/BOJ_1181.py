import sys
n = int(sys.stdin.readline())
words = set()
for _ in range(n):
    words.add(sys.stdin.readline().strip())

words = sorted(words, key = lambda w: (len(w), w))
print('\n'.join(words))



n = int(input())
words = set()
for _ in range(n):
    words.add(input().strip())

words = sorted(words, key = lambda w: (len(w), w))

print('='*20)
print('\n'.join(words))