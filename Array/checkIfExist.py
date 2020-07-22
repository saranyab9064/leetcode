class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        temp ={}
        for i in range(len(arr)):
            print(temp)
            if 2*arr[i] in temp or  (arr[i]%2==0 and arr[i]//2 in temp):
                return True
            else:
                temp[arr[i]]=1
            
                d={}
        return False
