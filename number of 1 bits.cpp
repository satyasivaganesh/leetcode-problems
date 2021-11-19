class Solution {
public:
    int hammingWeight(uint32_t n) {
        int l=0;
        while(n)
        {
            if((n&1)!=0)
                l++;
            n=n>>1;
        }
        return l;
        
    }
};
