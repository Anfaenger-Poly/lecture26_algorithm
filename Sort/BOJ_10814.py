n = int(input())
people = []
for _ in range(n):
    age, name = input().split()
    people.append((int(age), name))

people.sort(key = lambda x: x[0])

out = []
for age, name in people:
    out.append(f'{age} {name}')
print('='*20)
print('\n'.join(out))