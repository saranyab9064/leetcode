
# ============================================================================
# Name        : 24_First_Unique_Character_in_a_String.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        for i in range(0,len(s)):
            if s[i] in h:
                h[s[i]] += 1
            else:
                h[s[i]] = 1
        index =""
        flag = False
        for key in h:
            if h[key] == 1:
                flag = True
                index =  key
                break
        for i in range(0,len(s)) :
            if s[i] == index:
                return i

        if not flag:
             return -1




if __name__ == "__main__":
    test = Solution()
    s = "leetcode"
    res = test.firstUniqChar(s)
    print(res)
