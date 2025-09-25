class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}

        for letter in s:
            if letter in letters:
                letters[letter] += 1

            else:
                letters[letter] = 1
        
        for letter in t:
            if letter in letters:
                letters[letter] -= 1
            
            else:
                return False
        
        return all(letters[letter] == 0 for letter in letters)
        