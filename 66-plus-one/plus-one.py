class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
                continue
            
            digits[idx] += 1
            break
        
        if digits[0] == 0:
            digits.insert(0, 1)
        
        return digits