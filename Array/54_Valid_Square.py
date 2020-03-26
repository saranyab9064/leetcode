
# ============================================================================
# Name        : 54_Valid_Square.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dist = []
        # p1, p2
        d1 = ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)
        # p1, p3
        d2 = ((p3[1] - p1[1]) ** 2 + (p3[0] - p1[0]) ** 2)
        # p1, p4
        d3 = ((p4[1] - p1[1]) ** 2 + (p4[0] - p1[0]) ** 2)
        # p2, p3
        d4 = ((p3[1] - p2[1]) ** 2 + (p3[0] - p2[0]) ** 2)
        # p2, p4
        d5 = ((p4[1] - p2[1]) ** 2 + (p4[0] - p2[0]) ** 2)
        # p3, p4
        d6 = ((p4[1] - p3[1]) ** 2 + (p4[0] - p3[0]) ** 2)
        dist.append(d1)
        dist.append(d2)
        dist.append(d3)
        dist.append(d4)
        dist.append(d5)
        dist.append(d6)
        dist.sort()
        return 0 < dist[0] == dist[1] == dist[2] == dist[3] and 2 * dist[0] == dist[4] == dist[5]
if __name__ == '__main__':
    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]
    test = Solution()
    ans = test.validSquare(p1,p2,p3,p4)
    print(ans)
