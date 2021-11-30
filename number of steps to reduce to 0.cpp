class Solution {
public:
    int numberOfSteps(int num,int c=0) {
        if(num==0)
            return c;
        else if(num%2==0)
            return numberOfSteps(num/2,c+1);
        else if(num%2!=0)
            return numberOfSteps(num-1,c+1);
    return 0;   
    }
};
