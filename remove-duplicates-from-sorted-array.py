class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums)) # remove the duplicates; sort
        return len(nums) # return the length
