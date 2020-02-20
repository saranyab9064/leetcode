


# ============================================================================
# Name        : 41_Count_Primes.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution(object):
    def checkprime(self,num,prime_no):
        if num < 2:
            return False
        for j in prime_no:
            if num % j == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_list= []
        count = 0
        for i in range(1,n):
             if self.checkprime(i,count_list):
              count_list.append(i)
        return (count_list)



if __name__ == "__main__":
    valid = Solution()
    s = 95555
    res = valid.countPrimes(s)
    print(res)
