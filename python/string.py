def is_unique_string(str):
    dict = {}
    for s in str:
        if s not in dict.keys():
            dict[s] = True
        else:
            return False
    return True

print(is_unique_string("say"))

def sort_string(s):
    return ''.join(sorted(s))

def check_permutation(x, y):
    if len(x) != len(y):
        return False
    return sort_string(x).upper() == sort_string(y).upper()

print(check_permutation('as', 'sA'))

def change_space(str):
    result = ""
    for s in str:
        if s == ' ':
            result += '%20'
        else:
            result += s
    return result

print(change_space("s s"))

def check_palindrom(str):
    j = len(str) - 1
    for s in str:
        if s != str[j]:
            return False
        j -= 1
    return True

print(check_palindrom("anna"))

def check_replacement(str1, str2):
    if len(str1) != len(str2):
        return False
    j = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            j += 1
        if j > 1:
            return False
    return True

def check_insert_removed(str1, str2):
    if len(str1) == len(str2):
        return False
    if len(str1) < len(str2):
        long = str2
        short = str1
    else:
        long = str1
        short = str2
    idx_long = 0
    idx_short = 0
    j = 0
    while idx_long < len(long) and idx_short < len(short):
        if short[idx_short] != long[idx_long]:
            j += 1
        else:
            idx_short += 1
        idx_long += 1
        if j > 1:
            return False
    return True

def check_oneway(str1, str2):
    if check_replacement(str1, str2):
        return True
    elif check_insert_removed(str1, str2):
        return True
    return False

print(check_oneway("pale", "bales"))

def compress_string(string):
   i = 0
   result = ""
   is_comppresed = False
   while i < len(string):
       result += string[i]
       k = 1
       while len(string) - 1 > i and string[i + 1] == string[i]:
           k += 1
           i += 1
           is_comppresed = True
       result += str(k)
       i += 1
   if not is_comppresed:
       return string
   return result

print(compress_string("aabcd"))

def matrix_zero(data):
    dict_zero = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                dict_zero[i] = j
    """"
    for y, x in dict_zero.items():
        for i in data[y]:
            data[y][i] = 0
    """""
    cache = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) in cache.keys():
                break
            if i in dict_zero.keys():
                data[i][j] = 0
                cache[(i, j)] = True
            if j in dict_zero.values():
                data[i][j]= 0
                cache[(i, j)] = True

data = [
    [1,0,2],
    [1,2,3],
    [1,3,2,5],
    [4,2,1,4,0]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=" ")
    print()

def is_palindrome_permutation(string):
    char_count = {}
    valid = True
    for s in string:
        if s in char_count.keys():
            char_count[s] =+ 1
        else:
            char_count[s] = 1
        if char_count[s] % 2 == 1:
            valid = False
        else:
            valid = True
    return valid

print(is_palindrome_permutation("TactCoa"))

def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    length = n - 1
    for layer in range(n // 2):
        last = length - layer
        for i in range(layer, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[last - i][layer]
            matrix[last - i][layer] = matrix[last][last - i]
            matrix[last][last - i] = matrix[layer + i][last]
            matrix[layer + i][last] = top

data = [
    [1,4,5,34],
    [10,2,7,42],
    [11,3,4,31],
    [10,5,12,43]
]

rotate(data)

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=" ")
    print()
