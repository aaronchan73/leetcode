class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums) // 2
        ans = []
        
        for i in range(half):
            ans.append(nums[i])
            ans.append(nums[half])
            half += 1
        
        return ans