class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m=matrix.size();
        int n=matrix[0].size();
        int r=1,d=0,l=0,u=0;
        vector<int>ans;
        int i=-1;
        int j=-1;
        int len=0;
        while(len<(m*n))
        {
            
            if(r)
            {
            i=i+1;
            j=j+1;
                while(j<n and matrix[i][j]!='r')
                {
                    ans.push_back(matrix[i][j]);
                    len+=1;
                    matrix[i][j]='r';
                    j+=1;
                }
                r=0;
                d=1;
            }
            else if(d)
            {
                j=j-1;
                i=i+1;
                while(i<m and matrix[i][j]!='r')
                {
                    ans.push_back(matrix[i][j]);
                    len+=1;
                    matrix[i][j]='r';
                    i+=1;    
                }
                d=0;
                l=1;
                    
            }
            else if(l)
            {
                i=i-1;
                j=j-1;
                while(j>-1 and matrix[i][j]!='r')
                {
                    ans.push_back(matrix[i][j]);
                    len+=1;
                    matrix[i][j]='r';
                    j-=1;
                }
                l=0;
                u=1;
            }
            else if(u)
            {
                j=j+1;
                i=i-1;
                while(i>-1 and matrix[i][j]!='r')
                {
                    ans.push_back(matrix[i][j]);
                    len+=1;
                    matrix[i][j]='r';
                    i-=1;
                }
                u=0;
                r=1;
            }
            
            
        
    }return ans;
        
    }
};
