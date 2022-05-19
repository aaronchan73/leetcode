class Solution {
public:
    vector<int> countBits(int n) {
        
        vector<int> ans;
        
        for (int i = 0; i <= n; i++) {
            
            int ones = 0;
            int curr = i;
            
            while (curr >= 1) {
                ones += (curr & 1);
                curr = curr >> 1;
            }
            
            ans.push_back(ones);
            
        }
        
        return ans;
        
    }
};