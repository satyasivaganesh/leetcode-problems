class Solution {
public:
    string removeDuplicates(string s, int k) {
        stack<pair<char,int>>st;
        for(int i=0;i<s.size();i++)
        {
            if(st.empty())
            {
                st.push(pair(s[i],1));
            }
            else if(st.top().first==s[i])
            {
               st.top().second+=1;
                if(st.top().second==k)
                    st.pop();
            }
            else
            {
                st.push(pair(s[i],1));
            }
        }
        string s1="";
        while(!st.empty())
        {
            for(int i=0;i<st.top().second;i++)
            {
                s1.push_back(st.top().first);
            }
            st.pop();
        }
        reverse(s1.begin(),s1.end());
        return s1; 
        
    }
};
