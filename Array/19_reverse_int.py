
# ============================================================================
# Name        : 19_reverse_int.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        max = 2 ** 31 - 1
        min = -2 ** 31
        if x not in range(min,max):
            return 0
        if x > 0:
            while (x > 0):
                dig = x % 10
                rev = rev * 10 + dig
                x = x // 10
            return rev
        else:
            if x < 0:
                x = x * -1
            while (x > 0):
                dig = x % 10
                rev = rev * 10 + dig
                x = x // 10
            return rev * -1
if __name__ == '__main__':
    integer = Solution()
    n = 431567890909999
    res = integer.reverse(n)
    print(res)
