class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        My initial approach uses binary search to find the index to insert numbers from nums2, moving elements past that index
         right one space if it's inside the sorted array.

        Time: O(n * (m + n)) since it's possible we have to shift all elements from the first element
        Space: O(1)
        """
        leng = m + n # length of nums1
        end = m

        def move_elements_left(from_i: int):
            if from_i >= leng:
                return

            for j in range(end, from_i, -1):
                nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]

        # O(n)
        for num in nums2:
            # O(log m)
            insert_i = bisect.bisect(nums1, num, 0, end)

            if insert_i < end:
                # O(m + n)
                move_elements_left(insert_i)

            end += 1
            nums1[insert_i] = num