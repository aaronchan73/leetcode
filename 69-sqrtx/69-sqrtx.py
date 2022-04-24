class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        for i in range(x):
            if i * i == x or ((i * i < x) and (x < (i+1)*(i+1))):
                return i