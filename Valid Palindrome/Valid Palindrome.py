class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        sl = s.lower()

        while l <= r:
            while l < len(s) - 1 and not sl[l].isalnum():
                l += 1

            while r >= 0 and not sl[r].isalnum():
                r -= 1

            if sl[l] != sl[r]:
                return False

            l += 1
            r -= 1

        return True