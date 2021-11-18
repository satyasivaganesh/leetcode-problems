class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int l=nums.size();
        vector<int>t(l+1,0);
        vector<int>x;
        t[0]=1;
        for(int i=0;i<l;i++)
            t[nums[i]]=1;
        for(int j=0;j<l+1;j++)
            if(t[j]==0)
                x.push_back(j);
    return x;
    }
};
