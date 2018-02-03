def convert(s, numRows):
    dict = {}
    zig_count = numRows // 2
    for i in range(len(s)):
        index = i % (numRows + zig_count)
        if index >= numRows:
            index = (numRows - index + 1) * 2 - 1
        if index not in dict.keys():
            dict[index] = ""
        dict[index] += s[i]
    res = ""
    for d in dict.values():
        res += d
    return res


print(convert("PAYPALISHIRING", 3))
