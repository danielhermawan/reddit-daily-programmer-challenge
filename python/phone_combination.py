class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        arr = []
        dict = {'0': ' ', '1': "*", '2': "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                '9': 'wxyz'}
        for s in digits:
            arr.append(dict[s])
        # self.helper(res, arr, "", 0)
        path = ""
        pos = 0

        return res

    def helper(self, res, arr, path, pos):
        if len(arr) == 0:
            return
        if len(path) == len(arr):
            res.append(path)
            return
        for i in arr[pos]:
            self.helper(res, arr, path + i, pos + 1)


print(Solution().letterCombinations(""))
