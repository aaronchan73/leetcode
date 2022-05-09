class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        pos = (0,0)
        
        dict = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }
        
        for move in moves:
            pos = (pos[0] + dict[move][0], pos[1] + dict[move][1])
        
        return pos == (0,0)