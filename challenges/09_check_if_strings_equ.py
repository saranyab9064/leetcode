"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        '''
        str1 = "".join(word1)
        str2 = "".join(word2)
        if str1 == str2:
            return True
        else: return False
        '''
        # another solution using two pointers
        # define and initialise two pointers
        # since we have two strings , we need to initialise the pointers separately
        # ptr for word 1
        i1,j1=0,0
        # ptr for word 2s
        i2,j2=0,0
        while i1<len(word1) and i2<len(word2):
            if word1[i1][j1] != word2[i2][j2]:
                return False
            j1 = j1+1
            j2 = j2+1
            if j1==len(word1[i1]):
                i1 = i1+1
                j1 = 0
            if j2 == len(word2[i2]):
                i2 = i2+1
                j2 = 0
        if i1 ==len(word1) and i2 == len(word2):
            return True
        else: return False



        
if __name__ =="__main__":
    test = Solution()
    a = ["abc", "g", "defg"]
    b = ["abcgdefg"]
    out = test.arrayStringsAreEqual(a,b)
    print(out)
