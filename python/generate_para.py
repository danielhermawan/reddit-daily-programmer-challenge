def generate(res, strs, open, close, max):
    if len(strs) == max * 2:
        res.append(strs)
        return
    if open < max:
        generate(list, strs + "(", open + 1, close, max)
    if close < open:
        generate(list, strs + ")", open, close + 1, max)


res = []
generate(res, "", 0, 0, 3)
print(res)
