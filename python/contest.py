def matrixLand(arr):
    res = 0
    saved = {}
    for i in range(len(arr[0])):
        res = max(sub(arr, res, 0, i, saved), res)
    return res


def sub(arr, score, x, y, saved):
