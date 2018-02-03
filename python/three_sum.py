def three_sum(numbers):
    numbers = sorted(numbers)
    if len(numbers) < 3:
        return []
    result = []
    for i in range(len(numbers) - 2):
        if i != 0 and numbers[i - 1] == numbers[i]:
            continue
        x = i + 1
        y = len(numbers) - 1
        while x < y:
            res = numbers[x] + numbers[y] + numbers[i]
            if res == 0:
                result.append([numbers[i], numbers[x], numbers[y]])
                x += 1
                y -= 1
                while x < y and numbers[x] == numbers[x - 1]: x += 1
                while x < y and numbers[y] == numbers[y + 1]: y -= 1
            elif res < 0:
                x += 1
            else:
                y -= 1
    return result


arr = [4, 6, 10, 3, 11, 7, 21, 2, 0]
print(three_sum(arr))
