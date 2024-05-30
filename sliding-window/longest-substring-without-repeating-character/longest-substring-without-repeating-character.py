class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0 # left pointer
        longest = 0 # longest substring
        cset = set() # character set
        n = len(s) # length of string
        for right in range(n): # right pointer
            while s[right] in cset: # while right character in set
                cset.remove(s[left]) # remove the left character
                left += 1 # increment left pointer by one
            # if right character is not in set
            cset.add(s[right]) # add right character to set
            window_length = (right - left) + 1 # calculate window length
            longest = max(longest, window_length) #  set longest to highest value: longest, or window_length
        return longest
