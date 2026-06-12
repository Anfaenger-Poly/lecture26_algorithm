def quick_sort(A, left, right):
    if left < right:
        p = partition(A, left, right)
        quick_sort(A, left, p-1)
        quick_sort(A, p+1, right)

def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i + 1


test_cases = [
    [],
    [1],
    [2, 1],
    [5, 2, 4, 1, 3],
    [3, 3, 3, 3],
    [1, 1, 1, 1, 1],
    list(range(10, 0, -1)),
    [7, -3, 0, 7, -3, 5],
]

for t in test_cases:
    a = t[:]
    quick_sort(a, 0, len(a)-1)
    print(t, "->", a, "| 정답?", a == sorted(t))