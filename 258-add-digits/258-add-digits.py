class Solution:
    def addDigits(self, num: int) -> int:
        
        while (num // 10 != 0): 
            temp = num
            sum = 0
            
            while (temp != 0):
                sum += temp % 10
                temp = temp // 10
                
            num = sum
        
        return num