from typing import List


def three_sum(numbers: List[int]):
    result = []
    numbers.sort()
    if len(numbers) < 3:
        return result
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            find_number = -(numbers[i] + numbers[j])
            valid = False
            if (find_number != numbers[i] and find_number != numbers[j]):
                valid = True
            else:
                dupli = 0
                if find_number == numbers[i]: dupli += 1
                if find_number == numbers[j]: dupli += 1
                if numbers.count(find_number) > dupli:
                    valid = True
            if valid:
                out = [numbers[i], numbers[j], find_number]
                if find_number in numbers and out not in result:
                    result.append(out)
    return result

def new_three_sum(numbers):
    result = []
    numbers.sort()
    if len(numbers) < 3:
        return result
    for i in range(0, len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i-1]: continue
        find = -(numbers[i])
        j = i + 1
        k = len(numbers) - 1
        while j < k:
            if find == (numbers[j] + numbers[k]):
                result.append([numbers[i], numbers[j], numbers[k]])
                k -= 1
                j += 1
                while j < k and numbers[k + 1] == numbers[k]: k -= 1
                while j < k and numbers[j-1] == numbers[j]: j += 1
            elif numbers[j] + numbers[k] > find: k -= 1
            else: j += 1
    return result

print(new_three_sum([-1, 0, 1, 2, -1, -4]))