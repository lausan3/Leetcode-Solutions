class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # idea: this is a O(n^2) time complexity problem where you run through the sorted array once for each value
        # and perform a twosum 2 type two pointer problem
        answer = []
        nums.sort()

        for i in range(len(nums)):
            # continue if we're not at the first value and the current value is the same 
            # as the previous to save computing time
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                sum = nums[i] + nums[L] + nums[R]

                # sum is too big, make sum smaller by reducing R
                if sum > 0:
                    R -= 1
                # sum is too small, make sum bigger by increasing L
                elif sum < 0:
                    L += 1
                else:
                    answer.append([nums[i], nums[L], nums[R]])

                    # updating pointers to add any other variations of the appended list
                    L += 1
                    # skip copies of left pointer number
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        
        return answer