class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<2:
            return len(nums)
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                prev += 1
                nums[prev] = nums[i]
        return prev + 1
