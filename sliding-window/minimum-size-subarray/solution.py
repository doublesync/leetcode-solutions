class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) 
        shortest = float('inf')
        left, total = 0, 0

        for right in range(length):
            total += nums[right]
            while total >= target:
                w_length = (right - left) + 1
                shortest = min(w_length, shortest)
                total -= nums[left]
                left += 1

        return 0 if shortest == float('inf') else shortest
