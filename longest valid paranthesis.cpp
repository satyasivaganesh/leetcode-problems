class Solution {
public:
    int longestValidParentheses(string s) {
        int l=s.size();
        stack<int>st;
        vector<int>t(l,0);
        int m=0;
        int su=0;
        for (int i=0;i<l;i++)
        {
            if(s[i]=='(')
                st.push(i);
            else
                if(st.size())
                {
                    t[st.top()]=1;
                    t[i]=1;
                    st.pop();
                }
        }
        for(int j=0;j<l;j++)
        {
            if (t[j])
            {
                su+=t[j];
                if(j==l-1)
                    if(su>m)
                        m=su;
            }
            else
            {
                if(su>m)
                    m=su;
                su=0;
            }
        }
        return m; 
    }
};
