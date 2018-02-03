def insert_sort(arr):
    for i in range(len(arr) - 2, -1, -1):
        key = arr[i]
        j = i + 1
        while j < len(arr) and arr[j] < key:
            arr[j - 1] = arr[j]
            j += 1
        arr[j - 1] = key


arr = [3, 1, 2, 4, 2, 1]
insert_sort(arr)
print(*arr)


def binary_search(arr, find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == find:
            return mid
        elif arr[mid] < find:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, find, left, right):
    if left > right:
        return -1
    mid = (right + left) // 2
    if arr[mid] == find:
        return mid
    elif arr[mid] < find:
        return binary_search_recursive(arr, find, mid + 1, right)
    else:
        return binary_search_recursive(arr, find, left, mid - 1)


print(binary_search_recursive(arr, 5, 0, len(arr) - 1))
