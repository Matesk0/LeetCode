class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr = 0

        if len(nums) == 1:
            return 1

        for idx in range(1, len(nums)):
            if nums[curr] != nums[idx]:
                curr += 1

            nums[curr], nums[idx] = nums[idx], nums[curr]
        
        print(curr)

        return curr + 1

