class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        all_letters = {}
        result = []
        index = 0

        for word in strs:
            letters = {}

            for l in word:
                letters[l] = letters.get(l, 0) + 1

            key = tuple(sorted(letters.items()))
            
            check_idx = all_letters.get(key, None)

            if check_idx is None:
                all_letters[key] = index
                result.append([word])
                index += 1
            
            else:
                result[check_idx].append(word)
        
        return result