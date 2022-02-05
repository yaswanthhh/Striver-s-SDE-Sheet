class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = 0
        m = len(nums)//2
        for i in nums:
            d[i] += 1
            if d[i] > m:
                return i
        return -1
