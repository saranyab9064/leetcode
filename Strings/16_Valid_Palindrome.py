# ============================================================================
# Name        : 16_Valid_Palindrome.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
125. Valid Palindrome
Easy

853

2390

Add to List

Share
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        string = string.lower()
        return string == string[::-1]

if __name__ == "__main__":
    test = Solution()
    m = test.isPalindrome(s="A man, a plan, a canal: Panama")
    print(m)
