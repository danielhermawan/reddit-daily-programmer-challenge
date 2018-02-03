def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quicksort_helper(arr, low, part - 1)
        quicksort_helper(arr, part + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]
    return i + 1


arr = [30, 20, 40, 10, 50]
quicksort(arr)
print(arr)
