def lcs(str1, str2, m, n, map):
    if (m, n) in map.keys():
        return map[m, n]
    if m == 0 or n == 0:
        return 0
    elif str1[m - 1] == str2[n - 1]:
        key = str1[:m - 1], str2[:n - 1]
        map[key] = 1 + lcs(str1, str2, m - 1, n - 1, map)
        return map[key]
    else:
        v1 = lcs(str1, str2, m, n - 1, map)
        v2 = lcs(str1, str2, m - 1, n, map)
        map[str1[:m], str2[:n - 1]] = v1
        map[str1[:m - 1], str2[:n]] = v2
        return max(v1, v2)


str1 = "SHINCHAN"
str2 = "NOHARAAA"
print(lcs(str1, str2, len(str1), len(str2), {}))
