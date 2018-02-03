def selection_sort(arr):
    res = []
    for i in range(len(arr)):
        smaller = None
        pos = -1
        for j in range(len(arr)):
            if smaller is None or arr[j] < smaller:
                smaller = arr[j]
                pos = j
        res.append(arr.pop(pos))
    return res


print(selection_sort([4, 3, 2, 5, 1, 10, 1, 3]))
