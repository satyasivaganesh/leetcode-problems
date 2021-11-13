class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int l=temperatures.size();
        stack<int>st1;
        st1.push(temperatures[l-1]);
        stack<int>st2;
        st2.push(l-1);
        vector<int>ans;
        ans.push_back(0);
        for(int i=2;i<l+1;i++)
        {
            if(temperatures[l-i]<st1.top())
            {
                ans.push_back(st2.top()-l+i);
                st1.push(temperatures[l-i]);
                st2.push(l-i);
            }
            else
            {
                while(temperatures[l-i]>=st1.top())
                {
                    st1.pop();
                    st2.pop();
                    if(st1.empty())
                    {
                        ans.push_back(0);
                        break;
                    }
                    
                }
                if(!st1.empty())
                {
                    ans.push_back(st2.top()-l+i);
                }
                st1.push(temperatures[l-i]);
                st2.push(l-i);
                
            }
                
        }
        reverse(ans.begin(),ans.end());
        return ans;
        
    }
};
