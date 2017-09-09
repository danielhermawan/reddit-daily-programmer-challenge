def quicksort(list):
    quicksorthelper(list, 0, len(list) - 1)

def quicksorthelper(list, first, last):
    if first < last:
        split = partition(list, first, last)
        quicksorthelper(list, first, split - 1)
        quicksorthelper(list, split + 1, last)

def partition(list, first, last):
    pivot = list[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list[left] > pivot:
            left += 1
        while list[right] < pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            temp = list[right]
            list[right] = list[left]
            list[left] = temp
    temp = list[first]
    list[first] = list[right]
    list[right] = temp
    return right

def recursive(i):
    if i <= 1:
        return 1
    return recursive(i - 1) + recursive(i - 1)

def merge_sort_helper(numbers, left, right, middle):
    # 3,4 1,3,5 l-> 2, r ->\
    l = numbers[left:middle]
    r = numbers[middle:right+1]
    k = []
    while len(l) > 0 and len(r) > 0:
        if l[0] < r[0]:
            k.append(l.pop(0))
        else:
            k.append(r.pop(0))
    while len(l) != 0:
        k.append(l.pop(0))
    while len(r) != 0:
        k.append(r.pop(0))
    idx = 0
    for i in range(left, right):
        numbers[i] = k[idx]
        idx += 1


def merge_sort(numbers, left, right):
    if left != right:
        m = (left + right) // 2
        merge_sort(numbers, left, m)
        merge_sort(numbers, m + 1, right)
        merge_sort_helper(numbers, left, right, m)


def new_merge_sort(data):
    if len(data) > 1:
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]
        new_merge_sort(left)
        new_merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

alist = [ 21, 4, 5]
new_merge_sort(alist)
print(alist)

def permutation(str: str, prefix: str = ""):
    if len(str) == 0:
        print(prefix)
    else:
        for i in range(len(str)):
            rem = str[0:i] + str[i + 1:]
            permutation(rem, prefix + str[i])

permutation("saya")

def fib(n):
    if n <= 0: return 0
    elif n == 1: return 1
    return fib(n - 1) + fib(n - 2)

def fib_loop(n):
    result = 0
    a, b = 0, 1
    while a < n:
        a, b = b, b + a
    return a

print("fib %d" % fib_loop(10))

def binary_search(datas, search, left, right):
    if right < left:
        return -1
    else:
        middle = (left + right) // 2
        if datas[middle] == search:
            return middle
        elif datas[middle] > search:
            return binary_search(datas, search, left, middle - 1)
        elif datas[middle] < search:
            return binary_search(datas, search, middle + 1, right)

def binary_search_loop(datas, search):
    l = 0
    r = len(datas) - 1
    while l < r:
        middle = (l + r) // 2
        if datas[middle] == search:
            return middle
        elif datas[middle] > search:
            r = middle - 1
        elif datas[middle] < search:
            l = middle + 1
    return -1

binary = [2,4,6,7,8,9]
print(binary_search_loop(binary, 6))

