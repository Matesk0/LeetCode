class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = {}

        for word in strs:
            letters = {}

            key = ''.join(sorted(word))

            result[key] = result.get(key, []) + [word]
        
        return result.values()