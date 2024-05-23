class Solution(object):
    def removeDuplicates(self, nums):
        # must sort 'in-place; hence 'nums[:]'
        nums[:] = sorted(set(nums)) # remove the duplicates; sort
        return len(nums) # return the length
