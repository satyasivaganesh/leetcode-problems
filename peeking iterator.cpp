class PeekingIterator : public Iterator {
public:
    vector<int>v;
    int l=0;
    int iter=0;
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    for(auto it:nums)
        {
            v.push_back(it);
            l+=1;
        }
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        return v[iter];
        
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
    
        int n=v[iter];
        iter+=1;
        return n;
            
        
	    
	}
	
	bool hasNext() const {
        if(iter<l)return 1;
        return 0;
        
	    
	}
};
