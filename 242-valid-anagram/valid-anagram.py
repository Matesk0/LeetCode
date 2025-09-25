class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}

        for letter in s:
            if letter in letters.keys():
                letters[letter] += 1
            
            else:
                letters[letter] = 1
        
        for letter in t:
            check = letters.get(letter, None)

            if check is None:
                return False

            letters[letter] -= 1

            if letters[letter] == 0:
                letters.pop(letter)

        return not letters
        