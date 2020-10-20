class Solution(object):
    def isUnique(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # includes ascii 
        if len(s)>128:
            return False
        else:
            h = {}
            for i in range(0,len(s)):
                if s[i] not in h:
                    h[s[i]] = 1
                else:
                    h[s[i]] += 1
                    return False
        return True
    def uniqueCharacters(self,str):
        
        # If length is greater than 256,
        # some characters must have 
        # been repeated
        MAX_CHAR = 256
        if (len(str) > MAX_CHAR):
            return False
    
        chars = [False] * MAX_CHAR
    
        for i in range(len(str)):
            index = ord(str[i])
            #print(index)
    
            '''
            * If the value is already True, 
            string has duplicate characters, 
            return False'''
            if (chars[index] == True):
                return False
            print(chars)
            chars[index] = True
    
        ''' No duplicates encountered, 
            return True '''
        return True
        

if __name__ == "__main__":
    
    input2 = "abcdef12"
    test = Solution()
    #out1 = test.isUnique(input2)
    out1 = test.uniqueCharacters(input2)
    print(out1)
