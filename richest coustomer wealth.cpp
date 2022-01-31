class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int s=0;
        for(auto it:accounts)
        {
            int su=0;
            for(auto i:it)
            {
                su+=i;
            }
            if (su>s)
                s=su;
        }
        return s;
        
    }
};
