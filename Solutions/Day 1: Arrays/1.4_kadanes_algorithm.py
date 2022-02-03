class Solution(object):
    def maxSubArray(self, nums):
        maxi = total = nums[0]
        
        for i in nums[1:]:
            total = max(i, total+i)
            maxi = max(total,maxi)
        
        return maxi
