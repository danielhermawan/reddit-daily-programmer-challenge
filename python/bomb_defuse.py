"""
Easy Challenge
Reddit Case Link: https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/
"""

rules = {
    'w': ['r', 'o', 'g', 'p'],
    'r': ['g'],
    'b': ['r', 'b', 'o'],
    'o': ['r', 'b'],
    'g': ['w', 'o'],
    'p': ['r', 'b']
}
colors = input('Please input order of color(w, r, b, o, g, p): ').split()
next = rules.keys()
valid = True
for i in range(len(colors)):
    if colors[i] not in next:
        valid = False
        break
    next = rules[colors[i]]
if valid:
    print("Bomb defused")
else:
    print("Boom")