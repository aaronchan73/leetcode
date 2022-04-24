class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            rev = 0
            while rev < x:
                rev = rev * 10 + x % 10
                x = x // 10
            return rev == x or x == rev // 10
                
        