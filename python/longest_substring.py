def lengthOfLongestSubstring(s):
    has = ""
    result = 0
    temp = 0
    i = 0
    j = 1
    while i < len(s):
        if s[i] in has:
            has = s[j:i]
            temp = len(has)
            j += 1
        else:
            temp += 1
            has += s[i]
            if temp > result:
                result = temp
            i += 1
    return result

print(lengthOfLongestSubstring("abcabcbb"))