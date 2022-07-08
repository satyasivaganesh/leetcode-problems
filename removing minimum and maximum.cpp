class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        vector<int>v;
       int mi=nums[0];
        int ma=nums[0];
        int a=0;
        int b=0;
        for(int i=0;i<nums.size();i++)
        {
            if( nums[i]<mi)
            {
                mi=nums[i];
                a=i;
            }
            if(nums[i]>ma)
            {
                ma=nums[i];
                b=i;
            }
        }
        v.push_back(max(a,b)+1);
        v.push_back(nums.size()-min(a,b));
        v.push_back(a+1+nums.size()-b);
        v.push_back(b+1+nums.size()-a);
        int l=v[0];
        for(int i=1;i<4;i++)
        {
            if(v[i]<l)
                l=v[i];
        }
        return l;
        
        
    }
};
