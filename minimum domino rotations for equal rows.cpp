class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int x=tops[0];
        int y=bottoms[0];
        int t=0;
        int b=0;
        int ref=0;
        for(int i=0;i<tops.size();i++)
        {
            if(tops[i]==x and bottoms[i]!=x)
                b+=1;
            else if(bottoms[i]==x and tops[i]!=x)
                t+=1;
            else if(bottoms[i]==x and tops[i]==x)
                continue;
            else{
                ref=1;
                break;
                }
        }
        if(ref==0)
            return min(t,b);
        t=0;
        b=0;
        ref=0;
        for(int i=0;i<tops.size();i++)
        {
            if(tops[i]==y and bottoms[i]!=y)
                b+=1;
            else if(bottoms[i]==y and tops[i]!=y)
                t+=1;
            else if(tops[i]==y and bottoms[i]==y)
                continue;
            else{
                ref=1;
                break;
                }
            }
        if(ref==0)
            return min(t,b);
        return -1;
        
    }
};
