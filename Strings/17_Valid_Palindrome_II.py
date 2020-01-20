# ============================================================================
# Name        : 17_Valid_Palindrome_II.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:

        string = ""
        for i in s:
            if i.isalnum():
                string += i
        string = string.lower()
        for j in range(0,len(string)):
            temp = string[:j] + string [j+1:]
            if temp == temp[::-1]:
                return True
        return string == string[::-1]

if __name__ == "__main__":
    test = Solution()
    m = test.validPalindrome(s = "abca")
    print(m)
