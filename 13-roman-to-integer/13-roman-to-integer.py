class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        ans = 0
        
        for char in range(len(s)):
            if char > 0 and dict[s[char - 1]] < dict[s[char]]:
                ans += dict[s[char]] - 2*dict[s[char - 1]]
            else: 
                ans += dict[s[char]]
        return ans
        