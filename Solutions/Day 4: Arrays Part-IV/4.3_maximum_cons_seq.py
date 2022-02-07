class Solution:
    def longestConsecutive(self, nums):
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        longest = 1
        ctr = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] - 1:
                ctr += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                ctr = 1
            longest = max(longest, ctr)
        return longest
