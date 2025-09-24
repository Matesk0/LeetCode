class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_idx = m
        nums2_idx = 0

        while nums2_idx < n:
            curr_num = nums2[nums2_idx]
            nums1[nums1_idx] = curr_num

            diff = 0
            while nums1_idx - diff > 0 and nums1[nums1_idx - diff] < nums1[nums1_idx - 1 - diff]:
                nums1[nums1_idx - diff], nums1[nums1_idx - 1 - diff] = nums1[nums1_idx - 1 - diff], nums1[nums1_idx - diff]
                diff += 1

            nums1_idx += 1
            nums2_idx += 1
        return
        