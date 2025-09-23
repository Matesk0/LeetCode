class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = 0

        for step in range(10, 0, -1):
            while result ** 2 <= x:
                result += step
            
            if result ** 2 == x:
                return result

            if result ** 2 > x:
                result -= step

        return result