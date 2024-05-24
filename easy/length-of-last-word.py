class Solution(object):
    def lengthOfLastWord(self, s):
        array = s.rsplit(' ')
        array.reverse()
        for i, s in enumerate(array):
            if not s: continue
            return len(s)
