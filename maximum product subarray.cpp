class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int l=nums.size();
        int ma=nums[0];
        int mi=nums[0];
        int ans=nums[0];
        int x,y;
        for(int i=1;i<l;i++)
        {
            x=max(nums[i],max(nums[i]*ma,nums[i]*mi));
            y=min(nums[i],min(nums[i]*ma,nums[i]*mi));
            ma=x;
            mi=y;
            if(ma>ans)
                ans=ma;
        }
        return ans;
        
    }
};
