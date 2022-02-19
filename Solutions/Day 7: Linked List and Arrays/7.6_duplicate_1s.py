class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max = 0
        ctr = 0
        for i in nums:
            if i == 1:
                ctr += 1
            if i == 0:
                ctr = 0
            if ctr > max:
                max = ctr
        return max
