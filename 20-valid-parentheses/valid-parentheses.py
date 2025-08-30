class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        check = {')' : '(',
                ']' : '[',
                '}' : '{'}

        for symbol in s:
            if symbol in check.values():
                stack.append(symbol)
            
            else:
                if not stack or stack[-1] != check[symbol]:
                    return False

                stack.pop()
        
        return len(stack) == 0
        