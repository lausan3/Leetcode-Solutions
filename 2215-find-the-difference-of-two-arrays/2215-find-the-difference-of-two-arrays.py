class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # answer1_set = ~(nums1 intersection nums2)
        # answer2_set = ~(nums2 intersection nums1)
        answer1_set = set()
        answer2_set = set()
        nums1_set = set()
        nums2_set = set()
        
        # Construct sets of all distinct numbers in nums1 and nums2
        # O(n)
        for num in nums1:
            if num not in nums1_set:
                nums1_set.add(num)

        # O(n)
        for num in nums2:
            if num not in nums2_set:
                nums2_set.add(num)

        # O(n)
        for num in nums1:
            if num not in answer1_set and num not in nums2_set:
                answer1_set.add(num)
        
        # O(n)
        for num in nums2:
            if num not in answer2_set and num not in nums1_set:
                answer2_set.add(num)

        # O(2n)
        return [list(answer1_set), list(answer2_set)]