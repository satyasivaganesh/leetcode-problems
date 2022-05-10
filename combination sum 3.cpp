class Solution {
public:
    vector<vector<int>>ans;
    vector<vector<int>> combinationSum3(int k, int n) {
        for(int i=1;i<=pow(2,9);i++)
        {
            vector<int>v;
            int c=0;
            int s=0;
            int x=i;
            int z=1;
            while(x)
            {
                if(x&1==1)
                {
                    c++;
                    s+=z;
                    v.push_back(z);
                    
                }
                x=x>>1;
                z++;
            }
            if(c==k and s==n)
                ans.push_back(v);
        }
        return ans;
        
    }
};
