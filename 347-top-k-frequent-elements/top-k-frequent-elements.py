class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        numbers = {}

        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1
        
        return sorted(numbers.keys(), key = lambda x: (numbers[x], x), reverse = True)[:k]
