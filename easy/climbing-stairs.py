class Solution(object):
    def climbStairs(self, n):
        f1, f2 = 0, 1
        for i in range(n):
            result = f1 + f2
            f1 = f2
            f2 = result
        return result
