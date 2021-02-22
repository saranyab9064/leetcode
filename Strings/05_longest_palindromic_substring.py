'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                res.append(s[i:j])

        out = {}

        for i in range(len(res)):   
            temp  = res[i]
            if res[i] == temp[::-1]:
                out[temp] = len(temp)

        return max(out, key=out.get)
