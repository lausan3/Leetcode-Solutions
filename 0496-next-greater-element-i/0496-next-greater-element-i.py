class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for x in nums1]
        index = []  # index[i] = the index of nums[i]'s position in nums2

        # populate index list
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    index.append(j)
                    break
        
        # find next greatest element in the sublist to the right of the element nums1[i] in nums2
        for i in range(len(index)):
            for j in nums2[index[i]+1:]:
                if j > nums1[i]:
                    ans[i] = j
                    break

        return ans