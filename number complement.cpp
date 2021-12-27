class Solution {
public:
    int findComplement(int num) {
        int r,s=0,z=0;
        while(num)
        {
            r=num&1;
            num=num>>1;
            if(r)
                r=0;
            else
                r=1;
            s=s+r*pow(2,z);
            z+=1;
            
        }
        return s;
        
    }
};
