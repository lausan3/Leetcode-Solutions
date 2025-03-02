class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Time: O(i + j) where i is the amt of nums1, and j is the amt of nums2

        # ids -> sum of all ids seen so far
        ids = {}
        res = []

        n1, n2 = len(nums1), len(nums2)
        
        # combine ids
        for id1, val in nums1:
            ids[id1] = ids.get(id1, 0) + val
        
        for id2, val in nums2:
            ids[id2] = ids.get(id2, 0) + val

        i = j = 0

        while i < n1 or j < n2:
            id1 = nums1[i][0] if i < n1 else float("inf")
            id2 = nums2[j][0] if j < n2 else float("inf")

            if id1 < float("inf") and id1 < id2:
                res.append([id1, ids[id1]])
                i += 1
            elif id2 < float("inf") and id1 > id2:
                res.append([id2, ids[id2]])
                j += 1
            else:
                # id1 = id2
                res.append([id1, ids[id1]])

                i += 1
                j += 1

        return res

            