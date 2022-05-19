class Solution {
public:
    int minBitFlips(int start, int goal) {
        
        int flips = 0;
        
        int flipped = start ^ goal;
        
        while (flipped != 0) {
            flips += (flipped & 1);
            flipped >>= 1;
        }
        
        return flips;
        
    }
};