class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    ans += 1
        
        return ans
        