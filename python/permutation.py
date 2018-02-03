def dfs(res, pref, efix):
    full = pref + efix
    if len(full) - 1 == len(pref):
        res.append(full)
        return
    for i in range(len(full) - len(pref)):
        temp = efix[:]
        dfs(res, pref + [temp.pop(i)], temp)


def permutation(arr):
    res = []
    dfs(res, [], arr)
    return res


def dfs_2(res, left, right, arr):
    if left == right:
        res.append(arr)
        return
    for i in range(left, right + 1):
        arr[left], arr[i] = arr[i], arr[left]
        dfs_2(res, left + 1, right, arr)
        arr[left], arr[i] = arr[i], arr[left]


def permutation_2(arr):
    res = []
    dfs_2(res, 0, len(arr) - 1, arr)
    return res


print(permutation_2([1, 2, 3]))
