class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Sliding window solution:
         Calculate the x sum for the first iteration of i, then use it to adjust a heap
         that gives you the top k items to calculate new x-sums.
        Time: O(x log x). Space: O(n - k)

        Theoretically this works but I can't update the items in the heap without it
         being O(n)
        """
        # n = len(nums)
        # answer = [0] * (n - k + 1)

        # # O(k)
        # heap = [(-freq, val) for val, freq in Counter(nums[:k]).items()]
        # # O(k log k)
        # heapq.heapify(heap)

        # def calculate_x_sum(i: int) -> int:
            

        #     x_sum = 0

        #     # reduce doesn't work due to tuple typing in lambdas, so doing it manually
        #     for neg_freq, val in heap[:x]:
        #         x_sum += -neg_freq * val

        #     return x_sum

        # # O(n)
        # for i in range(len(answer)):
        #     # calculate x-sum
        #     x_sum = calculate_x_sum(i)

        #     answer[i] = x_sum

        # return answer

        """
        Brute force solution:
         Do exactly what the description says.
         This yields a solution of O(n log n) time complexity and O(n) space complexity
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
            x_sum = calculate_x_sum(nums[i:i + k])

            answer[i] = x_sum

        return answer