"""
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

 

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true
Example 2:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]
Example 3:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
Example 4:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
Example 5:

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false
 

Constraints:

1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""
import operator
from functools import reduce
class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        # Declare a hash map
        h = {}
        list1 = []
        flag = True
        if len(pieces)==0:
            return False
        else:
            for i in pieces:
                h[i[0]] = i
        for i in arr:
            if i in h:
                list1.append(h[i])
        print(list1)
        #list2 = reduce(operator.concat,list1)
        #converting list of lists to single list
        #https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        if len(list1)>1 or len(list1)==1:
            list2 = reduce(lambda x,y:x+y,list1)
            print(list2)
            print(len(arr),len(list2))
            if len(arr)==len(list2):
                for i in range(len(arr)):
                    if arr[i] !=list2[i]:
                        flag =  False
                    else: continue
            else: flag= False
        else: flag= False
        if flag == True: 
            return True
        else: return False


if __name__ == '__main__':
    test =  Solution()
    a1 = [17,89,1,72,69,70,18,39,92,51,47,99,71,5,16,57,67,26,62,24,23,15,61,37,81,30,82,96,3,94,7,41,43,2,66,8]
    p1=[[4,93],[3],[19],[87,62],[49],[54],[13,21],[82],[5],[73],[34],[28],[29],[27],[42],[45,67],[85,16],[58,31,37],[64],[81],[72,60],[59],[17],[6],[97],[1,92],[84]]
    a =  [1,3,5,7]
    p = [[2,4,6,8]]
    a = [85]
    b  = [[85]]
    out = test.canFormArray(a,b)
    print(out)
