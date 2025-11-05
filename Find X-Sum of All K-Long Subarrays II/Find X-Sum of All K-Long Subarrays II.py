class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Editorial solution. O(n log n) time and O(n) space.
        My attemps are below
        """
        class Helper:
            def __init__(self, x):
                self.x = x
                self.result = 0
                self.large = SortedList()
                self.small = SortedList()
                self.occ = defaultdict(int)

            def insert(self, num):
                if self.occ[num] > 0:
                    self.internal_remove((self.occ[num], num))
                self.occ[num] += 1
                self.internal_insert((self.occ[num], num))

            def remove(self, num):
                self.internal_remove((self.occ[num], num))
                self.occ[num] -= 1
                if self.occ[num] > 0:
                    self.internal_insert((self.occ[num], num))

            def get(self):
                return self.result

            def internal_insert(self, p):
                if len(self.large) < self.x or p > self.large[0]:
                    self.result += p[0] * p[1]
                    self.large.add(p)
                    if len(self.large) > self.x:
                        to_remove = self.large[0]
                        self.result -= to_remove[0] * to_remove[1]
                        self.large.remove(to_remove)
                        self.small.add(to_remove)
                else:
                    self.small.add(p)

            def internal_remove(self, p):
                if p >= self.large[0]:
                    self.result -= p[0] * p[1]
                    self.large.remove(p)
                    if self.small:
                        to_add = self.small[-1]
                        self.result += to_add[0] * to_add[1]
                        self.small.remove(to_add)
                        self.large.add(to_add)
                else:
                    self.small.remove(p)

        helper = Helper(x)
        ans = []

        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i - k])
            if i >= k - 1:
                ans.append(helper.get())

        return ans

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
        # n = len(nums)
        # answer = [0] * (n - k + 1)

        # # O(n log n)
        # def calculate_x_sum(arr: List[int]) -> int:
        #     freq = {}

        #     # O(n)
        #     for num in arr:
        #         freq[num] = freq.get(num, 0) + 1

        #     # O(n log n)
        #     freq_sorted = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
        #     top_x = [x[0] * x[1] for x in freq_sorted[:x]]

        #     # O(n)
        #     return sum(top_x)

        # # O(n)
        # for i in range(len(answer)):
        #     # calculate x-sum
        #     x_sum = calculate_x_sum(nums[i:i + k])

        #     answer[i] = x_sum

        # return answer