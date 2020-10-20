"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"

"""
class Solution(object):
    def URLify(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        res = ""
        s = str(s[0])
 
        for i in s:
                if i == ' ':
                   res = res + "%20"
                else:
                    res = res +i
        return res
        """
        res = ""
        s = s[0].strip()
        for i in s:
            if i == ' ':
                res = res +'%20'
            else:
                res = res +i
        return res



if __name__ == "__main__":
    
    in1 = "Mr John Smith   ", 13
    print(len(in1[0]))
    test = Solution()
    #out1 = test.isUnique(input2)
    out1 = test.URLify(in1)
    print(out1)
