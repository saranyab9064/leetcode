class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        for i in range(1,arr[-1]):
            if i not in arr:
                res.append(i)
        print(res)
        if len(res)>=k:
            return res[k-1]
        elif len(res)==0 and k >0:
            for i in range(len(arr)+1,len(arr)+k+1):
                res.append(i)
            return res[k-1]
"""
class Solution:
    def findKthPositive(self, arr, k):
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            print(i,k + len(arr) + 1)
            if i not in arr_set: k -= 1
            print(k)
            if k == 0: return i
"""
            

if __name__== '__main__':
    test = Solution()
    a = [1,13,18]
    k = 17
    out=test.findKthPositive(a,k)
    print(out)
