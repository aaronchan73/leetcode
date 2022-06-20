class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        ans = []
        
        for num in range(left, right + 1):
            
            temp = num
            
            while temp != 0:
                
                digit = temp % 10
                
                if (digit == 0) or (num % digit != 0): break
                    
                temp = temp // 10
                
            if temp == 0: ans.append(num)
                
        return ans