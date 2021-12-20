class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        vector<vector<int>>v;
        sort(arr.begin(),arr.end());
        v.push_back({arr[0],arr[1]});
        int d,x;
        d=arr[1]-arr[0];
        for(int i=1;i<arr.size()-1;i++)
        {
            x=arr[i+1]-arr[i];
            if(x==d)
                v.push_back({arr[i],arr[i+1]});
            else if(x<d)
            {
                d=x;
                if(v.size())
                {
                    v.clear();
                    v.push_back({arr[i],arr[i+1]});
                }
                else
                    v.push_back({arr[i],arr[i+1]});
                
            }
        }
        return v;
        
    }
};
