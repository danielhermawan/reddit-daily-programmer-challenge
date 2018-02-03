def solution(nums):
    rotate = 0
    map = {}
    for i in nums:
        if i not in map.keys():
            map[i] = 1
        else:
            map[i] += 1
    max = 0
    target = 0
    for keys, value in map.items():
        if value > max:
            target = keys
            max = value
    for i in nums:
        if i != target:
            if i + target == 7:
                rotate += 2
            else:
                rotate += 1
    return rotate


def solution_two(nums):
    rotate = None
    look_up = set(sorted(nums))
    for target in look_up:
        r = 0
        for n in nums:
            if n != target:
                if n + target == 7:
                    r += 2
                else:
                    r += 1
        if rotate == None or r < rotate:
            rotate = r
    return rotate


# print(solution([3,6,6]))
print(solution_two([1, 2, 3, 4, 5]))
# print(solution([2]))
