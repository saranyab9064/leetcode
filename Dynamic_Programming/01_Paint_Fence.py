
# ============================================================================
# Name        : 01_Paint_Fence.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3
 -----      -----  -----  -----
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1
   5         c2     c1     c2
   6         c2     c2     c1
"""

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # if there is zero post
        if n == 0:
            return 0
        # if there is only one post, no of ways to paint that post will be k
        elif n == 1:
            return k
        # if n is 2 or more, there are k times 1 possiblities
        same = k
        # if posts are different ,there are k time k-1 possiblities
        different = k * (k-1)

        for i in range(3,n+1):

            prev_diff_value = different
            # case 2 scenario
            different = (same + different) * (k-1)
            # case 1 scenario
            same = prev_diff_value * 1

        return same + different





if __name__ == '__main__':
    n = 3
    k = 2
    test = Solution()
    ans = test.numWays(n,k)
    print(ans)
