class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = 0
        
        for sentence in sentences:
            currWords = 0
            
            for char in sentence:
                if char == " ":
                    currWords += 1
            currWords += 1
            if currWords > words:
                words = currWords
        
        return words
        