class Solution(object):
    def minSubArrayLen(self, target, nums):
        length = len(nums) # the length of the nums array
        shortest = float('inf') # initializing shortest to infinity (for easy 'min' use)
        left, total = 0, 0 # initializing left pointer and total to zero

        for right in range(length): # iterate through each number in the array (number == right pointer)
            total += nums[right] # increment total by number right pointer is at
            while total >= target: # while total is greater/equal-to target value
                w_length = (right - left) + 1 # the length of the window/subarray
                shortest = min(w_length, shortest) # set shortest to shortest length
                total -= nums[left] # decrement total
                left += 1 # increment left pointer

        return 0 if shortest == float('inf') else shortest # return shortest based on value
