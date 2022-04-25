class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dict = {
            "--X": -1,
            "X--": -1,
            "++X": 1,
            "X++": 1
        }
        
        ans = 0
        
        for op in operations:
            ans += dict[op]
        
        return ans