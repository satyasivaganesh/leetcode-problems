class Solution {
public:
    int fnc(int &x,int &y,int &c,int n)
        {
        if(c==n) return y;
        else
            {
            int z=y;
            y=x+z;
            x=z;
            c++;
            return fnc(x,y,c,n);
            }
  
        
        }
    int fib(int n) {
        int x=1;
        int y=1;
        int c=2;
        if(n==0) return 0;
        else if(n==1 or n==2) return 1;
        else return fnc(x,y,c,n);
        
    }
};
