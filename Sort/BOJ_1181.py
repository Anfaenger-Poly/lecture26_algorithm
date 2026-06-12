n = int(input())
words = set()
for _ in range(n):
    words.add(input().strip())

words = sorted(words, key = lambda w: (len(w), w))

print('='*20)
print('\n'.join(words))