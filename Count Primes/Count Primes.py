class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        prime = [True] * n
        prime[0] = False
        prime[1] = False

        for i in range(2, ceil(sqrt(n))):
            if prime[i]:
                start = i * i
                for j in range(start, n, i):
                    prime[j] = False

        prime_count = 0

        for i in range(n):
            if prime[i]:
                prime_count += 1

        return prime_count
