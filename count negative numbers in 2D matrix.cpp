class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int l=grid.size(),c=0;
        for(int i=0;i<l;i++){
            int x=grid[i].size();
            for(int j=0;j<x;j++){
                if(grid[i][j]<0)c++;
                
            }
        }
        return c;
                
