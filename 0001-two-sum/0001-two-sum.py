class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for idx, num in enumerate(nums):
            need = target - num

            if (need) in seen:
                return [seen[need], idx]
            
            seen[num] = idx
        