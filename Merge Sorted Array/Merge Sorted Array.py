class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Optimized O(m + n) Solution:

        The optimized approach is very simple. Using a three pointer technique (one read pointer for each array and one write
         for nums1), we can effectively insert the correct values into nums1.

        You can do this intuitively going from least -> greatest, but that requires extra space to avoid overwriting existing
         values in nums1. Therefore, we are going to compare the greatest values.

        Time: O(m + n)
        Space: O(1)
        """
        p1 = m - 1
        p2 = n - 1

        for i in range(m + n - 1, -1, -1):
            if p2 < 0 or (p1 >= 0 and nums1[p1] >= nums2[p2]):
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

        """
        Initial Solution:

        My initial approach uses binary search to find the index to insert numbers from nums2, moving elements past that index
         right one space if it's inside the sorted array.

        Time: O(n * (m + n)) since it's possible we have to shift all elements from the first element
        Space: O(1)
        """
        # leng = m + n # length of nums1
        # end = m

        # def move_elements_left(from_i: int):
        #     if from_i >= leng:
        #         return

        #     for j in range(end, from_i, -1):
        #         nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]

        # # O(n)
        # for num in nums2:
        #     # O(log m)
        #     insert_i = bisect.bisect(nums1, num, 0, end)

        #     if insert_i < end:
        #         # O(m + n)
        #         move_elements_left(insert_i)

        #     end += 1
        #     nums1[insert_i] = num