def quicksort(arr, start, end):
    if start > end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)


def partition(arr, start, end):
    pivot = arr[end]


arr = [3, 2, 1, 4, 1, 2, 5]
quicksort(arr, 0, len(arr) - 1)
