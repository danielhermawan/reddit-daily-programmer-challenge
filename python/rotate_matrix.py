class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        max = len(matrix) - 1
        for lay in range(len(matrix) // 2):
            for i in range(max - (lay * 2)):
                temp = matrix[lay][lay + i]
                matrix[lay][lay + i] = matrix[max - lay - i][lay]
                matrix[max - lay - i][lay] = matrix[max - lay][max - lay - i]
                matrix[max - lay][max - lay - i] = matrix[lay + i][max - lay]
                matrix[lay + i][max - lay] = temp
        for row in matrix:
            for col in row:
                print(col, end=' ')
            print()


m = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
Solution().rotate(m)


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    r = str(abs(x))[::-1]
    if x < 0:
        r = int(r) * -1
    if -2147483648 < int(r) and int(r) < 2147483647:
        return int(r)
    else:
        return 0


print(reverse(-2147483648))
