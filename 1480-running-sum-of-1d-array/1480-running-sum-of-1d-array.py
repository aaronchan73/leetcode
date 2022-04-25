class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            ans.append(sum)
        
        return ans
                
            