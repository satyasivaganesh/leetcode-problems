class Solution {
public:
    int bitwiseComplement(int n) {
        int s=0,i=0;
        if(n==0)
            return 1;
        while(n)
        {
            int r=n%2;
            n=n/2;
            if(r==0)
                r=1;
            else
                r=0;
            s+=r*pow(2,i);
            i+=1;
        }
        return s;
        
    }
};
