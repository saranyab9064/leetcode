# ============================================================================
# Name        : 16_Valid_Palindrome.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Input : welcome to geeksforgeeks
Output : wlcm t gksfrgks

Input : what is your name ?
Output : wht s yr nm ?
"""
class Solution(object):
    def remVowels(self, s):
        string = ""
        list = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i not in list:
                string +=i
        return string



if __name__ == "__main__" :
        s =  "welcome to geeksforgeeks"
        test = Solution()
        a = test.remVowels(s)
        print(a)
