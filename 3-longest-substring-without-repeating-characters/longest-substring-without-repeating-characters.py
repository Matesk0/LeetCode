class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            result = max(result, right - left + 1)
        
        return result