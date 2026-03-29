class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1)
        total_length = len(nums1) + len(nums2)
        half = total_length // 2
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1

            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")

            r1 = nums1[mid1] if mid1 < len(nums1) else float("inf")
            r2 = nums2[mid2] if mid2 < len(nums2) else float("inf")


            if l2 > r1:
                left = mid1 + 1
            elif l1 > r2:
                right = mid1
            else:
                # is valid
                if total_length % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
        
        return -1
                                