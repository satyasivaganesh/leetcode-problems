class MyHashSet {
public:
    map<int,int>m;
    MyHashSet() {
        
    }
    
    void add(int key) {
        m[key]=1;
        
    }
    
    void remove(int key) {
        if(m[key]==1)
            m[key]=0;
        
    }
    
    bool contains(int key) {
        if (m[key]==1) return 1;
        return 0;
        
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
