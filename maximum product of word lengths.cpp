class Solution {
public:
    int maxProduct(vector<string>& words) {
        int p=0;
        for(int i=0;i<words.size();i++)
        {
            map<char,int>m;
            for(int j=0;j<words[i].size();j++) m[words[i][j]]+=1;
            for(int k=i+1;k<words.size();k++)
            {
                int ref=0;
                for(int l=0;l<words[k].size();l++)
                {
                    if (m.find(words[k][l]) !=m.end())
                    {
                        ref=1;
                        break;
                    }
                }
                if(ref==0)
                {
                    int x=words[i].size()*words[k].size();
                    if(x>p) p=x;
                }
            }
        }
        return p;
        
    }
};
