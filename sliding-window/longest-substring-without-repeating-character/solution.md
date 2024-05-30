## Logic Takeaways

- **A set won’t allow duplicates,** which is why it’s good for these types of problems. **It also operates in linear, or O(n) time.**
- We’ll use **two pointers (right and left)** to traverse through the array given.
- Think of the **‘window’** as anything between the **left and right pointers; resembling the window of a sliding door.**
- Always ask **‘is our window valid?’**

### **Longest Substring Without Repeating Characters**

**Initialization**

- **Left pointer;** initializes to zero.
- **Longest;** initializes to zero *(this will hold the length of the longest subarray in the given string)*
- **Set;** initializes to empty set *(to prevent any duplicates in O(n) time complexity)*
- **Right pointer;** initializes to the index of a for loop in the **range of the string given.**

```python
left = 0
longest = 0
cset = set()
n = len(s)

for right in range(n):
	...
```

**Solution**

*Is our window valid, are there duplicates in the set?*

1. For every iteration, we’ll run a while loop **until s[right] is not in the set.** 
2. If **s[right]** is in the set, we will remove the left pointer’s character off of the set, then increment the **left pointer** by one. 
    
    *This won’t necessarily remove the first element of the set, but instead wherever the left pointer’s character is at in the set.*
    
    ```python
    cset.remove(s[left])
    ```
    
3. If **s[right]** is not in the set, we’ll calculate the **window length,** which is 
    
    $$
    (right - left)  + 1
    $$
    
    then, we’ll set longest to the highest value between: the **longest variable (longest)**, and the **window length (wl)** variable.
    
    ```python
    longest = max(longest, wl)
    ```
    
4. We’ll then add **s[right]** to the set since it’s not already in there, or has been removed (either way it’s not in the set).
5. Lastly, outside of the for original loop, we’ll return the **longest** **variable (longest)**.
