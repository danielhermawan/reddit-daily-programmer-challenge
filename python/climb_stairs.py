class Solution(object):
    i = 0

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        map = {}
        a = self.climb(n, 0, map)
        print('Run time: ', self.i)
        return a

    def climb(self, target, num, map):
        self.i += 1
        res = 0
        if num in map.keys():
            return map[num]
        if target < num:
            return 0
        if target == num:
            return 1
        for i in range(1, 4):
            res += self.climb(target, num + i, map)
        map[num] = res
        return res


print(Solution().climbStairs(10))
