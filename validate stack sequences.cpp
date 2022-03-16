class Solution {
public:
    bool validateStackSequences(vector<int>& pu, vector<int>& po) {
        stack<int>t;
        int j=0;
        for(int i=0;i<pu.size();i++)
            if(pu[i]!=po[j])
                t.push(pu[i]);
            else
            {
                j++;
                while(t.size() and t.top()==po[j])
                {
                    t.pop();
                    j++;
                }
            }
        if(j==pu.size())
            return 1;
        return 0;
        
    }
};
