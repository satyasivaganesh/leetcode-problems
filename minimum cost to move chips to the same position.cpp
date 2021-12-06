class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int oc=0;
        int ec=0;
        for(int i=0;i<position.size();i++)
        {
            if(position[i]%2==0)
                ec++;
            else
                oc++;
        }
            
        return min(ec,oc);
    }
};
