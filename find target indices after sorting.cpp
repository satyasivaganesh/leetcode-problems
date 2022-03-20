class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int x=-1,y=-1;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==target)
            {
                x=i;
                break;
            }
        }
        for(int i=nums.size()-1;i>-1;i--)
        {
            if(nums[i]==target)
            {
                y=i;
                break;
            }
            
        }
        vector<int>v;
        if(x<0 and y<0)
            return v;
        for(int i=x;i<=y;i++)
            v.push_back(i);
        return v;
            
        
        
    }
};
