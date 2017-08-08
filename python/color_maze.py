"""
Easy Challenge
Reddit Case Link: https://www.reddit.com/r/dailyprogrammer/comments/6qutez/20170801_challenge_325_easy_color_maze/
"""

from typing import List, Tuple


def find_maze(sequence: List[str], maze: List[List[str]]) -> List[Tuple]:
    row = len(maze) - 1
    col = len(maze[0]) - 1
    seq_index = 0
    path = []
    for j in range(len(maze[row])):
        if maze[row][j] == sequence[seq_index]:
            path_temp = j, row, sequence[seq_index]
            path.append(path_temp)
            while True:
                seq_index = (seq_index + 1) % len(sequence)
                left_path = path_temp[0] - 1, path_temp[1]
                right_path = path_temp[0] + 1, path_temp[1]
                top_path = path_temp[0], path_temp[1] - 1
                # Check left path
                if path_temp[0] != 0:
                    if maze[path_temp[1]][path_temp[0] - 1] == sequence[seq_index] and left_path not in path:
                        path_temp = left_path + (sequence[seq_index],)
                # Check right path
                if path_temp[0] != col:
                    if maze[path_temp[1]][path_temp[0] + 1] == sequence[seq_index] and right_path not in path:
                        path_temp = right_path + (sequence[seq_index],)
                # Check top path
                if path_temp[1] != 0:
                    if maze[path_temp[1] - 1][path_temp[0]] == sequence[seq_index] and top_path not in path:
                        path_temp = top_path + (sequence[seq_index],)
                else:
                    break
                if path_temp[0] == path[-1][0] and path_temp[1] == path[-1][1]:
                    break
                else:
                    path.append(path_temp)
    return path

def new_find_maze(sequence: List[str], maze: List[List[str]]) -> List[Tuple]:
    row = len(maze) - 1
    seq_index = 0
    path = []
    possible_path = []

    for i in range(len(maze[0])):
        possible_path.append((i, row, seq_index))
    while row != 0 and len(possible_path) != 0:
        col, row, seq_index = possible_path.pop()
        if maze[row][col] == sequence[seq_index]:
            path.append((col, row, seq_index))
            seq_index = (seq_index + 1) % len(sequence)
            # Left path
            if col != 0 and row != len(maze[0]) - 1:
                possible_path.append((col - 1, row, seq_index))
            # Right Path
            if col != len(maze[0]) - 1 and row != len(maze[0]) - 1:
                possible_path.append((col + 1, row, seq_index))
            # Top path
            if row != 0:
                possible_path.append((col, row - 1, seq_index))
    return path

seq = ['R', 'O', 'Y', 'P', 'O']
str_maze = """R R B R R R B P Y G P B B B G P B P P R
B G Y P R P Y Y O R Y P P Y Y R R R P P
B P G R O P Y G R Y Y G P O R Y P B O O
R B B O R P Y O O Y R P B R G R B G P G
R P Y G G G P Y P Y O G B O R Y P B Y O
O R B G B Y B P G R P Y R O G Y G Y R P
B G O O O G B B R O Y Y Y Y P B Y Y G G
P P G B O P Y G B R O G B G R O Y R B R
Y Y P P R B Y B P O O G P Y R P P Y R Y
P O O B B B G O Y G O P B G Y R R Y R B
P P Y R B O O R O R Y B G B G O O P B Y
B B R G Y G P Y G P R R P Y G O O Y R R
O G R Y B P Y O P B R Y B G P G O O B P
R Y G P G G O R Y O O G R G P P Y P B G
P Y P R O O R O Y R P O R Y P Y B B Y R
O Y P G R P R G P O B B R B O B Y Y B P
B Y Y P O Y O Y O R B R G G Y G R G Y G
Y B Y Y G B R R O B O P P O B O R R R P
P O O O P Y G G Y P O G P O B G P R P B
R B B R R R R B B B Y O B G P G G O O Y"""
maze = [s.split() for s in str_maze.split('\n')]
path = new_find_maze(seq, maze)
tuple_path = {}
for i in path:
    tuple_path[(i[0], i[1])] = seq[i[2]]
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if (j, i) in tuple_path.keys():
            print(tuple_path[(j, i)], end=' ')
        else:
            print('/', end=' ')
    print('\n')
