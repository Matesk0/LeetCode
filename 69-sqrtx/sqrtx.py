class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = 1

        while result ** 2 <= x:
            result += 1
        
        return result - 1