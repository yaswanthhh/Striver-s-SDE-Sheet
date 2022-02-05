class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        elif len(nums) == 2:
            if nums[0] != nums[1]:
                return nums
        
        res = []
        nums.sort()
        ctr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                ctr += 1
            else:
                ctr = 1
            if ctr > len(nums)/3 and nums[i] not in res:
                res.append(nums[i])
        return res
