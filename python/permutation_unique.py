class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], nums)
        return res

    def dfs(self, res, pref, efix):
        full = pref + efix
        if len(full) - 1 == len(pref):
            res.append(full)
        for i in range(len(full) - len(pref)):
            temp = efix[:]
            temp_pref = pref + [temp.pop(i)]
            if temp_pref + temp in res:
                continue
            self.dfs(res, temp_pref, temp)


print(Solution().permuteUnique([1, 1, 2]))
