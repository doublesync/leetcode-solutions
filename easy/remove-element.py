class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            for i, n in enumerate(nums):
                if n == val:
                    nums.pop(i)
                    break
        return len(nums)
