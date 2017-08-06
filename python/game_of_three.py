"""
Easy Challenge
Reddit Case Link: https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/
"""

try:
    number = int(input('Please Input the number: '))
    while number != 1:
        modulo_result = (0, -1, 1)[int(number % 3)]
        print("%d %d" % (number, modulo_result))
        number = (number + modulo_result) / 3
    print(int(number))
except (EOFError, KeyboardInterrupt) as e:
    pass