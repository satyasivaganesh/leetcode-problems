class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int x=1;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]>0)
                if(nums[i]==x)
                    x++;
        }
        return x;
    }
}
