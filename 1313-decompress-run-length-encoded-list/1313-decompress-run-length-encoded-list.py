class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        ans = []
        i = 0
        
        while (i < len(nums)):
            freq = nums[i]
            val = nums[i+1]
            while (freq != 0):
                ans.append(val)
                freq -= 1
            
            i += 2
            
        return ans