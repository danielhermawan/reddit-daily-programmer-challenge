"""
Easy Challenge
Reddit Case Link: https://www.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/
"""

from itertools import combinations
from typing import List, Tuple, Set


def three_sum(numbers: List[int]) -> Set[Tuple[int]]:
    dupli_map = {}
    result = []
    for n in numbers:
        if n not in dupli_map:
            dupli_map[n] = False
        elif not dupli_map[n]:
            dupli_map[n] = True
    print()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            find_number = -(numbers[i] + numbers[j])
            if find_number in dupli_map:
                out = tuple(sorted([numbers[i], numbers[j], find_number]))
                if find_number != numbers[i] and find_number != numbers[j]:
                    result.append(out)
                elif dupli_map[find_number]:
                    result.append(out)
    return set(sorted(result))


def three_combinator_sum(numbers: List[int]) -> Set[Tuple]:
    result = [tuple(sorted(n)) for n in combinations(numbers, 3) if sum(n) == 0]
    return set(sorted(result))


try:
    while True:
        print('Input numbers: ', end='')
        example = [int(n) for n in input().split()]
        # example = [9, -6, -5, 9, 8, 3, -4, 8, 1, 7, -4, 9, -9, 1, 9, -9, 9, 4, -6, -8]
        print(*three_sum(example))
        print()
except (EOFError, KeyboardInterrupt) as e:
    pass
