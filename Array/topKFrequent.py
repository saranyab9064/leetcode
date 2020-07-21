class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        a = [0] * (len(h))
        j = 0
        for i in h:
            a[j] = [i, h[i]]
            j += 1
        a = sorted(a, key=lambda x: x[0],
                   reverse=True)
        a = sorted(a, key=lambda x: x[1],
                   reverse=True)
        list1 = []
        for i in range(k):
            list1.append(a[i][0])
        return sorted(list1)
