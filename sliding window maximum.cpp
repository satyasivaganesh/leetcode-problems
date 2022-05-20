class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int>v;
        priority_queue<pair<int,int>>q;
        for(int i =0; i<k;i++)
        {
            q.push(pair(nums[i],i));
        }
        v.push_back(q.top().first);
        int x=0;
        for(int i=k;i<nums.size();i++)
        {
            q.push(pair(nums[i],i));
            while(q.top().second<=x)
            {
                q.pop();
            }
            v.push_back(q.top().first);
            x++;
            
        }
        return v;
        
    }
};
