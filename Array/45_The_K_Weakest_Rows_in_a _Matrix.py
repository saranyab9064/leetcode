

# ============================================================================
# Name        : 45_The_K_Weakest_Rows_in_a _Matrix.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================

"""
Given a m * n matrix mat of ones (representing soldiers) and
zeros (representing civilians), return the indexes of the k weakest
rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers
in row i is less than the number of soldiers in row j,
or they have the same number of soldiers but i is less than j.
Soldiers are always stand in the frontier of a row, that is,
always ones may appear first and then zeros.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]
 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        
        res = []
        for i in mat:
            res.append(sum(i))
        if len(res)==0:
            return [0]
        ans = []
        print(res)
        for j in sorted(res):
            x = res.index(j)
            ans.append(x)
            res[x] = -1
            print(j,x,res)
        return ans[:k]
        """
        # run for loop and sum up all the values from row 1 to row n
        # store in a as a[ sum up value, row n] format
        a = [(sum(value), i) for i, value in enumerate(mat)]
        # sort a and store it in b eg b[1,0] 1 denoted sum up value and o denotes zeroth row
        b = sorted(a)
        # create a empty list
        out = []
        # based on k value run for loop 
        # for each element in sorted list b
        # append b[1] in newly created list and return it
        for b in b[:k]:
            out.append(b[1])
        return out





if __name__ == "__main__":
    test = Solution()
    mat = [[1, 0, 0, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 0]]
    k = 3
    res = test.kWeakestRows(mat,k)
    print(res)
