class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n == 1:
            return x
        
        if n == -1:
            return 1/x

        result = self.myPow(x, n//2)
    
        return result * result * (x if n % 2 else 1)