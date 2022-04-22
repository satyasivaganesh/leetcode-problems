class MyHashMap {
public:
    map<int,int>m;
    MyHashMap() {
        
    }
    
    void put(int key, int value) {
        m[key]=value;
        
    }
    
    int get(int key) {
        if(m.find(key)!=m.end()) return m[key];
        return -1;
        
    }
    
    void remove(int key) {
        m.erase(key);
        
    }
};
