class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(nums, res, 0, [])
        return res

    def backtrack(self, nums, res, start, path):
        res.append(path[:])
        if start == len(nums):
            temp = path[:]
            temp.append(nums[start - 1])
            res.append(temp)
        for i in range(start + 1, len(nums) + 1):
            path.append(nums[i - 1])
            self.backtrack(nums, res, start + i, path)
            path.pop()


print(Solution().subsets([1, 2, 3]))
