class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = [0] * (n - k + 1)

        def calculate_x_sum(arr: List[int]) -> int:
            freq = {}

            for num in arr:
                freq[num] = freq.get(num, 0) + 1

            freq_sorted = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
            top_x = [x[0] * x[1] for x in freq_sorted[:x]]

            return sum(top_x)

        for i in range(len(answer)):
            # calculate x-sum
            x_sum = calculate_x_sum(nums[i:i + k])

            answer[i] = x_sum

        return answer