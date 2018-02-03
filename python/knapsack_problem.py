def subproblem(weights, vals, max_weight, pos, sum_val, sum_w, map):
    res = sum_val
    for i in range(pos, len(vals)):
        sum_val += vals[i]
        sum_w += weights[pos]
        if sum_w > max_weight:
            return res
        map[i + 1] = subproblem(weights, vals, max_weight, i + 1, sum_val, sum_w, map)
        res = max(map[i + 1], res)
        sum_w -= weights[i]
        sum_val -= vals[i]
    return res


values = [60, 100, 120]
weights = [10, 20, 30]
w = 50
sum_w = 0
sum_v = 0
res = 0

for i in range(len(values)):
    sum_w += weights[i]
    if sum_w <= w:
        sum_v += values[i]
        for j in range(i + 1, len(values)):
            sum_w += weights[j]
            if sum_w <= w:
                sum_v += values[j]
            else:
                sum_w -= weights[j]
    res = max(sum_v, res)
    sum_w = 0
    sum_v = 0

print(subproblem(weights, values, w, 0, 0, 0, {}))
print(res)
