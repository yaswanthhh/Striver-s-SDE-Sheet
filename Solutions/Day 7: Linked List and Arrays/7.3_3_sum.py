#This code has wrong output

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i == 0 or (i > 0 and nums[i] !=nums[i-1]):
                lo, hi, s = i+1, len(nums)-1, 0-nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == 0:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]: 
                            lo += 1                    
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < s:
                        lo += 1
                    else:
                        hi -= 1
        return res
