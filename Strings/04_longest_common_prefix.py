#============================================================================
# Name        : 04_longest_common_prefix.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # first find the smallest length
        if len(strs) == 0:
            return ""
        a = 100000
        for i in range(0,len(strs)):
            if a > len(strs[i]):
                a = len(strs[i])
            i += 1
        smallest_len =  a

        # search the common alphabet
        string = ""
        for i in range(0,smallest_len):
            current = strs[0][i]
            for j in range (1,len(strs)):
                if strs[j][i] != current:
                  return string
            string += current
        return string






if __name__ == "__main__":
    long = Solution()
    strs = []
    res = long.longestCommonPrefix(strs)
    print(res)