## Logic Takeaways

My first solution worked, but worked in **O(n^2)** time complexity; so, it’s not a solution. 

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        shortest = None;
        length = len(nums)
        stop = (length - 1)

        if not nums: return 0

        for left in range(length):
            right = (left)
            while right <= stop:
                right += 1
                sub_array = nums[left:right]
                num_sum = sum(sub_array)
                if num_sum >= target:
                    shortest = min(len(sub_array), shortest) if shortest else len(sub_array)
            
        if not shortest:
            return 0
        else:
            return shortest
```

Here are my takeaways on finding a solution that works in **O(n)** time complexity.

- Instead of going through the sum of every possible sub-array, **don’t include the sub-arrays that don’t have the possibility of having a sum greater than or equal to the target value.**
- The idea is to not iterate over every sub-array.
    
    ```python
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    
    # 2 + 3 + 1 + 2 = 8
    # when we move our left pointer to 3: OBVIOUSLY (3 + 1 + 2) can't be >= 8
    ```
    
- We should keep a variable initialized to track the **total sum value; e**ach time we move the left pointer, we should **decrement the total value by the value removed.**
- There are several ways we can initialize **shortest.**
    
    ```python
    shortest = float('inf') # infinity (when we use min, this will work best)
    shortest = -1
    shortest = len(nums) + 1 # this will work the same as float('inf')
    ```
    

**Solution**

1. We should use the **sliding window technique** for this problem; it’s actually a rather simple application as well.
2. Let’s start with at least initializing: **our left pointer, our shortest variable, and our total variable.**
3. Let’s iterate through the range of the length of the **nums array** (and initialize our right pointer as the iterator).
4. For every iteration, let’s increment the **total variable** by the **number at the right pointer.**
    
    ```python
    total += nums[right]
    ```
    
5. Let’s create a **while loop** until our **total** is greater/equal-to our **target**. 
    
    For every loop, let’s set our **shortest variable** to the minimum value between: **the shortest variable, and the window length.**
    
    ```python
    w_length = (right - left) + 1
    # example: [2, 3, 1, 4]
    # left: index(1) 
    # right: index(3)
    # (3 - 1) = 2 (distance between pointers)
    # (2 + 1) = 3 (window/subarray length)
    ```
    
    Let’s also decrement the **total** by the **number at the left pointer, and increment the left pointer by one.**
    
6. Let’s return **zero if shortest is still at it’s initial state,** otherwise, let’s return the **shortest variable.**

**Voila!** All done.
