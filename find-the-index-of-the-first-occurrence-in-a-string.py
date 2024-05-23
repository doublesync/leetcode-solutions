class Solution(object):
    def strStr(self, haystack, needle):
        nlength = len(needle)
        hlength = len(haystack)
        start_char = needle[0]
        for i, char in enumerate(haystack):
            if char == start_char:
                end_index = (i + nlength)
                if not end_index > hlength:
                    if haystack[i:end_index] == needle:
                        return i
        return -1
