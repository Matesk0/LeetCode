class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def climbing(curr):
            if curr > n:
                return 0
            
            if curr == n: 
                return 1
            
            if curr in memo:
                return memo[curr]
            
            memo[curr] = climbing(curr + 1) + climbing(curr + 2)
            print(memo)
            return memo[curr]

        return climbing(0)