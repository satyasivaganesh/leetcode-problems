class Solution {
public:
    bool checkPerfectNumber(int num) {
        vector<int>t;
        if(num==1)
            return 0;
        for(int i=1;i<(int)pow(num,0.5)+1;i++)
            if(num%i==0)
            {
                t.push_back(i);
                if(i!=1)
                    t.push_back(num/i);
            }
        int sum=0;
        for(auto it:t)
            sum+=it;
        if(sum==num)
            return 1;
        return 0;
            
                
        
    }
};
