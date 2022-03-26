class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0;
        int u=nums.size()-1,m;
        while(l<=u)
        {
            m=(l+u)/2;
            if(nums[m]==target) return m;
            else if(nums[m]>target)
            {
                u=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        return -1;
    }
};
