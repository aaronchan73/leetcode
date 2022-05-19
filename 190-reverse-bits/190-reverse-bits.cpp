class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        
        uint32_t ans = 0;
        
        for (int i = 31; i >= 0; i--) {
            // remove last bit
            // truncate bits
            // bit shift left 31 times
            // set bit to leftside
            
            int lastBit = n % 2;
            n = n >> 1;
            lastBit = lastBit << i;
            ans = ans | lastBit;
        }
        return ans;
    }
};

// 1010
// lastBit = 0
// 0101
// 0000