def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, right)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right, temp):
    k = i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp[k] = A[i]
            k, i = k + 1, i + 1
        else:
            temp[k] = A[j]
            k, j = k + 1, j + 1

    if i > mid:
        temp[k:k + right - j + 1] = A[j:right + 1]
    else:
        temp[k:k + mid - i + 1] = A[i:mid + 1]

    A[left:right + 1] = temp[left:right + 1]


def merge_sort(A, left, right, temp):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid, temp)
        merge_sort(A, mid + 1, right, temp)
        merge(A, left, mid, right, temp)


def sort(A):
    temp = [0] * len(A)
    merge_sort(A, 0, len(A) - 1, temp)


if __name__ == "__main__":
    data = [10, 12, 15, 20, 27, 13, 22, 25]
    print("정렬 전:", data)
    sort(data)
    print("정렬 후:", data)