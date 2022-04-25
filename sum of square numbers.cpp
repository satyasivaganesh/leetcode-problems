class Solution {
public:
    bool judgeSquareSum(int c) {
        long long int i=0,j=int(pow(c,0.5))+1;
        while(i<=j)
        {
            if((i*i+j*j)==c) return 1;
            else if((i*i+j*j)<c) i++;
            else j--;
        }
        return 0; 
    }
};
