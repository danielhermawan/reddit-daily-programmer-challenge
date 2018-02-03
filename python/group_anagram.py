class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        res = []
        for i in range(len(strs)):
            if map.get(i, False): continue
            temp = [strs[i]]
            map[i] = True
            for j in range(i + 1, len(strs)):
                if not map.get(j, False) and self.is_valid(strs[i], strs[j]):
                    map[j] = True
                    temp.append(strs[j])
            res.append(temp)
        return res

    def is_valid(self, str1, str2):
        if len(str1) != len(str2):
            return False
        map = {}
        for s in str1: map[s] = map.get(s, 0) + 1
        for s in str2:
            if map.get(s, 0) == 0:
                return False
            else:
                map[s] -= 1
        for v in map.values():
            if v != 0: return False
        return True


print(Solution().groupAnagrams(["", ""]))
