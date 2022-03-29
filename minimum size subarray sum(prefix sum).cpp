class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        for(int i=1;i<nums.size();i++)
            nums[i]+=nums[i-1];
        int s;
        for(int i=0;i<nums.size();i++)
        {
            int x=0;
            s=nums[i];
            if(s>=target)
                return i+1;
            for(int j=i+1;j<nums.size();j++)
            {
                s=(nums[j]-nums[x]);
                if(s>=target)
                    return i+1;
                x+=1;
            }
        }
        return 0;
        
    }
};
