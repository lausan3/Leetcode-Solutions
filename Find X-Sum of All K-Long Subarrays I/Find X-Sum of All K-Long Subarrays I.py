class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Brute force solution:
         Do exactly what the description says.
         This yields a solution of O(n^2 log n) time complexity and O(n) space complexity
        """
        n = len(nums)
        answer = [0] * (n - k + 1)

        # O(n log n)
        def calculate_x_sum(arr: List[int]) -> int:
            freq = {}

            # O(n)
            for num in arr:
                freq[num] = freq.get(num, 0) + 1

            # O(n log n)
            freq_sorted = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
            top_x = [x[0] * x[1] for x in freq_sorted[:x]]

            # O(n)
            return sum(top_x)

        # O(n)
        for i in range(len(answer)):
            # calculate x-sum
            # O(n log n)
            x_sum = calculate_x_sum(nums[i:i + k])

            answer[i] = x_sum

        return answer