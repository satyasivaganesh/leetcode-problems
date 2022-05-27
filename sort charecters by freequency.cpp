class Solution {
public:
    string frequencySort(string s) {
        map<char,int>m;
        for(int i=0;i<s.size();i++)
            m[s[i]]+=1;
        priority_queue<pair<int,char>>q;
        for(auto it:m)
            q.push(pair(it.second,it.first));
        string ans;
        while(!q.empty())
        {
            for(int i=0;i<q.top().first;i++)
                ans.push_back(q.top().second);
            q.pop();
        }
        return ans;
    }
};
