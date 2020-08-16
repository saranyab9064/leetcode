



    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        comp = x
        rev = 0
        while x > 0:
            a = x % 10
            rev = rev * 10 + a
            x = x // 10
            print(rev,x)
        print(x,rev)
        if comp == rev:
            return True
        else:
            return False


if __name__ == "__main__":
    
    input2 = 121
    test = Solution()
    out1 = test.isPalindrome(input2)
    print(out1)
