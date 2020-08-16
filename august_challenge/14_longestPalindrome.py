

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for i in s:
            count[i] = count.get(i,0)+1
        print(count)
        res ,odd_found = 0, False
        for key,i in count.items():
            print(i)
            if i % 2 == 0:
                res += i
                print("even",res)
            else:
                odd_found = True
                res += i - 1
                print("odd",res)

        if odd_found: res += 1
        return res




if __name__ == "__main__":
    Input1 = "aaabccccdd"
    test = Solution()
    out = test.longestPalindrome(Input1)
    print(out)
