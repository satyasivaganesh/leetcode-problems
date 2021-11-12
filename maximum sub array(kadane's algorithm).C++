// KADANES ALGORITHM


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max=0;
        int ans=INT_MIN;
        for(int i=0;i<nums.size();i++)
        {
            max=max+nums[i];
            if(ans<max)
                ans=max;
            if(max<0)
                max=0;
        }
        return ans;
        
    }
};
