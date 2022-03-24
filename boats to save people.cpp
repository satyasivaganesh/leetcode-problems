class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int i=0;
        int j=people.size()-1;
        int c=0;
        while(i<=j)
        {
            if (i==j)
            {
                c+=1;
                break;
            }
            if((people[i]+people[j])>limit)
            {
                j--;
                c++;
            }
            else if(people[i]+people[j]<=limit)
            {
                i++;
                j--;
                c++;
            }
            
        }
        return c;
        
        
    }
};
