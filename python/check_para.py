class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = {'{': 0, '(': 1, '[': 2}
        back = {'}': 0, ')': 1, ']': 2}
        stack = []
        for i in range(len(s)):
            if s[i] in front.keys():
                stack.append(front[s[i]])
            elif len(stack) > 0 and back[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        else:
            return True


print(Solution().isValid('()'))
