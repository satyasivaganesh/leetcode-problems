class Solution {
public:
    
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>ans;
        for(int i=0;i<pow(2,nums.size());i++)
        {
            vector<int>t;
            int x=i;
            int pos=nums.size()-1;
            while(x)
            {
                int r=x&1;
                x=x>>1;
                if(r)
                    t.push_back(nums[pos]);
                pos--;
            }
            ans.push_back(t);
            
        }
        return ans;
        
    }
};
