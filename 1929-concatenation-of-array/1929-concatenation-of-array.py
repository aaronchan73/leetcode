class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 2
        
        while (count > 0):
            for num in nums:
                ans.append(num)
            count -= 1
            
        return ans
        