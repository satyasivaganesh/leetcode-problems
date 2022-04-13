class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int r=1,d=0,l=0,u=0;
        int num=1;
        vector<vector<int>>ans(n,vector<int>(n,0));
        int i=-1;
        int j=-1;
        while(num<(n*n)+1)
        {
            
            if(r)
            {
            i=i+1;
            j=j+1;
                while(j<n and ans[i][j]==0)
                {
                    ans[i][j]=num;
                    num+=1;
                    j+=1;
                }
                r=0;
                d=1;
            }
            else if(d)
            {
                j=j-1;
                i=i+1;
                while(i<n and ans[i][j]==0)
                {
                    ans[i][j]=num;
                    num+=1;
                    i+=1;    
                }
                d=0;
                l=1;
                    
            }
            else if(l)
            {
                i=i-1;
                j=j-1;
                while(j>-1 and ans[i][j]==0)
                {
                    ans[i][j]=num;
                    num+=1;
                    j-=1;
                }
                l=0;
                u=1;
            }
            else if(u)
            {
                j=j+1;
                i=i-1;
                while(i>-1 and ans[i][j]==0)
                {
                    ans[i][j]=num;
                    num+=1;
                    i-=1;
                }
                u=0;
                r=1;
            }
            
        }
        return ans;
        
    }
};
