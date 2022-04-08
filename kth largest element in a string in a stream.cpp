class KthLargest {
public:
    int k;
    vector<int>v;
   
    
    KthLargest(int k, vector<int>& nums)
    {
        this->k=k;
        v=nums;
        sort(v.begin(),v.end());
        
        
    }
    
    int add(int val) {
        if(v.size()==0)
        {
            v.insert(v.begin(),val);
            return v[0];
        }
        int l=0;
        int m;
        int u=v.size()-1;
        while(l<=u)
        {
            m=(l+u)/2;
            if(v[m]>val)
                u=m-1;
            else
                l=m+1;
                
        }
        if(v[m]==val)
            l=m;
        v.insert(v.begin()+l,val);
        return v[v.size()-k];
        
    }
};
