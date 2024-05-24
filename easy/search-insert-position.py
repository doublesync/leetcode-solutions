class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        nlength = len(nums) # 2
        if (target >= nums[-1]): return nlength
        if (target <= nums[0]): return 0
        for i, num in enumerate(nums):
            next_i = (i + 1) if (i + 1) <= (nlength) else None
            if next_i == None: break
            next_num = nums[next_i]
            if (target > num) and (target <= next_num):
                return next_i
                
