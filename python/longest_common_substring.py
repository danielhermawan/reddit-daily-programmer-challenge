def common_substring(s, t):
    map = {}
    z = 0
    res = ""
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            if i == 0 or j == 0:
                map[i, j] = 0
            elif s[i - 1] == t[j - 1]:
                map[i, j] = 1 + map[i - 1, j - 1]
                z = max(z, map[i, j])
                res = s[i - z:i]
            else:
                map[i, j] = 0
    return res


print(common_substring('baba', 'abab'))
